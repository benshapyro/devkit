---
tool: claude-code
event: PostToolUse
matcher: Edit|Write
type: command
command: python3 "$HOME/.claude/hooks/formatting/auto-format.py"
---

# Auto Format

Runs formatters after Edit/Write operations based on file extension.

## Behavior

- Intercepts Edit and Write tool calls after execution
- Checks file extension and runs appropriate formatter
- Non-blocking (exit code 1 is informational only)

## Supported Formatters

| Extension | Formatter |
|-----------|-----------|
| `.ts`, `.tsx`, `.js`, `.jsx` | `npx prettier --write` |
| `.py` | `black --line-length 100` |

## Requirements

- Prettier installed for JS/TS files
- Black installed for Python files

If formatter is not installed, the hook silently skips.

## Debug

Set `CLAUDE_HOOK_DEBUG=1` to enable verbose logging.

## Exit Codes

- `0` = Success or no action needed
- `1` = Formatter error (non-blocking)

## Script Location

`scripts/formatting/auto-format.py`
