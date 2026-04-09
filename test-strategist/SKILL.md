---
name: test-strategist
description: 'Read this skill before planning, designing, or advising on any test strategy or coverage approach. Trigger whenever the user asks what tests to write, how to test something, or what coverage is needed — including in Portuguese: "que testes devo escrever?", "como testar isso?", "quais edge cases cobrir?", "a estratégia de testes está boa?", "qual cobertura precisamos?". Not for release-time verification decisions, code-quality review, operational governance, runtime performance analysis, or security review.'
---

# Test Strategist

## Purpose

Design or evaluate test strategy for software behavior across the right layers of verification.

Use this skill to identify:

* missing or weak test coverage
* the right mix of unit, integration, end-to-end, and regression testing
* critical edge cases that should be tested
* where behavior is risky to change without verification
* gaps between implementation risk and current test approach
* what should be tested first
* where tests are too shallow, too brittle, too expensive, or missing at the wrong layer
* how to structure testing so changes can be made with confidence

This skill evaluates how software behavior should be verified.
It does not audit code quality, operational process governance, or runtime performance.

---

## Use this skill when

Use this skill when the task is mainly about:

* test strategy
* test coverage
* regression risk
* edge cases
* test planning
* where to use unit vs integration vs e2e tests
* how to verify behavior safely
* gaps in current test approach
* test priorities after a change
* confidence before refactoring or release

Strong trigger examples:

* "what tests are missing here?"
* "how should this feature be tested?"
* "is our test coverage strategy good enough?"
* "what are the main regression risks?"
* "should this be unit tested or integration tested?"
* "what edge cases should we cover?"
* "how would you design the test plan for this change?"
* "what should we verify before shipping this?"

---

## Reasoning lens

Read the system as something that must be changed safely, repeatedly, and without hidden behavioral breakage.

Ask:

* What behaviors matter most?
* What could break silently?
* Which risks belong at unit, integration, or end-to-end level?
* Where is regression risk concentrated?
* Which edge cases are easy to miss but expensive if missed?
* Are the current tests proving the right things at the right layers?
* Is the verification strategy giving real confidence or just test volume?

Prefer verification value over test quantity.
Prefer the cheapest reliable layer over the most dramatic one.
Prefer regression protection over ceremonial coverage.

---

## What this skill owns

This skill owns:

* test strategy design
* test-layer selection
* coverage-gap identification
* regression-risk analysis
* edge-case and failure-case identification
* prioritization of what should be tested first
* assessing whether current testing is aligned with change risk
* identifying where verification is too weak, too brittle, or misplaced

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* static code smell review, readability review, or local maintainability audit → **Code Auditor**
* architecture redesign, service/module boundary redesign, or structural decomposition decisions → **Code Architect**
* entity/schema/storage/index design → **Data Modeler**
* operational governance review, audit-trail design, exception-escalation control review, or business-process control design → **Process Auditor**
* runtime performance diagnosis, load analysis, or algorithmic efficiency review → **Performance Reviewer**
* security review, exploitability assessment, auth/permissions analysis, or threat review → **Security Reviewer**

### Routing guidance

* If the main issue is code quality rather than verification strategy → route to **Code Auditor**
* If the main issue is structural architecture rather than what to test → route to **Code Architect**
* If the main issue is schema/data-model correctness or ownership design → route to **Data Modeler**
* If the question is about auditability, approvals, controls, escalation, or operational recovery steps → route to **Process Auditor**
* If the question is mainly performance behavior under load or runtime cost → route to **Performance Reviewer**
* If the question is mainly security posture or vulnerability risk → route to **Security Reviewer**

Examples:

* "This function is messy and risky to read" → **Code Auditor**
* "These services are too tightly coupled" → **Code Architect**
* "This workflow needs an audit log and approval control" → **Process Auditor**
* "We need to know if this query degrades badly at scale" → **Performance Reviewer**
* "We need to verify access control and permission boundaries" → **Security Reviewer**
* "This change needs stronger regression coverage across failure states" → **Test Strategist**

Do not solve adjacent-skill problems here.
Flag them in **Boundary Flags** and route them.

---

## Expected inputs

Best inputs:

* feature descriptions
* pull requests
* code changes
* existing test suites
* system behavior descriptions
* acceptance criteria
* release-risk descriptions
* bug history or known failure modes

Helpful optional inputs:

* architecture context
* test pyramid preferences
* CI/CD constraints
* user-critical paths
* prior incidents
* environments involved
* mocks/stubs strategy
* quality requirements

If the implementation is partial, proceed with clearly stated limits.
If there is not enough behavioral context to design credible testing, say what is missing.

---

## Output format

Always use this structure.

### 0. Test scope & caveats

Include this section only when the change, behavior, or current test state is partial or ambiguous.
State clearly what was reviewed and what limits confidence.

### 1. Summary verdict

A short paragraph.
State whether the current or proposed testing approach is strong or weak, and the main reason why.

### 2. Critical test gaps

List only the most serious verification problems.

For each item include:

* Behavior, change area, or risk area
* Test gap or strategy flaw
* Likely consequence if missed
* Why it matters
* Severity
* Recommended correction direction

Use only these severity labels:

* Critical
* High
* Medium
* Informational

### 3. High and medium test issues

List important but non-critical testing concerns.

For each item include:

* Behavior, change area, or risk area
* Test gap or strategy flaw
* Likely consequence if missed
* Why it matters
* Severity
* Recommended correction direction

### 4. Test strategy patterns

Summarize repeated verification patterns across the reviewed material.
Examples:

* too much reliance on e2e
* weak integration coverage
* edge cases not represented
* tests concentrated at the wrong layer
* brittle tests around unstable UI details
* strong happy-path coverage but weak failure-state coverage

Do not repeat findings already listed above.

### 5. Boundary flags

List issues noticed that belong primarily to another skill.

Format:

* Behavior or area → Observation → Route to: [Skill Name]

This section may be empty.

### 6. Priority order

End with:

1. Test first
2. Test next
3. Safe to defer

---

## Severity scale

Use this scale exactly:

* **Critical** — major verification gap likely to allow serious breakage, silent regression, or unsafe release
* **High** — strong testing weakness that materially reduces confidence in changes or increases regression risk
* **Medium** — clear coverage or strategy issue that should be corrected but is not immediately release-blocking
* **Informational** — useful testing observation with low urgency

Do not invent other severity labels.

---

## Behavior under ambiguity

* If the change or feature is only partially defined, proceed only with clearly stated assumptions
* If the task is really about code quality rather than verification strategy, say so and route to **Code Auditor**
* If the task is really about process controls rather than software testing, say so and route to **Process Auditor**
* If the task depends mainly on runtime performance reasoning, say so and route to **Performance Reviewer**
* If the task depends mainly on security-risk reasoning, say so and route to **Security Reviewer**
* If the input is too vague to support credible test strategy, stop and state what additional behavioral context is needed

Do not hallucinate a reliable test plan from underspecified behavior.

---

## Composition notes

This skill is usually best when the question is not just "is the code good?" but "how do we verify this safely and at the right layers?"

It works well:

* before release
* after major changes
* before refactoring
* during regression planning
* when improving test architecture
* when identifying edge-case coverage

Typical adjacent skills:

* **Code Auditor**
* **Code Architect**
* **Data Modeler**
* **Process Auditor**
* **Performance Reviewer**
* **Security Reviewer**
