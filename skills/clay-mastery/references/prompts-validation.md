# Validation Prompts

Prompts for validating data quality, verifying accuracy, and catching errors before export.

---

## 1. Email Validity Assessment

**Use case:** Secondary check beyond email verification tools

**Prompt:**
```
Assess if this email appears valid for {{First Name}} {{Last Name}} at {{Company Name}}.

Email to validate: {{Email}}
Company domain: {{Domain}}
Email verification status: {{Verification Status}}

Check:
1. Does email domain match company domain?
2. Does email format match company pattern (if known)?
3. Is the name portion reasonable for this person?
4. Any red flags (typos, suspicious patterns)?

Return:
{
  "likely_valid": true/false,
  "confidence": "high/medium/low",
  "concerns": ["list any issues"],
  "domain_match": true/false,
  "format_assessment": "standard/unusual/suspicious"
}

Red flags to catch:
- Email domain doesn't match company website
- Generic email (info@, sales@, contact@)
- Name portion doesn't match provided name
- Unusual characters or formatting
- Known disposable email domain
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

**Note:** Use alongside ZeroBounce or similar verification tools, not as replacement.

---

## 2. Contact-Company Match Verification

**Use case:** Ensure contact actually works at stated company

**Prompt:**
```
Verify that {{Person Name}} currently works at {{Company Name}}.

Available data:
- LinkedIn URL: {{LinkedIn URL}}
- Email domain: {{Email Domain}}
- Title claimed: {{Title}}
- Company domain: {{Company Domain}}

Verification checks:
1. Does LinkedIn show current employment at this company?
2. Does email domain match company domain?
3. Is the title consistent with LinkedIn?
4. Any signs of job change?

Return:
{
  "verified": true/false,
  "confidence": "high/medium/low",
  "current_company_per_linkedin": "company name",
  "current_title_per_linkedin": "title",
  "discrepancies": ["list any mismatches"],
  "likely_stale": true/false,
  "recommended_action": "use/review/discard"
}

Confidence levels:
- High: All data points align
- Medium: Some data points align, minor discrepancies
- Low: Significant mismatches or can't verify
```

**Model:** Claygent Helium (1 credit) - needs to check LinkedIn

---

## 3. Data Consistency Check

**Use case:** Catch inconsistencies across enrichment sources

**Prompt:**
```
Check for inconsistencies in enriched data for {{Company Name}}.

Data from multiple sources:
- Clearbit employee count: {{Clearbit Employees}}
- Apollo employee count: {{Apollo Employees}}
- LinkedIn employee count: {{LinkedIn Employees}}
- Clearbit industry: {{Clearbit Industry}}
- Apollo industry: {{Apollo Industry}}
- Clearbit revenue: {{Clearbit Revenue}}
- Other revenue: {{Other Revenue}}

Analyze:
{
  "consistency_score": 1-10,
  "inconsistencies": [
    {
      "field": "field name",
      "values": ["source1: value", "source2: value"],
      "variance": "percentage or description",
      "recommended_value": "most reliable value",
      "reasoning": "why this value is preferred"
    }
  ],
  "data_quality": "good/fair/poor",
  "fields_needing_review": ["list fields with major discrepancies"]
}

Acceptable variance:
- Employee count: ±20%
- Revenue: ±30%
- Industry: Should match or be hierarchically related

Major inconsistencies to flag:
- Employee count differs by >50%
- Revenue differs by >50%
- Industry completely different
- Company names don't match
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

---

## 4. AI Output Quality Check

**Use case:** Validate AI-generated content before use

**Prompt:**
```
Review this AI-generated content for quality and accuracy.

Content type: {{Content Type}}
Generated content: {{AI Content}}
Context it was based on: {{Input Context}}

Quality checks:
1. Factual accuracy - Does it match the input context?
2. Hallucination check - Any claims not supported by input?
3. Tone appropriateness - Professional and relevant?
4. Completion - Is it complete or cut off?
5. Format compliance - Does it match expected format?

Return:
{
  "quality_score": 1-10,
  "passed": true/false,
  "issues": {
    "accuracy": ["list factual issues"],
    "hallucinations": ["unsupported claims"],
    "tone": ["tone issues"],
    "format": ["format issues"]
  },
  "usable_as_is": true/false,
  "suggested_fix": "correction if minor issue",
  "recommendation": "approve/edit/regenerate/discard"
}

Auto-fail conditions:
- Score below 6
- Any hallucinations detected
- Major factual errors
- Incomplete output
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

---

## 5. Phone Number Validation

**Use case:** Verify phone number format and likelihood

**Prompt:**
```
Validate this phone number for {{Person Name}} at {{Company Name}}.

Phone number: {{Phone}}
Person location: {{Location}}
Company HQ: {{Company Location}}

Checks:
1. Is format valid for the region?
2. Does area code match expected location?
3. Is it a mobile or landline?
4. Any signs it's a main company line vs. direct?

Return:
{
  "valid_format": true/false,
  "normalized": "+1-XXX-XXX-XXXX format",
  "phone_type": "mobile/landline/voip/unknown",
  "location_match": true/false,
  "likely_direct_line": true/false,
  "concerns": ["list any issues"],
  "dialable": true/false
}

Red flags:
- Format doesn't match region
- Area code is call center hub
- Matches company main line exactly
- Too short or too long
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

**Note:** For robust validation, use dedicated phone validation providers.

---

## 6. Pre-Export Validation Summary

**Use case:** Final check before pushing to CRM or sequencer

**Prompt:**
```
Perform pre-export validation on this lead record.

Record:
- Name: {{First Name}} {{Last Name}}
- Email: {{Email}}
- Phone: {{Phone}}
- Title: {{Title}}
- Company: {{Company Name}}
- Company Size: {{Employee Count}}
- Industry: {{Industry}}
- ICP Score: {{ICP Score}}
- Personalization: {{Personalization}}

Validation rules:
1. Required fields: Name, Email, Company (cannot be empty)
2. Email must pass verification or be catch-all
3. Company must match ICP criteria
4. Personalization cannot be "skip" or empty
5. No duplicate indicators

Return:
{
  "export_ready": true/false,
  "validation_status": "pass/warn/fail",
  "missing_required": ["list missing fields"],
  "warnings": ["non-blocking issues"],
  "blocking_issues": ["must fix before export"],
  "data_completeness": "X%",
  "recommendation": "export/review/hold/discard"
}

Export decision matrix:
- All required + no blockers = export
- Missing required = hold
- Blockers present = discard or fix
- Warnings only = export with flag
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

---

## Formula-Based Validation (FREE)

### Email Format Check

```javascript
const email = {{Email}} || "";
const domain = {{Company Domain}} || "";

// Basic format check
const validFormat = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

// Domain match
const emailDomain = email.split("@")[1] || "";
const domainMatch = emailDomain.toLowerCase() === domain.toLowerCase();

// Generic email check
const isGeneric = /^(info|sales|contact|support|hello|admin)@/.test(email.toLowerCase());

!validFormat ? "Invalid Format" :
!domainMatch ? "Domain Mismatch" :
isGeneric ? "Generic Email" :
"Valid"
```

### Required Fields Check

```javascript
const required = {
  "First Name": {{First Name}},
  "Last Name": {{Last Name}},
  "Email": {{Email}},
  "Company": {{Company Name}}
};

const missing = Object.entries(required)
  .filter(([k, v]) => !v || v.trim() === "")
  .map(([k]) => k);

missing.length === 0 ? "Complete" : `Missing: ${missing.join(", ")}`
```

### Duplicate Detection Formula

```javascript
// Create composite key for deduplication
const email = ({{Email}} || "").toLowerCase().trim();
const company = ({{Company Name}} || "").toLowerCase().replace(/[^a-z0-9]/g, "");
const name = ({{First Name}} || "").toLowerCase() + ({{Last Name}} || "").toLowerCase();

`${email}|${company}|${name}`

// Then use Clay's native deduplication on this column
```

### Data Quality Score

```javascript
let score = 0;
const max = 100;

// Required fields (40 points)
if ({{First Name}}) score += 10;
if ({{Last Name}}) score += 10;
if ({{Email}}) score += 15;
if ({{Company Name}}) score += 5;

// Valuable fields (35 points)
if ({{Phone}}) score += 10;
if ({{LinkedIn URL}}) score += 10;
if ({{Title}}) score += 10;
if ({{Employee Count}}) score += 5;

// Quality indicators (25 points)
if ({{Email Verified}} === "valid") score += 15;
if ({{ICP Score}} >= 60) score += 10;

`${score}%`
```

---

## Batch Validation Strategy

For large datasets:

1. **Run formula validations first** (free, instant)
2. **Filter to flagged records**
3. **Run AI validation on flagged records only** (saves credits)
4. **Manual review of AI-flagged issues**
5. **Export clean records**

```
Total Records: 10,000
├── Formula Validation: 10,000 (FREE)
├── Flagged for AI Review: 500 (5%)
├── AI Validation: 500 × 0.5 credits = 250 credits
├── Manual Review: 50 (0.5%)
└── Clean for Export: 9,450
```
