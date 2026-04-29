---
name: continue-work
description: Recovers context between sessions across Claude / Manus / GPT — reads the latest commits, CLAUDE.md, MEMORY.md, the current git status / branch / unstaged changes, and produces a "where we left off" briefing structured for the user's parallel-agent workflow. Critical for the situation where Oliver edits locally, pushes to GitHub, has Manus run, and then opens a new Claude session needing to know what changed in between. Use when the user says "continue", "where were we", "catch me up", "context", "resume", "onde paramos", or starts a fresh session on an existing project.
---

# Continue Work

Bridges the gap between agent sessions in a parallel-agent workflow. The user (Oliver) works with Claude + Manus + GPT in parallel; sessions end, work happens elsewhere, and the next session needs to know **what changed since I was last here**. This skill reads the live state of the repo, the project memory, the last few commits, and any open changes — and produces a briefing structured for action, not summary. Built primarily for EventPro (`MrBraun92/eventpro`, branch `main`) but generalizes to any code project with git + CLAUDE.md.

## When to use this skill
- A new conversation opens on an existing project — orient before any code change.
- The user explicitly says "continue", "where were we", "onde paramos", "catch me up".
- Manus or another agent finished a run; the user wants to see what landed.
- A long break (days / weeks) — codebase state may have drifted from the user's mental model.
- Switching contexts between EventPro and the thesis (or another project) and needing fast re-load.
- Before delegating to another agent — produces a briefing that goes as the initial prompt.

## Methodology

### Step 1: Identify the project
Ask (or infer from cwd / context) which project the user is resuming on:
- **EventPro** — SaaS, repo `MrBraun92/eventpro`, branch `main`. Memory in `CLAUDE.md` + `MEMORY.md` index + linked memory files (`project_eventpro.md`, `eventpro_oauth_hardening.md`, `feedback_workflow.md`).
- **Thesis** — UiS Management master's, English, APA 7. State lives in working dir / cloud doc / Drive folder.
- **Trading research / other** — state lives in user notes.

This skill works best for code projects with git. For document projects (thesis), pivot to reading the latest doc version + the supervisor's last feedback.

### Step 2: Pull the live git state
Capture (or have the user run):
- `git status` — staged + unstaged changes, untracked files.
- `git log --oneline -20` — last 20 commits on current branch.
- `git log --since="2 weeks ago" --pretty=format:"%h %ad %an %s" --date=short` — wider window after a long break.
- `git branch -vv` — current branch + tracking status (ahead / behind).
- `git diff` — unstaged diff (work in progress).
- `git diff --staged` — staged but uncommitted.
- `git stash list` — anything stashed.
- `gh pr list` — open PRs awaiting review or merge.

This is the ground truth of "where the code is". Do not skip in favor of memory.

### Step 3: Read the project memory
For EventPro:
- `CLAUDE.md` at repo root (or `/Users/mrbraun_mac/Documents/Codex_Dev/CLAUDE.md`) — project context. Pay special attention to the bottom section listing latest sprint and Item 17 ("para Oliver validar").
- User memory index `MEMORY.md` and the linked files.
- `docs/sprint-N/FECHAMENTO_SPRINT_N.md` for the most recent closed sprint.
- `TODO.md`, `BACKLOG.md`, `ROADMAP.md` if they exist.

The memory tells you what the user was working on and what was decided. Git tells you what landed.

### Step 4: Cross-reference memory and git
Important checks:

- **Sprint status**: CLAUDE.md says "Sprint 7 fechada"; git log should show the merge commits matching. Do they?
- **Open candidates**: memory may list "Sprint 8 candidates" — verify none silently landed (would be drift).
- **Hardening preserved**: per memory `eventpro_oauth_hardening`, commit `967310b` must be preserved. Search `git log --all` for that SHA; verify still present, no revert above it.
- **Cross-agent commits**: per memory `feedback_workflow`, user pushes → Manus runs. Look at recent commit authors. Were any from a Manus / bot account? What did they ship?
- **WIP**: are there unstaged changes? If yes, something was in flight.

Surface drift between memory and git as critical findings — this is the single most valuable thing this skill does.

### Step 5: Identify the last meaningful work boundary
- If on a clean main with no WIP and the last commit is days old: the user is starting something new. Focus the briefing on "what's the current goal?".
- If WIP exists: name what was being worked on. Read the diff and infer.
- If a recent commit landed: summarize it from the commit message + diff.
- If multiple commits in the last few days: identify the theme (feature shipped? bug fix? refactor?).

### Step 6: Surface staleness signals
Common staleness in a parallel-agent workflow:
- Memory says X was last sprint, but git shows newer commits → memory is stale.
- A test count is mentioned (260/260 post-Sprint 7); current `pnpm test` may show a different number → flag for verification before relying on the count.
- A "candidate for next sprint" item — was it touched? Started? Closed?
- Unmerged branches with recent activity → potentially abandoned work.
- TODO / FIXME comments added recently → in-progress signals.

### Step 7: Produce the briefing
Structured for fast read AND fast action. The user has limited cognitive budget; give the answer in the first 200 words and details below.

### Step 8: Suggest ONE concrete next step
Do not output a list of 5 maybe-tasks. Produce one named action, formatted: `<verb> + <object> + <one-sentence why>`. Examples:
- "Run `pnpm test` to confirm the recent Manus commit didn't regress the 260 Sprint 7 tests before opening any new branch."
- "Read `server/routers/budget.ts:142-180` — that's where the unstaged diff lives."

If everything is clean and there's no obvious next step, say so honestly — suggest opening a new initiative or taking a break.

## Output format

```
# Continue Work — <project> — <date>

## TL;DR (read this first)
- Repo / branch: <name> (<ahead/behind>)
- Last commit: <SHA short, date, message>
- WIP: <yes / no — if yes, what>
- Memory vs git: <consistent / drift detected — see below>
- Suggested next move: <ONE concrete action>

## Code state
- Last commit: `<sha>` — <message> (<date>, <author>)
- Uncommitted changes: <list>
- Tests: <last known state — passing / failing / unknown>
- TypeScript: <0 errors / X errors / unknown>

## Recent commit history (last <N>)
| SHA | Date | Author | Subject |
|---|---|---|---|

## Work in progress
1. <item 1 — exactly where it stopped>
2. <item 2 — exactly where it stopped>

## Memory / git drift detected (if any)
- ...

## Hardening / invariant checks (EventPro)
- OAuth hardening commit `967310b` preserved: <yes / no — if no, EMERGENCY>
- Sprint 5 `shared/financial.ts` untouched: <yes / no>
- Sprint 6 `shared/sponsors.ts` enum intact: <yes / no>
- Sprint 7 `shared/permissions.ts` and `shared/plans.ts` intact: <yes / no>

## Blockers / pending decisions
- <blocker 1 — who unblocks>
- <blocker 2>

## Recommended next step
**<verb + object>** — <one-sentence why>.

## Files to read first if you continue
- <path>: <why>
- <path>: <why>
```

## Quality checklist
- [ ] Project is identified by name, not assumed.
- [ ] Live git state was actually captured (not described from memory).
- [ ] Recent commits are summarized — both subject AND substance.
- [ ] Memory drift is surfaced if present.
- [ ] EventPro hardening invariants are explicitly checked when the project is EventPro.
- [ ] WIP is named, not hidden.
- [ ] TL;DR fits in <200 words.
- [ ] Suggested next step is a single concrete action, not a menu.
- [ ] If nothing is pending, that is stated honestly.

## Notes for the assistant
- The user works in parallel with multiple agents. Don't assume the previous Claude session is the source of truth — Manus or GPT may have made changes you don't know about. **Git is the source of truth.**
- Per user memory `feedback_workflow`: the user edits LOCALLY → pushes to GitHub → Manus runs. Do not run anything locally during a continue-work briefing — read only. The user runs the commands; this skill consumes the output.
- Per user memory `eventpro_oauth_hardening`: commit `967310b` must be preserved. ALWAYS verify this on a continue-work for EventPro. If it's been reverted, that is a critical finding — surface immediately, do not bury under "minor notes".
- CLAUDE.md is updated at the end of each significant sprint. If a new sprint landed but CLAUDE.md isn't updated, that's a drift signal worth surfacing.
- Memory files persist across conversations; CLAUDE.md is project-checked-in. They can drift from each other; surface that.
- For thesis projects: the equivalent of "git log" is reading the writing notes, the most recent doc version, and any feedback the supervisor sent. The principles transfer.
- Be honest if context is missing. If the user opens a session with no specific project named and no obvious cwd hint: ask, don't guess.
- Match the user's input language. CLAUDE.md is in PT-BR, MEMORY.md is mixed. Default to PT-BR if user wrote PT-BR; English if they wrote English.
- **Do not modify any state during a continue-work briefing — read only.** The user's first action after reading the briefing might be to revert something they didn't expect; don't preempt by editing.
- Tone: direct, executive, plain. The user reads this when tired — clarity beats completeness.
- Pair with `verification-before-completion` if the user wants to verify the current state passes gates before continuing.
