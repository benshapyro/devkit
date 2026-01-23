# Tool search tool (beta)

Use tool search when you have many tools (10+; especially 50+), or tool definitions are consuming too much context.

## Enable
Provider beta headers:
- Claude API / Microsoft Foundry: `advanced-tool-use-2025-11-20` (Opus 4.5, Sonnet 4.5)
- Vertex AI / Bedrock: `tool-search-tool-2025-10-19` (model support varies)

## Setup
1) Include a tool search tool in `tools`:

```json
{ "type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex" }
```

or

```json
{ "type": "tool_search_tool_bm25_20251119", "name": "tool_search_tool_bm25" }
```

2) Mark infrequently-used tools with `defer_loading: true`.

Constraints:
- At least one tool must be non-deferred.
- Regex variant expects Python `re.search()` patterns (not natural language).

## New content block types
- `server_tool_use` (tool search invocation)
- `tool_search_tool_result`
- `tool_reference` (inside tool search results)

The API auto-expands `tool_reference` blocks into full tool definitions before showing them to Claude.

## Limitations
- Not compatible with tool use examples (`input_examples`).
- Returns ~3–5 candidate tools per search.
