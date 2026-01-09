# Tech Stack Survey SOP

How Cadre captures and researches a client's technology inventory.

---

## What is the Tech Stack Survey?

An Excel-based inventory of all tools and systems a client uses. Captures what they have, who owns it, what it costs, and how it connects to other tools.

**Purpose:** Inform integration and automation recommendations. You can't suggest "connect Salesforce to QuickBooks" if you don't know they use both.

**Two parts:**
- **Client fills columns 1-7** — Tool name, purpose, department, owner, users, cost, vendor (stuff only they know)
- **Cadre fills columns 8+** — API availability, integrations, connection methods (stuff we research)

---

## Step-by-Step Instructions

### Part A: Sending the Survey

#### Step A1: Trigger
**When:** Every engagement, at or around kickoff

**Who:** AI Manager or whoever is leading the engagement

#### Step A2: Get the Template

**Option 1 — From Claude (preferred):**
1. Open Claude
2. Type: `/techstack template`
3. Claude generates the Tech Stack Survey Excel file
4. Download the file

**Option 2 — From Google Drive (backup):**
1. Go to: `Cadre Team Drive / Templates / Tech Stack Survey Template.xlsx`
2. Download or make a copy

#### Step A3: Identify the Right Client Contact

During discovery (or kickoff), ask:
> "Who on your team knows your tech stack best — tools, costs, who owns what?"

**Document the answer.** This is the person you'll send the survey to.

**Add this question to your discovery question bank under Technology.**

Common answers:
- IT Director / Systems Admin (knows tools + technical details)
- Finance / Accounting (knows costs)
- Operations lead (knows what's actually used day-to-day)
- Your champion (can delegate internally)

#### Step A4: Send the Survey

1. Email the Tech Stack Survey Excel to the identified contact
2. CC your champion if they're a different person
3. Use this framing:

**Subject:** Tech Stack Survey — [Client Name]

**Body:**
> Hi [Name],
>
> As part of our discovery, we're mapping out your technology stack to identify integration and automation opportunities.
>
> Attached is a short survey. Could you fill in columns A through G for each tool your team uses? We'll research the technical details (API, integrations, etc.) on our end.
>
> If you can get this back to us within the week, that would be great — the sooner we have it, the more we can prepare for our next conversation.
>
> Questions? Just reply to this email.
>
> Thanks!

#### Step A5: Track It

1. Note in ClickUp (or your project tracker) that survey was sent
2. Set a reminder to follow up in 5 business days if not received

---

### Part B: Processing the Response

#### Step B1: Save the Completed Survey

1. When client returns the survey, download it
2. Save to: `Cadre Team Drive / Clients / [Client Name] / Tech Stack Survey.xlsx`

#### Step B2: Review Client's Entries

Open the file and check:
- Did they fill in columns A-G? (Tool Name, Purpose, Department, Owner, Users, Cost, Vendor)
- Are there obvious gaps or questions?
- Did they include all the tools you've heard mentioned in discovery?

**Don't send it back for corrections.** Accept what you get.

#### Step B3: Run Tech Stack Research

1. Open Claude (client project)
2. Upload the completed survey
3. Type: `/techstack research [Client Name]`

**Example:** `/techstack research Acme Corp`

Claude will:
- Look up API availability for each tool
- Research common integrations
- Check Cadre's Tools Library for known info
- Fill in columns 8+ (API, Upstream, Downstream, Connection Method, etc.)

#### Step B4: Review Claude's Research

Claude outputs the completed survey with research added.

**Your job:**
1. Spot-check the research (especially for obscure tools)
2. Mark confidence level: High (verified), Medium (likely), Low (uncertain)
3. Flag anything that looks wrong

#### Step B5: Handle Missing Tools

If you know the client uses a tool they didn't list:

1. Add it to the survey
2. Mark source as "Research (unconfirmed)"
3. Add note: "Confirm with client"

**Example:**
| Tool | Source | Notes |
|------|--------|-------|
| Slack | Research (unconfirmed) | Found via LinkedIn job posting. Confirm with client. |

#### Step B6: Confirm Missing Tools

In your next discovery call, ask:
> "We saw you might be using [Tool] — is that right?"

Update the survey based on their answer.

#### Step B7: Save Completed Survey

1. Save the researched survey to Drive (same location, overwrite the client's version)
2. Upload to Claude Project Knowledge
3. Update ClickUp to mark survey as complete

---

### Part C: Handling Partial Responses

**If client only fills in some tools:**

1. Accept what you get
2. Research what you can
3. In the next discovery call, ask about specific gaps:
   > "You mentioned Salesforce but we didn't see a marketing automation tool — do you use one?"

**Never say:** "This is incomplete, please fill in the rest."

**Do say:** "Thanks for this. Quick question when we talk next — what do you use for X?"

---

### Part D: Handling Unknown Details

**For public info (API, integrations, vendor):**
- Cadre researches independently
- Don't bother client with questions we can answer ourselves

**For sensitive info (costs, internal ownership):**
- Flag for follow-up in next call
- Or ask champion to check internally

**Research priority:**
1. Check Cadre's Tools Library first (common tools already documented)
2. Check vendor documentation
3. Web search: "[Tool name] API" or "[Tool A] [Tool B] integration"
4. If still unknown after 5 minutes, mark as "Unknown" and move on

---

### Part E: Generating Artifacts

**When:** Before client presentations, deliverable deadlines, or anytime someone needs a visual summary of the tech stack.

#### Step E1: Ensure Data is Ready
1. Open the client's Claude Project
2. Confirm `Tech Stack Survey.xlsx` is uploaded to Project Knowledge
3. If survey was recently updated, re-upload the latest version

#### Step E2: Generate Tech Stack Overview
1. In Claude, type: `/artifact overview [Client Name]`
2. Claude generates an HTML artifact showing:
   - Summary stats (total tools, API-ready, annual spend, departments)
   - Tools by department breakdown
   - Full inventory table with owners, costs, API status

#### Step E3: Generate Integration Map
1. In Claude, type: `/artifact map [Client Name]`
2. Claude generates an artifact showing:
   - Visual diagram of tool connections
   - Click nodes to see upstream/downstream relationships
   - Color-coded by category

**Note:** If Claude generates JSX, ask: "Convert this to HTML for the Client Portal."

#### Step E4: Review and Revise
1. Review the artifact for accuracy
2. If something's wrong, tell Claude what to fix:
   - "The annual cost for Salesforce should be $120,000"
   - "Add Slack to the company-wide tools"
   - "Remove the Legacy CRM — they sunsetted it"
3. Claude revises the artifact
4. Repeat until it looks right

#### Step E5: Peer Review (Client-Facing Only)
If this artifact is going in front of the client:
1. Slack a teammate: "Quick review? [link to artifact]"
2. They spend 2-5 minutes checking for errors
3. Make any final fixes

*Skip this step for internal-only use.*

#### Step E6: Publish and Share
1. Click "Publish" on the artifact in Claude
2. Copy the shareable link
3. Use this link when presenting to client or sharing internally

#### Step E7: Add to Client Portal
1. Copy the HTML code from the artifact
2. Open the Client Portal
3. Navigate to the client's space
4. Paste the HTML into the code editor
5. Save

#### Step E8: (Optional) Update Source Data
If you made changes in the artifact that should be reflected in the source:
1. Open `Tech Stack Survey.xlsx`
2. Make the same updates
3. Re-upload to Claude Project Knowledge

*This keeps source and artifact in sync for future regeneration.*

---

### Part F: Connecting to Discovery Catalog

**Tech Stack Survey and Discovery Catalog are separate systems.**

| Tech Stack Survey | Discovery Catalog |
|-------------------|-------------------|
| Inventory (facts) | Findings (insights) |
| "What they have" | "What matters" |
| Reference data | Decision-useful data |

**When do things move from Survey to Catalog?**

When you identify an **issue or opportunity** related to a tool, create a catalog entry.

**Example:**
- **Survey fact:** "They use Salesforce and QuickBooks"
- **Catalog entry:** "Salesforce and QuickBooks aren't integrated — sales has no visibility into payment status"

The survey tells you what exists. The catalog captures what to do about it.

---

## Key Rules

### Who Fills What

| Columns | Who | What |
|---------|-----|------|
| A-G | Client | Tool Name, Purpose, Department, Owner, Users, Cost, Vendor |
| H+ | Cadre (Claude) | API, Upstream, Downstream, Connection Method, Integration Notes |

### Integration Detail Level

**Focus on primary connections** — where the main data flows.

If Salesforce connects to 12 systems, you don't need all 12. You need:
- CRM → Finance (quotes to invoices)
- CRM → Marketing (leads and campaigns)
- CRM → Support (customer history)

**Skip:** One-off integrations, rarely-used connections, things that don't affect recommendations.

### When Is It "Done"?

**When you can confidently make integration/automation recommendations.**

Ask yourself: "Do I know enough about their tech stack to advise them?"

**"Done" checklist:**
- [ ] Core business tools identified (CRM, Finance, Marketing, Ops)
- [ ] API status known for tools you might integrate
- [ ] Primary data flows mapped
- [ ] No critical unknowns blocking recommendations

---

## Naming Conventions

| Item | Format | Example |
|------|--------|---------|
| Survey file | `Tech Stack Survey.xlsx` | `Tech Stack Survey.xlsx` |
| Overview artifact | `Tech Stack Overview.html` | `Tech Stack Overview.html` |

---

## Folder Structure

```
Cadre Team Drive /
└── Clients /
    └── [Client Name] /
        ├── Tech Stack Survey.xlsx
        └── Deliverables /
            └── Tech Stack Overview.html
```

---

## Quick Reference

| Question | Answer |
|----------|--------|
| When to send? | Every engagement, at/around kickoff |
| Who fills it? | Client: columns A-G, Cadre: columns H+ |
| Who receives it? | Ask in discovery: "Who knows your tech stack best?" |
| Turnaround? | Within a week |
| Partial responses? | Accept it, research gaps, ask in next call |
| Forgot tools? | Add from research, mark unconfirmed, verify verbally |
| Integration detail? | Primary connections only |
| When done? | When you can make confident recommendations |
| Catalog relationship? | Survey = inventory, Catalog = issues/opportunities |

---

## Commands Reference

| Command | What It Does |
|---------|--------------|
| `/techstack template` | Get blank Tech Stack Survey Excel |
| `/techstack survey [client]` | Show survey questions to ask verbally |
| `/techstack research [client]` | Research API/integrations for tools in survey |
| `/techstack parse` | Parse completed survey responses |
| `/artifact overview [client]` | Generate Tech Stack Overview HTML |
| `/artifact map [client]` | Generate Integration Map (ask Claude to convert to HTML for Portal) |
