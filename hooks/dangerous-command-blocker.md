---
tool: claude-code
event: PreToolUse
matcher: Bash
type: command
command: python3 "$HOME/.claude/hooks/security/dangerous-command-blocker.py"
---

# Dangerous Command Blocker

Blocks dangerous shell commands before execution.

## Behavior

- Intercepts Bash tool calls before execution
- Checks command against dangerous patterns
- Exit code 2 blocks execution, 0 allows

## Blocked Patterns

| Pattern | Description |
|---------|-------------|
| `rm -rf /` | Recursive delete from root |
| `rm -rf ~` | Recursive delete from home |
| `chmod 777` | World-writable permissions |
| `sudo` | Elevated privileges |
| `dd if=` | Disk operations |
| `npm publish` | Accidental publishing |
| `git push --force` | Force push |

## Debug

Set `CLAUDE_HOOK_DEBUG=1` to enable verbose logging.

## Exit Codes

- `0` = Allow execution
- `2` = Block execution (PreToolUse convention)

## Script Location

`scripts/security/dangerous-command-blocker.py`
