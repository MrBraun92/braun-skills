---
name: repomix-safe-mixer
description: Packages a repository (or a subset) into a single bundle file suitable for sending to Claude / Manus / GPT — with secret detection and masking applied to prevent leaking .env, AWS keys, OAuth tokens, JWT secrets, OpenAI keys, S3 URLs with credentials, hardcoded passwords. Output is a sanitized bundle.txt plus a separate report listing what was masked. Use when the user says "bundle the repo for Claude", "repomix", "package this for ChatGPT", "share repo safely", "mix the repo", or any time a code dump is about to leave the local machine. Tuned for the EventPro stack but applies to any repo.
---

# Repomix — Safe Mixer

Bundles a repo (full or subset) into one text file an LLM can ingest, while detecting and masking secrets before the bundle leaves the local machine. Built around the realistic threat: copy-pasting code into ChatGPT or Claude can exfiltrate `.env` values, AWS keys, OAuth secrets, OpenAI keys — even if the user thought they only sent "the source code". This skill is the gate before that happens. Tuned for EventPro (`.env`, AWS S3, OpenAI, TiDB connection strings, OAuth tokens stored in `eventpro_oauth_hardening` per user memory) but the masking patterns are generic.

## When to use this skill
- User wants to send code to Claude / Manus / GPT for review or feature work.
- A bug report needs to include reproduction code from the repo.
- The user says "let me paste the whole project" — block first, sanitize, then bundle.
- Onboarding a new agent (a fresh Manus run, a new Claude conversation) and want the right slice of context.
- Auditing what the codebase actually leaks via filenames (`.env`, `*.pem`) before any sharing.

## Methodology

### Step 1: Confirm scope
Ask:
- Full repo or subset (single feature area)?
- Include lockfiles? (Usually NO — they're noise.)
- Include tests? (Often YES — they document behavior.)
- Include `node_modules` / `dist` / `.next`? (NEVER.)
- Target consumer? (Claude has 200k token context as of 2026; GPT-4 Turbo similar; size accordingly.)
- Already in a git repo? (If yes, can use `git ls-files` to list tracked files only — automatic ignore of `.gitignore` patterns.)

### Step 2: Build the file list
Default include patterns:
- `*.ts`, `*.tsx`, `*.js`, `*.jsx`
- `*.sql`, `*.json` (exclude lockfiles)
- `*.md` documentation (CLAUDE.md, README, docs/)
- `package.json`, `tsconfig.json`, `vite.config.ts`, `drizzle.config.ts`
- `.env.example` (templates without secrets)

Default exclude patterns (always):
- `.env`, `.env.local`, `.env.*.local`, `.env.production`
- `node_modules/`, `dist/`, `build/`, `.next/`, `.cache/`
- `*.pem`, `*.key`, `*.p12`, `*.pfx`, `id_rsa*`, `id_ed25519*`
- `pnpm-lock.yaml`, `package-lock.json`, `yarn.lock`
- `.git/` directory contents
- Coverage reports, `.nyc_output`, `coverage/`
- Database files (`*.sqlite`, `*.db`)
- Backup files (`*.bak`, `*~`)

For a git repo: prefer `git ls-files` to honor `.gitignore` automatically, then apply the excludes above as a second filter.

### Step 3: Per-file secret scan
For each file's content, run the secret detection pass. Patterns to match (in order — match means scrub):

- **Generic env-like assignments**: lines like `KEY=value`, `KEY:value`, `KEY = "value"` where KEY contains `SECRET|TOKEN|KEY|PASSWORD|PASS|API|AUTH|PRIVATE|CREDENTIAL|DSN|CONN`.
- **AWS access key**: regex `AKIA[0-9A-Z]{16}` and `ASIA[0-9A-Z]{16}` (session tokens). Matching value AND any nearby line with `secret_access_key` value.
- **AWS secret access key**: 40-char base64-like immediately after `aws_secret_access_key` or in proximity.
- **OpenAI API key**: `sk-[A-Za-z0-9]{20,}` and `sk-proj-[A-Za-z0-9_-]{20,}`.
- **Anthropic API key**: `sk-ant-[A-Za-z0-9-]{20,}`.
- **GitHub PAT**: `ghp_[A-Za-z0-9]{36}`, `gho_`, `ghu_`, `ghs_`, `ghr_`.
- **Slack tokens**: `xox[baprs]-[A-Za-z0-9-]+`.
- **Google API**: `AIza[0-9A-Za-z_-]{35}`.
- **JWT**: `eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+` (heuristic — header.payload.signature).
- **Connection strings with credentials**: `mysql://user:pass@`, `postgres://user:pass@`, `redis://:pass@`. **TiDB**: `mysql://USER.PROJECT:PASSWORD@gateway01...`.
- **S3 presigned URLs**: contain `X-Amz-Signature=`.
- **OAuth client secrets**: lines containing `client_secret`, `CLIENT_SECRET=`.
- **Private SSH keys**: file content starts with `-----BEGIN .* PRIVATE KEY-----`.
- **Hardcoded password literals**: `password = "..."`, `password: "..."` in source code. Heuristic, may have false positives — flag for human review rather than auto-mask.
- **Bearer tokens in code**: `Authorization: Bearer eyJ...` patterns.

For each match: replace the secret value with `<REDACTED:KIND>` (e.g., `<REDACTED:OPENAI_API_KEY>`), preserving line structure. NEVER include the original value in the bundle.

### Step 4: Per-file context check
Some files are inherently risky and need extra attention:

- `**/oauth*.ts`, `**/auth*.ts` — auth flows. Verify no hardcoded test tokens.
- `server/routers/*.ts` — endpoints. Verify no inline DB credentials.
- `*.test.*` — tests sometimes have fixture credentials. Mask them too — fixture or not, they look like secrets.
- `drizzle.config.ts` — DB connection string. If using `process.env.DATABASE_URL`, fine. If hardcoded, mask.
- `vite.config.ts` — env exposure config. Verify no `define` with secret values.
- `client/src/**/*` — client code is shipped to browser; any secret here is already public, but flag for the user to rotate.

### Step 5: Build the bundle
Format:

```
========================================
REPOMIX BUNDLE
Generated: <timestamp>
Source: <repo path or git remote>
File count: N
Total size: M chars
Secret masks applied: K
========================================

## DIRECTORY STRUCTURE
<tree of included files>

## FILES

### <relative/path/file1.ts>
```
<file content>
```

### <relative/path/file2.tsx>
```
<file content>
```

...

========================================
END OF BUNDLE
========================================
```

Output one `bundle.txt` (or `.md` for nicer code-fence handling).

### Step 6: Build the audit report
Separate file: `bundle-audit.txt`. NOT pasted to the LLM. For the user's local review:

```
## Repomix Audit
Bundle: bundle.txt
Files included: N
Files excluded: M (list with reasons)

## Secrets masked
| File | Line | Kind | Original (first 8 chars) | Replacement |
|---|---|---|---|---|

## Files flagged for human review (possible false positives)
- path:line — pattern matched, may not be a real secret

## Files NOT scanned (binary / encoded)
- path — kind
```

### Step 7: Final size and rotation advice
- Token estimate (rough: 4 chars ≈ 1 token).
- If bundle exceeds target context (e.g., >150k tokens for a 200k context), suggest subset strategies: by directory, by feature area, by recent git diff.
- If real secrets were masked: ROTATE THEM. Masking the bundle does not undo a leak that already happened locally if the file was committed to git history. Run `git log --all -S "<first 8 chars of secret>"` to confirm.

### Step 8: Suggest .gitignore additions if missing
If `.env` was found in the file list (it should not be — should have been excluded), check `.gitignore`. If `.env` is not gitignored, this is a critical finding — surface immediately and recommend the user audit git history.

## Output format

Two files plus a summary message:

1. **`bundle.txt`** (or `bundle.md`) — the sanitized package, ready to paste.
2. **`bundle-audit.txt`** — local-only audit log.
3. **Inline summary** — files included, files excluded, secrets masked count, size estimate.

```
## Repomix Bundle Ready

Bundle file: bundle.txt
Audit file: bundle-audit.txt (LOCAL ONLY — do not share)

Stats:
- Files included: N
- Files excluded: M
- Secrets masked: K (kinds: OPENAI_API_KEY × 1, JWT × 2, DB_CONN × 1)
- Size: ~Z chars (~T tokens)
- Fits in <model> context: Yes / No

Critical findings (if any):
- .env was found in the file list and excluded; verify it's in .gitignore
- Hardcoded password in <file>:<line> — masked, recommend rotation
```

## Quality checklist
- [ ] No `.env` content appears in `bundle.txt` (search the bundle to verify).
- [ ] Every match in the secret scan has a `<REDACTED:KIND>` replacement; no original values leak.
- [ ] `bundle-audit.txt` lists every mask with original first-8-chars (so user can identify) but never the full secret.
- [ ] Excluded directories (`node_modules`, `dist`, etc.) are not in the bundle.
- [ ] Lockfiles excluded by default.
- [ ] Token estimate matches the target consumer's window.
- [ ] User is reminded to rotate any leaked secrets.
- [ ] If `.env` is not in `.gitignore`, this is flagged.

## Notes for the assistant
- Default to **paranoid masking**. False positives (a constant named `API_KEY_LENGTH` matched as a secret) are recoverable; false negatives (a real key shipped to GPT) are not.
- The bundle goes outside the user's machine. Treat every byte that crosses that boundary as something a third party will see.
- Once a secret has been pasted into ChatGPT / Claude / Manus, assume it is compromised. Provider data-handling policies vary; some retain prompts. Rotation is the only safe response.
- For EventPro specifically: per user memory `eventpro_oauth_hardening`, OAuth changes were made to `const.ts`, `oauth.ts`, `LandingPage.tsx`. These files are CODE, not secrets — bundling them is fine. But verify the bundled versions match what's on `main` to avoid showing a stale state.
- TiDB connection strings are particularly sensitive: TiDB Serverless URLs leak the project name + cluster region in the host. Mask the password but consider whether to mask the full host as well if the user is sharing publicly.
- For private files like `id_rsa`, just exclude — never include even masked. Their existence in the bundle alone signals something is wrong with the file selection.
- This skill is preventive. If the user reports they ALREADY pasted secrets to an LLM: rotate now, audit git history, do not assume the leak is contained.
- Pair with `verification-before-completion` (the bundle is correct before it leaves the machine) and `error-detective` (if a leak already happened, trace impact).
