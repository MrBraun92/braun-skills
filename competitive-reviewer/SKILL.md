---
name: competitive-reviewer
description: 'Read this skill before analyzing any competitor or adjacent product. Trigger whenever the user asks how a competitor works, what features a rival has, or how the product compares to alternatives — including in Portuguese: "como o concorrente faz isso?", "o que X tem que a gente não tem?", "compare com Y", "onde estamos atrás da concorrência?", "análise competitiva". Not for market sizing, internal product strategy, your own analytics, general internet research, or broader market trend and category signal interpretation.'
---

# Competitive Reviewer

## Purpose

Analyze competing and adjacent products as structured product references.

Use this skill to examine:

* feature scope and coverage of direct competitors or substitutes
* UX and interaction patterns used by competing products
* workflow structure and operational logic in adjacent tools
* differentiation gaps between your product and competitors
* overbuilt and underbuilt areas relative to the competitive landscape
* positioning signals observable from product structure, packaging, and feature emphasis
* opportunities or blind spots that the competitive landscape reveals
* how a specific competitor approaches a problem your product also addresses

This skill produces structured product comparison and competitive signal extraction.
It does not perform market sizing, financial analysis, internal strategy decisions, or general internet research with no defined product comparison target.

---

## Use this skill when

Use this skill when the task is mainly about:

* comparing your product to one or more competitors
* understanding what a specific competitor does or how it works
* identifying feature gaps or overlaps with the competitive landscape
* analyzing how a competitor has structured a workflow or UX pattern
* finding where the market is overbuilt or underbuilt relative to your product
* surfacing differentiation opportunities from product-level observation
* understanding a competitor's product scope and positioning signals

Strong trigger examples:

* "how does our product compare to [Competitor]?"
* "what features does [Competitor] have that we don't?"
* "analyze the onboarding flow of [Competitor]"
* "what are the main differences between us and [adjacent tool]?"
* "where are we underbuilt compared to what's available?"
* "what do our direct competitors do better in this area?"
* "compare our workflow to [Competitor]'s workflow"
* "what is [Competitor]'s product scope and how does it differ from ours?"
* "what opportunities does the competitive landscape reveal?"
* "which competitors have solved this problem and how?"

---

## Reasoning lens

Read competing products as structured product references — examine how they have made choices about scope, workflow, UX, and positioning, and what those choices reveal relative to your comparison target.

Ask:

* What has this product chosen to include, exclude, or emphasize?
* How does this product structure the workflow for the problem it solves?
* Where does this product invest more or less than expected?
* What does the feature set and UX pattern reveal about the product's primary user and primary use case?
* Where is there a meaningful gap between what competitors offer and what your product offers?
* Is the gap a real opportunity, or is it absent because it is intentionally out of scope for that product?
* What does the competitive landscape collectively suggest is solved, unsolved, or poorly solved?

Prefer product-level observation over brand-level commentary.
Prefer specific feature and workflow analysis over vague impressions.
Prefer evidence of differentiation over opinion about quality.
Prefer calibrated opportunity identification over competitive alarmism.

---

## What this skill owns

This skill owns:

* direct competitor feature scope analysis
* adjacent and substitute product comparison
* UX and interaction pattern comparison across products
* workflow and operational logic comparison
* differentiation gap identification
* overbuilt and underbuilt area identification relative to the competitive set
* positioning signal extraction from product structure and feature emphasis
* opportunity surfacing grounded in observable product evidence
* high-level packaging and pricing structure as product signals (not financial modeling)

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* internal product prioritization, roadmap decisions, or feature-worth judgment → **Product Strategist**
* analysis of your own product's usage, funnel, or behavioral data → **Analytics Reviewer**
* visual design critique of your own interface → **Interface Designer**
* persona-based mental model or expectation analysis → **Persona Analyst**
* general market sizing, TAM/SAM/SOM analysis, or industry landscape reports
* financial analysis, revenue modeling, or investor-grade competitive intelligence
* marketing messaging, brand strategy, or sales enablement content
* deep pricing strategy or pricing optimization (flag as out of scope or future skill)
* general internet research with no specific product comparison target

### Routing guidance

* If the task is mainly about deciding what to build based on competitive insight → surface the insight here, then route the decision to **Product Strategist**
* If the task is about what your own product's data shows → route to **Analytics Reviewer**
* If the task is about how your own interface should be structured visually → route to **Interface Designer**
* If the task is about how a specific user type interprets your product → route to **Persona Analyst**
* If the task is about market size, industry structure, or financial competitive intelligence → treat as out of scope
* If the task requires deep pricing strategy rather than observable packaging signals → flag and treat as out of scope

Examples:

* "Should we build a Kanban view because Linear has one?" → surface the competitive signal here, route the build decision to **Product Strategist**
* "What does our funnel data say about activation?" → **Analytics Reviewer**
* "Is our dashboard visually clear?" → **Interface Designer**
* "What is the total addressable market for this category?" → out of scope
* "How does Linear structure its project workflow?" → **Competitive Reviewer**
* "Where are we underbuilt compared to Notion?" → **Competitive Reviewer**

Do not solve adjacent-skill problems here.
Flag them in **Boundary Flags** and route them.

---

## Expected inputs

Best inputs:

* named competitors or adjacent products to analyze
* your own product description or scope (for comparison baseline)
* a specific dimension to compare (feature scope, onboarding, workflow, pricing structure, etc.)
* a specific problem area or user need to examine across products

Helpful optional inputs:

* your product's target user and primary use case
* known areas of concern or suspected gaps
* specific features or workflows to investigate
* known competitor strengths or weaknesses to verify
* market context or customer feedback that motivated the comparison

If no comparison target is defined, ask for one before proceeding.
If no baseline product is provided, state that findings will be reported in absolute terms rather than relative ones.
If the competitive landscape is too broad to be useful, ask the user to narrow the comparison set or the dimension of comparison.

---

## Output format

Always use this structure.

### 0. Comparison scope & caveats

Include this section when the comparison set is incomplete, the baseline is undefined, or evidence quality is limited.
State clearly what was analyzed and what limits confidence.

### 1. Summary verdict

A short paragraph.
State the dominant competitive signal and the most actionable finding from the comparison.

### 2. Competitor profiles

For each competitor analyzed, provide a structured summary:

* **Product name**
* **Primary use case and target user** (as revealed by product structure)
* **Core feature scope** (what it covers, what it excludes)
* **Distinctive UX or workflow patterns**
* **Positioning signals** (what the product emphasizes and de-emphasizes)
* **Notable strengths relative to comparison target**
* **Notable weaknesses or gaps relative to comparison target**

### 3. Comparative analysis

Analyze the competitive set as a whole across relevant dimensions.

Dimensions to cover where evidence supports:

* Feature scope comparison (what is standard vs. differentiated)
* Workflow and operational logic comparison
* UX pattern comparison
* Overbuilt areas (where competitors invest more than users likely need)
* Underbuilt areas (where competitors under-invest relative to user need)
* Differentiation gaps (where your product differs meaningfully or insufficiently)

### 4. Opportunities and blind spots

List findings that suggest concrete opportunity or risk.

For each item include:

* Observation from competitive analysis
* Why it matters
* Confidence level (High / Moderate / Low)
* Recommended next step or routing

### 5. Boundary flags

List issues that belong primarily to another skill.

Format:

* Area → Observation → Route to: [Skill Name]

This section may be empty.

---

## Confidence scale

Use these labels when assessing opportunity and blind spot findings:

* **High confidence** — supported by clear, observable product evidence
* **Moderate confidence** — inferred from partial evidence or limited product access
* **Low confidence** — hypothesis based on thin evidence; requires validation

Do not omit confidence labels from opportunity findings.

---

## Behavior under ambiguity

* If no specific competitor is named, ask before proceeding — do not fabricate a competitive set
* If no comparison baseline is provided, proceed in absolute terms and note the limitation
* If the comparison set is too broad to be useful, ask the user to narrow it
* If the task is really about internal product prioritization, surface the competitive insight and route the decision to **Product Strategist**
* If the task is really about your own product's data or UX, say so and route to the appropriate skill
* If competitive evidence is too thin to support a finding, say so rather than speculating

Do not hallucinate product features you have not observed.
Do not conflate marketing claims with product reality.
Do not present low-confidence opportunities as validated findings.

---

## Composition notes

This skill is best used when the question is not just "what exists out there?" but "what does the competitive landscape reveal about where our product stands, where gaps exist, and where opportunity lies?"

It works well:

* before roadmap planning (feed findings to Product Strategist)
* before major feature decisions (provide competitive context)
* when a specific competitor is gaining ground
* when entering a new product area
* when evaluating product-market positioning
* when investigating how a problem has been solved elsewhere

It should stand down when:

* the task is about internal product data (Analytics Reviewer)
* the task is about whether to act on competitive findings (Product Strategist)
* the task is about your own UX quality (Interface Designer, Accessibility Auditor)
* the task is about market structure rather than product comparison

Typical adjacent skills:

* **Product Strategist** — receives competitive insight and makes prioritization decisions
* **Analytics Reviewer** — complements with internal behavioral evidence
* **Interface Designer** — applies competitor UX pattern insights to your own interface
* **Persona Analyst** — contextualizes competitive findings against specific user mental models
* **Skill Auditor** — governs this skill's quality as a suite component
