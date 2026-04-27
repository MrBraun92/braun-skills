---
name: repo-quality-setup
description: Configure repository quality gates such as formatting, linting, type checking, tests, pre-commit hooks, and staged-file checks. Use when a repo needs baseline engineering hygiene before AI-assisted implementation or release.
---

# Repo Quality Setup

## Purpose

Set up baseline engineering quality gates for a repository.

This skill configures or recommends tooling that prevents low-quality changes from entering the codebase.

It focuses on automated checks, not manual QA or release verification.

---

## Use this skill when

Use this skill when the task is mainly about:

* setting up pre-commit hooks
* configuring formatting
* configuring lint-staged
* adding typecheck/test checks before commit
* standardizing repository scripts
* improving baseline code hygiene
* preparing a repo for AI coding agents
* making quality checks easy to run locally and in CI

Strong trigger examples:

* "set up pre-commit"
* "add lint-staged and prettier"
* "make this repo safer before coding"
* "configure quality gates"
* "what checks should run before commit?"
* "standardize test/typecheck scripts"

---

## Do not use this skill when

Do not use this skill when the task is mainly about:

* writing tests for behavior → TDD Implementation Runner
* designing test strategy → Test Strategist
* manual exploratory QA → QA Executor
* release readiness → Release Verifier
* security risk review → Security Reviewer
* coding-agent destructive command safety → Coding Agent Safety Guardrails

---

## Typical quality gates

Depending on stack, configure or recommend:

* formatter
* linter
* staged-file formatting
* type checking
* unit tests
* integration tests where appropriate
* secret scanning
* commit hooks
* CI checks
* package manager consistency

---

## Workflow

### 1. Detect project stack

Inspect files such as:

* `package.json`
* lockfiles
* framework config
* test config
* TypeScript config
* existing formatter/linter config
* CI workflows

### 2. Detect package manager

Prefer existing lockfile:

* `package-lock.json` → npm
* `pnpm-lock.yaml` → pnpm
* `yarn.lock` → yarn
* `bun.lockb` → bun

Do not switch package managers without explicit approval.

### 3. Identify existing scripts

Check whether scripts exist for:

* format
* lint
* typecheck
* test
* build

Add or recommend missing scripts only when appropriate.

### 4. Configure pre-commit flow

When applicable, configure:

* Husky or equivalent
* lint-staged
* formatter for staged files
* typecheck/test commands when fast enough

If full tests are slow, recommend CI-only or pre-push rather than blocking every commit.

### 5. Verify setup

Run non-destructive checks:

* formatter dry-run or staged check
* lint
* typecheck
* tests
* hook smoke test

### 6. Document usage

Explain how developers/agents should run checks before handoff.

---

## Output format

Always use this structure.

### 1. Repo quality verdict

State current quality setup and main gap.

### 2. Detected stack

List package manager, framework, test runner, formatter/linter if known.

### 3. Changes configured or recommended

```md
| Area | Tool/Script | Status | Notes |
|---|---|---|---|
| Formatting | Prettier | Added / Existing / Recommended | Notes |
```

### 4. Quality command set

List commands developers and agents should run:

```bash
npm run format
npm run lint
npm run typecheck
npm run test
```

Adapt to actual package manager.

### 5. Verification results

Summarize checks run and outcomes.

### 6. Remaining gaps

List anything that still needs CI, branch protection, or manual setup.

### 7. Boundary flags

Format:

* Area → Observation → Route to: [Skill Name]

---

## Quality checklist

Before finalizing, verify:

* package manager detection is correct
* existing configs are not overwritten unnecessarily
* commands match actual scripts
* slow checks are placed appropriately
* generated setup is safe for AI agents
* verification is performed where possible
* remaining manual steps are explicit

---

## Composition notes

This skill works well before:

* Implementation Engineer
* TDD Implementation Runner
* QA Executor
* Release Verifier

It complements:

* Coding Agent Safety Guardrails
* Test Strategist
* Security Reviewer
