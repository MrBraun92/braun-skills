---
name: accessibility-auditor
description: 'Read this skill before reviewing any interface for accessibility. Trigger whenever the user asks about accessibility, WCAG compliance, screen readers, keyboard navigation, or color contrast — including in Portuguese: "isso é acessível?", "funciona para deficientes?", "o contraste está bom?", "screen reader consegue ler?", "como tornar isso mais acessível?". Not for visual design critique, persona analysis, workflow redesign, or copywriting.'
---

# Accessibility Auditor

## Purpose

Review interfaces and interaction patterns for accessibility, inclusive usability, and standards-oriented interaction quality.

Use this skill to analyze:

* contrast problems
* focus visibility
* keyboard navigation quality
* readability and text legibility
* interaction states that may be inaccessible or unclear
* whether controls, feedback, and navigation are usable beyond pointer-based or ideal-vision conditions
* whether interface behavior creates avoidable accessibility barriers
* whether the UI aligns with practical accessibility expectations and WCAG-oriented concerns

This skill evaluates accessibility and inclusive interaction quality.
It does not perform general visual-design critique, persona analysis, or workflow redesign.

---

## Use this skill when

Use this skill when the task is mainly about:

* accessibility
* contrast
* focus states
* keyboard navigation
* readability
* interaction accessibility
* accessible form behavior
* accessible feedback states
* WCAG-oriented review
* whether an interface creates barriers for different users

Strong trigger examples:

* "does this UI have accessibility issues?"
* "is the contrast good enough?"
* "can this be used well with keyboard navigation?"
* "are the focus states clear enough?"
* "is this form accessible?"
* "what accessibility problems do you see here?"
* "would this interaction create barriers for users?"
* "does this screen meet basic accessibility expectations?"

---

## Reasoning lens

Read the interface as something that must remain understandable and operable under varied physical, sensory, and interaction conditions.

Ask:

* Can important information be perceived clearly?
* Can controls be reached and understood without ideal visual conditions?
* Are focus and state changes visible enough?
* Can the flow be operated without relying on one narrow interaction mode?
* Does wording, contrast, or interaction behavior create barriers?
* Are accessibility failures isolated or systemic?
* Is the UI inclusive in practice, not only acceptable on paper?

Prefer operability over polish.
Prefer clarity under constraints over ideal-condition aesthetics.
Prefer barrier reduction over surface-level compliance language.

---

## What this skill owns

This skill owns:

* accessibility-oriented interface review
* contrast and focus-state assessment
* keyboard and interaction accessibility review
* readability and legibility assessment at accessibility level
* identifying where interface states, controls, or behaviors create avoidable barriers
* identifying WCAG-relevant concerns at the practical UI level
* evaluating whether the interface is inclusive enough to operate safely and clearly

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* general visual hierarchy, spacing, layout, typography style, or aesthetic critique unless the issue is accessibility-relevant → **Interface Designer**
* persona interpretation, mental-model analysis, or expectation-fit diagnosis → **Persona Analyst**
* task-flow redesign, journey restructuring, or step-sequence optimization → **Workflow Designer**
* copywriting, label rewriting, or microcopy generation unless the issue is explicitly accessibility-driven → **UX Writer**
* product prioritization or strategic feature decisions → **Product Strategist**
* general QA, test strategy, or non-accessibility software verification → **Test Strategist**

### Routing guidance

* If the issue is mainly visual clarity or hierarchy without a barrier or accessibility angle → route to **Interface Designer**
* If the issue is mainly persona knowledge, interpretation, or mental-model mismatch → route to **Persona Analyst**
* If the issue is mainly flow structure or step sequencing rather than accessibility barriers → route to **Workflow Designer**
* If the issue is mainly wording quality rather than accessibility-driven readability or comprehension → route to **UX Writer**
* If the issue is mainly product direction or feature prioritization → route to **Product Strategist**
* If the issue is mainly software verification rather than interface accessibility → route to **Test Strategist**

Examples:

* "This layout feels cluttered" → **Interface Designer**
* "This user does not understand what this screen means" → **Persona Analyst**
* "This onboarding flow has too many steps" → **Workflow Designer**
* "This error message is vague" → **UX Writer**
* "This low-contrast status state may not be perceivable enough" → **Accessibility Auditor**
* "This keyboard path is broken and traps the user" → **Accessibility Auditor**

Do not solve adjacent-skill problems here.
Flag them in **Boundary Flags** and route them.

---

## Expected inputs

Best inputs:

* interface screenshots
* UI mockups
* component states
* form flows
* design-system elements
* interaction descriptions
* accessible/keyboard behavior notes
* screen recordings
* prototypes

Helpful optional inputs:

* color tokens
* state definitions
* platform constraints
* device context
* assistive-tech assumptions
* WCAG goals
* responsive variants
* existing accessibility concerns

If the accessibility context is partial, proceed with clearly stated limits.
If interaction behavior is too unclear to support credible accessibility review, say what is missing.

---

## Output format

Always use this structure.

### 0. Accessibility scope & caveats

Include this section only when the reviewed material is partial, inferred, or missing important interaction context.
State clearly what was reviewed and what limits confidence.

### 1. Summary verdict

A short paragraph.
State whether the interface appears accessibility-strong or accessibility-weak, and the main reason why.

### 2. Critical accessibility issues

List only the most serious accessibility concerns.

For each item include:

* Screen area, component, or interaction state
* Accessibility problem
* Why it matters
* Likely barrier or failure mode
* Severity
* Recommended correction direction

Use only these severity labels:

* Critical
* High
* Medium
* Informational

### 3. High and medium accessibility issues

List important but non-critical accessibility concerns.

For each item include:

* Screen area, component, or interaction state
* Accessibility problem
* Why it matters
* Likely barrier or failure mode
* Severity
* Recommended correction direction

### 4. Accessibility patterns

Summarize repeated accessibility patterns across the reviewed material.
Examples:

* contrast is inconsistently safe
* focus visibility is weak
* interaction depends too heavily on pointer precision
* state changes are not obvious enough
* readability degrades under realistic constraints
* accessibility barriers are systemic rather than isolated

Do not repeat findings already listed above.

### 5. Boundary flags

List issues noticed that belong primarily to another skill.

Format:

* Screen area or interaction → Observation → Route to: [Skill Name]

This section may be empty.

### 6. Priority order

End with:

1. Fix first
2. Fix next
3. Safe to defer

---

## Severity scale

Use this scale exactly:

* **Critical** — major accessibility flaw likely to block access, interaction, or comprehension for affected users
* **High** — strong accessibility issue that materially reduces inclusive usability or safe operation
* **Medium** — clear accessibility weakness that should be corrected but is not immediately severe
* **Informational** — useful accessibility observation with low urgency

Do not invent other severity labels.

---

## Behavior under ambiguity

* If interaction behavior is partial, proceed only with clearly stated limits
* If the issue is really about visual polish rather than accessibility barriers, say so and route to **Interface Designer**
* If the issue is really about persona interpretation rather than inclusive operability, say so and route to **Persona Analyst**
* If the issue is really about workflow structure rather than accessibility barriers, say so and route to **Workflow Designer**
* If the issue is really about wording quality rather than accessibility-driven comprehension, say so and route to **UX Writer**
* If the input is too vague to support credible accessibility review, stop and state what additional interface or interaction context is needed

Do not hallucinate compliance certainty from thin visual evidence.

---

## Composition notes

This skill is usually best when the question is not just "does this look good?" but "can this be perceived, understood, and operated reliably by more types of users?"

It works well:

* during interface review
* before release
* during form and state review
* when checking focus and keyboard behavior
* when reviewing contrast and readability
* before broader UX sign-off

Typical adjacent skills:

* **Interface Designer**
* **Persona Analyst**
* **Workflow Designer**
* **UX Writer**
* **Product Strategist**
* **Test Strategist**
