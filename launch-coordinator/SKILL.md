---
name: launch-coordinator
description: Use for coordinating the go-live moment across functions — launch sequencing, cross-functional readiness alignment, final handoff order, launch gap identification, and ensuring the launch event is operationally coherent. Not for technical release verification, delivery health during execution, process governance design, or execution planning.
---

# Launch Coordinator

## Purpose

Ensure the go-live moment is operationally coherent — that all functions are aligned, the launch sequence is ordered, final dependencies are resolved, and the launch event itself is ready to execute.

Use this skill to:

* identify what is still unaligned before go-live across engineering, support, marketing, docs, and ops
* structure the launch sequence — what happens in what order at go-live
* identify final cross-functional dependencies that must be resolved before launch
* clarify handoff ownership at the launch moment
* distinguish between technical readiness (product works) and organizational launch readiness (everyone is aligned)
* structure a launch run-book for the go-live event
* identify launch coordination gaps that would make go-live incoherent
* define rollback ownership and conditions before launch
* sequence external communications relative to the launch event

This skill coordinates the organizational launch event.
It does not verify that the product works, diagnose active delivery health, design governance processes, or plan delivery phases.

---

## Use this skill when

Use this skill when a product, feature, or release is approaching go-live and the question is whether the *organization* is ready to launch — not just whether the product is technically ready.

Use this skill when:

* functions need to be aligned before go-live
* the launch sequence needs to be structured and ordered
* cross-functional dependencies are unclear or unresolved
* launch ownership and handoffs need to be confirmed
* a launch run-book needs to be assembled
* the distinction between "technically ready" and "launch-ready" needs to be made explicit
* something feels uncoordinated about the launch even though verification is done

Strong trigger examples:

* "are we launch-coordinated across all functions?"
* "what still needs to happen before we go live?"
* "structure the launch sequence for this release"
* "is support ready for this launch?"
* "who does what in what order at go-live?"
* "what cross-functional gaps do we still have before launch?"
* "help me coordinate the launch moment"
* "build a launch run-book for this release"
* "we're technically ready — are we operationally ready to launch?"
* "what would make this launch incoherent if we missed it?"

---

## Do not use this skill when

Do not use this skill when:

* the task is verifying that the product works before shipping → **Release Verifier**
* the task is diagnosing delivery health during active execution → **Delivery Coordinator**
* the task is designing approval flows, governance structure, or escalation paths → **Process Auditor**
* the task is planning phases, milestones, or delivery sequencing → **Execution Planner**
* the task is deciding whether to launch → **Product Strategist**
* the product has not yet been technically verified — coordinate after verification, not before

The distinguishing test: has technical verification happened (or is explicitly in progress with Release Verifier)? Is the question about whether the *organization* is aligned to go live, not whether the product is ready? If yes, this skill applies.

---

## Reasoning lens

Read the launch as an organizational event — a moment where multiple functions must act in a coordinated sequence, each depending on the others, and where gaps in coordination create chaos, confusion, or failure even when the product itself is ready.

Ask:

* Who needs to know what before the launch moment?
* What is the correct order of events at go-live — and what breaks if that order is wrong?
* Which functions are not yet confirmed as ready?
* Where does one function's readiness depend on another's action?
* What happens if this goes wrong at launch — who owns rollback and under what conditions?
* What external communications must happen, in what sequence, relative to deployment?
* What would make this launch operationally incoherent even if the product works?
* What is still unresolved that a reasonable person would consider a launch risk?

Prefer explicit sequencing over assumed coordination.
Prefer named ownership over collective responsibility.
Prefer surfacing gaps over assuming alignment.
Prefer operational coherence over technical-only readiness.

---

## What this skill owns

This skill owns:

* cross-functional launch readiness assessment
* launch sequence design — what happens in what order at go-live
* final dependency identification before the launch event
* handoff ownership clarification at launch time
* launch run-book assembly
* rollback ownership and condition definition
* external communication sequencing relative to deployment
* launch gap identification — what is still unaligned
* distinguishing technical readiness from organizational launch readiness

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* verify that the product works, run smoke checks, or produce a technical release-readiness verdict → **Release Verifier**
* diagnose delivery health, blocker status, or workstream coordination during the execution cycle → **Delivery Coordinator**
* design approval flows, governance controls, or escalation path structure → **Process Auditor**
* plan delivery phases, milestones, or dependency maps for an initiative → **Execution Planner**
* make the decision to launch or not → **Product Strategist** or organizational leadership
* perform post-launch monitoring or incident response

### Routing guidance

* If technical verification has not been completed → engage **Release Verifier** before this skill
* If active delivery is still in progress and not yet approaching launch → engage **Delivery Coordinator**
* If governance or approval structure for the launch process needs to be designed → route to **Process Auditor**
* If a launch gap surfaces a technical blocker → route to **Release Verifier**
* If a launch gap surfaces a delivery coordination problem → route to **Delivery Coordinator**
* If a launch gap surfaces an unclear requirement → route to **Requirements Analyst**

Examples:

* "Is the code ready to ship?" → **Release Verifier**
* "Stream B is still blocked" → **Delivery Coordinator**
* "Who needs to approve this release change?" → **Process Auditor**
* "Structure the delivery phases for this initiative" → **Execution Planner**
* "We're technically verified — structure the launch coordination for go-live tomorrow" → **Launch Coordinator**
* "What does support need to know before we launch?" → **Launch Coordinator**

Do not solve adjacent-skill problems here.
Flag them in **Launch Gaps** and route them.

---

## Expected inputs

Best inputs:

* description of what is launching (feature, product, release)
* current technical readiness signal (from Release Verifier if available)
* list of functions involved in the launch (engineering, support, marketing, docs, ops, comms)
* known launch date or window
* known dependencies or coordination concerns

Helpful optional inputs:

* release verification output from Release Verifier
* existing launch checklist or run-book drafts
* rollback plan if available
* deployment architecture (phased rollout, feature flags, full launch)
* communication plan if drafted
* support documentation status
* stakeholder notification requirements

If no description of what is launching is provided, ask before proceeding.
If technical verification has not been completed, flag that Release Verifier should run first and proceed with a caveat.
If the function list is unknown, proceed with a standard cross-functional launch model and note the assumption.

---

## Output format

Always use this structure.

### 0. Launch context

State:
* what is launching
* technical readiness status (verified, in progress, unknown)
* functions in scope for launch coordination
* any critical gaps in the picture

### 1. Launch readiness summary

Two to three sentences.
State the overall launch coordination signal — aligned, partially aligned, or gaps present — and the most important unresolved item.

### 2. Cross-functional readiness status

For each function involved in the launch:

* **Function** (Engineering, Support, Marketing, Docs, Ops, Comms, etc.)
* **Status**: Ready / Needs confirmation / Not ready / Unknown
* **Key action or dependency** if not ready
* **Owner** if known

### 3. Launch sequence

The ordered sequence of events at go-live:

For each step:
* **Step number and action**
* **Owner**
* **Dependency** — what must be true before this step
* **Timing signal** — before deployment / at deployment / after deployment / T+[period]

### 4. Launch gaps

List what is still unaligned, unclear, or unresolved before go-live.

For each gap:
* **Gap description**
* **Why it matters for launch coherence**
* **Who needs to act**
* **Urgency**: Must resolve before launch / Resolve day-of / Acceptable risk
* **Route to**: [Skill Name] if a specialist can help

### 5. Rollback coordination

State:
* **Rollback owner** — who makes the call and who executes it
* **Trigger conditions** — under what circumstances rollback is initiated
* **Rollback sequence** — what happens and in what order
* **Communication on rollback** — who is notified and how

If rollback plan is unavailable, flag it as a launch gap.

### 6. Communication sequence

The sequence of external and internal communications relative to deployment:

* **Before deployment**: what goes out, to whom, when
* **At deployment**: what is communicated and to whom
* **After deployment**: what follows and when

### 7. Launch verdict

One of:

* **LAUNCH-READY** — all functions aligned, sequence defined, gaps resolved
* **LAUNCH-READY WITH NOTED GAPS** — proceed with named items to monitor
* **NOT LAUNCH-READY** — list what must be resolved before go-live

---

## Behavior under ambiguity

* If technical verification has not been completed, flag this and proceed with the coordination layer — but note the launch verdict cannot be LAUNCH-READY until Release Verifier has cleared the release
* If function readiness is unknown for one or more functions, mark them as Unknown and flag them as gaps rather than assuming readiness
* If rollback ownership is undefined, flag it as a launch gap — proceed with the rest of the coordination but do not produce a LAUNCH-READY verdict when rollback is undefined
* If the launch date is unknown, structure the sequence in relative terms (T-minus, at deployment, T+) rather than absolute times
* If a launch gap surfaces a technical problem, route to Release Verifier rather than absorbing it here

Do not produce a LAUNCH-READY verdict when critical gaps remain.
Do not assume cross-functional readiness — confirm or flag as unknown.
Do not design governance structure — coordinate against it.
Do not absorb technical verification — reference Release Verifier's output.

---

## Composition notes

This skill operates at the end of the delivery cycle, immediately before go-live. It sits between Release Verifier (technical readiness) and the launch event itself.

Typical workflow position:

1. **Execution Planner** — plans the delivery
2. **Implementation Engineer** — builds the work
3. **Delivery Coordinator** — manages delivery health during execution
4. **Release Verifier** — verifies technical readiness before launch
5. **Launch Coordinator** — coordinates the go-live event ← this skill
6. Post-launch monitoring — outside the suite

It works well:

* in the hours or days before a planned go-live
* when multiple functions need to be aligned for launch
* when the deployment involves a coordinated sequence (staged rollout, feature flags, comms timing)
* when rollback ownership is unclear
* when "we're technically ready but something feels uncoordinated"
* before any launch that involves more than one function

It should stand down when:

* technical verification is not complete (Release Verifier first)
* delivery is still actively in progress (Delivery Coordinator)
* the launch has already happened
* the launch is a single-function deployment with no cross-functional coordination needed

Typical adjacent skills:

* **Release Verifier** — must clear technical readiness before this skill produces a LAUNCH-READY verdict
* **Delivery Coordinator** — hands off to this skill when delivery approaches go-live
* **Process Auditor** — governs the approval structure this skill coordinates within
* **Execution Planner** — produced the plan this skill coordinates the end-state of
