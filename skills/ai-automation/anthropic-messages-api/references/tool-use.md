# Anthropic Tool Use (Snapshot)

Snapshot date: 2026-01-05
Source: Anthropic tool-use documentation

## Tool definitions
- Define tools with `name`, `description`, and `input_schema`.
- Optional fields you may encounter:
  - `strict: true` (requires structured outputs beta)
  - `input_examples` (beta; provider-specific header)
  - `defer_loading: true` (tool search tool)
  - `allowed_callers` (programmatic tool calling)
- Provide tools in the request `tools` array.

## Tool use flow
1) Model responds with `tool_use` content blocks (id, name, input).
2) Execute the tool.
3) Send the results back as `tool_result` content blocks in the next user message.
4) `tool_result` blocks must appear before any other content in that message.

### Ordering rules (strict)
- Tool result blocks must immediately follow their corresponding tool use blocks in the message history.
- In the user message with tool results, `tool_result` blocks must come first; any text must come after.

### Programmatic tool calling caveat
If a tool call is programmatic (caller is code execution), your response must contain **only** `tool_result` blocks (no extra text) while there are pending programmatic tool calls.

## tool_choice behavior
- `tool_choice` is an object:

```json
{ "type": "auto" | "any" | "tool" | "none", "name"?: "<toolName>", "disable_parallel_tool_use"?: true }
```

- `auto` lets the model decide whether to use tools.
- `any` forces the model to use one of the provided tools.
- `tool` forces a specific tool by name.
- `none` prevents the model from using tools.
- `disable_parallel_tool_use: true` changes tool-call cardinality:
  - with `type: "auto"`: at most one tool
  - with `type: "any"` / `type: "tool"`: exactly one tool
- For extended thinking, only `tool_choice: {"type":"auto"}` and `tool_choice: {"type":"none"}` are supported.

## Notes
- Server tools (e.g. web search) appear as `server_tool_use` blocks and return corresponding server tool result blocks (e.g. `web_search_tool_result`).
- Some tool features require beta headers:
  - `fine-grained-tool-streaming-2025-05-14`
  - `advanced-tool-use-2025-11-20` (tool examples, tool search tool, programmatic tool calling)
  - `structured-outputs-2025-11-13` (strict tools)
- Prefer the SDK tool runner when you don't need custom tool-loop control.
