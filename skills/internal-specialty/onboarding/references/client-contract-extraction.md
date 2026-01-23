# Contract Extraction Playbook

Advanced techniques for extracting structured information from client contracts, MSAs, Schedules A, and SOWs.

---

## Contract Document Types

### Master Services Agreement (MSA)
**Purpose:** Legal framework, general terms, relationship structure  
**What to extract:**
- Effective date
- Term and renewal provisions
- Termination clauses
- Liability limits
- IP ownership
- Confidentiality terms
- Governing law

**Search terms:** "MSA", "master services agreement", "[Client] agreement effective"

### Schedule A / Statement of Work (SOW)
**Purpose:** Specific deliverables, pricing, timeline  
**What to extract:**
- Deliverables with quantities
- Payment structure
- Timeline and milestones
- Acceptance criteria
- Monthly obligations
- Scope boundaries

**Search terms:** "Schedule A", "SOW", "statement of work", "scope of services"

### Amendments / Change Orders
**Purpose:** Modifications to original agreement  
**What to extract:**
- What changed (scope, price, timeline)
- Effective date of change
- New terms replacing old terms
- Signatures and approval

**Search terms:** "amendment", "change order", "[Client] revised", "version 2"

---

## Layered Search Strategy

### Layer 1: Broad Discovery
**Goal:** Find what contract documents exist

**Queries:**
```
1. "[Client] contract"
2. "[Client] agreement"
3. "[Client] MSA"
4. "[Client] signed"
```

**Expected results:** Multiple contract documents, possibly versions

**What to look for:**
- Document dates (find most recent)
- Signed vs unsigned (prioritize signed)
- Version numbers (v1, v2, final)
- PDF file size (larger = more complete)

### Layer 2: Targeted Extraction
**Goal:** Find specific contract sections

**Queries by topic:**
```
Payment terms:
- "[Client] payment $[amount] monthly"
- "[Client] invoice net 30 commencement"

Deliverables:
- "[Client] deliverables services"
- "[Client] CustomGPT training reports" (use actual deliverable terms)

Timeline:
- "[Client] effective date term months"
- "[Client] start date end date renewal"

Scope:
- "[Client] scope work services description"
- "[Client] in scope out of scope exclusions"
```

### Layer 3: Cross-Reference Validation
**Goal:** Reconcile contradictions, find latest terms

**Approach:**
1. If you find multiple documents with same info → Use most recent date
2. If you find contradictions → Check for amendments
3. If payment differs from proposal → Contract wins (it's signed)
4. If deliverables ambiguous → Search discovery transcripts for clarification

---

## PDF Extraction Techniques

### Using pdfplumber (Preferred)
**When:** Complex formatting, tables, multi-column layouts

```python
import pdfplumber

with pdfplumber.open(contract_path) as pdf:
    # Extract all text
    full_text = ""
    for page in pdf.pages:
        full_text += page.extract_text()
    
    # Extract tables
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            # Process table data
            pass
```

**Advantages:**
- Handles tables well
- Preserves structure
- Works with complex PDFs

### Using PyPDF2 (Fallback)
**When:** Simple text extraction, pdfplumber fails

```python
import PyPDF2

with open(contract_path, 'rb') as file:
    pdf = PyPDF2.PdfReader(file)
    full_text = ""
    for page in pdf.pages:
        full_text += page.extract_text()
```

**Limitations:**
- Tables often mangled
- Formatting lost
- Multi-column issues

### Handling OCR PDFs
Some contracts are scanned images, not text.

**Detection:** Extract first page → if empty or garbled, it's OCR

**Solutions:**
1. **Try pdfplumber first** (has OCR support)
2. **Manual reading:** Read PDF visually, extract manually
3. **Flag for user:** "Contract appears to be scanned, extraction may be incomplete"

---

## Contract Parsing Framework

### Section Identification

Most contracts follow standard structure:

```
1. Parties
2. Recitals (WHEREAS clauses)
3. Agreement
   a. Services / Scope
   b. Deliverables
   c. Timeline
   d. Payment
   e. Term and Termination
4. General Provisions
5. Signatures
```

**Search for section headers:**
- "SCOPE OF SERVICES"
- "DELIVERABLES"
- "PAYMENT TERMS"
- "TERM AND TERMINATION"

### Deliverables Extraction Pattern

**Look for:**
- Numbered lists (1., 2., 3.)
- Bullet points (•, -)
- Tables with columns [Deliverable | Quantity | Due Date]
- "Cadre shall deliver..." statements
- "Client will receive..." statements

**Common deliverable indicators:**
```
Keywords to search for:
- "deliver", "provide", "create", "develop"
- "report", "strategy", "analysis", "document"
- "training", "session", "workshop", "presentation"
- "monthly", "quarterly", "upon completion"
- Quantities: "eight (8)", "7 sessions", "25 prompts"
```

**Example extraction:**
```
Contract text: "Cadre will deliver eight (8) CustomGPTs, 
two per department, by Month 3."

Extracted:
- Deliverable: CustomGPTs
- Quantity: 8 total (2 per department)
- Departments: 4 (inferred from 8/2)
- Due: Month 3
```

### Payment Structure Extraction

**Look for:**
- Total contract value
- Monthly/quarterly payment amounts
- Payment timing (Net 30, upon signature, etc)
- Special payments (commencement, success fees)
- Expense reimbursement terms

**Payment patterns:**
```
"$81,000 over 6 months" → Total: $81K, Duration: 6mo
"$13,500 per month" → Monthly: $13,500
"First and last month paid upon execution" → Commencement: $27,000
"Net 30 days" → Payment timing: 30 days after invoice
```

**Parse this pattern:**
```
Total contract value: $[amount]
Duration: [X] months
Monthly: $[amount/month]
Special payments: [description]
Payment terms: [Net X, upon signature, etc]
```

### Timeline Extraction

**Look for:**
- Start date / Effective date
- End date / Term duration
- Renewal provisions
- Milestone dates
- Deliverable schedules

**Date formats to handle:**
```
"Effective November 1, 2025"
"This Agreement shall commence on the Effective Date and continue for six (6) months"
"Month 1: [deliverables]"
"Q1 2025: [milestones]"
```

**Extract:**
- Start date: [Date]
- End date: [Date or calculated from duration]
- Duration: [X months/years]
- Auto-renewal: [Yes/No, terms]
- Termination notice: [X days]

---

## Deliverables Organization Framework

### Pillar/Phase/Workstream Detection

Many contracts organize deliverables into groups:

**Common frameworks:**
- **Pillars:** Thematic groupings (e.g., "AI Command Center", "Culture Shift")
- **Phases:** Sequential stages (e.g., "Discovery", "Strategy", "Implementation")
- **Workstreams:** Parallel tracks (e.g., "Sales", "Operations", "Technology")

**Detection pattern:**
Look for:
- Headers like "Pillar 1:", "Phase A:", "Workstream 1:"
- Numbered top-level sections with sub-deliverables
- Tables with "Category" or "Area" columns

**Example extraction:**
```
Contract structure:
"Pillar 1: AI Command Center
  - 8 CustomGPTs (2 per department)
  - 25 Custom Prompts
  - ChatGPT Enterprise Setup
  
Pillar 2: AI-First Culture Shift
  - 7 Training Sessions (AI 101-107)
  - Champions Network Establishment
  - AI Help Desk Setup"

Organized as:
Pillar 1: AI Command Center
  ├─ CustomGPTs (8)
  ├─ Custom Prompts (25)
  └─ ChatGPT Enterprise Setup (1)

Pillar 2: AI-First Culture Shift
  ├─ Training Sessions (7)
  ├─ Champions Network (1)
  └─ AI Help Desk (1)
```

### Month-by-Month Mapping

If contract specifies timing, map deliverables to calendar:

**Pattern to look for:**
```
"Month 1: Kickoff, Discovery Phase 1
Month 2: Discovery Phase 2, Current State Reports (2)
Month 3: Strategy Development, CustomGPTs (4)"
```

**Extract as:**
```
Month 1 (Dec 2025):
- [ ] Kickoff meeting
- [ ] Discovery Phase 1

Month 2 (Jan 2026):
- [ ] Discovery Phase 2
- [ ] Current State Reports (2)

Month 3 (Feb 2026):
- [ ] Strategy Development
- [ ] CustomGPTs (4)
```

---

## Special Contract Provisions

### Auto-Renewal Clauses

**Pattern:**
```
"This Agreement shall automatically renew for successive 
[period] terms unless either party provides written notice 
of termination at least [X] days prior to the end of the 
then-current term."
```

**Extract:**
- Auto-renewal: Yes
- Renewal period: [X months]
- Notice required: [X days]
- **Flag:** Set calendar reminder for [End Date - Notice Period]

### Scope Exclusions

**Critical for managing expectations**

**Look for:**
- "Out of Scope"
- "Exclusions"
- "Cadre will NOT..."
- "Client is responsible for..."

**Example:**
```
"Out of Scope: Custom software development, system 
implementation, ongoing IT support"

Extracted:
❌ NOT in scope:
- Custom software development
- System implementation  
- Ongoing IT support

⚠️ Risk flag: Client may expect these (check discovery)
```

### Change Order Process

**Look for:**
- How scope changes are handled
- Who can approve changes
- Pricing for additional work

**Extract:**
```
Change process:
- Written request required: [Yes/No]
- Approval authority: [Title/Person]
- Pricing: [Hourly rate / Fixed markup / Negotiated]
```

---

## Quality Assurance Checklist

Before considering contract extraction complete:

### Completeness Check
- [ ] Total contract value identified
- [ ] Monthly payment amount identified
- [ ] Payment terms/timing identified
- [ ] Start date identified
- [ ] Duration identified
- [ ] All deliverables extracted
- [ ] Deliverable quantities specified
- [ ] Deliverable timing specified (when available)
- [ ] Organization framework identified (pillars/phases/workstreams)
- [ ] Monthly/recurring obligations identified
- [ ] Auto-renewal terms identified
- [ ] Termination provisions identified
- [ ] Scope exclusions identified

### Accuracy Check
- [ ] All dollar amounts match contract exactly
- [ ] All dates match contract exactly
- [ ] All deliverable counts match contract exactly
- [ ] No assumptions made without flagging
- [ ] Ambiguous terms flagged for clarification

### Consistency Check
- [ ] Total value = Monthly × Duration (if applicable)
- [ ] Deliverable counts add up correctly
- [ ] Timeline makes sense (no overlaps/gaps)
- [ ] Payment schedule aligns with deliverables

### Flag Check
- [ ] Ambiguities flagged: ⚠️
- [ ] Scope risks flagged: ⚠️
- [ ] Contradictions with discovery flagged: ⚠️
- [ ] Critical dates flagged: 📅

---

## Common Contract Pitfalls

### Pitfall 1: Vague Deliverables

**Problem:**
```
"Cadre will provide strategic guidance and reports as needed"
```

**Issue:** "As needed" is undefined, creates scope creep risk

**Solution:**
- Extract literally: "Strategic guidance (quantity TBD)"
- Flag: ⚠️ "Undefined quantity - scope risk"
- Check discovery: Did client specify expectations?
- Recommend: Clarify in kickoff meeting

### Pitfall 2: Implied Deliverables

**Problem:**
```
Discovery transcripts mention "client portal" but contract 
says only "technology recommendations"
```

**Issue:** Client expects more than contracted

**Solution:**
- Extract only what's in contract
- Flag contradiction: ⚠️ "Client portal mentioned in discovery but not in contract - alignment needed"
- Add to Risk Assessment: "Scope creep from implementation expectations"

### Pitfall 3: Conflicting Versions

**Problem:**
```
Found 3 documents:
- Schedule_A_v1.pdf ($72K, 5 months)
- Schedule_A_v2.pdf ($81K, 6 months)
- Schedule_A_FINAL_SIGNED.pdf ($81K, 6 months, different deliverables)
```

**Solution:**
- Use signed version always
- Note versions found: "3 versions identified, using signed v2"
- If unsigned docs have newer info: Flag for client confirmation

### Pitfall 4: Hidden Exclusions

**Problem:**
```
Contract says "AI Strategy" but deep in contract: 
"Implementation, custom development, and ongoing support 
are out of scope"
```

**Issue:** Title sounds broad, exclusions make it narrow

**Solution:**
- Extract exclusions prominently
- Flag mismatch: ⚠️ "Strategy scope, but client may expect implementation"
- Cross-reference with discovery expectations

---

## Advanced Extraction Techniques

### Table Extraction

When contracts use tables for deliverables:

**Example table in PDF:**
```
| Deliverable          | Qty | Due Date | Department |
|---------------------|-----|----------|------------|
| CustomGPT           |  2  | Month 2  | Sales      |
| Current State Report|  1  | Month 1  | Sales      |
```

**pdfplumber extraction:**
```python
for page in pdf.pages:
    tables = page.extract_tables()
    for table in tables:
        headers = table[0]
        for row in table[1:]:
            deliverable = {
                'name': row[0],
                'quantity': row[1],
                'due_date': row[2],
                'department': row[3]
            }
```

### Multi-Column Layout Handling

Some contracts use 2-column format.

**Problem:** Text extraction merges columns incorrectly

**Solution with pdfplumber:**
```python
for page in pdf.pages:
    # Set bounding boxes for left and right columns
    left = page.crop((0, 0, page.width/2, page.height))
    right = page.crop((page.width/2, 0, page.width, page.height))
    
    left_text = left.extract_text()
    right_text = right.extract_text()
    
    # Process columns separately then combine
```

### Nested Deliverable Extraction

When deliverables have sub-deliverables:

**Example:**
```
"Pillar 1: AI Command Center
  a. CustomGPTs (8 total)
     i. Sales GPT (2)
     ii. Marketing GPT (2)
     iii. Operations GPT (2)
     iv. Finance GPT (2)
  b. Custom Prompts (25)
  c. Enterprise Setup (1)"
```

**Extracted structure:**
```
Pillar 1: AI Command Center
├─ CustomGPTs (8)
│  ├─ Sales (2)
│  ├─ Marketing (2)
│  ├─ Operations (2)
│  └─ Finance (2)
├─ Custom Prompts (25)
└─ Enterprise Setup (1)

Total Pillar 1 deliverables: 10 distinct items
```

---

## Contract Extraction Output Format

### Recommended Structure

```markdown
## Contract Commitments (from [Document Name], dated [Date])

### Payment Structure
[Table format with all payment details]

### [Framework Name] (e.g., Four-Pillar Delivery Framework)

Brief description of framework

#### Pillar 1: [Name]
Description

**Deliverables:**
1. **[Deliverable]** (Qty: X)
   - Due: Month X
   - Acceptance criteria: [If specified]

[Subtotal: X deliverables]

#### Pillar 2-N: [Repeat]

### Monthly/Recurring Obligations
- [Obligation 1]: [Frequency, duration, details]

### Special Provisions
- Auto-renewal: [Terms]
- Termination: [Notice period]
- Scope exclusions: [List]

### Ambiguities & Clarifications Needed
⚠️ [Item 1]: [What's unclear]
⚠️ [Item 2]: [What's unclear]
```

---

## Integration with Discovery Intelligence

After extracting contract, cross-reference with discovery:

### Alignment Check

| Contract Says | Discovery Says | Status | Action |
|---------------|----------------|--------|--------|
| "$81K strategy engagement" | "Want to blow up entire tech stack" | ⚠️ MISALIGNED | Scope conversation needed |
| "8 CustomGPTs" | "Need AI for 12 processes" | 🔄 ALIGNED | Good, can propose more in Phase 2 |
| "4 departments" | "Finance dept not engaged yet" | ⚠️ RISK | Need Finance stakeholder |

### Expectation Gaps

Look for:
- Contract: "Strategy and recommendations"
- Discovery: "When will you build this for us?"
- **Gap**: Implementation expectation vs strategy scope

**Flag:** ⚠️ "Client expects implementation, contract is strategy - continuous alignment needed"

---

## Contract Extraction Workflow Summary

1. **Search** → Layered search to find all contract documents
2. **Identify** → Determine which document is authoritative (signed, recent)
3. **Extract** → Pull structured data (payment, deliverables, timeline)
4. **Organize** → Map to framework (pillars/phases), create calendar
5. **Validate** → Check completeness, accuracy, consistency
6. **Flag** → Mark ambiguities, contradictions, risks
7. **Cross-Reference** → Compare contract to discovery intelligence
8. **Document** → Create structured output for onboarding brief

**Time estimate:** 30-60 minutes for typical 10-20 page contract
