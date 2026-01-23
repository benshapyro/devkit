#!/usr/bin/env bash
set -euo pipefail

: "${ANTHROPIC_API_KEY:?Set ANTHROPIC_API_KEY}"

# Requires beta: structured-outputs-2025-11-13
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: ${ANTHROPIC_API_KEY}" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: structured-outputs-2025-11-13" \
  -d @- <<'JSON'
{
  "model": "claude-sonnet-4-5",
  "max_tokens": 512,
  "messages": [
    {"role": "user", "content": "Extract name and email: John Smith (john@example.com)."}
  ],
  "output_format": {
    "type": "json_schema",
    "schema": {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"}
      },
      "required": ["name", "email"],
      "additionalProperties": false
    }
  }
}
JSON
