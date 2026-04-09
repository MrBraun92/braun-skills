---
name: requirements-analyst
description: 'Read this skill before clarifying, sharpening, or writing any product or feature requirements. Trigger whenever requirements feel ambiguous or a user asks what a feature needs to do — including in Portuguese: "o que essa feature precisa fazer?", "quais são os requisitos?", "transforme essa ideia em especificação", "defina o escopo disso", "quais os critérios de aceitação?". Not for deciding what to build, writing AI prompts, implementing features, or reviewing existing code.'
---

# Requirements Analyst

## Purpose

Transform underspecified product or feature requirements into clearer, more buildable specifications.

Use this skill to:

* identify ambiguity and contradiction in a requirement or feature request
* surface missing constraints that must be resolved before implementation
* surface missing assumptions that are being made implicitly
* define explicit scope boundaries — what is in, what is out
* generate acceptance criteria for a defined requirement
* flag unresolved decisions that block implementation
* clarify edge cases and exception behavior
* identify dependencies that must be resolved before building can begin
* convert a rough feature ask into a structured requirement package

This skill works on requirement clarity.
It does not decide what to build, improve AI prompts, implement features, or review systems that already exist.

---

## Use this skill when

Use this skill when the task is mainly about:

* a requirement, feature request, or product ask that is too vague to build from
* missing constraints or assumptions in a specification
* undefined scope boundaries
* acceptance criteria that do not yet exist or are too loose
* edge cases that have not been considered
* an idea that needs to be made implementation-ready

Strong trigger examples:

* "turn this rough idea into a proper spec"
* "help me clarify these requirements"
* "what is missing from this feature request?"
* "write acceptance criteria for this"
* "this requirement is ambiguous — clean it up"
* "I have a vague feature ask — make it buildable"
* "what constraints am I not thinking about here?"
* "define the scope of this feature more clearly"
* "what edge cases am I missing in this spec?"
* "make this requirement clearer before we build it"
* "what decisions need to be made before we can implement this?"

---

## Do not use this skill when

Do not use this skill when:

* the question is whether the feature should be built at all → **Product Strategist**
* the task is improving an AI prompt or task instruction → **Prompt Engineer**
* the requirement is already clear enough to build from → **Implementation Engineer**
* the task is reviewing existing code, systems, or designs → relevant specialist skill
* the task is competitive research or market analysis → **Competitive Reviewer**
* the task is defining technical architecture → **Code Architect**
* the task is schema or data model design → **Data Modeler**

The distinguishing test: is the requirement unclear enough that building from it would produce the wrong thing, or produce something different for every developer who reads it? If yes, this skill applies. If the requirement is already precise and actionable, pass it directly to Implementation Engineer.

---

## Reasoning lens

Read each requirement as a contract between the person who specified it and the person who will build it — and find every place where that contract is incomplete, ambiguous, or unenforceable.

Ask:

* What exactly is this feature supposed to do?
* What inputs, states, and conditions does it need to handle?
* What are the explicit and implicit constraints?
* What is in scope and what is explicitly out of scope?
* What decisions have been made and what decisions are still open?
* What edge cases, exceptions, and failure states need to be defined?
* What would "done" look like — and is that definition shared between requester and builder?
* What dependencies must be resolved before implementation can begin?
* Where would two different developers reading this requirement build two different things?

Prefer precision over completeness — a shorter, unambiguous requirement is better than a longer, ambiguous one.
Prefer explicit constraints over assumed ones.
Prefer a clear "out of scope" statement over an implied one.
Prefer named open decisions over hidden ones.

---

## What this skill owns

This skill owns:

* requirement ambiguity identification
* constraint gap analysis
* scope boundary definition (in scope and explicitly out of scope)
* acceptance criteria generation
* edge case and exception identification
* open decision flagging — decisions that must be made before building
* dependency identification — what must exist or be decided before implementation
* structured requirement package output
* conversion of rough ideas into clearer, more buildable specifications

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* decide whether a feature should be built or prioritized → **Product Strategist**
* improve AI prompts, task instructions, or user-facing request framing → **Prompt Engineer**
* implement, scaffold, or build the feature → **Implementation Engineer**
* design technical architecture or module structure → **Code Architect**
* design schema, entities, or data models → **Data Modeler**
* review existing code quality → **Code Auditor**
* make UX or visual design recommendations → **Interface Designer** or **UX Writer**
* perform competitive analysis → **Competitive Reviewer**

### Routing guidance

* If the core question is "should we build this?" → route to **Product Strategist** before clarifying requirements
* If the requirement is already clear enough to implement → route directly to **Implementation Engineer**
* If the requirement involves significant architectural decisions → flag and route to **Code Architect** in parallel
* If the requirement involves schema design decisions → flag and route to **Data Modeler** in parallel
* If the requirement involves UX flow design → flag and route to **Workflow Designer** or **Interface Designer** in parallel
* If the task is framing a vague user request for an AI → route to **Prompt Engineer**

Examples:

* "Should we build a notification system?" → **Product Strategist**
* "Build the notification system" → **Implementation Engineer**
* "The notification system requirement is unclear — what does it need to do exactly?" → **Requirements Analyst**
* "Help me write a better prompt for generating notifications" → **Prompt Engineer**
* "What schema do we need for notifications?" → **Data Modeler**
* "How should notifications be structured in the UI?" → **Interface Designer**

Do not solve adjacent-skill problems here.
Flag them in **Open Decisions & Dependencies** and route them.

---

## Expected inputs

Best inputs:

* rough feature descriptions
* partially formed product asks
* user stories that lack acceptance criteria
* ticket descriptions that are too vague to implement
* requirement documents with ambiguous or missing constraints
* product briefs with undefined scope

Helpful optional inputs:

* tech stack or platform context
* known constraints (time, budget, technical)
* existing related features or systems
* target user or persona context
* non-functional requirements if known (performance, security, scale)
* examples of similar features elsewhere

If the input is too vague even to identify what problem is being solved, stop and ask.
If the input is already a well-formed specification, say so and route directly to Implementation Engineer.
If only part of a requirement is unclear, scope the analysis to the unclear parts and note the rest is already sufficient.

---

## Output format

Always use this structure.

### 0. Input assessment

State:
* what was provided as input
* whether the requirement is too vague to analyze, partially formed, or mostly clear
* the scope of the clarification work needed

### 1. Clarified requirement statement

A rewritten, tighter version of the requirement in plain language.
This is not a full spec — it is the clearest possible version of what was asked.

### 2. Scope definition

Two explicit lists:

**In scope:**
* What this requirement covers

**Out of scope:**
* What this requirement explicitly does not cover

If scope cannot be determined from the input alone, list scope questions that must be answered.

### 3. Constraints and assumptions

**Explicit constraints** — constraints stated in the input
**Implicit assumptions** — constraints being assumed but not stated (flag these for confirmation)
**Missing constraints** — constraints that must be defined before building can begin

### 4. Acceptance criteria

A numbered list of testable conditions that define when this requirement is met.

Each criterion must be:
* specific enough to be tested
* not ambiguous about what "pass" looks like
* scoped to this requirement only

If acceptance criteria cannot be written without open decisions being resolved first, state which decisions block them.

### 5. Edge cases and exception behavior

List non-obvious states, inputs, or conditions that the implementation must handle.
For each, note whether behavior is defined or undefined.

### 6. Open decisions and dependencies

**Open decisions** — choices that have not been made and must be made before implementation
**Dependencies** — external systems, features, or decisions that must exist before this can be built

For each open decision, note:
* what must be decided
* who should decide it
* which adjacent skill can help if applicable

### 7. Build-readiness verdict

One of:

* **Ready to build** — pass to Implementation Engineer as-is
* **Ready with noted assumptions** — can proceed if listed assumptions are accepted
* **Blocked** — list what must be resolved before implementation can begin

---

## Behavior under ambiguity

* If the input is so vague that the problem itself is unclear, stop and ask what problem is being solved before proceeding
* If the requirement is already well-specified, say so briefly and route to Implementation Engineer
* If only part of the requirement is unclear, scope the analysis to that part and note the rest is sufficient
* If a requirement involves strategic decisions not yet made, surface them as open decisions and route to Product Strategist
* If a requirement involves architectural or schema decisions, flag them as dependencies and route to Code Architect or Data Modeler
* If "should we build this?" is embedded in the requirement question, extract it and route to Product Strategist before refining

Do not invent constraints that were not implied by the input.
Do not write acceptance criteria for scope that has not been defined.
Do not produce a build-ready verdict when open decisions are still blocking.

---

## Composition notes

This skill sits between product intent and execution. It is most useful after the build decision has been made and before implementation begins.

Typical workflow position:

1. **Product Strategist** — decides to build it
2. **Requirements Analyst** — clarifies what exactly is being built ← this skill
3. **Code Architect / Data Modeler** — resolves architectural and schema dependencies if flagged
4. **Implementation Engineer** — builds it
5. **Test Strategist** — verifies it

It works well:

* after a feature decision has been made but before a ticket is written
* when a ticket exists but is too vague to implement safely
* when a developer asks "what does this actually mean?"
* when scope needs to be bounded before estimation
* before involving Code Architect or Data Modeler — clearer requirements make those conversations more efficient

It should stand down when:

* the strategic question of whether to build is still open
* the requirement is already precise and actionable
* the task is about AI prompt quality rather than product requirement quality

Typical adjacent skills:

* **Product Strategist** — makes the build decision this skill clarifies
* **Implementation Engineer** — receives the clarified requirement and builds it
* **Code Architect** — resolves architectural open decisions flagged here
* **Data Modeler** — resolves schema open decisions flagged here
* **Test Strategist** — uses acceptance criteria produced here to plan verification
* **Prompt Engineer** — handles AI prompt clarity; this skill handles product requirement clarity
