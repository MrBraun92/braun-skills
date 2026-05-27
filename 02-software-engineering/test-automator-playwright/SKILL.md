---
name: test-automator-playwright
description: Generates end-to-end tests with Playwright for the EventPro SaaS (React 19 + Vite + tRPC + Drizzle/MySQL TiDB + AWS S3). Covers login, event creation, BudgetTable interactions, payment flow, share modal, AI chat. Includes patterns for testing drag-and-drop with @dnd-kit, tRPC mocking, and shadcn/ui component selectors. Use when the user says "write E2E tests", "Playwright test for X", "test the budget table", "regression test", "automate this flow", or wants coverage for a new EventPro feature.
---

# E2E Test Automator — Playwright (EventPro)

Generates Playwright end-to-end tests tuned to the EventPro stack: React 19 + Vite 7 + TypeScript, tRPC 11 frontend, shadcn/ui (Radix) components, wouter routing, @tanstack/react-query, @dnd-kit drag-and-drop. Knows the EventPro page structure (Dashboard, EventPage with dynamic tabs, CentralEventoPage at `/app/cockpit`, SettingsPage, SharedEventView) and writes tests against the actual selectors and flows.

## When to use this skill
- A new feature lands (e.g., a new tab in EventPage) and needs regression coverage.
- A bug was fixed; the user wants a test to lock in the behavior.
- Pre-deploy: smoke test for login → dashboard → create event → add budget item → mark paid.
- Drag-and-drop on `BudgetTable` is fragile and needs test coverage.
- Share-link flow (`SharedEventView` at `/view/:token`) needs to be verified after auth changes.

## Methodology

### Step 1: Confirm scope
Ask:
- Which user flow / page? (Dashboard, EventPage budget tab, payments tab, share modal, AI chat, settings/members, group page.)
- Smoke test (happy path only) or full regression (happy + edge + error)?
- Authenticated or anonymous? (Anonymous = `/view/:token`; everything else = authenticated.)
- Environment: local dev (`pnpm dev`), Sandbox/Manus, or production?
- Should tRPC be mocked or hit real backend?

### Step 2: Set up the test scaffold
Standard Playwright structure for EventPro:

```ts
import { test, expect, type Page } from '@playwright/test';

const BASE_URL = process.env.E2E_BASE_URL ?? 'http://localhost:5173';

async function login(page: Page, email = 'oliver@test.local') {
  await page.goto(`${BASE_URL}/`);
  // EventPro uses OAuth — for E2E, prefer a test-user shortcut endpoint
  // or seed a session cookie directly via API.
  // ...
}

test.beforeEach(async ({ page }) => {
  await login(page);
});
```

For EventPro, prefer **session-cookie injection** in `beforeEach` over actually clicking the OAuth button (OAuth providers are flaky in E2E). Use a backend test-only endpoint that mints a session for a test workspace.

### Step 3: Select elements correctly
- shadcn/ui components are Radix primitives — use `getByRole` over CSS selectors when possible.
- For Radix `Dialog`, `Popover`, `Select`: assert via `getByRole('dialog')`, `getByRole('combobox')`, etc.
- For wouter routes: assert via URL — `await expect(page).toHaveURL(/\/app\/events\/\d+\/orcamento/);`
- For tables (BudgetTable, PaymentsTab calendar), prefer `getByRole('row')` + filter by text.
- Avoid `data-testid` unless absolutely needed — let the test exercise real-user selectors.
- React Query / tRPC loading states: wait for `await page.waitForResponse(r => r.url().includes('/trpc/budget.list'))` instead of arbitrary timeouts.

### Step 4: Test critical EventPro flows
Standard test recipes:

**Login → Dashboard → Create Event:**
```ts
test('user can create an event', async ({ page }) => {
  await page.goto(`${BASE_URL}/app`);
  await page.getByRole('button', { name: /novo evento/i }).click();
  // Dashboard shows wizard with EVENT_TYPES grid (excluding 'corrida')
  await page.getByRole('button', { name: /festival/i }).click();
  await page.getByLabel(/nome do evento/i).fill('Festival E2E Test');
  await page.getByLabel(/data inicial/i).fill('2026-08-15');
  await page.getByRole('button', { name: /criar/i }).click();
  await expect(page).toHaveURL(/\/app\/events\/\d+\/overview/);
});
```

**BudgetTable — add item:**
```ts
test('adds a budget item under a category', async ({ page }) => {
  await page.goto(`${BASE_URL}/app/events/1/infraestrutura`);
  // Wait for hierarchical tree to load
  await page.waitForResponse(r => r.url().includes('/trpc/budget.list'));
  // Click "+ Adicionar item" inside the category row
  const categoryRow = page.getByRole('row').filter({ hasText: /palco principal/i });
  await categoryRow.getByRole('button', { name: /adicionar/i }).click();
  // ...
});
```

**Drag-and-drop with @dnd-kit:**
@dnd-kit uses pointer events, not native HTML5 drag. Use Playwright's manual `mouse.down` / `mouse.move` / `mouse.up` sequence at the item's center, OR use the `dragTo` helper with `targetPosition`. Key gotcha: @dnd-kit requires a small initial movement (>3px) before `onDragStart` fires.

```ts
test('reorders a budget item via DnD', async ({ page }) => {
  const handle = page.locator('[data-dnd-handle]').first();
  const target = page.locator('[data-dnd-handle]').nth(2);
  const handleBox = await handle.boundingBox();
  const targetBox = await target.boundingBox();
  if (!handleBox || !targetBox) throw new Error('boxes not found');
  await page.mouse.move(handleBox.x + 5, handleBox.y + 5);
  await page.mouse.down();
  await page.mouse.move(handleBox.x + 5, handleBox.y + 15); // initial nudge
  await page.mouse.move(targetBox.x + 5, targetBox.y + 5, { steps: 10 });
  await page.mouse.up();
  // Assert via tRPC response or order in the DOM
});
```

Note: per CLAUDE.md, DnD reorders only within the same `parentId`. Tests must respect that — drag-target must be a sibling.

**Payment flow:**
```ts
test('marks a budget item as paid', async ({ page }) => {
  await page.goto(`${BASE_URL}/app/events/1/pagamentos`);
  await page.getByRole('row').filter({ hasText: /gerador/i })
    .getByRole('combobox', { name: /status/i }).click();
  await page.getByRole('option', { name: /pago/i }).click();
  await page.waitForResponse(r => r.url().includes('/trpc/budget.update'));
  await expect(page.getByText(/✓ salvo/i)).toBeVisible();
});
```

**Share modal:**
```ts
test('generates a share link', async ({ page }) => {
  await page.goto(`${BASE_URL}/app/events/1/overview`);
  await page.getByRole('button', { name: /compartilhar/i }).click();
  await expect(page.getByRole('dialog')).toBeVisible();
  await page.getByRole('button', { name: /gerar link/i }).click();
  const input = page.getByRole('textbox', { name: /link público/i });
  await expect(input).toHaveValue(/\/view\/[A-Za-z0-9]+/);
});
```

### Step 5: tRPC mocking strategy
Two options:
- **Real backend** (preferred for E2E): seed test data via the `seed` router, run against actual TiDB test database, clean up via `events.delete` afterward.
- **Mocked tRPC** (faster, brittle): intercept `/trpc/*` POSTs with `page.route` and respond with fixtures. Use only when the test focuses on UI behavior, not backend integration.

```ts
// Real backend — seed test event in beforeEach
test.beforeEach(async ({ page, request }) => {
  await request.post(`${BASE_URL}/trpc/seed.createTestEvent`, {
    data: { input: { workspaceId: 1, name: 'E2E test event' } }
  });
});
```

### Step 6: Anonymous (share link) tests
For `/view/:token`:
```ts
test('share link renders without auth', async ({ browser }) => {
  const context = await browser.newContext({ storageState: undefined });
  const page = await context.newPage();
  await page.goto(`${BASE_URL}/view/${shareToken}`);
  await expect(page.getByRole('heading', { name: /festival/i })).toBeVisible();
  // Should NOT show edit affordances
  await expect(page.getByRole('button', { name: /editar/i })).toHaveCount(0);
});
```

### Step 7: Configure `playwright.config.ts`
EventPro-tuned config:

```ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: false, // EventPro has shared TiDB seed state; parallel risks collisions
  retries: process.env.CI ? 2 : 0,
  reporter: [['list'], ['html', { open: 'never' }]],
  use: {
    baseURL: process.env.E2E_BASE_URL ?? 'http://localhost:5173',
    trace: 'on-first-retry',
    locale: 'pt-BR', // EventPro UI is PT-BR; affects date pickers
    timezoneId: 'America/Sao_Paulo',
  },
  webServer: {
    command: 'pnpm dev',
    port: 5173,
    reuseExistingServer: !process.env.CI,
  },
});
```

Note locale + timezone — EventPro uses date-fns-tz and Sprint 6 #6 fixed timezone bugs by using UTC calendar-day comparisons. Tests should run with a deterministic timezone to avoid drift.

## Output format

A complete `.spec.ts` file (or set of files) plus a brief setup note:

```
## Playwright tests for <feature>

### Setup notes
- BASE_URL: configured via env or default localhost:5173
- Auth strategy: <session cookie injection / OAuth click-through>
- tRPC strategy: <real backend with seed / mocked>
- Locale/timezone: pt-BR / America/Sao_Paulo

### Files
- e2e/<feature>.spec.ts — <main test file>
- e2e/helpers/login.ts — <auth helper>
- playwright.config.ts — <if config changes needed>

### Code:
<full TypeScript source>

### How to run
pnpm exec playwright test e2e/<feature>.spec.ts
```

## Quality checklist
- [ ] Tests use `getByRole` / `getByLabel` over CSS selectors where possible.
- [ ] No arbitrary `waitForTimeout` — uses `waitForResponse` or `expect.toBeVisible` with timeout.
- [ ] DnD tests respect the @dnd-kit initial-nudge requirement.
- [ ] Tests use Portuguese accessible names (button labels, headings) since UI is PT-BR.
- [ ] Locale is `pt-BR` and timezone is set in config.
- [ ] Cleanup happens in `afterEach` or `afterAll` — no test-data leaks across runs.
- [ ] Anonymous flow tests use a fresh browser context (no cookies).
- [ ] Tests do NOT depend on production data — use seed router or fixtures.

## Notes for the assistant
- EventPro uses **wouter**, not React Router. URL assertions are reliable; component-level routing assertions are not (no `useNavigate`).
- The Cockpit / "Central do Evento" page is at `/app/cockpit` (file `CentralEventoPage.tsx`). Don't write tests against `/app/central-evento`.
- DnD on `BudgetTable.tsx` is per-level (`parentId`). Tests that drag across hierarchy levels will fail intentionally — that's the contract.
- For real-backend tests, the `seed` router has no auth guard (per CLAUDE.md item 17). Fine for test environments; do NOT enable in production.
- AI chat (`EventAIChat`) hits OpenAI — for E2E, mock the response or skip in CI to control cost.
- File upload tests must mock S3 or use a test bucket. Avoid uploading to production AWS.
- TiDB Cloud is the prod DB; for tests, use a separate database or schema. Drizzle migrations 0014+ should run against test DB before suite.
- The `/view/:token` route should NOT show edit affordances — that's a security regression test worth keeping.
- Tests should fail loudly when EventPro Sprint 7 invariants break: e.g., owner-only buttons appearing for non-owners, seat-limit warnings missing when at capacity.
- Pair with `verification-before-completion` skill — Playwright passing is one piece of evidence among several before declaring "done".
