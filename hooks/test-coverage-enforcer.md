---
tool: claude-code
event: PostToolUse
matcher: Edit|Write
type: command
command: python3 "$CLAUDE_DEVKIT/hooks/scripts/coverage/test-coverage-enforcer.py"
timeout: 5
---

# Test Coverage Enforcer

Warns when new or changed source code lacks corresponding tests.

## Behavior

- Intercepts Edit and Write tool calls after execution
- Checks if modified source files have corresponding test files
- Uses delta coverage approach - only checks new code, ignores legacy gaps
- Non-blocking (exit code 1 = warning only)

## Supported File Types

| Extension | Test Patterns |
|-----------|---------------|
| `.py` | `tests/test_{name}.py`, `tests/{name}_test.py`, `{dir}/test_{name}.py` |
| `.ts`, `.tsx` | `__tests__/{name}.test.ts`, `{name}.test.ts`, `{name}.spec.ts` |
| `.js`, `.jsx` | `__tests__/{name}.test.js`, `{name}.test.js`, `{name}.spec.js` |

## Skipped Files

- Files with `test` in path (test files themselves)
- Files in `__tests__/` directory
- Files in `spec/` directory
- Files in `.claude/` directory
- Non-source files (configs, data, etc.)

## Output

When test file is missing:

```
[MEDIUM] No test file found for src/feature.ts

Suggestion: Create test file at __tests__/feature.test.ts
```

## Exit Codes

- `0` = Test file exists or file skipped (not applicable)
- `1` = Test file missing (non-blocking warning)

## Configuration

Set in `~/.claude/settings.json`:

```json
{
  "devkit": {
    "extensions": {
      "test-coverage-enforcer": {
        "enabled": true,
        "options": {
          "skipPatterns": ["*.config.ts", "*.d.ts"]
        }
      }
    }
  }
}
```

## Environment Variables

- `CLAUDE_DEVKIT`: Path to devkit (for finding scripts)
- `CLAUDE_HOOK_DEBUG=1`: Enable verbose logging

## Script Location

`scripts/coverage/test-coverage-enforcer.py`
