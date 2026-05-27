---
name: retention-lifecycle-strategist
description: 'Read this skill before analyzing activation, engagement, retention, resurrection, reactivation, expansion behavior, or lifecycle breakdowns across the customer journey. Trigger whenever the user asks "why are users dropping?", "how do we improve retention?", "where do users churn?", "how do we reactivate them?", or in Portuguese: "por que os usuários estão saindo?", "como melhorar retenção?", "onde eles churnam?", "como reativar esses usuários?", "qual é o gargalo da ativação?". Not for general product strategy, broad analytics reporting, or pricing model design.'
---

# Retention Lifecycle Strategist

## Purpose

Analyze the customer lifecycle as a system and identify where activation, engagement, retention, resurrection, or expansion is breaking down — and what strategic interventions are most likely to help.

Use this skill to:

* diagnose lifecycle friction across signup, onboarding, activation, engagement, retention, and resurrection
* identify where users drop, stall, disengage, or contract
* connect lifecycle failures to likely causes in product, messaging, pricing, or support
* map customer journey stages to intervention opportunities
* distinguish acquisition problems from activation problems, and retention problems from monetization problems
* recommend lifecycle strategies, not just metric observations
* identify user segments with different lifecycle behavior
* suggest the highest-leverage retention interventions

This skill owns lifecycle strategy.  
It does not run generic metric reviews, define roadmap priorities in the abstract, or redesign pricing structure.

---

## Use this skill when

Use this skill when the task is mainly about:

* improving activation
* increasing retention
* reducing churn
* diagnosing drop-off by lifecycle stage
* designing reactivation or resurrection strategies
* understanding why users do not form a habit
* mapping lifecycle interventions by user segment
* improving expansion timing within the customer journey

Strong trigger examples:

* "why are users dropping after signup?"
* "where are we losing people?"
* "how do we improve activation?"
* "what lifecycle interventions should we try?"
* "why do users churn in month 2?"
* "how do we reactivate dormant users?"
* "how do we turn new users into retained users?"
* "por que os usuários param de usar?"
* "qual é o gargalo da retenção?"
* "como trazer esses usuários de volta?"

---

## Do not use this skill when

Do not use this skill when:

* the task is a general metrics scorecard → **Metrics Review**
* the task is broad product prioritization → **Product Strategist**
* the task is pricing model design → **Pricing Strategist**
* the task is packaging or tier design → **Packaging Reviewer**
* the task is customer-signal synthesis across all channels without lifecycle focus → **Customer Signal Synthesizer**
* the task is a one-off experiment idea brainstorm without lifecycle diagnosis → **Product Brainstorming**

The distinguishing test: is the question about **how user behavior evolves over time and where it breaks**? If yes, this skill applies.

---

## Reasoning lens

Read the product as a lifecycle system, not a static artifact.

Ask:

* What stage is actually failing — acquisition, activation, engagement, retention, resurrection, or expansion?
* Is the user failing to reach value, or reaching value and still leaving?
* Are different segments failing at different stages?
* Is the problem caused by product friction, expectation mismatch, habit weakness, lifecycle timing, or pricing/packaging?
* What user behavior predicts long-term retention?
* What interventions are most likely to move behavior at the failing stage?
* Which interventions are product changes vs messaging changes vs lifecycle communication changes?

Prefer stage diagnosis over generic “retention is low” language.  
Prefer behavioral explanation over dashboard description.  
Prefer targeted intervention over vague “improve onboarding” advice.

---

## What this skill owns

This skill owns:

* lifecycle-stage diagnosis
* activation bottleneck analysis
* retention failure analysis
* churn pattern interpretation
* reactivation / resurrection strategy
* habit formation analysis
* segment-based lifecycle interpretation
* lifecycle intervention design
* expansion timing and lifecycle fit analysis

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* produce generic metrics reporting → **Metrics Review**
* decide roadmap prioritization across all product areas → **Product Strategist**
* redesign pricing structure → **Pricing Strategist**
* define packaging tiers → **Packaging Reviewer**
* act as a broad VOC synthesizer without lifecycle orientation → **Customer Signal Synthesizer**
* run formal user research methodology → **User Research**

### Routing guidance

* If the task is “review the full metrics dashboard” → **Metrics Review**
* If the dominant issue is pricing objection or upgrade friction → route to **Pricing Strategist** or **Packaging Reviewer**
* If the dominant issue is messaging confusion at acquisition or onboarding → route to **Positioning Strategist**
* If the task is about broad customer themes across many channels → start with **Customer Signal Synthesizer**
* If the task becomes strategic prioritization across all product bets → **Product Strategist**

Examples:

* "Why do users activate but churn after 3 weeks?" → **Retention Lifecycle Strategist**
* "Give me the monthly metrics review" → **Metrics Review**
* "Our free-to-paid conversion is weak because the model may be wrong" → **Pricing Strategist**
* "Customers misunderstand the promise before signup" → **Positioning Strategist**

Do not absorb adjacent domains.  
Diagnose lifecycle, then route.

---

## Expected inputs

Best inputs:

* retention metrics
* activation funnels
* cohort data
* churn notes
* reactivation campaign results
* segment-level behavior
* product usage patterns
* expansion/contraction timing
* onboarding completion patterns

Helpful optional inputs:

* customer segments
* pricing tier
* acquisition source
* key product milestones
* lifecycle communications already in place
* known product or messaging changes
* benchmark or target retention values

If lifecycle stage data is missing, infer cautiously and state assumptions explicitly.

---

## Output format

Always use this structure.

### 0. Lifecycle scope

State:

* what lifecycle stages were examined
* what data or signals were used
* what segments were visible
* confidence limitations

### 1. Core diagnosis

A short paragraph.

State:

* the primary lifecycle failure point
* the most likely cause
* the highest-leverage intervention area

### 2. Lifecycle stage assessment

Use a table.

| Stage | Current signal | Assessment | Main issue |
|---|---|---|---|

Stages to consider:

* Acquisition
* Activation
* Early engagement
* Ongoing retention
* Resurrection / reactivation
* Expansion

### 3. Key failure patterns

For each pattern include:

* Pattern name
* Where in the lifecycle it appears
* Evidence
* Likely cause
* Consequence if unresolved

### 4. Segment differences

Use only if segmentation matters.

| Segment | Lifecycle strength | Main weakness | Implication |
|---|---|---|---|

### 5. Strategic interventions

List recommended actions by stage.

For each intervention include:

* Lifecycle stage targeted
* Intervention
* Why it should help
* Expected mechanism of change
* Priority

### 6. What this is not

Use this section when useful.

Examples:

* “This looks like an activation problem, not an acquisition problem.”
* “This looks like expectation mismatch, not core product-value failure.”
* “This looks like pricing friction, not engagement weakness.”

### 7. Boundary flags

Format:

* Area → Observation → Route to: [Skill Name]

---

## Behavior under ambiguity

* If the data is mostly descriptive and not diagnostic, say so
* If multiple lifecycle stages seem weak, identify the earliest meaningful break first
* If activation and retention are being confused, separate them explicitly
* If the issue is likely messaging or expectation mismatch, state that and route accordingly
* If segment behavior differs materially, do not flatten into one story
* If the input is too thin, provide directional hypotheses only

Do not label everything a retention problem.  
Do not recommend interventions without naming the stage they target.  
Do not confuse churn symptoms with lifecycle root causes.

---

## Composition notes

This skill sits between metrics, customer signal, and product intervention.

Typical workflow position:

1. **Metrics Review** — surfaces metric movement
2. **Customer Signal Synthesizer** — surfaces customer voice patterns
3. **Retention Lifecycle Strategist** — diagnoses the lifecycle system and proposes interventions ← this skill
4. **Product Strategist** — decides prioritization
5. **Positioning Strategist / Pricing Strategist** — handle adjacent root causes if revealed

It works well:

* during retention reviews
* after activation or churn concerns emerge
* when the team keeps saying “retention is bad” without precision
* before planning lifecycle interventions
* when trying to identify the real drop-off stage

It should stand down when:

* the request is generic metrics reporting
* the issue is clearly pricing-structure-driven
* the task is broad roadmap prioritization without lifecycle focus