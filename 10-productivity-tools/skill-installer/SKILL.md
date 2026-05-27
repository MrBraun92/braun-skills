---
name: skill-installer
description: Install new Manus skills from a GitHub repository or create them from scratch, ending with the delivery of Add-to-My-Skills cards so the user can save each skill with one click. Use when the user wants to add, import, or create skills in their Manus environment.
---

# Skill Installer

## Purpose

Fetch skills from a GitHub repository (public or private) or create new skills from scratch, then deliver each one as an interactive card so the user can click **Add to My Skills** to save them permanently.

This skill owns the full installation pipeline: discovery → content extraction → local file creation → validation → delivery.

## Use this skill when

Use this skill when the task is mainly about:

- importing skills from a GitHub repository into Manus
- creating a new skill from scratch and saving it
- bulk-installing multiple skills at once
- re-delivering an existing skill so the user can save it
- syncing skills from a remote repo after a GPT or collaborator added new ones

**Strong trigger examples:**

- "instale as skills do meu repositório"
- "crie uma skill para X e me deixe salvar"
- "importe as skills do GitHub MrBraun92/manus-skills"
- "adicione essas skills ao meu ambiente Manus"
- "install skills from my repo"
- "create and deliver this skill so I can save it"

## Do not use this skill when

Do not use this skill when the task is mainly about:

- writing the *content* of a brand-new specialist skill from scratch → Skill Creator
- auditing or reviewing existing skill quality → Skill Auditor
- routing which skill to use for a task → Skill Router
- finding skills on the internet → Internet Skill Finder

## Workflow

### Step 1 — Identify source and skills to install

Determine the installation source:

- **GitHub repo** (public or private): user provides owner/repo or URL
- **Skill list**: user provides names of skills to create or import
- **From scratch**: user describes what the skill should do

If the source is a GitHub repo, read the README or browse the directory tree to identify which skills are new (not yet installed locally at `/home/ubuntu/skills/`).

To check which skills are already installed:

```bash
ls /home/ubuntu/skills/
```

### Step 2 — Access the skill content

**For GitHub repos (private or public via browser):**

Navigate to each skill's `SKILL.md` on GitHub using the browser (already authenticated). The URL pattern is:

```
https://github.com/{owner}/{repo}/blob/{branch}/{skill-name}/SKILL.md
```

Extract the full Markdown content from the page's extracted markdown output.

**For GitHub repos via CLI (if `gh` is authenticated):**

```bash
gh repo clone {owner}/{repo} /tmp/skills-import --depth=1
```

Then read files directly from `/tmp/skills-import/{skill-name}/SKILL.md`.

**For skills created from scratch:**

Use the Skill Creator init script to scaffold the directory:

```bash
python /home/ubuntu/skills/skill-creator/scripts/init_skill.py {skill-name}
```

Then write the full SKILL.md content based on the user's description.

### Step 3 — Write SKILL.md files locally

For each skill, save the content to:

```
/home/ubuntu/skills/{skill-name}/SKILL.md
```

Every SKILL.md must have valid YAML frontmatter with `name` and `description` fields:

```yaml
---
name: skill-name
description: What the skill does and when to use it.
---
```

### Step 4 — Validate each skill

Run the official validator for each skill:

```bash
python /home/ubuntu/skills/skill-creator/scripts/quick_validate.py {skill-name}
```

Fix any validation errors before proceeding. Common issues: missing frontmatter fields, SKILL.md over 500 lines, broken Markdown.

### Step 5 — Deliver the skills as saveable cards

Send all SKILL.md files as **attachments** in a single `result` message using the `message` tool.

The system automatically detects the path pattern `/home/ubuntu/skills/*/SKILL.md`, packages each skill directory into a `.skill` file, and renders an interactive card in the frontend with three options:

- **Add to My Skills** — saves the skill permanently to the user's Manus account
- **Download** — downloads the `.skill` file
- **Preview** — shows the skill content

Always end with a `result` message listing all skills delivered and instructing the user to click **Add to My Skills** on each card.

## Handling private repositories

When the target repository is private and `gh` CLI is not authenticated:

1. Use the browser (already logged into GitHub) to navigate to each file.
2. Extract content from the rendered Markdown on the GitHub blob page.
3. Do not attempt `curl` or `wget` against raw.githubusercontent.com — these will return 404 for private repos without a token.

## Handling large batches

When installing 5 or more skills at once:

- Process skills sequentially to avoid losing content between browser navigations.
- Save each SKILL.md to disk immediately after reading it.
- Validate all skills before delivering any.
- Deliver all skills in a single `result` message with all attachments at once.

## Quality checklist

Before delivering, verify:

- every SKILL.md has `name` and `description` in frontmatter
- no SKILL.md exceeds 500 lines
- all files exist at `/home/ubuntu/skills/{skill-name}/SKILL.md`
- validation passed for each skill (or errors were fixed)
- the final message uses `result` type with all SKILL.md paths as attachments

## Composition notes

This skill works well **after**:

- Skill Creator (when a skill was just authored and needs to be delivered)
- Internet Skill Finder (when skills were discovered online and need to be installed)

It works well **alongside**:

- Skill Auditor (to review quality before installing)
