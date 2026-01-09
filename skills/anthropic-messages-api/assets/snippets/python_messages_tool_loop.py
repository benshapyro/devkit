"""Minimal manual tool loop using the official Anthropic Python SDK.

This is a template: wire execute_tool() to your real functions.
"""

from __future__ import annotations

import json
import os
from typing import Any

import anthropic


def execute_tool(name: str, tool_input: dict[str, Any]) -> str:
	# Replace with your real tool implementations.
	if name == "add":
		return str(tool_input["a"] + tool_input["b"])
	raise ValueError(f"Unknown tool: {name}")


def main() -> None:
	client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

	tools = [
		{
			"name": "add",
			"description": "Add two integers and return the sum as a string.",
			"input_schema": {
				"type": "object",
				"properties": {"a": {"type": "integer"}, "b": {"type": "integer"}},
				"required": ["a", "b"],
				"additionalProperties": False,
			},
		}
	]

	messages: list[dict[str, Any]] = [
		{"role": "user", "content": "What is 12 + 30? Use the add tool."}
	]

	while True:
		resp = client.messages.create(
			model="claude-sonnet-4-5",
			max_tokens=256,
			messages=messages,
			tools=tools,
			tool_choice={"type": "auto"},
		)

		if resp.stop_reason != "tool_use":
			print(resp.content[0].text if resp.content else "")
			return

		tool_results: list[dict[str, Any]] = []
		for block in resp.content:
			if block.type != "tool_use":
				continue
			result = execute_tool(block.name, dict(block.input))
			tool_results.append(
				{
					"type": "tool_result",
					"tool_use_id": block.id,
					"content": result,
				}
			)

		# Append assistant tool_use content, then user tool_result blocks.
		messages.append({"role": "assistant", "content": resp.content})
		messages.append({"role": "user", "content": tool_results})


if __name__ == "__main__":
	main()
