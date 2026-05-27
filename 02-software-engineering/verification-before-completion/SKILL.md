---
name: verification-before-completion
description: Operational gate that prevents an agent (or the user) from declaring a task "done" before producing concrete evidence — build OK, tests passing, lint clean, screenshots if UI, no console errors, regressions verified. Replaces "I think it works" with a checklist of evidence. Use when an agent is about to claim completion, when the user says "is this really done?", "verify before commit", "check before declaring complete", or as a pre-PR / pre-deploy gate. Built primarily for the EventPro stack (React 19 + Vite + tRPC + Drizzle + pnpm + Vitest) but the gate is stack-agnostic.
---

# Verification Before Completion

A discipline gate. The single most common failure mode of AI-assisted coding is the agent declaring "done" based on optimism rather than evidence. This skill blocks that pattern: completion requires *artifacts* — passing build, passing tests, screenshots of changed UI, clean lint, no console errors, no regressions in the area touched. Built for EventPro (`pnpm tsc --noEmit` and `pnpm test` are the canonical gates per CLAUDE.md §15) but the principle generalizes.

## When to use this skill
- An agent is about to write "Done" / "Complete" / "Ready to merge" / "Pronto".
- The user is about to commit + push.
- A PR is about to be opened against the EventPro main branch.
- A bug fix is "applied" but not verified.
- The end of any agent session that touched code.
- After Manus or Claude or another agent runs ahead and declares success — verify before trusting.

## Methodology

### Step 1: Identify what changed
List explicitly:
- Files modified (with line counts).
- Areas of the app touched (Dashboard, BudgetTable, payment flow, etc.).
- Database migrations added (if any).
- Public API / tRPC contract changes (if any).
- Dependencies added or removed.

This list scopes the verification effort. A 3-line typo fix needs less verification than a refactor of `BudgetTable.tsx`.

### Step 2: Run the canonical gates
For EventPro, the canonical gates per CLAUDE.md §15:
- `pnpm tsc --noEmit` — must return 0 errors.
- `pnpm test` — must return 260/260 passing (or current expected count post-Sprint 7).
- `pnpm build` — must complete without errors.
- `pnpm lint` — if configured, must pass.

For non-EventPro projects: identify the equivalent commands and run them. Capture the exit code and last 20 lines of output as evidence.

If any gate fails: STOP. The task is not done. Surface the failure with full output to the user. Do not skip and do not claim partial completion.

### Step 3: Manual verification per change type

**Backend / tRPC change:**
- Endpoint hit at least once via `pnpm dev` + browser network tab OR via direct request.
- Response shape matches the expected output.
- Authorization guard is present (`requireWorkspaceAccess`, `requireEventAccess`, `requireEventEditAccess`, or `requireWorkspaceRole` per CLAUDE.md §6).
- Soft-delete filter present (`isNull(events.deletedAt)`) where applicable.
- Dashboard invalidation called from frontend mutations that affect financials (per CLAUDE.md §7).

**Frontend / UI change:**
- Browser screenshot of the changed component, light AND dark mode (EventPro supports both).
- Mobile viewport (375px) screenshot if the component is responsive.
- Console: no warnings, no errors. React 19 warnings about hydration, key props, or effects are real bugs.
- Network tab: no failing tRPC requests, no 401/403/500.
- If the change involves date/timezone: verify in `America/Sao_Paulo` AND a non-BR timezone (EventPro Sprint 6 #6 fixed TZ bugs; do not regress).

**Database migration:**
- Migration file matches Drizzle schema in `drizzle/schema.ts`.
- `_journal.json` updated with the new entry.
- Migration is idempotent (re-running is safe).
- Index migrations include `ALGORITHM=INPLACE, LOCK=NONE` for TiDB if applicable.
- Tested locally before applying to TiDB Cloud.

**Dependency change:**
- `pnpm install` runs cleanly.
- Bundle size impact checked (per CLAUDE.md item 17 about framer-motion / i18next discussions).
- License compatible with the project.
- No transitive vulnerabilities flagged by `pnpm audit`.

### Step 4: Regression check on the touched area
- Adjacent functionality still works. (Touched BudgetTable? Verify Payments tab and Dashboard KPIs still render.)
- Sprint 5 financial canon intact: `shared/financial.ts` not modified unless explicitly in scope.
- Sprint 6 group invariants intact: σ helper(event) === helper(group union) per CLAUDE.md §13 holding.
- Sprint 7 collaboration invariants intact: pending invites do not consume seats, owner-only buttons are owner-only, requireEventAccess does NOT bypass admin restrictions added.
- No new `console.log` debug statements (per CLAUDE.md §16).

### Step 5: Evidence artifact bundle
Produce a single deliverable that contains:
- Output of each gate command (last 20 lines + exit code).
- Screenshots (if UI changed) named `before-<area>.png`, `after-<area>.png`.
- Network log excerpt (if backend changed).
- Brief test plan: what the user should manually click to confirm.
- Anything that's NOT verified — surface honestly.

### Step 6: Issue the verdict
One of:
- **GO** — all gates passed, manual checks done, evidence attached. Safe to commit / merge / deploy.
- **GO with notes** — passed, but here are 1-3 known limitations the user should be aware of (e.g., "tested in Chrome only, Safari not verified").
- **NO-GO** — gate failed or evidence missing. Concrete actions to fix: ...

NEVER issue a vague "looks good" verdict. The whole point of this skill is concrete evidence vs vibes.

### Step 7: Document the verification
For meaningful changes (anything beyond a typo), append a short verification log to the commit message or PR description:

```
Verification:
- pnpm tsc --noEmit: 0 errors
- pnpm test: 260/260 passing
- Manual: Dashboard renders KPIs correctly; budget reorder DnD works in infraestrutura tab.
- Screenshots attached.
```

This makes the next reviewer's job easier and creates an audit trail.

## Output format

```
## Verification Report — <task name>

### Scope
- Files changed: <list>
- Areas touched: <list>
- Migrations: <list>
- Dependencies: <list>

### Canonical gates
| Gate | Result | Output (last lines) |
|---|---|---|
| pnpm tsc --noEmit | PASS / FAIL | ... |
| pnpm test | 260/260 PASS / X FAIL | ... |
| pnpm build | PASS / FAIL | ... |
| pnpm lint | PASS / FAIL / N/A | ... |

### Manual verification
- [ ] Backend endpoint hit, response shape verified
- [ ] Authorization guard present
- [ ] Frontend screenshots: light + dark + mobile
- [ ] Console clean
- [ ] Network: no failing requests
- [ ] Timezone tested in BR + non-BR (if relevant)
- [ ] Migration idempotent (if relevant)

### Regression check
- [ ] Sprint 5 financial canon intact
- [ ] Sprint 6 group invariants intact
- [ ] Sprint 7 collaboration invariants intact
- [ ] No new console.log statements

### Evidence
- Screenshots: <paths>
- Logs: <paths>

### Verdict
<GO / GO with notes / NO-GO>

### Notes for the user
<anything they should know>
```

## Quality checklist
- [ ] No verdict issued without all gates run.
- [ ] Failed gates produce NO-GO, never GO-with-notes.
- [ ] Screenshots are real, not described in prose.
- [ ] Manual checks are itemized, not waved at.
- [ ] Regression areas are specifically named (not "everything else still works").
- [ ] The verdict is one of three explicit values.

## Notes for the assistant
- This is a **gate**, not a checklist to optionally complete. If the gate fails, the task is not done — full stop. Do not soften the verdict to spare feelings.
- The user (Oliver) explicitly works in a parallel-agent setup (Claude + Manus + GPT). Other agents may run ahead and declare success. This skill is the brake.
- For EventPro: the test count moves with sprints. CLAUDE.md says 260/260 post-Sprint 7. If the count is different, reconcile (someone added/removed tests) BEFORE issuing GO.
- For UI changes: a verbal description of what the user should see is NOT a screenshot. If you cannot capture a screenshot, explicitly say "screenshot pending — user should manually verify component renders" and downgrade to NO-GO or GO-with-notes.
- "I'm confident this works" without evidence is exactly what this skill exists to block.
- For database migrations on TiDB Cloud: extra caution — TiDB has different DDL semantics than vanilla MySQL. Verify the migration ran successfully via the TiDB console before claiming GO.
- Pair with `error-detective` if a gate failed and root-cause is unclear. Pair with `test-automator-playwright` if regression coverage is missing.
- Do not run `git push --force`, `pnpm install --force`, or any other destructive command as part of verification.
- If the user asks "is it done?", the answer is not "yes" — the answer is "let's verify", followed by the gate output.
