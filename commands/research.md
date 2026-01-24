---
tool: claude-code
description: Deep research on a topic with parallel sub-agents
allowed-tools: Task, Read, Grep, Glob, WebSearch, WebFetch
argument-hint: "[--auto] [topic or question]"
---

# Research Command

Comprehensive research using parallel sub-agents.

## Flags

- `--auto` - Skip approval, execute research plan immediately

## Validation

If no topic provided, ask for one.

## Research Flow

### 1. Analyze Request

- Understand the question/topic
- Consider project context (CLAUDE.md, tech stack)
- Identify knowledge gaps

### 2. Propose Research Plan

Determine which research dimensions are needed:

| Dimension | When |
|-----------|------|
| Codebase - Patterns | Feature touches existing code |
| Codebase - Architecture | Architectural decision needed |
| Documentation - Framework | Using framework features |
| Documentation - Libraries | Using external libraries |
| Community - Best Practices | Common patterns needed |

**Output:**
```
## Research Plan: [topic]

### Proposed Agents (N)

1. **[Category]: [Focus]**
   - What: [investigation]
   - Why: [relevance]

2. ...

---
Proceed? (yes / adjust / cancel)
```

### 3. Await Approval (unless --auto)

- **Approve**: "yes", "proceed"
- **Adjust**: "skip X", "also check Y"
- **Cancel**: "nevermind"

### 4. Execute Research

Spawn agents in parallel:

**Agent mapping:**
- Codebase → `subagent_type: "Explore"`
- Documentation → `subagent_type: "documentation-researcher"`
- Community → `subagent_type: "documentation-researcher"` with web search

**IMPORTANT:** Use SINGLE message with multiple Task calls for parallel execution.

### 5. Synthesize Findings

```
## Research Findings: [topic]

### Summary
[2-3 sentence executive summary]

### Key Discoveries

**Codebase:**
- [Finding with file:line reference]

**Documentation:**
- [Finding with source link]

**Community:**
- [Best practice or pitfall]

### Recommendations
1. [Action]
2. [Action]

### Next Steps
- [ ] [Task]

---
Save findings? Use `/progress` to create knowledge doc.
```

## Guidelines

- 3-5 agents typical, 7+ is too broad
- Each agent should have clear, specific mission
- Synthesize findings - don't dump raw results

## Quick Research (--auto)

For simple topics, `--auto` skips approval:
```
/research --auto "how does auth work in this codebase"
```
