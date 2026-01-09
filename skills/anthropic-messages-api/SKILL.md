---
name: anthropic-messages-api
description: Implement and troubleshoot Anthropic Messages API calls, model selection, tool use blocks, and response parsing. Use when integrating Claude via the Messages API, adding tool use, or checking model IDs and alias behavior.
---

# Anthropic Messages API

## Overview
Use this skill to build or debug Claude Messages API integrations: request shape, streaming, prompt caching, tool use (client + server tools), structured outputs, and stop-reason handling.

## Quick start
1) Choose a model (prefer fixed snapshot IDs for production).
2) Build the request with `model`, `max_tokens`, and `messages` (role + content blocks).
3) Provide system instructions via the top-level `system` field.
4) If tools are needed, include `tools` and `tool_choice` (object); handle `tool_use` + `tool_result` blocks.
5) If you need streaming, set `stream: true` and parse SSE events.
6) If you need caching, use `cache_control` on content blocks.
7) If you need guaranteed JSON/tool inputs, use structured outputs (beta).
8) Parse response content blocks and check `stop_reason`.

## Tool use flow
- When `stop_reason` is `tool_use`, extract `tool_use` blocks (id, name, input).
- Execute the tool and respond with `tool_result` blocks in the next user message.
- `tool_result` blocks must come before any other content in that message.

### tool_choice (object)
Use the documented object shape:

```json
{ "type": "auto" | "any" | "tool" | "none", "name"?: "<toolName>", "disable_parallel_tool_use"?: true }
```

Notes:
- `disable_parallel_tool_use: true` means:
  - with `type: "auto"`: at most one tool
  - with `type: "any"` / `type: "tool"`: exactly one tool
- With extended thinking enabled, only `tool_choice: {"type":"auto"}` or `{"type":"none"}` are allowed.

### Server tools (e.g. web search)
Server tools appear as `server_tool_use` blocks (not `tool_use`) and typically do not require you to send `tool_result` back.

## Streaming (SSE)
When `stream: true`, parse these event types:
- `message_start`
- `content_block_start` / `content_block_delta` / `content_block_stop`
- `message_delta` (contains `stop_reason`)
- `message_stop`
- `ping`, `error` (may appear anytime)

Tool inputs stream via `input_json_delta.partial_json` (accumulate and parse at `content_block_stop`). Thinking streams via `thinking_delta` plus a `signature_delta` before block stop.

## Prompt caching
Use `cache_control` on content blocks to cache prompt prefixes:

```json
{ "cache_control": { "type": "ephemeral", "ttl": "5m" | "1h" } }
```

Key gotchas:
- Cache hierarchy is `tools → system → messages`.
- Changing `tool_choice` invalidates message caching but not tool/system caching.
- Empty text blocks cannot be cached.

## Structured outputs (beta)
Two related features:
- **JSON outputs**: `output_format: { type: "json_schema", schema: ... }`
- **Strict tool use**: `tools[].strict: true`

Enable with beta `structured-outputs-2025-11-13`. Refusals and `max_tokens` can still break schema guarantees.

## Advanced agent patterns (optional)
- **Tool runner (SDK beta)**: auto tool-loop execution + optional compaction.
- **Fine-grained tool streaming (beta)**: streams tool parameters without buffering/validation.
- **Tool search tool (beta)**: supports `defer_loading: true` + `tool_reference` blocks for large tool catalogs.
- **Programmatic tool calling (beta)**: uses code execution containers; tools may declare `allowed_callers`; has “tool_result-only response” restrictions while pending.
- **Message Batches API**: async processing at ~50% cost; fits large offline jobs.

## References
- `references/messages-api.md` - request/response field snapshot and headers.
- `references/tool-use.md` - tool_use and tool_result handling rules.
- `references/models.md` - model IDs, aliases, and selection guidance.

Additional references:
- `references/prompt-caching.md`
- `references/streaming-sse.md`
- `references/stop-reasons.md`
- `references/structured-outputs.md`
- `references/advanced-tool-use.md`
- `references/fine-grained-tool-streaming.md`
- `references/tool-search.md`
- `references/programmatic-tool-calling.md`
- `references/batches.md`

## Assets (optional)
See `assets/snippets/` for minimal curl + Python + TypeScript templates.
