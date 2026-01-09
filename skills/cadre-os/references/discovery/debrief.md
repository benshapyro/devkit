# Discovery Session Debrief

Process discovery session notes and transcripts into structured insights and Catalog records.

---

## Contents

1. [Mode Selection](#mode-selection)
2. [Quick Mode](#quick-mode)
3. [Full Mode](#full-mode)
4. [Entity Extraction Reference](#entity-extraction-reference)
5. [Insight Markers](#insight-markers)
6. [Quote Selection](#quote-selection)
7. [Error Recovery](#error-recovery)
8. [Handoff](#handoff)

---

## Mode Selection

| Mode | Duration | Use When | Catalog Writes |
|------|----------|----------|----------------|
| **Quick** | 3-5 min | Session < 10 min, < 2000 words, or "just the summary" | No |
| **Full** | 10-15 min | Standard discovery sessions, full transcripts, >20 min sessions | Yes |

**Default to Full for transcripts.** Use Quick for brief check-ins or when user requests summary only.

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
Read: references/data/discovery-catalog.md
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

**If yes:** See `brain-update-generator.md`

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

## Insight Markers

Flag patterns in debrief output:

| Marker | Meaning | When to Use |
|--------|---------|-------------|
| ⚡ | Surprise | Contradicted an assumption |
| 🔄 | Pattern | Theme mentioned 3+ times |
| ⚠️ | Contradiction | Conflicting statements |
| 💡 | Opportunity | Unprompted solution idea |

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

## Quality Checklist (Full Mode)

Before delivering:

- [ ] Session type confirmed with user
- [ ] Attendees confirmed with user
- [ ] All 5 dimensions extracted
- [ ] Quotes extracted (3-5 minimum)
- [ ] Insight markers applied (⚡🔄⚠️💡)
- [ ] Compact summary shown before save
- [ ] User confirmed or revised
- [ ] Records created in correct order
- [ ] Change History populated
- [ ] Brain Update offered
- [ ] Comms offered
- [ ] Handoff prompt included

---

## Handoff

After delivering debrief:

> "Want me to draft the **follow-up email**? **Internal Slack summary**?"

Then offer:

> "Want me to run **gap analysis** or **prioritize challenges**?"
