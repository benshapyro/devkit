---
name: cadre-os
description: "Cadre AI consulting operating system for strategy engagements. Use when working with Cadre clients for: (1) Discovery - session prep, debriefs, transcripts, (2) Context - client data, stakeholders, (3) Synthesis - patterns, gaps, priorities, (4) Deliverables - decks, summaries, reports, roadmaps, (5) Communications - emails, agendas, MBRs, (6) Tech Stack - surveys, research, integrations, (7) Lite Mode - Excel-based capture, (8) Solutions - AI assistants, prompts, discovery, scoping, specs, client catalog, (9) Brand - on-brand artifacts. Triggers on /prep, /debrief, /deck, /techstack, /lite, /solutions, or Cadre client names."
---

# Cadre OS

Cadre AI's consulting operating system. Single entry point for discovery, context, synthesis, deliverables, communications, and branded outputs.

**Lite Mode** = Excel-based data capture when Airtable is unavailable. Use `discovery-catalog-lite-template.xlsx` instead of Airtable Discovery Catalog.

---

## Commands & Routing

Slash commands and natural language triggers both route to the same references.

### Discovery & Analysis

| Command / Trigger | Action | Reference |
|-------------------|--------|-----------|
| `/prep` or "prep me for" | Session prep | prep.md |
| `/debrief` or transcript pasted | Process session | debrief.md |
| `/debrief lite` or Excel file | Lite mode debrief | debrief.md + data-schema.md |
| `/lite template` | Get Excel template | debrief.md |
| `/lite populate [client]` | Fill template | debrief.md + data-schema.md |
| `/context [client]` or "what do we know" | Pull client data | data-schema.md |
| `/gaps` or "coverage", "what's missing" | Coverage gap analysis | synthesis.md |
| `/patterns` or "themes" | Cross-session patterns | synthesis.md |
| `/priorities` or "rank" | Challenge/solution ranking | synthesis.md |
| "what questions should I ask" | Question selection | questions.md |

### Tech Stack

| Command / Trigger | Action | Reference |
|-------------------|--------|-----------|
| `/techstack survey` | Output Google Form questions | tech-stack.md |
| `/techstack template` | Provide blank Excel template | tech-stack.md |
| `/techstack parse` | Parse survey responses | tech-stack.md |
| `/techstack research [verbose]` | Research APIs/integrations | tech-stack.md |
| `/techstack migrate` | Promote to Discovery Catalog | tech-stack.md + data-schema.md |

### Artifacts

| Command / Trigger | Action | Reference |
|-------------------|--------|-----------|
| `/artifact overview` | Tech Stack Overview (HTML) | synthesis.md + tech-stack.md |
| `/artifact map` | Integration Map (JSX) | synthesis.md + tech-stack.md |
| `/artifact findings` | Findings Summary (HTML) | synthesis.md + debrief.md |

### Solutions (AI Builds)

| Command / Trigger | Action | Reference |
|-------------------|--------|-----------|
| `/solutions discover` | Scan for assistant/prompt opportunities | assistants.md |
| `/solutions catalog` | Generate client-facing catalog HTML | assistants.md + brand.md |
| `/solutions brief [use case]` | Generate solution brief | deliverables.md + brand.md |
| `/solutions assistants library` | Browse 50 proven patterns | assistants.md + assistants-library.json |
| `/solutions assistants prioritize` | Score, rank, classify | assistants.md |
| `/solutions assistants validate` | Check feasibility blockers | assistants.md |
| `/solutions assistants estimate` | Calculate build time/cost | assistants.md + assistants-scoping.json |
| `/solutions assistants spec [light|full]` | Generate implementation spec | assistants.md |
| `/solutions prompts patterns [category]` | Browse 45+ prompt patterns | prompts.md |
| `/solutions prompts audit` | Review/improve a prompt | prompts.md |
| `/solutions prompts template [type]` | Generate system prompt | prompts.md |
| `/solutions prompts optimize [model]` | Model-specific guidance | prompts.md |
| `/solutions prompts agentic` | Agent patterns, multi-agent | prompts.md |

### Deliverables

| Command / Trigger | Action | Reference |
|-------------------|--------|-----------|
| `/deck` or "strategy presentation" | Strategy deck | deliverables.md + brand.md |
| `/summary` or "executive summary" | One-pager for leadership | deliverables.md + brand.md |
| `/report` or "findings report" | Detailed findings document | deliverables.md + brand.md |
| `/roadmap` or "implementation plan" | Implementation roadmap | deliverables.md + brand.md |
| `/brief` or "solution brief" | Solution/product brief | deliverables.md + brand.md |

### Communications

| Command / Trigger | Action | Reference |
|-------------------|--------|-----------|
| `/email` or "weekly email" | Client weekly update | comms.md + brand.md |
| `/agenda` or "meeting agenda" | Meeting agenda | comms.md |
| `/mbr` or "monthly review" | Monthly business review | comms.md + brand.md |
| `/3p` or "progress update" | Internal 3P update | comms.md |
| `/newsletter` | Internal newsletter | comms.md |

### SOPs & Meta

| Command / Trigger | Action | Reference |
|-------------------|--------|-----------|
| `/sop discovery` | Show Discovery Catalog process | assets/sops/discovery-catalog-sop.md |
| `/sop techstack` | Show Tech Stack Survey process | assets/sops/tech-stack-survey-sop.md |
| `/sop solutions` | Show Solutions process | assets/sops/solutions-sop.md |
| `/help` | List available commands | (this file) |
| `/brand` | Show brand quick reference | brand.md |

**Arguments are optional.** If omitted, Claude will ask for needed info.

---

## Workflows

### Discovery Session

**Before call:** Load prep reference → Query Catalog + Brain for context → Identify attendee archetype → Select gap-targeted questions → Generate brief

**After call:** Load debrief reference → Extract entities by dimension → Score challenges/solutions → Write to Catalog → Update Brain

### Synthesis

**Pattern analysis:** Query all Catalog tables for client → Group by dimension → Identify cross-cutting themes → Score pattern strength by evidence count

**Gap analysis:** Load coverage checklist from playbook → Map existing findings → Identify uncovered areas → Recommend targeted sessions

**Prioritization:** Use stored Priority Score (challenges) and DVF Score (solutions) — do NOT recalculate

### Deliverables

**Always apply:**
1. Run synthesis first (patterns, priorities)
2. Pull client context from Catalog/Brain
3. Apply Cadre brand (load brand.md)
4. Use appropriate system skill (pptx, docx)

**Selection guide:**
| Audience | Time | Deliverable |
|----------|------|-------------|
| Executive sponsor | 5 min | Executive Summary |
| Leadership team | 30-60 min | Strategy Deck |
| Project team | Reference doc | Findings Report |
| Implementation team | Planning | Roadmap |

### Communications

**Client comms:** Always check recent context (Catalog, Slack, Email) before drafting.

| Type | Cadence | Section |
|------|---------|---------|
| Weekly Email | Weekly | comms.md#weekly-email |
| Meeting Agenda | Per meeting | comms.md#meeting-agendas |
| Monthly Review | Monthly | comms.md#monthly-business-review |

**Internal comms:** Use 3P format for progress updates.

| Type | Cadence | Section |
|------|---------|---------|
| 3P Update | Weekly | comms.md#internal-communications |
| Newsletter | Monthly | comms.md#internal-communications |

---

## Data Write Rules

Before creating ANY Catalog records:

1. **Load schema first** — Read `data-schema.md`
2. **Get client record ID** — Query 0_Clients, capture record ID
3. **Check existing records** — Query relevant tables for UPDATE vs CREATE
4. **Validate before writing:**
   - All field names match schema exactly
   - All select options are valid (API rejects invalid values)
   - All link fields are arrays: `["recXXX"]`

**Record creation order** (dependencies must exist first):
```
1. Session (1_Discovery_Log) → get session ID
2. People (2_People)
3. Processes (3_Process)
4. Technology (4_Technology)
5. Challenges (5_Challenges)
6. Solutions (6_Solutions)
7. Quotes (7_Quotes) → links to all above
8. Update Session with links to created records
```

**If schema read fails:** DO NOT create records. Output JSON for manual entry instead.

---

## Permission Gates

| Source | Permission |
|--------|------------|
| Catalog, Brain, Project files | Just do it (internal) |
| Slack, Gmail, Web, LinkedIn | Ask once per session, bundled |

**Bundle external sources:**
> "Should I also search Slack/Gmail and do web research? This helps with new contacts and recent context."

---

## Graceful Degradation

| Situation | Response |
|-----------|----------|
| No Brain exists | Use Catalog only, note limited narrative context |
| No Catalog records | First session — use generic framework |
| No attendees specified | Ask, or generate general prep |
| Sparse notes | Extract what's available, note low confidence |
| Unknown client | Ask for clarification, list known clients |
| Schema read fails | DO NOT create records; output JSON |
| Synthesis returns sparse results | Note limited evidence, run gap analysis |
| Brand assets unavailable | Use brand reference file |
| Lite template structure mismatch | Ask for standard template or create fresh |
| Department name mismatch (Lite) | Flag and ask for correction |
| Solution referenced but missing (Lite) | Create placeholder, flag for user |
| Lite migration fails | Output JSON for manual Airtable entry |

---

## Asset Templates

Pre-built HTML/JSX templates for common artifacts. See [assets/README.md](assets/README.md) for full inventory.

### Artifact Kit
| File | Use For |
|------|---------|
| [cadre-components.html](assets/artifact-kit/cadre-components.html) | Reusable HTML components with Cadre styling |
| [cadre-components.jsx](assets/artifact-kit/cadre-components.jsx) | Reusable React components with Cadre styling |

### Ready-to-Use Templates
| File | Use For |
|------|---------|
| [client-kickoff.html](assets/artifact-templates/client-kickoff.html) | Client engagement kickoff presentation |
| [monthly-business-review.html](assets/artifact-templates/monthly-business-review.html) | MBR presentation template (HTML artifact) |
| [mbr-template-01-07-25.pptx](assets/templates/mbr-template-01-07-25.pptx) | MBR slide library (42 slides, 13 sections, 29 variations) |
| [roi-calculator.jsx](assets/artifact-templates/roi-calculator.jsx) | Interactive ROI calculator |
| [transformation-deck.html](assets/artifact-templates/transformation-deck.html) | AI transformation strategy deck |
| [discovery-catalog-lite-template.xlsx](assets/templates/discovery-catalog-lite-template.xlsx) | Lite mode Excel template |
| [tech-stack-survey-template.xlsx](assets/templates/tech-stack-survey-template.xlsx) | Tech stack inventory template |
| [tech-stack-overview.html](assets/artifact-templates/tech-stack-overview.html) | Tech stack summary from survey data |
| [integration-map.jsx](assets/artifact-templates/integration-map.jsx) | Visual tool connection map |
| [findings-summary.html](assets/artifact-templates/findings-summary.html) | Discovery findings from Lite data |

**To use:** Copy template, replace placeholder content with client data from synthesis.

---

## Reference Files

All reference files are in the `references/` directory.

| File | Purpose |
|------|---------|
| [prep.md](references/prep.md) | Session prep workflow, archetypes, follow-up patterns |
| [debrief.md](references/debrief.md) | Session debrief, Lite mode, insight markers, quality checks |
| [questions.md](references/questions.md) | Question library for discovery sessions |
| [synthesis.md](references/synthesis.md) | Pattern analysis, gap analysis, prioritization, artifact generation |
| [data-schema.md](references/data-schema.md) | Airtable Discovery Catalog + Lite Excel + Client Brain schemas |
| [tech-stack.md](references/tech-stack.md) | Tech stack survey, research, Tools Library |
| [deliverables.md](references/deliverables.md) | Strategy deck, executive summary, report, roadmap, solution brief |
| [comms.md](references/comms.md) | Weekly email, meeting agenda, MBR, 3P updates, newsletter |
| [assistants.md](references/assistants.md) | Assistant discovery, prioritization, estimation, specs |
| [prompts.md](references/prompts.md) | Prompt patterns (content, analysis, code, education), model optimization, agentic |
| [brand.md](references/brand.md) | Brand positioning, voice, messaging, UI components |

### Data Files

| File | Purpose |
|------|---------|
| [assistants-library.json](references/assistants-library.json) | 50 proven assistant patterns |
| [assistants-scoping.json](references/assistants-scoping.json) | Build time and cost calculations |

---

## SOPs (User-Facing)

| File | Present When |
|------|--------------|
| [discovery-catalog-sop.md](assets/sops/discovery-catalog-sop.md) | User asks about discovery process |
| [tech-stack-survey-sop.md](assets/sops/tech-stack-survey-sop.md) | User asks about tech stack process |
| [solutions-sop.md](assets/sops/solutions-sop.md) | User asks about solutions/builds process |

**SOP Behavior:**
- **Present SOP** when user asks about the process: "What's the process for debriefing?"
- **Follow SOP** when user requests action: "Debrief this transcript"
- **When unclear:** Default to following the SOP, mention: "I'm following the Discovery Catalog SOP — want me to show you the full process?"
