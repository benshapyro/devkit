---
tool: claude-code
description: Learn about Claude Code, the devkit, commands, skills, and workflows
allowed-tools: Read, Glob, Task
argument-hint: [question or topic]
---

# Learn Command

Interactive help for Claude Code and the devkit.

## Question Routing

| Question | Action |
|----------|--------|
| Claude Code features | Use `claude-code-guide` subagent |
| Devkit structure | Read devkit files directly |
| Specific command | Read `commands/{command}.md` |
| Specific skill | Read `skills/{skill}/SKILL.md` |
| Hooks | Read `hooks/` + settings.json |

## Response Style

1. **Direct answer first**
2. Then context if helpful
3. Show concrete examples
4. Link to source files

## Example Interactions

### "How do hooks work?"
1. Explain hooks are in `~/.claude/settings.json` (or `.claude/settings.json`)
2. Cover event types: PreToolUse, PostToolUse, Stop, etc.
3. Show example structure
4. Mention `CLAUDE_HOOK_DEBUG=1` for debugging

### "What's the difference between /plan and /greenfield?"
- `/greenfield` = new project from scratch → creates SPEC/DESIGN/PLAN docs
- `/plan` = feature in existing project → creates implementation plan
- Use greenfield first, then plan for each feature

### "Show available commands"
Read `commands/` directory and list with descriptions.

### "What's the workflow for shipping code?"
```
/plan [feature]
  ↓
[implement]
  ↓
/slop (optional - clean AI artifacts)
  ↓
/review (code review)
  ↓
/validate (automated checks)
  ↓
/ship (commit)
```

## Dynamic Discovery

For questions about current setup, read actual files:

```
"What commands are available?"
→ ls commands/*.md

"What skills do I have?"
→ ls skills/*/SKILL.md

"Show me the hooks"
→ Read ~/.claude/settings.json hooks section
```

## Teaching Mode

If "teach me about X" or "explain X":
1. Big picture first
2. Break into components
3. Practical examples
4. Suggest hands-on exercises

## No Question Provided

```
I can help you learn about:

- **Commands** - /greenfield, /plan, /review, /validate, /ship
- **Skills** - Domain knowledge that auto-loads
- **Hooks** - Event-driven automation
- **Agents** - Specialized sub-agents
- **Workflow** - How everything fits together

What would you like to know?

Quick starts:
- "How do I start a new project?"
- "What's the workflow for shipping code?"
- "How do hooks work?"
```

## Claude Code Questions

For Claude Code (not devkit) questions:
```
Task(
  subagent_type="claude-code-guide",
  prompt="User question: {question}"
)
```

## Devkit Questions

Read actual files when possible to give accurate, current answers.
