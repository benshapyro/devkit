# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Repository Purpose

A **multi-tool extension library** for agentic CLI tools. Contains reusable skills, hooks, commands, and agents that are built once here and deployed to individual tools.

**Current tool support:** Claude Code (others planned)

## Repository Structure

```
devkit/
├── skills/                 # Portable skills (Agent Skills spec)
│   ├── CLAUDE.md          # Skills-specific context
│   ├── <skill-name>/      # Individual skill directories
│   │   └── SKILL.md       # Required: frontmatter + instructions
│   └── archive/           # Excluded from deployment
│
├── hooks/                  # Event-driven automation
│   ├── CLAUDE.md          # Hooks-specific context
│   ├── <hook-name>.md     # Individual hook files
│   └── archive/           # Excluded from deployment
│
├── commands/               # User-invoked slash commands
│   ├── CLAUDE.md          # Commands-specific context
│   ├── <command-name>.md  # Individual command files
│   └── archive/           # Excluded from deployment
│
├── agents/                 # Specialized sub-agents
│   ├── CLAUDE.md          # Agents-specific context
│   ├── <agent-name>.md    # Individual agent files
│   └── archive/           # Excluded from deployment
│
├── scripts/                # Deployment and management tooling
│   ├── deploy.py          # Unified interactive deployment
│   ├── status.py          # Compare deployed vs source
│   └── validate.py        # Validate artifact formats
│
├── CUSTOMIZATION.md        # Spec for hooks, commands, agents
└── CLAUDE.md               # This file
```

## Artifact Types

| Type | Purpose | Format | Spec |
|------|---------|--------|------|
| **Skills** | Domain knowledge & workflows | SKILL.md in directory | [skills/CLAUDE.md](skills/CLAUDE.md) |
| **Hooks** | Event-driven automation | .md with YAML frontmatter | [CUSTOMIZATION.md](CUSTOMIZATION.md) |
| **Commands** | User-invoked workflows | Native Claude Code format | [CUSTOMIZATION.md](CUSTOMIZATION.md) |
| **Agents** | Delegated sub-agents | Native Claude Code format | [CUSTOMIZATION.md](CUSTOMIZATION.md) |

## Key Conventions

**Naming:** All artifacts use kebab-case (e.g., `test-runner.md`, `format-on-write.md`)

**Discovery:**
- Skills: Directory contains `SKILL.md`
- Hooks/Commands/Agents: Any `.md` file except README.md, CLAUDE.md

**Exclusions:** `archive/` directories are excluded from deployment

**Tool field:** All artifacts include `tool: claude-code` in frontmatter for future multi-tool support

## Deployment

```bash
# Interactive deployment of all types
./scripts/deploy.py

# Check what's deployed vs source
./scripts/status.py

# Validate artifact formats
./scripts/validate.py
```

**Target paths:**
- Skills: `~/.claude/skills/`
- Hooks: `~/.claude/settings.json` (merged)
- Commands: `~/.claude/commands/`
- Agents: `~/.claude/agents/`

## Working in Subdirectories

When working in a specific directory, read its CLAUDE.md for detailed guidance:

- `skills/CLAUDE.md` - Skill authoring, SKILL.md format, bundled resources
- `hooks/CLAUDE.md` - Hook events, matchers, command/prompt types
- `commands/CLAUDE.md` - Arguments, bash execution, file references
- `agents/CLAUDE.md` - Tool restrictions, permission modes, auto-invocation

## Adding New Artifacts

**Skill:** Create directory with SKILL.md. See `skills/skill-creator/` for tooling.

**Hook:** Create `.md` file in `hooks/` with event, matcher, command in frontmatter.

**Command:** Create `.md` file in `commands/` with native Claude Code format.

**Agent:** Create `.md` file in `agents/` with name, description, tools in frontmatter.

## Reference Documentation

- [CUSTOMIZATION.md](CUSTOMIZATION.md) - Hooks, commands, agents specification
- [skills/CLAUDE.md](skills/CLAUDE.md) - Skills specification
- [Agent Skills Spec](https://agentskills.io) - Portable skills format
- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code) - Official documentation
