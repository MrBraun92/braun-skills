---
name: database-optimizer
description: Identifies slow queries, N+1 patterns, missing indexes, and bad execution plans in the EventPro stack (Drizzle ORM + MySQL/TiDB Cloud). Suggests idempotent Drizzle migrations following the project's naming convention (drizzle/NNNN_*.sql + _journal.json). Knows TiDB-specific quirks (DDL semantics, ALGORITHM=INPLACE, ANALYZE TABLE, optimistic vs pessimistic txn). Use when the user says "this query is slow", "optimize the database", "add an index", "EXPLAIN this", "N+1", "TiDB", or when Dashboard / BudgetTable / financial endpoints feel laggy.
---

# Database Optimizer (EventPro / TiDB)

Diagnoses and fixes performance problems in the EventPro database layer. Stack-specific: **Drizzle ORM 0.x + mysql2 + TiDB Cloud (MySQL-compatible, but not vanilla MySQL)**. Knows the EventPro schema (events, event_tabs, budget_items, sponsors, tickets, pos, artists, staff, event_groups, workspace_members, workspace_invites — 19+ tables), the existing indexes (`idx_budget_items_event_tab` from migration 0012, `ix_event_tabs_event` from 0014, etc.), and the optimization work already done in Sprint 5 / Sprint 6.

## When to use this skill
- Dashboard takes >2s to render its KPIs.
- BudgetTable lags when an event has 200+ items.
- A specific tRPC endpoint shows up in production logs as slow.
- A new feature adds a query and the user wants it reviewed before merge.
- TiDB Cloud's slow query log surfaces a candidate.
- The user is about to add a migration and wants the index plan reviewed.

## Methodology

### Step 1: Confirm the slow query
Ask:
- Which endpoint / page is slow?
- Approximate latency (median, p95)?
- Sample event size (small workspace, big workspace, big group)?
- TiDB region and cluster tier (Serverless vs Dedicated)?
- Is the slowness consistent or intermittent?

If the user only says "the dashboard is slow", the FIRST step is identifying which query — not guessing. Pull from server logs (pino) or add temporary timing logs around tRPC calls in `server/routers/dashboard.ts`.

### Step 2: Pull EXPLAIN
For each candidate query, run `EXPLAIN ANALYZE` (TiDB supports it; output is richer than vanilla MySQL):

```sql
EXPLAIN ANALYZE
SELECT * FROM budget_items
WHERE event_id = 42 AND tab_key = 'infraestrutura'
  AND deleted_at IS NULL
ORDER BY order_index;
```

Look for:
- **Full table scan** (`TableFullScan`) on a large table — index probably missing.
- **`IndexLookUp`** with high `actRows` per row — index hit but selectivity is bad.
- **`Selection`** node filtering after scan — column predicates not using the index.
- **`HashJoin`** with a giant probe side — query plan choosing the wrong join order.
- **`Sort`** without index assistance — composite index might let it sort directly.

For TiDB specifically: also check `TIKV_REGION_STATUS` if region splits look uneven, and `INFORMATION_SCHEMA.TIDB_HOT_REGIONS` for hot-spot patterns.

### Step 3: Identify the root cause
Common EventPro patterns and their root causes:

- **Dashboard KPIs slow** → likely missing batch helper. CLAUDE.md §13 confirms `dashboard.ts` uses `batchBudgetItems/Tickets/Sponsors/PosRevenue` with `inArray`. If a NEW endpoint regressed to per-event loops, that's an N+1.
- **BudgetTable slow** → likely missing `idx_budget_items_event_tab`. Confirmed present in migration 0012. If regression, check.
- **EventPage tab list slow** → likely missing `ix_event_tabs_event`. Confirmed present in migration 0014.
- **Group rollup slow** → `event_groups` queries should join via `events.groupId`; missing index there is plausible.
- **Workspace member list slow** → `workspace_members(workspaceId, userId)` index status; `workspace_invites(workspaceId, email)` for unique-pending check.
- **Sponsor listing slow** → `sponsors(eventId, status)` if status filter used in queries (post-Sprint 6 #2 enum).
- **Soft-delete scans** → if `deletedAt IS NULL` is in WHERE but the index doesn't include it, MySQL/TiDB may still scan deleted rows.

### Step 4: Recommend the fix
Choose the cheapest effective fix:

- **Add a composite index** if a query consistently filters on (col1, col2) and sorts by col3 → index on `(col1, col2, col3)`.
- **Add a partial / functional index** — TiDB supports expression indexes; useful for `WHERE deleted_at IS NULL`.
- **Rewrite the query** if the structure is wrong (e.g., subquery that should be a JOIN, or `OR` that prevents index usage).
- **Use `inArray` (Drizzle)** for batched fetches instead of per-row queries (the canonical N+1 fix per CLAUDE.md §7).
- **Cache** at React Query level only if data is stable (e.g., event_tabs); never cache financial data.
- **Run `ANALYZE TABLE`** if the optimizer's stats are stale (TiDB sometimes needs a manual nudge).

### Step 5: Write the migration
Follow EventPro's migration convention (CLAUDE.md §11):

1. Create file `drizzle/00NN_<name>.sql` (next sequential number — currently `0021_workspace_plan` is the latest, so next would be `0022`).
2. Write idempotent SQL — `CREATE INDEX IF NOT EXISTS` if the engine supports it; otherwise wrap in a check.
3. For TiDB, use online DDL hints when applicable: `ALGORITHM=INPLACE, LOCK=NONE` (TiDB DDL is online by default but explicit hints help).
4. Update `drizzle/meta/_journal.json` — append entry following the existing pattern (idx, when, tag, breakpoints).
5. Update `drizzle/schema.ts` — add the index definition to the relevant table so Drizzle introspection stays consistent.

Example:

```sql
-- drizzle/0022_idx_event_groups.sql
ALTER TABLE events
  ADD INDEX idx_events_group_id (group_id);
```

```ts
// drizzle/schema.ts (snippet)
export const events = mysqlTable('events', {
  // ... existing columns
  groupId: bigint('group_id', { mode: 'number' }),
}, (t) => ({
  groupIdx: index('idx_events_group_id').on(t.groupId),
}));
```

Note: never run `drizzle-kit push` against production without reviewing the SQL it generates. Apply manually via TiDB Cloud SQL editor for production.

### Step 6: Verify
- Re-run `EXPLAIN ANALYZE`. Confirm the plan switched (full scan → index seek; high actRows → reasonable).
- Measure latency before/after via the same endpoint.
- Run `pnpm test` — query changes can break tests if they depend on row order.
- Check no regression in adjacent endpoints (per `verification-before-completion`).

### Step 7: Document
A short note in the migration file's leading comment: why this index was added, which endpoint benefits, expected size of the table at workspace scale.

## Output format

```
## Database Optimization — <endpoint or query>

### Diagnosis
- Query: <SQL or Drizzle expression>
- EXPLAIN ANALYZE summary: <plan nodes, actRows, execution time>
- Root cause: <missing index / N+1 / bad plan / stale stats>

### Recommended fix
<index definition / query rewrite / batch helper change>

### Migration (if needed)
File: drizzle/00NN_<name>.sql
SQL:
<sql>

drizzle/schema.ts addition:
<typescript>

drizzle/meta/_journal.json entry:
<json>

### Verification plan
- EXPLAIN ANALYZE before/after
- Endpoint latency before/after
- Tests still pass

### TiDB notes
<anything specific to TiDB DDL or regions>
```

## Quality checklist
- [ ] Diagnosis is based on actual EXPLAIN output, not guesswork.
- [ ] Migration filename follows convention (next sequential number).
- [ ] Migration is idempotent (re-running is safe).
- [ ] `_journal.json` and `schema.ts` updated alongside the SQL file.
- [ ] No `drizzle-kit push` applied to production without review.
- [ ] TiDB DDL semantics considered (online DDL hints, region behavior).
- [ ] Verification plan includes both EXPLAIN re-check and endpoint latency.
- [ ] Adjacent endpoints regression-checked.

## Notes for the assistant
- TiDB ≠ vanilla MySQL. Differences that matter: distributed plan, regional hot spots, online DDL is default, optimistic txn default, AUTO_INCREMENT may not be sequential, `SELECT FOR UPDATE` semantics differ slightly.
- TiDB Serverless has cold-start latency on the first query of an idle period. Don't misdiagnose cold-start as a query plan issue.
- For Drizzle, the schema definition MUST stay in sync with applied migrations. A migration that adds an index without a corresponding `index('...')` in `schema.ts` will work at runtime but break introspection.
- N+1 detection: count tRPC requests in browser devtools Network tab; if loading one page causes 50+ similar requests, that's the smoke. Look at the server endpoint, not the client.
- Per CLAUDE.md §13, the dashboard's N+1 was already resolved with batch helpers. Do not re-introduce per-event loops "for clarity" — the loops are slow for a reason.
- Index ordering matters: `(eventId, tabKey)` is different from `(tabKey, eventId)`. The leftmost prefix rule applies in TiDB the same as MySQL.
- For soft-delete columns (`deletedAt`), including the column in a partial index reduces scan size, but TiDB's expression index support is more limited than Postgres. Prefer composite `(eventId, deletedAt)` only if `deletedAt IS NULL` is the dominant predicate.
- Pair with `verification-before-completion` for the migration verification gate, and with `error-detective` if a slow query is causing user-visible errors (timeouts, partial renders).
- Do not enable query caching at the application layer for financial data — Sprint 5 vocabulary (`shared/financial.ts`) is the canonical source; cached values risk staleness mid-edit.
