# Fine-grained tool streaming (beta)

Purpose: stream tool parameters faster by skipping buffering / JSON validation.

## Enable
- Beta: `fine-grained-tool-streaming-2025-05-14`
- Request must use tools + `stream: true`

## Implications
- Tool `input` deltas may be invalid JSON mid-stream.
- If `stop_reason: "max_tokens"` occurs mid-parameter, you may end with incomplete JSON.

## Suggested handling
- Treat streamed tool input as a best-effort incremental preview.
- Only attempt JSON parsing at block stop; if parsing fails, handle as recoverable error (retry with higher `max_tokens` or ask model to re-emit inputs).
- If you need to pass invalid JSON back to the model, wrap it in a JSON object like:

```json
{ "INVALID_JSON": "<raw partial_json>" }
```
