---
name: module-interface-designer
description: Design and compare alternative technical interfaces for modules, APIs, services, adapters, and contracts. Use when a system needs a clean contract before implementation or when multiple interface shapes should be explored.
---

# Module Interface Designer

## Purpose

Design technical interfaces that make software modules easier to use, test, evolve, and reason about.

This skill focuses on contracts between system parts, not visual UI.

It explores multiple possible interface shapes before choosing one.

---

## Use this skill when

Use this skill when the task is mainly about:

* designing a module interface
* defining an API contract
* comparing service boundaries
* shaping adapters or ports
* deciding what a caller should know
* hiding implementation complexity behind a clean contract
* designing testable seams
* exploring multiple interface options before coding

Strong trigger examples:

* "design the interface for this module"
* "what should this service API look like?"
* "compare possible contracts for this feature"
* "how should the frontend talk to the backend?"
* "design an adapter interface"
* "make this module easier to test"

---

## Do not use this skill when

Do not use this skill when the task is mainly about:

* visual interface layout → Interface Designer
* broad architecture → Code Architect
* schema/entity design → Data Modeler
* implementation → Implementation Engineer
* test strategy → Test Strategist
* product feature choice → Product Strategist

---

## Core principles

A good interface:

* is small but powerful
* hides implementation complexity
* is hard to misuse
* supports the most important use cases naturally
* exposes stable concepts rather than internal mechanics
* can be tested through public behavior
* avoids leaking storage, UI, or framework details unless necessary

A bad interface:

* mirrors internal implementation too closely
* forces callers to know too much
* has many shallow methods
* creates ambiguous responsibilities
* makes valid behavior hard and invalid behavior easy

---

## Workflow

### 1. Gather requirements

Understand:

* what problem the module solves
* who the callers are
* what operations matter
* what invariants must hold
* what should be hidden inside
* performance or compatibility constraints
* expected future use cases

### 2. Generate multiple designs

Create at least three meaningfully different interface options:

* minimal interface
* flexible interface
* common-case optimized interface
* domain-driven interface
* adapter/port-based interface when relevant

Do not produce cosmetic variations. Each option should reflect a different design philosophy.

### 3. Show usage examples

For each interface, show how a caller would use it.

Usage examples reveal whether the interface is actually simple.

### 4. Compare trade-offs

Evaluate:

* simplicity
* flexibility
* misuse risk
* testability
* implementation efficiency
* domain clarity
* long-term evolution

### 5. Recommend a direction

Pick the best option or synthesize a hybrid.

Explain why it fits the primary use case.

---

## Output format

Always use this structure.

### 1. Interface design context

Briefly summarize the module, callers, and key constraints.

### 2. Design options

For each option:

```md
## Option A — [name]

### Interface shape

[Types, functions, methods, endpoints, or contract shape]

### Example usage

[Caller-side example]

### What this hides

[Complexity hidden behind the interface]

### Trade-offs

- Strength:
- Weakness:
- Best fit:
```

### 3. Comparison

Compare options in prose or a compact table.

Include:

* easiest to use correctly
* most flexible
* most testable
* most aligned with domain language
* riskiest option

### 4. Recommendation

State the recommended interface and why.

### 5. Implementation notes

Durable guidance for Implementation Engineer.

### 6. Boundary flags

Format:

* Area → Observation → Route to: [Skill Name]

---

## Quality checklist

Before finalizing, verify:

* at least three distinct interface shapes were considered when appropriate
* usage examples are included
* the recommendation is tied to caller needs
* the interface hides real complexity
* implementation details do not leak unnecessarily
* testability is considered
* domain language is used consistently

---

## Composition notes

This skill works well after:

* Code Architect
* Data Modeler
* Domain Language Cartographer

It hands off naturally to:

* Implementation Engineer
* TDD Implementation Runner
* Test Strategist
