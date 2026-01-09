# stop_reason handling

Claude returns `stop_reason` on successful Messages responses.

## Values and what to do

### end_turn
Normal completion. Parse the message content.

### max_tokens
Output hit your requested `max_tokens`. Options:
- increase `max_tokens`
- ask the model to continue (new user message)

### stop_sequence
Your `stop_sequences` matched. Handle like completion; use `stop_sequence` to identify which one.

### tool_use
Model is requesting client tool execution.
- extract `tool_use` blocks
- execute them
- respond with `tool_result` blocks (must be first in that user message)

### pause_turn
Typically returned for long-running server tool turns (e.g. web search). To continue:
- send a follow-up request including the assistant content **as-is**
- include the same `tools` so the model can continue its paused turn

### refusal
Model refused (safety / streaming classifiers).
- treat as a successful response that you should display/handle
- consider a safer rephrase or fallback behavior

### model_context_window_exceeded
Response hit the model’s context limit before hitting `max_tokens`.
- treat content as valid but truncated
- respond by reducing context, compacting/summarizing, or splitting the task

## Streaming note
In streaming mode:
- `stop_reason` is `null` in `message_start`
- it arrives in `message_delta`
