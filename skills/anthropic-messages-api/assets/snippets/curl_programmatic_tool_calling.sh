#!/usr/bin/env bash
set -euo pipefail

: "${ANTHROPIC_API_KEY:?Set ANTHROPIC_API_KEY}"

# Template only. Requires code execution tool to be enabled for your org.
# Beta: advanced-tool-use-2025-11-20
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: ${ANTHROPIC_API_KEY}" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: advanced-tool-use-2025-11-20" \
  -d @- <<'JSON'
{
  "model": "claude-sonnet-4-5",
  "max_tokens": 2048,
  "messages": [
    {
      "role": "user",
      "content": "Call query_database for 3 regions, aggregate totals, and tell me which region is highest."
    }
  ],
  "tools": [
    {"type": "code_execution_20250825", "name": "code_execution"},
    {
      "name": "query_database",
      "description": "Execute a SQL query and return rows as JSON.",
      "input_schema": {
        "type": "object",
        "properties": {"sql": {"type": "string"}},
        "required": ["sql"],
        "additionalProperties": false
      },
      "allowed_callers": ["code_execution_20250825"]
    }
  ]
}
JSON
