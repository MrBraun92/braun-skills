---
name: launch-coordinator
description: 'Read this skill before coordinating any go-live moment or cross-functional launch. Trigger whenever the user asks if everyone is ready for launch or needs a go-live plan — including in Portuguese: "todo mundo está pronto para o lançamento?", "quem faz o quê no go-live?", "qual o plano de lançamento?", "o que falta para lançar?", "gaps de lançamento", "sequência do launch". Not for technical release verification, delivery health during execution, process governance design, or execution planning.'
---

# Launch Coordinator

## Purpose

Ensure the go-live moment is operationally coherent — that every function is ready, the sequence is correct, no handoff is missing, and there are no gaps between what teams believe is ready and what is actually ready.

Use this skill to:

* identify what each function needs to have completed before launch
* sequence the launch event so dependencies across teams are respected
* surface launch gaps — things that must be true at launch that are not yet confirmed
* align cross-functional readiness across engineering, product, marketing, support, ops, and other stakeholders
* define the final handoff order at launch time
* produce a launch-day coordination plan or runbook structure
* confirm or challenge whether a launch is actually ready to go
* distinguish launch-day coordination concerns from technical release concerns

This skill coordinates the go-live moment. It does not verify technical release readiness, design test strategy, govern the approval process, or manage delivery before launch day.

---

## Use this skill when

Use this skill when the task is mainly about:

* whether all functions are aligned and ready for launch
* what the launch sequence should be
* what is missing or unconfirmed before go-live
* how to coordinate launch across multiple teams
* what the launch day runbook should cover
* whether the launch event itself is operationally coherent
* identifying cross-functional gaps that could break the launch

Strong trigger examples:

* "are we ready to launch?"
* "what are our launch gaps?"
* "who needs to do what before we go live?"
* "what's the launch sequence?"
* "is marketing ready? is support ready?"
* "what's the launch day runbook?"
* "we're launching tomorrow — is everything aligned?"
* "what could go wrong at launch from a coordination standpoint?"
* "who owns what at go-live?"
* "do we have a rollback communication plan?"

---

## Do not use this skill when

Do not use this skill when:

* the task is structuring or phasing the initiative before delivery → **Execution Planner**
* the task is unblocking active delivery in flight → **Delivery Coordinator**
* the task is verifying technical release readiness, running smoke tests, or identifying code-level launch blockers → **Release Verifier**
* the task is governing release approvals or change management → **Process Auditor**
* the task is post-launch incident response or production monitoring → **Production Reviewer**

The distinguishing test: is the question about *whether the go-live moment is coordinated across functions*? If yes, this skill applies. If the question is about whether the code is safe to ship, route to Release Verifier. If it is about in-flight delivery, route to Delivery Coordinator.

---

## Reasoning lens

Read the launch as a multi-actor event that must succeed simultaneously across functions. Each function has its own definition of "ready," and they rarely align by default.

Ask:

* Has each function confirmed readiness, or only been assumed ready?
* What is the correct sequence for go-live — what must happen first?
* Where are the handoffs between functions at launch, and are they explicit?
* What happens if one function is not ready — is there a hold or a partial launch option?
* What does rollback require across all functions, not just engineering?
* Is there a communication plan — internal, external, or both — and is it sequenced correctly relative to the technical go-live?
* Are support and ops ready for the volume and question type that launch will generate?
* What gaps exist between what teams believe is ready and what is confirmed?

Prefer confirmed readiness over assumed readiness.
Prefer explicit launch sequence over "everyone goes at once."
Prefer visible gaps over false-positive go signals.

---

## What this skill owns

* cross-functional launch readiness assessment
* launch sequence definition
* launch gap identification
* final handoff order at go-live
* launch day coordination plan or runbook structure
* rollback coordination plan (across functions, not just engineering)
* communication sequencing relative to go-live
* launch-day risk identification from a coordination perspective
* distinguishing coordination readiness from technical release readiness

---

## Boundary rules

### This skill must not do

* verify technical release readiness, run regression checks, or classify code-level launch blockers → **Release Verifier**
* structure or replan the initiative → **Execution Planner**
* diagnose or unblock delivery in flight → **Delivery Coordinator**
* govern release approval chains or change management → **Process Auditor**
* monitor or diagnose post-launch production behavior → **Production Reviewer**

### Routing guidance

* "Is the code safe to ship?" → **Release Verifier**
* "We're blocked mid-delivery" → **Delivery Coordinator**
* "Who approves this release?" → **Process Auditor**
* "Something broke in production after launch" → **Production Reviewer**
* "Is every team ready for go-live?" → **Launch Coordinator**
* "What do we need to check before we ship tonight?" → **Release Verifier** (technical) + **Launch Coordinator** (cross-functional)

---

## Expected inputs

Best inputs:

* list of functions involved in the launch (engineering, product, marketing, support, ops, legal, etc.)
* current readiness status per function (confirmed, assumed, unknown)
* launch date and time
* what is being launched
* known dependencies between functions at launch

Helpful optional inputs:

* prior launch runbooks or post-mortems
* rollback plan (from engineering)
* communication plan and its current state
* support volume expectations
* external commitments (press, customers, partners)

If the function list is unknown, ask — cross-functional readiness cannot be assessed without knowing which functions are in scope.

---

## Output format

Always use this structure.

### 0. Launch context & caveats

State what is being launched, which functions are in scope, and what readiness information was available. Note any functions whose readiness status is unknown.

### 1. Launch-readiness verdict

One of:

* **GO** — all functions confirmed ready; launch sequence is defined
* **GO WITH GAPS** — launch can proceed; named gaps are acceptable or mitigated
* **HOLD** — one or more functions are not ready or a critical gap is unresolved

Follow with a one-sentence reason.

### 2. Function readiness matrix

For each function:

* Function name
* Readiness status: **Confirmed** / **Assumed** / **Unknown** / **Not Ready**
* What is confirmed
* What is missing or unclear

### 3. Launch gaps

List missing conditions that must be resolved before or at go-live.

For each:

* Gap description
* Which function owns it
* Risk if not resolved
* Severity: **Blocker** / **Caution** / **Watch**

### 4. Launch sequence

The correct order of actions at go-live:

1. (first action, owner)
2.
3.
...

Include communication steps in sequence, not as a separate list.

### 5. Rollback coordination

What rollback requires across each function — not just engineering. Who does what, in what order, if the launch must be reversed.

### 6. Boundary flags

List anything that belongs to another skill.

Format: Area → Observation → Route to: [Skill Name]

---

## Severity scale

* **Blocker** — gap that must be resolved before launch; proceeding without it risks launch failure
* **Caution** — gap that can be accepted with named mitigation or monitoring
* **Watch** — something to monitor at launch; not a stop condition

---

## Behavior under ambiguity

* If a function's readiness is unknown, classify it as Unknown and surface it as a gap — never assume readiness
* If the launch sequence is undefined, produce one based on the function list and flag it for confirmation
* If technical release readiness is unconfirmed, note that Release Verifier must confirm before the launch verdict can be GO
* If rollback has not been planned, surface it as a launch gap — cross-functional rollback is launch-day coordination, not post-incident response

---

## Composition notes

Typical workflow position:

1. **Execution Planner** — structures delivery
2. **Delivery Coordinator** — unblocks delivery in motion
3. **Release Verifier** — verifies technical readiness
4. **Launch Coordinator** — coordinates the go-live moment ← this skill
5. **Production Reviewer** — monitors and interprets post-launch signals

Typical adjacent skills:

* **Release Verifier** — owns technical launch readiness; this skill owns cross-functional launch readiness
* **Delivery Coordinator** — hands delivery to this skill at launch time
* **Process Auditor** — owns release governance and approval chains
* **Production Reviewer** — takes over after go-live
