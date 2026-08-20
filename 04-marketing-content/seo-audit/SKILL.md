---
name: seo-audit
description: Canonical SEO strategy and audit router. Use for technical SEO, indexing, ranking drops, keyword and content strategy, structured data, Search Console, local or ecommerce SEO, Core Web Vitals, and any request to improve organic visibility in Google. Always checks current Google Search Central documentation before prescribing tactics, then routes execution through vetted professional repositories and available tools.
---

# SEO Audit and Strategy Router

This is the repository's **canonical SEO authority**. Do not rely on memorized SEO rules when current documentation or live evidence can be checked.

## Non-negotiable source order

For every substantive SEO strategy, audit, implementation plan, or recommendation:

1. **Consult current Google Search Central documentation first** at `https://developers.google.com/search?hl=pt-br` and the relevant linked pages.
2. Check the page's **last-updated date** and record the research date in the output.
3. Use first-party Google tools and data when available: Search Console, URL Inspection, Rich Results Test, PageSpeed Insights, CrUX, Lighthouse, Google Trends, Merchant Center, and Business Profile.
4. Use the vetted repositories in `references/source-registry.md` as implementation and diagnostic references, never as authority over Google.
5. Use secondary SEO commentary only to generate hypotheses. Validate each material recommendation against first-party documentation, observed crawl/index data, or a reproducible test.

If sources conflict, Google documentation and direct site evidence win. State uncertainty instead of presenting folklore as a rule.

## Router

Classify the request and run only the necessary modules:

| Request | Route |
|---|---|
| Crawl, indexing, rendering, robots, sitemap, canonicals, redirects | Technical discovery |
| Traffic or ranking decline | Incident diagnosis |
| Keyword, intent, content gaps, topical architecture | Search demand and content |
| Titles, snippets, headings, internal links, media | On-page and information architecture |
| Schema or rich results | Structured data |
| Speed, UX, mobile, CWV | Page experience |
| Local business | Local discovery |
| Products or ecommerce | Commerce discovery |
| International or multilingual | International SEO |
| AI Overviews, AI Mode, ChatGPT, Claude, Gemini, citations | Route jointly to `geo-ai-discovery` |
| Code or implementation changes | Route findings to the appropriate engineering skill after evidence is collected |

## Evidence gate

Before diagnosing a URL or domain, gather as much of the following as access permits:

- crawlable HTML and HTTP status;
- robots.txt, sitemap, canonical, robots meta and response headers;
- rendered page when JavaScript affects important content;
- Search Console Performance, Pages/Indexing and URL Inspection data;
- PageSpeed Insights or CrUX field data and Lighthouse lab data;
- structured-data output from Rich Results Test or Schema Markup Validator;
- internal-link graph, orphan pages, redirect chains and duplicate clusters;
- analytics and conversion data, separated from rankings and impressions;
- date of deployment, migration, redesign, content changes or known Google updates.

Never invent search volume, keyword difficulty, ranking, backlinks, traffic, CWV, domain authority, competitor data, or indexation. Label estimates and proxies explicitly.

## Current-doc verification protocol

At execution time, search or open the exact relevant Google documentation. At minimum, check:

- Search Essentials and spam policies;
- SEO Starter Guide and developer guide;
- crawling/indexing controls;
- canonicalization and duplicate handling;
- sitemaps and robots.txt;
- JavaScript SEO when relevant;
- structured-data feature documentation for the exact type;
- Core Web Vitals and page-experience guidance;
- Search Console documentation and data limitations;
- AI features and your website when AI Overviews or AI Mode are in scope.

Do not freeze numeric limits as universal laws. In particular:

- title and snippet display is query-, device-, and rendering-dependent;
- meta descriptions are suggestions, not guaranteed snippets;
- one H1 can be a useful convention, but multiple H1 elements are not automatically a Google violation;
- word count is not a ranking factor and thinness is judged by usefulness, originality, intent coverage, and evidence rather than a fixed threshold;
- Lighthouse scores are diagnostics, not direct ranking factors;
- structured data must match visible content and does not guarantee a rich result;
- indexing and ranking are never guaranteed.

## Audit workflow

### 1. Define business outcome and search surface

Identify the conversion goal, audience, geography, languages, device mix, page types, search intents, and whether the target is classic results, local, shopping, images, video, news, AI features, or several surfaces.

### 2. Establish baseline

Create a dated baseline for clicks, impressions, CTR, average position, indexed URLs, conversions, branded/non-branded demand, top landing pages, query clusters, CWV, crawl errors, and major releases. Segment before comparing.

### 3. Technical discovery

Test server accessibility, status codes, redirect behavior, robots and noindex controls, canonical consistency, sitemap quality, internal discovery, rendering, mobile parity, pagination/facets, duplicate parameters, hreflang, soft 404s, security, and structured-data eligibility.

Prioritize failures that block crawling, indexing, canonical consolidation, rendering of primary content, or conversion. Do not confuse an audit-tool warning with a confirmed Google issue.

### 4. Search demand and content

Build a query-to-page map based on intent and business value. Review first-party SERPs and competitors for coverage, format, evidence, freshness, entity relationships, and unmet user tasks. Create or improve pages only when they add original value, experience, data, tools, examples, or clearer decision support.

Avoid scaled low-value pages, doorway patterns, copied summaries, keyword stuffing, fabricated expertise, and content created mainly to manipulate rankings.

### 5. On-page and architecture

Evaluate title clarity, heading hierarchy, answer-first structure, descriptive links, page purpose, entity disambiguation, author/company evidence where relevant, media accessibility, internal-link pathways, breadcrumbs, URL consistency, and conversion continuity. Recommendations must fit actual templates and user intent.

### 6. Page experience

Use field data first when available. Diagnose LCP, INP and CLS at page-type level, then use Lighthouse and DevTools to identify causes. Include accessibility, mobile usability, HTTPS, intrusive interstitials, visual stability and interaction quality without reducing the analysis to a single score.

### 7. Structured data

Use only supported types that match visible page content. Validate syntax, required/recommended properties, eligibility rules, policy compliance and template coverage. Treat Schema.org vocabulary and Google rich-result eligibility as related but distinct.

### 8. Validation and monitoring

For every major change define hypothesis, affected templates, expected leading and lagging indicators, deployment date, validation method, rollback condition, and review window. Compare equivalent periods and annotate seasonality, campaigns, migrations and algorithmic volatility.

## Professional repository router

Use the five selected repositories according to purpose; inspect their current README, release activity, issues and implementation before reusing anything:

1. `GoogleChrome/lighthouse` — reproducible performance, accessibility, best-practice and basic SEO diagnostics.
2. `harlan-zw/unlighthouse` — site-wide Lighthouse crawling and aggregated template diagnostics.
3. `StJudeWasHere/seonaut` — open-source technical crawler and issue inventory.
4. `eliasdabbas/advertools` plus `eliasdabbas/seo-audit-and-analysis` — programmatic crawling, robots/sitemap/log/SERP analysis and reproducible notebooks.
5. `AgriciDaniel/claude-seo` — LLM-native orchestration patterns, falsifiability and specialist coverage. Treat it as a workflow reference, not a source of search-engine truth.

Additional candidates may be evaluated, but they do not replace this core set without checking maintenance, licensing, security, evidence quality and overlap. See `references/source-registry.md`.

## Required output

Deliver:

1. **Executive finding** with the most likely constraint and business consequence.
2. **Evidence ledger** with source, observed fact, date, confidence and limitation.
3. **Issue table** with URL/template, evidence, severity, impact, recommended action and validation.
4. **Prioritized roadmap** split into blockers, high-leverage improvements and experiments.
5. **Implementation notes** with owners, dependencies and acceptance criteria.
6. **Measurement plan** with baseline, KPIs, segmentation and review dates.
7. **Sources consulted**, including exact official Google pages and repository references.

Use severity based on demonstrated impact:

- **Critical:** prevents access, indexation, canonical consolidation, legal/safety compliance, or core conversion.
- **High:** affects a major template, high-value demand, or broad user experience.
- **Medium:** supported opportunity with limited scope or uncertain magnitude.
- **Low:** hygiene or experiment, not a ranking emergency.

## Completion gate

Do not call the strategy optimized until:

- current Google documentation was checked;
- live evidence or explicit missing-data limitations are shown;
- recommendations are prioritized by business impact and confidence;
- no unsupported guarantee is made;
- implementation has acceptance tests and monitoring;
- GEO implications were routed to `geo-ai-discovery` when applicable.
