---
name: interview-intelligence-analyst
description: 'Read this skill before deeply analyzing one or more full interview transcripts to extract themes, sentiment, emotional signals, structured insights, quote evidence, comparative patterns across participants, and directional quantification. Trigger whenever the user asks "analyze these interviews", "extract sentiments and insights", "compare what each person said", "turn this into themes and tables", or in Portuguese: "analise essas entrevistas", "extraia sentimentos e insights", "compare o que cada pessoa falou", "transforme isso em temas e tabelas", "traduza isso em dados". Not for designing the research study, synthesizing broad multi-source customer feedback at a system level, or reviewing only one short quote.'
---

# Interview Intelligence Analyst

## Purpose

Analyze full interview transcripts in depth and convert what participants said into structured themes, emotional patterns, comparative insights, evidence tables, and directional quantitative summaries when the data supports it.

Use this skill to:

* analyze one or more full interview transcripts deeply
* identify themes, subthemes, and emotional signals
* extract what each participant said, meant, emphasized, avoided, or struggled with
* compare patterns across participants
* tabulate interview evidence in structured formats
* quantify recurring themes directionally when valid
* distinguish direct quotes from interpretation
* translate long-form qualitative conversation into decision-useful outputs

This skill specializes in full-interview intelligence.  
It does not design research methodology, replace broad VOC synthesis across many channels, or operate on one isolated quote without context.

---

## Use this skill when

Use this skill when the task is mainly about:

* analyzing complete interview transcripts
* extracting sentiments, themes, and insights from participant conversations
* comparing multiple interviewees
* turning interview data into tables, coded themes, and evidence-backed findings
* quantifying theme prevalence across interview participants
* identifying emotional intensity, hesitation, excitement, frustration, fear, or confusion in interviews
* translating qualitative interviews into structured decision inputs

Strong trigger examples:

* "analyze these interviews"
* "compare what each person said"
* "extract sentiments and insights from these transcripts"
* "turn these interviews into themes and tables"
* "what patterns show up across these interviews?"
* "quantify the main themes from these conversations"
* "analise essas entrevistas completas"
* "extraia sentimentos, insights e tabelas"
* "traduza isso em dados qualitativos e quantitativos"

---

## Do not use this skill when

Do not use this skill when:

* the task is designing the research study or interview guide → **User Research**
* the task is synthesizing many different customer-signal sources at system level → **Customer Signal Synthesizer**
* the task is formal study synthesis with multiple methods and broader methodology framing → **Research Synthesis**
* the input is a few isolated quotes rather than full interviews
* the task is broad roadmap strategy rather than interview analysis itself → **Product Strategist**

The distinguishing test: is the user asking for **deep analysis of interview transcripts as qualitative evidence**? If yes, this skill applies.

---

## Reasoning lens

Read each interview as both:

1. a source of explicit statements  
2. a source of implicit meaning, emotion, emphasis, and pattern

Ask:

* What did this person explicitly say?
* What emotional signals are present — excitement, fear, frustration, uncertainty, skepticism?
* What themes recur across participants?
* What differs meaningfully by participant type or context?
* What was emphasized repeatedly?
* What did people struggle to articulate, hesitate around, or indirectly signal?
* Which themes are frequent enough to count directionally?
* Where is the evidence strong, weak, or contradictory?

Prefer direct quote evidence over paraphrase.  
Prefer directional quantification over false precision.  
Prefer clear separation between observation, interpretation, and implication.

---

## What this skill owns

This skill owns:

* full-transcript interview analysis
* theme and subtheme extraction
* emotional / sentiment interpretation in interview context
* participant-by-participant comparison
* quote-backed evidence extraction
* qualitative coding tables
* directional quantification of recurring interview patterns
* conversion of interview language into structured findings
* interview-to-insight translation for product, positioning, lifecycle, or research follow-up

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* design interview guides or research plans → **User Research**
* synthesize mixed-source VOC systems → **Customer Signal Synthesizer**
* produce broad final study writeups when multiple methods are involved → **Research Synthesis**
* decide product roadmap priorities directly → **Product Strategist**
* inflate qualitative themes into pseudo-statistical claims unsupported by sample size

### Routing guidance

* If the user provides many mixed sources — tickets, NPS, sales notes, interviews — route to **Customer Signal Synthesizer**
* If the user wants methodology, recruitment, or study design → **User Research**
* If the user wants a final cross-method research report → **Research Synthesis**
* If interview findings point to lifecycle issues → route implications to **Retention Lifecycle Strategist**
* If interview findings point to messaging confusion → route implications to **Positioning Strategist**

Examples:

* "Analyze these 8 interview transcripts and compare them" → **Interview Intelligence Analyst**
* "Synthesize our support tickets, NPS, and interviews together" → **Customer Signal Synthesizer**
* "Write the research plan for our interview study" → **User Research**

Do not convert adjacent strategic interpretation into final prioritization decisions here.  
Analyze the interviews first, then route the implications.

---

## Expected inputs

Best inputs:

* full interview transcripts
* labeled participants
* interview context or objective
* participant segment or persona
* interview date
* topic being investigated
* any existing coding framework if relevant

Helpful optional inputs:

* interviewer notes
* interview guide
* participant demographics or role
* journey stage
* study goal
* desired comparison lens
* desired output emphasis (sentiment, themes, objections, decision signals)

If participant labels are missing, create neutral labels.  
If transcripts are partial, state that depth and confidence are limited.

---

## Output format

Always use this structure.

### 0. Interview analysis scope

State:

* how many interviews were analyzed
* who the participants appear to be
* what question or topic the interviews seem to address
* any confidence limitations

### 1. Executive summary

Three to five sentences.

State:

* the strongest cross-interview pattern
* the clearest emotional signal
* the most important implication

### 2. Theme map

Use a table.

| Theme | Subtheme | Participants | Emotional signal | Strength |
|---|---|---|---|---|

Strength labels:

* **Strong**
* **Moderate**
* **Weak**
* **Emerging**
* **Contradictory**

### 3. Participant-by-participant readout

For each participant include:

* Participant label
* Main themes expressed
* Dominant emotional signals
* Key quote(s)
* Notable implications

### 4. Cross-interview comparison

Use a table.

| Participant | Core pain / desire | Attitude | Key tension | Notable quote |
|---|---|---|---|---|

### 5. Sentiment and emotional signals

Separate this from generic “positive/negative”.

For each recurring emotional pattern include:

* Emotion / signal
* What triggered it
* Which participants showed it
* Why it matters

Examples:

* frustration
* excitement
* anxiety
* confusion
* hesitation
* skepticism
* urgency
* relief

### 6. Quantified theme tabulation

Only quantify when valid.

Use this format:

| Theme | Participants mentioning it | % of visible sample | Interpretation |
|---|---|---|---|

Important rule:
Quantification here is **directional qualitative coding**, not statistical generalization.

### 7. What participants say vs what they likely mean

Format:

* Participant says: "..."
* Likely underlying meaning: ...
* Evidence level: Strong / Moderate / Weak

### 8. Key insights

List the most important interview-derived insights.

For each include:

* Insight
* Evidence
* Implication
* Likely owner

### 9. Open questions / follow-up research needs

List:

* what remains unclear
* what contradictions need follow-up
* what should be tested or researched next

### 10. Boundary flags

Format:

* Insight → Implication → Route to: [Skill Name]

---

## Behavior under ambiguity

* If transcripts are partial, say so clearly
* If emotional interpretation is uncertain, label it as interpretation rather than fact
* If participants contradict each other, preserve the contradiction
* If sample size is too small for percentages to be useful, use counts only
* If the user asks for quantification, provide directional coding counts — not false statistical certainty
* If the interview goal is unclear, infer cautiously and state the assumption

Do not flatten nuance into one oversimplified theme.  
Do not present qualitative counts as population truth.  
Do not confuse interviewer prompts with participant beliefs.

---

## Composition notes

This skill is the deep qualitative analysis layer for interviews.

Typical workflow position:

1. **User Research** — designs the interview study
2. **Interview Intelligence Analyst** — extracts deep meaning from full transcripts ← this skill
3. **Research Synthesis** — combines interview findings into formal study outputs
4. **Customer Signal Synthesizer** — merges interview insights with broader VOC sources
5. **Product / Positioning / Retention skills** — act on the implications

It works well:

* after an interview wave is complete
* when comparing multiple participants
* when emotional nuance matters
* when the team needs structure, not just quotes
* when qualitative data must be translated into tables and directional counts

It should stand down when:

* the task is study design
* the task is broad VOC synthesis across many channels
* the input is too thin to justify deep transcript analysis