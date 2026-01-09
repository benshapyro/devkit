/* Minimal manual tool loop via fetch (no SDK). */

type ToolUseBlock = {
	type: "tool_use";
	id: string;
	name: string;
	input: Record<string, unknown>;
};

type ContentBlock =
	| { type: "text"; text: string }
	| ToolUseBlock
	| { type: string; [k: string]: unknown };

type MessageResponse = {
	content: ContentBlock[];
	stop_reason: string | null;
};

function executeTool(name: string, input: Record<string, unknown>): string {
	if (name === "add") {
		return String(Number(input.a) + Number(input.b));
	}
	throw new Error(`Unknown tool: ${name}`);
}

async function createMessage(params: Record<string, unknown>): Promise<MessageResponse> {
	const apiKey = process.env.ANTHROPIC_API_KEY;
	if (!apiKey) throw new Error("Set ANTHROPIC_API_KEY");

	const res = await fetch("https://api.anthropic.com/v1/messages", {
		method: "POST",
		headers: {
			"content-type": "application/json",
			"x-api-key": apiKey,
			"anthropic-version": "2023-06-01",
		},
		body: JSON.stringify(params),
	});

	if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
	return (await res.json()) as MessageResponse;
}

async function main() {
	const tools = [
		{
			name: "add",
			description: "Add two numbers and return the sum as a string.",
			input_schema: {
				type: "object",
				properties: { a: { type: "number" }, b: { type: "number" } },
				required: ["a", "b"],
				additionalProperties: false,
			},
		},
	];

	const messages: Array<{ role: "user" | "assistant"; content: unknown }> = [
		{ role: "user", content: "What is 12 + 30? Use the add tool." },
	];

	while (true) {
		const resp = await createMessage({
			model: "claude-sonnet-4-5",
			max_tokens: 256,
			tools,
			tool_choice: { type: "auto" },
			messages,
		});

		if (resp.stop_reason !== "tool_use") {
			const text = resp.content.find((b) => b.type === "text") as { type: "text"; text: string } | undefined;
			console.log(text?.text ?? "");
			return;
		}

		const toolUses = resp.content.filter((b): b is ToolUseBlock => b.type === "tool_use");
		const toolResults = toolUses.map((u) => ({
			type: "tool_result",
			tool_use_id: u.id,
			content: executeTool(u.name, u.input),
		}));

		messages.push({ role: "assistant", content: resp.content });
		messages.push({ role: "user", content: toolResults });
	}
}

main().catch((err) => {
	console.error(err);
	process.exit(1);
});
