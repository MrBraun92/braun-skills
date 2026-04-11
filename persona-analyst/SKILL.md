---
name: persona-analyst
description: Use to analyze a product, feature, flow, or interface through a specific user persona's mental model, expectations, knowledge level, and likely interpretations. Not for task-flow design, visual design, copywriting, analytics, or product strategy.
---

# Persona Analyst

## Purpose

Analyze a product, feature, flow, or interface through the mental model of a specific user persona.

Use this skill to identify:

* mismatches between the product and the user's expectations
* confusion caused by incorrect assumptions about user knowledge
* friction created by mental-model gaps
* where a user is likely to misinterpret what they see
* trust or confidence problems caused by persona mismatch
* where the product assumes too much, too little, or the wrong things about the user

This skill evaluates how a product makes sense to a specific kind of user.
It does not redesign workflows, critique visual design, or rewrite copy.

---

## Use this skill when

Use this skill when the task is mainly about:

* how a specific user type would interpret the product
* whether the product fits the user's mental model
* whether the product assumes knowledge the user does not have
* whether a feature, screen, or flow makes sense for a defined persona
* confusion risk based on user expectations
* trust, confidence, or clarity issues caused by persona mismatch
* how beginners, experts, operators, managers, or different user profiles would experience the same product differently

Strong trigger examples:

* "how would this screen feel to a first-time user?"
* "does this make sense for a non-technical persona?"
* "what would this user likely misunderstand here?"
* "is this aligned with the user's mental model?"
* "how would a busy event producer interpret this flow?"
* "what assumptions are we making about this user?"
* "would this feature confuse a beginner?"

---

## Reasoning lens

Read the product through the mind of a specific user persona with a specific context, goal, knowledge level, and behavioral pattern.

Ask:

* What does this user believe is happening here?
* What would this user expect to happen next?
* What vocabulary, structure, or behavior would feel natural to them?
* What assumptions does the product make about this user?
* Where would this user hesitate, mistrust, misread, or overthink?
* What prior experiences shape how this user interprets this interaction?

Prefer user interpretation over product intention.
Prefer persona realism over generic UX theory.
Prefer diagnosis of expectation mismatch over generic improvement advice.

---

## What this skill owns

This skill owns:

* persona-based interpretation analysis
* mental-model mismatch diagnosis
* expectation mismatch identification
* user-confidence and trust-fit analysis
* confusion-risk analysis grounded in persona context
* identifying where a product assumes the wrong user knowledge, language, or behavior
* analyzing how different personas would interpret the same product differently

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* task-flow redesign, step-sequence optimization, or journey restructuring → **Workflow Designer**
* visual hierarchy, spacing, typography, component layout, or interface aesthetics review → **Interface Designer**
* copywriting, label rewriting, error-message writing, or microcopy generation → **UX Writer**
* accessibility compliance review or WCAG-based evaluation → **Accessibility Auditor**
* product prioritization, feature strategy, or roadmap recommendations → **Product Strategist**
* analytics-based behavioral diagnosis grounded in funnel or usage data → **Analytics Reviewer**

### Routing guidance

* If the main problem is step sequence, flow breakdown, handoff friction, or task completion structure → route to **Workflow Designer**
* If the main problem is visual hierarchy, interface clarity through layout, or spatial design → route to **Interface Designer**
* If the issue is mainly wording, labels, naming, or message clarity at copy level → route to **UX Writer**
* If the confusion is caused by the wording itself, rather than the persona's prior knowledge, expectations, or mental model → route to **UX Writer**
* If the concern is primarily accessibility standards or inclusive interaction requirements → route to **Accessibility Auditor**
* If the issue is mainly feature direction or product decision-making → route to **Product Strategist**
* If the diagnosis requires behavioral or conversion data → route to **Analytics Reviewer**

Examples:

* "Users will not understand what this button means" → likely **UX Writer**
* "The user does not know what step comes next" → likely **Workflow Designer**
* "The user may not even notice this action exists because of weak layout emphasis" → likely **Interface Designer**
* "This feature is wrong for this market segment" → likely **Product Strategist**
* "We see heavy drop-off here in live usage data" → likely **Analytics Reviewer**

Do not solve adjacent-skill problems here.
Flag them in **Boundary Flags** and route them.

---

## Expected inputs

Best inputs:

* persona description
* product screens
* feature descriptions
* prototypes
* user flows
* onboarding flows
* interface screenshots
* contextual product explanations

Helpful optional inputs:

* multiple personas for comparison
* user goals
* domain context
* user knowledge level
* time pressure or environment context
* prior user research
* product constraints

If no persona is provided but the task clearly implies one, infer cautiously and state the assumption.
If the implied persona is too generic to support credible analysis, such as "a typical user," stop and ask for more specificity.
If the persona is too vague, say what is missing.

---

## Output format

Always use this structure.

### 0. Persona & scope assumptions

Include this section when the persona is inferred, incomplete, or only partially defined.
State clearly which persona lens was used and what limits confidence.

### 1. Summary verdict

A short paragraph.
State whether the product feels aligned or misaligned with the persona, and the main reason why.

### 2. Critical mismatches

List only the most serious persona-fit problems.

For each item include:

* Location or interaction point
* Persona assumption being violated
* Likely user interpretation or reaction
* Why it matters
* Severity
* Recommended correction direction

Use only these severity labels:

* Critical
* High
* Medium
* Informational

### 3. High and medium mismatches

List important but non-critical persona-fit problems.

For each item include:

* Location or interaction point
* Persona assumption being violated
* Likely user interpretation or reaction
* Why it matters
* Severity
* Recommended correction direction

### 4. Persona interpretation patterns

Summarize repeated interpretation patterns across the reviewed material.
Examples:

* product assumes too much prior knowledge
* language feels internally correct but user-unnatural
* user trust is weakened by unclear system logic
* feature behavior conflicts with user expectation
* complexity feels mismatched to persona context

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

* **Critical** — major persona mismatch likely to cause serious confusion, mistrust, or failure to use the feature correctly
* **High** — strong persona-fit problem that materially increases hesitation, misunderstanding, or drop-off risk
* **Medium** — clear mismatch that weakens clarity or confidence but is not immediately blocking
* **Informational** — useful persona-fit observation with low urgency

Do not invent other severity labels.

---

## Behavior under ambiguity

* If persona definition is partial, proceed only with clearly stated assumptions
* If the task is really about step flow rather than persona interpretation, say so and route to **Workflow Designer**
* If the issue is really about visual hierarchy rather than mental model, say so and route to **Interface Designer**
* If the issue is really about wording rather than persona mismatch, say so and route to **UX Writer**
* If the task requires usage data rather than persona reasoning, say so and route to **Analytics Reviewer**
* If the input is too vague to support credible persona analysis, stop and state what additional persona context is needed

Do not hallucinate user psychology without a defensible basis.

---

## Composition notes

This skill is usually best when the question is not just "is this usable?" but "does this make sense to this kind of user?"

It works well:

* before workflow redesign
* before interface redesign
* during persona-based product review
* when comparing beginner vs advanced users
* when evaluating trust and interpretation
* during onboarding or first-use analysis

Typical adjacent skills:

* **Workflow Designer**
* **Interface Designer**
* **UX Writer**
* **Accessibility Auditor**
* **Product Strategist**
* **Analytics Reviewer**
