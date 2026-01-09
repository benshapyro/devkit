---
tool: claude-code
event: UserPromptSubmit
matcher: .*
type: command
command: $HOME/.claude/hooks/skill-activation-prompt.sh
---

# Skill Activation

Suggests relevant skills and agents based on user prompts.

## Behavior

- Intercepts all user prompts on submit
- Matches prompt against configured keyword patterns and regex
- Returns `additionalContext` suggesting relevant skills/agents

## Configuration

Requires `skill-rules.json` in one of:
- `$CLAUDE_PROJECT_DIR/.claude/skill-rules.json` (project)
- `~/.claude/skill-rules.json` (user)

### skill-rules.json Format

```json
{
  "skills": {
    "test-generator": {
      "priority": "high",
      "promptTriggers": {
        "keywords": ["test", "jest", "pytest", "coverage"],
        "intentPatterns": ["write.*tests?", "add.*test"]
      }
    }
  },
  "agents": {
    "code-reviewer": {
      "priority": "medium",
      "promptTriggers": {
        "keywords": ["review", "check code"],
        "intentPatterns": ["review.*code"]
      }
    }
  }
}
```

## Output

Returns JSON with `additionalContext` field:
```json
{
  "additionalContext": "Relevant skills detected: test-generator. Consider using the Skill tool."
}
```

## Script Location

`scripts/skill-activation-prompt.sh`
