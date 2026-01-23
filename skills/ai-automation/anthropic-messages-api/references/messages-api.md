# Anthropic Messages API Reference (Snapshot)

Snapshot date: 2026-01-05
Sources: Anthropic messages examples and model docs

## Endpoint and headers
- POST /v1/messages
- Headers:
  - x-api-key: API key
  - anthropic-version: required API version
  - content-type: application/json

## Request fields (common)
- model: string, required
- max_tokens: integer, required
- messages: array of { role, content }
- system: string or array of system content blocks (top-level)
- tools: array of tool definitions
- tool_choice: object controlling tool usage (see tool-use doc)
- stream: boolean
- stop_sequences: array of strings
- temperature: float
- top_p: float
- top_k: integer
- metadata: object
- output_format: optional (structured outputs beta)

### content blocks (high level)
`messages[*].content` and `system` can be strings or arrays of content blocks. Common block types:
- `text`
- `image` (base64 or url)
- `document` (base64 or url)
- `tool_use`
- `tool_result`
- `thinking`, `redacted_thinking`
- server tool blocks like `server_tool_use` / `web_search_tool_result`

### prompt caching
Many content blocks accept `cache_control: { type: "ephemeral", ttl?: "5m" | "1h" }`.

## Response fields (common)
- id: string
- type: "message"
- role: "assistant"
- content: array of content blocks (text, tool_use, etc.)
- model: string
- stop_reason: string
- stop_sequence: string or null
- usage: object (token counts)

### stop_reason values (documented)
- `end_turn`
- `max_tokens`
- `stop_sequence`
- `tool_use`
- `pause_turn`
- `refusal`
- `model_context_window_exceeded`

### usage highlights (documented)
- `input_tokens`, `output_tokens`
- prompt caching: `cache_read_input_tokens`, `cache_creation_input_tokens`, `cache_creation` (per-ttl breakdown)
- server tools: `server_tool_use` (e.g. `{ web_search_requests: n }`)
- `service_tier`: `standard` | `priority` | `batch`

Notes:
- This is a curated snapshot based on public docs and examples. Verify the full parameter list in the official API reference during quarterly refreshes.
