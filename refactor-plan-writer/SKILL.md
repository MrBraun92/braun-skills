---
name: refactor-plan-writer
description: Create safe refactor plans broken into tiny working commits with scope, decisions, tests, and out-of-scope boundaries. Use when a refactor needs to be planned before coding or recorded as an implementation issue.
---

# Refactor Plan Writer

## Purpose

Turn a refactoring intention into a safe, incremental plan that can be executed without destabilizing the codebase.

This skill creates micro-commit refactor plans where every step should leave the system working.

It plans refactors. It does not primarily execute them.

---

## Use this skill when

Use this skill when the task is mainly about:

* planning a refactor
* breaking a refactor into small commits
* creating a refactor RFC or GitHub issue
* reducing technical debt safely
* improving structure without changing behavior
* sequencing refactor work around existing tests
* defining refactor scope and non-goals

Strong trigger examples:

* "plan this refactor"
* "break this refactor into commits"
* "create a refactor issue"
* "how can we safely clean this up?"
* "make a no-behavior-change refactor plan"
* "what should be refactored first?"

---

## Do not use this skill when

Do not use this skill when the task is mainly about:

* diagnosing whether architecture is good → Code Architect
* finding deep module opportunities → Deep Module Architect
* reviewing code quality → Code Auditor
* implementing the refactor → Implementation Engineer or TDD Implementation Runner
* test strategy only → Test Strategist
* product requirement changes → Product Strategist or Requirements Analyst

---

## Core principles

A good refactor plan:

* preserves behavior
* reduces risk through tiny steps
* keeps the system working after each commit
* separates mechanical changes from semantic changes
* defines tests before risky movement
* avoids bundling cleanup with feature work
* makes rollback easy

A bad refactor plan:

* says "rewrite X"
* combines broad architectural change with feature delivery
* changes behavior accidentally
* lacks verification checkpoints
* produces giant commits
* depends on vague goals like "clean up code"

---

## Workflow

### 1. Understand the refactor problem

Clarify:

* what pain exists now
* what behavior must remain unchanged
* what code or module area is affected
* what is explicitly out of scope
* whether tests already cover the area
* whether any decisions are unresolved

### 2. Verify the current state

When codebase context is available, inspect relevant modules and tests.

Identify:

* coupling
* duplication
* confusing seams
* brittle tests
* missing characterization tests
* dependency direction problems

### 3. Define safe target shape

Describe the intended structure in durable language.

Avoid overcommitting to file paths unless necessary.

### 4. Break into tiny commits

Each commit should:

* be understandable in isolation
* leave the system working
* be reversible
* have a verification step
* avoid changing behavior unless explicitly marked

### 5. Identify test checkpoints

If coverage is weak, add characterization tests before movement.

---

## Output format

Always use this structure.

### 1. Refactor summary

State the problem, target improvement, and risk level.

### 2. Scope

**In scope:**

- Item 1

**Out of scope:**

- Item 1

### 3. Current friction

List the structural or maintainability problems being addressed.

### 4. Target shape

Describe the intended result after refactoring.

### 5. Tiny commit plan

```md
1. Commit: [short title]
   Purpose: [why this step exists]
   Change: [what changes]
   Verification: [test/check]
   Behavior change: No / Yes, explicitly described

2. Commit: [short title]
   Purpose:
   Change:
   Verification:
   Behavior change:
```

### 6. Testing decisions

State what tests should exist before, during, and after the refactor.

### 7. GitHub issue draft

Provide a copy-ready issue body when useful.

### 8. Boundary flags

Format:

* Area → Observation → Route to: [Skill Name]

---

## Quality checklist

Before finalizing, verify:

* every step keeps the system working
* behavior-preserving steps are clearly separated from behavior changes
* tests or checks are attached to risky steps
* the plan avoids huge commits
* out-of-scope boundaries are explicit
* the plan can be executed by an implementation agent without broad invention

---

## Composition notes

This skill works well after:

* Code Auditor
* Code Architect
* Deep Module Architect
* Test Strategist

It hands off naturally to:

* TDD Implementation Runner
* Implementation Engineer
* QA Executor
