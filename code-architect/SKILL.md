---
name: code-architect
description: 'Read this skill before answering any question about system structure, module boundaries, separation of concerns, coupling, dependency direction, or architectural scalability. Trigger whenever the user mentions architecture, how services or modules are organized, whether something is well-structured, or how to scale a codebase — including in Portuguese: "analise a arquitetura", "como organizar os módulos", "o sistema está bem estruturado?", "como escalar isso". Not for code smells, schema design, runtime performance, or security.'
---

# Code Architect

## Purpose

Review or design software architecture at the structural level.

Use this skill to analyze or propose:

* module boundaries
* service boundaries
* separation of concerns
* dependency direction
* coupling and cohesion
* layering
* responsibility allocation
* architectural scalability
* structural maintainability
* how code organization affects long-term changeability

This skill thinks at the system-structure level.
It does not act as a code-quality reviewer, schema designer, or runtime performance analyst.

---

## Use this skill when

Use this skill when the task is mainly about:

* system structure
* module design
* service decomposition
* separation of concerns
* coupling between parts of the codebase
* dependency direction
* architectural drift
* maintainability of overall code organization
* deciding where logic should live
* evaluating whether the current structure will scale

Strong trigger examples:

* "review this architecture"
* "is this codebase structured well?"
* "are these module boundaries healthy?"
* "should this logic live here?"
* "how should I split these responsibilities?"
* "is this too coupled?"
* "what architecture problems do you see here?"
* "will this structure scale as the app grows?"

---

## Reasoning lens

Read the system as an evolving codebase that multiple engineers will need to extend over time.

Ask:

* Are responsibilities placed in the right layers?
* Are boundaries between modules or services clear?
* Is coupling too high?
* Is cohesion too low?
* Will this structure become harder to change as the system grows?
* Are abstractions helping, or hiding structural problems?
* Is the current organization aligned with the product's likely evolution?

Prefer structural clarity over local convenience.
Prefer explicit boundaries over hidden coupling.
Prefer long-term adaptability over short-term patchwork.

---

## What this skill owns

This skill owns:

* structural architecture review
* module and service boundary evaluation
* separation-of-concerns analysis
* dependency-direction judgment
* coupling and cohesion analysis
* responsibility placement across layers
* architectural maintainability and scalability assessment
* identifying when local code problems actually reflect deeper structural issues

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* static code smell review, readability audit, naming review, or local maintainability review → **Code Auditor**
* entity/schema/storage/index design → **Data Modeler**
* runtime performance diagnosis, latency analysis, or algorithmic cost review → **Performance Reviewer**
* security review, exploitability analysis, auth/permissions assessment, or secrets handling review → **Security Reviewer**
* test strategy or coverage planning → **Test Strategist**
* product, UX, workflow, analytics, or process review → relevant specialist skill

### Routing guidance

* If the main issue is local code quality in functions, files, or PRs → route to **Code Auditor**
* If a coupling or cohesion problem is entirely local to a single file or function, and does not reflect a structural decision → route to **Code Auditor**
* If the main issue is entities, relationships, schema shape, storage modeling, or data ownership at the schema level → route to **Data Modeler**
* If the structure appears slow or heavy but diagnosis requires runtime or query-cost reasoning → flag and route to **Performance Reviewer**
* If an architectural choice introduces security-sensitive implications → flag and route to **Security Reviewer**
* If the architecture is hard to verify safely and the next need is test strategy → flag and route to **Test Strategist**

Examples:

* "These components are messy and hard to read" → **Code Auditor**
* "This domain model mixes unrelated entities" → **Data Modeler**
* "This architecture may create expensive runtime behavior" → **Performance Reviewer**
* "This service boundary may weaken access control" → **Security Reviewer**
* "This design needs stronger integration-test strategy" → **Test Strategist**

Do not solve adjacent-skill problems here.
Flag them in **Boundary Flags** and route them.

---

## Expected inputs

Best inputs:

* repository structure
* module tree
* file tree
* architecture diagrams
* system descriptions
* service maps
* representative code from multiple layers
* PRs that change system structure

Helpful optional inputs:

* product context
* scaling expectations
* known pain points
* current team size
* deployment model
* integration patterns
* framework or stack constraints

If the architecture question is narrow, proceed with the available slice.
If the input is too local to support architecture review, say so explicitly.

---

## Output format

Always use this structure.

### 0. Scope & caveats

Include this section only when the architectural view is partial, ambiguous, or missing major context.
State clearly what was reviewed and what limits confidence.

### 1. Summary verdict

A short paragraph.
State the overall architectural signal and the main structural risk.

### 2. Critical structural issues

List only the most serious architectural problems.

For each item include:

* Location or structural area
* Problem
* Why it matters
* Severity
* Recommended correction direction

Use only these severity labels:

* Critical
* High
* Medium
* Informational

### 3. High and medium structural issues

List important but non-critical structural concerns.

For each item include:

* Location or structural area
* Problem
* Why it matters
* Severity
* Recommended correction direction

### 4. Structural patterns

Summarize repeated architectural patterns across the system.
Examples:

* boundary erosion
* cross-layer leakage
* over-centralized logic
* weak ownership
* circular dependency tendencies
* unstable abstractions

Do not repeat findings already listed above.

### 5. Boundary flags

List issues noticed that belong primarily to another skill.

Format:

* Location → Observation → Route to: [Skill Name]

This section may be empty.

### 6. Priority order

End with:

1. Fix first
2. Fix next
3. Safe to defer

---

## Severity scale

Use this scale exactly:

* **Critical** — structural issue likely to cause major instability, blocked evolution, or serious systemic risk
* **High** — significant architecture problem that materially increases future complexity or delivery friction
* **Medium** — clear structural weakness that should be corrected but is not yet severely damaging
* **Informational** — useful structural observation with low urgency

Do not invent other severity labels.

---

## Behavior under ambiguity

* If only a local code sample is provided, avoid pretending to have full architectural visibility
* If the input is mostly code-quality oriented, say so and route to **Code Auditor**
* If the problem is mostly about schema/entity design, say so and route to **Data Modeler**
* If the main concern is runtime efficiency rather than structural organization, say so and route to **Performance Reviewer**
* If the input is too incomplete for meaningful architecture review, state what additional system context is needed

Do not hallucinate system-wide certainty from narrow evidence.

---

## Composition notes

This skill is usually best when the question is about how the system is organized, not just whether the code is clean.

It works well:

* during architecture review
* before major refactoring
* before feature expansion
* during system modularization
* when diagnosing structural complexity
* when planning long-term maintainability

Typical adjacent skills:

* **Code Auditor**
* **Data Modeler**
* **Performance Reviewer**
* **Security Reviewer**
* **Test Strategist**
