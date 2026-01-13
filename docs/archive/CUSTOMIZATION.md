# CUSTOMIZATION.md

This specification defines the library format for Claude Code customization artifacts: **hooks**, **commands**, and **agents**. These complement the [skills/](./skills/) library which follows the [Agent Skills specification](https://agentskills.io).

**Current tool support:** Claude Code only (designed for future expansion)

## Overview

| Artifact | Purpose | Format | Deploy Target |
|----------|---------|--------|---------------|
| **Hooks** | Event-driven automation | YAML frontmatter + docs | `~/.claude/settings.json` (merged) |
| **Commands** | User-invoked workflows | Native Claude Code format | `~/.claude/commands/` |
| **Agents** | Delegated assistants | Native Claude Code format | `~/.claude/agents/` |

**Key principle:** Commands and agents use the exact native Claude Code format. Hooks use a Markdown wrapper that transforms to the native JSON format during deployment.

## Repository Structure

```
devkit/
├── hooks/                      # Event-driven automation
│   ├── CLAUDE.md              # Context for Claude when working here
│   ├── README.md              # Format guide and examples
│   ├── format-on-write.md     # Example hook
│   ├── block-env-edit.md      # Example hook
│   ├── archive/               # Excluded from deployment
│   └── examples/              # Working samples (deployable)
│
├── commands/                   # User-invoked slash commands
│   ├── CLAUDE.md
│   ├── README.md
│   ├── review-pr.md           # Example command
│   ├── ship.md                # Example command
│   ├── archive/
│   └── examples/
│
├── agents/                     # Specialized sub-agents
│   ├── CLAUDE.md
│   ├── README.md
│   ├── test-runner.md         # Example agent
│   ├── security-scanner.md    # Example agent
│   ├── archive/
│   └── examples/
│
├── skills/                     # Existing skills library
│   └── ...
│
├── scripts/                    # Deployment tooling
│   ├── deploy.py              # Unified interactive deployment
│   ├── deploy_hooks.py        # Hook-specific deployment
│   ├── deploy_commands.py     # Command-specific deployment
│   ├── deploy_agents.py       # Agent-specific deployment
│   ├── status.py              # Compare deployed vs source
│   └── validate.py            # Validate artifact formats
│
└── CUSTOMIZATION.md           # This specification
```

## Discovery and Exclusions

**Deployable items:** Any `.md` file in the artifact directory.

**Excluded from deployment:**
- `README.md`, `CLAUDE.md`, `AGENTS.md` (documentation files)
- `archive/` subdirectory contents
- `.archive/` subdirectory contents

**Naming convention:** kebab-case only (e.g., `format-on-write.md`, `test-runner.md`)

---

## Hooks

Hooks are event-driven scripts that execute in response to Claude Code lifecycle events. They are defined as Markdown files with YAML frontmatter and transformed to JSON during deployment.

### HOOK.md Format

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
timeout: 60
---

# Block .env File Edits

Prevents accidental modification of environment files containing secrets.

## Behavior

- Intercepts Edit and Write tool calls
- Checks if target path contains `.env`
- Returns exit code 2 to block, 0 to allow

## Why This Exists

Environment files often contain API keys and secrets that should not be
modified by automated tools without explicit human review.
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `tool` | Yes | Target tool identifier (currently `claude-code`) |
| `event` | Yes | Lifecycle event (see Events table below) |
| `matcher` | No | Regex pattern for tool names (default: all tools) |
| `type` | No | `command` (shell) or `prompt` (LLM). Default: `command` |
| `command` | Yes | Shell command or prompt text (use YAML `\|` for multi-line) |
| `timeout` | No | Seconds before timeout. Default: 60, max: 600 |

### Available Events

| Event | Can Block? | Use Cases |
|-------|------------|-----------|
| `UserPromptSubmit` | Yes | Add context, validate input |
| `PreToolUse` | Yes | Validate, log, modify tool parameters |
| `PostToolUse` | No | Format code, run linters, log results |
| `PermissionRequest` | Yes | Auto-approve/deny permissions |
| `Notification` | No | Custom alerts (Slack, desktop) |
| `Stop` | Yes | Force test-and-fix loops |
| `SubagentStop` | Yes | Validate subagent output |
| `PreCompact` | No | Backup transcripts |
| `SessionStart` | No | Inject context, set env vars |
| `SessionEnd` | No | Cleanup, logging |

### Hook Types

**Command hooks** (`type: command`): Execute shell commands. Receive JSON via stdin, return via stdout/exit codes.

**Prompt hooks** (`type: prompt`): Use LLM evaluation. Only valid for `Stop` and `SubagentStop` events. The `command` field contains the prompt text.

### Exit Codes

- **0**: Success (JSON in stdout processed, text shown in verbose mode)
- **2**: Blocking error (stderr shown to Claude/user, action blocked)
- **Other**: Non-blocking error (execution continues)

### Deployment Transformation

HOOK.md files are transformed to JSON and merged into `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 -c \"...\"",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**Merge behavior:** Library hooks are appended to existing arrays. Identical hooks (same event + matcher + command) are skipped to avoid duplicates.

### Input/Output Reference

Hooks receive JSON via stdin. See [official Claude Code hooks documentation](https://docs.anthropic.com/en/docs/claude-code/hooks) for the complete schema.

---

## Commands

Commands are user-invoked workflows triggered by `/command-name` in Claude Code. They use the **exact native Claude Code format**.

### Command Format

```markdown
---
allowed-tools: Bash(git:*), Read, Edit
argument-hint: [branch-name] [description]
description: Create a feature branch and initial commit
model: sonnet
---

Create a new feature branch for the given work.

## Context

- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`
- Status: !`git status --short`

## Instructions

1. Create branch: `feat/$1`
2. Switch to the new branch
3. Create initial commit with message based on $2

## Conventions

Follow the git workflow in @.claude/references/git-workflow.md
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `tool` | Yes | Target tool identifier (currently `claude-code`) |
| `allowed-tools` | No | Tool whitelist (e.g., `Bash(git:*)`, `Read`, `Edit`) |
| `argument-hint` | No | Expected arguments for autocomplete |
| `description` | No | Brief description (defaults to first line of body) |
| `model` | No | Model alias: `sonnet`, `opus`, `haiku` |
| `disable-model-invocation` | No | Prevent SlashCommand tool from calling this |

### Special Syntax

**Arguments:**
- `$ARGUMENTS` - All arguments as single string
- `$1`, `$2`, `$3` - Positional arguments

**Bash execution (prefix `!`):**
```markdown
Current status: !`git status`
```

**File references (prefix `@`):**
```markdown
Follow patterns in @src/utils/helpers.ts
```

### Model Selection Guidance

| Model | Characteristics |
|-------|-----------------|
| `haiku` | Fast, cost-effective. Good for simple lookups, formatting, quick tasks |
| `sonnet` | Balanced. Good default for most commands |
| `opus` | Most capable. Complex reasoning, multi-step analysis |

Choose based on your command's complexity. Omit to inherit from conversation.

### Deployment

Commands are copied directly to `~/.claude/commands/` with no transformation.

Filename becomes the command name: `review-pr.md` → `/review-pr`

---

## Agents

Agents are specialized sub-agents that Claude can delegate work to. They run in isolated context windows with restricted tool access. They use the **exact native Claude Code format**.

### Agent Format

```markdown
---
tool: claude-code
name: test-runner
description: Proactively runs tests after code changes. MUST BE USED when implementation is complete.
tools: Bash, Read, Grep, Glob
model: sonnet
permissionMode: acceptEdits
skills: test-generator
---

You are a test automation specialist. When delegated work:

## Process

1. Identify the test framework (Jest, pytest, vitest, etc.)
2. Run the appropriate test command
3. Analyze any failures
4. If tests fail:
   - Read the failing test and implementation
   - Determine if test or implementation needs fixing
   - Fix the issue while preserving test intent
   - Re-run to verify

## Output

Always provide:
- Number of tests run
- Pass/fail counts
- Summary of any changes made
- Remaining issues (if any)

## Constraints

- Never modify test assertions without understanding intent
- Prefer fixing implementation over changing tests
- If uncertain, report findings without making changes
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `tool` | Yes | Target tool identifier (currently `claude-code`) |
| `name` | Yes | Unique identifier (lowercase, hyphens, matches filename) |
| `description` | Yes | When to invoke. Include "PROACTIVELY" or "MUST BE USED" for auto-invocation |
| `tools` | No | Comma-separated tool list. Omit to inherit all tools |
| `model` | No | Model alias: `sonnet`, `opus`, `haiku`, or `inherit` |
| `permissionMode` | No | `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan` |
| `skills` | No | Comma-separated skill names to auto-load |

### Tool Access

**Explicit restriction:** List only the tools the agent needs.
```yaml
tools: Read, Grep, Glob
```

**Full access:** Omit the `tools` field entirely.
```yaml
# tools field omitted - agent has access to all tools
```

**Recommendation:** Always specify tools explicitly. Limit to minimum needed for the agent's purpose.

### Permission Modes

| Mode | Behavior |
|------|----------|
| `default` | Inherits from conversation |
| `acceptEdits` | Auto-approve file edits |
| `dontAsk` | Skip most permission prompts |
| `bypassPermissions` | Skip all permission prompts (use carefully) |
| `plan` | Read-only exploration mode |

### Agent Invocation

**Automatic:** Claude proactively delegates based on the `description` field.

**Explicit:** User requests in conversation:
```
Use the test-runner agent to verify my changes
```

**Resumable:** Agents can be resumed with their context:
```
Resume agent abc123 and also check the integration tests
```

### Deployment

Agents are copied directly to `~/.claude/agents/` with no transformation.

Filename becomes the agent identifier: `test-runner.md` → agent `test-runner`

---

## Deployment

### Prerequisites

```bash
pip install rich inquirer
```

### Interactive Deployment

```bash
./scripts/deploy.py
```

Presents TUI for selecting which artifacts to deploy. Matches the skills deployment experience.

### Per-Type Deployment

```bash
./scripts/deploy_hooks.py      # Deploy hooks only
./scripts/deploy_commands.py   # Deploy commands only
./scripts/deploy_agents.py     # Deploy agents only
```

Useful for automation and CI.

### Deployment Behavior

| Artifact | Target | Transformation |
|----------|--------|----------------|
| Hooks | `~/.claude/settings.json` | YAML → JSON merge |
| Commands | `~/.claude/commands/` | Copy as-is |
| Agents | `~/.claude/agents/` | Copy as-is |

**Conflict handling:** Interactive prompt per file (skip, overwrite, or rename).

**JSON errors:** If `settings.json` is invalid JSON, deployment aborts with error. User must fix manually.

### Check Status

```bash
./scripts/status.py
```

Shows comparison of library vs deployed:
- New items (in library, not deployed)
- Modified items (deployed differs from library)
- Deployed items (up to date)

### Validation

```bash
./scripts/validate.py                    # Validate all
./scripts/validate.py hooks/my-hook.md   # Validate specific file
```

Validates:
- Frontmatter presence and required fields
- Event validity (for hooks)
- Naming conventions
- Tool field presence

---

## Migration Guide

### Existing Hooks in settings.json

To add existing hooks to the library:

1. Create `hooks/<descriptive-name>.md`
2. Add frontmatter with `tool`, `event`, `matcher`, `type`, `command`, `timeout`
3. Add documentation in the body (optional but recommended)
4. Keep the original in `settings.json` until you've verified the library version works

### Existing Commands in .claude/commands/

Commands already match the library format:

1. Copy your `.md` file to `commands/`
2. Add `tool: claude-code` to frontmatter
3. Optionally add to examples/ if it demonstrates a pattern

### Existing Agents in .claude/agents/

Agents already match the library format:

1. Copy your `.md` file to `agents/`
2. Add `tool: claude-code` to frontmatter
3. Optionally add to examples/ if it demonstrates a pattern

---

## Relationships Between Artifacts

These artifacts compose but do not formally depend on each other:

```
┌─────────────────────────────────────────────────────────┐
│                    CLAUDE.md (Always Active)            │
│         Project memory, conventions, standards          │
└─────────────────────────────────────────────────────────┘
                             │
                             ▼
         ┌───────────────────────────────────┐
         │   Main Conversation (Context)     │
         │   • User prompts                  │
         │   • Skills (auto-applied)         │
         │   • Commands (user-invoked)       │
         └───────────────────────────────────┘
                    │                │
        ┌───────────┘                └───────────┐
        ▼                                        ▼
  ┌──────────┐                            ┌──────────┐
  │  Hooks   │ ◄────────────────────────► │  Agents  │
  │ (Events) │    Monitor & Control       │(Isolated)│
  └──────────┘                            └──────────┘
```

**Commands → Agents:** Commands can invoke agents via the Task tool.

**Hooks → Commands:** Hooks can add context suggesting commands, but cannot invoke directly.

**Hooks → Agents:** Hooks monitor agent lifecycle via `SubagentStop` event.

**No validation:** The library does not validate cross-references. Authors are responsible for ensuring referenced items exist.

---

## Testing Guidance

Before adding to the library:

### Hooks

1. Add the JSON directly to your local `~/.claude/settings.json`
2. Trigger the event (e.g., edit a file for `PreToolUse`)
3. Verify expected behavior
4. Convert to HOOK.md format

### Commands

1. Place the `.md` file in `.claude/commands/` (project) or `~/.claude/commands/` (global)
2. Run `/command-name` in Claude Code
3. Verify behavior matches expectations

### Agents

1. Place the `.md` file in `.claude/agents/` (project) or `~/.claude/agents/` (global)
2. Ask Claude to use the agent: "Use the test-runner agent to..."
3. Verify agent receives correct context and produces expected output

---

## Removal

To remove deployed artifacts, manually delete:

- **Hooks:** Remove from `~/.claude/settings.json` (find by matcher/command)
- **Commands:** Delete `~/.claude/commands/<name>.md`
- **Agents:** Delete `~/.claude/agents/<name>.md`

---

## Future Tool Support

The `tool` field in frontmatter enables future expansion:

```yaml
tool: claude-code    # Current
tool: codex          # Future
tool: factory        # Future
```

Deploy scripts filter by tool, allowing the same library to support multiple targets.

---

## Reference Documentation

- **Claude Code Hooks:** https://docs.anthropic.com/en/docs/claude-code/hooks
- **Claude Code Slash Commands:** https://docs.anthropic.com/en/docs/claude-code/slash-commands
- **Claude Code Sub-agents:** https://docs.anthropic.com/en/docs/claude-code/sub-agents
- **Skills Library:** [./skills/CLAUDE.md](./skills/CLAUDE.md)
- **Agent Skills Spec:** https://agentskills.io
