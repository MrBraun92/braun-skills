---
name: audit-orchestrator
description: 'Read this skill before conducting any broad, multi-dimensional review of a product, system, or initiative. Trigger whenever the user asks to "review everything", "audit the whole product", "give me a full picture", wants findings consolidated across multiple specialist lenses, OR uses meta-language about using skills — "use suas skills", "use your skills", "use all available skills", "faça com todas as skills", "use o máximo de skills possível", "trabalhe com suas capacidades completas". Not for single-skill reviews, isolated strategy questions, or standalone specialist analysis.'
---

# Audit Orchestrator

## Purpose

Coordinate multi-skill product audits and synthesize specialist findings into a single prioritized output.

Use this skill to:

* decide which specialist skills are relevant for a given audit scope
* sequence specialist skill invocations in a logical order
* apply each relevant specialist lens to the product, feature, or system under review
* consolidate findings across all applied skills into one unified output
* remove duplicate observations that appear across multiple specialist outputs
* normalize severity labels across skills into a consistent priority order
* surface the highest-priority findings across the full audit
* identify where further specialist review is still needed after the audit
* produce one coherent, actionable audit output instead of fragmented specialist reports

This skill coordinates and synthesizes. It does not generate specialist findings independently — it directs the right specialists and merges their outputs.

---

## Use this skill when

Use this skill when the task requires:

* a comprehensive audit across multiple product dimensions simultaneously
* consolidation of findings from more than one specialist skill
* a single prioritized output from a multi-lens review
* coordination of engineering, UX, product, and process review in one audit
* a complete picture of risks and opportunities rather than a single-dimension view

Strong trigger examples:

* "do a full product audit"
* "give me a comprehensive review of this product"
* "audit this product across all relevant dimensions"
* "I want a complete picture of what is wrong with this product"
* "run a multi-skill audit on this feature"
* "what are the biggest risks across engineering, UX, and product?"
* "give me one consolidated audit output"
* "review this from every relevant angle and tell me what to fix first"
* "I need a full audit, not just one perspective"

---

## Do not use this skill when

Do not use this skill when the task is cleanly handled by one specialist:

* "Review this code" → **Code Auditor**
* "What should we build next?" → **Product Strategist**
* "Analyze our competitor" → **Competitive Reviewer**
* "Is this skill ready to install?" → **Skill Auditor**
* "What does our analytics data show?" → **Analytics Reviewer**
* "Is this interface visually clear?" → **Interface Designer**
* Any request that names one dimension → invoke that specialist directly

The orchestrator adds value only when multiple specialist lenses are genuinely needed and their findings need to be merged. If one specialist covers the request cleanly, use that specialist.

---

## Reasoning lens

Read the audit scope as a multi-dimensional system that must be examined through the right set of specialist lenses, in a sensible order, with findings merged into one coherent output.

Ask:

* What is the full scope of what needs to be audited?
* Which specialist lenses are genuinely relevant — and which would add noise?
* What is the right sequence for applying these lenses?
* Where do findings from different specialists overlap or contradict?
* What is the consolidated priority order across all findings?
* What is still unknown or under-examined after this audit?
* What should the reader act on first, and why?

Prefer focused specialist selection over exhaustive invocation of every skill.
Prefer clear synthesis over preserving all raw specialist output.
Prefer honest uncertainty over false completeness.
Prefer one actionable priority order over multiple ranked lists.

---

## What this skill owns

This skill owns:

* specialist skill selection for a given audit scope
* audit sequencing logic
* cross-skill finding consolidation
* duplication removal across specialist outputs
* severity normalization across the full finding set
* final priority ordering across all audit findings
* identification of remaining audit gaps after synthesis
* production of one unified audit output

This skill does not own the specialist findings themselves. Each finding originates from a specialist skill. The orchestrator synthesizes, not generates.

---

## Available specialist skills

The orchestrator selects from the installed specialist suite. Current suite:

**Engineering cluster:**
Code Auditor · Code Architect · Data Modeler · Test Strategist · Security Reviewer · Performance Reviewer · Implementation Engineer

**UX cluster:**
Persona Analyst · Workflow Designer · Interface Designer · UX Writer · Accessibility Auditor

**Product cluster:**
Product Strategist · Analytics Reviewer · Competitive Reviewer · Process Auditor

**Meta skills:**
Skill Auditor · Prompt Engineer · Audit Orchestrator

When selecting specialists for an audit, choose only those whose lens is genuinely relevant to the scope. Do not invoke all skills by default.

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* generate specialist findings independently without invoking the relevant skill
* make product prioritization decisions → **Product Strategist**
* perform competitive analysis → **Competitive Reviewer**
* govern skill quality → **Skill Auditor**
* reframe vague requests before routing → **Prompt Engineer**
* act as a generalist product reviewer that absorbs all specialist work
* produce findings that duplicate what a single specialist would produce — if one specialist covers the request, use that specialist directly

### Routing guidance

* If the request is clearly handled by one specialist skill → route directly to that specialist without invoking the orchestrator
* If the audit produces strategic recommendations about what to build → surface findings here, route decisions to **Product Strategist**
* If the audit reveals a need for competitive context → flag it and invoke **Competitive Reviewer** as part of the audit scope
* If the request is too vague to scope the audit — flag it and invoke **Prompt Engineer** before beginning

Examples:

* "Review this code for maintainability" → **Code Auditor** directly
* "Do a full audit of our onboarding flow" → **Audit Orchestrator** (multi-skill: Workflow Designer, Persona Analyst, UX Writer, Interface Designer)
* "What should we cut from our roadmap?" → **Product Strategist** directly
* "Audit this product end to end and tell me the biggest risks" → **Audit Orchestrator**
* "Is this skill ready to install?" → **Skill Auditor** directly

---

## Expected inputs

Best inputs:

* product description or scope definition
* feature, flow, or system to audit
* audit focus area (e.g., onboarding, checkout, settings, API, dashboard)
* known concerns or suspected problem areas
* list of dimensions to cover (or instruction to select automatically)

Helpful optional inputs:

* existing specialist findings to incorporate
* tech stack context
* user type or persona context
* recent changes or releases
* business goals or constraints
* time or depth constraints for the audit

If the audit scope is too vague to select specialists, ask for clarification before proceeding.
If the user specifies which specialists to include, respect that selection.
If the user asks for a full audit with no scope constraint, select specialists based on what the product description makes relevant.

---

## Output format

Always use this structure.

### 0. Audit scope & specialist selection

State:
* what is being audited
* which specialist skills were selected and why
* which specialist skills were excluded and why
* any scope limitations

### 1. Executive summary

Two to four sentences.
State the dominant risk, the most important opportunity, and the overall audit signal.

### 2. Consolidated findings

Present findings from all specialists in a unified list, not separated by skill.
De-duplicate observations that appeared across multiple specialists.
Tag each finding with the originating skill(s).

For each finding include:

* Area or component
* Finding
* Why it matters
* Originating skill(s)
* Priority level

Use only these priority labels:

* **P0** — critical: address immediately
* **P1** — high: address before next release or major milestone
* **P2** — medium: address in the near term
* **P3** — informational: low urgency, monitor or defer

### 3. Priority order

Flat ranked list across all findings.

1. Address first
2. Address next
3. Address soon
4. Safe to defer

No sub-lists by skill. One unified order.

### 4. Remaining audit gaps

List areas that were not covered or could not be fully assessed.

For each gap include:

* Area not covered
* Why it was not covered
* Recommended next step

### 5. Boundary flags

List findings that belong to a skill outside the invoked set, or require action that goes beyond audit scope.

Format:

* Area → Observation → Route to: [Skill Name]

---

## Behavior under ambiguity

* If the audit scope is too vague to select specialists, stop and ask — do not invoke all skills by default
* If the user names a specific set of specialists, use that set; do not substitute
* If only one specialist is relevant, say so and route directly — do not wrap a single-skill review in orchestration overhead
* If findings from different specialists directly contradict each other, surface the contradiction explicitly rather than silently resolving it
* If a finding requires specialist depth beyond what this audit produced, flag it as a remaining gap
* If the input is too thin to support a meaningful multi-skill audit, state what additional context is needed

Do not hallucinate specialist findings.
Do not silently generate findings without specialist grounding.
Do not produce false completeness when coverage is partial.

---

## Composition notes

This skill sits above the specialist layer and below the strategic decision layer. Its job is coordination and synthesis, not analysis or strategy.

Feed order in a full product workflow:

1. **Audit Orchestrator** — identifies what is wrong and at what priority
2. **Product Strategist** — decides what to do about it
3. **Specialist skills** — execute on specific fix directions

It works well:

* at the start of a product improvement cycle
* before a major release or milestone review
* when multiple problems are suspected across different dimensions
* when fragmented specialist outputs need to be unified
* when a single prioritized action list is needed across all dimensions

It should stand down when:

* the request is clearly handled by one specialist
* the audit scope is too narrow to justify multi-skill coordination
* the user wants strategic decisions rather than diagnostic findings

Typical adjacent skills:

* **Product Strategist** — receives audit findings and makes prioritization decisions
* **Competitive Reviewer** — may be included as one of the audit lenses
* **Skill Auditor** — governs this skill's own quality as a suite component
* All specialist skills — invoked by this skill as needed
