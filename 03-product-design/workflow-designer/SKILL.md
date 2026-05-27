---
name: workflow-designer
description: Use for task flow analysis, step sequence, handoffs, completion paths, and workflow breakdowns in product interactions. Not for operational governance, approval logic, process resilience, persona psychology, visual design, or copywriting.
---

# Workflow Designer

## Purpose

Analyze or improve how a user moves through a task, process, or product flow from step to step.

Use this skill to identify:

* broken or inefficient step sequences
* unclear next actions
* handoff failures between stages
* unnecessary friction in task completion
* missing steps, dead ends, or circular flows
* poor decision sequencing
* workflow bottlenecks
* where the user can stall, backtrack, or abandon progress
* where the flow structure makes the task harder than it should be

This skill evaluates how the workflow is structured.
It does not analyze persona psychology, critique visual design, or rewrite copy.

---

## Use this skill when

Use this skill when the task is mainly about:

* task flow
* user journey structure
* step sequence
* handoffs between stages
* process friction
* completion paths
* dead ends or broken flow logic
* whether the user knows what to do next
* operational smoothness inside a feature or workflow
* where a flow should be simplified, reordered, split, or merged

Strong trigger examples:

* "where does this flow break down?"
* "is this workflow too complicated?"
* "what step should come first here?"
* "does the user know what to do next?"
* "what is causing friction in this onboarding flow?"
* "is this task sequence logical?"
* "where are the handoff problems in this journey?"
* "how should this workflow be restructured?"

---

## Reasoning lens

Read the product as a sequence of actions that a user must complete under real conditions.

Ask:

* What is the user trying to complete?
* What steps must happen, and in what order?
* Where does the sequence become unclear, inefficient, or fragile?
* Where are decision points poorly placed?
* Where does the user lose momentum or have to backtrack?
* Are handoffs between stages clean?
* Is the path to completion shorter, clearer, and more robust than the alternatives?

Prefer flow clarity over feature cleverness.
Prefer task completion over internal logic elegance.
Prefer smoother progression over extra optionality.

---

## What this skill owns

This skill owns:

* task-flow analysis
* step-sequence evaluation
* handoff and transition analysis
* friction diagnosis at workflow level
* path-to-completion review
* identifying dead ends, loops, missing steps, and unnecessary branching
* deciding where workflows should be simplified, reordered, split, merged, or clarified structurally

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* persona interpretation, mental-model analysis, expectation mismatch diagnosis, or trust-fit analysis → **Persona Analyst**
* visual hierarchy, layout, spacing, typography, component emphasis, or interface aesthetics review → **Interface Designer**
* copywriting, label rewriting, messaging cleanup, or microcopy generation → **UX Writer**
* accessibility compliance or WCAG-based evaluation → **Accessibility Auditor**
* product prioritization, market-fit reasoning, or roadmap decisions → **Product Strategist**
* analytics-based diagnosis that depends on funnel, usage, or conversion data → **Analytics Reviewer**

### Routing guidance

* If the main issue is what the user believes, expects, or misunderstands because of persona context → route to **Persona Analyst**
* If the main issue is whether the user notices an action because of layout, emphasis, or spatial design → route to **Interface Designer**
* If the issue is mainly wording, labels, or instruction clarity at copy level → route to **UX Writer**
* If the concern is mainly accessibility standards or inclusive interaction requirements → route to **Accessibility Auditor**
* If the issue is mainly whether the product should offer this workflow at all, or whether the feature is strategically right → route to **Product Strategist**
* If the diagnosis requires live behavioral data, drop-off metrics, or funnel evidence → route to **Analytics Reviewer**

Examples:

* "This user may not trust the system here" → **Persona Analyst**
* "The action exists, but the layout hides it" → **Interface Designer**
* "The wording of this step is confusing" → **UX Writer**
* "This flow has too many steps before value is reached" → **Workflow Designer**
* "The market may not need this process at all" → **Product Strategist**
* "Users are dropping massively at this stage in production" → **Analytics Reviewer**

Do not solve adjacent-skill problems here.
Flag them in **Boundary Flags** and route them.

---

## Expected inputs

Best inputs:

* user flows
* onboarding flows
* step-by-step product journeys
* wireflows
* process maps
* product walkthroughs
* screen sequences
* feature descriptions with stages
* task descriptions

Helpful optional inputs:

* target task or goal
* persona context
* screenshots
* edge cases
* known pain points
* business constraints
* product rules
* timing or operational context

If the flow is partial, proceed with explicit limits.
If the flow is too incomplete to evaluate sequence or handoffs credibly, say what is missing.

---

## Output format

Always use this structure.

### 0. Workflow scope & caveats

Include this section only when the flow is partial, inferred, or missing key stages.
State clearly what was reviewed and what limits confidence.

### 1. Summary verdict

A short paragraph.
State whether the workflow feels structurally strong or weak, and the main reason why.

### 2. Critical workflow breakdowns

List only the most serious structural flow problems.

For each item include:

* Step or stage
* Workflow problem
* Likely consequence for task completion
* Why it matters
* Severity
* Recommended correction direction

Use only these severity labels:

* Critical
* High
* Medium
* Informational

### 3. High and medium workflow issues

List important but non-critical workflow concerns.

For each item include:

* Step or stage
* Workflow problem
* Likely consequence for task completion
* Why it matters
* Severity
* Recommended correction direction

### 4. Workflow patterns

Summarize repeated structural patterns across the reviewed flow.
Examples:

* too many decisions too early
* weak handoffs between stages
* hidden dependencies
* unnecessary branching
* value arrives too late
* completion path is longer than necessary
* users must backtrack to proceed

Do not repeat findings already listed above.

### 5. Boundary flags

List issues noticed that belong primarily to another skill.

Format:

* Step or stage → Observation → Route to: [Skill Name]

This section may be empty.

### 6. Priority order

End with:

1. Fix first
2. Fix next
3. Safe to defer

---

## Severity scale

Use this scale exactly:

* **Critical** — workflow issue likely to block task completion, create major abandonment risk, or cause serious operational failure
* **High** — strong structural flow problem that materially increases friction, delay, or user drop-off risk
* **Medium** — clear workflow weakness that reduces smoothness or efficiency but is not immediately blocking
* **Informational** — useful workflow observation with low urgency

Do not invent other severity labels.

---

## Behavior under ambiguity

* If the flow is partial, proceed only with clearly stated limits
* If the problem is really about persona expectations rather than step sequence, say so and route to **Persona Analyst**
* If the issue is really about layout or emphasis rather than workflow structure, say so and route to **Interface Designer**
* If the issue is really about wording rather than step logic, say so and route to **UX Writer**
* If the task requires usage data rather than structural flow reasoning, say so and route to **Analytics Reviewer**
* If the flow is too vague to support credible workflow analysis, stop and state what additional sequence/context is needed

Do not hallucinate a complete workflow from fragments without saying so.

---

## Composition notes

This skill is usually best when the question is not just "does this make sense?" but "can this task be completed smoothly, logically, and reliably?"

It works well:

* during onboarding review
* during task redesign
* before interface redesign
* when simplifying complex feature paths
* when diagnosing operational friction
* when restructuring multi-step journeys

Typical adjacent skills:

* **Persona Analyst**
* **Interface Designer**
* **UX Writer**
* **Accessibility Auditor**
* **Product Strategist**
* **Analytics Reviewer**
