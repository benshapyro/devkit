# Streaming (SSE) for Messages API

## How to enable
Set `stream: true` in your `/v1/messages` request. The response is server-sent events (SSE).

## Event flow
Typical order:
1. `message_start` (message object with empty content)
2. For each content block index:
   - `content_block_start`
   - one or more `content_block_delta`
   - `content_block_stop`
3. one or more `message_delta`
4. `message_stop`

Other events:
- `ping` can appear anytime
- `error` can appear anytime

In streaming mode, `stop_reason` is:
- `null` in `message_start`
- set in `message_delta`

## Delta types you must handle
### Text
`content_block_delta.delta.type = "text_delta"` with `text`.

### Tool inputs
For `tool_use` / `server_tool_use` blocks, deltas can be:

```json
{ "type": "input_json_delta", "partial_json": "{\"location\": \"San Fra" }
```

Accumulate `partial_json` chunks (string concatenation) until the block stops, then parse as JSON.

### Thinking
When extended thinking is enabled:
- `thinking_delta` emits `thinking`
- a `signature_delta` occurs before the block ends

You must preserve the final `signature` if you pass thinking blocks back during tool loops.

## Error handling
Streaming errors can arrive as:

```json
{ "type": "error", "error": { "type": "overloaded_error", "message": "Overloaded" } }
```

Treat unknown event types as non-fatal (versioning policy).

## Recovery pattern (high level)
If the stream is interrupted, you can retry by:
- saving all content blocks you received
- constructing a follow-up request including the partial assistant content
- asking to continue

Note: tool blocks and thinking blocks generally cannot be “partially recovered” in a meaningful way; prefer retrying with higher `max_tokens` if truncation occurs during tool emission.
