# Engenharia de Software e Arquitetura / Software Engineering & Architecture

---

## 🇧🇷 Português

Este diretório reúne as **Agent Skills** especializadas em arquitetura de software, codificação, testes e deploy.

### Skills disponíveis

| Skill | Descrição |
|---|---|
| [architecture](./architecture/SKILL.md) | Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decisio... |
| [bug-triage-tdd-planner](./bug-triage-tdd-planner/SKILL.md) | Investigate reported bugs, identify likely root cause, and produce a TDD-based fix plan with RED-GREEN cycles. Use when a bug needs diagnosis befor... |
| [code-architect](./code-architect/SKILL.md) | Use for system structure, module boundaries, separation of concerns, coupling, dependency direction, and architectural scalability. Not for code sm... |
| [code-auditor](./code-auditor/SKILL.md) | Use for code smells, readability, maintainability, technical debt, PR review, and refactor-readiness in existing code. Not for architecture, perfor... |
| [coding-agent-safety-guardrails](./coding-agent-safety-guardrails/SKILL.md) | Set up operational safety guardrails for AI coding agents, especially blocking destructive git, filesystem, deployment, or secret-exposing commands... |
| [continue-work](./continue-work/SKILL.md) | Recovers context between sessions across Claude / Manus / GPT — reads the latest commits, CLAUDE.md, MEMORY.md, the current git status / branch / u... |
| [data-modeler](./data-modeler/SKILL.md) | Use for entity design, schema shape, relationships, cardinality, data ownership, normalization trade-offs, and storage-model clarity. Not for syste... |
| [database-optimizer](./database-optimizer/SKILL.md) | Identifies slow queries, N+1 patterns, missing indexes, and bad execution plans in the EventPro stack (Drizzle ORM + MySQL/TiDB Cloud). Suggests id... |
| [debug](./debug/SKILL.md) | Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not ... |
| [deep-module-architect](./deep-module-architect/SKILL.md) | Identify opportunities to turn shallow modules into deep modules with smaller interfaces, stronger seams, better locality, and higher leverage. Use... |
| [deploy-checklist](./deploy-checklist/SKILL.md) | Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI... |
| [devops-sre-agent](./devops-sre-agent/SKILL.md) | Use for cloud infrastructure management, uptime monitoring, load testing, incident response (downtime), and CI/CD pipeline optimization. Not for ap... |
| [domain-language-cartographer](./domain-language-cartographer/SKILL.md) | Extract, normalize, and document domain terminology into a canonical glossary with definitions, relationships, aliases to avoid, and ambiguity flag... |
| [error-detective](./error-detective/SKILL.md) | Root-cause analysis for production errors in EventPro — cross-references stack trace, server logs (pino / console), recent git log, the lines of co... |
| [github-gem-seeker](./github-gem-seeker/SKILL.md) | > |
| [implementation-engineer](./implementation-engineer/SKILL.md) | Use for building, implementing, scaffolding, prototyping, and writing code when requirements are clear enough to execute. Not for reviewing existin... |
| [incident-response](./incident-response/SKILL.md) | Run an incident response workflow — triage, communicate, and write postmortem. Trigger with "we have an incident", "production is down", an alert t... |
| [module-interface-designer](./module-interface-designer/SKILL.md) | Design and compare alternative technical interfaces for modules, APIs, services, adapters, and contracts. Use when a system needs a clean contract ... |
| [performance-reviewer](./performance-reviewer/SKILL.md) | Use for runtime cost, latency, bottlenecks, query cost, rendering cost, throughput, and scale-related performance diagnosis. Not for code-quality r... |
| [production-reviewer](./production-reviewer/SKILL.md) | Use for interpreting production telemetry — logs, error signals, incident patterns, operational degradation, and post-deploy signals — to distingui... |
| [publish-rendercv-typst-package](./publish-rendercv-typst-package/SKILL.md) | Create a PR to publish a new version of the rendercv-typst package to the Typst Universe (typst/packages repository). Validates package integrity, ... |
| [rag-architect](./rag-architect/SKILL.md) | Designs end-to-end RAG architecture for the EventPro AI Chat (currently OpenAI-based, in server/routers/ai.ts) — chunking strategy, embedding model... |
| [react-expert](./react-expert/SKILL.md) | Senior React expert for the EventPro stack — React 19 + Vite 7 + TypeScript strict + Tailwind 4 + shadcn/ui (Radix) + wouter + @tanstack/react-quer... |
| [refactor-plan-writer](./refactor-plan-writer/SKILL.md) | Create safe refactor plans broken into tiny working commits with scope, decisions, tests, and out-of-scope boundaries. Use when a refactor needs to... |
| [refactoring-specialist](./refactoring-specialist/SKILL.md) | Performs safe, incremental refactors of large components and modules in the EventPro stack — extract component, extract hook, lift state, split fil... |
| [release-verifier](./release-verifier/SKILL.md) | Use for pre-release verification planning, smoke test prioritization, regression risk assessment, critical path validation, launch-blocker identifi... |
| [rendercv-development-context](./rendercv-development-context/SKILL.md) | RenderCV codebase architecture, source code standards, and project references. Use when writing or reviewing RenderCV code. |
| [rendercv-testing-context](./rendercv-testing-context/SKILL.md) | RenderCV test authoring standards, structure, and conventions. Use when writing or reviewing tests. |
| [repo-quality-setup](./repo-quality-setup/SKILL.md) | Configure repository quality gates such as formatting, linting, type checking, tests, pre-commit hooks, and staged-file checks. Use when a repo nee... |
| [repomix-safe-mixer](./repomix-safe-mixer/SKILL.md) | Packages a repository (or a subset) into a single bundle file suitable for sending to Claude / Manus / GPT — with secret detection and masking appl... |
| [review-rendercv-pr](./review-rendercv-pr/SKILL.md) | Review a GitHub pull request against RenderCV's codebase standards, architecture, and test requirements, then post a detailed review. |
| [runbook](./runbook/SKILL.md) | Create or update an operational runbook for a recurring task or procedure. Use when documenting a task that on-call or ops needs to run repeatably,... |
| [secops-agent](./secops-agent/SKILL.md) | Use for managing security operations, IAM (Identity and Access Management), data privacy compliance (LGPD/GDPR), vulnerability monitoring, and secu... |
| [security-reviewer](./security-reviewer/SKILL.md) | Use for auth, permissions, secrets, input handling, attack surface, exploitability risk, and security-sensitive design or implementation review. No... |
| [solve-rendercv-issue](./solve-rendercv-issue/SKILL.md) | Pick up a GitHub issue (or accept one), fully understand the RenderCV codebase, implement the fix/feature with tests, and open a PR to origin/main. |
| [system-design](./system-design/SKILL.md) | Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right ... |
| [tdd-implementation-runner](./tdd-implementation-runner/SKILL.md) | Execute feature development or bug fixes using a strict red-green-refactor loop. Use when implementation should be test-first, behavior-driven, inc... |
| [tech-debt](./tech-debt/SKILL.md) | Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or... |
| [test-automator-playwright](./test-automator-playwright/SKILL.md) | Generates end-to-end tests with Playwright for the EventPro SaaS (React 19 + Vite + tRPC + Drizzle/MySQL TiDB + AWS S3). Covers login, event creati... |
| [test-strategist](./test-strategist/SKILL.md) | Use for test strategy, coverage planning, regression risk, edge cases, and deciding what to verify at unit, integration, or end-to-end level. Not f... |
| [triage-rendercv-issue](./triage-rendercv-issue/SKILL.md) | Analyze a newly opened GitHub issue, comment with findings and an action plan, and offer to open a PR. |
| [verification-before-completion](./verification-before-completion/SKILL.md) | Operational gate that prevents an agent (or the user) from declaring a task "done" before producing concrete evidence — build OK, tests passing, li... |
| [vertical-slice-planner](./vertical-slice-planner/SKILL.md) | Break PRDs, specs, plans, or feature ideas into thin independently implementable vertical-slice GitHub issues. Use when work needs to be decomposed... |

### Como usar

Cada skill vive em sua própria pasta com um arquivo `SKILL.md` no formato canônico. Para ativar uma skill no Manus ou no Claude, compartilhe a URL raw do `SKILL.md` correspondente.

---

## 🇺🇸 English

This directory contains **Agent Skills** specialized in software architecture, coding, testing, and deployment.

### Available Skills

| Skill | Description |
|---|---|
| [architecture](./architecture/SKILL.md) | Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decisio... |
| [bug-triage-tdd-planner](./bug-triage-tdd-planner/SKILL.md) | Investigate reported bugs, identify likely root cause, and produce a TDD-based fix plan with RED-GREEN cycles. Use when a bug needs diagnosis befor... |
| [code-architect](./code-architect/SKILL.md) | Use for system structure, module boundaries, separation of concerns, coupling, dependency direction, and architectural scalability. Not for code sm... |
| [code-auditor](./code-auditor/SKILL.md) | Use for code smells, readability, maintainability, technical debt, PR review, and refactor-readiness in existing code. Not for architecture, perfor... |
| [coding-agent-safety-guardrails](./coding-agent-safety-guardrails/SKILL.md) | Set up operational safety guardrails for AI coding agents, especially blocking destructive git, filesystem, deployment, or secret-exposing commands... |
| [continue-work](./continue-work/SKILL.md) | Recovers context between sessions across Claude / Manus / GPT — reads the latest commits, CLAUDE.md, MEMORY.md, the current git status / branch / u... |
| [data-modeler](./data-modeler/SKILL.md) | Use for entity design, schema shape, relationships, cardinality, data ownership, normalization trade-offs, and storage-model clarity. Not for syste... |
| [database-optimizer](./database-optimizer/SKILL.md) | Identifies slow queries, N+1 patterns, missing indexes, and bad execution plans in the EventPro stack (Drizzle ORM + MySQL/TiDB Cloud). Suggests id... |
| [debug](./debug/SKILL.md) | Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not ... |
| [deep-module-architect](./deep-module-architect/SKILL.md) | Identify opportunities to turn shallow modules into deep modules with smaller interfaces, stronger seams, better locality, and higher leverage. Use... |
| [deploy-checklist](./deploy-checklist/SKILL.md) | Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI... |
| [devops-sre-agent](./devops-sre-agent/SKILL.md) | Use for cloud infrastructure management, uptime monitoring, load testing, incident response (downtime), and CI/CD pipeline optimization. Not for ap... |
| [domain-language-cartographer](./domain-language-cartographer/SKILL.md) | Extract, normalize, and document domain terminology into a canonical glossary with definitions, relationships, aliases to avoid, and ambiguity flag... |
| [error-detective](./error-detective/SKILL.md) | Root-cause analysis for production errors in EventPro — cross-references stack trace, server logs (pino / console), recent git log, the lines of co... |
| [github-gem-seeker](./github-gem-seeker/SKILL.md) | > |
| [implementation-engineer](./implementation-engineer/SKILL.md) | Use for building, implementing, scaffolding, prototyping, and writing code when requirements are clear enough to execute. Not for reviewing existin... |
| [incident-response](./incident-response/SKILL.md) | Run an incident response workflow — triage, communicate, and write postmortem. Trigger with "we have an incident", "production is down", an alert t... |
| [module-interface-designer](./module-interface-designer/SKILL.md) | Design and compare alternative technical interfaces for modules, APIs, services, adapters, and contracts. Use when a system needs a clean contract ... |
| [performance-reviewer](./performance-reviewer/SKILL.md) | Use for runtime cost, latency, bottlenecks, query cost, rendering cost, throughput, and scale-related performance diagnosis. Not for code-quality r... |
| [production-reviewer](./production-reviewer/SKILL.md) | Use for interpreting production telemetry — logs, error signals, incident patterns, operational degradation, and post-deploy signals — to distingui... |
| [publish-rendercv-typst-package](./publish-rendercv-typst-package/SKILL.md) | Create a PR to publish a new version of the rendercv-typst package to the Typst Universe (typst/packages repository). Validates package integrity, ... |
| [rag-architect](./rag-architect/SKILL.md) | Designs end-to-end RAG architecture for the EventPro AI Chat (currently OpenAI-based, in server/routers/ai.ts) — chunking strategy, embedding model... |
| [react-expert](./react-expert/SKILL.md) | Senior React expert for the EventPro stack — React 19 + Vite 7 + TypeScript strict + Tailwind 4 + shadcn/ui (Radix) + wouter + @tanstack/react-quer... |
| [refactor-plan-writer](./refactor-plan-writer/SKILL.md) | Create safe refactor plans broken into tiny working commits with scope, decisions, tests, and out-of-scope boundaries. Use when a refactor needs to... |
| [refactoring-specialist](./refactoring-specialist/SKILL.md) | Performs safe, incremental refactors of large components and modules in the EventPro stack — extract component, extract hook, lift state, split fil... |
| [release-verifier](./release-verifier/SKILL.md) | Use for pre-release verification planning, smoke test prioritization, regression risk assessment, critical path validation, launch-blocker identifi... |
| [rendercv-development-context](./rendercv-development-context/SKILL.md) | RenderCV codebase architecture, source code standards, and project references. Use when writing or reviewing RenderCV code. |
| [rendercv-testing-context](./rendercv-testing-context/SKILL.md) | RenderCV test authoring standards, structure, and conventions. Use when writing or reviewing tests. |
| [repo-quality-setup](./repo-quality-setup/SKILL.md) | Configure repository quality gates such as formatting, linting, type checking, tests, pre-commit hooks, and staged-file checks. Use when a repo nee... |
| [repomix-safe-mixer](./repomix-safe-mixer/SKILL.md) | Packages a repository (or a subset) into a single bundle file suitable for sending to Claude / Manus / GPT — with secret detection and masking appl... |
| [review-rendercv-pr](./review-rendercv-pr/SKILL.md) | Review a GitHub pull request against RenderCV's codebase standards, architecture, and test requirements, then post a detailed review. |
| [runbook](./runbook/SKILL.md) | Create or update an operational runbook for a recurring task or procedure. Use when documenting a task that on-call or ops needs to run repeatably,... |
| [secops-agent](./secops-agent/SKILL.md) | Use for managing security operations, IAM (Identity and Access Management), data privacy compliance (LGPD/GDPR), vulnerability monitoring, and secu... |
| [security-reviewer](./security-reviewer/SKILL.md) | Use for auth, permissions, secrets, input handling, attack surface, exploitability risk, and security-sensitive design or implementation review. No... |
| [solve-rendercv-issue](./solve-rendercv-issue/SKILL.md) | Pick up a GitHub issue (or accept one), fully understand the RenderCV codebase, implement the fix/feature with tests, and open a PR to origin/main. |
| [system-design](./system-design/SKILL.md) | Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right ... |
| [tdd-implementation-runner](./tdd-implementation-runner/SKILL.md) | Execute feature development or bug fixes using a strict red-green-refactor loop. Use when implementation should be test-first, behavior-driven, inc... |
| [tech-debt](./tech-debt/SKILL.md) | Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or... |
| [test-automator-playwright](./test-automator-playwright/SKILL.md) | Generates end-to-end tests with Playwright for the EventPro SaaS (React 19 + Vite + tRPC + Drizzle/MySQL TiDB + AWS S3). Covers login, event creati... |
| [test-strategist](./test-strategist/SKILL.md) | Use for test strategy, coverage planning, regression risk, edge cases, and deciding what to verify at unit, integration, or end-to-end level. Not f... |
| [triage-rendercv-issue](./triage-rendercv-issue/SKILL.md) | Analyze a newly opened GitHub issue, comment with findings and an action plan, and offer to open a PR. |
| [verification-before-completion](./verification-before-completion/SKILL.md) | Operational gate that prevents an agent (or the user) from declaring a task "done" before producing concrete evidence — build OK, tests passing, li... |
| [vertical-slice-planner](./vertical-slice-planner/SKILL.md) | Break PRDs, specs, plans, or feature ideas into thin independently implementable vertical-slice GitHub issues. Use when work needs to be decomposed... |

### How to Use

Each skill lives in its own folder with a canonical `SKILL.md` file. To activate a skill in Manus or Claude, share the raw URL of the corresponding `SKILL.md`.
