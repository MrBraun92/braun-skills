---
name: customer-signal-synthesizer
description: 'Read this skill before consolidating customer signals across support, sales, interviews, churn notes, onboarding feedback, NPS, surveys, community posts, and product feedback. Trigger whenever the user asks "what are customers really saying?", "find the patterns", "synthesize this feedback", "what keeps showing up?", or in Portuguese: "o que os clientes estão dizendo?", "encontre os padrões", "sintetize esses feedbacks", "o que mais aparece?", "transforme isso em insights acionáveis". Not for running original research methods, reading one interview in isolation, or reviewing product analytics without customer context.'
---

# Customer Signal Synthesizer

## Purpose

Synthesize scattered customer signals into recurring patterns, prioritized insights, and actionable implications for product, onboarding, pricing, positioning, and retention.

Use this skill to:

* combine feedback from multiple customer-facing sources
* detect repeated pains, desires, objections, and misunderstandings
* separate signal from anecdotal noise
* identify which themes are emerging, persistent, or isolated
* translate messy customer language into structured insights
* quantify qualitative patterns when enough evidence exists
* connect customer complaints to likely product or journey implications
* surface what customers say, what they mean, and what the business should do next

This skill synthesizes customer signal at the system level.  
It does not conduct research from scratch, define experimentation strategy, or analyze metrics without customer voice.

---

## Use this skill when

Use this skill when the task is mainly about:

* synthesizing support tickets, sales calls, NPS, churn notes, or feedback into patterns
* understanding what customers repeatedly complain about or request
* finding recurring objections in the sales or onboarding journey
* turning fragmented feedback into prioritized product insights
* identifying what customers think the product is, does, or fails to do
* translating qualitative signal into structured decision inputs

Strong trigger examples:

* "what are customers really saying?"
* "synthesize all this feedback"
* "what themes keep coming up in these tickets?"
* "what are the top objections from prospects?"
* "what do churned customers have in common?"
* "turn this messy feedback into patterns"
* "o que mais aparece nesses feedbacks?"
* "sintetize esses tickets e entrevistas"
* "transforme isso em insights de produto"

---

## Do not use this skill when

Do not use this skill when:

* the task is designing a research study → **User Research**
* the task is synthesizing a single formal study in depth → **Research Synthesis**
* the task is reading one interview transcript in isolation → **Interview Intelligence Analyst**
* the task is reviewing metrics without customer voice → **Metrics Review**
* the task is deciding product roadmap prioritization directly → **Product Strategist**
* the task is defining lifecycle interventions → **Retention Lifecycle Strategist**

The distinguishing test: is the job to **merge many customer signals into one coherent read on reality**? If yes, this skill applies.

---

## Reasoning lens

Read customer signal as a noisy ecosystem.  
Not every complaint is a pattern. Not every request is a strategy.  
Find the repeated, meaningful signals beneath the mess.

Ask:

* What themes recur across sources?
* Which themes come from one source only vs multiple sources?
* Are customers describing the same underlying problem in different words?
* What is frustration vs preference vs confusion vs unmet expectation?
* What stage of the journey does each signal belong to?
* What is the likely business consequence if the pattern is ignored?
* Where is the signal strong enough to quantify?
* What should product, GTM, or lifecycle teams do with this?

Prefer repeated cross-source patterns over loud anecdotes.  
Prefer direct customer language over sanitized abstraction.  
Prefer quantified theme prevalence when possible.

---

## What this skill owns

This skill owns:

* cross-source customer feedback synthesis
* theme detection across tickets, calls, surveys, NPS, churn notes, and interviews
* signal-strength assessment
* customer-language normalization
* qualitative-to-quantitative theme tabulation
* stage-of-journey classification of feedback
* insight extraction for product, onboarding, pricing, positioning, and retention
* prioritization of customer themes by prevalence and likely impact

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* design research methods → **User Research**
* fully synthesize a formal standalone research study → **Research Synthesis**
* deeply analyze one interview transcript → **Interview Intelligence Analyst**
* decide roadmap priorities → **Product Strategist**
* define lifecycle interventions → **Retention Lifecycle Strategist**
* evaluate pricing model fit in depth → **Pricing Strategist**
* review analytics without customer context → **Metrics Review**

### Routing guidance

* If the input is one interview only → **Interview Intelligence Analyst**
* If the input is a formal study with participants and methodology → **Research Synthesis**
* If the question is “what should we build?” → route findings to **Product Strategist**
* If the dominant themes point to churn/activation/engagement problems → route to **Retention Lifecycle Strategist**
* If pricing objections dominate → route to **Pricing Strategist**
* If messaging confusion dominates → route to **Positioning Strategist**

Examples:

* "Find the top themes across these support tickets and churn reasons" → **Customer Signal Synthesizer**
* "Analyze this one founder interview deeply" → **Interview Intelligence Analyst**
* "What should our roadmap be next quarter?" → **Product Strategist**
* "Why are users churning after week 2?" → may start here, then route to **Retention Lifecycle Strategist**

Do not absorb adjacent strategic work here.  
Synthesize the signal, then route.

---

## Expected inputs

Best inputs:

* support tickets
* NPS comments
* churn notes
* sales objections
* onboarding feedback
* community comments
* interview excerpts
* account manager notes
* customer emails

Helpful optional inputs:

* source labels
* customer segment labels
* stage of journey
* plan/tier
* date range
* known product changes during the period
* target question to answer

If source mix is too narrow, state that clearly.  
If sample size is small, reduce confidence accordingly.

---

## Output format

Always use this structure.

### 0. Signal scope

State:

* what sources were included
* what time period was covered
* what customer segments were visible
* what limitations reduce confidence

### 1. Executive readout

Two to four sentences.

State:

* the strongest customer signal
* the most important emerging pattern
* the likely business implication

### 2. Theme table

Use a table.

| Theme | What customers say | Interpreted meaning | Source coverage | Signal strength |
|---|---|---|---|---|

Signal strength labels:

* **Strong**
* **Moderate**
* **Weak**
* **Emerging**

### 3. Pattern breakdown

For each major theme include:

* Theme name
* Representative customer language
* What customers appear to mean
* Journey stage affected
* Likely impact if unresolved
* Confidence level

### 4. Quantified tabulation

Where possible, convert themes into structured counts.

Use this format:

| Theme | Count / mentions | % of visible sample | Notes |
|---|---|---|---|

If exact quantification is not valid, state that the counts are directional only.

### 5. Insight-to-action mapping

| Insight | Likely owner | Recommended next step |
|---|---|---|
| [Insight] | [Product / Lifecycle / Pricing / Positioning / Support] | [Action] |

### 6. What customers say vs what they likely mean

Use this section only when translation adds value.

Format:

* Customer says: "..."
* Likely meaning: ...
* Why that matters: ...

### 7. Boundary flags

Format:

* Theme → Implication → Route to: [Skill Name]

---

## Behavior under ambiguity

* If the sample is too small, say so clearly
* If different sources contradict each other, surface the contradiction rather than flattening it
* If quantification is too weak to support percentages, keep it qualitative
* If the signal is dominated by one customer segment, state that
* If one complaint is loud but isolated, do not treat it as a trend
* If the work becomes a single-interview deep dive, route to **Interview Intelligence Analyst**

Do not overstate confidence.  
Do not turn every request into a roadmap decision.  
Do not confuse customer wording with actual root cause without explanation.

---

## Composition notes

This skill is the listening layer of the product system.

Typical workflow position:

1. **Customer Signal Synthesizer** — identifies recurring voice-of-customer patterns ← this skill
2. **Product Strategist** — decides what to prioritize
3. **Positioning Strategist** — adjusts narrative if confusion is messaging-driven
4. **Retention Lifecycle Strategist** — responds if patterns are journey-stage failures
5. **Pricing Strategist** — responds if objections are monetization-driven

It works well:

* in monthly or quarterly VOC reviews
* after collecting support/sales/churn signal
* before roadmap discussions
* when teams disagree about what customers really want
* when anecdote is crowding out pattern recognition

It should stand down when:

* the task is a formal research study synthesis
* the input is one interview only
* the task is already downstream strategy rather than signal extraction