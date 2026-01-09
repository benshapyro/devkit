# Hooks

Event-driven automation for Claude Code. Hooks execute shell commands or LLM prompts in response to lifecycle events.

## Quick Start

1. Create a new `.md` file in this directory
2. Add YAML frontmatter with required fields
3. Add documentation in the body
4. Deploy with `../scripts/deploy_hooks.py`

## Example Hook

```markdown
---
tool: claude-code
event: PostToolUse
matcher: Write
type: command
command: |
  jq -r '.tool_input.file_path' | {
    read file_path
    if echo "$file_path" | grep -q '\.ts$'; then
      npx prettier --write "$file_path" 2>/dev/null
    fi
  }
timeout: 30
---

# Format TypeScript on Write

Automatically runs Prettier on TypeScript files after they are written.

## Behavior

- Triggers after any Write tool call
- Checks if file has .ts extension
- Runs prettier --write on matching files
- Silent on non-TS files

## Requirements

- Node.js with npx available
- Prettier installed (globally or in project)
```

## Available Events

| Event | Can Block? | Common Uses |
|-------|------------|-------------|
| `UserPromptSubmit` | Yes | Add context, validate input |
| `PreToolUse` | Yes | Validate, log, modify parameters |
| `PostToolUse` | No | Format code, run linters |
| `PermissionRequest` | Yes | Auto-approve/deny |
| `Notification` | No | Custom alerts |
| `Stop` | Yes | Force test loops |
| `SubagentStop` | Yes | Validate agent output |
| `PreCompact` | No | Backup transcripts |
| `SessionStart` | No | Inject context |
| `SessionEnd` | No | Cleanup |

## Hook Types

**Command hooks** (`type: command`): Execute shell commands. Input via stdin (JSON), output via stdout/exit codes.

**Prompt hooks** (`type: prompt`): LLM evaluation. Only for `Stop` and `SubagentStop` events.

## Exit Codes

- **0**: Success
- **2**: Block the action (PreToolUse, UserPromptSubmit, etc.)
- **Other**: Non-blocking error

## Input Format

Hooks receive JSON via stdin:

```json
{
  "session_id": "abc123",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": { "file_path": "/path", "content": "..." },
  "cwd": "/current/directory"
}
```

See [Claude Code hooks documentation](https://docs.anthropic.com/en/docs/claude-code/hooks) for complete schema.

## Directory Structure

```
hooks/
├── CLAUDE.md           # Context for Claude
├── README.md           # This file
├── format-on-write.md  # Example hook
├── block-env-edit.md   # Example hook
├── archive/            # Excluded from deployment
└── examples/           # Working samples
```

## Deployment

Hooks are transformed to JSON and merged into `~/.claude/settings.json`:

```bash
# Interactive deployment
../scripts/deploy.py

# Hooks only
../scripts/deploy_hooks.py
```

## More Information

- [CUSTOMIZATION.md](../CUSTOMIZATION.md) - Full specification
- [Claude Code Hooks Docs](https://docs.anthropic.com/en/docs/claude-code/hooks) - Official reference
