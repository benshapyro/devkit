# Advanced tool use (2025-era features)

## tool_choice shape and parallel control
`tool_choice` is an object:

```json
{ "type": "auto" | "any" | "tool" | "none", "name"?: "<toolName>", "disable_parallel_tool_use"?: true }
```

- `disable_parallel_tool_use: true` with `type: "auto"` => at most one tool
- `disable_parallel_tool_use: true` with `type: "any"` / `type: "tool"` => exactly one tool

## Tool use examples (input_examples) (beta)
For complex tools, `input_examples` can improve call quality.

Provider-specific beta headers:
- Claude API / Microsoft Foundry: `advanced-tool-use-2025-11-20`
- Vertex AI / Bedrock: `tool-examples-2025-10-29` (Opus 4.5 only)

Limitations:
- Examples must validate against `input_schema` (invalid examples cause 400).
- Not supported for server-side tools.

## Tool runner (SDK beta)
SDKs provide an auto-looping tool runner that:
- detects tool calls
- executes tools
- formats tool results
- can use client-side compaction to manage long contexts

Use it unless you need custom control over the tool loop.

## Fine-grained tool streaming (beta)
Beta: `fine-grained-tool-streaming-2025-05-14`

Streams tool params without buffering / JSON validation.
This means you may receive invalid or partial JSON; your code must handle that.
