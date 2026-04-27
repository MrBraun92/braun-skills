---
name: deep-module-architect
description: Identify opportunities to turn shallow modules into deep modules with smaller interfaces, stronger seams, better locality, and higher leverage. Use when codebase architecture needs to become more testable, maintainable, and AI-navigable.
---

# Deep Module Architect

## Purpose

Find architectural opportunities to make modules deeper: small stable interfaces hiding meaningful implementation complexity.

This skill focuses on module depth, seams, adapters, locality, and leverage.

It complements Code Architect by applying a specific deep-module lens.

---

## Use this skill when

Use this skill when the task is mainly about:

* finding shallow modules
* improving testability through better seams
* reducing pass-through abstractions
* consolidating scattered behavior
* hiding complexity behind stable contracts
* making a codebase easier for AI agents to navigate
* improving locality of change
* turning brittle module boundaries into durable interfaces

Strong trigger examples:

* "find deep module opportunities"
* "this codebase has too many shallow services"
* "make this architecture more AI-navigable"
* "where are the bad seams?"
* "how can we improve module depth?"
* "which abstractions are not earning their keep?"

---

## Do not use this skill when

Do not use this skill when the task is mainly about:

* broad architecture review without deep-module focus → Code Architect
* local code quality review → Code Auditor
* interface contract design for one module → Module Interface Designer
* data schema design → Data Modeler
* implementation → Implementation Engineer
* refactor sequencing → Refactor Plan Writer

---

## Core vocabulary

Use these terms consistently:

* **Module** — any unit with an interface and implementation
* **Interface** — everything a caller must know to use the module
* **Implementation** — code and complexity hidden inside the module
* **Depth** — amount of leverage behind a small interface
* **Deep module** — small interface, substantial hidden behavior
* **Shallow module** — interface almost as complex as implementation
* **Seam** — place where behavior can vary without editing callers
* **Adapter** — concrete implementation behind a seam
* **Locality** — ability to understand or change behavior in one place
* **Leverage** — value callers get from a compact interface

---

## Diagnostic heuristics

Look for:

* modules that only pass data through
* services with many methods but little hidden behavior
* duplicated workflow logic across callers
* callers that know too much about internals
* tests forced to mock private details
* abstractions with only one hypothetical implementation
* concepts split across too many files
* framework details leaking into domain logic
* modules that fail the deletion test

### Deletion test

Ask:

If this module were deleted, would complexity disappear or simply move into callers?

* If deleting it removes ceremony, it may be shallow.
* If deleting it forces many callers to reimplement complexity, it is probably earning its keep.

---

## Workflow

### 1. Read context first

When available, read domain context, ADRs, glossary files, or architecture notes.

Do not re-litigate documented decisions unless current friction is strong enough.

### 2. Explore module usage

Inspect:

* callers
* public interfaces
* implementation depth
* tests
* duplication
* adapter patterns
* domain terms

### 3. Identify candidates

For each candidate, explain:

* what is shallow or leaky
* what complexity should move behind the interface
* what seam should exist
* what callers would no longer need to know
* what tests would become stronger

### 4. Recommend exploration order

Prioritize candidates that improve:

* high-change areas
* hard-to-test behavior
* repeated domain workflows
* risky coupling
* AI-agent navigability

---

## Output format

Always use this structure.

### 1. Architecture depth verdict

Briefly state whether the codebase/area shows shallow-module friction.

### 2. Deepening opportunities

For each candidate:

```md
## Candidate [#] — [name]

### Current friction

[What is shallow, leaky, duplicated, or hard to test.]

### Proposed deeper module

[What module/seam should exist and what it should hide.]

### Interface direction

[High-level shape, not full implementation.]

### Locality gain

[What changes become concentrated.]

### Leverage gain

[What callers get from the deeper abstraction.]

### Testing impact

[How tests become more behavior-oriented or stable.]

### Risk

Low / Medium / High
```

### 3. Recommended priority

Rank what to explore first and why.

### 4. Suggested next skill

Route each candidate to:

* Module Interface Designer
* Refactor Plan Writer
* Code Architect
* Test Strategist

### 5. Boundary flags

Format:

* Area → Observation → Route to: [Skill Name]

---

## Quality checklist

Before finalizing, verify:

* candidates are based on real friction, not aesthetic preference
* the proposed module hides meaningful complexity
* the interface direction is smaller than the implementation complexity
* testing impact is explicit
* risks are stated honestly
* documented decisions are respected unless there is reason to revisit them

---

## Composition notes

This skill works well after:

* Code Auditor
* Domain Language Cartographer
* Code Architect

It hands off naturally to:

* Module Interface Designer
* Refactor Plan Writer
* TDD Implementation Runner
