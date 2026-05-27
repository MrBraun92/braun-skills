---
name: tdd-implementation-runner
description: Execute feature development or bug fixes using a strict red-green-refactor loop. Use when implementation should be test-first, behavior-driven, incremental, and safe across public interfaces.
---

# TDD Implementation Runner

## Purpose

Implement features or fixes through disciplined test-driven development.

This skill owns the execution loop:

1. write one failing behavior test
2. implement the smallest change that passes
3. refactor only after green
4. repeat one vertical behavior at a time

It is not a general test planning skill. It is an implementation skill with tests as the steering mechanism.

---

## Use this skill when

Use this skill when the task is mainly about:

* implementing a feature test-first
* fixing a bug with regression coverage
* using red-green-refactor
* writing one behavior test at a time
* preventing overimplementation
* making code changes safely through public interfaces
* building a vertical slice with tests included

Strong trigger examples:

* "implement this using TDD"
* "fix this bug with a failing test first"
* "use red-green-refactor"
* "write the test first, then code"
* "build this slice with regression coverage"
* "do not implement without tests"

---

## Do not use this skill when

Do not use this skill when the task is mainly about:

* deciding what tests are needed without implementing → Test Strategist
* auditing existing test coverage → Test Strategist
* manual QA execution → QA Executor
* architectural redesign → Code Architect
* broad code implementation without test-first requirement → Implementation Engineer
* production telemetry diagnosis → Production Reviewer

---

## Core philosophy

Tests should verify observable behavior through public interfaces.

Good tests:

* describe what the system does
* exercise public APIs, UI behavior, commands, or documented contracts
* survive internal refactors
* fail for real behavior regressions

Bad tests:

* assert private implementation details
* mock internal collaborators unnecessarily
* depend on fragile file structure
* test imagined behavior in bulk before implementation begins

---

## Anti-patterns

Avoid horizontal TDD:

* writing all tests first
* implementing all code second
* testing internal structure instead of behavior
* adding speculative abstractions for future cases
* refactoring while tests are red

Correct pattern:

* one behavior
* one failing test
* smallest passing code
* optional refactor
* next behavior

---

## Workflow

### 1. Confirm behavior boundary

Before coding, identify:

* the public interface or user-visible behavior being changed
* the first behavior to prove
* any existing test patterns to follow
* the minimum success condition

If behavior is unclear, stop and ask only the minimum clarification needed.

### 2. Create the first RED test

Write one failing test for one behavior.

The test must:

* prove observable behavior
* fail before implementation
* avoid implementation coupling
* be narrow enough to diagnose failure clearly

### 3. Make it GREEN

Implement the smallest change that passes the test.

Do not:

* add future behavior
* redesign unrelated modules
* overgeneralize
* write code for tests that do not exist yet

### 4. Refactor only after green

After tests pass:

* remove duplication
* improve names
* simplify flow
* deepen modules only when naturally revealed
* keep behavior unchanged

Run tests again after refactor.

### 5. Repeat

Move to the next behavior only after the previous behavior is green.

---

## Output format

When reporting progress or final result, use this structure.

### 1. TDD scope

State the behavior or slice implemented.

### 2. RED-GREEN cycles

For each cycle:

```md
#### Cycle 1 — [behavior]

**RED:** [test written and why it failed]

**GREEN:** [minimal implementation added]

**REFACTOR:** [cleanup performed, or "none"]
```

### 3. Tests added or changed

List behavior coverage, not just filenames.

### 4. Implementation summary

Briefly state what now works.

### 5. Boundary flags

List any issues that belong to other skills.

Format:

* Area → Observation → Route to: [Skill Name]

---

## Quality checklist

Before finishing, verify:

* at least one test failed before implementation
* tests verify behavior, not private internals
* each cycle is small and understandable
* all tests pass after implementation
* refactor only happened after green
* no unrelated scope was added
* final behavior matches acceptance criteria

---

## Composition notes

This skill works well after:

* Vertical Slice Planner defines a slice
* Bug Triage TDD Planner identifies a fix path
* Test Strategist identifies priority behaviors

It hands off naturally to:

* Code Auditor
* QA Executor
* Release Verifier
