# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

A **multi-tool extension library** for agentic CLI tools. Contains reusable skills, hooks, commands, and agents that are built once here and deployed to individual tools.

**Current tool support:** Claude Code (others planned)

## Repository Structure

```
devkit/
├── skills/                 # Portable skills (Agent Skills spec)
│   ├── CLAUDE.md          # Skills-specific context
│   ├── <skill-name>/      # Individual skill directories
│   │   ├── SKILL.md       # Required: frontmatter + instructions
│   │   ├── scripts/       # Optional: executable code
│   │   ├── references/    # Optional: docs loaded on demand
│   │   └── assets/        # Optional: templates, resources
│   └── archive/           # Excluded from deployment
│
├── hooks/                  # Event-driven automation
│   ├── CLAUDE.md          # Hooks-specific context
│   ├── scripts/           # Reusable hook scripts (Python)
│   └── <hook-name>.md     # Individual hook files
│
├── commands/               # User-invoked slash commands
│   ├── CLAUDE.md          # Commands-specific context
│   └── <command-name>.md  # Individual command files
│
├── agents/                 # Specialized sub-agents
│   ├── CLAUDE.md          # Agents-specific context
│   └── <agent-name>.md    # Individual agent files
│
├── CUSTOMIZATION.md        # Spec for hooks, commands, agents
└── CLAUDE.md               # This file
```

## Artifact Types

| Type | Purpose | Format | Deploy Target |
|------|---------|--------|---------------|
| **Skills** | Domain knowledge & workflows | SKILL.md in directory | `~/.claude/skills/` |
| **Hooks** | Event-driven automation | .md with YAML frontmatter | `~/.claude/settings.json` (merged) |
| **Commands** | User-invoked workflows | Native Claude Code format | `~/.claude/commands/` |
| **Agents** | Delegated sub-agents | Native Claude Code format | `~/.claude/agents/` |

## Key Conventions

**Naming:** All artifacts use kebab-case (e.g., `test-runner.md`, `format-on-write.md`)

**Discovery:**
- Skills: Directory contains `SKILL.md`
- Hooks/Commands/Agents: Any `.md` file except README.md, CLAUDE.md

**Exclusions:** `archive/` directories are excluded from deployment

**Tool field:** All artifacts include `tool: claude-code` in frontmatter for future multi-tool support

## Development Commands

```bash
# Validate a skill
./skills/skill-creator/scripts/quick_validate.py <path/to/skill-folder>

# Create a new skill from template
./skills/skill-creator/scripts/init_skill.py <skill-name> --path ./skills

# Package a skill for distribution
./skills/skill-creator/scripts/package_skill.py <path/to/skill-folder> [output-dir]
```

**Manual deployment:** Copy artifacts to their target paths. Commands and agents copy directly. Hooks require JSON transformation and merge into `settings.json`.

## Working in Subdirectories

Read the CLAUDE.md in each directory for detailed guidance:

- `skills/CLAUDE.md` - Skill authoring, SKILL.md format, bundled resources
- `hooks/CLAUDE.md` - Hook events, matchers, command/prompt types
- `commands/CLAUDE.md` - Arguments, bash execution, file references
- `agents/CLAUDE.md` - Tool restrictions, permission modes, auto-invocation

## Adding New Artifacts

**Skill:** Create directory with SKILL.md. Use `./skills/skill-creator/scripts/init_skill.py` for scaffolding.

**Hook:** Create `.md` file in `hooks/` with event, matcher, command in frontmatter.

**Command:** Create `.md` file in `commands/` with native Claude Code format. Filename becomes `/command-name`.

**Agent:** Create `.md` file in `agents/` with name, description, tools in frontmatter. Filename must match `name` field.

## Reference Documentation

- [CUSTOMIZATION.md](CUSTOMIZATION.md) - Hooks, commands, agents specification
- [skills/CLAUDE.md](skills/CLAUDE.md) - Skills specification
- [Agent Skills Spec](https://agentskills.io) - Portable skills format
- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code) - Official documentation
