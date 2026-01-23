# Structured outputs (beta)

Structured outputs provide schema guarantees via constrained decoding.

Enable with beta: `structured-outputs-2025-11-13`.

## JSON outputs (output_format)
Use when you want Claude’s *final response text* to be valid JSON.

```json
{
  "output_format": {
    "type": "json_schema",
    "schema": {
      "type": "object",
      "properties": { "name": {"type": "string"} },
      "required": ["name"],
      "additionalProperties": false
    }
  }
}
```

The JSON is returned as `response.content[0].text`.

## Strict tool use (tools[].strict)
Use when you need tool `name` + `input` to be schema-valid.

```json
{
  "tools": [
    {
      "name": "get_weather",
      "description": "...",
      "strict": true,
      "input_schema": { "type": "object", "properties": {"location": {"type": "string"}}, "required": ["location"], "additionalProperties": false }
    }
  ]
}
```

## When guarantees can fail
- `stop_reason: "refusal"` can override schema.
- `stop_reason: "max_tokens"` can truncate JSON.

## Compatibility notes
- Incompatible with citations when using `output_format`.
- Incompatible with message prefilling when using `output_format`.
- Works with streaming and batches.
