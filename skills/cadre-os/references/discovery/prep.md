# Discovery Session Prep

Prepare for client discovery sessions with targeted research and question selection.

---

## Contents

1. [Mode Selection](#mode-selection)
2. [Quick Mode](#quick-mode)
3. [Deep Mode](#deep-mode)
4. [Question Scaling](#question-scaling)
5. [Question Sequencing](#question-sequencing)
6. [Follow-Up Patterns](#follow-up-patterns)
7. [Graceful Degradation](#graceful-degradation)
8. [Handoff](#handoff)

---

## Mode Selection

| Mode | Duration | Use When |
|------|----------|----------|
| **Quick** | 2-5 min | Known client, profiled attendees, recent engagement, strong Brain context |
| **Deep** | 10-15 min | Unknown attendees, thin Brain/Catalog context, no recent engagement, new topics |

**Default to Quick.** Escalate to Deep when internal sources are insufficient.

---

## Quick Mode

Fast pre-call briefing using Catalog + Brain only (no external research).

### Step 1: Gather Context

**1A: Client Brain (Google Drive)**
```
Search: "[Client Name]" in folder "Client Brains"
```

Extract:
- Company context (industry, size)
- Stakeholder map (roles, power/sentiment)
- Relationship health + trend
- Recent updates
- What works/doesn't with this client

**1B: Discovery Catalog (Airtable)**

Base: `apprH2AppvnKfUpT0`

```
Query 0_Clients → get Client ID
Query 2_People → get attendee profiles (filter by Client ID)
Query 5_Challenges → get open challenges (Status != "Resolved", sort by Priority)
Query 1_Discovery_Log → get last 3 sessions (sort by Date desc)
```

### Step 2: Analyze Gaps

Compare known context against the Five Dimensions:

| Dimension | Coverage Check |
|-----------|----------------|
| People | Who's in the room? Any unknowns? |
| Process | Do we understand their workflows? |
| Technology | What systems are involved? |
| Challenges | What problems are we solving? |
| Solutions | What opportunities exist? |

Flag:
- ✅ Well-covered areas
- ❓ Gaps to probe
- ⚠️ Low-confidence items to validate

### Step 3: Select Questions

Pull from question-library.md based on:

1. **Attendee types** (Executive, Manager, Practitioner, Technical)
2. **Dimension gaps** — prioritize under-covered areas
3. **Session type** — match to meeting purpose

### Step 4: Generate Quick Briefing

```markdown
# Discovery Prep: [Client Name]
**Meeting:** [Type] | **Date:** [Date] | **Duration:** [X min]

---

## Quick Context
[2-3 sentences: Who is this client, where are we, what's the situation]

## Relationship Pulse
**Health:** [X]/10 ([↑/↓/→])
**Last Interaction:** [Date] — [1 sentence]
**Watch For:** [Signals, concerns, sensitivities]

---

## Attendee Profiles

### [Name] — [Title]
| Power | Sentiment | Archetype |
|-------|-----------|-----------|
| [X]/10 | [X]/10 | [Type] |

**Key Insight:** [What we know about this person]
**Approach:** [How to engage them]
**Questions for Them:**
- [Specific question 1]
- [Specific question 2]

[Repeat for each attendee]

---

## What We Know
[Bulleted list of established facts]

## What We Need to Learn
- [ ] [Gap 1]
- [ ] [Gap 2]
- [ ] [Gap 3]

---

## Suggested Agenda
1. [Opening] — X min
2. [Topic 1] — X min
3. [Topic 2] — X min
4. [Next steps] — X min

## Key Questions

**[Dimension with biggest gap]:**
- [Question with inline follow-up: "If yes → [follow-up]"]
- [Question]

**[Second dimension]:**
- [Question]
- [Question]

---

## Landmines
[Things to avoid based on client preferences or past issues]

## Opportunity
[What success looks like for this meeting]
```

---

## Deep Mode

Comprehensive pre-call briefing with external research for unknown attendees or thin context.

### Phase 1: Internal Research (Always — No Permission Needed)

**1A: Client Brain (Google Drive)**
```
Search: "[Client Name]" in folder "Client Brains"
```

Extract:
- Company context
- Stakeholder map
- Relationship health + trend
- Recent updates
- Preferences and sensitivities

**1B: Discovery Catalog (Airtable)**

Base: `apprH2AppvnKfUpT0`

```
Query 0_Clients → Client ID
Query 2_People → existing profiles
Query 5_Challenges → open challenges (Status != "Resolved")
Query 1_Discovery_Log → last 3 sessions
```

**1C: Project Files**
- Search for: past transcripts, meeting notes, proposals
- Extract: pain points mentioned, decisions made, commitments

**1D: Conversation Memory**
- Search past conversations for client context
- Time limit: 1 minute

**Gap Assessment:**
After internal research, evaluate:
- Do we have enough to create a valuable brief?
- Are key attendees profiled?
- Is the context current (last 21 days)?

**If sufficient** → Skip to Brief Generation
**If gaps remain** → Request permission for external research

### Phase 2: Communication Search (Ask Permission First)

**Permission Request (bundled):**
```
I've searched internal files and found [X key pieces of context].

Should I also search Slack, Gmail, and Fireflies for additional context? This helps find:
• Informal discussions about this client
• Email threads with the attendees
• Previous call transcripts

This will take ~5 minutes.
```

**Wait for response.** Only proceed if granted.

**If Permission Granted:**

**Slack Search** (2-3 min):
- Terms: [client name], [project name], [attendee names]
- Look for: informal context, team sentiment, concerns
- Extract: insights not in formal docs

**Gmail Search** (2-3 min):
- Terms: [client name], [attendee emails]
- Look for: formal communications, commitments, stated priorities
- Extract: official positions, scope agreements

**Fireflies Search** (2-3 min):
- Terms: [client name], [attendee names]
- Look for: previous calls, topics discussed
- Extract: themes, repeated concerns, prior commitments

**If sufficient** → Skip to Brief Generation
**If gaps remain (especially about contacts)** → Request web research

### Phase 3: Web Research (Ask Permission — Light Touch)

**Permission Request:**
```
I have context from internal sources but [attendee name] isn't in our system.

Should I do light web research? This would give us:
• Professional background (LinkedIn)
• Recent company news
• Industry context

Takes ~5-10 minutes.
```

**Wait for response.** Only proceed if granted.

**If Permission Granted:**

**Contact Research** (3-5 min per person):

| Source | What to Find |
|--------|--------------|
| LinkedIn | Current role, tenure, previous roles, education |
| Recent posts | Professional interests, thought leadership |
| Company page | Their position in org structure |

Extract for profile:
- Background relevant to conversation
- Rapport-building topics
- Professional interests
- Communication style hints

**Company Research** (5 min):

| Source | What to Find |
|--------|--------------|
| Company website | Products/services, recent news |
| LinkedIn company | Size, growth, recent posts |
| Google News (3 months) | Major events, announcements |

Extract:
- Size/revenue indicators
- Growth trajectory
- Recent changes
- Market position

**Stop Gate:**
- Total research should not exceed 10 minutes
- If early phases provide rich context, skip remaining

### Phase 4: Analyze and Identify Gaps

Organize findings by dimension:

| Dimension | What We Know | What We Need |
|-----------|--------------|--------------|
| People | [findings] | [gaps] |
| Process | [findings] | [gaps] |
| Technology | [findings] | [gaps] |
| Challenges | [findings] | [gaps] |
| Solutions | [findings] | [gaps] |

**Gap-Targeted Questions:**
- Don't ask what we already know
- Prioritize under-covered dimensions
- Target specific unknowns

### Phase 5: Generate Deep Briefing

```markdown
# Discovery Prep: [Client Name]
**Meeting:** [Type] | **Date:** [Date] | **Duration:** [X min]
**Research Depth:** Deep (internal + [sources used])

---

## Executive Summary
• [Most critical context point]
• [Key insight from research]
• [Primary focus for questions]
• [Expected outcome]

---

## Quick Context
[2-3 sentences integrating what we know with what we need to learn]

## Relationship Pulse
**Health:** [X]/10 ([↑/↓/→])
**Last Interaction:** [Date] — [1 sentence]
**Watch For:** [Signals, concerns, sensitivities]

---

## Attendee Profiles

### [Name] — [Title]
| Power | Sentiment | Archetype |
|-------|-----------|-----------|
| [X]/10 | [X]/10 | [Type] |

**Background:** [From research — role, tenure, previous experience]
**Key Insight:** [What we know about this person]
**Approach:** [How to engage them]
**Rapport Topics:** [Professional interests, shared context]

**Questions for Them:**
- [Specific question]
  → If [trigger]: [follow-up]
- [Specific question]
  → If [trigger]: [follow-up]

[Repeat for each attendee]

---

## What We Know (With Gaps Integrated)

**Company Context:**
We know [X]. We need to learn [Y].

**Department Context:**
We know [X]. We need to learn [Y].

**Technical Context:**
We know [X]. We need to learn [Y].

---

## Suggested Agenda
1. [Opening] — X min
2. [Topic 1] — X min
3. [Topic 2] — X min
4. [Next steps] — X min

## Key Questions

### Opening (Landscape) — 3-4 questions
Build rapport, understand success metrics, identify what's working.

1. [Question]
   → If [trigger]: [follow-up]
   → If [trigger]: [follow-up]

2. [Question]
   → If [trigger]: [follow-up]

### Problems & Priorities — 4-6 questions
Surface pain points, understand priority order.

3. [Question]
   → If [trigger]: [follow-up]
   → If [trigger]: [follow-up]

4. [Question]
   → If mentions time: "How many hours per week?"
   → If mentions errors: "What's the error rate?"

### Process Deep Dive — 3-4 questions
Walk through specific workflows.

5. [Question]
   → If [trigger]: [follow-up]

### Specifics & Quantification — 2-3 questions
Get concrete numbers and data.

6. [Question]
   → If [trigger]: [follow-up]

---

## Landmines & Sensitivities
[Things to avoid based on research]

## Opportunity
[What success looks like for this meeting]

---

**After your call:** Say "debrief [client]" and paste your notes.
```

---

## Question Scaling

| Duration | Total | Opening | Problems | Process | Specifics |
|----------|-------|---------|----------|---------|-----------|
| 30 min | 6-8 | 2 | 3 | 2 | 1 |
| 45 min | 10-12 | 3 | 4 | 3 | 2 |
| 60 min | 12-15 | 4 | 5 | 4 | 2 |
| 90 min | 15-18 | 4 | 6 | 5 | 3 |

---

## Question Sequencing

Always follow: **Landscape → Problems → Process → Specifics**

| Layer | Purpose | Example |
|-------|---------|---------|
| Landscape | Establish context | "What does success look like for your team?" |
| Problems | Surface pain points | "What's your biggest operational challenge?" |
| Process | Walk through workflows | "Walk me through how quotes get approved" |
| Specifics | Get numbers | "How many hours per week does this consume?" |

---

## Follow-Up Patterns

Every main question gets 2-3 conditional follow-ups:

```
Q: What's your biggest pain point?

→ If mentions "approvals": "Walk me through the approval chain"
→ If mentions "data": "What systems hold that data?"
→ If shows frustration: "Give me a recent example"
→ If mentions "time": "How many hours per week?"
```

See `follow-up-patterns.md` for comprehensive library.

---

## Graceful Degradation

| Situation | Adaptation |
|-----------|------------|
| Attendee not in Catalog | Note as "New contact — learn about them" |
| No recent sessions | Note "Context may be stale — validate early" |
| Thin Brain context | Lean heavier on Catalog data |
| No external permission | Note gaps, use generic questions |
| Contact not findable | Note as "Unknown — learn about them" |
| Sparse results | Note low confidence, ask user for input |

---

## Quality Checklist (Deep Mode)

Before delivering:

- [ ] Research completed within time limits (≤10 min)
- [ ] All permissions requested where needed
- [ ] Knowledge gaps integrated (not separate section)
- [ ] People profiles included for known contacts
- [ ] Questions target specific gaps
- [ ] Questions sequenced: Landscape → Problems → Process → Specifics
- [ ] Quantity matches duration
- [ ] Each question has 2-3 conditional follow-ups
- [ ] Plain English throughout
- [ ] Scannable in <5 minutes
- [ ] Handoff prompt included

---

## Handoff

After generating briefing:

> "After your call, say 'debrief [client]' and paste your notes."
