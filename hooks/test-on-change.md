---
tool: claude-code
event: PostToolUse
matcher: Edit
type: command
command: python3 "$HOME/.claude/hooks/testing/test-on-change.py"
---

# Test On Change

Runs tests after source file edits to catch regressions early.

## Behavior

- Intercepts Edit tool calls after execution
- Runs related tests for modified source files
- Skips test files to avoid infinite loops
- Non-blocking (exit code 1 is warning only)

## Supported File Types

| Extension | Test Command |
|-----------|--------------|
| `.ts`, `.tsx`, `.js`, `.jsx` | `npm test -- --bail --findRelatedTests <file>` |
| `.py` | `pytest -x -q --tb=short` |

## Skipped Files

- Files with `test` in path
- Files in `__tests__/` directory
- Files in `.claude/` directory

## Timeout

Tests timeout after 60 seconds.

## Debug

Set `CLAUDE_HOOK_DEBUG=1` to enable verbose logging.

## Exit Codes

- `0` = Tests passed or no action needed
- `1` = Tests failed (non-blocking warning)

## Script Location

`scripts/testing/test-on-change.py`
