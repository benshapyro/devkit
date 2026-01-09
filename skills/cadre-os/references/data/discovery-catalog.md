# Discovery Catalog Schema Reference

The Discovery Catalog is the structured data store for all client discovery findings. This document is the **single source of truth** for the Airtable schema, field definitions, valid values, and record templates.

**Last Updated:** 2024-11-29

---

## Contents

1. [Quick Reference](#quick-reference)
2. [Required Fields by Table](#required-fields-by-table)
3. [Common Errors](#common-errors)
4. [Base Information](#base-information)
5. [Table Schemas](#table-schemas)
6. [Record Templates](#record-templates)
7. [Query Patterns](#query-patterns)
8. [Workflow: Building ID Reference Maps](#workflow-building-id-reference-maps)

---

## Quick Reference

### Base & Table IDs

```
Base ID: apprH2AppvnKfUpT0
```

| Table | Table ID | Primary Field |
|-------|----------|---------------|
| 0_Clients | tbl9MiW4wWEHoNw6t | Client Name |
| 1_Discovery_Log | tblS0FNxft1FRkytp | Session Title |
| 2_People | tbl10xPpFKblRy3PL | Full Name |
| 3_Process | tblAibn7iHAvGqP1P | Process Name |
| 4_Technology | tblDdIuLzEQ2DwBYF | Tool Name |
| 5_Challenges | tblmGPfC8Y85laT6j | Challenge Name |
| 6_Solutions | tblleK2rzvC5V7sR0 | Solution Name |
| 7_Quotes | tbl6dIJFlKBqlqmp4 | Quote Text |

### Active Clients

Query dynamically (do not hardcode):

```
Airtable MCP: list_records
baseId: apprH2AppvnKfUpT0
tableId: tbl9MiW4wWEHoNw6t
filterByFormula: NOT({Engagement Status} = 'Churned')
```

Returns current clients with record IDs, engagement status, and metadata.

---

## Required Fields by Table

| Table | Required Fields |
|-------|-----------------|
| 0_Clients | Client Name |
| 1_Discovery_Log | Session Title, Date, Session Type, Summary, Client |
| 2_People | Full Name, Client |
| 3_Process | Process Name, Client |
| 4_Technology | Tool Name, Client |
| 5_Challenges | Challenge Name, Clear Explanation, Problem Type, Category, Impact, Urgency, Readiness, Client |
| 6_Solutions | Solution Name, Solution Type, Horizon, Client |
| 7_Quotes | Quote Text, Quote Type, Client |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| "Unknown field name" | Wrong field name | Check exact spelling in table schemas below |
| "Invalid multiple choice option" | Wrong select value | Use exact values from schema options |
| "Invalid value for field" | Type mismatch | Link fields need arrays: `["recXXX"]` |

---

## Base Information

The Discovery Catalog uses a relational structure where:
- **0_Clients** is the master anchor
- **1_Discovery_Log** captures each session (links to Client)
- **2-6 tables** capture entities discovered (each links to Client AND Discovery_Log)
- **7_Quotes** captures powerful stakeholder statements (links to all entities)
- Cross-links between entity tables capture relationships

### Link Architecture

```
0_Clients (anchor)
    ↓
1_Discovery_Log (sessions) ←──────────────────────────┐
    ↓                                                  │
2_People ────────→ 3_Process ←──────→ 4_Technology   │
    ↓                  ↓                    ↓         │
    └────────→ 5_Challenges ←───────────────┘         │
                    ↓                                  │
              6_Solutions ─────────────────────────────┤
                    ↓                                  │
              7_Quotes ←───────────────────────────────┘
              (links to all entity tables)
```

---

## Table Schemas

### 0_Clients

Master client list. All discovery data links back here.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Client Name | singleLineText | ✓ | Official company name |
| Industry | singleLineText | | Primary industry vertical |
| Company Size | singleSelect | | See options below |
| Annual Revenue | singleSelect | | See options below |
| Engagement Status | singleSelect | | See options below |
| AI Maturity | singleSelect | | 1-5 scale |
| Primary Contact | singleLineText | | Main POC name |
| Contact Email | email | | Primary email |
| Slack Channel | singleLineText | | Internal Slack channel |
| Brain Link | url | | Link to Client Brain Google Doc |
| Pod | singleLineText | | Assigned Cadre pod |
| AI Manager | singleLineText | | Cadre AI Manager |
| Discovery Start Date | date | | YYYY-MM-DD |
| Notes | multilineText | | Additional context |
| 1_Discovery_Log | multipleRecordLinks | | → 1_Discovery_Log (reverse) |
| 2_People | multipleRecordLinks | | → 2_People (reverse) |
| 3_Process | multipleRecordLinks | | → 3_Process (reverse) |
| 4_Technology | multipleRecordLinks | | → 4_Technology (reverse) |
| 5_Challenges | multipleRecordLinks | | → 5_Challenges (reverse) |
| 6_Solutions | multipleRecordLinks | | → 6_Solutions (reverse) |
| 7_Quotes | multipleRecordLinks | | → 7_Quotes (reverse) |

**Company Size Options:**
- `< 50 employees`
- `50-200 employees`
- `200-500 employees`
- `500-1000 employees`
- `1000-5000 employees`
- `5000+ employees`

**Annual Revenue Options:**
- `< $10M`
- `$10M - $50M`
- `$50M - $100M`
- `$100M - $500M`
- `$500M - $1B`
- `$1B - $2B`
- `> $2B`

**Engagement Status Options:**
- `Discovery`
- `Strategy`
- `Implementation`
- `Optimization`
- `Paused`
- `Churned`

**AI Maturity Options:**
- `1 - No AI`
- `2 - Exploring`
- `3 - Piloting`
- `4 - Scaling`
- `5 - Optimizing`

| Change History | multilineText | | Append-only log of changes (see format below) |

---

### 1_Discovery_Log

Session records for all discovery activities.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Session Title | singleLineText | ✓ | Descriptive session name |
| Date | date | ✓ | YYYY-MM-DD format |
| Session Type | singleSelect | ✓ | See options below |
| Cadre Attendees | multilineText | | Cadre team members present |
| Client Attendees | multilineText | | Client participants present |
| Duration (minutes) | number | | Length of session |
| Key Topics | multilineText | | Main topics discussed |
| Summary | multilineText | ✓ | Executive summary |
| Confidence | singleSelect | | See options below |
| Transcript Link | url | | Link to Fireflies transcript |
| Recording Link | url | | Link to meeting recording |
| Follow-up Items | multilineText | | Questions to ask next time |
| Notes | multilineText | | Additional observations |
| Client | multipleRecordLinks | ✓ | → 0_Clients |
| People Discovered | multipleRecordLinks | | → 2_People |
| Processes Discovered | multipleRecordLinks | | → 3_Process |
| Technologies Discovered | multipleRecordLinks | | → 4_Technology |
| Challenges Discovered | multipleRecordLinks | | → 5_Challenges |
| Solutions Proposed | multipleRecordLinks | | → 6_Solutions |
| Quotes Captured | multipleRecordLinks | | → 7_Quotes |
| Change History | multilineText | | Append-only log of changes (see format below) |

**Session Type Options:**
- `Kickoff`
- `Interview`
- `Workshop`
- `Document Review`
- `Observation`
- `Follow-up`
- `Presentation`
- `System Demo`
- `Validation`

**Mapping:** "Process Deep Dive" → use `Observation`

**Confidence Options:**
- `1 - Low`
- `2 - Medium-Low`
- `3 - Medium`
- `4 - Medium-High`
- `5 - High`

---

### 2_People

Stakeholder profiles from discovery.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Full Name | singleLineText | ✓ | First and last name |
| Title | singleLineText | | Job title |
| Department | singleLineText | | Department or team |
| Power (1-10) | number | | Influence: 10=CEO, 5=Manager, 1=IC |
| Sentiment (1-10) | number | | Support: 10=Champion, 5=Neutral, 1=Blocker |
| Stakeholder Type | singleSelect | | See options below |
| Champion Potential | singleSelect | | Yes / Maybe / No |
| Key Insights | multilineText | | Important discoveries |
| Concerns | multilineText | | Fears, risks, objections |
| Personal Motivators | multilineText | | Career goals, pain points |
| Engagement Strategy | multilineText | | How to work with them |
| AI Readiness (1-5) | number | | 1=No AI skills, 5=Expert |
| ADKAR Stage | singleSelect | | See options below |
| Influence Network | multilineText | | Who they influence/are influenced by |
| Prior Change Experience | multilineText | | History with change initiatives |
| Email | email | | Contact email |
| Phone | phoneNumber | | Contact phone |
| Last Interaction | date | | Most recent interaction date |
| Notes | multilineText | | Additional context |
| 1_Discovery_Log | multipleRecordLinks | | → 1_Discovery_Log |
| Client | multipleRecordLinks | ✓ | → 0_Clients |
| Related Processes | multipleRecordLinks | | → 3_Process |
| Related Technologies | multipleRecordLinks | | → 4_Technology |
| Related Challenges | multipleRecordLinks | | → 5_Challenges |
| Change History | multilineText | | Append-only log of changes (see format below) |

**Stakeholder Type Options:**
- `Champion`
- `Decision-Maker`
- `Influencer`
- `User`
- `Affected`
- `Neutral`
- `Blocker`

**Champion Potential Options:**
- `Yes`
- `Maybe`
- `No`

**ADKAR Stage Options:**
- `Awareness`
- `Desire`
- `Knowledge`
- `Ability`
- `Reinforcement`

---

### 3_Process

Workflow and process documentation.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Process Name | singleLineText | ✓ | Descriptive workflow name |
| Department | singleLineText | | Primary department responsible |
| Process Owner | singleLineText | | Person accountable |
| Frequency/Month | number | | Times per month this runs |
| Hours per Instance | number | | Hours each run (1 decimal) |
| Monthly Hours Total | number | | Frequency × Hours |
| Labor Roles Involved | multilineText | | Job titles involved |
| Weighted Labor Rate ($/hr) | currency | | Blended hourly rate |
| Monthly Labor Cost | currency | | Monthly Hours × Rate |
| Annual Labor Cost | currency | | Monthly × 12 |
| AI/Automation Readiness (1-5) | number | | 1=Hard, 5=Easy |
| Accuracy (1-5) | number | | 1=Many errors, 5=Accurate |
| Efficiency (1-5) | number | | 1=Wasteful, 5=Efficient |
| Data Quality (1-5) | number | | 1=Messy, 5=Clean |
| Error Rate (%) | percent | | Percentage rework |
| Rework Cost ($/month) | currency | | Monthly error cost |
| Bottleneck? | checkbox | | Is this a constraint? |
| Redesign Opportunity? | checkbox | | Redesign vs automate? |
| System Span | number | | Count of systems touched |
| Context Type | singleSelect | | Formal / Informal / Tribal |
| Decomposition Level | singleSelect | | Workflow / Process / Task / Subtask |
| Peak Period | singleLineText | | When is it busiest? |
| Time Variance | singleSelect | | High / Medium / Low |
| Downstream Impact | multilineText | | What breaks if this fails? |
| Accuracy Notes | multilineText | | Error pattern details |
| Efficiency Notes | multilineText | | Waste details |
| Automation Notes | multilineText | | Automation potential |
| Notes | multilineText | | Additional context |
| 1_Discovery_Log | multipleRecordLinks | | → 1_Discovery_Log |
| Client | multipleRecordLinks | ✓ | → 0_Clients |
| 2_People | multipleRecordLinks | | → 2_People |
| Related Technologies | multipleRecordLinks | | → 4_Technology |
| Related Challenges | multipleRecordLinks | | → 5_Challenges |
| Proposed Solutions | multipleRecordLinks | | → 6_Solutions |
| Change History | multilineText | | Append-only log of changes (see format below) |

**Context Type Options:**
- `Formal`
- `Informal`
- `Tribal`

**Decomposition Level Options:**
- `Workflow`
- `Process`
- `Task`
- `Subtask`

**Time Variance Options:**
- `High`
- `Medium`
- `Low`

---

### 4_Technology

Technology stack inventory.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Tool Name | singleLineText | ✓ | Name of tool/system |
| Vendor | singleLineText | | Company that makes it |
| Status | singleSelect | | Active / Planned / Evaluating / Sunsetting / Inactive |
| Primary JTBD | singleLineText | | Main job this tool does |
| Secondary JTBD | multilineText | | Other jobs it does |
| Department | singleLineText | | Primary department |
| User Count | number | | Number of users |
| Annual Cost | currency | | Yearly spend |
| Pricing Model | singleSelect | | See options below |
| Contract End Date | date | | Renewal date |
| Satisfaction (1-10) | number | | User happiness |
| Reliability (1-10) | number | | Uptime/stability |
| Switching Cost | singleSelect | | High / Medium / Low |
| Integration Quality | singleSelect | | High / Medium / Low / None |
| Integrates With | multilineText | | Connected systems |
| Data Flow | multilineText | | How data moves in/out |
| API | checkbox | | Has API? |
| API Type | singleSelect | | REST / GraphQL / SOAP / Webhooks / Other |
| API Quality (1-5) | number | | Doc quality and reliability |
| MCP Support | checkbox | | Model Context Protocol? |
| OpenAI Integration | singleSelect | | Official / Community / None |
| Claude Integration | singleSelect | | Official / Community / None |
| Gemini Integration | singleSelect | | Official / Community / None |
| Copilot Integration | singleSelect | | Official / Community / None |
| Recommendation | singleSelect | | Keep / Optimize / Evaluate / Replace |
| Security/Compliance | multilineText | | SOC2, HIPAA, GDPR, etc. |
| Data Retention | singleLineText | | How long data stored |
| Champion | singleLineText | | Internal advocate |
| Notes | multilineText | | Additional context |
| 1_Discovery_Log | multipleRecordLinks | | → 1_Discovery_Log |
| Client | multipleRecordLinks | ✓ | → 0_Clients |
| 2_People | multipleRecordLinks | | → 2_People |
| 3_Process | multipleRecordLinks | | → 3_Process |
| Related Challenges | multipleRecordLinks | | → 5_Challenges |
| Proposed Solutions | multipleRecordLinks | | → 6_Solutions |
| Change History | multilineText | | Append-only log of changes (see format below) |

**Status Options:**
- `Active`
- `Planned`
- `Evaluating`
- `Sunsetting`
- `Inactive`

**Pricing Model Options:**
- `Per User/Month`
- `Per User/Year`
- `Flat Monthly`
- `Flat Annual`
- `Usage-Based`
- `One-Time`
- `Free`

**Switching Cost Options:**
- `High`
- `Medium`
- `Low`

**Integration Quality Options:**
- `High`
- `Medium`
- `Low`
- `None`

**Recommendation Options:**
- `Keep`
- `Optimize`
- `Evaluate`
- `Replace`

---

### 5_Challenges

Problems, gaps, and pain points discovered.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Challenge Name | singleLineText | ✓ | Short descriptive name |
| Clear Explanation | multilineText | ✓ | Plain-English description |
| Problem Type | singleSelect | ✓ | See options below |
| Category | singleSelect | ✓ | See options below |
| Annual Cost Impact | currency | | Estimated yearly cost |
| Cost Calculation | multilineText | | Show your work |
| Impact (1-5) | number | ✓ | 1=Minor, 5=Critical |
| Urgency (1-5) | number | ✓ | 1=Can wait, 5=Immediate |
| Readiness (1-5) | number | ✓ | 1=Blockers, 5=Ready now |
| Priority Score | number | | Impact × Urgency × Readiness |
| Quick Win? | checkbox | | High readiness + high impact |
| Root Cause Analysis | multilineText | | 5 Whys or fishbone |
| Evidence/Quotes | multilineText | | Direct quotes/data |
| Risk if Unaddressed | multilineText | | What happens if ignored |
| Stakeholders Affected | multilineText | | Who feels the pain |
| Discovery Source | singleSelect | | See options below |
| Confidence | singleSelect | | 1-5 scale |
| Status | singleSelect | | See options below |
| Notes | multilineText | | Additional context |
| 1_Discovery_Log | multipleRecordLinks | | → 1_Discovery_Log |
| Client | multipleRecordLinks | ✓ | → 0_Clients |
| 2_People | multipleRecordLinks | | → 2_People |
| 3_Process | multipleRecordLinks | | → 3_Process |
| 4_Technology | multipleRecordLinks | | → 4_Technology |
| Proposed Solutions | multipleRecordLinks | | → 6_Solutions |
| Change History | multilineText | | Append-only log of changes (see format below) |

**Problem Type Options:**
- `Root Cause`
- `Symptom`
- `Constraint`
- `Risk`
- `Opportunity Cost`

**Category Options:**
- `Process`
- `Technology`
- `People`
- `Data`
- `Strategy`
- `Culture`

**Discovery Source Options:**
- `Interview`
- `Workshop`
- `Observation`
- `Document Review`
- `Data Analysis`
- `Self-Reported`

**Confidence Options:**
- `1 - Low`
- `2 - Medium-Low`
- `3 - Medium`
- `4 - Medium-High`
- `5 - High`

**Status Options:**
- `Identified`
- `Validated`
- `Solving`
- `Resolved`
- `Won't Fix`

---

### 6_Solutions

Proposed solutions and opportunities.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Solution Name | singleLineText | ✓ | Short descriptive name |
| User Story | multilineText | | As a [role], I want... |
| Solution Type | singleSelect | ✓ | See options below |
| Technical Approach | multilineText | | How to build/implement |
| Horizon | singleSelect | ✓ | See options below |
| Implementation Weeks | number | | Weeks to implement |
| Cadre Hours | number | | Cadre consulting hours |
| Client Hours | number | | Client team hours |
| Implementation Cost | currency | | Total cost |
| Annual Savings | currency | | Yearly savings |
| Annual Value Add | currency | | New revenue/value |
| ROI Year 1 | percent | | (Savings + Value - Cost) / Cost |
| Payback Months | number | | Months until payoff |
| Desirability (1-5) | number | | 1=Nobody wants, 5=Everyone |
| Viability (1-5) | number | | 1=Bad ROI, 5=Great ROI |
| Feasibility (1-5) | number | | 1=Very hard, 5=Easy |
| DVF Score | number | | D × V × F |
| Complexity | singleSelect | | Low / Medium / High |
| Risk Level | singleSelect | | Low / Medium / High |
| Risk Factors | multilineText | | What could go wrong |
| Dependencies | multilineText | | What's needed first |
| Success Criteria | multilineText | | How we know it worked |
| Change Mgmt Effort | singleSelect | | Low / Medium / High |
| Training Required | multilineText | | What training needed |
| Priority | singleSelect | | See options below |
| Recommendation | multilineText | | Cadre's recommendation |
| Status | singleSelect | | See options below |
| Notes | multilineText | | Additional context |
| 1_Discovery_Log | multipleRecordLinks | | → 1_Discovery_Log |
| Client | multipleRecordLinks | ✓ | → 0_Clients |
| 3_Process | multipleRecordLinks | | → 3_Process |
| 4_Technology | multipleRecordLinks | | → 4_Technology |
| 5_Challenges | multipleRecordLinks | | → 5_Challenges |
| Change History | multilineText | | Append-only log of changes (see format below) |

**Solution Type Options:**
- `Process Redesign`
- `Automation`
- `AI Enhancement`
- `New Tool`
- `Integration`
- `Training`
- `Org Change`

**Horizon Options:**
- `Now (0-3 months)`
- `Next (3-6 months)`
- `Later (6-12 months)`
- `Future (12+ months)`

**Complexity Options:**
- `Low`
- `Medium`
- `High`

**Risk Level Options:**
- `Low`
- `Medium`
- `High`

**Change Mgmt Effort Options:**
- `Low`
- `Medium`
- `High`

**Priority Options:**
- `1 - Critical`
- `2 - High`
- `3 - Medium`
- `4 - Low`
- `5 - Nice to Have`

**Status Options:**
- `Proposed`
- `Approved`
- `In Progress`
- `Completed`
- `On Hold`
- `Rejected`

---

### 7_Quotes

Powerful stakeholder statements captured during discovery — the voice of the client.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Quote Text | multilineText | ✓ | The exact words spoken |
| Speaker Name | singleLineText | | Who said it (text for flexibility) |
| Speaker Title | singleLineText | | Role/title at time of quote |
| Date Captured | date | | YYYY-MM-DD when this was said |
| Session Context | multilineText | | What was being discussed |
| Quote Type | singleSelect | ✓ | See options below |
| Dimension | singleSelect | | Which discovery dimension |
| Emotional Tone | singleSelect | | Sentiment expressed |
| Power Rating (1-5) | number | | 5 = Executive presentation worthy |
| Verified | checkbox | | Has accuracy been confirmed |
| Used In | multilineText | | Where quote has been used |
| Notes | multilineText | | Additional context |
| Change History | richText | | Audit trail of changes |
| Client | multipleRecordLinks | ✓ | → 0_Clients |
| Discovery Session | multipleRecordLinks | | → 1_Discovery_Log |
| Speaker | multipleRecordLinks | | → 2_People (if in People table) |
| Related People | multipleRecordLinks | | → 2_People (others mentioned) |
| Related Processes | multipleRecordLinks | | → 3_Process |
| Related Technology | multipleRecordLinks | | → 4_Technology |
| Related Challenges | multipleRecordLinks | | → 5_Challenges |
| Related Solutions | multipleRecordLinks | | → 6_Solutions |

**Quote Type Options:**
- `Pain Point` — Expresses frustration or problem
- `Insight` — Reveals non-obvious information
- `Opportunity` — Identifies potential improvement
- `Vision` — Describes desired future state
- `Objection` — Raises concern or resistance
- `Endorsement` — Expresses support or enthusiasm
- `Question` — Reveals gap in understanding

**Dimension Options:**
- `People`
- `Process`
- `Technology`
- `Challenges`
- `Solutions`
- `General`

**Emotional Tone Options:**
- `Frustration`
- `Excitement`
- `Concern`
- `Neutral`
- `Hope`
- `Pride`

---

## Change History Format

All tables include a `Change History` field for tracking modifications over time. This is an append-only log — never delete or modify existing entries.

### Format

Each entry follows this structure:
```
[YYYY-MM-DD | Session: Session Title] Action. Field: old → new (context)
```

### Entry Types

**Record Creation:**
```
[2024-12-01 | Session: CES Kickoff] Created. Power: 7, Sentiment: 5, Type: Influencer
```

**Field Updates:**
```
[2024-12-08 | Session: Interview with Sarah] Sentiment: 5 → 7 (showed enthusiasm about AI pilot)
```

**Multiple Changes:**
```
[2024-12-15 | Session: Validation] Sentiment: 7 → 8, Champion Potential: Maybe → Yes (volunteered to lead pilot)
```

**Status Changes:**
```
[2024-12-20 | Session: Strategy Review] Status: Identified → Validated (confirmed by 3 stakeholders)
```

### Guidelines

1. **Always include the session** — Links the change to its source
2. **Note what changed** — Use `field: old → new` format
3. **Add context in parentheses** — Why did this change?
4. **Append only** — Never edit previous entries
5. **One entry per session** — Combine all changes from a single session

### When to Update

Update Change History when:
- Creating a new record (note initial values for key fields)
- Modifying scored fields (Power, Sentiment, Impact, Urgency, etc.)
- Changing Status
- Updating Stakeholder Type or other classification fields
- Adding significant new information to text fields

Do NOT update Change History for:
- Adding linked records (these are tracked by the links themselves)
- Minor text edits or typo fixes
- Initial data entry during the same session

---

## Record Templates

Copy-paste-ready JSON for creating records via Airtable MCP.

### Discovery Log Entry

```json
{
  "Session Title": "",
  "Date": "YYYY-MM-DD",
  "Session Type": "Interview",
  "Cadre Attendees": "",
  "Client Attendees": "",
  "Duration (minutes)": 0,
  "Key Topics": "",
  "Summary": "",
  "Confidence": "5 - High",
  "Follow-up Items": "",
  "Client": ["rec_CLIENT_ID"],
  "Change History": "[YYYY-MM-DD | Session: Session Title] Created. Type: Interview, Attendees: X"
}
```

**Session Type must be one of:** `Kickoff`, `Interview`, `Workshop`, `Document Review`, `Observation`, `Follow-up`, `Presentation`, `System Demo`, `Validation`

**Mapping:** "Process Deep Dive" → use `Observation`

### Person Record

```json
{
  "Full Name": "",
  "Title": "",
  "Department": "",
  "Power (1-10)": 5,
  "Sentiment (1-10)": 5,
  "Stakeholder Type": "Influencer",
  "Champion Potential": "Maybe",
  "Key Insights": "",
  "ADKAR Stage": "Awareness",
  "Client": ["rec_CLIENT_ID"],
  "1_Discovery_Log": ["rec_SESSION_ID"],
  "Change History": "[YYYY-MM-DD | Session: Session Title] Created. Power: 5, Sentiment: 5, Type: Influencer"
}
```

**Stakeholder Type must be one of:** `Champion`, `Decision-Maker`, `Influencer`, `User`, `Affected`, `Neutral`, `Blocker`

### Process Record

```json
{
  "Process Name": "",
  "Department": "",
  "Process Owner": "",
  "Frequency/Month": 0,
  "Hours per Instance": 0,
  "AI/Automation Readiness (1-5)": 3,
  "Context Type": "Informal",
  "Notes": "",
  "Client": ["rec_CLIENT_ID"],
  "1_Discovery_Log": ["rec_SESSION_ID"],
  "Change History": "[YYYY-MM-DD | Session: Session Title] Created. Readiness: 3, Context: Informal"
}
```

### Technology Record

```json
{
  "Tool Name": "",
  "Vendor": "",
  "Status": "Active",
  "Primary JTBD": "",
  "Department": "",
  "Satisfaction (1-10)": 5,
  "Integration Quality": "Medium",
  "Notes": "",
  "Client": ["rec_CLIENT_ID"],
  "1_Discovery_Log": ["rec_SESSION_ID"],
  "Change History": "[YYYY-MM-DD | Session: Session Title] Created. Status: Active, Satisfaction: 5"
}
```

**Integration Quality must be one of:** `High`, `Medium`, `Low`, `None`

### Challenge Record

```json
{
  "Challenge Name": "",
  "Clear Explanation": "",
  "Problem Type": "Root Cause",
  "Category": "Process",
  "Impact (1-5)": 3,
  "Urgency (1-5)": 3,
  "Readiness (1-5)": 3,
  "Priority Score": 27,
  "Evidence/Quotes": "",
  "Risk if Unaddressed": "",
  "Stakeholders Affected": "",
  "Discovery Source": "Interview",
  "Confidence": "5 - High",
  "Status": "Identified",
  "Client": ["rec_CLIENT_ID"],
  "1_Discovery_Log": ["rec_SESSION_ID"],
  "Change History": "[YYYY-MM-DD | Session: Session Title] Created. Impact: 3, Urgency: 3, Readiness: 3, Priority: 27, Status: Identified"
}
```

**Problem Type must be one of:** `Root Cause`, `Symptom`, `Constraint`, `Risk`, `Opportunity Cost`

**Category must be one of:** `Process`, `Technology`, `People`, `Data`, `Strategy`, `Culture`

### Solution Record

```json
{
  "Solution Name": "",
  "User Story": "As a [role], I want [capability] so that [benefit]",
  "Solution Type": "AI Enhancement",
  "Technical Approach": "",
  "Horizon": "Now (0-3 months)",
  "Desirability (1-5)": 4,
  "Viability (1-5)": 4,
  "Feasibility (1-5)": 4,
  "DVF Score": 64,
  "Complexity": "Medium",
  "Risk Level": "Medium",
  "Dependencies": "",
  "Success Criteria": "",
  "Priority": "3 - Medium",
  "Recommendation": "",
  "Status": "Proposed",
  "Client": ["rec_CLIENT_ID"],
  "1_Discovery_Log": ["rec_SESSION_ID"],
  "5_Challenges": ["rec_CHALLENGE_ID"],
  "Change History": "[YYYY-MM-DD | Session: Session Title] Created. DVF: 64 (D:4 V:4 F:4), Horizon: Now, Status: Proposed"
}
```

**Solution Type must be one of:** `Process Redesign`, `Automation`, `AI Enhancement`, `New Tool`, `Integration`, `Training`, `Org Change`

**Horizon must be one of:** `Now (0-3 months)`, `Next (3-6 months)`, `Later (6-12 months)`, `Future (12+ months)`

### Quote Record

```json
{
  "Quote Text": "",
  "Speaker Name": "",
  "Speaker Title": "",
  "Date Captured": "YYYY-MM-DD",
  "Session Context": "",
  "Quote Type": "Insight",
  "Dimension": "General",
  "Emotional Tone": "Neutral",
  "Power Rating (1-5)": 3,
  "Verified": false,
  "Notes": "",
  "Client": ["rec_CLIENT_ID"],
  "Discovery Session": ["rec_SESSION_ID"],
  "Change History": "[YYYY-MM-DD | Session: Session Title] Created. Type: Insight, Power: 3"
}
```

**Quote Type must be one of:** `Pain Point`, `Insight`, `Opportunity`, `Vision`, `Objection`, `Endorsement`, `Question`

**Dimension must be one of:** `People`, `Process`, `Technology`, `Challenges`, `Solutions`, `General`

**Emotional Tone must be one of:** `Frustration`, `Excitement`, `Concern`, `Neutral`, `Hope`, `Pride`

---

## Query Patterns

### Get All Entities for a Client

```python
# Get client record ID first
client = list_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tbl9MiW4wWEHoNw6t",  # 0_Clients
    filterByFormula="{Client Name} = '[ClientName]'"
)
CLIENT_ID = client[0]["id"]

# Then query each entity table
list_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tbl10xPpFKblRy3PL",  # 2_People
    filterByFormula="{Client} = '[ClientName]'"
)
```

### Get High-Priority Challenges

```python
list_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tblmGPfC8Y85laT6j",  # 5_Challenges
    filterByFormula="AND({Client} = '[ClientName]', {Priority Score} >= 64)"
)
```

### Get Recent Discovery Sessions

```python
list_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tblS0FNxft1FRkytp",  # 1_Discovery_Log
    filterByFormula="{Client} = '[ClientName]'",
    sort=[{"field": "Date", "direction": "desc"}],
    maxRecords=5
)
```

### Search for a Person

```python
search_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tbl10xPpFKblRy3PL",  # 2_People
    searchTerm="Karl"
)
```

---

## Workflow: Building ID Reference Maps

Before creating or updating records during a debrief, build a lookup map of all existing record IDs for the client. This enables:
- UPDATE vs CREATE decisions
- Proper linking between records
- Avoiding duplicate records

### Step 1: Get Client ID

```python
result = list_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tbl9MiW4wWEHoNw6t",
    filterByFormula="{Client Name} = '[CLIENT_NAME]'"
)
CLIENT_ID = result[0]["id"]
```

### Step 2: Build Entity Maps

Query each table and build name→ID maps:

```python
# People
people = list_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tbl10xPpFKblRy3PL",
    filterByFormula="{Client} = '[CLIENT_NAME]'"
)
PEOPLE_MAP = {r["fields"]["Full Name"]: r["id"] for r in people}
# → {"Karl Winters": "recMcgxlLFZMrDElU", "Sarah Walker": "reccC8R1JieIIDhDl", ...}

# Processes
processes = list_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tblAibn7iHAvGqP1P",
    filterByFormula="{Client} = '[CLIENT_NAME]'"
)
PROCESS_MAP = {r["fields"]["Process Name"]: r["id"] for r in processes}

# Technology
tech = list_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tblDdIuLzEQ2DwBYF",
    filterByFormula="{Client} = '[CLIENT_NAME]'"
)
TECH_MAP = {r["fields"]["Tool Name"]: r["id"] for r in tech}

# Challenges
challenges = list_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tblmGPfC8Y85laT6j",
    filterByFormula="{Client} = '[CLIENT_NAME]'"
)
CHALLENGE_MAP = {r["fields"]["Challenge Name"]: r["id"] for r in challenges}

# Solutions
solutions = list_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tblleK2rzvC5V7sR0",
    filterByFormula="{Client} = '[CLIENT_NAME]'"
)
SOLUTION_MAP = {r["fields"]["Solution Name"]: r["id"] for r in solutions}

# Quotes
quotes = list_records(
    baseId="apprH2AppvnKfUpT0",
    tableId="tbl6dIJFlKBqlqmp4",
    filterByFormula="{Client} = '[CLIENT_NAME]'"
)
QUOTE_MAP = {r["fields"]["Quote Text"][:50]: r["id"] for r in quotes}
# Note: Uses first 50 chars of quote text as key
```

### Step 3: Use Maps When Creating Records

When extracting entities from a transcript:
1. Check if name exists in map → **UPDATE** existing record
2. If name doesn't exist → **CREATE** new record
3. Use IDs from maps for linking fields

Example:
```python
# New challenge needs to link to existing person
challenge_fields = {
    "Challenge Name": "No Net Working Capital Visibility",
    "Client": [CLIENT_ID],
    "2_People": [PEOPLE_MAP["Karl Winters"]]  # Use lookup
}
```

### Record Creation Order

To ensure proper linking:

1. **Create Discovery Log entry first** → get SESSION_ID
2. **Create new People records** → add to PEOPLE_MAP
3. **Create new Process records** → add to PROCESS_MAP
4. **Create new Technology records** → add to TECH_MAP
5. **Create new Challenges** → link to SESSION_ID, PEOPLE, PROCESS, TECH
6. **Create new Solutions** → link to SESSION_ID, CHALLENGES
7. **Create new Quotes** → link to SESSION_ID, SPEAKER, CHALLENGES, SOLUTIONS
8. **Update Discovery Log** → add links to all created records

---

## Common Errors & Fixes

### "Unknown field name"
Field name doesn't match schema exactly. Check spelling and case.
- ❌ `Attendees`
- ✓ `Client Attendees`

### "Invalid multiple choice option"
Select value not in allowed options. Check options list above.
- ❌ `"Session Type": "Process Deep Dive"` → use "Observation"
- ✓ `"Session Type": "Observation"`

### "Invalid value for field"
Usually a type mismatch.
- Link fields need arrays: `["recXXX"]` not `"recXXX"`
- Numbers need integers: `5` not `"5"`
- Dates need ISO format: `"2024-11-22"` not `"Nov 22"`

### "Insufficient permissions to create new select option"
Select value not in allowed options list. Double-check exact string.
- ❌ `"Integration Quality": "Limited"`
- ✓ `"Integration Quality": "Low"`
