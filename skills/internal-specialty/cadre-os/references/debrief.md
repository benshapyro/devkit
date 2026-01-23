# Discovery Session Debrief

Complete reference for processing discovery sessions: debrief workflows, quality checklists, insight extraction, brain updates, and special scenarios.

## Table of Contents

- [Debrief Workflow](#debrief-workflow)
  - [Mode Selection](#mode-selection)
  - [Quick Mode](#quick-mode)
  - [Full Mode](#full-mode)
  - [Lite Mode](#lite-mode)
  - [Entity Extraction Reference](#entity-extraction-reference)
- [Quality Checklists](#quality-checklists)
  - [Pre-flight Check](#pre-flight-check)
  - [Prep Quality Checklist](#prep-quality-checklist)
  - [Debrief Quality Checklist](#debrief-quality-checklist)
  - [Record Creation Order](#record-creation-order)
- [Insight Extraction](#insight-extraction)
  - [Insight Markers](#insight-markers)
  - [Surprise Detection](#-surprise-detection)
  - [Pattern Detection](#-pattern-detection)
  - [Contradiction Detection](#️-contradiction-detection)
  - [Opportunity Detection](#-opportunity-detection)
- [Brain Update Generator](#brain-update-generator)
  - [Execution Flow](#execution-flow)
  - [Brain Section Mapping](#brain-section-mapping)
  - [Document Template](#document-template)
- [Special Scenarios](#special-scenarios)
  - [Multiple Attendees](#multiple-attendees)
  - [Follow-Up Sessions](#follow-up-sessions)
  - [Conflicting Information](#conflicting-information)
  - [Thin Sessions](#thin-sessions)

---

# Debrief Workflow

Process discovery session notes and transcripts into structured insights and Catalog records.

---

## Mode Selection

| Mode | Duration | Use When | Writes To |
|------|----------|----------|-----------|
| **Quick** | 3-5 min | Session < 10 min, < 2000 words, or "just the summary" | Display only |
| **Full** | 10-15 min | Standard discovery sessions, full transcripts, >20 min | Airtable Catalog |
| **Lite** | 5-10 min | Early engagement, no Airtable access, client handoff | Excel file |

**Default to Full for transcripts.** Use Quick for brief check-ins. Use Lite when Airtable isn't available or for portable deliverables.

### Mode Detection

**Auto-detect Lite Mode when:**
- User uploads Excel file matching template structure
- User references "lite", "excel", or "template"
- User says "quick capture" or "don't use Airtable"

**Auto-detect Full Mode when:**
- Client exists in Airtable Catalog
- No Excel file present
- User says "save to Catalog" or "full debrief"

**Explicit override:** User can always say "use lite mode" or "use full mode"

---

## Quick Mode

Fast capture for short sessions or sparse notes. Display only — no Catalog writes.

### Step 1: Capture Input

Accept:
- Pasted notes
- Brief verbal summary
- Short transcript

**Identify:**
- Client name
- Attendees (if mentioned)
- Session type (infer, then confirm)
- Date (default: today)

### Step 2: Extract Key Points

**TL;DR:** 3-4 sentence summary capturing:
- What was discussed
- Key decision or insight
- What's next

**Key Takeaways:** 3-5 bullets, each with:
- The insight
- Why it matters
- Confidence level (High/Medium/Low)

**Follow-Up Items:** Action items or open questions

### Step 3: Flag Insights

Apply markers to noteworthy items:

| Marker | Meaning | Look For |
|--------|---------|----------|
| ⚡ | Surprise | Contradicted our assumptions |
| 🔄 | Pattern | Theme we've heard before |
| ⚠️ | Contradiction | Conflicting info, needs clarification |
| 💡 | Opportunity | Client suggested a solution idea |

### Step 4: Extract Quotes (Display Only)

Scan for powerful quotes worth capturing:

**Selection criteria:**
- Captures problem vividly
- Shows emotional investment
- Would resonate in a presentation
- Quantifies impact
- Unprompted solution idea (💡)

**Skip:**
- Generic/vague statements
- Just agreeing or acknowledging
- Off-topic tangents

⚠️ **Quick Mode does NOT save quotes to Catalog.** Note in output:
> "To save these quotes and full entity extraction to the Discovery Catalog, run Full Debrief."

### Step 5: Generate Quick Output

```markdown
# Quick Debrief: [Client Name]
**Session:** [Type] | **Date:** [Date] | **Attendees:** [Names]

---

## TL;DR
[3-4 sentences: What happened, key insight, what's next]

---

## Key Takeaways

1. **[Insight]** — [Why it matters] *(Confidence: High)*
2. **[Insight]** — [Why it matters] *(Confidence: Medium)*
3. ⚡ **[Surprise]** — [What we assumed vs reality]
4. 💡 **[Opportunity]** — [Client-originated idea]

---

## Notable Quotes

> "[Quote 1]"
> — [Speaker], [Title]
> 📌 Pain Point: Process | Tone: Frustration

> "[Quote 2]"
> — [Speaker], [Title]
> 📌 Opportunity: Technology | Tone: Hope

*To save quotes to Catalog, run Full Debrief.*

---

## Follow-Up Items
- [ ] [Action or question]
- [ ] [Action or question]

---

## Quick Assessment

| Dimension | Coverage | Notes |
|-----------|----------|-------|
| People | ◐ | [Brief note] |
| Process | ○ | [Brief note] |
| Technology | ● | [Brief note] |
| Challenges | ◐ | [Brief note] |
| Solutions | ○ | [Brief note] |

*Legend: ● Strong | ◐ Partial | ○ Gap*

---

**Next:** Run Full Debrief to save to Catalog, or ask me to prioritize what we learned.
```

### When to Upgrade to Full Mode

Suggest Full Debrief if:
- User pasted substantial content (>2000 words)
- Multiple new entities identified
- High-value quotes worth preserving
- User wants Brain Update

**Prompt:**
> "This session has rich content — want me to run Full Debrief to extract entities and save to Catalog?"

---

## Full Mode

Complete entity extraction with Discovery Catalog writes and Brain Update generation.

### Step 0: Pre-flight Check (CRITICAL)

**0A: Load Schema**
```
Read: references/data-schema.md
```

**0B: Get Client Record**
```
Airtable: list_records
Base: apprH2AppvnKfUpT0
Table: tbl9MiW4wWEHoNw6t (0_Clients)
Filter: {Client Name} = "[Client]"
```

**0C: Build Entity Maps**
Query existing records to enable UPDATE vs CREATE:

```
2_People (tbl10xPpFKblRy3PL) → name→ID map
3_Process (tblAibn7iHAvGqP1P) → name→ID map
4_Technology (tblDdIuLzEQ2DwBYF) → name→ID map
5_Challenges (tblmGPfC8Y85laT6j) → name→ID map
6_Solutions (tblleK2rzvC5V7sR0) → name→ID map
7_Quotes (tbl6dIJFlKBqlqmp4) → existing quotes
```

⚠️ **DO NOT proceed if Pre-flight fails.** Output JSON for manual entry.

### Step 1: Gather Input & Confirm Metadata

Accept input:
- Full transcript (Fireflies or other)
- Detailed notes
- Verbal recap

**1A: Detect Session Type**

Analyze content for signals:

| Type | Signals |
|------|---------|
| Kickoff | First meeting, introductions, "getting started" |
| Interview | 1-3 attendees, Q&A pattern |
| Workshop | 4+ attendees, collaborative language |
| Document Review | References to docs, SOPs |
| Observation | Shadowing, "day in the life" |
| Follow-up | References to prior sessions |
| Presentation | One-way delivery, slides |
| System Demo | Product walkthrough, "let me show you" |
| Validation | Confirming findings, "does this match" |

**Confirm with user:**
> "This looks like an **Interview**. Correct?"

**1B: Detect Attendees**

Extract names from transcript or notes.

**Confirm with user:**
> "I see **Karl Winters** and **Sarah Chen**. Anyone else?"

**1C: Capture Metadata**
- Client name
- Session date (default: today)
- Duration (estimate from transcript length)
- Key topics (extract from content)

### Step 2: Extract Entities

Parse transcript across all dimensions. See [Entity Extraction Reference](#entity-extraction-reference) for field details.

**Mark each entity:** NEW or UPDATE (check entity map from Step 0)

### Step 3: Apply Insight Markers

Review extracted entities and flag:

| Marker | Apply When |
|--------|------------|
| ⚡ Surprise | Contradicted an assumption we held |
| 🔄 Pattern | Theme mentioned 3+ times across sessions |
| ⚠️ Contradiction | Conflicting statements needing clarification |
| 💡 Opportunity | Unprompted solution idea from client |

**💡 is high-value:** Client-originated ideas have built-in buy-in.

### Step 4: Generate Confirmation Summary

Before saving, show user a compact summary:

```markdown
## Ready to Save to Discovery Catalog

**Session:** CES Discovery Interview - Sarah & Mike
**Date:** 2025-01-15 | **Type:** Interview

---

### Extraction Summary

📍 **People:** 2 (1 new, 1 update)
- Sarah Chen — UPDATE (Sentiment: 7→8)
- Mike Rodriguez — NEW (IT Director, Power: 6)

📍 **Processes:** 1 new
- Quote-to-Cash workflow (Bottleneck: Yes)

📍 **Technology:** 2 (1 new, 1 update)
- Salesforce — UPDATE (Satisfaction: 5→4)
- Access Database — NEW (Status: Active)

📍 **Challenges:** 3 new
- Manual data entry errors (Priority: 100) ⚡
- Approval bottlenecks (Priority: 64)
- System integration gaps (Priority: 48)

📍 **Solutions:** 1 new
- Quote validation automation (DVF: 80) 💡

📍 **Quotes:** 4 new
- 2 Pain Points, 1 Opportunity, 1 Insight

---

**Save to Catalog?** [Creates 13 records]

Or say "show details" to review before saving.
```

**User responses:**
- "Yes" / "Save" → Create records
- "Show details" / "Review" → Show full extraction, accept revisions
- "Skip" / "Hold" → Output JSON, continue to Brain Update

### Step 5: Create Records (In Order)

**Order matters — dependencies must exist first.**

```
1. Session (1_Discovery_Log) — get session ID
2. People (2_People) — link to session
3. Processes (3_Process) — link to session, people
4. Technology (4_Technology) — link to session, processes
5. Challenges (5_Challenges) — link to session, people, processes, tech
6. Solutions (6_Solutions) — link to session, challenges
7. Quotes (7_Quotes) — link to session, speaker, related entities
8. Update Session — add links to all created records
```

**Change History Format:**

NEW records:
```
[YYYY-MM-DD | Session: Title] Created. [key]: [value], [key]: [value]
```

UPDATE records:
```
[YYYY-MM-DD | Session: Title] [field]: [old] → [new]
```

### Step 6: Generate Full Output

```markdown
# Debrief: [Client Name]
**Session:** [Type] | **Date:** [Date] | **Attendees:** [Names]

---

## TL;DR
[3-4 sentences: What happened, key insight, what's next]

---

## Key Takeaways

1. ⚡ **[Surprise finding]** — [Why it matters]
2. 🔄 **[Pattern confirmed]** — [Context]
3. 💡 **[Client-originated idea]** — [Their words, high buy-in potential]
4. **[Key insight]** — [Confidence: High/Medium/Low]
5. ⚠️ **[Contradiction]** — [Needs clarification]

---

## Powerful Quotes

> "[Quote 1 - captures problem vividly]"
> — [Speaker], [Title]
> 📍 Type: Pain Point | Dimension: Process | Tone: Frustration | Power: 5
> 📍 Linked to: [Challenge name]

> "[Quote 2 - client-originated idea]"
> — [Speaker], [Title]
> 📍 Type: Opportunity | Dimension: Technology | Tone: Hope | Power: 4
> 📍 Linked to: [Solution name]

💡 **Client-Originated Idea:**
> "[Exact quote of their solution idea]"
> — [Speaker], during [context]
> 📍 This is gold for buy-in — the client suggested it themselves

---

## Extracted Entities

### People (X new, Y updated)

**[Name]** — [Title] | Power: X | Sentiment: X | [Type]
- Key insight: [What we learned]
- Status: [NEW/UPDATE]

### Processes (X new)

**[Process Name]** — [Department] | [Frequency] | [Hours/instance]
- AI Readiness: X/5 | Bottleneck: [Yes/No]
- Status: [NEW/UPDATE]

### Technology (X new, Y updated)

**[Tool Name]** — [Vendor] | Status: [Active/etc] | Satisfaction: X/10
- JTBD: [What job it does]
- Status: [NEW/UPDATE]

### Challenges (X new)

**[Challenge Name]** — Priority: [Score] ([Impact]×[Urgency]×[Readiness])
- [Clear explanation]
- Evidence: "[Quote]"
- Status: [NEW/UPDATE]

### Solutions (X new)

**[Solution Name]** — DVF: [Score] | Horizon: [Now/Next/Later]
- [Technical approach]
- Addresses: [Linked challenges]
- Status: [NEW/UPDATE]

---

## Follow-Up Items
- [ ] [Action or question]
- [ ] [Action or question]
- [ ] ⚠️ [Item to clarify]

---

## Catalog Status
✅ [X] records created in Discovery Catalog
📍 Session ID: [recXXX]

---

**Next:** Should I generate a Brain Update document?
```

### Step 7: Offer Brain Update

After debrief output:

> "Should I generate a **Brain Update** document? This compares findings to the current Brain and creates a copy/paste-ready Word doc."

**If yes:** See [Brain Update Generator](#brain-update-generator) section.

### Step 8: Offer Comms

After Brain Update (or if declined):

> "Want me to draft the **follow-up email**? **Internal Slack summary**?"

**If follow-up email:** Generate client-facing email summarizing:
- Thank you for the session
- Key topics discussed (high-level, no internal observations)
- Next steps and timeline
- Any action items for client

**If Slack summary:** Generate internal TL;DR for team channel:
- 2-3 sentence summary
- Key insights (with ⚡🔄💡 markers if applicable)
- Follow-up items
- Next session date if known

---

## Lite Mode

Lightweight Excel-based discovery capture for early-stage engagements, rapid assessments, or client handoffs.

> **Schema:** See [data-schema.md](data-schema.md) for Excel field definitions and Airtable mapping.
>
> **Full SOP:** See `assets/sops/discovery-catalog-sop.md` for complete step-by-step instructions.

### When to Use Lite Mode

| Scenario | Use Lite Mode |
|----------|---------------|
| First 1-2 discovery sessions | ✓ Quick capture, migrate later |
| Rapid assessment / workshop | ✓ Same-day deliverable |
| Client wants raw data | ✓ Handoff artifact |
| Full engagement (3+ sessions) | ✗ Use Full Mode (Airtable) |
| Need scoring (Priority/DVF) | ✗ Use Full Mode (Airtable) |
| Cross-client pattern analysis | ✗ Use Full Mode (Airtable) |

---

### Lite Mode Workflows

#### Provide Blank Template

**Triggers:** "give me the discovery template", "I need the excel catalog", "start a new lite capture"

**Action:**
1. Copy template from `assets/templates/discovery-catalog-lite-template.xlsx`
2. Present to user
3. Offer: "Want me to populate this from a transcript, web research, or information you provide?"

---

#### Populate from Transcript

**Triggers:** User provides transcript + Excel template, "fill in the template", "debrief [client] lite mode"

**Process:**
1. Extract entities using standard extraction (see [Entity Extraction Reference](#entity-extraction-reference))
2. Map to Lite schema (see [data-schema.md](data-schema.md))
3. Write to Excel using openpyxl
4. Present updated file with summary

**Field Mapping:**

| Extracted Entity | Lite Location |
|------------------|---------------|
| Department/Team mentioned | Departments sheet |
| Challenges | Issues sheet |
| Solutions/Opportunities | Solutions sheet |
| Quotes | Issues → Pain Point Quote |
| Root causes | Issues → Pain Point Cause |
| Supporting data | Issues → Finding 1, 2, 3... |
| Technology mentioned | Solutions → Tech columns |

---

#### Populate from Research

**Triggers:** "research [company] and fill in the template", "populate from what we know"

**Process:**
1. Search connected sources (Drive, Slack, web) for client info
2. Extract issues and solutions from findings
3. Map to Lite schema
4. Write to Excel
5. Present with confidence notes

---

#### Migrate to Full Catalog

**Triggers:** "migrate this to Airtable", "convert to full catalog", "promote to catalog"

**Process:**
1. Read Excel file
2. Map fields to Airtable schema (see [data-schema.md](data-schema.md) mapping table)
3. Create records in dependency order: Client → Session → People → Challenges → Solutions
4. Report created record counts
5. Offer to archive Excel

**Notes:**
- Impact Category → Challenge Type
- Pain Point Cause → Root Cause field
- Findings → Notes field (concatenated)
- No scoring in Lite → Set scores to 0, flag for manual review

---

### Lite Mode Output

When presenting filled Excel:

```markdown
Here's your populated Discovery Catalog Lite:

**Summary:**
- Departments: 3 (Sales, Marketing, Product)
- Issues: 12 identified
- Solutions: 8 proposed

**Confidence notes:**
- High confidence: Issues from direct transcript quotes
- Medium: Solutions inferred from problem descriptions
- Low: Tech stack (needs validation)

[Download: discovery-catalog-acme-2024-12.xlsx]

Want me to migrate this to the full Airtable Catalog?
```

---

### Lite Mode Operational Details

**File Location & Naming:**

```
Cadre Team Drive /
└── Clients /
    └── [Client Name] /
        ├── Discovery Catalog.xlsx        ← The catalog
        ├── Transcripts /
        │   └── [YYYY-MM-DD] [Type] - [Attendees].txt
        └── Discovery /
            └── Debriefs /
                └── [YYYY-MM-DD] Debrief - [Attendees].md
```

**When to Create:** SOW is signed OR first discovery call is scheduled (whichever comes first). Have the empty catalog ready before meetings.

**Claude Project Setup:**
1. Create a Claude Project for the client
2. Upload `Discovery Catalog.xlsx` to Project Knowledge
3. After each update, re-upload the latest version

---

### Lite Mode Post-Call Workflow

1. **Download Transcript** — Get from Fireflies, save to `Transcripts/`
2. **Create Claude Chat** — Name: `[YYYY-MM-DD] Debrief - [Attendee(s)]`
3. **Run Debrief** — Upload transcript, type: `/debrief [Client Name] lite`
4. **Review & Revise** — Human reviews, fixes errors, iterates until accurate
5. **Save Debrief Summary** — Download artifact as `.md`, save to `Debriefs/`
6. **Update Catalog** — Add entries to Excel, re-upload to Claude Project
7. **Peer Review** — If client-facing, get quick teammate review (2-5 min)

---

### Lite Mode Validation

Run these checks before writing to Excel:

1. Check departments exist for all issues/solutions
2. Check solution references in issues match Solutions sheet
3. Check required fields (name, description)
4. Check impact category values match valid options

**Valid Impact Categories:**
`New Revenue` | `Time Efficiency` | `Revenue Loss` | `Customer Experience` | `Competitive Position` | `Brand Awareness` | `Lead Quality` | `Brand Consistency` | `Product Quality` | `Strategic Decisions` | `Cost Reduction` | `Risk Mitigation` | `Employee Experience` | `Compliance`

**If errors exist:** Stop and ask user to clarify
**If only warnings:** Proceed but note warnings in output

---

### Generate Artifacts from Lite Data

After populating the Lite template, offer to generate branded artifacts.

**Triggers:** "create findings summary", "visualize the findings", "generate artifact"

| Artifact | What It Shows |
|----------|---------------|
| Findings Summary | Issues + solutions side by side, quick wins, next steps |

See [synthesis.md](synthesis.md) for detailed generation steps.

---

## Entity Extraction Reference

### People

| Field | Extract |
|-------|---------|
| Full Name | Direct mention |
| Title | Stated or inferred |
| Department | Context clues |
| Power (1-10) | Role level + influence signals |
| Sentiment (1-10) | Tone, engagement |
| Stakeholder Type | Champion, Decision-Maker, Influencer, User, Affected, Neutral, Blocker |
| Key Insights | What they said/believe |
| Concerns | Worries expressed |
| ADKAR Stage | Awareness, Desire, Knowledge, Ability, Reinforcement |

### Processes

| Field | Extract |
|-------|---------|
| Process Name | What they call it |
| Department | Who owns it |
| Process Owner | Person accountable |
| Frequency/Month | How often |
| Hours per Instance | Time to complete |
| AI/Automation Readiness (1-5) | Rule-based? Repetitive? |
| Bottleneck? | Did they call it out? |
| Context Type | Formal, Informal, Tribal |

### Technology

| Field | Extract |
|-------|---------|
| Tool Name | What they call it |
| Vendor | If mentioned |
| Status | Active, Planned, Evaluating, Sunsetting, Inactive |
| Primary JTBD | What job it does |
| Department | Who uses it |
| Satisfaction (1-10) | How they talk about it |

### Challenges

| Field | Extract |
|-------|---------|
| Challenge Name | Short descriptive name |
| Clear Explanation | Full context |
| Problem Type | Efficiency, Quality, Speed, Cost, Compliance, Communication, Data, Other |
| Category | Strategic, Operational, Technical, Cultural |
| Impact (1-5) | Business impact |
| Urgency (1-5) | Time sensitivity |
| Readiness (1-5) | Willingness to address |
| Priority Score | Impact × Urgency × Readiness (max 125) |
| Evidence/Quotes | Direct quote |
| Status | Identified, Validated, In Discovery, Addressed, Resolved |

### Solutions

| Field | Extract |
|-------|---------|
| Solution Name | Descriptive name |
| Solution Type | AI Automation, Process Redesign, System Integration, Training, Custom Build, Off-the-Shelf, Hybrid |
| Technical Approach | How it works |
| Horizon | Now (0-3 mo), Next (3-6 mo), Later (6-12 mo), Future (12+ mo) |
| Desirability (1-5) | Do they want it? |
| Viability (1-5) | Does it make business sense? |
| Feasibility (1-5) | Can it be built? |
| DVF Score | D × V × F (max 125) |
| Status | Proposed, Validated, In Development, Delivered, Rejected |

---

## Quote Selection

### Selection Criteria

- ✅ Captures problem vividly with emotion
- ✅ Reveals unexpected insight
- ✅ Shows emotional investment
- ✅ Would resonate in client presentation
- ✅ Quantifies impact with specific numbers
- ✅ 💡 Unprompted solution idea from client

### Skip

- ❌ Generic or vague
- ❌ Just agreeing/acknowledging
- ❌ Off-topic tangents

### Quote Fields

| Field | Extract |
|-------|---------|
| Quote Text | Clean up filler words (um, uh, like) |
| Speaker Name | Who said it |
| Speaker Title | Their role |
| Session Context | What was being discussed |
| Quote Type | Pain Point, Insight, Opportunity, Vision, Objection, Endorsement, Question |
| Dimension | People, Process, Technology, Challenges, Solutions, General |
| Emotional Tone | Frustration, Excitement, Concern, Neutral, Hope, Pride |
| Power Rating (1-5) | Presentation-worthiness |

---

## Error Recovery

| Error | Cause | Fix |
|-------|-------|-----|
| Schema read fails | Connection issue | Output JSON for manual entry |
| Field name rejected | Typo | Check exact spelling in schema |
| Invalid select option | Wrong value | Check valid options in schema |
| Record creation fails | Link issue | Output remaining JSON, continue |

**Never block entire flow on technical glitch.**

---

## Confidence Calibration

| Level | When to Use | Example |
|-------|-------------|---------|
| High | Direct quote, explicit | "She said 'this takes 4 hours'" |
| Medium | Clear implication | He complained repeatedly |
| Low | Reading between lines | Based on role, probably high power |

**Flag low confidence:**
> ⚠️ Low confidence — validate in next session

---

## Graceful Degradation

| Input Quality | Response |
|---------------|----------|
| **Good notes** | Full extraction as described |
| **Sparse notes** | Extract what's there, note gaps |
| **Just attendees** | Record who met, prompt for details |
| **No client identified** | Ask which client |

---

# Quality Checklists

Pre-delivery quality checks for prep and debrief outputs.

---

## Pre-flight Check

Run before any synthesis, deliverable, or analysis task. This check ensures data is ready and accessible.

| # | Check | If Failed |
|---|-------|-----------|
| 1 | **Client exists** — Record found in 0_Clients table | Stop, create client record first |
| 2 | **Data is current** — Last session within 30 days OR user confirms data is current | Warn user, ask if data is still valid |
| 3 | **Schema loaded** — Read data-schema.md before any writes | Stop, load schema before proceeding |
| 4 | **Permissions confirmed** — External tools asked once per session | Ask permission before accessing Gmail, Drive, Slack, web |

**When to run:**
- Before `/prep`, `/debrief`, `/gaps`, `/patterns`, `/priorities`
- Before `/deck`, `/report`, `/roadmap`, `/brief`
- Before `/solutions discover`, `/solutions catalog`
- Before any operation that reads from or writes to the Discovery Catalog

**If any check fails:** Inform user and ask how to proceed. Do not continue silently.

---

## Prep Quality Checklist

### Quick Prep (2-5 min)

Before delivering briefing, verify:

| # | Check | Required |
|---|-------|----------|
| 1 | Mode explained to user | ✓ |
| 2 | Attendee names and titles included | ✓ |
| 3 | Session type confirmed | ✓ |
| 4 | Key context from Brain/Catalog present | ✓ |
| 5 | Questions target known gaps | ✓ |
| 6 | Questions scaled to duration | ✓ |
| 7 | Questions in plain English | ✓ |
| 8 | Handoff prompt included | ✓ |

**Quick Prep Minimum:**
- [ ] 3+ questions included
- [ ] At least 1 attendee profiled
- [ ] Session goal clear

---

### Deep Prep (10-15 min)

Before delivering briefing, verify:

| # | Check | Required |
|---|-------|----------|
| 1 | Mode explained to user | ✓ |
| 2 | All attendees profiled (name, title, background) | ✓ |
| 3 | Research phases completed or stopped appropriately | ✓ |
| 4 | Permissions requested before external research | ✓ |
| 5 | Time limits respected (≤10 min research) | ✓ |
| 6 | Questions target dimension gaps | ✓ |
| 7 | Questions match attendee roles | ✓ |
| 8 | Question count matches duration | ✓ |
| 9 | Conditional follow-ups included | ✓ |
| 10 | Proper sequencing (Landscape → Problems → Process → Specifics) | ✓ |
| 11 | Landmines/sensitive topics flagged | ✓ |
| 12 | Rapport topics identified | ✓ |
| 13 | Handoff prompt included | ✓ |

**Deep Prep Minimum:**
- [ ] All attendees have profile
- [ ] 8+ questions with follow-ups
- [ ] Gap analysis documented
- [ ] Research documented (even if minimal)

---

## Debrief Quality Checklist

### Quick Debrief (3-5 min)

Before delivering summary, verify:

| # | Check | Required |
|---|-------|----------|
| 1 | Mode explained to user | ✓ |
| 2 | TL;DR is ≤3 sentences | ✓ |
| 3 | Key takeaways have confidence levels | ✓ |
| 4 | Notable quotes captured (if any) | ✓ |
| 5 | Insight markers applied (⚡🔄⚠️💡) | ✓ |
| 6 | Quick assessment table included | ✓ |
| 7 | Full Debrief suggestion offered (if substantial content) | ✓ |
| 8 | Handoff prompt included | ✓ |

**Quick Debrief Confirms:**
- [ ] NO records created (display only)
- [ ] User knows records not saved

---

### Full Debrief (10-15 min)

Before saving to Catalog, verify:

| # | Check | Required |
|---|-------|----------|
| 1 | Pre-flight check passed (8 tables loaded) | ✓ |
| 2 | Client ID confirmed | ✓ |
| 3 | Session type confirmed with user | ✓ |
| 4 | Attendees confirmed with user | ✓ |
| 5 | All 5 dimensions extracted | ✓ |
| 6 | Quotes extracted (3-5 minimum for 60min) | ✓ |
| 7 | Insight markers applied | ✓ |
| 8 | Confirmation summary shown | ✓ |
| 9 | User confirmed (or revised) | ✓ |
| 10 | Records created in order | ✓ |
| 11 | Brain Update offered | ✓ |
| 12 | Handoff prompt included | ✓ |

---

## Pre-Save Checklist

### Before Creating Any Catalog Records

| # | Check | If Failed |
|---|-------|-----------|
| 1 | All 8 table schemas loaded | Stop, reload |
| 2 | Client record exists | Stop, create client first |
| 3 | Entity maps built (existing records) | May create duplicates |
| 4 | Session record exists or will be created first | Link will fail |
| 5 | Required fields populated | Save will fail |
| 6 | Select field values match schema exactly | Save will fail |
| 7 | Link fields use record IDs (not names) | Link will fail |

### Field Validation

| Field Type | Validation |
|------------|------------|
| singleSelect | Value must match schema options exactly |
| multipleRecordLinks | Must be array of record IDs |
| number | Must be numeric (no strings) |
| checkbox | Must be boolean |
| date | Must be ISO format (YYYY-MM-DD) |

---

## Record Creation Order

Always create records in this sequence:

```
1. Session (1_Discovery_Log) — get session ID
2. People (2_People) — link to Session
3. Processes (3_Process) — link to Session, People
4. Technology (4_Technology) — link to Session
5. Challenges (5_Challenges) — link to Session, People, Process, Tech
6. Solutions (6_Solutions) — link to Session, Challenges
7. Quotes (7_Quotes) — link to all above
8. Update Session — add links to all created records
```

**Why This Order:**
- Session must exist before anything links to it
- People often linked from other records
- Challenges often link to Process/Tech
- Solutions often link to Challenges
- Quotes link to everything

---

## Output Quality Checks

### Briefing Output (Prep)

| Section | Check |
|---------|-------|
| Quick Context | ≤3 sentences |
| Attendee Profiles | Name, title, background, rapport topic |
| Key Questions | Numbered, scaled to duration |
| Follow-ups | Nested under relevant questions |
| Landmines | Sensitive topics flagged |
| Handoff | One-line, not pushy |

### Summary Output (Debrief)

| Section | Check |
|---------|-------|
| TL;DR | ≤3 sentences |
| Key Takeaways | 3-5 bullets, insight markers applied |
| Powerful Quotes | Attribution, type, power rating |
| Extracted Entities | Organized by dimension |
| Follow-Up Items | Actionable, assigned if possible |

---

## Error Recovery Checklist

### If Catalog Save Fails

| Step | Action |
|------|--------|
| 1 | Note which records failed |
| 2 | Output JSON for manual entry |
| 3 | Continue with remaining workflow |
| 4 | Offer Brain Update despite failure |
| 5 | Document what needs manual follow-up |

### If Schema Mismatch

| Step | Action |
|------|--------|
| 1 | Check field name spelling |
| 2 | Check select option exact match |
| 3 | Check field ID vs field name |
| 4 | Output corrected JSON if fixable |
| 5 | Flag for schema refresh if needed |

---

## Quality Signals

### Good Debrief Indicators

- [ ] 3+ insight markers applied
- [ ] 5+ quotes captured (for 60min session)
- [ ] All 5 dimensions have content
- [ ] At least 1 ⚡ Surprise or 💡 Opportunity
- [ ] Entity counts feel proportional to session length

### Warning Signs

- 0 insight markers → Review for missed patterns
- <3 quotes from 60min session → Transcript quality issue?
- 0 entities in a dimension → Dimension not covered in session
- Many ⚠️ Contradictions → May need follow-up before saves
- Session feels thin → Consider Quick Debrief instead

---

## Handoff Prompts

### After Prep

```
After your call, say "debrief [client]" and paste your notes.
```

### After Full Debrief

```
Want me to run gap analysis or prioritize challenges?
```

### After Quick Debrief

```
Ready for Full Debrief to save to Catalog? Or want me to prep for your next session?
```

---

# Insight Extraction

How to identify and apply insight markers during debrief to surface high-value findings.

---

## Insight Markers

| Marker | Name | Meaning | Value |
|--------|------|---------|-------|
| ⚡ | Surprise | Contradicted an assumption we held | High learning value |
| 🔄 | Pattern | Theme mentioned 3+ times | Validates trend |
| ⚠️ | Contradiction | Conflicting statements | Needs clarification |
| 💡 | Opportunity | Unprompted solution idea from client | High buy-in potential |

---

## ⚡ Surprise Detection

### What Qualifies

A surprise is information that contradicts what we expected based on:
- Prior sessions with this client
- Industry norms
- Common assumptions
- Stated vs. actual behavior

### Detection Criteria

| Source of Assumption | Surprise Indicator |
|---------------------|-------------------|
| Prior session said X | This session reveals not-X |
| Industry typical is X | Client does Y instead |
| Stated goal was X | Actual priority is Y |
| Expected pain in X | Pain is actually in Y |
| Assumed they had X | They lack X |

### Examples

```
Prior session: "Our CRM is working great"
This session: "We've stopped using the CRM for forecasting"
→ ⚡ Surprise: CRM usage has degraded since last session

Industry norm: Sales teams prioritize pipeline
This session: "We focus more on customer retention than new sales"
→ ⚡ Surprise: Counter-typical sales strategy

Assumption: Executive sponsor is bought in
This session: "Leadership isn't sure this is the right timing"
→ ⚡ Surprise: Executive alignment weaker than assumed
```

### Application

Apply ⚡ to:
- Key findings that flip an assumption
- Information that requires strategy adjustment
- Facts that should inform future sessions

---

## 🔄 Pattern Detection

### What Qualifies

A pattern emerges when the same theme appears 3+ times:
- Within a single session (multiple mentions)
- Across sessions (different people say same thing)
- Across dimensions (shows up in process, technology, AND challenges)

### Detection Criteria

| Pattern Type | Threshold | Example |
|--------------|-----------|---------|
| Single session | 3+ mentions | "Approvals" mentioned 4 times |
| Cross-session | 2+ people | Sarah and Mike both cite "data quality" |
| Cross-dimension | 2+ dimensions | "Manual work" in Process AND Technology |

### Pattern Categories

| Category | What to Track |
|----------|---------------|
| Pain themes | Same problem repeatedly |
| System mentions | Same tool/system repeatedly |
| Department friction | Same handoff issue |
| Process bottlenecks | Same step causes delays |
| People dynamics | Same person/role mentioned |

### Examples

```
Session mentions:
- "The approval process takes forever" (minute 12)
- "We wait weeks for sign-off" (minute 28)
- "Getting VP approval is the bottleneck" (minute 41)
→ 🔄 Pattern: Approval delays (3 mentions)

Across sessions:
- CEO: "Data quality is our biggest issue"
- VP Ops: "We can't trust the numbers in our reports"
- Analyst: "I spend half my time cleaning data"
→ 🔄 Pattern: Data quality (3 stakeholders)
```

### Application

Apply 🔄 to:
- Challenges mentioned 3+ times (strong signal)
- Processes that multiple people cite as problematic
- Technology that comes up repeatedly
- Themes that span stakeholder levels

---

## ⚠️ Contradiction Detection

### What Qualifies

A contradiction occurs when:
- Same person says two conflicting things
- Different people give conflicting accounts
- Stated priority conflicts with behavior
- Official process differs from actual practice

### Detection Criteria

| Contradiction Type | Example |
|-------------------|---------|
| Self-contradiction | "We're customer-focused" but "We don't track NPS" |
| Cross-stakeholder | CEO says A, Manager says not-A |
| Say vs. Do | "Our top priority is X" but no resources on X |
| Policy vs. Practice | "Process is X" but "We actually do Y" |

### Examples

```
Same person:
- Minute 8: "Our team works well together"
- Minute 34: "There's constant friction between sales and ops"
→ ⚠️ Contradiction: Team cohesion — needs clarification

Different people:
- VP (last week): "Budget is approved and ready"
- Manager (today): "We're still waiting on budget confirmation"
→ ⚠️ Contradiction: Budget status unclear

Say vs. Do:
- Stated: "AI is our strategic priority"
- Reality: No AI budget, no AI hires, no AI projects
→ ⚠️ Contradiction: AI priority stated but not resourced
```

### Application

Apply ⚠️ to:
- Findings that require follow-up clarification
- Information that affects scope or approach
- Statements that warrant validation
- Areas where we need to dig deeper

**Action Required:** Every ⚠️ needs a follow-up plan

---

## 💡 Opportunity Detection

### What Qualifies

An opportunity is when the client unprompted:
- Suggests a solution idea
- Describes their ideal future state
- Identifies a specific change they want
- Proposes an approach or tool

### Why It Matters

Client-originated ideas have:
- Built-in buy-in (it's their idea)
- Validation of need (they've thought about it)
- Direction for solutions (they know what they want)
- Potential quick wins (they're ready to act)

### Detection Criteria

| Signal | Example Phrase |
|--------|---------------|
| Solution suggestion | "What if we could..." |
| Ideal state | "In a perfect world..." |
| Wish | "I wish we had..." |
| Specific ask | "We need something that..." |
| Vision | "Imagine if..." |

### Examples

```
"What if we could automatically route approvals based on deal size?"
→ 💡 Opportunity: Client suggests approval automation with tiered routing

"I wish we had a single view of the customer across all our systems"
→ 💡 Opportunity: Client wants unified customer view (360 dashboard)

"In a perfect world, the sales team wouldn't have to enter data twice"
→ 💡 Opportunity: Client identifies duplicate entry as target for automation
```

### Application

Apply 💡 to:
- Any unprompted solution idea from client
- Specific feature requests or wishes
- Described ideal future states
- Areas where client has clear vision

**Capture exactly:** Quote the client's words — their language matters for buy-in

---

## Marker Application Rules

### When Extracting

1. **Read through transcript/notes** looking for marker signals
2. **Tag as you go** — don't wait until the end
3. **One marker per insight** — choose the most relevant
4. **Include context** — what makes this significant

### Marker Priority

If an insight could have multiple markers, prioritize:

1. 💡 Opportunity (highest — actionable, client-owned)
2. ⚠️ Contradiction (needs resolution)
3. ⚡ Surprise (high learning value)
4. 🔄 Pattern (validation of known theme)

### Minimum Counts

For a typical 60-minute session, expect:
- ⚡ Surprises: 1-3
- 🔄 Patterns: 2-4
- ⚠️ Contradictions: 0-2
- 💡 Opportunities: 1-3

If you find none, dig deeper or flag as a thin session.

---

## Insight Output Format

When reporting insights:

```markdown
## Key Insights

### ⚡ Surprises
- **CRM abandonment**: Team has stopped using CRM for forecasting despite prior positive feedback

### 🔄 Patterns
- **Approval delays**: Mentioned 4x — consistent theme across discussion
- **Data quality**: Third stakeholder to cite this as top issue

### ⚠️ Contradictions (Follow-up Needed)
- **Budget status**: VP says approved, Manager says pending — clarify with CFO
- **Team alignment**: Mixed signals on cross-functional collaboration

### 💡 Opportunities (Client Ideas)
- **Tiered approval routing**: "What if approvals auto-routed by deal size?"
- **Customer 360 view**: "I wish we had a single view across all systems"
```

---

## Linking Insights to Catalog

When creating Discovery Catalog records:

| Marker | Primary Table | Notes Field |
|--------|---------------|-------------|
| ⚡ | Challenges or appropriate dimension | Add "⚡ SURPRISE:" prefix in notes |
| 🔄 | Challenges (usually) | Add "🔄 PATTERN:" prefix in notes |
| ⚠️ | Challenges | Add "⚠️ CONTRADICTION:" prefix, create follow-up |
| 💡 | Solutions | Add "💡 CLIENT IDEA:" prefix |

This ensures insights are preserved and searchable in the Catalog.

---

# Brain Update Generator

Generate formatted documents for updating Client Brains after discovery sessions.

---

## When to Use

After completing a debrief (Steps 1-7), generate a Brain Update document when:
- New stakeholder insights were captured
- Relationship dynamics changed
- Decisions were made
- New preferences/patterns were learned
- Any information belongs in the narrative Brain (not just structured Catalog)

**The Brain Update doc makes it easy to copy/paste into the Client Brain Google Doc.**

---

## Execution Flow

### Step 8A: Fetch Current Brain

The Brain Link was captured during Pre-flight Check (Step 0B). Now fetch the actual content:

```
Google Drive MCP: google_drive_fetch
Document ID: [extracted from Brain Link URL]
```

**Extracting Document ID from Brain Link:**
```
URL: https://docs.google.com/document/d/1ABC123xyz/edit
Document ID: 1ABC123xyz
```

If Brain Link is empty or fetch fails:
- Note: "No existing Brain found - all entries will be NEW"
- Continue with generation (treat everything as NEW)

### Step 8B: Parse Brain into Sections

Extract current state from each Brain section:

```
CURRENT_BRAIN = {
  "stakeholders": {
    "Karl Winters": {
      "title": "CFO",
      "role_type": "Economic Buyer",
      "power": 9,
      "sentiment": 5,
      "notes": "Conservative, data-driven"
    },
    ...
  },
  "relationship_health": {
    "score": 7,
    "trend": "improving",
    "last_contact": "2024-11-15"
  },
  "active_context": {
    "phase": "Discovery",
    "blockers": ["IT bandwidth", "Budget approval pending"],
    "open_questions": ["Timeline for Phase 2?"],
    "whats_working": ["Direct communication"],
    "whats_not": ["Long email chains"]
  },
  "decisions": [
    {"date": "2024-11-01", "decision": "Proceed with discovery", "made_by": "Karl"}
  ],
  "preferences": {
    "communication": ["Prefers Slack over email"],
    "meetings": ["Morning meetings preferred"],
    "avoid": ["Don't surprise in large meetings"]
  }
}
```

### Step 8C: Compare to Debrief Findings

For each extracted insight from the debrief, categorize:

| Category | Criteria | Action |
|----------|----------|--------|
| **NEW** | Entity/item not in current Brain | Add with full details |
| **UPDATE** | Entity exists, values changed | Show old → new |
| **CONFIRM** | Entity exists, might need update (low confidence) | Flag for review |
| **SKIP** | Already captured accurately | Don't include |

**Comparison Logic:**

```
For each PERSON from debrief:
  IF name NOT IN current_brain.stakeholders:
    → NEW
  ELSE:
    old = current_brain.stakeholders[name]
    IF sentiment changed OR power changed OR role changed:
      → UPDATE (show diff)
    ELSE IF new notes/insights:
      → UPDATE (append notes)
    ELSE:
      → SKIP

For each DECISION from debrief:
  IF decision NOT IN current_brain.decisions (fuzzy match):
    → NEW
  ELSE:
    → SKIP

For each PREFERENCE/PATTERN learned:
  IF not already in preferences section:
    → NEW
  ELSE:
    → SKIP
```

### Step 8D: Generate Update Document

Use the docx skill to create a formatted Word document:

```
Read: docx skill
```

Generate the document using the template below.

---

## Brain Section Mapping

Map debrief findings to Brain sections:

| Debrief Finding | Brain Section | Format |
|-----------------|---------------|--------|
| Person with Power/Sentiment | 2. Stakeholder Map | Table row |
| Person insights/concerns | 2. Stakeholder Map (Notes column) | Bullet points |
| Relationship observation | 3. Relationship Health | Paragraph with date |
| Current blocker | 4. Active Context → Blockers | Bullet point |
| Open question | 4. Active Context → Open Questions | Bullet point |
| Win/progress | 4. Active Context → Recent Wins | Bullet with date |
| Decision made | 5. Key Decisions Log | Table row |
| Communication preference | 6. Preferences → Communication | Bullet point |
| Meeting preference | 6. Preferences → Meetings | Bullet point |
| Thing that works | 6. Preferences → Things that work | Bullet point |
| Thing to avoid | 6. Preferences → Things to avoid | Bullet point |

---

## Parsing the Current Brain

### Section Detection

Look for these headers in the Brain document:

```
"Client Overview" or "## Client Overview" → Section 1
"Stakeholder Map" or "## Stakeholder Map" → Section 2
"Relationship Health" or "## Relationship Health" → Section 3
"Active Context" or "## Active Context" → Section 4
"Key Decisions" or "## Key Decisions" → Section 5
"Preferences" or "## Preferences" → Section 6
"Update Log" or "## Update Log" → Section 7
```

### Stakeholder Table Parsing

The Stakeholder Map typically has a table format:

```
| Name | Title | Role Type | Power | Sentiment | Notes |
|------|-------|-----------|-------|-----------|-------|
| Karl Winters | CFO | Economic Buyer | 9 | 5 | Conservative... |
```

Extract into structured format for comparison.

### Handling Variations

Brains may have slight variations in structure. Be flexible:
- Headers might be `##` or `###` or bold text
- Tables might use `|` or be formatted lists
- Sections might be in different order

If parsing fails for a section, note it and treat those items as potentially NEW.

---

## Document Template

### Section: Stakeholder Map

```
📍 SECTION 2: STAKEHOLDER MAP
─────────────────────────────

🆕 NEW: Sarah Chen
━━━━━━━━━━━━━━━━━━
Add this row to the Stakeholder Map table:

| Name | Title | Role Type | Power | Sentiment | Notes |
|------|-------|-----------|-------|-----------|-------|
| Sarah Chen | Controller | Influencer | 6 | 5 | Reports to Karl. Owns month-end close. Cautious about change but open to pilots. |


✏️ UPDATE: Karl Winters
━━━━━━━━━━━━━━━━━━━━━━━━
Find Karl Winters in the table and update:

• Sentiment: 5 → 8  (volunteered to champion AI pilot)
• Add to Notes: "Now acting as interim COO. Increasingly bought-in to AI transformation."
```

### Section: Relationship Health

```
📍 SECTION 3: RELATIONSHIP HEALTH
─────────────────────────────────

APPEND to the relationship narrative:

[2024-12-01] Strong session. Karl has evolved from cautious supporter
to active champion - volunteered to personally sponsor the AI pilot
before we even asked. Relationship trending positive.
Score recommendation: 7 → 8.
```

### Section: Key Decisions

```
📍 SECTION 5: KEY DECISIONS LOG
───────────────────────────────

🆕 ADD this row to the decisions table:

| Date | Decision | Made By | Rationale |
|------|----------|---------|-----------|
| 2024-12-01 | Approved AI pilot for month-end close | Karl Winters | "Let's prove the value quickly with a contained scope" |
```

### Section: Preferences

```
📍 SECTION 6: PREFERENCES & PATTERNS
────────────────────────────────────

🆕 ADD to "Things that work well":
• Lead with ROI numbers - Karl responds well to concrete financial impact
• Keep slides minimal - he prefers discussion over presentation

🆕 ADD to "Things to avoid":
• Don't schedule meetings after 4pm - he has hard stop for family
```

### Section: Update Log

```
📍 SECTION 7: UPDATE LOG
────────────────────────

ADD this entry at the top:

[2024-12-01] Interview with Karl Winters:
Updated stakeholder sentiment (Karl 5→8), added new stakeholder (Sarah Chen),
logged AI pilot decision. See Discovery Catalog session ID: recXXXXX.
```

---

## Output Delivery

After generating the document:

1. Save to `/mnt/user-data/outputs/[Client]-brain-update-[Date].docx`
2. Provide download link to user
3. Summarize what's in the update:
   - X new stakeholders
   - Y stakeholder updates
   - Z decisions logged
   - N preferences captured

**Example response:**

```
Brain Update document generated:

[Download: CES Brain Update 2024-12-01](computer:///mnt/user-data/outputs/CES-brain-update-2024-12-01.docx)

**Summary:**
• 1 new stakeholder (Sarah Chen)
• 1 stakeholder update (Karl Winters - sentiment 5→8)
• 1 decision logged (AI pilot approved)
• 2 new preferences captured

Open your CES Brain Google Doc and copy/paste from each section.
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Brain Link missing | Generate doc with all items as NEW, note "No existing Brain found" |
| Brain fetch fails | Generate doc with all items as NEW, note "Could not access Brain" |
| Brain parse fails | Generate doc with all items as NEW/CONFIRM, note parsing issue |
| No updates needed | Skip document generation, note "No Brain updates needed from this session" |
| Only Catalog updates | Note "All findings captured in Discovery Catalog - no narrative Brain updates needed" |

---

# Special Scenarios

Handling edge cases in discovery prep and debrief.

---

## Multiple Attendees

### Prep Considerations

**Question Allocation:**
| Attendees | Approach |
|-----------|----------|
| 2-3 people | Prepare questions for each, but expect organic flow |
| 4-6 people | Prepare 2-3 targeted questions per person |
| 7+ people | Workshop format — group questions, not individual |

**Briefing Format Adjustment:**
```markdown
## Attendee Profiles (Multiple)

### [Name 1] — [Title] (Primary)
- Background: [key context]
- Priority questions: [2-3 specific to them]
- Rapport: [connection point]

### [Name 2] — [Title]
- Background: [key context]
- Priority questions: [2-3 specific to them]
- Rapport: [connection point]

### [Name 3] — [Title]
- Background: [key context]
- Priority questions: [2-3 specific to them]
- Rapport: [connection point]
```

**Dynamic Navigation Tips:**
- Start with most senior person (sets tone)
- Use names when redirecting: "Sarah, you mentioned..."
- Watch for quiet attendees — invite them in
- Note who defers to whom (reveals dynamics)

### Debrief Considerations

**Entity Attribution:**
- Tag quotes to specific speakers
- Note sentiment per person (may differ)
- Capture interpersonal dynamics observed

**Conflicting Information:**
- When attendees disagree, capture both views
- Mark as ⚠️ Contradiction
- Note which person said what
- Don't resolve — flag for follow-up

---

## Follow-Up Sessions

### What Changes

Follow-up sessions differ from initial discovery:
- Context already exists
- Skip Landscape layer (unless new topic)
- Go deeper on Problems/Specifics
- Validate prior findings

### Prep Adjustments

**Before:**
1. Review prior session notes
2. Check Catalog for this client's records
3. Identify what was learned vs. still unknown
4. Focus questions on gaps

**Briefing Format:**
```markdown
## Session Context

**Prior Session:** [Date] — [Type] — [Key takeaways]

**What We Learned:**
- [Confirmed fact 1]
- [Confirmed fact 2]

**What We Still Need:**
- [ ] [Gap 1] — priority question
- [ ] [Gap 2] — priority question

**Follow-Up Questions:**
1. "Last time you mentioned [X]. Has anything changed?"
2. "We want to dig deeper on [Y]. Can you walk me through..."
3. "You mentioned [Z] was a challenge. What's happened since?"
```

### Debrief Adjustments

**Update vs. Create:**
- Check if People/Process/Technology records exist
- UPDATE existing records (add to notes, adjust scores)
- Only CREATE if truly new entity
- Use Change History format for updates

**Change History Entry:**
```
[YYYY-MM-DD | Session: Follow-up with Sarah]
Updated AI Readiness: 2 → 3 (pilot completed successfully)
```

---

## Scope Changes

### Mid-Engagement Pivot

When client priorities shift during engagement:

**Detection Signals:**
- New stakeholder introduces different priority
- Original sponsor's focus has changed
- External event shifted company direction
- Budget or timeline constraints changed

**Debrief Handling:**
1. Document the shift explicitly
2. Mark as ⚡ Surprise
3. Capture what changed and why
4. Note impact on existing findings

**Catalog Updates:**
- Don't delete prior findings — they're still valid context
- Add new records for new direction
- Update existing records with changed context
- Create Challenge record for "Scope Shift" if significant

### New Topic Emerges

When conversation reveals area outside original scope:

**During Session:**
- Note it but don't derail
- Ask one clarifying question
- Flag for potential expansion

**In Debrief:**
```markdown
## Scope Expansion Opportunity

New topic emerged: [Topic]
- Mentioned by: [Who]
- Context: [Why it came up]
- Relevance: [How it connects to engagement]

**Recommendation:**
- [ ] Explore in follow-up session
- [ ] Add to current scope
- [ ] Note for future engagement
```

---

## Conflicting Information

### Same Person, Different Statements

When an individual contradicts themselves:

**During Session:**
- Note both statements with timestamps
- If safe, gently probe: "Earlier you mentioned X, now Y — help me understand"

**In Debrief:**
- Mark as ⚠️ Contradiction
- Capture both statements
- Don't resolve — flag for clarification
- Note possible explanations (context changed, nuance lost, etc.)

### Different People, Different Views

When stakeholders disagree:

**Capture Approach:**
```markdown
### ⚠️ Contradiction: [Topic]

**View A** — [Name, Title]:
"[Quote or summary]"

**View B** — [Name, Title]:
"[Quote or summary]"

**Analysis:**
- Possible explanation: [e.g., different visibility, role perspective]
- Impact: [How this affects our work]
- Resolution needed: [Yes/No, how]
```

**Catalog Handling:**
- Create records for both views
- Link both to the contradiction topic
- Add notes explaining the disagreement
- Create follow-up action to resolve

---

## Thin Sessions

### What Makes a Session "Thin"

- Duration < 15 minutes
- Transcript < 1500 words
- Few substantive answers
- Surface-level responses
- Dominated by logistics or small talk

### Debrief Approach

**Use Quick Debrief:**
- Don't force Full Debrief extraction
- Capture what exists, note the gaps
- Suggest follow-up session

**Output Format:**
```markdown
## Session Summary (Limited Content)

**Duration:** [X] minutes
**Content Level:** Thin — limited substantive discussion

**What We Captured:**
- [Finding 1]
- [Finding 2]

**Gaps Remaining:**
- [Dimension 1]: No coverage
- [Dimension 2]: Minimal coverage

**Recommendation:** Schedule focused follow-up on [specific gaps]
```

---

## Technical Issues

### Transcript Quality Problems

**Partial Transcript:**
- Work with what's available
- Note gaps: "Minutes 12-18 missing"
- Flag any context that might be lost

**Poor Speaker Attribution:**
- Note uncertainty: "Speaker unclear"
- Use context clues to attribute
- Ask user to clarify critical quotes

**Audio Quality Issues:**
- Mark unclear passages: "[inaudible]"
- Don't guess at missing words
- Note impact on findings

### Catalog Save Failures

**If record creation fails:**
1. Don't panic — capture the data
2. Output JSON for manual entry
3. Continue with remaining workflow
4. Note which records need manual creation

**Fallback Output:**
```markdown
## Manual Entry Required

Catalog save failed for the following records.
Please create manually in Airtable.

### [Record Type]
```json
{
  "fields": {
    "Name": "...",
    "Client": ["rec..."],
    ...
  }
}
```
```

---

## Sensitive Information

### When Sensitive Topics Emerge

**During Session:**
- Don't probe unnecessarily
- Respect boundaries
- Note the topic was raised

**In Debrief:**
- Capture relevance to engagement
- Don't include personal details
- Mark as sensitive if needed for team awareness

**Catalog Handling:**
- Use discretion in what's recorded
- Some things belong in conversation memory, not permanent records
- When in doubt, ask user before saving

### Off-the-Record Comments

When someone says "off the record" or "between us":

**Approach:**
- Honor the request
- Don't include in formal Catalog
- Note that relevant context exists
- User can decide what to do with it

---

## Session Types: Special Handling

### Group Workshop (4+ people)

**Prep:**
- Focus on group dynamics, not individual questions
- Prepare facilitation structure
- Identify likely perspectives by role

**Debrief:**
- Note group consensus vs. dissent
- Capture emerging themes
- Track participation levels
- Mark group decisions explicitly

### Observation/Shadowing

**Prep:**
- Minimal questions — focus on what to watch for
- Prepare observation checklist

**Debrief:**
- Focus on Process and Technology dimensions
- Note workarounds observed
- Capture what people do vs. what they say they do
- Time-stamp key observations

### System Demo

**Prep:**
- Prepare technical questions
- Know what capabilities to evaluate

**Debrief:**
- Heavy Technology dimension focus
- Capture screenshots/recordings if available
- Note system limitations observed
- Document integration points
