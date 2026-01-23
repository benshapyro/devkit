# Smart Parameters & Property Management

Patterns for multi-output nodes, connection routing, and property handling.

## IF Node Connections

**Use `branch` parameter, NOT `sourceIndex`.**

```javascript
// CORRECT: Use branch parameter
{type: "addConnection", source: "IF", target: "Success Handler", branch: "true"}
{type: "addConnection", source: "IF", target: "Failure Handler", branch: "false"}
```

### Critical: sourceIndex Trap
Using `sourceIndex=0` for multiple connections puts ALL on the same branch.

```javascript
// WRONG: Both connections go to TRUE branch!
{type: "addConnection", source: "IF", target: "Handler1", sourceIndex: 0}
{type: "addConnection", source: "IF", target: "Handler2", sourceIndex: 0}

// CORRECT: Explicit branch assignment
{type: "addConnection", source: "IF", target: "Handler1", branch: "true"}
{type: "addConnection", source: "IF", target: "Handler2", branch: "false"}
```

## Switch Node Connections

**Use `case` parameter for Switch nodes.**

```javascript
{type: "addConnection", source: "Switch", target: "Case 0 Handler", case: 0}
{type: "addConnection", source: "Switch", target: "Case 1 Handler", case: 1}
{type: "addConnection", source: "Switch", target: "Default Handler", case: 2}
```

## Rewiring Connections

Combine remove + add in one operation with smart parameters.

```javascript
// Rewire IF branch
{type: "rewireConnection", source: "IF", oldTarget: "OldSuccess", newTarget: "NewSuccess", branch: "true"}

// Rewire Switch case
{type: "rewireConnection", source: "Switch", oldTarget: "OldCase1", newTarget: "NewCase1", case: 1}
```

## Property Management

### Removing Properties
**Use `undefined` (not `null`) to remove properties completely.**

```javascript
// Set to undefined removes the property
{type: "updateNode", nodeName: "HTTP Request", updates: {
  continueOnFail: undefined,  // Removes this property
  onError: "continueErrorOutput"  // Sets new value
}}

// Using null just sets property to null (NOT removed)
{type: "updateNode", nodeName: "HTTP Request", updates: {
  continueOnFail: null  // Property exists with null value - probably not what you want
}}
```

### Nested Property Removal
Use dot notation for nested properties.

```javascript
{type: "updateNode", nodeName: "Code", updates: {
  "parameters.authentication": undefined
}}
```

### Migrating Deprecated Properties
```javascript
{type: "updateNode", nodeName: "Webhook", updates: {
  responseMode: undefined,  // Remove old location
  "options.responseMode": "responseNode"  // Add at new location
}}
```

## Cleanup & Recovery

### cleanStaleConnections
Remove all broken connection references. Use after node deletions or renames.

```javascript
{type: "cleanStaleConnections"}
```

### continueOnError Mode
Apply valid operations even if some fail. Useful for bulk operations.

```javascript
n8n_update_partial_workflow({
  id: "abc123",
  operations: [...],
  continueOnError: true
})
```

### ignoreErrors on removeConnection
Graceful cleanup - won't fail if connection doesn't exist.

```javascript
{type: "removeConnection", source: "A", target: "B", ignoreErrors: true}
```

## Auto-Sanitization

When ANY workflow update is made, auto-sanitization runs on ALL nodes:
- Fixes binary operator structures (removes singleValue)
- Fixes unary operator structures (adds singleValue: true)
- Adds missing IF/Switch conditions.options structure

**Cannot auto-fix:**
- Broken connections
- Branch count mismatches
- Paradoxical states

## Automatic Connection Reference Updates

When renaming nodes with `updateNode`, all connection references auto-update:

```javascript
{type: "updateNode", nodeName: "Old Name", updates: {name: "New Name"}}
// All connections referencing "Old Name" automatically update to "New Name"
```
