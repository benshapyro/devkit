---
name: openai-responses-api
description: Implement and troubleshoot OpenAI Responses API calls, model selection, tool use (web_search, file_search, code interpreter), output parsing, and routing decisions. Use when integrating OpenAI APIs, migrating from Chat Completions, enabling built-in tools, or checking parameter support/limits.
---

# OpenAI Responses API

## Overview
Use this skill to build or debug Responses API integrations and built-in tool usage. Keep it current with quarterly refreshes and verify critical details against the official docs when needed.

## Quick start
1) Choose a model and decide if built-in tools are required.
2) Build the request with `model`, `input`, `instructions`, `max_output_tokens`, and optional `tools` + `tool_choice`.
3) Parse output via `response.output_text` when available; otherwise iterate `response.output` for `message` items and `output_text` parts.
4) When tools are enabled, use `include` fields to return sources or raw results if you need citations or debugging.
5) Log model, tokens, and tool calls for traceability.

## Core tasks
### Use web_search
- Add `{ "type": "web_search" }` in `tools`.
- Use `include: ["web_search_call.action.sources"]` to get the full sources list.
- Respect inline citations in the model response.

### Use file_search
- Create a vector store, upload files, and attach file IDs to the vector store.
- Add `{ "type": "file_search", "vector_store_ids": ["..."] }` in `tools`.
- Use `include: ["file_search_call.results"]` if you need raw retrieval results.

### Migrate from Chat Completions
- System prompt -> `instructions`.
- Messages -> `input` (string or structured input items).
- `max_tokens` -> `max_output_tokens`.
- Tool calling uses `tools` and `tool_choice`.

### Conversation state
- Use `previous_response_id` or `conversation` for multi-turn state; do not use both in the same request.

## References
- `references/responses-api.md` - request/response field list and object layout.
- `references/tools-web-search.md` - web_search behavior, citations, and sources.
- `references/tools-file-search.md` - vector stores, file uploads, file_search tool usage.
- `references/models-gpt5-mini.md` - GPT-5 mini capabilities, pricing, and tool support.
