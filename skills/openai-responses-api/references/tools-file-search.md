# OpenAI File Search Tool (Snapshot)

Snapshot date: 2026-01-05
Source: OpenAI file_search guide

## Enable file_search
- Create a vector store, then upload files to it.
- Add the file IDs to the vector store.
- Call Responses API with `tools: [{"type": "file_search", "vector_store_ids": ["..."]}]`.

## Response shape
- Results are returned through tool calls.
- Use `include: ["file_search_call.results"]` to retrieve the raw match list when needed.

## Notes
- File search uses hosted embeddings and retrieval; it is not the same as local vault search.
- Verify available tool parameters (such as result limits) in the official docs during quarterly refresh.
