# Prompt caching (Messages API)

## What it is
Prompt caching caches a prefix of your request so subsequent calls can reuse it at much lower latency and cost.

You place cache breakpoints by attaching `cache_control` to a **content block**.

```json
{ "cache_control": { "type": "ephemeral", "ttl": "5m" | "1h" } }
```

## Where cache_control can go
`cache_control` can be placed on many content blocks in:
- `tools` tool definitions (cached first)
- `system` content blocks (cached second)
- `messages[*].content` blocks (cached last)

This forms a caching hierarchy:
`tools → system → messages`.

## TTLs
- Default TTL is 5 minutes.
- `ttl: "1h"` enables 1-hour caching (higher write cost).

You can mix TTLs, but longer TTL breakpoints must appear before shorter TTL breakpoints.

## Cache hit behavior
Cache hits require exact matching of the prompt prefix up to a breakpoint.

The system checks for cache hits by searching backwards from your explicit breakpoint with a **20-block lookback window**. If you edit content earlier than that window, you may need earlier breakpoints.

You can include up to 4 cache breakpoints.

## What cannot be cached (key gotchas)
- Empty text blocks cannot be cached.
- Sub-objects (like `citations` objects) can’t be cached directly; cache the parent block.

## What invalidates the cache (high-signal table)
Changes invalidate that level and all following levels:
- Tool definitions → invalidates tools + system + messages
- Enabling/disabling web search or citations → invalidates system + messages
- Changing `tool_choice` → invalidates messages only
- Adding/removing images anywhere → invalidates messages only
- Changing thinking parameters → invalidates messages only

## Tracking cache usage
Read cache metrics from `response.usage`:
- `cache_creation_input_tokens`
- `cache_read_input_tokens`
- `cache_creation` (per-TTL breakdown)

Total input tokens:

```text
total_input_tokens = cache_read_input_tokens + cache_creation_input_tokens + input_tokens
```

## Recommended patterns
- Put stable content first: tool definitions, long system context, reference documents.
- Put your breakpoint right after the stable prefix.
- For long conversations (>20 blocks), use additional breakpoints earlier to preserve hits when older blocks change.
