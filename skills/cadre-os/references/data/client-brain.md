# Client Brain Reference

The Client Brain is a Google Doc containing narrative relationship context for each client.

## Contents

1. [Brain Document Structure](#brain-document-structure)
2. [Finding Brains](#finding-brains)
3. [Querying Brains](#querying-brains)
4. [Suggesting Updates](#suggesting-updates)

---

## Brain Document Structure

Each Client Brain follows this structure:

### Section 1: Client Overview
- Company name, industry, size
- Engagement type and timeline
- Why they engaged Cadre

### Section 2: Stakeholder Map
| Field | Description |
|-------|-------------|
| Name | Full name |
| Title | Current role |
| Role Type | Economic Buyer / Champion / Technical Lead / Blocker / Influencer |
| Power (1-10) | Decision-making authority |
| Sentiment (1-10) | Current support level |
| Notes | Key context, preferences, concerns |

### Section 3: Relationship Health
- Overall score (1-10)
- Last contact date
- Engagement trend (improving/stable/declining)
- Warning signs

### Section 4: Active Context
- Current engagement phase
- Open questions
- Recent wins
- Current blockers
- What's working / What's not working

### Section 5: Key Decisions Log
| Date | Decision | Made By | Rationale |
|------|----------|---------|-----------|
| Chronological log of significant decisions |

### Section 6: Preferences & Patterns
- Communication preferences
- Meeting preferences  
- Decision-making patterns
- Things that work well
- Things to avoid

### Section 7: Update Log
- Automatic entries from n8n workflow
- Manual additions

---

## Finding Brains

### Search Patterns

```
# Find by client name
google_drive_search:
  api_query: name contains '[Client Name]' and name contains 'Brain'

# Find all Brains
google_drive_search:
  api_query: name contains 'Brain' and mimeType = 'application/vnd.google-apps.document'

# Search Brain content
google_drive_search:
  api_query: fullText contains '[search term]' and name contains 'Brain'
  semantic_query: [what you're looking for]
```

### Finding Brain Documents

**Option 1: Get link from Catalog (preferred)**

Query 0_Clients table for the Brain Link field:
```
Airtable MCP: list_records
Base: apprH2AppvnKfUpT0
Table: tbl9MiW4wWEHoNw6t
Filter: {Client Name} = '[ClientName]'
```
Use the "Brain Link" field value to fetch the document directly.

**Option 2: Search Google Drive**

If Brain Link is empty, search by naming convention:
```
Google Drive: search
Query: name contains '[ClientName] Brain'
```

Common patterns: `[Client] Brain`, `[ShortName] Brain`

---

## Querying Brains

### For Stakeholder Information

1. Find the Brain document
2. Read Section 2: Stakeholder Map
3. Look for: name, title, role type, power, sentiment, notes

**Example response format:**
```
Key stakeholders at [Client]:

**[Name]** — [Title]
- Role: [Economic Buyer/Champion/etc.]
- Power: [X]/10 | Sentiment: [Y]/10
- Notes: [Key context]
```

### For Current Status

1. Read Section 4: Active Context
2. Include: current phase, blockers, open questions
3. Add Section 3: Relationship Health score

### For Pre-Meeting Brief

Combine:
- Section 1: Quick company context
- Section 2: People on the call (filter by attendees if known)
- Section 4: Current blockers and open questions
- Section 6: What works / what to avoid

---

## Suggesting Updates

This skill can suggest updates to Brains. Format suggestions clearly:

```
📝 **Suggested Brain Update for [Client]:**

**Section:** [Section name]
**Addition:**
[Formatted content to add]

Would you like me to add this to the Brain?
```

### Update Types

| Type | Section | Format |
|------|---------|--------|
| New stakeholder | 2. Stakeholder Map | Table row |
| Decision | 5. Key Decisions Log | Table row with date |
| Blocker | 4.4 Current Blockers | Bullet point |
| Preference | 6. Preferences | Bullet under relevant subsection |
| Win | 4.2 Recent Wins | Bullet with date |

### Update Principles

- **Don't overwrite** — Add to existing content
- **Include dates** — Timestamp new entries
- **Cite source** — Note where info came from (meeting, email, etc.)
- **Ask for confirmation** — User approves before committing
