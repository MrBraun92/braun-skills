---
name: vertical-slice-planner
description: Break PRDs, specs, plans, or feature ideas into thin independently implementable vertical-slice GitHub issues. Use when work needs to be decomposed into AFK/HITL implementation slices with dependencies, acceptance criteria, and verification paths.
---

# Vertical Slice Planner

## Purpose

Convert product plans, specs, PRDs, feature briefs, or implementation ideas into small vertical slices that can be independently picked up by an implementation agent or developer.

A vertical slice is a narrow but complete path through the system. It should produce observable progress and be independently verifiable.

This skill turns broad plans into execution-ready issues.

---

## Use this skill when

Use this skill when the task is mainly about:

* breaking a feature into implementation issues
* converting a PRD into tickets
* decomposing an MVP into buildable increments
* sequencing work for an AI coding agent
* identifying which tasks can be executed autonomously and which need human decisions
* avoiding vague, oversized implementation requests
* turning a product plan into thin demoable slices

Strong trigger examples:

* "break this into GitHub issues"
* "turn this PRD into implementation tickets"
* "split this MVP into vertical slices"
* "make this plan agent-executable"
* "what should Claude Code build first?"
* "create AFK and HITL tasks from this spec"

---

## Do not use this skill when

Do not use this skill when the task is mainly about:

* deciding product direction before scope exists → Product Strategist
* clarifying a vague requirement before slicing → Requirements Analyst
* designing architecture before tasks can be sliced → Code Architect
* implementing the slices → Implementation Engineer
* testing strategy across a change → Test Strategist
* manual QA execution → QA Executor

---

## Core principles

### Slice vertically, not horizontally

Avoid issues like:

* "Build database schema"
* "Build backend"
* "Build frontend"
* "Add tests"

Prefer issues like:

* "Import one CSV file and display parsed event expenses in a basic table"
* "Create one editable budget item and persist the update"
* "Show cash-flow summary for imported expenses with regression coverage"

Each slice should ideally touch every layer needed to prove user-visible behavior.

### Prefer many thin slices over few thick slices

Each slice should be small enough that a coding agent can complete it without inventing broad scope.

### Separate AFK from HITL

Use:

* **AFK** — can be implemented without further human decision
* **HITL** — requires human-in-the-loop decision, design approval, domain clarification, or trade-off selection

Prefer AFK where the decision is already clear.

---

## Workflow

### 1. Gather context

Use the current conversation, PRD, plan, codebase notes, or user-provided spec.

Identify:

* target user behavior
* system areas involved
* known constraints
* dependencies
* missing decisions
* success criteria

If the source material is vague, flag what is missing before slicing too aggressively.

### 2. Identify user-visible outcomes

List the smallest observable outcomes the system should support.

Ask:

* What can be demonstrated after this slice?
* What behavior can be verified independently?
* What is the narrowest end-to-end path?

### 3. Draft vertical slices

For each slice, define:

* title
* type: AFK or HITL
* goal
* user-visible behavior
* affected areas
* dependencies
* acceptance criteria
* verification path
* notes for implementation agent

### 4. Order the work

Order slices so that:

* blockers come first
* early slices prove the riskiest paths
* foundations are created only when tied to visible behavior
* each slice leaves the system in a working state

### 5. Output execution-ready issues

Produce issue bodies that can be copied into GitHub or handed to a coding agent.

---

## Output format

Always use this structure.

### 1. Slicing verdict

Briefly state whether the plan is ready to slice or still has major ambiguity.

### 2. Slice map

| # | Slice | Type | Blocked by | Outcome |
|---|---|---|---|---|
| 1 | Slice title | AFK/HITL | None / # | Observable result |

### 3. GitHub issue drafts

For each slice:

```md
## What to build

[Concise description of the vertical slice and the user-visible behavior.]

## Type

AFK or HITL

## Why this slice exists

[Why this is the next useful increment.]

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Verification path

- [ ] How to manually verify
- [ ] What automated test or regression check should exist

## Blocked by

None / list dependencies

## Implementation notes

[Only include durable guidance. Avoid brittle file-specific instructions unless necessary.]
```

### 4. HITL decisions needed

List decisions that block autonomous execution.

### 5. Recommended build order

Numbered implementation order with rationale.

---

## Quality checklist

Before finalizing, verify:

* each slice has a user-visible or behavior-visible result
* no slice is merely a horizontal layer unless unavoidable
* acceptance criteria are specific and testable
* dependencies are explicit
* HITL/AFK classification is honest
* the first slices reduce uncertainty quickly
* the plan can be handed to an implementation agent without broad invention

---

## Composition notes

This skill works best after:

* Requirements Analyst clarifies scope
* Product Strategist confirms priority
* Code Architect defines major structure

It hands off naturally to:

* Implementation Engineer
* TDD Implementation Runner
* QA Executor
* Release Verifier
