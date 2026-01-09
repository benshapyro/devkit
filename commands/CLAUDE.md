# CLAUDE.md

This file provides guidance to Claude Code when working with commands in this directory.

## Directory Purpose

User-invoked slash commands for Claude Code. Commands are workflows triggered by `/command-name`.

## File Format

Commands use the **exact native Claude Code format**:

```markdown
---
tool: claude-code
allowed-tools: Bash(git:*), Read, Edit
argument-hint: [branch-name] [description]
description: Create a feature branch
model: sonnet
---

Your command prompt here.

Use $1 for first argument, $2 for second, etc.
Use $ARGUMENTS for all arguments as a string.

Include context with:
- !`shell-command` for live output
- @path/to/file for file contents
```

## Required Fields

- `tool`: Must be `claude-code`

## Optional Fields

- `allowed-tools`: Tool whitelist (e.g., `Bash(git:*)`, `Read`)
- `argument-hint`: Expected arguments for autocomplete
- `description`: Brief description (defaults to first line)
- `model`: `sonnet`, `opus`, or `haiku`
- `disable-model-invocation`: Prevent SlashCommand tool from calling

## Naming Convention

Use kebab-case: `review-pr.md`, `ship-changes.md`

Filename becomes the command: `review-pr.md` → `/review-pr`

## Deployment

Commands copy directly to `~/.claude/commands/`. Run:

```bash
../scripts/deploy_commands.py
```

## Excluded from Deployment

- This file (CLAUDE.md)
- README.md
- archive/ directory contents

## Reference

See [CUSTOMIZATION.md](../CUSTOMIZATION.md) for full specification.
