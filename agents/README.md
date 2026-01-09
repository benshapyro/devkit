# Agents

Specialized sub-agents for Claude Code. Agents run in isolated context windows and can be delegated complex tasks.

## Quick Start

1. Create a new `.md` file in this directory
2. Add YAML frontmatter with required fields
3. Write agent instructions in the body
4. Deploy with `../scripts/deploy_agents.py`
5. Invoke: "Use the agent-name agent to..."

## Example Agent

```markdown
---
tool: claude-code
name: test-runner
description: Runs tests after code changes. MUST BE USED when implementation is complete.
tools: Bash, Read, Grep, Glob
model: sonnet
permissionMode: acceptEdits
skills: test-generator
---

You are a test automation specialist.

## Process

1. Identify the test framework (Jest, pytest, vitest)
2. Run appropriate test command
3. Analyze any failures
4. If tests fail:
   - Read failing test and implementation
   - Determine root cause
   - Fix while preserving test intent
   - Re-run to verify

## Output

Always provide:
- Tests run count
- Pass/fail summary
- Changes made (if any)
- Remaining issues

## Constraints

- Never change test assertions without understanding intent
- Prefer fixing implementation over modifying tests
- Report uncertainty rather than guessing
```

## Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `tool` | Yes | Must be `claude-code` |
| `name` | Yes | Unique ID (matches filename) |
| `description` | Yes | When to invoke |
| `tools` | No | Tool whitelist (omit for all) |
| `model` | No | `sonnet`, `opus`, `haiku`, `inherit` |
| `permissionMode` | No | Permission handling |
| `skills` | No | Skills to auto-load |

## Auto-Invocation

Include these phrases in `description` for automatic delegation:

- `PROACTIVELY` - Claude may invoke without being asked
- `MUST BE USED` - Claude should always invoke for matching tasks

```yaml
description: Security scanner. PROACTIVELY use when reviewing code changes.
```

## Permission Modes

| Mode | Behavior |
|------|----------|
| `default` | Inherit from conversation |
| `acceptEdits` | Auto-approve file edits |
| `dontAsk` | Skip most prompts |
| `bypassPermissions` | Skip all prompts |
| `plan` | Read-only mode |

## Tool Restriction

**Explicit tools:** Only listed tools available
```yaml
tools: Read, Grep, Glob
```

**Full access:** Omit field entirely
```yaml
# No tools field = all tools available
```

**Recommendation:** Always specify minimum required tools.

## Invocation Methods

**Automatic:** Claude delegates based on description keywords.

**Explicit:** User requests in conversation:
```
Use the test-runner agent to verify my changes
```

**Resumable:** Continue with previous context:
```
Resume agent abc123 and check integration tests too
```

## Directory Structure

```
agents/
├── CLAUDE.md            # Context for Claude
├── README.md            # This file
├── test-runner.md       # Example agent
├── code-reviewer.md     # Example agent
├── archive/             # Excluded from deployment
└── examples/            # Working samples
```

## Deployment

Agents copy directly to `~/.claude/agents/`:

```bash
# Interactive deployment
../scripts/deploy.py

# Agents only
../scripts/deploy_agents.py
```

## More Information

- [CUSTOMIZATION.md](../CUSTOMIZATION.md) - Full specification
- [Claude Code Sub-agents](https://docs.anthropic.com/en/docs/claude-code/sub-agents) - Official reference
