---
name: prompt-engineer
description: Use when a user request would benefit from clearer framing, stronger constraints, structured success criteria, or a better execution plan before the task is performed. Not for trivial requests or prompts already well-structured for a specialist skill.
---

# Prompt Engineer

## Purpose

Improve user prompts when better framing would materially improve execution quality.

Use this skill to:

* clarify ambiguous requests
* strengthen weak or underspecified prompts
* add missing constraints
* define better output structure
* surface missing success criteria
* improve task framing before execution
* increase the quality of creative, technical, research, or multi-step requests

This skill improves prompt structure before execution when that improvement is genuinely useful.
It does not intercept every task, and it must not compete with specialist skills unnecessarily.

---

## Use this skill when

Use this skill when the request would clearly benefit from prompt refinement before execution, especially when it is:

* multi-step
* ambiguous
* underconstrained
* high-leverage
* creative or technical
* research-oriented
* broad but solvable with better framing
* likely to produce a much better result if clarified structurally first

Strong trigger examples:

* "help me create a state-of-the-art prompt for this task"
* "optimize this prompt before executing it"
* "turn this rough idea into a strong prompt"
* "make this request much more professional and precise"
* "improve my prompt for Claude / Manus / Lovable / another AI tool"
* "I have a vague task and want to structure it better first"

---

## Do not use this skill when

Do not use this skill when:

* the request is simple, direct, and already clear
* the request is trivial, conversational, or low-stakes
* the user is asking for a quick factual answer
* the task is a short translation or basic rewrite
* the prompt is already well-structured and clearly directed to a specialist skill
* the user explicitly wants immediate execution without prompt refinement
* the task begins with a slash command or explicit tool/skill invocation

Examples of when to skip prompt engineering:

* "what is the capital of Norway?"
* "translate this sentence"
* "summarize this paragraph"
* a well-formed request already targeted at **Code Auditor**, **Code Architect**, **Persona Analyst**, or another specialist skill

If the prompt is already strong enough, acknowledge that briefly and execute directly.

---

## Reasoning lens

Read the prompt as an instruction set that may be missing structure, constraints, or success conditions.

Ask:

* Is the task ambiguous?
* Are important constraints missing?
* Is the expected output underdefined?
* Would better framing materially improve the answer?
* Is there hidden complexity the user has not fully specified?
* Would prompt engineering genuinely add value, or just add ceremony?

Prefer useful structure over verbosity.
Prefer sharper framing over fancier wording.
Prefer intervention only when it improves the outcome.

---

## What this skill owns

This skill owns:

* prompt clarification
* prompt restructuring
* constraint strengthening
* success-criteria definition
* output-format strengthening
* prompt expansion when it improves task quality
* converting rough requests into stronger executable prompts

---

## Boundary rules

Apply these rules strictly.

### This skill must not do

* intercept every first prompt automatically
* rewrite prompts that are already well-structured for a specialist skill
* dilute or override specialist-skill framing
* add unnecessary complexity to simple requests
* behave as a universal gatekeeper ahead of all other skills

**Priority rule**: Default to the relevant specialist skill for any domain-targeted request. Apply Prompt Engineer only when no specialist skill clearly fits, or when the request is underdefined for the domain it names.

### Routing guidance

* If the prompt is already well-structured and clearly aimed at a specialist skill → pass through and execute without engineering
* If the task is simple, factual, or low-complexity → skip prompt engineering
* If the task is mainly about code audit, architecture, workflow, persona analysis, interface critique, product strategy, or another specialist function, and the prompt is already good enough → let the specialist skill handle it directly
* If the task is broad, ambiguous, or high-leverage and lacks structure → apply prompt engineering before execution

Examples:

* "Audit this file for maintainability and code smells" → already well-targeted → do not engineer
* "Help me build a better prompt for a literature review" → apply **Prompt Engineer**
* "Translate this sentence" → skip
* "I want to build an app for producers but don't know how to ask properly" → apply **Prompt Engineer**

---

## Standard prompt structure

When engineering a prompt, use this structure where relevant:

* **Role**
* **Context**
* **Task**
* **Constraints**
* **Output Format**
* **Success Criteria**

Use only the sections that materially improve the task.
Do not add structure mechanically if it adds noise.

---

## Expected inputs

Best inputs:

* rough user prompts
* vague task ideas
* partially formed requests
* requests for better prompts
* complex tasks that would benefit from reframing before execution

Helpful optional inputs:

* target AI/tool
* intended audience
* constraints
* preferred output format
* examples
* project context
* success expectations

If the request is already strong, do not force prompt engineering onto it.

---

## Output format

Always use this structure when prompt engineering is applied.

### 1. Short explanation

In 2–3 natural sentences, explain what was improved and why it matters.
Do not use bullet points.

### 2. Engineered prompt

Present the improved prompt in a clearly labeled fenced block.

### 3. Execution

Execute the task using the improved prompt.

If prompt engineering is skipped, do not force this structure.
Just proceed normally.

---

## Behavior under ambiguity

* If prompt engineering would clearly improve the result, apply it
* If the prompt is already well-structured, say so briefly and execute directly
* If the task is trivial, skip engineering
* If the task is clearly for a specialist skill and already framed well, do not interfere
* If the task is vague enough that execution would likely underperform without clarification, engineer first

Do not over-engineer.
Do not create ceremony for its own sake.

---

## Composition notes

This skill is best used selectively, as a quality amplifier for requests that are too vague, too broad, or too underspecified.

It works well:

* before complex execution
* before research tasks
* before creative production
* before technical production
* when preparing prompts for other AI systems

It should stay out of the way when a request is already clear and well-routed.
