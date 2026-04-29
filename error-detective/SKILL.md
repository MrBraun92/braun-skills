---
name: error-detective
description: Root-cause analysis for production errors in EventPro — cross-references stack trace, server logs (pino / console), recent git log, the lines of code involved, the TiDB schema, and the recent migration history to pinpoint the actual cause (not the symptom). Different from generic debugging — focuses on "this is happening in production" with limited reproduction. Use when the user pastes a stack trace, a 500 error, a Sentry alert, a production incident, says "production is broken", "what caused this error", or "why did the dashboard 500".
---

# Error Detective (EventPro Production)

Forensic investigation of production errors in EventPro. Differs from generic `debug` skills by focusing specifically on **production** signals — stack trace + logs + git history + schema + migration timeline — to identify the change that broke production, not just the line where the error throws. Built for the EventPro stack (Node + Express + tRPC + Drizzle + mysql2 + TiDB Cloud + AWS S3 + OpenAI).

## When to use this skill
- A 500 error appeared in production after a deploy.
- Sentry / error reporting flagged a spike.
- A specific user reports "I clicked X and got an error" with limited detail.
- A scheduled job (paymentDueNotifier, trashCleaner) failed silently overnight.
- A tRPC mutation returns "Internal Server Error" intermittently.
- TiDB query timed out under load.

## Methodology

### Step 1: Capture the evidence
Ask the user (or ask them to capture) all five evidence types. The skill is only as good as what it gets in:

1. **Stack trace** — full, including file paths and line numbers. NOT a screenshot of a truncated error toast — the full stack from server logs.
2. **Surrounding logs** — pino logs from server, ideally 30s before and after the error. Includes request ID, user ID (if logged), endpoint hit.
3. **Recent commits** — `git log --oneline -20` and `git diff` on the suspect file(s) since the last known-good deploy.
4. **Database state at incident** — was a migration recently applied? What does the affected table look like now (`SHOW CREATE TABLE`)?
5. **Reproduction conditions** — what did the user do? what data was involved (event ID, item ID, amounts)?

If any are missing, ask explicitly. Do not start guessing.

### Step 2: Triage by error category
EventPro production errors usually fall into one of these buckets:

- **Authorization / 403** — `requireWorkspaceAccess`/`requireEventAccess`/`requireWorkspaceRole` rejected the call. Either the guard is correct and a UI bug let the user reach the action, or the guard logic regressed.
- **Validation / 400** — Zod rejected the input. Either the client sends bad data or the schema tightened without UI updating.
- **Database / 500 from Drizzle** — query failed. Common: missing column after migration mismatch, NOT NULL violation, FK constraint, deadlock under load.
- **TiDB-specific** — connection limits, region failover, slow query timeout, optimistic txn conflict (TiDB default).
- **External integration failure** — S3 upload (AWS creds, bucket policy, region), OpenAI rate limit, OAuth provider downtime.
- **Race condition** — two requests modifying the same row; one wins, one fails. Sometimes silent.
- **Timezone bug** — Sprint 6 #6 standardized this; but if the user introduced `toLocaleDateString` on a business date, regressions are possible.
- **Currency aggregation** — Sprint 6 #11 made this honest; misuse of `defaultCurrency` as if it were canonical can produce wrong-sum + wrong-symbol errors.

Classify the error into one of these buckets first.

### Step 3: Trace from the throw site backwards
At the line in the stack trace, ask: what would have to be true for THIS line to throw?

Example: stack trace points to `await db.update(events).set(...).where(...)` throwing `ER_BAD_FIELD_ERROR`. Working backwards:
- The `set(...)` references a column. Which one?
- Does that column exist in the current `drizzle/schema.ts`?
- Does it exist in the actual TiDB table? (`SHOW COLUMNS FROM events`)
- If yes in schema but not in DB: a migration was added to schema.ts but not applied to TiDB. Common when developers run `drizzle-kit push` locally but skip prod.
- If yes in both: the value type doesn't match. Check Drizzle column type.

This is the diagnostic chain. Do not stop at "the line threw" — keep asking why.

### Step 4: Cross-reference with git
- `git log --since="<deploy-time>" --until="<error-first-seen>"` — what changed?
- For each commit in that window, `git show <sha> -- <suspect-file>` to see the diff.
- A commit that touched the throwing function in the relevant window is the prime suspect.
- Migrations in the window: `git log --since=... -- drizzle/` — schema changes shipping with the deploy?

### Step 5: Cross-reference with database
For DB errors specifically:
- `SHOW CREATE TABLE <table>;` — current schema.
- Compare with `drizzle/schema.ts` definition.
- Check `drizzle/meta/_journal.json` last entry vs the latest migration applied (in TiDB, list applied migrations from the meta table or the journal).
- If schema.ts has columns that the DB lacks, OR vice versa, that's the cause.

### Step 6: Reproduce locally if possible
- Note the exact input (event ID, item ID, payload).
- Spin up local with the same Drizzle schema and matching seed data.
- Run the same tRPC call via the dev frontend or a direct `curl`.
- If reproduces locally: deterministic bug, easy fix path.
- If doesn't reproduce: state-dependent (specific data, specific timing, race). Investigate state.

### Step 7: Identify the fix path
Two flavors:

- **Code fix** — the code is wrong. Apply minimal change. Add a regression test if there's a clear input → expected output. Pair with `verification-before-completion`.
- **Data fix** — the code is fine; production data is in an unexpected state. May need a one-off SQL repair (with backup first) or a migration to enforce an invariant going forward.

If the fix is data-only, do NOT also ship a code change in the same commit. Separate concerns.

### Step 8: Write the postmortem
Even for small incidents, a 5-minute postmortem prevents repetition:

```
## Incident: <short title>

### Timeline
- Detected: <time, source>
- Root cause identified: <time>
- Fix deployed: <time>

### Root cause
<one paragraph>

### Why the test suite did not catch it
<honest answer — usually because no test covered this path>

### Fix
- Code: <commit SHA, file>
- Data (if any): <SQL applied, with backup reference>

### Prevention
- New test added: <yes/no, link>
- Guard / invariant added: <yes/no, what>
- Monitoring added: <yes/no, what>
```

## Output format

```
## Error Detective Report — <error title>

### 1. Evidence captured
- Stack trace: <yes / partial / missing>
- Logs window: <range>
- Recent commits: <count>
- DB state: <captured / missing>
- Reproduction: <yes / no>

### 2. Triage classification
Bucket: <auth / validation / DB / TiDB / external / race / timezone / currency / other>

### 3. Trace from throw site
- Line: ...
- Backward chain: ...

### 4. Suspect commit (if found)
- SHA: ...
- Author: ...
- Diff summary: ...

### 5. Database state mismatch (if any)
- schema.ts says: ...
- TiDB has: ...

### 6. Local reproduction
- Result: <reproduces / does not reproduce>
- Conditions: ...

### 7. Root cause
<paragraph>

### 8. Recommended fix
- Type: <code / data / both>
- Plan: ...

### 9. Postmortem (after fix)
<the postmortem template>
```

## Quality checklist
- [ ] All five evidence types were either captured or explicitly noted as missing.
- [ ] Triage bucket is one of the listed kinds, not a vague "something broke".
- [ ] Backward chain from the throw site is articulated, not skipped.
- [ ] Git suspect commit is named (SHA + author) when one exists.
- [ ] Schema-vs-DB mismatch is explicitly checked when the bucket is DB.
- [ ] Local reproduction was attempted; failure to reproduce is itself a finding.
- [ ] Fix path is separated into code-vs-data.
- [ ] A short postmortem accompanies non-trivial incidents.

## Notes for the assistant
- "Try this and see" is a debugging anti-pattern in production. Diagnose first, then fix, then verify. The order matters because production touches real users.
- Do NOT recommend re-deploying as a fix. Re-deploying without identifying root cause papers over the issue and trains the team to ignore signals.
- TiDB-specific: optimistic transactions (default) can throw write conflicts at commit time, not at the offending statement. Stack trace points to the commit, but the bug is upstream. Look at the full transaction.
- If the error is in a scheduled job (`server/jobs/`), there's no user reproduction — capture the job's last-run logs and recent input changes (e.g., `paymentDueNotifier` runs daily; what payments hit the threshold today?).
- AWS S3 errors: distinguish `AccessDenied` (creds / bucket policy) from `NoSuchKey` (file genuinely missing) from `NetworkingError` (transient). They have different fixes.
- OpenAI errors: rate limits are 429 (retry with backoff), invalid request is 400 (input shape), auth is 401 (key issue). Don't retry-on-error blindly.
- Per user memory `eventpro_oauth_hardening`, OAuth-related code in `const.ts`, `oauth.ts`, `LandingPage.tsx` was hardened. If the error is OAuth-flavored, check whether a recent commit re-touched those files in a way that undid the hardening.
- Pair with `verification-before-completion` for the post-fix gate, with `database-optimizer` if root cause is query plan, with `react-expert` if the error is on the frontend stack trace.
- Be honest in postmortems. "The test suite did not cover this path" is a real finding. "It was a freak occurrence" is rarely true.
