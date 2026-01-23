# OpenAI Web Search Tool (Snapshot)

Snapshot date: 2026-01-05
Source: OpenAI web_search guide

## Enable web_search
- Add `{ "type": "web_search" }` to the `tools` array in a Responses API request.
- Optionally set `tool_choice` to force or disable tool use.

## Response shape
- Responses include a `web_search_call` item describing the search action.
- The assistant message includes `output_text` and annotations with source pointers.

## Sources and citations
- Use `include: ["web_search_call.action.sources"]` to return the full sources list.
- Preserve citations in the final response when sources are used.

## Domain filtering
- Use web_search filters to allow or block specific domains when you need higher quality sources.

## Notes
- web_search is only available via the Responses API, not Chat Completions.
- Always validate for freshness and stability when citing web results.
