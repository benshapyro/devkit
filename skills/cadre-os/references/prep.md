# Discovery Session Prep

Complete reference for preparing discovery sessions: prep workflows, stakeholder archetypes, methodology, and follow-up techniques.

## Table of Contents

- [Prep Workflow](#prep-workflow)
  - [Mode Selection](#mode-selection)
  - [Quick Mode](#quick-mode)
  - [Deep Mode](#deep-mode)
  - [Question Scaling](#question-scaling)
  - [External Research Protocols](#external-research-protocols)
- [Stakeholder Archetypes](#stakeholder-archetypes)
  - [Power/Sentiment Matrix](#the-powersentiment-matrix)
  - [The Nine Archetypes](#the-nine-archetypes)
  - [ADKAR Assessment](#adkar-stage-assessment)
- [Discovery Playbook](#discovery-playbook)
  - [Five Dimensions](#the-five-discovery-dimensions)
  - [Discovery Phases](#discovery-phases)
  - [Session Types](#session-types)
  - [Coverage Checklist](#discovery-coverage-checklist)
- [Follow-Up Patterns](#follow-up-patterns)
  - [Energy-Based Follow-Ups](#energy-based-follow-ups)
  - [Advanced Techniques](#advanced-techniques)
  - [Quantification Patterns](#quantification-patterns)

---

# Prep Workflow

Prepare for client discovery sessions with targeted research and question selection.

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

> See [data-schema.md](data-schema.md) for base ID and schema.

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

Pull from [questions.md](questions.md) based on:

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

> See [data-schema.md](data-schema.md) for base ID and schema.

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

> **Detailed protocols:** See [External Research Protocols](#external-research-protocols) for search patterns, extraction guidelines, and time limits.

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

> **Detailed protocols:** See [External Research Protocols](#external-research-protocols) for company and contact research patterns.

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

## External Research Protocols

Detailed protocols for Deep Mode external research. Reference this section when executing Phase 2 (Communications) or Phase 3 (Web Research).

> **Time Limits:** Total external research should not exceed 10 minutes. Stop early if you have 80%+ of needed context.

### Research Sequence Overview

| Phase | Source | Permission | Time Limit |
|-------|--------|------------|------------|
| 1 | Internal (Brain, Catalog, files) | Just do it | 2-3 min |
| 2 | Communications (Slack, Gmail, Fireflies) | Ask once, bundled | 5 min total |
| 3 | Web (LinkedIn, company site, news) | Ask once | 5-10 min |

**Stop Gate Rule:** After each phase, assess: "Do we have enough for a valuable brief?" If yes, stop. If critical gaps remain, proceed to next phase.

---

### Slack Search Protocol

**Time Limit:** 2 minutes

**Search Patterns:**
- `[Company name]` — Recent mentions
- `[Contact name]` — Specific person discussions
- `[Project name]` — Project-specific context
- `from:@[teammate] [client]` — Colleague conversations about client

**Extract:**
- Recent developments or updates
- Open questions or concerns
- Action items pending
- Relationship dynamics
- Tone and communication style

**Red Flags to Surface:**
- Unresolved complaints
- Delayed deliverables
- Scope concerns
- Relationship friction

---

### Gmail Search Protocol

**Time Limit:** 2 minutes

**Search Patterns:**
- `from:[client domain]` — Inbound emails
- `to:[client domain]` — Outbound emails
- `[client name] subject:[topic]` — Topic-specific threads
- `[contact name]` — Person-specific exchanges

**Extract:**
- Formal communications and commitments
- Decision trails
- Scheduling patterns (response times, preferences)
- Stakeholder cc patterns (who's looped in)
- Tone indicators

**Look For:**
- Recent email threads (last 30 days priority)
- Key decisions documented
- Outstanding asks
- Meeting follow-ups

---

### Fireflies Search Protocol

**Time Limit:** 2-3 minutes

**Search Patterns:**
- `[Company name]` — All client meetings
- `[Contact name]` — Meetings with specific person
- Filter by date — Most recent first

**For Each Relevant Transcript, Extract:**
- Key topics discussed
- Decisions made
- Action items assigned
- Pain points mentioned
- Quotes worth referencing
- Sentiment and energy

**Compare Across Transcripts:**
- Pattern identification
- Topic progression
- Changes in tone or priority
- Questions answered vs. remaining

---

### Company Research Protocol

**Time Limit:** 5 minutes total

**Company Website (2 min):**

| Page | Extract |
|------|---------|
| About | Mission, history, leadership team |
| Products/Services | Offerings, differentiation |
| News/Press | Recent announcements, initiatives |
| Careers | Growth signals, culture indicators |

**LinkedIn Company Page (2 min):**

| Section | Extract |
|---------|---------|
| About | Company stats, overview |
| Posts | Recent priorities, initiatives |
| People | Growth patterns, hiring focus |

**Recent News (1 min):**

Search: `[Company name] news` (past 3 months)

Look for: Funding announcements, product launches, leadership changes, partnerships, challenges.

---

### Contact Research Protocol

**Time Limit:** 3-5 minutes per key contact

**LinkedIn Profile — Extract:**

| Field | Purpose |
|-------|---------|
| Current role | Tenure, scope, reporting |
| Previous roles | Career trajectory, expertise areas |
| Education | Common ground, background |
| Posts/activity | Current interests, thought leadership |
| Skills/endorsements | Technical vs. business orientation |

**Rapport Topics to Note:**
- Shared connections
- Common background (school, employer, industry)
- Recent posts or articles
- Professional interests

**Professional Signals:**

| Signal | What It Suggests |
|--------|------------------|
| Long tenure in role | Deep expertise, may resist change |
| Recent promotion | Motivated to make mark, open to ideas |
| Multiple short stints | Change-oriented, or problem pattern |
| Technical background | Detail-oriented, wants specifics |
| Business background | Outcome-oriented, wants ROI |

---

### Research Documentation Format

Capture findings concisely:

```markdown
## Research Summary

### Company Context
- [Key fact 1]
- [Key fact 2]
- Recent: [news/development]

### Contact Profiles

**[Name 1]** — [Title]
- Background: [relevant experience]
- Rapport: [shared connection/interest]
- Style: [communication preference]

### Communication Context
- Recent topics: [from Slack/Email/Fireflies]
- Open items: [pending questions/actions]
- Sentiment: [overall tone]

### Knowledge Gaps Remaining
- [ ] [Gap 1]
- [ ] [Gap 2]
```

---

### Time Management

**Strict Limits:**

| Activity | Max Time |
|----------|----------|
| Slack search | 2 min |
| Gmail search | 2 min |
| Fireflies review | 3 min |
| Company web research | 5 min |
| Contact research (per person) | 3 min |
| **Total external research** | **10 min max** |

**Stop Conditions:**
- You have 80%+ of needed context
- Time limit reached
- Diminishing returns (searches repeat same info)
- Enough for strong question selection

**Quality Over Completeness:** Better to have solid prep on key topics than shallow coverage of everything. Prioritize:
1. Attendee backgrounds (for rapport)
2. Recent developments (for relevance)
3. Known pain points (for question targeting)
4. Relationship context (for tone calibration)

---

# Stakeholder Archetypes

Common stakeholder patterns and how to engage them effectively.

---

## Why Archetypes Matter

Every client organization has different people, but certain patterns repeat. Recognizing archetypes helps you:
- Anticipate concerns before they surface
- Tailor your approach to what resonates
- Avoid common missteps
- Convert skeptics into supporters

**Important:** Real people are complex. Use archetypes as starting hypotheses, not fixed labels.

---

## The Power/Sentiment Matrix

Plot stakeholders on two dimensions:

```
                    SENTIMENT
           Resistant ◄────────► Supportive
              1                    10
              │
        10    │  ┌─────────────┬─────────────┐
              │  │             │             │
     HIGH     │  │   THREAT    │  CHAMPION   │
              │  │  Powerful   │  Powerful   │
              │  │  Resistant  │  Supportive │
              │  │             │             │
   P    5     │  ├─────────────┼─────────────┤
   O          │  │             │             │
   W    │     │  │  SKEPTIC    │  ADVOCATE   │
   E    │     │  │  Less power │  Less power │
   R    │     │  │  Resistant  │  Supportive │
              │  │             │             │
        1     │  └─────────────┴─────────────┘
              │
```

| Quadrant | Power | Sentiment | Strategy |
|----------|-------|-----------|----------|
| **Champion** | High | Supportive | Leverage, empower, use as ambassador |
| **Threat** | High | Resistant | Understand concerns, find common ground, neutralize |
| **Advocate** | Low | Supportive | Elevate their voice, use for grassroots momentum |
| **Skeptic** | Low | Resistant | Address concerns, may convert with evidence |

---

## The Nine Archetypes

### The Champion
**Profile:**
- Often: Rising leader or frustrated innovator
- Already believes change is needed
- Willing to spend political capital
- Wants to be part of the solution

**Signals:**
- Enthusiastic engagement from the start
- "I've been saying this for years"
- Volunteers information proactively
- Asks how they can help
- Leans forward, nods, takes notes

**Engagement Strategy:**
- Make them a partner, not just a source
- Give them visible roles and credit
- Keep them informed and involved
- Use them to navigate internal politics
- Leverage as ambassador to skeptics

**Watch Out For:**
- May over-promise on behalf of organization
- May burn political capital too fast
- Don't over-rely on them — build broader support

---

### The Skeptic
**Profile:**
- Often: Mid-level manager or veteran employee
- Has seen initiatives come and go
- Protective of team and status quo
- Wants proof, not promises

**Signals:**
- "We tried something like this before..."
- "My team is already overloaded"
- "What happens to our jobs?"
- Arms crossed, minimal engagement
- Asks pointed, challenging questions

**Engagement Strategy:**
- Acknowledge past experiences, ask what went wrong
- Focus on their pain points, not your solution
- Show evidence from similar situations
- Give them ownership of part of the solution
- Address job security concerns directly
- Don't try to "sell" — let evidence speak

**Watch Out For:**
- Can become active blocker if ignored
- Influences others quietly behind the scenes
- Skepticism may be covering valid concerns

---

### The Political
**Profile:**
- Often: Senior manager or cross-functional leader
- Focused on perception and positioning
- Careful about what they say publicly
- Plays multiple stakeholders

**Signals:**
- Vague, non-committal answers
- "Off the record..."
- Asks who else you've talked to
- Watches others before speaking in groups
- Hedges bets, avoids strong positions

**Engagement Strategy:**
- Build trust through confidentiality
- Read between the lines
- Triangulate what they say with others
- Don't put them on the spot publicly
- Understand their incentives and pressures
- Build private rapport before group settings

**Watch Out For:**
- May say one thing, do another
- May play factions against each other
- Their real opinion may never surface publicly

---

### The Technical
**Profile:**
- Often: IT lead, engineer, or specialist
- Deep expertise in systems and processes
- Values accuracy and precision
- May be skeptical of "business speak"

**Signals:**
- Deep dives into technical details
- Uses jargon and acronyms freely
- "Actually, the way it works is..."
- Wants specifics, not generalities
- May challenge technical claims

**Engagement Strategy:**
- Speak their language, respect their expertise
- Ask detailed technical questions
- Don't oversimplify or hand-wave
- Acknowledge complexity they deal with
- Validate findings with them before presenting
- Consider making them a co-designer

**Watch Out For:**
- Can be territorial about their domain
- May dismiss non-technical perspectives
- May over-engineer solutions

---

### The Executive
**Profile:**
- Often: C-suite or senior VP
- Time-pressured, strategic focus
- Wants outcomes, not process
- Decisions carry organizational weight

**Signals:**
- Checks watch/phone frequently
- "What's the bottom line?"
- Asks about ROI, timeline, risk
- Delegates details to others
- Short attention for deep dives

**Engagement Strategy:**
- Lead with outcomes and business impact
- Be concise — respect their time
- Have the details ready but don't lead with them
- Connect everything to strategic priorities
- Make asks clear and actionable
- Follow up in writing with key points

**Watch Out For:**
- May commit to unrealistic timelines
- May lose interest when implementation gets hard
- Their time is limited — use it wisely

---

### The Quiet
**Profile:**
- Often: Individual contributor or introverted expert
- Has valuable insights but doesn't volunteer them
- Prefers listening to speaking
- May be overlooked in group settings

**Signals:**
- Brief answers, reserved demeanor
- Rarely speaks first in meetings
- More forthcoming in 1:1 settings
- Answers questions but doesn't elaborate
- May communicate better in writing

**Engagement Strategy:**
- Create space for them to contribute
- Use 1:1 conversations, not just group settings
- Ask direct questions and wait for answers
- Follow up in writing for more detail
- Don't mistake quiet for disagreement
- Value their observations — often most insightful

**Watch Out For:**
- Easy to overlook but often have key insights
- May disengage if not explicitly included
- Group settings may silence them entirely

---

### The Overwhelmed
**Profile:**
- Often: Practitioner or front-line manager
- Drowning in day-to-day work
- Wants help but has no bandwidth
- Change feels like more burden

**Signals:**
- "I just don't have time"
- Frazzled, mentions scope concerns
- Short, distracted responses
- Reschedules meetings frequently
- Focuses on immediate fires

**Engagement Strategy:**
- Keep interactions short and focused
- Show immediate value proposition
- Do the work for them (bring drafts, summaries)
- Position change as reducing burden, not adding
- Demonstrate quick wins early
- Be flexible with their schedule

**Watch Out For:**
- May disengage from discovery entirely
- Implementation may stall at their level
- Their pain points are real — don't dismiss

---

### The Historian
**Profile:**
- Often: Long-tenured employee or institutional memory
- Knows how things got to be this way
- References past attempts and decisions
- Protective of what has worked

**Signals:**
- "We tried that in 2019..."
- "The reason we do it this way is..."
- References people and projects from years ago
- Past-focused in explanations
- May resist change that ignores history

**Engagement Strategy:**
- Honor the history — ask about past attempts
- Understand what worked and what didn't
- Show how this is different from before
- Acknowledge institutional knowledge
- Position them as valuable continuity
- Learn the political history from them

**Watch Out For:**
- May be anchored to "how we've always done it"
- Past failures may create learned helplessness
- Their knowledge is valuable — don't dismiss

---

### The New Arrival
**Profile:**
- Often: Recent hire (< 1 year)
- Fresh perspective, fewer assumptions
- Limited political awareness
- May see things others have normalized

**Signals:**
- "At my last company, we..."
- Fresh eyes on dysfunction
- Asks "naive" questions that are actually insightful
- Less aware of political landmines
- May not know key history

**Engagement Strategy:**
- Value their outside perspective
- Help them navigate internal politics
- Use them to challenge assumptions
- Don't dismiss their observations as uninformed
- Pair with a Historian for balanced view
- They may see things clearly that others miss

**Watch Out For:**
- May not understand why things are the way they are
- Could step on political landmines unknowingly
- Fresh perspective is valuable but incomplete

---

## ADKAR Stage Assessment

Assess each stakeholder's change readiness:

| Stage | Meaning | Signals | What They Need |
|-------|---------|---------|----------------|
| **Awareness** | Know change is happening | "I didn't know..." "Really?" | Information about what and why |
| **Desire** | Want to participate | "That would be nice..." Interest | Personal motivation, WIIFM |
| **Knowledge** | Know how to change | "How would we...?" Detail questions | Training, process clarity |
| **Ability** | Can actually do it | "We tried but..." Struggles | Practice, support, time |
| **Reinforcement** | Sustaining change | "It's working but..." Backsliding | Recognition, feedback, iteration |

### Stage-Specific Engagement

| If They're At... | Don't... | Do... |
|------------------|----------|-------|
| **Awareness** | Jump to training | Explain the why and what |
| **Desire** | Assume they're bought in | Connect to their personal motivations |
| **Knowledge** | Expect behavior change | Provide detailed how-to |
| **Ability** | Get frustrated | Offer support and practice |
| **Reinforcement** | Declare victory | Monitor and reinforce |

---

## Stakeholder Engagement Quick Reference

| Archetype | First Meeting Focus | Key Question | Avoid |
|-----------|---------------------|--------------|-------|
| Champion | Enlisting as partner | "How can we work together?" | Taking them for granted |
| Skeptic | Listening to concerns | "What should I know about past attempts?" | Dismissing their experience |
| Political | Building trust | "What matters to you in this?" | Putting them on the spot |
| Technical | Learning from them | "Help me understand how this really works" | Hand-waving over details |
| Executive | Strategic alignment | "What does success look like?" | Drowning them in details |
| Quiet | Creating space | "What's your perspective on this?" | Overlooking them in groups |
| Overwhelmed | Showing quick value | "What's your biggest headache?" | Adding to their burden |
| Historian | Understanding history | "What have you tried before?" | Ignoring institutional knowledge |
| New Arrival | Valuing fresh eyes | "What stands out to you as odd?" | Dismissing their observations |

---

## Building Your Stakeholder Map

For each key stakeholder, capture:

| Field | How to Assess |
|-------|---------------|
| **Power (1-10)** | Role level + informal influence |
| **Sentiment (1-10)** | Current support level |
| **Archetype** | Best-fit pattern from the nine |
| **ADKAR Stage** | Where they are in change journey |
| **Key Concerns** | What's top of mind for them |
| **Personal Motivators** | What do they want |
| **Engagement Strategy** | How to work with them |
| **Champion Potential** | Could they become a champion |

### Quick Detection Guide

In the first 5 minutes, look for:

| Signal | Likely Archetype |
|--------|------------------|
| Enthusiastic, volunteering info | Champion |
| Arms crossed, "prove it" attitude | Skeptic |
| Watches others, hedges answers | Political |
| Deep dives into technical details | Technical |
| Time-pressured, wants bottom line | Executive |
| Brief answers, reserved | Quiet |
| Frazzled, mentions bandwidth | Overwhelmed |
| References past attempts | Historian |
| Fresh perspective, "at my last company" | New Arrival |

### Common Archetype Combinations

Real people often blend archetypes:
- **Technical + Skeptic** — Wants proof AND technical depth
- **Executive + Political** — Strategic but careful about positioning
- **Champion + Overwhelmed** — Supportive but has no bandwidth
- **Historian + Skeptic** — Past-focused resistance
- **New Arrival + Champion** — Fresh and enthusiastic

---

# Discovery Playbook

Codifies how Cadre conducts discovery — the methodology that makes our work consistent and thorough.

---

## What Is Discovery?

Discovery is the process of deeply understanding a client's current state before proposing solutions. It's the foundation of everything we do — skip it or do it poorly, and everything downstream suffers.

**Discovery answers:** What's really going on here, and what should we do about it?

### Why Discovery Matters

| Without Good Discovery | With Good Discovery |
|------------------------|---------------------|
| Solutions address symptoms, not root causes | Solutions target the actual problem |
| Recommendations feel generic | Recommendations feel tailored |
| Stakeholders feel unheard | Stakeholders feel understood |
| Implementation hits unexpected blockers | Risks are anticipated |
| ROI is hard to prove | Baseline is established for measurement |

### The Discovery Mindset

- **Curious, not assumptive** — We don't know the answer yet; we're here to learn
- **Empathetic, not judgmental** — Their current state exists for reasons
- **Systematic, not scattered** — We cover all dimensions methodically
- **Evidence-based, not opinion-based** — We capture quotes and data, not just impressions

---

## The Five Discovery Dimensions

Everything we learn in discovery maps to one of five dimensions:

```
┌─────────────────────────────────────────────────────────────────┐
│                    THE FIVE DIMENSIONS                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                        │
│  │ PEOPLE  │  │ PROCESS │  │  TECH   │                        │
│  │         │  │         │  │         │                        │
│  │ Who's   │  │ How work│  │ What    │                        │
│  │involved │  │ happens │  │ tools   │                        │
│  └────┬────┘  └────┬────┘  └────┬────┘                        │
│       │            │            │                              │
│       └────────────┼────────────┘                              │
│                    │                                           │
│                    ▼                                           │
│            ┌─────────────┐                                     │
│            │ CHALLENGES  │                                     │
│            │             │                                     │
│            │ What's      │                                     │
│            │ broken      │                                     │
│            └──────┬──────┘                                     │
│                   │                                            │
│                   ▼                                            │
│            ┌─────────────┐                                     │
│            │ SOLUTIONS   │                                     │
│            │             │                                     │
│            │ What could  │                                     │
│            │ fix it      │                                     │
│            └─────────────┘                                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Dimension Details

| Dimension | What We Learn | Key Questions |
|-----------|---------------|---------------|
| **People** | Who matters, what they want, how they feel about change | Who makes decisions? Who does the work? Who's affected? Who's supportive/resistant? |
| **Process** | How work actually happens (not just how it's supposed to) | What's the workflow? How long does it take? Where are the bottlenecks? What's manual? |
| **Technology** | What systems exist, how they connect, how well they work | What tools do you use? Do they talk to each other? What's missing? What do you hate? |
| **Challenges** | Pain points, inefficiencies, risks, unmet needs | What's frustrating? What takes too long? What breaks? What keeps you up at night? |
| **Solutions** | Ideas, wishes, past attempts, constraints | What have you tried? What would ideal look like? What's off the table? |

---

## Discovery Phases

Discovery happens in three phases:

### Phase 1: Foundation (Sessions 1-2)
**Goal:** Understand the landscape

- Company context and strategy
- Organizational structure
- Key stakeholders and their roles
- Current state overview
- Initial hypothesis about opportunities

**Outputs:**
- Stakeholder map draft
- Initial process inventory
- Technology landscape sketch
- Preliminary challenge list

### Phase 2: Deep Dive (Sessions 3-6)
**Goal:** Understand the details

- Detailed process walkthroughs
- Stakeholder interviews (individual)
- System demonstrations
- Data review
- Pain point validation

**Outputs:**
- Detailed process documentation
- Stakeholder profiles with Power/Sentiment
- Challenge prioritization (Impact × Urgency × Readiness)
- Emerging patterns and themes

### Phase 3: Synthesis (Sessions 7-8)
**Goal:** Validate and refine

- Pattern presentation to stakeholders
- Gap validation
- Solution ideation workshop
- Priority alignment
- Next steps agreement

**Outputs:**
- Validated challenge list
- Prioritized opportunity matrix
- Initial roadmap concepts
- Agreed next steps

---

## Session Types

### Kickoff Session
**Purpose:** Align on discovery scope and approach
**Duration:** 60-90 minutes
**Attendees:** Project sponsors, key stakeholders
**Agenda:**
1. Introductions and context (10 min)
2. Discovery objectives and approach (15 min)
3. Current understanding and hypotheses (20 min)
4. Stakeholder identification (15 min)
5. Logistics and scheduling (10 min)
6. Questions and next steps (10 min)

### Stakeholder Interview
**Purpose:** Deep understanding of one person's perspective
**Duration:** 45-60 minutes
**Attendees:** Single stakeholder + Cadre team
**Structure:**
1. Background and role (5 min)
2. Day-in-the-life / workflow (15 min)
3. Pain points and frustrations (15 min)
4. Tools and systems (10 min)
5. Wishes and ideas (10 min)
6. Who else should we talk to? (5 min)

### Process Deep Dive
**Purpose:** Detailed understanding of a specific workflow
**Duration:** 60-90 minutes
**Attendees:** Process owner + practitioners
**Structure:**
1. Process overview and trigger (10 min)
2. Step-by-step walkthrough (30-45 min)
3. Variations and exceptions (15 min)
4. Pain points within the process (15 min)
5. Volume and frequency data (10 min)

### Workshop
**Purpose:** Collaborative exploration with multiple stakeholders
**Duration:** 90-180 minutes
**Attendees:** Mixed stakeholder group
**Structure:**
1. Context setting (10 min)
2. Current state mapping (30 min)
3. Problem identification (30 min)
4. Prioritization exercise (20 min)
5. Solution brainstorming (30 min)
6. Next steps (10 min)

### System Demo
**Purpose:** Understand technology in practice
**Duration:** 30-60 minutes
**Attendees:** System users/admins
**Structure:**
1. System purpose and users (5 min)
2. Live walkthrough of key workflows (20-30 min)
3. Pain points and workarounds (15 min)
4. Integration points (10 min)

### Validation Session
**Purpose:** Confirm findings and fill gaps
**Duration:** 60 minutes
**Attendees:** Key stakeholders
**Structure:**
1. Summary of findings (20 min)
2. Gap identification (15 min)
3. Clarification and correction (15 min)
4. Priority alignment (10 min)

---

## Discovery Coverage Checklist

Before concluding discovery, ensure coverage across all dimensions:

### People Coverage
- [ ] Key decision maker(s) identified
- [ ] Economic buyer identified
- [ ] Champion(s) identified
- [ ] Potential blockers identified
- [ ] Power/Sentiment mapped for key stakeholders
- [ ] ADKAR stage assessed for change readiness
- [ ] Influence network understood

### Process Coverage
- [ ] Core processes documented
- [ ] Process owners identified
- [ ] Frequency and volume captured
- [ ] Time/cost estimates obtained
- [ ] Pain points within processes identified
- [ ] Automation readiness assessed
- [ ] Dependencies mapped

### Technology Coverage
- [ ] Key systems inventoried
- [ ] Integration landscape understood
- [ ] Data flow mapped
- [ ] Satisfaction/reliability assessed
- [ ] API/automation capability known
- [ ] Contract/renewal timelines captured
- [ ] AI integration potential assessed

### Challenge Coverage
- [ ] Challenges categorized (root cause vs symptom)
- [ ] Impact quantified where possible
- [ ] Urgency assessed
- [ ] Readiness to address assessed
- [ ] Quick wins identified
- [ ] Evidence/quotes captured
- [ ] Stakeholders affected identified

### Solution Coverage
- [ ] Past attempts understood
- [ ] Constraints identified
- [ ] Stakeholder ideas captured
- [ ] Solution types considered (process, tech, people, data)
- [ ] Horizons defined (Now, Next, Later)
- [ ] Dependencies mapped
- [ ] Success criteria drafted

---

## Discovery Anti-Patterns

### Things That Derail Discovery

| Anti-Pattern | What It Looks Like | How to Avoid |
|--------------|-------------------|--------------|
| **Solutioneering** | Jumping to recommendations before understanding | Discipline: no solutions until Phase 3 |
| **Executive Echo** | Only hearing leadership perspective | Insist on frontline interviews |
| **Happy Path Only** | Missing edge cases and exceptions | Ask: "What happens when...?" |
| **Tech Fixation** | Assuming technology is always the answer | Explore process and people dimensions equally |
| **Surface Skating** | Accepting first answers without probing | Use "5 Whys" technique |
| **Confirmation Bias** | Finding evidence for pre-existing beliefs | Actively seek disconfirming data |
| **Scope Creep** | Discovery expands indefinitely | Define boundaries upfront, timebox sessions |
| **Analysis Paralysis** | Gathering data without synthesizing | Synthesize after each session, not just at end |

### Recovery Tactics

| If You Notice... | Do This... |
|------------------|------------|
| Only talked to managers | Request frontline interviews |
| Haven't seen systems in action | Schedule system demos |
| Lots of symptoms, no root causes | Run 5 Whys on top challenges |
| Conflicting information | Bring stakeholders together for alignment |
| Can't quantify impact | Ask for volume, frequency, time estimates |
| Missing a dimension entirely | Add targeted session to fill gap |

---

## Discovery Outputs

### What Gets Captured (Discovery Catalog)

| Table | Key Fields | Captured During |
|-------|------------|-----------------|
| **People** | Name, Title, Power, Sentiment, ADKAR Stage, Key Insights | All sessions |
| **Process** | Name, Frequency, Hours, Cost, Automation Readiness | Process deep dives |
| **Technology** | Name, Vendor, Satisfaction, Integration Quality, API | System demos |
| **Challenges** | Name, Impact, Urgency, Readiness, Evidence | All sessions |
| **Solutions** | Name, Type, Horizon, DVF Score, Dependencies | Phase 3 |

### What Gets Synthesized

- **Stakeholder Map** — Visual of power/sentiment landscape
- **Process Inventory** — Prioritized list with automation potential
- **Tech Landscape** — Systems and integration assessment
- **Challenge Priorities** — Ranked by I×U×R with quick wins flagged
- **Opportunity Matrix** — Solutions mapped to gaps with DVF scores
- **Patterns & Themes** — Cross-cutting insights from multiple sources

---

## Discovery Timing Guidelines

| Engagement Type | Discovery Duration | Sessions | Output Depth |
|-----------------|-------------------|----------|--------------|
| Quick Assessment | 1-2 weeks | 3-5 | High-level priorities |
| Standard Discovery | 3-4 weeks | 6-10 | Detailed analysis |
| Comprehensive Discovery | 6-8 weeks | 12-20 | Deep organizational understanding |

### Typical Session Cadence

- **Week 1:** Kickoff + 2-3 stakeholder interviews
- **Week 2:** 3-4 stakeholder interviews + 1-2 process deep dives
- **Week 3:** 2-3 system demos + remaining interviews
- **Week 4:** Synthesis + validation session

---

## Integration with Client Brain

Discovery feeds the Client Brain:

| Discovery Output | Brain Section Updated |
|------------------|----------------------|
| Key stakeholder insights | Stakeholder Map |
| Relationship signals | Relationship Health |
| Decisions made | Key Decisions Log |
| Client preferences learned | What Works / Doesn't |
| Engagement context | Active Schedule |

The Brain provides continuity; the Discovery Catalog provides depth.

---

# Follow-Up Patterns

Advanced techniques for deepening discovery conversations. Use these patterns when responses warrant deeper exploration.

> **Note:** Common topic-based follow-ups are embedded inline in [questions.md](questions.md). This section covers advanced techniques and energy-based patterns.

---

## Energy-Based Follow-Ups

Respond to emotional signals with appropriate deepening questions.

### Frustration Signals

**Detect when they:**
- Use words like "nightmare," "disaster," "terrible," "hate"
- Voice pitch changes or speaking speed increases
- Sigh or express exasperation
- Use extreme language

**Follow-Up Patterns:**
- "You mentioned [X] is a 'nightmare' — tell me more about what makes it so challenging"
- "Walk me through the last time [X] happened — what was that experience like?"
- "If you could wave a magic wand and fix one aspect of [X], what would it be?"
- "What impact does [X] have on you personally? On your team?"

**Example:**
> "The approval process is a complete nightmare"
> → "Walk me through the last approval you needed. What made it so difficult?"

---

### Pride/Excitement Signals

**Detect when they:**
- Use words like "love," "excited," "proud," "great"
- Speak faster or with more energy
- Volunteer more detail than asked

**Follow-Up Patterns:**
- "What made [X] successful?"
- "How did you overcome the challenges in getting [X] implemented?"
- "Could this approach work for [other problem area]?"

**Example:**
> "We're really proud of how our onboarding works now"
> → "What specifically makes it work so well? What did you change?"

---

### Hesitation/Uncertainty Signals

**Detect when they:**
- Pause before answering
- Use qualifiers like "I think," "maybe," "probably"
- Give vague or incomplete answers
- Change topics quickly

**Follow-Up Patterns:**
- "I noticed you paused there — is there complexity I should understand?"
- "What makes [X] tricky to explain?"
- "What would you need to know to answer that more definitively?"

**Example:**
> "Well... I think the problem is maybe with the system, but I'm not totally sure"
> → "I hear some uncertainty — what makes this hard to pin down?"

---

### Defensive Signals

**Detect when they:**
- Justify decisions or processes
- Deflect to others or external factors
- Minimize problems
- Become formal or withdrawn

**Follow-Up Patterns:**
- "I appreciate that context — help me understand what constraints you were working within"
- "If you were starting fresh today, what would you do differently?"
- "No criticism intended — I'm trying to understand how things evolved"

**Example:**
> "We had to do it that way because leadership wanted it fast"
> → "Totally understand the pressure — if you'd had more time, what would you have done differently?"

---

## Advanced Techniques

### The 5 Whys

Dig to root cause by asking "why" repeatedly (but gently):

```
Problem: "Reports are always late"
→ Why? "We have to manually compile data"
→ Why? "The systems don't talk to each other"
→ Why? "We bought them at different times without integration in mind"
→ Why? "There was no enterprise architecture function"
→ Root cause: Lack of integration strategy (not "reports are late")
```

**Softening Language:**
- "What do you think causes that?"
- "What leads to that?"
- "What's behind that?"

---

### Mirroring

Repeat the last few words as a question. Creates space for elaboration.

```
Them: "It's really frustrating when the system crashes."
You: "When it crashes...?"
Them: "Yeah, it happens maybe twice a week, usually during month-end..."
```

**Key:** Use rising intonation. Let silence do the work.

---

### Strategic Silence

After they answer, wait 3-5 seconds. They'll often add the most important part.

**When to use:**
- After they give a short answer
- When you sense they're holding back
- After emotionally charged statements

**What happens:** Discomfort fills silence. They elaborate, often with the real issue.

---

### Labeling

Name the emotion you're sensing. Validates their experience and invites elaboration.

**Patterns:**
- "It sounds like that's really frustrating."
- "It seems like there's some concern about timeline."
- "I'm sensing some hesitation about that approach."

**Key:** Start with "It sounds like..." or "It seems like..." — less confrontational than "You're frustrated."

---

### Calibrated Questions

Start with "What" or "How" instead of "Why" (less defensive):

| Instead of | Try |
|------------|-----|
| "Why did that fail?" | "What do you think contributed to that outcome?" |
| "Why do you do it that way?" | "How did you arrive at this approach?" |
| "Why is that a problem?" | "What makes this challenging?" |

---

## Quantification Patterns

When they use vague language, push for specifics:

| Vague Statement | Quantification Follow-Up |
|-----------------|-------------------------|
| "It takes too long" | "How long exactly? What's the fastest it's been?" |
| "There are too many errors" | "What's the error rate? How many per week?" |
| "It's inefficient" | "How many steps? How many people touch it?" |
| "It costs too much" | "What's the dollar amount? Per instance or per year?" |
| "It happens all the time" | "How often specifically? Daily? Weekly?" |
| "Lots of people are affected" | "How many exactly? Which teams?" |

---

## Topic Trigger Quick Reference

When they mention... dig into:

| Topic Mentioned | Quantify | Process | Impact |
|-----------------|----------|---------|--------|
| Approvals | How many steps? How long? | Who's involved? | What gets delayed? |
| Data | How many systems? | How does it flow? | What decisions suffer? |
| Time | Hours per week? | Where does it go? | What gets dropped? |
| Manual process | Volume? Error rate? | Walk through steps | What if person is out? |
| System/tool | User adoption? | How integrated? | What workarounds exist? |
| Communication | How often breaks down? | Between whom? | What's the cost? |
| Training | How long to proficiency? | What's the method? | What's retention? |
| Integration | API? File? Manual? | Who maintains? | What breaks? |

---

## Pattern Application Rules

### When to Use Advanced Techniques

| Situation | Technique |
|-----------|-----------|
| Surface-level answer | 5 Whys |
| Short answer, seems like more | Mirroring or Silence |
| Emotional statement | Labeling |
| Defensive response | Calibrated Questions |
| Vague claim | Quantification |

### When to Move On

- You've asked 2-3 follow-ups on the same topic
- They're repeating themselves
- Body language shows discomfort
- Time is limited and other gaps exist
- You have enough to inform strategy

### Pacing

- Don't machine-gun follow-ups
- Let one follow-up land before asking another
- Mix techniques — don't overuse any single approach
- Watch the clock — deep dives eat time
