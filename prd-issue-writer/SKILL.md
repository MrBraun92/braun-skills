---
name: prd-issue-writer
description: Convert existing conversation context, product ideas, specs, or codebase understanding into a concise PRD formatted as a GitHub issue. Use when the user wants a product requirement artifact that can directly guide implementation.
---

# PRD Issue Writer

## Purpose

Turn already-discussed context into a product requirements document that is ready to become a GitHub issue.

This skill synthesizes. It does not run a long discovery interview unless essential information is missing.

Use it to convert strategic discussion into an implementation-facing artifact.

---

## Use this skill when

Use this skill when the task is mainly about:

* turning a conversation into a PRD
* creating a GitHub issue from product context
* documenting a feature before implementation
* translating user needs into user stories and acceptance criteria
* capturing implementation decisions without over-specifying code
* creating a durable product artifact for an AI coding agent

Strong trigger examples:

* "turn this into a PRD"
* "create a GitHub issue for this feature"
* "write the implementation PRD"
* "convert our conversation into a product spec"
* "document this as a build ticket"

---

## Do not use this skill when

Do not use this skill when the task is mainly about:

* clarifying vague requirements from scratch → Requirements Analyst
* deciding whether the feature should exist → Product Strategist
* breaking a PRD into slices → Vertical Slice Planner
* designing architecture → Code Architect
* implementing code → Implementation Engineer
* test planning → Test Strategist

---

## Workflow

### 1. Gather available context

Use the current conversation, attached notes, codebase context, existing plans, or user-provided brief.

Identify:

* problem
* target users
* desired behavior
* known constraints
* business/product rationale
* implementation decisions already made
* testing expectations
* out-of-scope items

### 2. Avoid over-interviewing

If enough context exists, synthesize directly.

Ask only when a missing decision would materially change the PRD.

### 3. Write durable requirements

Write requirements that stay useful even if file paths, components, or implementation details change.

Prefer:

* user-visible behavior
* system contracts
* acceptance criteria
* constraints
* testing decisions

Avoid brittle line-level or file-specific instructions unless the user explicitly needs them.

### 4. Prepare GitHub-ready issue body

The output should be directly copyable into GitHub.

---

## Output format

Always use this structure.

```md
## Problem Statement

[The problem from the user's perspective.]

## Goal

[The outcome this feature or change should create.]

## Target Users

- [User / actor]

## Solution Overview

[Concise explanation of the proposed solution.]

## User Stories

1. As a [actor], I want [capability], so that [benefit].
2. As a [actor], I want [capability], so that [benefit].

## Functional Requirements

- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Requirement 3

## Acceptance Criteria

- [ ] Observable criterion 1
- [ ] Observable criterion 2
- [ ] Observable criterion 3

## Implementation Decisions

- Decision 1
- Decision 2

## Testing Decisions

- Behavior to test
- Suggested verification layer

## Out of Scope

- Item 1
- Item 2

## Open Questions

- Question 1, if any
```

---

## Quality checklist

Before finalizing, verify:

* the problem is written from the user's perspective
* requirements are specific enough to implement
* acceptance criteria are observable
* user stories are not vague
* out-of-scope boundaries are explicit
* implementation details are durable rather than brittle
* the artifact can be handed to Vertical Slice Planner or Implementation Engineer

---

## Composition notes

This skill works well before:

* Vertical Slice Planner
* TDD Implementation Runner
* Implementation Engineer
* QA Executor

It works well after:

* Requirements Analyst
* Product Strategist
* Code Architect
