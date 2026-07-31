---
name: geo-ai-discovery
description: Canonical GEO, AEO, AI-search and agent-discovery router. Use when optimizing a website, app, product or brand to be discovered, retrieved, cited, recommended or used by ChatGPT, Gemini, Claude, AI Overviews, AI Mode, deep research systems and web agents. Always checks current first-party documentation from OpenAI, Google and Anthropic, distinguishes search/retrieval from model training, and produces a measurable evidence-based strategy without promising inclusion.
---

# GEO and AI Discovery Router

This skill governs **Generative Engine Optimization (GEO)**, answer-engine optimization, AI-search visibility, citation readiness and agent accessibility.

No strategy can guarantee that an AI system will cite, recommend or use a site. The goal is to maximize technical eligibility, retrievability, source usefulness, entity confidence and measurable business outcomes while preserving the publisher's training and access choices.

## Mandatory freshness rule

Before every substantive strategy or audit:

1. Consult current first-party documentation from:
   - OpenAI publisher/developer guidance;
   - Anthropic crawler and web-search guidance;
   - Google Search Central, especially AI features, Search Essentials, structured data and crawler controls.
2. Record the execution date and the last-updated date when visible.
3. Check official robot names and policy changes at execution time. Never assume crawler names or behavior from memory.
4. Consult the peer-reviewed and reputable research registry in `references/source-registry.md` for hypotheses and measurement design.
5. Use third-party GEO repositories only as implementation references. Validate tactics against official documentation and controlled tests.

## Core distinction: four separate permissions

Do not collapse these controls into one concept:

1. **Classic search crawling/indexing**: whether a search engine may crawl and index a page.
2. **AI search/retrieval**: whether an AI search or user-directed retrieval agent may access the page.
3. **Model training**: whether content may be collected for potential model development or training.
4. **Interactive agent use**: whether an agent can understand and operate a site's forms, menus, buttons, APIs or app actions.

A site may allow discovery while disallowing training. Make this distinction explicit in every robots and crawler recommendation.

## Platform router

### OpenAI / ChatGPT

At execution time, verify official guidance and current user agents. The baseline model is:

- allow the official search crawler when the publisher wants discoverability in ChatGPT search;
- make deliberate, separate choices for the training crawler;
- preserve access for user-directed retrieval when desired;
- use `noindex` or snippet controls only with a clear understanding of their effects;
- track ChatGPT referrals and tagged inbound traffic in analytics;
- for agent usability, use semantic HTML, accessible names, descriptive labels, predictable controls, valid states and robust mobile layouts.

Do not infer that allowing a training crawler improves ranking or citation. Do not infer that blocking training necessarily blocks search retrieval.

### Anthropic / Claude

At execution time, verify Anthropic's current crawler documentation. Treat the documented roles separately:

- model-development crawler;
- search-quality crawler;
- user-initiated retrieval agent.

Allow or block each based on the site's policy. Test that CDN, WAF, rate limits and robots rules produce the intended result. For agent usability, favor accessible, deterministic interfaces and clear page semantics.

### Google / Gemini and AI features

For Google Search AI Overviews and AI Mode, route technical eligibility through `seo-audit`. Google states that foundational SEO remains the basis for appearing in these search features and that no special AI file or special schema is required merely for eligibility. A supporting page generally needs to be indexed and eligible to appear with a snippet.

Keep these controls distinct:

- Googlebot and normal Search controls govern crawling/indexing and Search AI features;
- preview controls such as `nosnippet`, `data-nosnippet`, `max-snippet` and `noindex` affect what may appear;
- Google-Extended governs specified uses outside normal Google Search and must not be treated as the switch for AI Overviews or AI Mode without checking current documentation.

For Gemini products outside Search, verify the exact official product guidance rather than extrapolating from Google Search.

## GEO strategy layers

### 1. Eligibility and access

Audit:

- HTTP availability and stable canonical URLs;
- robots.txt for each relevant crawler;
- noindex and snippet controls;
- CDN/WAF blocks, bot challenges, geo restrictions and rate limits;
- XML sitemaps and internal discovery;
- server-rendered or reliably rendered primary content;
- page speed, mobile access and accessible interaction;
- public versus authenticated content boundaries;
- licensing, consent, privacy and publisher policy.

Provide a crawler-policy matrix with columns for platform, user agent, purpose, current rule, desired rule, evidence and risk.

### 2. Retrieval and passage usefulness

Create content that can answer real tasks, not content designed to imitate an LLM response. Improve:

- clear page purpose and answer-first summaries;
- precise definitions, steps, comparisons and decision criteria;
- self-contained passages with enough context to quote accurately;
- descriptive headings and anchors;
- stable facts, dates, units and version labels;
- original research, first-party data, examples, demonstrations and expert experience;
- transparent sourcing and links to primary evidence;
- explicit limitations, assumptions and update dates;
- tables and structured lists only when they improve comprehension;
- text equivalents for important visual, audio or interactive information.

Never fabricate statistics, citations, testimonials, authorship, experience or consensus.

### 3. Entity and authority confidence

Strengthen consistent, verifiable identity across the web:

- organization, product, people, locations and service relationships;
- accurate About, Contact, editorial and policy pages;
- author and reviewer information where relevant;
- consistent names, descriptions, addresses, identifiers and social profiles;
- reputable third-party mentions, reviews, directories and citations;
- primary-source documentation, changelogs, APIs and support materials;
- structured data that matches visible content and official eligibility rules.

Schema is a machine-readable clarification layer, not a citation guarantee.

### 4. Distribution and corroboration

Identify the sources likely to be consulted for the target query class: official documentation, recognized media, specialist publications, communities, marketplaces, academic sources, app directories, review sites and local listings. Build legitimate visibility through useful contributions, public data, integrations, partnerships, case studies and expert commentary.

Do not recommend link schemes, fake reviews, mass-generated profiles, reputation manipulation, hidden text, doorway pages or synthetic consensus.

### 5. Agent readiness

When a site or app should be usable by AI agents, test:

- semantic HTML and ARIA labels;
- keyboard-operable controls;
- explicit button and form labels;
- deterministic navigation and clear error states;
- stable URLs and deep links;
- authentication and confirmation boundaries;
- safe idempotent actions where possible;
- APIs, OpenAPI descriptions, app integrations or platform-specific app protocols when officially supported;
- resistance to prompt injection and untrusted page instructions;
- privacy-preserving defaults and human confirmation for consequential actions.

Agent accessibility is not identical to SEO or citation optimization. Report it separately.

## Research and experiment protocol

Research findings are probabilistic and engine-specific. The foundational GEO literature and subsequent empirical work may indicate useful patterns, but results vary across engines, query wording, location, time and repeated runs.

For each experiment:

1. define target audience, decision and query set;
2. include branded, non-branded, comparison, problem, local and transactional prompts as relevant;
3. freeze a dated test set and record engine/model/product, account state, locale and run time;
4. repeat prompts across multiple runs;
5. separate mention, citation, linked citation, recommendation, ranking/order and factual accuracy;
6. compare against a control or pre-change baseline;
7. record source overlap and volatility;
8. evaluate downstream qualified visits, actions and conversions;
9. avoid automating queries in ways that violate product terms;
10. report uncertainty and sample limitations.

## Metrics

Measure four layers independently:

| Layer | Example metrics |
|---|---|
| Eligibility | crawler access, indexability, render success, snippet eligibility, agent task completion |
| Visibility | mention rate, citation rate, linked-citation rate, share of cited sources, query coverage |
| Quality | factual fidelity, correct entity attribution, passage support, sentiment/context, citation stability |
| Business | qualified referral sessions, assisted conversions, leads, purchases, app actions, revenue, support deflection |

A mention without a link is not traffic. A citation is not endorsement. A recommendation is not conversion.

## Required output

Deliver:

1. **Executive assessment**: eligibility, retrievability, authority, agent readiness and business measurement.
2. **Platform matrix**: OpenAI, Anthropic, Google and any additional engine requested.
3. **Crawler policy**: exact current official user agents and proposed allow/block logic.
4. **Evidence ledger**: claim, source, date, confidence and limitation.
5. **Content and entity gaps**: prioritized by query and business value.
6. **Technical implementation plan**: file/template, change, owner, acceptance test and rollback risk.
7. **Experiment plan**: fixed prompts, controls, repeated runs and measurement cadence.
8. **Source list**: official docs, research papers and repositories consulted during that run.

## Completion gate

Do not call a GEO strategy complete until:

- current official OpenAI, Anthropic and Google guidance was checked;
- search/retrieval, training and user-agent access were separated;
- robots recommendations were tested against the actual site stack;
- claims are supported and dated;
- tactics are framed as hypotheses where evidence is uncertain;
- SEO foundations were routed to `seo-audit`;
- citation and referral measurement is defined;
- no guarantee of inclusion, citation, ranking or recommendation is made.
