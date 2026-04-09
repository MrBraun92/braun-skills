---
name: performance-reviewer
description: 'Read this skill before diagnosing any performance problem — latency, slowness, bottlenecks, query cost, rendering cost, throughput, or scale. Trigger whenever the user says something is slow, wants to optimize performance, or asks about scaling — including in Portuguese: "está lento", "por que demora tanto?", "otimize a performance", "como escalar isso?", "as queries estão pesadas". Not for code-quality review, general architecture critique, security review, product analytics, or production telemetry interpretation and log-signal analysis.'
---

# Performance Reviewer

## Purpose

Review software behavior for runtime inefficiency, bottlenecks, and scale-related performance risk.

Use this skill to analyze:

* runtime cost
* latency risk
* throughput limitations
* bottlenecks
* rendering inefficiency
* query cost
* algorithmic inefficiency
* resource-heavy paths
* where the system may degrade badly at scale
* where implementation or design choices create avoidable performance problems

This skill evaluates performance behavior and efficiency risk.
It does not perform general code-quality review, broad architecture critique, or product-behavior analytics.

---

## Use this skill when

Use this skill when the task is mainly about:

* performance
* latency
* bottlenecks
* rendering cost
* query cost
* runtime inefficiency
* scale behavior
* slow paths
* heavy operations
* performance risk under load or growth

Strong trigger examples:

* "what is making this slow?"
* "where are the bottlenecks here?"
* "will this degrade badly at scale?"
* "is this query too expensive?"
* "what is hurting runtime performance?"
* "is this rendering path too heavy?"
* "what performance risks do you see?"
* "where is this implementation inefficient?"

---

## Reasoning lens

Read the system as something that must execute repeatedly, efficiently, and predictably under real load and scale.

Ask:

* What work is being done at runtime?
* What is expensive, repeated, or unnecessary?
* Where are the likely bottlenecks?
* What gets worse as volume, traffic, or data size grows?
* Is this cost justified?
* Is the performance risk local, structural, or data-shaped?
* What is signal versus premature optimization?

Prefer meaningful bottleneck reduction over cosmetic micro-optimization.
Prefer scale-aware diagnosis over local intuition.
Prefer cost clarity over vague speed claims.

---

## What this skill owns

This skill owns:

* runtime performance diagnosis
* bottleneck identification
* query and rendering cost review
* algorithmic-efficiency review
* scale-risk analysis
* identifying where systems do unnecessary or repeated work
* identifying whether performance problems are primarily implementation-level, architecture-level, or data-shape-driven

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* static code smell review, readability review, or general maintainability audit → **Code Auditor**
* general module/service decomposition or architecture review unless the issue is explicitly performance-driven → **Code Architect**
* entity/schema design review unless the issue is explicitly driven by query shape, data volume, or storage access cost → **Data Modeler**
* security review, exploitability analysis, auth/permissions review, or secrets handling review → **Security Reviewer**
* test-strategy design or general coverage planning → **Test Strategist**
* product-behavior diagnosis based on funnel, retention, or conversion data → **Analytics Reviewer**

### Routing guidance

* If the main issue is code clarity, smell, or maintainability rather than runtime cost → route to **Code Auditor**
* If the main issue is structural system design without a clear performance driver → route to **Code Architect**
* If the main issue is schema/entity clarity without a clear performance driver → route to **Data Modeler**
* If the issue is about abuse, exposure, trust boundaries, or protection failure rather than efficiency → route to **Security Reviewer**
* If the issue is about how to verify behavior safely rather than how efficiently it runs → route to **Test Strategist**
* If the issue is about product usage metrics rather than technical runtime behavior → route to **Analytics Reviewer**

Examples:

* "This code is messy and hard to maintain" → **Code Auditor**
* "These services are coupled in the wrong way" → **Code Architect**
* "This model is mixing unrelated entity concerns" → **Data Modeler**
* "This endpoint may expose unauthorized data" → **Security Reviewer**
* "Users drop off heavily after this step" → **Analytics Reviewer**
* "This query path may become very expensive as data grows" → **Performance Reviewer**

Do not solve adjacent-skill problems here.
Flag them in **Boundary Flags** and route them.

---

## Expected inputs

Best inputs:

* code paths
* queries
* rendering logic
* profiling notes
* benchmark notes
* performance complaints
* architecture slices with cost-sensitive behavior
* endpoints or jobs with scale concerns
* representative workloads

Helpful optional inputs:

* traffic assumptions
* data volume assumptions
* latency expectations
* resource constraints
* profiling output
* cache behavior
* concurrency context
* infrastructure context

If the performance context is partial, proceed with clearly stated limits.
If the runtime path or workload assumptions are too unclear, say what is missing.

---

## Output format

Always use this structure.

### 0. Performance scope & caveats

Include this section only when the reviewed material is partial, inferred, or missing key runtime context.
State clearly what was reviewed and what limits confidence.

### 1. Summary verdict

A short paragraph.
State whether the performance posture looks strong or weak, and the main reason why.

### 2. Critical performance issues

List only the most serious performance concerns.

For each item include:

* Location, path, or workload area
* Performance problem
* Why it matters
* Likely scaling or runtime consequence
* Severity
* Recommended correction direction

Use only these severity labels:

* Critical
* High
* Medium
* Informational

### 3. High and medium performance issues

List important but non-critical performance concerns.

For each item include:

* Location, path, or workload area
* Performance problem
* Why it matters
* Likely scaling or runtime consequence
* Severity
* Recommended correction direction

### 4. Performance patterns

Summarize repeated performance patterns across the reviewed material.
Examples:

* repeated unnecessary work
* query shape does not scale with data growth
* rendering cost is driven by avoidable churn
* heavy work happens on the wrong path
* throughput risk is hidden behind acceptable low-volume behavior
* convenience decisions created avoidable cost

Do not repeat findings already listed above.

### 5. Boundary flags

List issues noticed that belong primarily to another skill.

Format:

* Location or area → Observation → Route to: [Skill Name]

This section may be empty.

### 6. Priority order

End with:

1. Fix first
2. Fix next
3. Safe to defer

---

## Severity scale

Use this scale exactly:

* **Critical** — major performance flaw likely to create severe latency, instability, or unacceptable degradation under realistic load or growth
* **High** — strong efficiency problem that materially increases runtime cost or scale risk
* **Medium** — clear performance weakness that should be corrected but is not yet severely harmful
* **Informational** — useful performance observation with low urgency

Do not invent other severity labels.

---

## Behavior under ambiguity

* If runtime context is incomplete, proceed only with clearly stated assumptions
* If the issue is really about code quality rather than runtime cost, say so and route to **Code Auditor**
* If the issue is really about architecture without a performance driver, say so and route to **Code Architect**
* If the issue is really about data structure clarity rather than cost behavior, say so and route to **Data Modeler**
* If the task is really about product metrics rather than technical efficiency, say so and route to **Analytics Reviewer**
* If the input is too vague to support credible performance diagnosis, stop and state what additional workload or runtime context is needed

Do not hallucinate precise bottlenecks from thin evidence.

---

## Composition notes

This skill is usually best when the question is not just "does this work?" but "does this run efficiently enough now and at scale?"

It works well:

* during bottleneck review
* before scale-sensitive releases
* during query and rendering diagnosis
* when evaluating runtime-heavy paths
* when investigating performance regressions
* when checking scale risk

Typical adjacent skills:

* **Code Auditor**
* **Code Architect**
* **Data Modeler**
* **Security Reviewer**
* **Test Strategist**
* **Analytics Reviewer**
