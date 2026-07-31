# Organic Discovery Pack: SEO + GEO

This pack contains two complementary Agent Skills:

- `seo-audit`: canonical Google SEO audit and strategy router
- `geo-ai-discovery`: canonical AI-search, citation and agent-discovery router

The reference folders are part of each skill and must remain beside `SKILL.md`.

## Directory structure

```text
seo-audit/
├── SKILL.md
└── references/
    └── source-registry.md

geo-ai-discovery/
├── SKILL.md
└── references/
    └── source-registry.md
```

## Claude Code

Install for the current project:

```bash
mkdir -p .claude/skills
cp -R seo-audit .claude/skills/
cp -R geo-ai-discovery .claude/skills/
```

Install for the current user across projects:

```bash
mkdir -p ~/.claude/skills
cp -R seo-audit ~/.claude/skills/
cp -R geo-ai-discovery ~/.claude/skills/
```

Restart or reload the Claude Code session after installation. Keep both folders intact so relative references continue to work.

## Claude.ai / Cowork / environments with uploaded Skills

Upload each complete folder as a skill, not only the `SKILL.md` file. When the interface accepts ZIP packages, upload the complete pack ZIP and confirm that both skill names appear:

- `seo-audit`
- `geo-ai-discovery`

If the interface accepts only individual files, upload `SKILL.md` together with its `references/source-registry.md`, preserving the relative folder structure when possible.

## Manus

Import or upload both complete skill folders. If Manus supports repository or raw-file import in the current interface, use the files from the active branch or merged `master`; otherwise upload the ZIP package.

After installation, test with:

```text
Audit this domain for SEO and AI discovery. Before recommending anything, show which current official Google, OpenAI and Anthropic documentation you consulted, separate search visibility from model-training permissions, and provide an evidence ledger.
```

Expected behavior:

1. `seo-audit` handles Search eligibility, technical SEO, content and measurement.
2. `geo-ai-discovery` handles ChatGPT, Claude, Gemini/Google AI features, crawler-policy separation, citations and agent accessibility.
3. Both skills disclose missing live data and do not promise rankings, citations or recommendations.

## Updating

These skills intentionally depend on current external documentation. Update the local installation whenever the repository changes, but the agent must still consult live official sources during each substantive execution.

## Security

Third-party repositories listed in the source registries are untrusted implementation references. Do not execute copied code or instructions without reviewing licensing, dependencies, network behavior, secrets handling, destructive commands and prompt-injection risks.
