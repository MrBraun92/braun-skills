---
name: interface-designer
description: 'Read this skill before giving any feedback on the visual design or layout of a screen, UI, or interface. Trigger whenever the user shares a UI and asks for critique or wants to improve visual clarity — including in Portuguese: "analise o design", "a interface está clara?", "melhore a hierarquia visual", "o layout está bom?", "como melhorar a aparência disso?". Not for mental model or persona interpretation, workflow design, copywriting, analytics, or accessibility compliance.'
---

# Interface Designer

## Purpose

Analyze or improve the visual structure of an interface at the screen and component level.

Use this skill to identify:

* weak visual hierarchy
* cluttered or unbalanced layouts
* unclear emphasis
* poor spacing and grouping
* typography problems
* component misuse
* inconsistent visual patterns
* low scannability
* interfaces that feel visually noisy, flat, or hard to parse
* where layout and emphasis make actions, status, or information harder to notice than they should be

This skill evaluates how the interface is visually organized.
It does not analyze persona psychology, redesign workflows, or rewrite copy.

---

## Use this skill when

Use this skill when the task is mainly about:

* visual hierarchy
* layout
* spacing
* typography
* emphasis
* component arrangement
* interface clarity through visual structure
* scannability
* consistency across screens or UI elements
* whether an interface looks visually balanced, readable, and easy to parse

Strong trigger examples:

* "does this screen have clear visual hierarchy?"
* "what is visually weak in this UI?"
* "why does this interface feel cluttered?"
* "is the layout guiding attention properly?"
* "what should stand out more here?"
* "is this screen easy to scan?"
* "what visual inconsistencies do you see?"
* "how should this interface be visually improved?"

---

## Reasoning lens

Read the interface as a visual communication system competing for limited user attention.

Ask:

* What draws attention first, and should it?
* Is the hierarchy clear?
* Are grouping and spacing helping comprehension?
* Do typography and component choices support clarity?
* Is the screen easy to scan quickly?
* Are important actions, states, and information visually legible?
* Is the interface calm, coherent, and intentional rather than noisy or ambiguous?

Prefer visual clarity over decorative cleverness.
Prefer strong hierarchy over equal emphasis.
Prefer scannability over density.
Prefer consistency over one-off visual decisions.

---

## What this skill owns

This skill owns:

* visual hierarchy analysis
* layout and spacing review
* typography and grouping assessment
* component emphasis judgment
* visual balance and screen composition review
* consistency analysis across interface patterns
* identifying where layout, grouping, or emphasis make the interface harder to read or act on

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* persona interpretation, mental-model analysis, or expectation mismatch diagnosis → **Persona Analyst**
* task-flow redesign, step sequencing, handoff analysis, or workflow restructuring → **Workflow Designer**
* copywriting, label rewriting, error-message writing, or microcopy generation → **UX Writer**
* accessibility compliance review, WCAG-based evaluation, keyboard navigation review, or inclusive-design standards assessment → **Accessibility Auditor**
* product prioritization, feature strategy, or roadmap recommendations → **Product Strategist**
* analytics-based diagnosis requiring usage, funnel, or conversion data → **Analytics Reviewer**

### Routing guidance

* If the main issue is how a specific user interprets or mentally models the product → route to **Persona Analyst**
* If the main issue is task sequence, flow progression, or handoff breakdown → route to **Workflow Designer**
* If the issue is mainly wording, labels, or message clarity → route to **UX Writer**
* If the concern is primarily accessibility standards or inclusive interaction requirements → route to **Accessibility Auditor**
* If the issue is mainly product direction or feature strategy → route to **Product Strategist**
* If the diagnosis requires behavioral or conversion data → route to **Analytics Reviewer**

Examples:

* "This user may not understand what this means" → **Persona Analyst**
* "The user does not know what to do next" → **Workflow Designer**
* "This label is too vague" → **UX Writer**
* "This contrast may fail accessibility requirements" → **Accessibility Auditor**
* "This feature should not be prioritized" → **Product Strategist**
* "Users are ignoring this section in production data" → **Analytics Reviewer**

Do not solve adjacent-skill problems here.
Flag them in **Boundary Flags** and route them.

---

## Expected inputs

Best inputs:

* interface screenshots
* mockups
* wireframes
* high-fidelity UI designs
* product screens
* design-system examples
* screen sequences when comparing consistency
* component states

Helpful optional inputs:

* design goals
* brand constraints
* device context
* responsive variants
* existing design system
* comparison screens
* target audience context
* product constraints

If the screen is partial, proceed with explicit limits.
If the visual context is too incomplete to judge hierarchy or layout credibly, say what is missing.

---

## Output format

Always use this structure.

### 0. Screen scope & caveats

Include this section only when the interface view is partial, ambiguous, or missing important context.
State clearly what was reviewed and what limits confidence.

### 1. Summary verdict

A short paragraph.
State whether the interface feels visually strong or weak, and the main reason why.

### 2. Critical visual issues

List only the most serious interface problems.

For each item include:

* Screen area or component
* Visual problem
* Why it matters
* Likely effect on attention, readability, or clarity
* Severity
* Recommended correction direction

Use only these severity labels:

* Critical
* High
* Medium
* Informational

### 3. High and medium visual issues

List important but non-critical interface concerns.

For each item include:

* Screen area or component
* Visual problem
* Why it matters
* Likely effect on attention, readability, or clarity
* Severity
* Recommended correction direction

### 4. Visual patterns

Summarize repeated interface patterns across the reviewed material.
Examples:

* weak primary focus
* over-dense layout
* inconsistent spacing rhythm
* too many competing elements
* flat hierarchy
* unclear grouping
* inconsistent component emphasis

Do not repeat findings already listed above.

### 5. Boundary flags

List issues noticed that belong primarily to another skill.

Format:

* Screen area or component → Observation → Route to: [Skill Name]

This section may be empty.

### 6. Priority order

End with:

1. Fix first
2. Fix next
3. Safe to defer

---

## Severity scale

Use this scale exactly:

* **Critical** — major interface problem likely to block recognition of key information or actions, or severely damage visual clarity
* **High** — strong visual issue that materially weakens hierarchy, readability, or attention guidance
* **Medium** — clear interface weakness that reduces scannability or polish but is not severely damaging
* **Informational** — useful visual observation with low urgency

Do not invent other severity labels.

---

## Behavior under ambiguity

* If the visual sample is partial, proceed only with clearly stated limits
* If the issue is really about persona expectations rather than layout or emphasis, say so and route to **Persona Analyst**
* If the issue is really about workflow sequence rather than visual structure, say so and route to **Workflow Designer**
* If the issue is really about wording rather than interface design, say so and route to **UX Writer**
* If the task requires accessibility-standard analysis rather than general interface critique, say so and route to **Accessibility Auditor**
* If the input is too incomplete to support credible interface analysis, stop and state what additional visual context is needed

Do not hallucinate full design-system conclusions from a narrow sample.

---

## Composition notes

This skill is usually best when the question is not just "is this usable?" but "is this visually clear, legible, and well-organized?"

It works well:

* before interface redesign
* during design critique
* when improving screen clarity
* when reviewing hierarchy and emphasis
* when comparing consistency across UI patterns
* before accessibility review

Typical adjacent skills:

* **Persona Analyst**
* **Workflow Designer**
* **UX Writer**
* **Accessibility Auditor**
* **Product Strategist**
* **Analytics Reviewer**
