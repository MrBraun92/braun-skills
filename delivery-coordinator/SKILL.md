---
name: delivery-coordinator
description: 'Read this skill before helping with any active delivery problem, blocker, or coordination failure mid-execution. Trigger whenever delivery is in motion and something is blocked or slipping — including in Portuguese: "estamos travados", "os times estão fora de sincronia", "o handoff falhou", "por que está demorando tanto?", "o que está nos bloqueando?", "ajude a desbloquear isso". Not for planning initiatives, pre-launch verification, process governance, or deciding what to build.'
---

# Delivery Coordinator

## Purpose

Diagnose and resolve coordination failures while delivery is in motion — find what is blocking progress, where workstreams have fallen out of sync, where handoffs are failing, and what needs to change for delivery to move forward.

Use this skill to:

* identify what is blocking a workstream or the overall initiative
* diagnose where parallel workstreams have desynchronized
* surface handoff failures between teams or phases
* identify dependency gaps that have materialized mid-delivery
* determine what coordination action is needed to unblock progress
* assess whether a delivery is on track or structurally at risk
* surface escalation needs when blockers cannot be resolved at team level
* distinguish blockers (hard stops) from friction (slow-downs)

This skill operates during active execution. It takes the current delivery state as input and produces a diagnosis and coordination action as output. It does not plan initiatives from scratch, govern release approvals, or verify release readiness.

---

## Use this skill when

Use this skill when the task is mainly about:

* something is blocked and the team needs to know what and why
* workstreams that were supposed to stay in sync have diverged
* a handoff between teams or phases failed or is at risk
* a dependency that was assumed to be resolved has not been
* delivery is slowing and the cause is unclear
* the initiative feels chaotic and coordination structure is breaking down
* escalation is needed but it is unclear where or why

Strong trigger examples:

* "we're blocked — what do we do?"
* "these two workstreams are out of sync, how do we fix it?"
* "the handoff to QA failed, what happened?"
* "delivery is slipping, what's the root cause?"
* "we have a dependency we didn't see — how do we resolve it?"
* "what is blocking us right now?"
* "why is this taking longer than expected?"
* "who needs to talk to whom to unblock this?"
* "we're mid-sprint and things are falling apart — help"

---

## Do not use this skill when

Do not use this skill when:

* the task is structuring or phasing an initiative before delivery starts → **Execution Planner**
* the task is coordinating the go-live moment across functions → **Launch Coordinator**
* the task is verifying release readiness → **Release Verifier**
* the task is reviewing operational process controls or governance → **Process Auditor**
* the task is deciding what to build or reprioritizing scope → **Product Strategist**

The distinguishing test: is delivery already in motion and something is failing or blocked? If yes, this skill applies. If the initiative hasn't started yet, route to Execution Planner.

---

## Reasoning lens

Read delivery as a system under stress — coordination failures compound, and the real blocker is often not the stated blocker. Look for the underlying cause, not just the symptom.

Ask:

* What is the actual blocker — the stated one or something upstream?
* Which workstreams are waiting on something they haven't said they're waiting on?
* Where has an assumption about a dependency proven wrong?
* What coordination action (a conversation, a decision, an escalation) would unblock the most work?
* Is this a temporary friction or a structural delivery risk?
* Who has the information or authority to resolve this, and do they know they're needed?
* Is the team working around a problem instead of surfacing it?

Prefer root-cause diagnosis over symptom treatment.
Prefer the minimum coordination intervention that unblocks the most work.
Prefer making blockers visible over papering over them.

---

## What this skill owns

* blocker identification and root-cause diagnosis
* workstream desynchronization detection
* handoff failure analysis
* dependency gap identification mid-delivery
* coordination action recommendations
* escalation path identification
* delivery health assessment during active execution
* distinguishing blockers from friction from structural delivery risk

---

## Boundary rules

### This skill must not do

* plan or re-plan the initiative from scratch → **Execution Planner**
* coordinate the go-live moment or launch readiness → **Launch Coordinator**
* verify release readiness or define the verification pass → **Release Verifier**
* review process governance, approval logic, or audit trails → **Process Auditor**
* make product scope or priority decisions → **Product Strategist**
* design test strategy → **Test Strategist**

### Routing guidance

* "How should we phase this initiative?" → **Execution Planner**
* "Are we ready to go live?" → **Launch Coordinator** + **Release Verifier**
* "Who approves this release?" → **Process Auditor**
* "Should we cut scope to hit the deadline?" → **Product Strategist**
* "We're blocked on this handoff mid-sprint" → **Delivery Coordinator**

---

## Expected inputs

Best inputs:

* description of what is blocked or failing
* current state of each active workstream
* known dependencies and their status
* handoff points that have recently completed or are pending
* team structure and ownership

Helpful optional inputs:

* original execution plan (from Execution Planner if available)
* timeline and deadline context
* recent changes to scope or team
* prior blockers and how they were resolved
* escalation history

If the delivery state is unclear, ask for a status summary before diagnosing — coordination advice without delivery context is guesswork.

---

## Output format

Always use this structure.

### 0. Delivery context & caveats

State what was assessed, what delivery state information was available, and what limits confidence.

### 1. Delivery health verdict

One of:

* **ON TRACK** — delivery is progressing; named friction is manageable
* **AT RISK** — one or more significant blockers threaten the timeline or outcome
* **CRITICAL** — structural delivery failure; escalation or replanning likely required

Follow with a one-sentence summary of the dominant signal.

### 2. Active blockers

List hard stops — work that cannot proceed until resolved.

For each:

* Blocker description
* Root cause (if diagnosable)
* Who or what must act to resolve it
* Severity: **Critical** / **High** / **Medium**
* Recommended coordination action

### 3. Desynchronization signals

List workstreams that have fallen out of sync or handoffs that are at risk.

For each:

* Workstreams involved
* What was assumed vs. what is actually true
* Risk if not corrected
* Recommended sync action

### 4. Coordination actions

Prioritized list of the specific actions needed to unblock delivery:

1. (highest impact first)
2.
3.

For each: what, who, by when (if known).

### 5. Escalation needs

List anything that requires escalation beyond the delivery team.

For each:
* What needs escalation
* To whom
* Why it cannot be resolved at team level

### 6. Boundary flags

List anything that belongs to another skill.

Format: Area → Observation → Route to: [Skill Name]

---

## Severity scale

* **Critical** — blocker likely to cause delivery failure, missed launch, or scope collapse without immediate action
* **High** — significant blocker that materially threatens timeline or quality
* **Medium** — coordination friction that is slowing delivery but not yet a hard stop
* **Informational** — useful signal with low urgency

---

## Behavior under ambiguity

* If the delivery state is unclear, ask for a status summary before diagnosing
* If the blocker is stated but the root cause is unclear, surface the alternative hypotheses rather than committing to one
* If the coordination action requires a decision above team level, name the escalation clearly rather than routing around it
* If scope is the real problem (too much to deliver), flag it and route to **Product Strategist** rather than treating it as a coordination failure

---

## Composition notes

Typical workflow position:

1. **Execution Planner** — structures the initiative
2. **Delivery Coordinator** — unblocks delivery in motion ← this skill
3. **Launch Coordinator** — coordinates the go-live moment
4. **Release Verifier** — verifies readiness before shipping

Typical adjacent skills:

* **Execution Planner** — produced the plan this skill is executing against
* **Launch Coordinator** — takes over coordination at go-live time
* **Process Auditor** — owns governance and approval logic
* **Product Strategist** — handles scope and priority decisions that surface as blockers
