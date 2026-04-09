---
name: production-reviewer
description: 'Read this skill before interpreting any production logs, error signals, or post-deploy telemetry. Trigger whenever the user shares logs or says something broke after a deploy — including in Portuguese: "o que esses logs dizem?", "tem erro em produção?", "algo quebrou após o deploy", "essa taxa de erro é normal?", "o que está degradando?", "parece que tem um problema em prod". Not for runtime performance diagnosis, product analytics, security threat assessment, or incident response management.'
---

# Production Reviewer

## Purpose

Interpret production signals — logs, error rates, deployment telemetry, operational degradation patterns, and post-deploy behavior — to determine what is actually happening in production, separate signal from noise, and route findings to the right specialist for action.

Use this skill to:

* read production logs and error signals to identify what is real vs. noise
* interpret post-deploy telemetry to assess whether a deployment is behaving as expected
* identify degradation patterns and what they suggest about root cause
* distinguish transient spikes from structural issues
* determine the severity and urgency of a production signal
* route confirmed findings to the right specialist (performance, security, engineering)
* surface early warning signals before they become incidents
* interpret incident patterns across time to identify recurring failure modes

This skill interprets production signals and routes findings. It does not diagnose performance root causes, conduct security investigations, manage incident response, or analyze product usage behavior.

---

## Use this skill when

Use this skill when the task is mainly about:

* reading logs and deciding what they mean
* understanding whether a post-deploy signal is a real problem
* identifying what is degrading in production and how seriously
* distinguishing a spike from a trend
* deciding whether a production signal warrants escalation
* interpreting what an error pattern suggests
* assessing the health of a recent deployment from its telemetry

Strong trigger examples:

* "what do these logs mean?"
* "is this error rate a real problem or noise?"
* "something looks off after this deploy — what does the telemetry say?"
* "we're seeing degradation — is it serious?"
* "what is this error pattern telling us?"
* "should we be worried about this signal?"
* "is this a transient spike or a structural issue?"
* "help me read this production incident"
* "what's causing this operational degradation?"
* "are these post-deploy signals normal?"

---

## Do not use this skill when

Do not use this skill when:

* the task is diagnosing latency, throughput, or query performance root cause → **Performance Reviewer**
* the task is product usage analytics, funnel analysis, or behavioral metrics → **Analytics Reviewer**
* the task is security threat analysis, exploit investigation, or auth anomaly review → **Security Reviewer**
* the task is managing an active incident or coordinating incident response → out of scope (incident management)
* the task is pre-release verification or release readiness → **Release Verifier**

The distinguishing test: is the question about *what production signals are telling you right now*? If yes, this skill applies. If the question is about why performance is slow (root cause diagnosis), route to Performance Reviewer.

---

## Reasoning lens

Read production signals as evidence about system health — but always ask first whether the signal is real before deciding what it means.

Ask:

* Is this signal real or noise — is the anomaly above the baseline variance?
* Is this transient (spike, burst) or structural (trend, degradation)?
* What is the blast radius — how many users or services are affected?
* What changed recently — deploy, config, traffic pattern, upstream dependency?
* Is this a new pattern or a known recurring failure mode?
* What does the combination of signals suggest vs. any single signal alone?
* How urgent is this — does it require immediate action or monitoring?
* What specialist is best positioned to diagnose the root cause from here?

Prefer signal confirmation before root-cause speculation.
Prefer blast radius assessment before severity classification.
Prefer routing to the right specialist over attempting to diagnose outside this skill's scope.

---

## What this skill owns

* production log interpretation
* error signal analysis — real vs. noise classification
* post-deploy telemetry assessment
* operational degradation pattern identification
* incident pattern recognition across time
* severity and urgency classification of production signals
* routing confirmed findings to Performance Reviewer, Security Reviewer, or engineering
* early warning signal identification

---

## Boundary rules

### This skill must not do

* diagnose latency, throughput, query cost, or performance root cause → **Performance Reviewer**
* conduct security investigations, review auth anomalies, or assess exploitability → **Security Reviewer**
* analyze product usage behavior, funnels, or conversion signals → **Analytics Reviewer**
* manage active incident response or coordinate an incident → out of scope
* verify pre-release readiness → **Release Verifier**
* review code quality or architecture → **Code Auditor** / **Code Architect**

### Routing guidance

* "Why is our API slow?" → **Performance Reviewer** (after production-reviewer confirms the signal is real and scopes it)
* "Is this auth anomaly a security threat?" → **Security Reviewer**
* "Why are users dropping off in the onboarding funnel?" → **Analytics Reviewer**
* "We're in an active incident — who does what?" → out of scope (incident management)
* "These logs look weird after the deploy — is this real?" → **Production Reviewer**

---

## Expected inputs

Best inputs:

* log samples or error output
* error rate metrics or graphs
* deployment timeline and what changed
* service or component context
* baseline behavior for comparison (if known)

Helpful optional inputs:

* alerting rules and current alert state
* recent incidents and their resolutions
* upstream dependency status
* deployment rollback availability
* traffic pattern context

If no log samples or signal data are provided, ask — production signals cannot be interpreted without evidence.

---

## Output format

Always use this structure.

### 0. Signal context & caveats

State what was analyzed, what baseline information was available, and what limits confidence.

### 1. Signal verdict

One of:

* **NOISE** — signal is within normal variance; no action required
* **WATCH** — signal is above baseline but not yet confirmed as a problem; monitor
* **REAL ISSUE** — signal confirms a meaningful problem; routing to specialist required
* **CRITICAL** — signal indicates active degradation or failure; immediate action required

Follow with a one-sentence summary of the dominant signal.

### 2. Signal analysis

For each significant signal:

* Signal description
* Baseline vs. observed
* Real vs. noise assessment: **Confirmed real** / **Likely real** / **Ambiguous** / **Noise**
* Transient vs. structural: **Transient** / **Structural** / **Unknown**
* Blast radius: what is affected, at what scale

### 3. Pattern interpretation

What does the combination of signals suggest?

* Most likely explanation
* Alternative explanations (if evidence is ambiguous)
* Confidence level: **High** / **Moderate** / **Low**

### 4. Routing

List what confirmed findings need specialist follow-up.

For each:

* Finding
* Route to: [Skill Name]
* Why this specialist

### 5. Recommended immediate actions

What should happen right now, before specialist diagnosis is complete.

### 6. Boundary flags

Format: Area → Observation → Route to: [Skill Name]

---

## Severity scale

* **Critical** — active production failure or degradation affecting users at scale; immediate action required
* **High** — confirmed real issue with meaningful blast radius; specialist review required promptly
* **Medium** — real signal with limited impact; investigate within normal workflow
* **Informational** — useful signal worth tracking; no immediate action

---

## Behavior under ambiguity

* If no signal data is provided, ask — interpretation without evidence is speculation
* If baseline is unknown, note that noise vs. signal classification is limited and flag the gap
* If the signal is ambiguous between noise and real, surface both interpretations with confidence levels
* If the signal clearly falls into another skill's domain (performance root cause, security threat), route immediately rather than attempting to diagnose here

---

## Composition notes

Typical workflow position:

1. **Release Verifier** — verifies readiness before shipping
2. **Launch Coordinator** — coordinates go-live
3. **Production Reviewer** — interprets production signals after launch ← this skill
4. **Performance Reviewer** — diagnoses performance root cause from routed findings
5. **Security Reviewer** — investigates security signals from routed findings

Typical adjacent skills:

* **Release Verifier** — hands pre-release context to this skill post-deploy
* **Performance Reviewer** — receives performance-confirmed findings
* **Security Reviewer** — receives security-signal findings
* **Analytics Reviewer** — receives product-behavior signals (not operational signals)
