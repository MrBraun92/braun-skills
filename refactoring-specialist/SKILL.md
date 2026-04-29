---
name: refactoring-specialist
description: Performs safe, incremental refactors of large components and modules in the EventPro stack — extract component, extract hook, lift state, split file, rename — with tests intact at every step. Specifically tuned to the EventPro giants: BudgetTable.tsx (1093 lines), Dashboard.tsx (~987 lines), EventPage.tsx (864 lines). Each step is independently committable and verifiable. Use when the user says "this file is too big", "split this component", "extract a hook", "refactor BudgetTable", "this is unmaintainable", or "make this testable".
---

# Refactoring Specialist (EventPro)

Splits, extracts, and renames in steps so small that each step is independently verifiable. The goal is the test suite passes after every step, type-checks pass after every step, and the user can stop at any step without leaving the codebase in a broken middle state. Built for the EventPro stack and the three giant components — BudgetTable, Dashboard, EventPage — but the pattern generalizes.

## When to use this skill
- A component is over ~600 lines and changes there are slow / risky.
- A repeated pattern across files should become a custom hook.
- State that's grown in one place should be lifted, split, or extracted into a reducer / context.
- A file mixes unrelated concerns (rendering + data fetching + business logic) and the user wants separation.
- A bug fix surfaces design debt that's blocking the fix.

## Methodology

### Step 1: Confirm the scope and the success criterion
Ask:
- Which file(s)?
- What's the user's pain — slowness, confusion, untestability, merge conflicts?
- What does "done" look like? Smaller files? A specific extracted hook? A clear separation between data and presentation?
- Are tests in place for this area? If `pnpm test` doesn't cover it, the refactor needs tests written FIRST.

Without a success criterion, refactors balloon. Lock it in writing before touching code.

### Step 2: Read the entire file
Per CLAUDE.md §16, the giants must be read in full first. List every:
- Top-level export and its consumers.
- Internal hook usage (useState, useEffect, useMemo, useCallback, custom hooks).
- Context consumed.
- Sub-components defined inline.
- Functions defined outside the component body.
- tRPC queries and mutations.
- Side effects.

This inventory is the map. Without it, "extract" recommendations are guesses.

### Step 3: Choose the smallest first move
Order refactors by least-risk-first:

1. **Extract pure helper functions to a sibling file** (or to `client/src/lib/utils.ts` if generic). No behavior change, no React. Easy win, easy verify.
2. **Extract sub-components defined inline** to their own files. Move JSX + props interface; state stays with parent for now.
3. **Extract a custom hook** for stateful logic shared between components or with a clear boundary inside one component.
4. **Lift / split state** — separate independent state slices that don't need to trigger each other's renders.
5. **Introduce a reducer** if state transitions are getting complex (BudgetTable cell-edit + DnD + selection + comments).
6. **Split file by concern** — render vs data fetch vs business logic.
7. **Reorganize folder structure** — last, only if multiple files now need a shared home.

Each step is a separate commit. Each commit must pass `pnpm tsc --noEmit` and `pnpm test`.

### Step 4: For each step, write the plan before the diff
Per step:
- What's being extracted / moved / renamed.
- Where it goes.
- What imports change.
- Which tests are expected to keep passing (and why).
- Estimated diff size.

If the diff is bigger than ~200 lines net, the step is too big — split further.

### Step 5: Apply, run gates, commit
Per step in order:
1. Make the change.
2. Run `pnpm tsc --noEmit` — must be 0 errors.
3. Run `pnpm test` — must remain at expected count (260+ post-Sprint 7).
4. Smoke-test in browser: the page that uses the refactored code still works.
5. Commit with label like `refactor: extract <thing> from <File>` (per CLAUDE.md §15 commit format, but `refactor:` prefix).
6. Move to next step.

If a step breaks, REVERT immediately. Do not "fix forward" mid-step — the small-step contract is the entire safety net.

### Step 6: Specific patterns for the EventPro giants

**BudgetTable.tsx (1093 lines):**
- Likely candidates for extraction: `BudgetRow` (already a separate component per CLAUDE.md §13), `BudgetCell` editors, `useBudgetReorder` hook (DnD logic), `useCommentsPanel` hook (Sheet open/close + active item).
- Don't split the per-level `SortableContext` architecture — it's correct and tested.
- The cell-edit auto-save pattern (toast.success "✓ Salvo" with 1200ms duration per CLAUDE.md §7) is core; preserve.

**Dashboard.tsx (~987 lines):**
- Reorganized in P3.1 / P3.2 / P3.3 with hero alert, KPI tiles, EVENT_TYPE_VISUAL map, temporal grouping (Acontecendo Agora / Esta Semana / Este Mês / Próximos / Confirmados / Planejando / Encerrados).
- Candidates: `useDashboardData` hook (consolidating the multiple tRPC `dashboard.*` queries), `EventCard` component (the contextual cards by group), `KpiTile` component, `HeroAlert` component, `EventGroupingNav` component.
- `invalidateDashboard` helper (per CLAUDE.md §7) is the correct pattern; don't replace.

**EventPage.tsx (864 lines):**
- Tab routing is dynamic from `event_tabs` table with FALLBACK_NAV_TABS. Preserve.
- Candidates: `useEventTabs` hook (combining DB tabs + fallback), `EventHeader` component, `TabNav` component, `useTabKeyValidation` hook.

### Step 7: Document the new structure
After the refactor lands, update CLAUDE.md if the file structure changed materially. Specifically:
- New file paths added under `## 3. Estrutura de arquivos`.
- New hooks added to the `hooks/` listing.
- Changes to which file owns which responsibility.

This is a 4-6 line edit, not a rewrite.

### Step 8: Verify with `verification-before-completion`
Final gate. Before declaring the refactor done, run the full verification skill checklist.

## Output format

A multi-step plan, commit-by-commit:

```
## Refactor Plan — <target file>

### Goal
<one sentence>

### Inventory of <file>
- Exports: ...
- State hooks: ...
- Effects: ...
- Inline components: ...
- Helpers: ...
- tRPC: ...

### Plan (ordered, smallest-first)
**Step 1**: <name>
- Change: ...
- New files: ...
- Imports updated: ...
- Tests expected to pass unchanged: ...
- Estimated diff: ~N lines
- Commit message: refactor: <message>

**Step 2**: <name>
...

### Per-step verification
After each step:
- pnpm tsc --noEmit — 0 errors
- pnpm test — <expected count>
- Manual smoke: <which page to click>

### Final state
- Files: <new layout>
- Public API unchanged: <Yes / No, with details>
- Behavior unchanged: <Yes / No, with details>
```

## Quality checklist
- [ ] Success criterion is named and measurable (LOC, separation, testability).
- [ ] Each step's diff is under ~200 lines net.
- [ ] Each step commits independently — no "stage 3 depends on uncommitted stage 2 work".
- [ ] After each step: tsc + test gates run.
- [ ] No public tRPC contract changes unless explicitly in scope.
- [ ] No shadcn/ui (`components/ui/`) edits.
- [ ] CLAUDE.md updated if structure materially changed.
- [ ] Behavior is unchanged unless the user explicitly asked for a behavior change.

## Notes for the assistant
- The cardinal rule: **if you can't run gates between steps, the refactor is too big**.
- "Refactor + bug fix in same commit" is anti-pattern. Refactor steps are pure structural changes; bug fixes go in separate commits.
- Be honest with the user when a refactor would not pay off. Sometimes the existing 1000-line file is fine; the user has lived with it for months. Forced refactors burn time without solving real pain.
- For the EventPro giants: do NOT propose splitting just because they're long. Propose splitting because a specific change is hard. CLAUDE.md notes per-level SortableContext is correct architecture; don't undo it.
- Renames cascade through the whole codebase — verify every import via search before finalizing. tRPC contract names ripple to the frontend (CLAUDE.md item 17 about `importData` vs `import`).
- For test files: refactors should rarely touch tests. If a refactor changes test imports widely, the public surface of the module changed — flag this as a design decision the user should approve.
- Pair with `react-expert` for the "what to extract" judgment, with `verification-before-completion` for gating, and with `code-architect` for module-boundary questions.
- Don't refactor and add tests in the same step — separate commits, separate verifications.
