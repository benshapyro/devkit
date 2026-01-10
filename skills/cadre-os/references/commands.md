# Commands Reference

Slash commands provide explicit control. Use natural language OR commands — both work.

## Discovery & Analysis

| Command | Action | Arguments |
|---------|--------|-----------|
| `/prep` | Discovery session prep | `[client]` `[attendee]` `[duration]` |
| `/debrief` | Process session transcript | `[client]` `[mode:quick\|full\|lite]` |
| `/context` | Pull client data | `[client]` `[dimension]` |
| `/gaps` | Coverage gap analysis | `[client]` |
| `/patterns` | Cross-session pattern analysis | `[client]` |
| `/priorities` | Rank challenges and solutions | `[client]` |
| `/lite` | Get or populate lite Excel template | `[client]` `[action:template\|populate\|migrate]` |

## Tech Stack Inventory

| Command | Action | Arguments |
|---------|--------|-----------|
| `/techstack survey` | Output Google Form questions | `[client]` |
| `/techstack template` | Provide blank Excel template | — |
| `/techstack parse` | Parse survey responses into grid | (paste text or upload file) |
| `/techstack research` | Research API/integrations for tools | `[client]` `[verbose]` |
| `/techstack migrate` | Promote to Discovery Catalog | `[client]` |

## Artifacts

| Command | Action | Arguments |
|---------|--------|-----------|
| `/artifact overview` | Generate Tech Stack Overview (HTML) | `[client]` |
| `/artifact map` | Generate Integration Map (JSX; say "convert to HTML" for Portal) | `[client]` |
| `/artifact findings` | Generate Findings Summary (HTML) | `[client]` |

## Solutions (AI Builds)

| Command | Action | Arguments |
|---------|--------|-----------|
| `/solutions discover` | Scan docs + Catalog for assistant and prompt opportunities | `[client]` |
| `/solutions catalog` | Generate client-facing Solution Catalog HTML | `[client]` |
| `/solutions brief` | Generate solution brief for AI opportunity | `[use case]` |
| `/solutions assistants library` | Browse 50 proven assistant patterns | — |
| `/solutions assistants prioritize` | Score, rank, and classify opportunities | `[client]` |
| `/solutions assistants validate` | Check feasibility blockers | `[use case]` |
| `/solutions assistants estimate` | Calculate build time and cost | `[use case]` |
| `/solutions assistants spec` | Generate implementation spec | `[use case]` `[light\|full\|formal]` |
| `/solutions prompts patterns` | Browse 45+ prompt patterns by category | `[category]` |
| `/solutions prompts audit` | Review and improve an existing prompt | (paste prompt) |
| `/solutions prompts template` | Generate production system prompt | `[type]` |
| `/solutions prompts optimize` | Model-specific optimization guidance | `[model]` |

## Deliverables

| Command | Action | Arguments |
|---------|--------|-----------|
| `/deck` | Generate strategy deck | `[client]` |
| `/summary` | Executive summary | `[client]` |
| `/report` | Detailed findings report | `[client]` |
| `/roadmap` | Implementation roadmap | `[client]` |
| `/brief` | Solution/product brief | `[solution name]` |

## Communications

| Command | Action | Arguments |
|---------|--------|-----------|
| `/email` | Weekly client email | `[client]` |
| `/agenda` | Meeting agenda | `[client]` `[meeting-type]` |
| `/mbr` | Monthly business review | `[client]` |
| `/3p` | Internal 3P update | `[client]` |
| `/newsletter` | Internal newsletter | — |

## SOPs (Standard Operating Procedures)

| Command | Action |
|---------|--------|
| `/sop discovery` | Show Discovery Catalog SOP |
| `/sop techstack` | Show Tech Stack Survey SOP |
| `/sop solutions` | Show Solutions SOP |

## Meta

| Command | Action |
|---------|--------|
| `/help` | List available commands |
| `/brand` | Show brand quick reference |

## Usage Examples

```
/prep Acme Corp Sarah Chen 60min
/debrief Acme Corp full
/lite template
/lite populate Acme Corp
/techstack survey Acme Corp
/techstack research Acme Corp verbose
/artifact overview Acme Corp
/artifact map Acme Corp
/artifact findings Acme Corp
/solutions discover Acme Corp
/solutions catalog Acme Corp
/solutions assistants library
/solutions assistants prioritize Acme Corp
/solutions assistants spec Policy Lookup full
/solutions prompts patterns content-creation
/solutions prompts audit
/solutions prompts template customer-support
/deck Acme Corp
/email Acme Corp
/sop discovery
/sop techstack
/sop solutions
```

**Arguments are optional.** If omitted, Claude will ask for needed info.
