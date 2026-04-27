---
name: bug-triage-tdd-planner
description: Investigate reported bugs, identify likely root cause, and produce a TDD-based fix plan with RED-GREEN cycles. Use when a bug needs diagnosis before implementation or when a regression issue should become an actionable GitHub ticket.
---

# Bug Triage TDD Planner

## Purpose

Diagnose bugs and convert them into actionable fix plans driven by behavior tests.

This skill investigates symptoms, identifies likely root cause, and defines a safe test-first correction path.

It plans the fix. It does not primarily execute the implementation unless paired with TDD Implementation Runner.

---

## Use this skill when

Use this skill when the task is mainly about:

* triaging a bug
* finding root cause
* turning a bug report into a GitHub issue
* planning a regression test
* deciding the smallest safe fix
* designing RED-GREEN cycles for a bug fix
* distinguishing symptom from cause

Strong trigger examples:

* "triage this bug"
* "why is this failing?"
* "create a fix plan for this issue"
* "find the root cause and make a TDD plan"
* "turn this bug into an issue"
* "what regression test should we add?"

---

## Do not use this skill when

Do not use this skill when the task is mainly about:

* executing the fix immediately → TDD Implementation Runner
* manually testing the app → QA Executor
* broad code quality review → Code Auditor
* architectural redesign → Code Architect
* performance diagnosis under load → Performance Reviewer
* security vulnerability analysis → Security Reviewer
* production incident telemetry review → Production Reviewer

---

## Workflow

### 1. Capture the symptom

Record:

* actual behavior
* expected behavior
* reproduction steps if known
* environment if known
* affected user path
* frequency or severity if known

If the user has not described the bug, ask one concise question: what problem are you seeing?

### 2. Investigate the path

Explore the relevant code, tests, logs, or product flow.

Look for:

* entry point where the bug manifests
* user action or system event that triggers it
* contract violated
* missing validation
* stale state
* data mismatch
* broken assumption
* similar working patterns elsewhere
* missing regression coverage

### 3. Identify root cause

State the likely root cause in durable terms.

Prefer describing behavior and contracts over fragile file-line references.

### 4. Design TDD fix plan

Create ordered RED-GREEN cycles:

* **RED** — one failing test that captures the broken behavior
* **GREEN** — smallest code change to pass
* **REFACTOR** — cleanup after green, if needed

### 5. Define acceptance criteria

Acceptance criteria must prove the bug is fixed and does not regress.

---

## Output format

Always use this structure.

### 1. Triage summary

Briefly state the bug, likely severity, and confidence level.

### 2. Observed vs expected behavior

**Observed:**

**Expected:**

### 3. Root cause analysis

Describe:

* affected behavior path
* broken assumption or contract
* why the symptom occurs
* related areas that may be impacted

### 4. TDD fix plan

```md
1. RED: Write a test that [behavior currently broken]
   GREEN: Change [system behavior] so that [expected outcome]

2. RED: Write a test that [edge/regression behavior]
   GREEN: Change [system behavior] so that [expected outcome]

REFACTOR: [cleanup after all tests pass]
```

### 5. Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] New regression test fails before fix and passes after fix
- [ ] Existing tests still pass

### 6. GitHub issue draft

Provide a copy-ready issue body if requested or appropriate.

### 7. Boundary flags

Format:

* Area → Observation → Route to: [Skill Name]

---

## Quality checklist

Before finalizing, verify:

* the root cause is not just a restatement of the symptom
* the first test would fail before the fix
* each cycle is small and behavior-driven
* tests target public behavior or stable contracts
* the fix plan avoids broad unrelated refactors
* acceptance criteria are observable

---

## Composition notes

This skill works well before:

* TDD Implementation Runner
* Vertical Slice Planner
* QA Executor

It works well after:

* Production Reviewer
* QA Executor
* Code Auditor
