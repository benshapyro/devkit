# Commands

User-invoked slash commands for Claude Code. Trigger with `/command-name` in conversation.

## Quick Start

1. Create a new `.md` file in this directory
2. Add YAML frontmatter with `tool: claude-code`
3. Write your command prompt in the body
4. Deploy with `../scripts/deploy_commands.py`
5. Use with `/your-command-name` in Claude Code

## Example Command

```markdown
---
tool: claude-code
allowed-tools: Bash(git:*), Read, Grep
argument-hint: [issue-number]
description: Create a bug fix branch for an issue
model: sonnet
---

# Create Bug Fix Branch

Create a new branch for fixing issue #$1.

## Current State

- Branch: !`git branch --show-current`
- Status: !`git status --short`
- Recent commits: !`git log --oneline -5`

## Instructions

1. Fetch latest: `git fetch origin`
2. Create branch from main: `git checkout -b fix/issue-$1 origin/main`
3. Confirm branch created

## Conventions

Follow patterns in @.claude/references/git-workflow.md
```

## Special Syntax

### Arguments

```markdown
$ARGUMENTS    # All arguments as string
$1            # First argument
$2            # Second argument
$3            # Third argument (etc.)
```

### Bash Execution (prefix `!`)

```markdown
Current status: !`git status`
Node version: !`node --version`
```

### File References (prefix `@`)

```markdown
Follow the style in @src/utils/helpers.ts
Review @README.md for context
```

## Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `tool` | Yes | Must be `claude-code` |
| `allowed-tools` | No | Restrict available tools |
| `argument-hint` | No | Autocomplete hint |
| `description` | No | Brief description |
| `model` | No | `sonnet`, `opus`, `haiku` |
| `disable-model-invocation` | No | Block SlashCommand tool |

## Model Selection

| Model | Use For |
|-------|---------|
| `haiku` | Fast, simple tasks |
| `sonnet` | Balanced (default) |
| `opus` | Complex reasoning |

## Directory Structure

```
commands/
├── CLAUDE.md         # Context for Claude
├── README.md         # This file
├── review-pr.md      # Example command
├── ship.md           # Example command
├── archive/          # Excluded from deployment
└── examples/         # Working samples
```

## Deployment

Commands copy directly to `~/.claude/commands/`:

```bash
# Interactive deployment
../scripts/deploy.py

# Commands only
../scripts/deploy_commands.py
```

Filename becomes command name: `review-pr.md` → `/review-pr`

## More Information

- [CUSTOMIZATION.md](../CUSTOMIZATION.md) - Full specification
- [Claude Code Slash Commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands) - Official reference
