# Common Pitfalls

Mistakes to avoid and how to prevent them.

## Critical Pitfalls

| Pitfall | Consequence | Prevention |
|---------|-------------|------------|
| Using `sourceIndex` for IF branches | All connections go to same branch | Use `branch="true"/"false"` parameter |
| Forgetting webhook `.body` | Cannot access payload data | Always access `$json.body` for webhook data |
| AI agent without language model | Validation failure | Connect language model BEFORE enabling agent |
| Main connections to AI nodes | Incorrect workflow structure | AI nodes only use AI-specific connections |
| Using `null` to remove properties | Property set to null, not removed | Use `undefined` to remove completely |
| Large batch ops without `continueOnError` | Single failure stops all operations | Set `continueOnError: true` for bulk ops |

## Connection Pitfalls

| Pitfall | Consequence | Prevention |
|---------|-------------|------------|
| Using personas in prompts | 13-30% performance degradation | Use methodology-based instructions |
| Skipping validation before deploy | Import failures, runtime errors | Always `validate_workflow()` before create/update |
| Missing `toolDescription` on HTTP Request Tool | Validation fails (min 15 chars) | Add descriptive tool purpose |
| Streaming mode with main outputs | AI Agent validation fails | Remove main outputs when streaming |
| Fallback model without `needsFallback` | Fallback never triggers | Set `needsFallback: true` on AI Agent |

## Code Node Pitfalls

| Pitfall | Consequence | Prevention |
|---------|-------------|------------|
| Not returning array with `json` key | Node fails silently | Always `return [{ json: {...} }]` |
| Using external Python libraries | ImportError at runtime | Use HTTP Request node for APIs |
| Accessing `$json` directly for webhooks | Missing data | Use `$json.body` for webhook payloads |
| Forgetting `await` on async operations | Promise returned instead of data | Always `await` httpRequest and async calls |

## Workflow Structure Pitfalls

| Pitfall | Consequence | Prevention |
|---------|-------------|------------|
| Hardcoded credentials | Security vulnerability | Always use credential references |
| Duplicate webhook paths | Only first one triggers | Use unique paths per workflow |
| Missing error handling | Silent failures | Add error branches at critical points |
| No `executionOrder` setting | Unpredictable flow in complex workflows | Set `"executionOrder": "v1"` in settings |

## Update Operation Pitfalls

| Pitfall | Consequence | Prevention |
|---------|-------------|------------|
| Using `n8n_update_full_workflow` for small changes | Risk of losing nodes/connections | Use `n8n_update_partial_workflow` |
| Forgetting `cleanStaleConnections` after deletions | Broken connection references | Run cleanup after node removals |
| Not including `intent` in full updates | Poor error messages | Always include intent description |
| Renaming nodes manually in connections | Orphaned references | Let auto-update handle via `updateNode` |

## Validation Pitfalls

| Pitfall | Consequence | Prevention |
|---------|-------------|------------|
| Using `profile: "minimal"` for production | Missing critical checks | Use `profile: "strict"` for production |
| Ignoring `postUpdateGuidance` from autofix | Missing manual migration steps | Always review guidance output |
| Applying autofix without preview | Unexpected changes | Preview first, then apply with confidence threshold |

## Performance Pitfalls

| Pitfall | Consequence | Prevention |
|---------|-------------|------------|
| Loading all items in memory | Out of memory on large datasets | Use streaming/pagination |
| Synchronous loops with API calls | Slow execution, timeouts | Use SplitInBatches node |
| No rate limiting on external APIs | API throttling, bans | Add Wait nodes or use built-in rate limiting |
