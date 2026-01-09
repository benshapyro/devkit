# OpenAI Responses API Reference (Snapshot)

Snapshot date: 2026-01-05
Source: OpenAI Responses API reference

## Request fields (create)
- model: string, required
- input: string or structured content items
- instructions: string system guidance
- max_output_tokens: integer output cap
- temperature: float sampling
- top_p: float nucleus sampling
- stream: boolean
- stream_options: object
- include: array of strings to return additional tool details
- tools: array of tool definitions (web_search, file_search, code_interpreter, etc.)
- tool_choice: object or string directive
- parallel_tool_calls: boolean
- max_tool_calls: integer
- previous_response_id: string, resume prior response state
- conversation: string, conversation identifier
- metadata: object
- prompt: string or object (legacy compatibility)
- prompt_cache_key: string
- prompt_cache_retention: string
- reasoning: object
- safety_identifier: string
- service_tier: string
- store: boolean
- text: object

Notes:
- Use max_output_tokens (not max_tokens) for Responses API.
- Use include when you need raw tool results or source lists.
- Use previous_response_id or conversation, not both.

## Response fields (high level)
- id: string
- object: string
- created_at: timestamp
- model: string
- output: array of items (messages, tool calls, tool results)
- output_text: convenience string (SDK)
- usage: token usage
- error: error payload if request fails

## Output parsing hints
- Prefer response.output_text if present.
- Otherwise iterate response.output for items where type == "message" and content has type == "output_text".

For full details, re-check the official API reference on each quarterly refresh.
