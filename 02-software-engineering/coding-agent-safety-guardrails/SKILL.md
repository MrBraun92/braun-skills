---
name: coding-agent-safety-guardrails
description: Set up operational safety guardrails for AI coding agents, especially blocking destructive git, filesystem, deployment, or secret-exposing commands. Use when working with Claude Code, Manus, Codex, or terminal-based agents that can modify repositories.
---

# Coding Agent Safety Guardrails

## Purpose

Protect repositories and development environments from destructive or unauthorized actions by AI coding agents.

This skill defines and configures guardrails for terminal-based coding workflows, especially when agents can run shell commands, edit files, commit changes, or interact with git.

---

## Use this skill when

Use this skill when the task is mainly about:

* preventing destructive git operations
* configuring Claude Code or coding-agent hooks
* blocking risky shell commands
* protecting branches from accidental pushes
* preventing secret exposure
* making agent execution safer
* setting project-level or global AI coding guardrails
* creating rules for what an agent may not do

Strong trigger examples:

* "set up Claude Code guardrails"
* "block dangerous git commands"
* "prevent the agent from pushing code"
* "make this repo safe for AI coding"
* "add safety hooks before Manus/Claude edits files"
* "what commands should agents be forbidden to run?"

---

## Do not use this skill when

Do not use this skill when the task is mainly about:

* security vulnerabilities in application code → Security Reviewer
* release readiness → Release Verifier
* QA execution → QA Executor
* CI quality setup → Repo Quality Setup
* code implementation → Implementation Engineer
* git workflow strategy without agent safety concerns → Delivery Coordinator

---

## Guardrail categories

### Destructive git commands

Block or require explicit approval for:

* `git push`
* `git push --force`
* `git reset --hard`
* `git clean -f`
* `git clean -fd`
* `git branch -D`
* `git checkout .`
* `git restore .`
* deleting remotes or changing remote URLs

### Dangerous filesystem commands

Block or require explicit approval for:

* `rm -rf` outside clearly scoped generated folders
* deleting source directories
* mass file deletion
* moving large folder trees
* overwriting environment files

### Secret and credential risks

Block or flag:

* printing `.env` contents
* committing secrets
* uploading private keys
* exposing tokens in logs
* writing credentials into prompts or docs

### Deployment and external side effects

Require explicit approval for:

* production deploys
* database migrations on shared environments
* destructive database commands
* sending emails to real users
* running paid API jobs
* modifying cloud resources

---

## Workflow

### 1. Determine scope

Clarify whether guardrails apply to:

* this project only
* all local projects
* Claude Code only
* Manus/Codex/other coding agents generally
* CI/CD or local terminal as well

### 2. Inspect current environment

When possible, inspect:

* `.claude/settings.json`
* `.claude/hooks/`
* repo scripts
* package scripts
* deployment scripts
* git remotes and branch conventions
* existing CI checks

### 3. Define blocked and approval-required actions

Create two lists:

* hard-blocked commands
* approval-required commands

### 4. Implement guardrails

Depending on environment, this may include:

* Claude Code PreToolUse hooks
* shell wrapper scripts
* repo documentation
* protected branch rules guidance
* pre-commit checks for secrets
* agent instruction files

### 5. Verify

Run safe dry-run tests to confirm blocked commands are blocked.

Never run destructive commands as a test.

---

## Output format

Always use this structure.

### 1. Safety scope

State what environment and risk surface is being protected.

### 2. Risk assessment

List the main risks for this repo or workflow.

### 3. Guardrails configured or recommended

```md
| Guardrail | Action | Status |
|---|---|---|
| Block git push | Hard block | Configured / Recommended |
```

### 4. Blocked commands

List commands that should not run without explicit human control.

### 5. Approval-required commands

List commands that may be valid but need human approval.

### 6. Verification

Show safe verification steps and results.

### 7. Remaining gaps

State what still needs manual platform configuration, such as GitHub branch protection.

---

## Quality checklist

Before finalizing, verify:

* destructive commands are not executed during setup
* project/global scope is clear
* guardrails do not block normal harmless development
* secret exposure is considered
* deployment side effects are considered
* verification uses safe test inputs
* user remains in control of push/deploy/destructive actions

---

## Composition notes

This skill works well before:

* Implementation Engineer
* TDD Implementation Runner
* Refactor Plan Writer

It complements:

* Repo Quality Setup
* Security Reviewer
* Release Verifier
