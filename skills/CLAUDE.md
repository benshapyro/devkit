# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

A **multi-tool skill library** for agentic CLI tools (Claude Code, OpenAI Codex, Factory Droid, etc.). Skills are built once here and deployed to individual tools. This repo follows the [Agent Skills specification](https://agentskills.io) exactly.

**Current tool support:** Claude Code (others planned)

## Repository Structure

```
skills/
├── scripts/                 # Deployment and management tooling (planned)
│   ├── deploy.py           # Interactive skill deployment (TUI)
│   ├── status.py           # Check deployed vs source skills
│   └── deploy_claude.py    # Claude Code-specific deployment
├── skill-creator/          # Meta-skill for creating new skills
│   └── scripts/            # init_skill.py, package_skill.py, quick_validate.py
├── <skill-name>/           # Individual skill directories
│   ├── SKILL.md           # Required: frontmatter + instructions
│   ├── scripts/           # Optional: executable code
│   ├── references/        # Optional: docs loaded on demand
│   └── assets/            # Optional: templates, resources
├── archive/                # Excluded from deployment
├── skill-specification.md  # Agent Skills format spec
├── what-are-skills.md      # Introduction to skills
└── integrating-skills.md   # How to integrate skills into agents
```

**Skill detection:** Any directory containing a `SKILL.md` file is a deployable skill.

**Excluded from deployment:** `archive/`, `.archive/`, and any directory without `SKILL.md`.

## Deployment Tooling (Planned)

### Deploy Skills

Interactive TUI for selecting which skills to deploy to which tools:

```bash
./scripts/deploy.py
```

Deployment copies skill directories (not symlinks) to tool-specific locations. No transformations are applied—skills are copied as-is.

**Target paths:**
- Claude Code: `~/.claude/skills/`
- Codex: `~/.codex/skills/`
- Factory: `~/.factory/skills/`

### Check Deployment Status

Compare what's deployed vs what's in this repo:

```bash
./scripts/status.py
```

### Tool-Specific Scripts

Each supported tool has its own deployment script:

```bash
./scripts/deploy_claude.py   # Deploy to Claude Code
# ./scripts/deploy_codex.py  # Future
# ./scripts/deploy_droid.py  # Future
```

## Skill Authoring

### Creating a New Skill

```bash
# Initialize from template
./skill-creator/scripts/init_skill.py <skill-name> --path .
```

### Validating a Skill

```bash
./skill-creator/scripts/quick_validate.py <path/to/skill-folder>
```

### Packaging for Distribution

```bash
./skill-creator/scripts/package_skill.py <path/to/skill-folder> [output-directory]
```

Creates a `.skill` file (zip archive) for sharing.

## SKILL.md Format

Every skill must have a `SKILL.md` with YAML frontmatter:

```yaml
---
name: skill-name              # Required: lowercase, hyphens only, 1-64 chars
description: What it does...  # Required: 1-1024 chars, includes WHEN to use
license: License info         # Optional
---
```

**Body (Markdown):** Instructions, examples, references to bundled resources.

### Design Principles

**Conservative context sizing:** All skills should be designed for the smallest common context window across tools. Keep SKILL.md under 500 lines.

**Assume full capabilities:** Skills can assume all tools have Claude Code-level capabilities (bash, python, network access, file system).

**Tool-agnostic format:** Skills use markdown. Avoid tool-specific syntax. Tools handle their own permission models and UI.

### Progressive Disclosure

1. **Metadata** (~100 tokens): `name` and `description` loaded at startup
2. **SKILL.md body** (<5k tokens): Loaded when skill triggers
3. **Bundled resources**: Loaded only when needed

Split content into reference files when SKILL.md approaches 500 lines.

### Bundled Resources

**scripts/** - Executable code for deterministic/repeated operations

**references/** - Documentation loaded into context as needed (keep under 10k words per file)

**assets/** - Files used in output, not loaded into context (templates, images, fonts)

## Development Workflow

1. **Primary development:** Build and test skills with Claude Code
2. **Verification:** Test on other tools before considering complete
3. **Deploy:** Use `./scripts/deploy.py` to push to tool locations

## Adding New Tool Support

Create a new deployment script in `scripts/`:

```
scripts/deploy_<toolname>.py
```

The script should:
1. Define the target path (e.g., `~/.toolname/skills/`)
2. Handle skill discovery (directories with SKILL.md)
3. Copy skills to target location
4. Respect exclusions (archive/, .archive/)

Update `deploy.py` to include the new tool in the interactive selection.

## Tooling Dependencies

Deployment scripts use:
- **rich**: Terminal formatting and output
- **python-inquirer**: Interactive prompts and selection

```bash
pip install rich inquirer
```

## Current Skills

Skills are auto-detected by presence of SKILL.md. Current skills include:

### Document Processing
- **pdf** - PDF manipulation, form filling, text extraction
- **docx** - Word document creation/editing via docx-js and OOXML
- **pptx** - PowerPoint creation/editing via OOXML
- **xlsx** - Excel processing

### Development
- **mcp-builder** - MCP server development guide
- **skill-creator** - Meta-skill for creating new skills
- **frontend-design** - UI/UX design guidance

### Business Strategy
- **strategy-frameworks** - Porter's Five Forces, BCG Matrix, SWOT, McKinsey 7S
- **competitive-intelligence** - Battle cards, competitive matrices, win/loss analysis

### Content & Marketing
- **editorial-calendar** - Content planning with SEO integration and multi-channel coordination
- **content-repurposer** - Transform content across formats and platforms

### Finance & Operations
- **expense-categorizer** - Expense categorization with tax rules and policy compliance

### Other
- **cadre-os** - Consulting methodology and workflows
- And others (run `./scripts/status.py` to see full list)

## Reference Documentation

- **Agent Skills spec:** https://agentskills.io
- **Local spec:** skill-specification.md
- **Skill authoring guide:** skill-creator/SKILL.md
- **Output patterns:** skill-creator/references/output-patterns.md
- **Workflow patterns:** skill-creator/references/workflows.md
