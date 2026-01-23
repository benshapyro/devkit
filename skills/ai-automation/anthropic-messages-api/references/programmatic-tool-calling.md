# Programmatic tool calling (beta)

Programmatic tool calling lets Claude call your tools from within a code execution container, reducing latency and token usage for multi-tool workflows.

## Enable
- Beta: `advanced-tool-use-2025-11-20`
- Requires the code execution tool (e.g. `code_execution_20250825`) in `tools`.
- Supported models (per docs): Sonnet 4.5 and Opus 4.5.

## Tool configuration
Tools can specify `allowed_callers`:

```json
{
  "name": "query_database",
  "input_schema": {"type": "object", "properties": {"sql": {"type": "string"}}, "required": ["sql"]},
  "allowed_callers": ["code_execution_20250825"]
}
```

Possible values:
- `["direct"]` (default)
- `["code_execution_20250825"]`
- `["direct", "code_execution_20250825"]`

## Response differences
Tool use blocks include a `caller` field:
- direct: `{ "type": "direct" }`
- programmatic: `{ "type": "code_execution_20250825", "tool_id": "srvtoolu_..." }`

## Container lifecycle
- Responses can include `container: { id, expires_at }`.
- Containers expire after minutes of inactivity; you must respond to tool calls before expiration.
- Pass `container: "container_..."` back to reuse state.

## Formatting restriction (critical)
When responding to *pending programmatic tool calls*, your message must contain **only** `tool_result` blocks.

```json
{ "role": "user", "content": [ {"type":"tool_result", "tool_use_id":"toolu_...", "content":"..."} ] }
```

No text content is allowed in that message until the programmatic calls are resolved.

## Incompatibilities
- Structured outputs strict tools are not supported with programmatic calling.
- `disable_parallel_tool_use: true` is not supported with programmatic calling.
