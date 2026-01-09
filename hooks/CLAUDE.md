# CLAUDE.md

This file provides guidance to Claude Code when working with hooks in this directory.

## Directory Purpose

Event-driven automation scripts for Claude Code. Hooks execute in response to lifecycle events (tool calls, session start/end, etc.).

## File Format

Each hook is a Markdown file with YAML frontmatter:

```markdown
---
tool: claude-code
event: PreToolUse
matcher: Edit|Write
type: command
command: |
  your-shell-command-here
timeout: 60
---

# Hook Name

Documentation about what this hook does and why.
```

## Required Fields

- `tool`: Must be `claude-code`
- `event`: One of: UserPromptSubmit, PreToolUse, PostToolUse, PermissionRequest, Notification, Stop, SubagentStop, PreCompact, SessionStart, SessionEnd
- `command`: Shell command (for type: command) or prompt text (for type: prompt)

## Optional Fields

- `matcher`: Regex pattern for tool names (default: all tools)
- `type`: `command` or `prompt` (default: command)
- `timeout`: Seconds before timeout (default: 60, max: 600)

## Naming Convention

Use kebab-case: `format-on-write.md`, `block-env-edit.md`

## Deployment

Hooks transform to JSON and merge into `~/.claude/settings.json`. Run:

```bash
../scripts/deploy_hooks.py
```

## Excluded from Deployment

- This file (CLAUDE.md)
- README.md
- archive/ directory contents

## Reference

See [CUSTOMIZATION.md](../CUSTOMIZATION.md) for full specification.
