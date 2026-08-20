# GEO and AI Discovery Source Registry

This registry must be refreshed at execution time. AI search products, crawler names, access rules and measurement behavior change quickly.

## Source hierarchy

1. Current first-party platform documentation
2. Direct technical tests on the target website or app
3. Peer-reviewed papers and well-documented empirical studies
4. Maintained open-source tools and repositories
5. Reputable practitioner research, clearly labeled as secondary evidence

## OpenAI official sources

- Publishers and Developers FAQ: https://help.openai.com/en/articles/12627856
- OpenAI crawler documentation and IP ranges: verify the current official page linked from the FAQ at execution time
- OpenAI platform documentation: https://platform.openai.com/docs
- Apps SDK documentation: https://developers.openai.com/apps-sdk

### Required interpretation

At execution time, verify the current roles and names of:

- the crawler used for ChatGPT search discovery;
- the crawler used for potential model training;
- user-directed retrieval or agent access.

Do not combine them into one allow/block rule. Verify analytics referral parameters and any platform-specific app or agent guidance before implementation.

## Anthropic official sources

- Anthropic crawler guidance: https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Anthropic documentation: https://docs.anthropic.com/

### Required interpretation

Verify the current documented roles of:

- `ClaudeBot` for potential model-development collection;
- `Claude-SearchBot` for search discovery and result quality;
- `Claude-User` for user-initiated retrieval.

Names and purposes must be rechecked before every robots recommendation.

## Google official sources

- Google Search Central: https://developers.google.com/search?hl=pt-br
- AI features and your website: https://developers.google.com/search/docs/appearance/ai-features
- Search Essentials: https://developers.google.com/search/docs/essentials
- Helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Robots meta controls: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
- Google crawlers overview: https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers
- Google-Extended: https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers#google-extended
- Structured data: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Search Console: https://support.google.com/webmasters/

### Required interpretation

For AI Overviews and AI Mode in Google Search, use ordinary Search eligibility and current Googlebot controls. Do not claim that an `llms.txt` file, special AI schema or Google-Extended permission is required for inclusion. Verify all claims against the current AI-features documentation.

## Web and accessibility standards

- Robots Exclusion Protocol, RFC 9309: https://www.rfc-editor.org/rfc/rfc9309
- WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/
- Web Content Accessibility Guidelines: https://www.w3.org/WAI/standards-guidelines/wcag/
- Schema.org: https://schema.org/

## Research foundation

### Generative Engine Optimization

- Aggarwal et al., “GEO: Generative Engine Optimization,” KDD 2024. Find the current publisher or proceedings version and record DOI/proceedings metadata before citing.
- Role: foundational controlled study of methods intended to improve source visibility in generative-engine responses.
- Limitation: experimental results do not prove a universal tactic across commercial engines, models, locales and future versions.

### Retrieval, source selection and volatility

Use peer-reviewed publications when available; otherwise label preprints explicitly. Relevant research questions include:

- overlap between classic search and generative citations;
- source-quality and claim-support fidelity;
- sensitivity to query wording and repeated runs;
- activation frequency of AI answers;
- publisher traffic effects;
- engine and model differences.

Candidate studies to verify at execution time:

- “How Generative AI Disrupts Search: An Empirical Study of Google Search, Gemini, and AI Overviews” (2026 preprint): https://arxiv.org/abs/2604.27790
- “Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact” (2026 preprint): https://arxiv.org/abs/2605.14021
- “Impact of AI Search Summaries on Website Traffic: Evidence from Google AI Overviews and Wikipedia” (2026 preprint): https://arxiv.org/abs/2602.18455

Do not call a preprint peer reviewed unless publication status is confirmed.

## Reputable implementation repositories

These are workflow or tooling references, not platform authority:

- AgriciDaniel/claude-seo: https://github.com/AgriciDaniel/claude-seo
- zubair-trabzada/geo-seo-claude: https://github.com/zubair-trabzada/geo-seo-claude
- RivalSee/ai-seo-tools: https://github.com/RivalSee/ai-seo-tools
- GoogleChrome/lighthouse: https://github.com/GoogleChrome/lighthouse
- harlan-zw/unlighthouse: https://github.com/harlan-zw/unlighthouse
- StJudeWasHere/seonaut: https://github.com/StJudeWasHere/seonaut
- eliasdabbas/advertools: https://github.com/eliasdabbas/advertools

Before using any third-party prompt or agent skill, inspect it for prompt injection, destructive commands, hidden network calls, secrets handling, licensing, stale crawler names and unsupported guarantees.

## Experimental files and claims

### llms.txt

Treat `llms.txt` as an emerging voluntary convention, not a universal standard or guaranteed ranking/citation mechanism. Before recommending it:

- verify whether the target platform officially supports it;
- ensure it does not conflict with canonical HTML, sitemaps or access controls;
- keep it accurate and derived from the public site;
- present implementation as a low-risk experiment, not a requirement.

### “AI schema”

Do not invent special schema types. Use Schema.org and platform-supported structured data that accurately represents visible content. Structured data may aid machine understanding but does not guarantee retrieval, citation or recommendation.

### Citation formatting tricks

Readable, self-contained passages, original evidence, clear sourcing and stable facts may improve usefulness. However, no fixed paragraph length, keyword density, heading count, quotation count or schema stack is proven to guarantee citation across engines.

## Robots policy template

Always generate a site-specific matrix before editing robots.txt:

| Platform | Current verified user agent | Purpose | Desired access | robots.txt rule | Other controls | Risk |
|---|---|---|---|---|---|---|
| Google Search | verify | crawl/index and Search AI features | ... | ... | noindex/snippet | ... |
| OpenAI Search | verify | search discovery | ... | ... | noindex | ... |
| OpenAI training | verify | potential model development | ... | ... | policy/legal | ... |
| Anthropic Search | verify | search discovery | ... | ... | ... | ... |
| Anthropic user retrieval | verify | user-directed access | ... | ... | auth/WAF | ... |
| Anthropic training | verify | potential model development | ... | ... | policy/legal | ... |

Test the final rules against the live CDN/WAF and server response. Robots.txt is not authentication or confidentiality protection.

## Measurement cautions

- Search Console may aggregate Google AI-feature traffic into broader web-search reporting.
- Referral data can be lost through apps, privacy controls, copied links or untagged navigation.
- An engine response can change between repeated identical prompts.
- Source citation can differ by locale, account, model, product surface and query wording.
- Automated testing must comply with platform terms and rate limits.
- Visibility without qualified downstream behavior is not business success.

## Freshness record

Every GEO strategy should include:

| Source | Last updated/publication status | Checked on | Material conclusion | Limitation |
|---|---|---|---|---|
| OpenAI | ... | ... | ... | ... |
| Anthropic | ... | ... | ... | ... |
| Google | ... | ... | ... | ... |
| Research | ... | ... | ... | ... |
| Repository/tool | ... | ... | ... | ... |
