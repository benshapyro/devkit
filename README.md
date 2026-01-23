# Devkit

A library of reusable skills, hooks, commands, and agents for agentic CLI tools. Build once, deploy to Claude Code and other tools.

## Table of Contents

- [Why a Library?](#why-a-library)
- [Prerequisites](#prerequisites)
- [Architecture](#architecture)
- [Skills](#skills)
- [Hooks](#hooks)
- [Commands](#commands)
- [Agents](#agents)
- [Creating New Artifacts](#creating-new-artifacts)
- [Deployment](#deployment)
- [Documentation](#documentation)

## Why a Library?

You can customize Claude Code directly in `~/.claude/`. Why use a library instead?

| Approach | Pros | Cons |
|----------|------|------|
| **Direct customization** | Simple, immediate | No version control, can't share, tool-specific |
| **Library (this repo)** | Version controlled, shareable, multi-tool ready | Extra step to deploy |

This repo is the **source of truth**. Edit here, deploy to your tools. Track changes in git. Share artifacts across machines or teams.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and working
- Python 3.11+ (for skill scripts and validation)

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         devkit/                             │
├─────────────┬─────────────┬─────────────┬──────────────────┤
│   skills/   │   hooks/    │  commands/  │     agents/      │
│             │             │             │                  │
│  Domain     │  Event      │  User       │  Delegated       │
│  knowledge  │  automation │  workflows  │  sub-agents      │
└──────┬──────┴──────┬──────┴──────┬──────┴────────┬─────────┘
       │             │             │               │
       ▼             ▼             ▼               ▼
┌─────────────────────────────────────────────────────────────┐
│                      Claude Code                            │
│                                                             │
│  skills ◄───────── loaded on demand                         │
│  hooks ◄────────── triggered by events                      │
│  commands ◄─────── invoked with /name ──────► agents        │
│  agents ◄───────── delegated work                           │
└─────────────────────────────────────────────────────────────┘
```

**Relationships:**
- **Skills** provide knowledge and workflows, loaded when relevant
- **Hooks** intercept events (tool calls, session start, etc.) and can block or modify
- **Commands** are user-invoked with `/name` and can delegate to agents
- **Agents** run in isolated contexts with restricted tools

## Skills

Portable domain knowledge following the [Agent Skills spec](https://agentskills.io). Each skill is a directory with a `SKILL.md` file.

### Example

```markdown
---
name: code-review
description: Reviews code for quality, security, and maintainability. Use when reviewing PRs or checking code before commit.
---

You are a code review specialist.

## Process

1. Check for security vulnerabilities (injection, XSS, etc.)
2. Verify error handling covers edge cases
3. Assess readability and maintainability
4. Flag any code smells or anti-patterns

## Output

Provide findings as:
- **Critical**: Must fix before merge
- **Warning**: Should fix, but not blocking
- **Suggestion**: Optional improvements
```

### Organization

Skills are organized into 9 groups (122 skills total):

| Group | Skills | Examples |
|-------|--------|----------|
| **Marketing** | 27 | copywriting, page-cro, seo-audit, email-sequence, pricing-strategy |
| **Communications** | 3 | presentation-composer, doc-coauthoring, internal-comms |
| **Development Tools** | 22 | api-design-patterns, test-generator, react-best-practices, TDD, debugging |
| **Data & Documents** | 6 | pdf, docx, pptx, xlsx, ai-data-analyst |
| **Design & UI** | 10 | frontend-design, canvas-design, web-design-guidelines, Figma integration |
| **Infrastructure & Ops** | 9 | security-guardian, observability, Vercel deployment |
| **Business & Strategy** | 8 | product-discovery, strategy-frameworks, competitive-intelligence |
| **AI & Automation** | 13 | anthropic-messages-api, openai-responses-api, n8n workflows |
| **Internal & Specialty** | 24 | skill-creator, vibe-coding, Claude Code plugin development |

See `skills/README.md` for the full catalog with descriptions and example prompts.

## Hooks

Event-driven scripts that execute in response to Claude Code lifecycle events. Defined as Markdown with YAML frontmatter, deployed as JSON to `settings.json`.

### Example

```markdown
---
tool: claude-code
event: PreToolUse
matcher: Edit|Write
type: command
command: |
  python3 -c "
  import json, sys
  data = json.load(sys.stdin)
  path = data.get('tool_input', {}).get('file_path', '')
  sys.exit(2 if '.env' in path else 0)
  "
---

# Block .env Edits

Prevents modification of environment files containing secrets.
Exit code 2 blocks the action, 0 allows it.
```

### Events

| Event | Can Block? | Use Case |
|-------|------------|----------|
| `PreToolUse` | Yes | Validate/block tool calls |
| `PostToolUse` | No | Format, lint, log results |
| `UserPromptSubmit` | Yes | Add context, validate input |
| `Stop` | Yes | Force test-and-fix loops |

### Hook Scripts

The `hooks/scripts/` directory contains reusable Python helpers for common patterns (security checks, formatting, testing).

## Commands

User-invoked workflows triggered by `/command-name`. Use native Claude Code format.

### Example

```markdown
---
tool: claude-code
allowed-tools: Bash(git:*), Read, Grep
description: Review current branch changes
---

Review the changes on this branch.

## Context

- Branch: !`git branch --show-current`
- Diff: !`git diff main...HEAD --stat`

## Instructions

1. Summarize what changed and why
2. Flag any concerns (security, performance, breaking changes)
3. Suggest improvements if applicable
```

**Special syntax:**
- `$1`, `$2` - Positional arguments
- `$ARGUMENTS` - All arguments as string
- `!`backticks` - Execute shell, inject output
- `@path` - Include file contents

## Agents

Specialized sub-agents that run in isolated contexts. Claude delegates work to them automatically or on request.

### Example

```markdown
---
tool: claude-code
name: test-runner
description: Runs tests after code changes. PROACTIVELY use after completing implementations.
tools: Bash, Read, Grep, Glob
model: sonnet
---

You are a test automation specialist.

## Process

1. Identify test framework (Jest, pytest, etc.)
2. Run appropriate test command
3. If failures: analyze, fix, re-run
4. Report results with pass/fail counts

## Constraints

- Prefer fixing implementation over changing test assertions
- If uncertain, report findings without making changes
```

**Trigger words:** Include `PROACTIVELY` or `MUST BE USED` in description for auto-invocation.

## Creating New Artifacts

### Skill

```bash
./skills/skill-creator/scripts/init_skill.py my-skill --path ./skills
```

Creates `skills/my-skill/SKILL.md` with required frontmatter.

### Hook

Create `hooks/my-hook.md`:

```yaml
---
tool: claude-code
event: PreToolUse      # or PostToolUse, UserPromptSubmit, etc.
matcher: ToolName      # regex pattern, optional
type: command          # or prompt
command: |
  your-command-here
---
```

### Command

Create `commands/my-command.md`:

```yaml
---
tool: claude-code
description: What this command does
allowed-tools: Bash, Read  # optional restriction
---

Your prompt here. Use $1 for first argument.
```

Filename becomes `/my-command`.

### Agent

Create `agents/my-agent.md`:

```yaml
---
tool: claude-code
name: my-agent         # must match filename
description: When to use. Include PROACTIVELY for auto-invocation.
tools: Bash, Read      # optional restriction
---

Your agent instructions here.
```

## Deployment

This repo is the source of truth. Deploy by copying to Claude Code's config locations:

| Artifact | Target | Method |
|----------|--------|--------|
| Skills | `~/.claude/skills/` | Copy directory |
| Hooks | `~/.claude/settings.json` | Transform YAML→JSON, merge |
| Commands | `~/.claude/commands/` | Copy file |
| Agents | `~/.claude/agents/` | Copy file |

```bash
# Deploy a skill
cp -r skills/pdf ~/.claude/skills/

# Deploy a command
cp commands/review.md ~/.claude/commands/

# Deploy an agent
cp agents/debugger.md ~/.claude/agents/
```

Hooks require JSON transformation. See `hooks/CLAUDE.md` for the JSON format.

### Validation

```bash
./skills/skill-creator/scripts/quick_validate.py ./skills/my-skill
```

## Multi-tool Support

The architecture supports multiple agentic tools. The `tool: claude-code` field in frontmatter enables filtering during deployment. Additional tool support planned.

## Documentation

- `skills/CLAUDE.md` - Skill authoring details
- `hooks/CLAUDE.md` - Hook events and JSON format
- `commands/CLAUDE.md` - Command syntax reference
- `agents/CLAUDE.md` - Agent configuration options
- [Agent Skills Spec](https://agentskills.io) - Portable skills format
- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code) - Official documentation
