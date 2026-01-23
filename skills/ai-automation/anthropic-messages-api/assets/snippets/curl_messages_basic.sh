#!/usr/bin/env bash
set -euo pipefail

: "${ANTHROPIC_API_KEY:?Set ANTHROPIC_API_KEY}"

curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: ${ANTHROPIC_API_KEY}" \
  -H "anthropic-version: 2023-06-01" \
  -d @- <<'JSON'
{
  "model": "claude-sonnet-4-5",
  "max_tokens": 256,
  "messages": [
    {"role": "user", "content": "Hello"}
  ]
}
JSON
