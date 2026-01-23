# Message Batches API (batch processing)

Use batches for offline / non-interactive workloads where immediate responses are not required.

## What it is
Submit many Messages requests to `/v1/messages/batches` for asynchronous processing.

Benefits:
- ~50% cost reduction vs standard requests
- high throughput, asynchronous

## Limits (documented)
- Up to 100,000 requests per batch or 256 MB total size (whichever comes first)
- Most batches finish in <1 hour; expire after 24 hours if not completed
- Results are available for 29 days

## Request shape (high level)
Each entry has:
- `custom_id` (you choose)
- `params` (a normal `/v1/messages` request payload)

Batch results are returned as `.jsonl` and are not guaranteed to be in the same order as requests—use `custom_id`.

## Prompt caching with batches
Batches support prompt caching (discounts can stack), but cache hits are best-effort because requests execute concurrently.

For long-running batches, consider `ttl: "1h"`.
