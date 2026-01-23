---
name: n8n-architect
description: Design and build production-ready n8n workflows using MCP tools. Use when building n8n workflows, automating business processes, implementing AI agents, or troubleshooting existing workflows. Handles complexity from simple webhook→transform→output to multi-agent orchestration with memory systems.
---

# N8N Adaptive Architect

Build n8n workflows through MCP-validated construction. Adapts depth based on requirement clarity.

## Quick Start

**Always begin with:**
```javascript
tools_documentation()  // Get MCP capabilities overview
```

**Standard workflow pattern (80% of cases):**
```javascript
// 1. Find nodes
search_nodes({query: "webhook"})

// 2. Get configuration details
get_node({nodeType: "nodes-base.webhook", detail: "standard"})

// 3. Find templates for patterns
search_templates({query: "slack notification"})

// 4. Validate before deploy
validate_workflow({workflow: {...}, options: {profile: "runtime"}})
```

## Complexity Routing

**Lightweight Path** → Simple requirements, proceed directly:
- Single trigger, clear data flow
- Standard nodes (webhook, HTTP, transform, output)
- No branching or error handling specified

**Standard Path** → Ask 2-3 clarifying questions:
- Multiple triggers or conditional logic
- External service integrations
- Error handling requirements

**Comprehensive Path** → Full discovery session:
- Enterprise integration across systems
- AI/ML workflow components → See [references/ai-workflows.md](references/ai-workflows.md)
- Complex branching logic → See [references/smart-parameters.md](references/smart-parameters.md)

## Core MCP Tools

### Discovery
| Tool | Use For |
|------|---------|
| `tools_documentation()` | Always call first |
| `search_nodes({query: "..."})` | Find nodes by keyword |
| `get_node({nodeType: "...", detail: "standard"})` | Get node config (95% of cases) |
| `search_templates({query: "..."})` | Find pre-built patterns |

### Validation
| Tool | Use For |
|------|---------|
| `validate_node({nodeType, config})` | Check single node |
| `validate_workflow({workflow})` | Full workflow check before deploy |
| `n8n_autofix_workflow({id})` | Preview/apply automatic fixes |

### Workflow Management
| Tool | Use For |
|------|---------|
| `n8n_create_workflow({...})` | Create new workflow |
| `n8n_update_partial_workflow({id, operations})` | Incremental updates |
| `n8n_get_workflow({id})` | Retrieve existing workflow |

For complete tool reference → See [references/mcp-tools.md](references/mcp-tools.md)

## Essential Patterns

### Webhook Data Access
```javascript
// Webhook payload is under .body
const data = $json.body;
```

### Code Node Returns
```javascript
// JavaScript - MUST return array with json property
return [{ json: { result: data } }];
```
```python
# Python - MUST return list with "json" key
return [{"json": {"result": data}}]
```

For complete code patterns → See [references/code-nodes.md](references/code-nodes.md)

### IF Node Connections
```javascript
// Use branch parameter, NOT sourceIndex
{type: "addConnection", source: "IF", target: "Success", branch: "true"}
{type: "addConnection", source: "IF", target: "Failure", branch: "false"}
```

For branching and Switch nodes → See [references/smart-parameters.md](references/smart-parameters.md)

## Workflow JSON Structure

```json
{
  "name": "Workflow Name",
  "nodes": [
    {
      "id": "uuid",
      "name": "Display Name",
      "type": "nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "parameters": {}
    }
  ],
  "connections": {
    "Source Node": {
      "main": [[{"node": "Target Node", "type": "main", "index": 0}]]
    }
  },
  "settings": {"executionOrder": "v1"}
}
```

## Validation Checklist

Before any create/update:
- [ ] `validate_workflow()` passes with target profile
- [ ] Credentials referenced (never hardcoded)
- [ ] Error handling at critical points
- [ ] Webhook paths are unique

## Common Pitfalls

| Mistake | Fix |
|---------|-----|
| Using `sourceIndex` for IF branches | Use `branch="true"/"false"` |
| Forgetting webhook `.body` | Access `$json.body` for payload |
| AI agent without language model | Connect model BEFORE enabling agent |
| Using `null` to remove properties | Use `undefined` instead |

For complete pitfalls list → See [references/pitfalls.md](references/pitfalls.md)

## Reference Navigation

| Need | Reference File |
|------|----------------|
| Complete MCP tool signatures | [mcp-tools.md](references/mcp-tools.md) |
| AI agents, LangChain, memory | [ai-workflows.md](references/ai-workflows.md) |
| IF/Switch branching, property removal | [smart-parameters.md](references/smart-parameters.md) |
| JavaScript/Python code patterns | [code-nodes.md](references/code-nodes.md) |
| Common mistakes and prevention | [pitfalls.md](references/pitfalls.md) |
| Cadre consulting patterns | [cadre-patterns.md](references/cadre-patterns.md) |
