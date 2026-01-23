# MCP Tools Reference

Complete reference for all n8n MCP tools with signatures and examples.

## Table of Contents
- [Discovery Tools](#discovery-tools)
- [Validation Tools](#validation-tools)
- [Workflow Management](#workflow-management)
- [Instance Management](#instance-management)

---

## Discovery Tools

### tools_documentation()
Get MCP overview or specific tool docs. **Always call first.**

```javascript
tools_documentation()                                    // Quick start
tools_documentation({topic: "get_node", depth: "full"}) // Specific tool
tools_documentation({topic: "javascript_code_node_guide", depth: "full"})  // Code guides
```

### search_nodes()
Find nodes by keyword.

```javascript
search_nodes({query: "slack"})
search_nodes({query: "webhook", includeExamples: true})  // With template configs
search_nodes({query: "http request", mode: "AND", limit: 10})
// Modes: OR (any word), AND (all words), FUZZY (typo-tolerant)
```

### get_node()
Unified node information. Replaces 4 previous tools.

```javascript
// Standard detail (95% of cases, ~1-2K tokens)
get_node({nodeType: "nodes-base.httpRequest", detail: "standard"})

// Minimal for quick reference (~200 tokens)
get_node({nodeType: "nodes-base.slack", detail: "minimal"})

// Full when standard insufficient (~3-8K tokens)
get_node({nodeType: "nodes-langchain.agent", detail: "full"})

// With real-world examples
get_node({nodeType: "nodes-base.webhook", detail: "standard", includeExamples: true})

// Search specific properties
get_node({nodeType: "nodes-base.httpRequest", mode: "search_properties", propertyQuery: "auth"})

// Markdown documentation
get_node({nodeType: "nodes-base.code", mode: "docs"})

// Version comparison
get_node({nodeType: "nodes-base.executeWorkflow", mode: "compare", fromVersion: "1.0", toVersion: "1.1"})

// Breaking changes
get_node({nodeType: "nodes-base.webhook", mode: "breaking"})
```

### search_templates()
Find pre-built solutions (2,700+ templates).

```javascript
// Keyword search
search_templates({query: "slack notification"})

// Find by nodes used
search_templates({searchMode: "by_nodes", nodeTypes: ["nodes-base.slack", "nodes-base.httpRequest"]})

// Task-based search
search_templates({searchMode: "by_task", task: "webhook_processing"})
// Tasks: ai_automation, data_sync, webhook_processing, email_automation,
//        slack_integration, data_transformation, file_processing,
//        scheduling, api_integration, database_operations

// Metadata filters
search_templates({
  searchMode: "by_metadata",
  complexity: "simple",        // simple, medium, complex
  maxSetupMinutes: 30,
  requiredService: "slack"
})
```

### get_template()
Retrieve specific template.

```javascript
get_template({templateId: 1234, mode: "full"})        // Complete workflow
get_template({templateId: 1234, mode: "nodes_only"})  // Just node list
get_template({templateId: 1234, mode: "structure"})   // Nodes + connections
```

---

## Validation Tools

### validate_node()
Validate single node configuration.

```javascript
// Full validation (default)
validate_node({
  nodeType: "nodes-base.slack",
  config: {resource: "message", operation: "post"},
  mode: "full",
  profile: "strict"  // minimal, runtime (default), ai-friendly, strict
})

// Quick required fields only
validate_node({
  nodeType: "nodes-base.httpRequest",
  config: {method: "GET", url: "https://api.example.com"},
  mode: "minimal"
})
```

### validate_workflow()
Full workflow validation before deploy.

```javascript
validate_workflow({
  workflow: {
    name: "My Workflow",
    nodes: [...],
    connections: {...}
  },
  options: {
    validateNodes: true,
    validateConnections: true,
    validateExpressions: true,
    profile: "runtime"  // Use "strict" for production
  }
})
```

---

## Workflow Management

### n8n_create_workflow()
Create new workflow. Returns inactive workflow with ID.

```javascript
n8n_create_workflow({
  name: "New Workflow",
  nodes: [...],
  connections: {...},
  settings: {timezone: "America/New_York"}
})
```

### n8n_get_workflow()
Retrieve workflow with configurable detail.

```javascript
n8n_get_workflow({id: "abc123"})                    // Full (default)
n8n_get_workflow({id: "abc123", mode: "details"})   // With execution stats
n8n_get_workflow({id: "abc123", mode: "structure"}) // Nodes + connections only
n8n_get_workflow({id: "abc123", mode: "minimal"})   // Metadata only
```

### n8n_update_partial_workflow()
Incremental updates with diff operations.

```javascript
n8n_update_partial_workflow({
  id: "workflow_id",
  operations: [
    // Node operations
    {type: "addNode", node: {...}},
    {type: "removeNode", nodeName: "Old Node"},
    {type: "updateNode", nodeName: "HTTP Request", updates: {
      parameters: {url: "https://new-api.com"}
    }},
    {type: "moveNode", nodeName: "Code", position: [500, 300]},
    {type: "enableNode", nodeName: "Slack"},
    {type: "disableNode", nodeName: "Debug"},

    // Connection operations (see smart-parameters.md for IF/Switch)
    {type: "addConnection", source: "Webhook", target: "Transform"},
    {type: "removeConnection", source: "Transform", target: "Old Output", ignoreErrors: true},
    {type: "rewireConnection", source: "IF", oldTarget: "OldHandler", newTarget: "NewHandler", branch: "true"},
    {type: "cleanStaleConnections"},
    {type: "replaceConnections", nodeName: "Router", connections: {...}},

    // Metadata operations
    {type: "updateSettings", settings: {timezone: "UTC"}},
    {type: "updateName", name: "New Workflow Name"},
    {type: "addTag", tag: "production"},
    {type: "removeTag", tag: "development"},

    // Activation
    {type: "activateWorkflow"},
    {type: "deactivateWorkflow"}
  ],
  continueOnError: true  // Best-effort mode for bulk operations
})
```

### n8n_update_full_workflow()
Complete workflow replacement. **Warning: Missing nodes/connections deleted.**

```javascript
n8n_update_full_workflow({
  id: "abc123",
  intent: "Add error handling branch",  // Always include
  name: "Updated Workflow",
  nodes: [...],      // Complete nodes array
  connections: {...} // Complete connections object
})
```

### n8n_list_workflows()
List workflows with filters.

```javascript
n8n_list_workflows({
  limit: 50,
  active: true,
  tags: ["production"],
  cursor: "pagination_cursor"
})
// Returns: minimal metadata (id, name, active, tags, nodeCount)
```

### n8n_delete_workflow()
Permanent deletion. **Cannot be undone.**

```javascript
n8n_delete_workflow({id: "abc123"})
```

---

## Instance Management

### n8n_health_check()
Verify n8n connectivity.

```javascript
n8n_health_check({})                              // Quick status
n8n_health_check({mode: "diagnostic", verbose: true})  // Detailed
```

### n8n_autofix_workflow()
Auto-fix common issues.

```javascript
// Preview fixes first (default)
n8n_autofix_workflow({id: "abc123"})

// Apply fixes
n8n_autofix_workflow({
  id: "abc123",
  applyFixes: true,
  confidenceThreshold: "high",  // high (≥90%), medium (≥70%), low (any)
  fixTypes: [
    "expression-format",      // Fix {{ }} → ={{ }}
    "typeversion-correction", // Downgrade unsupported versions
    "error-output-config",    // Fix conflicting error settings
    "node-type-correction",   // Fix unknown node types
    "webhook-missing-path",   // Generate UUID for webhooks
    "typeversion-upgrade",    // Smart version upgrades
    "version-migration"       // Migration guidance
  ],
  maxFixes: 20
})
// Returns: postUpdateGuidance for manual migration steps
```

### n8n_executions()
Manage execution history.

```javascript
// List executions
n8n_executions({action: "list", workflowId: "abc123", status: "error", limit: 10})

// Get execution details
n8n_executions({action: "get", id: "exec_456", mode: "summary"})
// Modes: preview (structure), summary (2 items/node), filtered, full

// Filter specific nodes
n8n_executions({
  action: "get",
  id: "exec_456",
  mode: "filtered",
  nodeNames: ["HTTP Request", "Code"],
  itemsLimit: 5
})

// Delete execution
n8n_executions({action: "delete", id: "exec_456"})
```

### n8n_trigger_webhook_workflow()
Trigger via webhook. **Workflow must be ACTIVE.**

```javascript
n8n_trigger_webhook_workflow({
  webhookUrl: "https://n8n.example.com/webhook/abc",
  httpMethod: "POST",
  data: {key: "value"},
  headers: {"Authorization": "Bearer token"},
  waitForResponse: true
})
```

### n8n_workflow_versions()
Version management.

```javascript
// List versions
n8n_workflow_versions({mode: "list", workflowId: "abc123", limit: 10})

// Get specific version
n8n_workflow_versions({mode: "get", versionId: 42})

// Rollback
n8n_workflow_versions({mode: "rollback", workflowId: "abc123", versionId: 42, validateBefore: true})

// Cleanup old versions
n8n_workflow_versions({mode: "prune", workflowId: "abc123", maxVersions: 5})
```
