# CLAUDE.md

This file provides guidance to Claude Code when working with agents in this directory.

## Directory Purpose

Specialized sub-agents for Claude Code. Agents run in isolated context windows with configurable tool access.

## File Format

Agents use the **exact native Claude Code format**:

```markdown
---
tool: claude-code
name: agent-name
description: What this agent does. Include PROACTIVELY or MUST BE USED for auto-invocation.
tools: Bash, Read, Edit, Write
model: sonnet
permissionMode: acceptEdits
skills: test-generator
---

You are a specialized agent for [purpose].

## Your Process

1. First step
2. Second step
3. Third step

## Output Format

Always provide:
- Summary of actions
- Results or findings
- Any issues encountered
```

## Required Fields

- `tool`: Must be `claude-code`
- `name`: Unique identifier (must match filename without .md)
- `description`: When to invoke (include trigger words for auto-invocation)

## Optional Fields

- `tools`: Comma-separated tool list (omit for full access)
- `model`: `sonnet`, `opus`, `haiku`, or `inherit`
- `permissionMode`: `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan`
- `skills`: Comma-separated skill names to auto-load

## Naming Convention

Use kebab-case: `test-runner.md`, `code-reviewer.md`

Filename must match `name` field: `test-runner.md` has `name: test-runner`

## Deployment

Agents copy directly to `~/.claude/agents/`. Run:

```bash
../scripts/deploy_agents.py
```

## Excluded from Deployment

- This file (CLAUDE.md)
- README.md
- archive/ directory contents

## Reference

See [CUSTOMIZATION.md](../CUSTOMIZATION.md) for full specification.
