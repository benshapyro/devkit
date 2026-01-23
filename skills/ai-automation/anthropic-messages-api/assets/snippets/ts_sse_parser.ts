/* Minimal SSE parser for Anthropic Messages streaming via fetch().

This prints events and assembles the final message in-memory.
*/

type SSEEvent = { event: string; data: unknown };

function parseSSEFrames(buffer: string): { events: SSEEvent[]; rest: string } {
	const events: SSEEvent[] = [];
	let rest = buffer;

	while (true) {
		const sep = rest.indexOf("\n\n");
		if (sep === -1) break;
		const frame = rest.slice(0, sep);
		rest = rest.slice(sep + 2);

		let eventName = "message";
		let dataStr = "";
		for (const line of frame.split("\n")) {
			if (line.startsWith("event:")) eventName = line.slice("event:".length).trim();
			if (line.startsWith("data:")) dataStr += line.slice("data:".length).trim();
		}
		if (!dataStr) continue;
		try {
			events.push({ event: eventName, data: JSON.parse(dataStr) });
		} catch {
			events.push({ event: eventName, data: dataStr });
		}
	}

	return { events, rest };
}

async function main() {
	const apiKey = process.env.ANTHROPIC_API_KEY;
	if (!apiKey) throw new Error("Set ANTHROPIC_API_KEY");

	const res = await fetch("https://api.anthropic.com/v1/messages", {
		method: "POST",
		headers: {
			"content-type": "application/json",
			"x-api-key": apiKey,
			"anthropic-version": "2023-06-01",
		},
		body: JSON.stringify({
			model: "claude-sonnet-4-5",
			max_tokens: 512,
			stream: true,
			messages: [{ role: "user", content: "Say hi." }],
		}),
	});

	if (!res.ok || !res.body) throw new Error(`HTTP ${res.status}: ${await res.text()}`);

	const reader = res.body.getReader();
	const decoder = new TextDecoder();
	let buf = "";

	while (true) {
		const { value, done } = await reader.read();
		if (done) break;
		buf += decoder.decode(value, { stream: true });

		const { events, rest } = parseSSEFrames(buf);
		buf = rest;

		for (const e of events) {
			console.log("event:", e.event, "data:", e.data);
		}
	}
}

main().catch((err) => {
	console.error(err);
	process.exit(1);
});
