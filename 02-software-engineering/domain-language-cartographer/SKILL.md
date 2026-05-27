---
name: domain-language-cartographer
description: Extract, normalize, and document domain terminology into a canonical glossary with definitions, relationships, aliases to avoid, and ambiguity flags. Use before product modeling, data modeling, architecture, or AI-agent implementation when domain language needs consistency.
---

# Domain Language Cartographer

## Purpose

Create a canonical language map for a product, business domain, or software system.

This skill extracts domain terms from conversation, documents, specs, interviews, or codebase context and turns them into a precise glossary that humans and AI agents can use consistently.

It reduces ambiguity before requirements, data modeling, architecture, and implementation.

---

## Use this skill when

Use this skill when the task is mainly about:

* defining domain terms
* creating a glossary
* resolving ambiguous terminology
* identifying synonyms and aliases to avoid
* aligning product, business, and technical language
* preparing for data modeling or architecture
* making a domain easier for AI agents to reason about
* documenting relationships between concepts

Strong trigger examples:

* "create a domain glossary"
* "map the language of this product"
* "define the key terms for EventPro"
* "what terms are ambiguous here?"
* "standardize our domain vocabulary"
* "create ubiquitous language"

---

## Do not use this skill when

Do not use this skill when the task is mainly about:

* schema/entity design → Data Modeler
* module/API design → Module Interface Designer
* product prioritization → Product Strategist
* writing marketing positioning → Positioning Strategist
* implementation → Implementation Engineer
* academic thematic coding → Interview Intelligence Analyst

---

## Core principles

Good domain language:

* uses one canonical term for one concept
* avoids multiple names for the same thing
* avoids one word meaning many things
* defines what something is, not just what it does
* captures relationships between concepts
* uses business/user language before technical jargon
* helps future agents avoid hallucinating product structure

---

## Workflow

### 1. Scan source material

Use conversation context, specs, interviews, product docs, codebase comments, UI text, spreadsheets, or user notes.

Extract:

* nouns
* roles
* lifecycle states
* events
* workflows
* business objects
* metrics
* financial terms
* operational terms

### 2. Cluster terms

Group related terms by domain area, such as:

* people and roles
* core objects
* lifecycle states
* financial concepts
* workflow actions
* external integrations
* reporting metrics

### 3. Resolve ambiguity

Identify:

* same term used for different concepts
* different terms used for the same concept
* terms that are too vague
* terms borrowed from other domains that may mislead implementation

Choose canonical terms and list aliases to avoid.

### 4. Define relationships

Document how terms relate:

* one-to-one
* one-to-many
* parent-child
* lifecycle transitions
* ownership
* dependency

### 5. Produce a durable glossary

The glossary should be useful for product, data modeling, architecture, prompts, and implementation.

---

## Output format

Always use this structure.

### 1. Domain language verdict

Briefly state whether the current language is clear or has ambiguity risk.

### 2. Canonical glossary

Group terms into tables:

```md
## [Domain group]

| Term | Definition | Aliases to avoid | Notes |
|---|---|---|---|
| **Term** | One-sentence definition. | Alias 1, Alias 2 | Optional note |
```

### 3. Relationships

Use bullets:

* A **Producer** owns one or more **Events**.
* An **Event** has many **Budget Items**.
* A **Budget Item** may become an **Actual Expense**.

### 4. Flagged ambiguities

For each ambiguity:

```md
- "Term" was used to mean [A] and [B]. Recommendation: use **Canonical A** for [A] and **Canonical B** for [B].
```

### 5. Example domain dialogue

Write a short dialogue between a domain expert and developer showing the terms used correctly.

### 6. Suggested next skills

Recommend whether to hand off to:

* Data Modeler
* Requirements Analyst
* Module Interface Designer
* Code Architect
* UX Writer

---

## Quality checklist

Before finalizing, verify:

* each definition is one sentence where possible
* terms are domain-relevant, not generic programming concepts
* aliases to avoid are listed
* ambiguous terms are flagged explicitly
* relationships are documented
* the glossary would help an AI coding agent avoid confusion

---

## Composition notes

This skill works well before:

* Data Modeler
* Code Architect
* Module Interface Designer
* Requirements Analyst
* UX Writer

It works well after:

* Interview Intelligence Analyst
* Product Strategist
* Customer Signal Synthesizer
