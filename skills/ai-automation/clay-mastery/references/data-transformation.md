# Data Transformation

Techniques for cleaning, normalizing, and preparing data within Clay workflows.

## Table of Contents
1. [Native Cleaning Tools](#native-cleaning-tools)
2. [Data Cleaning Patterns](#data-cleaning-patterns)
3. [Normalization Techniques](#normalization-techniques)
4. [AI-Powered Classification](#ai-powered-classification)
5. [Scoring Model Implementation](#scoring-model-implementation)

---

## Native Cleaning Tools

Clay provides free built-in tools for common transformations:

| Tool | Function | Access |
|------|----------|--------|
| Normalize Company Names | Removes Inc., LLC, GmbH, Corp, etc. | Add Enrichment → Tools |
| Normalize Whitespace | Eliminates extra spaces, tabs, newlines | Add Enrichment → Tools |
| Normalize Phone Numbers | Standardizes to consistent format | Add Enrichment → Tools |
| Normalize Locations | Uniform address representation | Add Enrichment → Tools |
| Auto-dedupe | Removes duplicate rows | Click icon (bottom right) |

### Using Auto-Dedupe

1. Click the dedupe icon (bottom right of table)
2. Select column to dedupe on (e.g., Email)
3. Choose which duplicate to keep (first, last, or most complete)
4. Run deduplication
5. Review removed rows before confirming

---

## Data Cleaning Patterns

### Removing Unwanted Characters

**Remove all non-numeric from phone:**
```javascript
{{Phone}}.replace(/\D/g, "")
// "(555) 123-4567" → "5551234567"
```

**Remove special characters:**
```javascript
{{Field}}.replace(/[^\w\s]/g, "")
// "Hello! @World#" → "Hello World"
```

**Remove extra whitespace:**
```javascript
{{Field}}.replace(/\s+/g, " ").trim()
// "  Hello    World  " → "Hello World"
```

### Fixing Casing

**Title case:**
```javascript
{{Name}}.split(" ").map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join(" ")
// "JOHN SMITH" → "John Smith"
```

**Sentence case:**
```javascript
{{Field}}.charAt(0).toUpperCase() + {{Field}}.slice(1).toLowerCase()
// "HELLO WORLD" → "Hello world"
```

### Handling Null Values

**Replace null with default:**
```javascript
{{Field}} || "Not Available"
```

**Replace empty string with null (for CRM):**
```javascript
{{Field}} === "" ? null : {{Field}}
```

**Coalesce multiple fields:**
```javascript
{{Primary Email}} || {{Secondary Email}} || {{Work Email}} || "No Email"
```

---

## Normalization Techniques

### Company Name Standardization

**Remove legal suffixes:**
```javascript
{{Company}}.replace(/,?\s*(Inc\.?|LLC|Ltd\.?|Corporation|Corp\.?|Co\.?|Limited|PLC|GmbH|AG|SA|SAS|BV|NV)\s*$/gi, "").trim()
```

**Remove "The" prefix:**
```javascript
{{Company}}.replace(/^The\s+/i, "")
// "The Coca-Cola Company" → "Coca-Cola Company"
```

### Job Title Normalization

**Standardize common variations:**
```javascript
{{Title}}
  .replace(/Vice President/i, "VP")
  .replace(/Chief Executive Officer/i, "CEO")
  .replace(/Chief Technology Officer/i, "CTO")
  .replace(/Chief Financial Officer/i, "CFO")
  .replace(/Chief Operating Officer/i, "COO")
  .replace(/Chief Marketing Officer/i, "CMO")
  .replace(/Chief Revenue Officer/i, "CRO")
  .replace(/Senior Vice President/i, "SVP")
  .replace(/Executive Vice President/i, "EVP")
```

### Location Formatting

**State abbreviation to full name:**
```javascript
const states = {
  "CA": "California", "NY": "New York", "TX": "Texas", 
  "FL": "Florida", "IL": "Illinois" // ... etc
};
states[{{State}}] || {{State}}
```

**Country standardization:**
```javascript
{{Country}}
  .replace(/^US$|^USA$|United States of America/i, "United States")
  .replace(/^UK$|^GB$/i, "United Kingdom")
```

### Phone Number Formatting

**US phone format:**
```javascript
const digits = {{Phone}}.replace(/\D/g, "");
digits.length === 10 ? 
  `(${digits.slice(0,3)}) ${digits.slice(3,6)}-${digits.slice(6)}` : 
  {{Phone}}
// "5551234567" → "(555) 123-4567"
```

**E.164 format (international):**
```javascript
const digits = {{Phone}}.replace(/\D/g, "");
digits.startsWith("1") ? `+${digits}` : `+1${digits}`
// "5551234567" → "+15551234567"
```

### Email Domain Extraction

**Get domain:**
```javascript
{{Email}}.split("@").pop().toLowerCase()
// "john@Company.com" → "company.com"
```

**Get root domain (remove subdomain):**
```javascript
{{Email}}.split("@").pop().split(".").slice(-2).join(".").toLowerCase()
// "john@mail.company.co.uk" → "co.uk" (careful with this one)
```

---

## AI-Powered Classification

For complex categorization beyond simple rules, use "Use AI" columns.

### Industry Classification

**Prompt:**
```
Classify this company into ONE of these industries based on their description:
- Technology
- Healthcare
- Financial Services
- Manufacturing
- Retail
- Professional Services
- Education
- Government
- Non-Profit
- Other

Company Description: {{Company Description}}

Return ONLY the industry name, nothing else.
```

### Seniority Level Detection

**Prompt:**
```
Based on this job title, determine the seniority level.
Job Title: {{Title}}

Return ONLY one of these levels:
- C-Suite (CEO, CFO, CTO, etc.)
- VP (Vice President, SVP, EVP)
- Director
- Manager
- Senior Individual Contributor
- Individual Contributor

Output the level only.
```

### Department Classification

**Prompt:**
```
What department does this person likely work in based on their title?
Title: {{Title}}

Return ONLY one of:
- Sales
- Marketing
- Engineering
- Product
- Operations
- Finance
- HR
- Legal
- Customer Success
- IT
- Executive
- Other
```

### Buying Intent Classification

**Prompt:**
```
Based on this company's recent news/activity, rate their buying intent for {{Product Category}}.

Company: {{Company Name}}
Recent Activity: {{News/Activity}}

Rate as:
- High Intent: Active evaluation or recent trigger event
- Medium Intent: Potential need indicated
- Low Intent: No clear signals
- Unknown: Insufficient information

Return ONLY the rating.
```

---

## Scoring Model Implementation

### Point-Based Scoring

**Simple ICP score formula:**
```javascript
let score = 0;

// Company size (30 points max)
score += {{Employee Count}} > 500 ? 30 :
         {{Employee Count}} > 100 ? 20 :
         {{Employee Count}} > 50 ? 10 : 0;

// Industry fit (25 points max)
score += ["Technology", "Healthcare", "Finance"].includes({{Industry}}) ? 25 : 0;

// Title seniority (25 points max)
score += {{Title}}.match(/chief|ceo|cfo|cto|coo|president/i) ? 25 :
         {{Title}}.match(/vp|vice president/i) ? 20 :
         {{Title}}.match(/director|head/i) ? 15 :
         {{Title}}.match(/manager/i) ? 10 : 5;

// Geography (20 points max)
score += ["CA", "NY", "TX", "FL"].includes({{State}}) ? 20 : 10;

score
```

### Weighted Attribute Scoring

**Prompt for AI-assisted scoring:**
```
Evaluate this lead against our ICP criteria and return a score from 0-100.

Lead Data:
- Company: {{Company Name}}
- Industry: {{Industry}}
- Employee Count: {{Employee Count}}
- Title: {{Title}}
- Location: {{Location}}

ICP Criteria (weights):
- Company Size 50-500 employees (weight: 30%)
- Industry: SaaS, Technology (weight: 25%)
- Title: Director+ (weight: 25%)
- Location: US (weight: 20%)

Scoring rules:
- Perfect match on criterion = full weight
- Partial match = half weight
- No match = 0

Calculate weighted score and return ONLY a number from 0-100.
```

### Lead Grading (A/B/C/D)

**Formula-based grading:**
```javascript
{{Score}} >= 80 ? "A" :
{{Score}} >= 60 ? "B" :
{{Score}} >= 40 ? "C" : "D"
```

**Multi-factor grading:**
```javascript
const firmographicFit = {{Firmographic Score}} >= 70;
const titleFit = {{Title Score}} >= 60;
const engagementSignal = {{Engagement Score}} >= 50;

firmographicFit && titleFit && engagementSignal ? "A" :
firmographicFit && (titleFit || engagementSignal) ? "B" :
firmographicFit || titleFit ? "C" : "D"
```

### Prioritization Matrix

**Combining score with timing signals:**
```javascript
const baseScore = {{ICP Score}};
const urgencyBoost = {{Recent Funding}} ? 20 : 0;
const intentBoost = {{Hiring Signal}} ? 15 : 0;
const recencyBoost = {{Job Change 90d}} ? 10 : 0;

Math.min(100, baseScore + urgencyBoost + intentBoost + recencyBoost)
```
