---
tool: claude-code
event: UserPromptSubmit
type: command
command: python3 "$CLAUDE_DEVKIT/hooks/scripts/context/smart-context-loader.py"
timeout: 2
---

# Smart Context Loader

Automatically injects relevant project context based on prompt analysis.

## Behavior

- Intercepts user prompts before processing
- Analyzes prompt for domain keywords (auth, api, database, etc.)
- Finds relevant files, recent changes, and TODOs
- Injects context as a prefix to the prompt
- Fast execution (<2s timeout)

## Keyword Mappings

| Keyword | Searches For |
|---------|--------------|
| `auth` | src/auth/, login, session, authentication |
| `api` | src/api/, routes/, controllers/, endpoints |
| `database` | migrations/, models/, schema, queries |
| `test` | tests/, __tests__/, *.test.*, *.spec.* |
| `config` | .env.example, config/, settings |
| `build` | webpack, vite, rollup, build scripts |
| `deploy` | docker, k8s, terraform, CI/CD |

## Injected Context

When keywords are detected, injects:

```
[Auto-loaded context]

Relevant files: src/auth/controller.ts, src/auth/middleware.ts
Recent changes:
  - abc123 feat(auth): add OAuth support
  - def456 fix(auth): handle expired tokens
TODOs found:
  - src/auth/controller.ts:42: TODO: add rate limiting

{original prompt}
```

## Exit Codes

- `0` = No keywords found, prompt unchanged
- `3` = Context injected, prompt modified

## Configuration

Set in `~/.claude/settings.json`:

```json
{
  "devkit": {
    "extensions": {
      "smart-context-loader": {
        "enabled": true,
        "options": {
          "maxFiles": 5,
          "maxCommits": 5,
          "maxTodos": 3,
          "customKeywords": {
            "payments": ["stripe", "billing", "subscription"]
          }
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

`scripts/context/smart-context-loader.py`
