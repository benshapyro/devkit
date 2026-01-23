# CRM Integrations

Patterns for bidirectional sync between Clay and CRMs (HubSpot, Salesforce).

## Table of Contents
1. [HubSpot Integration](#hubspot-integration)
2. [Salesforce Integration](#salesforce-integration)
3. [Deduplication Strategies](#deduplication-strategies)
4. [Field Mapping Best Practices](#field-mapping-best-practices)
5. [Sync Scheduling](#sync-scheduling)
6. [Data Integrity](#data-integrity)

---

## HubSpot Integration

HubSpot is Clay's most common CRM integration. With your own API key, imports are **free** (0 credits).

### Available Actions

| Action | Credits | Use Case |
|--------|---------|----------|
| Import from HubSpot | 0 (with API key) | Pull contacts/companies for enrichment |
| Lookup Contact | 0 | Check if contact exists before creating |
| Lookup Company | 0 | Check if company exists |
| Create Contact | 0 | Add new enriched contact |
| Create Company | 0 | Add new enriched company |
| Update Contact | 0 | Push enriched data back |
| Update Company | 0 | Push company enrichments |
| Create Association | 0 | Link contact to company |

### Import from HubSpot

**Setup:**
1. Add Enrichment → HubSpot → Import Objects
2. Select object type (Contact, Company, Deal)
3. Choose list OR set filters:
   - Property filters (e.g., "Created date > 30 days ago")
   - List membership
   - Lifecycle stage
4. Select properties to import
5. Run import

**Common import filters:**
```
# Contacts needing enrichment
Last Modified Date is more than 90 days ago
AND Email is known

# New contacts for qualification
Create Date is within last 7 days
AND Lifecycle Stage is Lead

# High-value accounts
Annual Revenue is greater than $1,000,000
AND Industry is known
```

### Lookup Before Create (Critical Pattern)

**Always check if record exists before creating:**

1. **Column 1: Lookup Contact by Email**
   - Add Enrichment → HubSpot → Lookup Contact
   - Search by: Email = {{Email}}
   - Output: HubSpot Contact ID (or empty)

2. **Column 2: Create Contact (Conditional)**
   - Add Enrichment → HubSpot → Create Contact
   - Run Settings → Only run if: `!{{HubSpot Contact ID}}`
   - Map fields from Clay columns

3. **Column 3: Update Contact (Conditional)**
   - Add Enrichment → HubSpot → Update Contact
   - Run Settings → Only run if: `{{HubSpot Contact ID}}`
   - Use HubSpot Contact ID from lookup
   - Map enriched fields

### Create Contact

**Field mapping:**
```
HubSpot Property    →    Clay Column
email               →    {{Email}}
firstname           →    {{First Name}}
lastname            →    {{Last Name}}
phone               →    {{Phone}}
company             →    {{Company Name}}
jobtitle            →    {{Title}}
linkedin_url        →    {{LinkedIn URL}}
```

**Custom properties:**
- Map to HubSpot internal names (not display names)
- Find internal names in HubSpot Settings → Properties
- Example: "lead_source" not "Lead Source"

### Update Contact

**Required:** HubSpot Contact ID (from lookup or import)

**Important settings:**
- ✅ Enable "Ignore blank values" - Prevents overwriting good data with empty Clay fields
- ✅ Enable "Only update if changed" - Reduces API calls

### Create Association

**Link contact to company:**
1. Lookup company by domain first
2. Create association: Contact ID → Company ID
3. Association type: "Contact to Company"

---

## Salesforce Integration

Salesforce integration requires Pro plan or higher.

### Available Actions

| Action | Use Case |
|--------|----------|
| Import via SOQL | Pull records with precise queries |
| Lookup Record | Find existing records |
| Create Record | Add new leads/contacts/accounts |
| Update Record | Push enrichments |
| Upsert Record | Create or update in one step |

### SOQL Queries for Import

**Basic contact import:**
```sql
SELECT Id, FirstName, LastName, Email, Phone, Account.Name
FROM Contact
WHERE Email != null
AND LastModifiedDate < LAST_N_DAYS:90
LIMIT 1000
```

**Accounts needing enrichment:**
```sql
SELECT Id, Name, Website, Industry, NumberOfEmployees
FROM Account
WHERE Website != null
AND (NumberOfEmployees = null OR Industry = null)
```

**Leads from specific campaign:**
```sql
SELECT Id, FirstName, LastName, Email, Company, LeadSource
FROM Lead
WHERE CampaignId = '701XX000001ABCD'
AND IsConverted = false
```

### Upsert (Recommended Approach)

Upsert combines create/update logic—simpler than lookup-then-create:

1. Add Enrichment → Salesforce → Upsert Record
2. Select object type (Lead, Contact, Account)
3. Choose external ID field for matching (usually Email)
4. Map fields
5. Clay automatically creates new records or updates existing

**Limitation:** Requires external ID field enabled in Salesforce.

### Update Record

**Required:** Salesforce Record ID (not email!)

**Getting Salesforce ID:**
1. Import includes ID automatically
2. OR use Lookup action first
3. Store ID in Clay column
4. Reference in Update action

### Permission Considerations

Salesforce integration requires:
- Connected app setup in Salesforce
- OAuth authentication
- User permissions for objects being accessed
- Field-level security for all mapped fields

---

## Deduplication Strategies

### Always Lookup Before Create

**Pattern:**
```
1. Lookup by Email
2. If found → Update existing
3. If not found → Create new
```

**Formula for conditional logic:**
```javascript
// Run Create only if Lookup returned empty
!{{Salesforce ID}} && {{Email}}
```

### Using Email as Unique Identifier

Email is typically the most reliable deduplication key:
- Unique per person
- Standardized format
- Available early in workflow

**Normalize before matching:**
```javascript
{{Email}}.toLowerCase().trim()
```

### Handling Fuzzy Matches

When exact email match fails:
1. Search by name + company combination
2. Use Claygent to verify match
3. Flag for manual review if uncertain

**Formula for flagging potential duplicates:**
```javascript
{{Lookup Result}} === "Multiple Found" ? "Review" : "OK"
```

### Company Deduplication

Companies are harder to dedupe than contacts:

**Strategy 1: Domain matching**
```javascript
{{Website}}.replace(/^https?:\/\/(www\.)?/, "").split("/")[0].toLowerCase()
```

**Strategy 2: Normalized name matching**
```javascript
{{Company}}.toLowerCase()
  .replace(/,?\s*(inc|llc|ltd|corp)\.?\s*$/i, "")
  .replace(/[^\w\s]/g, "")
  .trim()
```

---

## Field Mapping Best Practices

### Standard Field Mappings

| Clay Output | HubSpot Property | Salesforce Field |
|-------------|------------------|------------------|
| Email | email | Email |
| First Name | firstname | FirstName |
| Last Name | lastname | LastName |
| Phone | phone | Phone |
| Mobile | mobilephone | MobilePhone |
| Company | company | Company (Lead) / Account.Name |
| Title | jobtitle | Title |
| LinkedIn URL | hs_linkedinid | LinkedIn_URL__c |
| Website | website | Website |
| Industry | industry | Industry |
| Employee Count | numberofemployees | NumberOfEmployees |

### Custom Field Handling

**HubSpot custom properties:**
- Use internal name (found in property settings)
- Format: lowercase, underscores (e.g., `lead_score_clay`)

**Salesforce custom fields:**
- Use API name ending in `__c`
- Example: `Clay_Enrichment_Date__c`

### Preserving Existing Data

**Critical setting: "Ignore blank values"**

When enabled:
- Empty Clay fields won't overwrite CRM data
- Partial enrichments are safe
- Existing good data is preserved

**When to disable:**
- Intentionally clearing fields
- Full replacement scenarios
- Data cleanup workflows

### Picklist Field Handling

CRM picklists require exact value matches:

**Problem:** Clay returns "Technology" but HubSpot expects "Information Technology"

**Solutions:**
1. Create mapping formula before CRM push:
```javascript
{{Industry}} === "Technology" ? "Information Technology" :
{{Industry}} === "Finance" ? "Financial Services" :
{{Industry}}
```

2. Push to text field first, use CRM workflow to map

3. Create custom text field in CRM for raw values

---

## Sync Scheduling

### Auto-Update Configuration

**For continuous enrichment:**
1. Import from CRM with filter (e.g., last 7 days)
2. Enable "Auto-update" on import
3. Set schedule (daily, hourly)
4. New matching records automatically processed

### Scheduled Imports

**Weekly CRM refresh pattern:**
1. Import contacts modified in last 90 days
2. Run enrichment waterfall
3. Push updates back
4. Schedule to run every Sunday

### Real-Time vs Batch

| Approach | Use Case | Setup |
|----------|----------|-------|
| Real-time (webhook) | Inbound leads, urgent updates | CRM workflow → Clay webhook |
| Batch (scheduled) | CRM refresh, bulk enrichment | Clay scheduled import |
| Manual | One-time projects | Manual import + run |

**Real-time setup:**
1. Create Clay table with webhook source
2. Copy webhook URL
3. In CRM, create workflow trigger
4. POST to Clay webhook on record create/update

---

## Data Integrity

### Preventing Overwrites

**Field-level protection:**
- Enable "Ignore blank values"
- Use conditional updates: only update if new value exists
- Create "enrichment timestamp" field to track changes

**Formula for conditional update:**
```javascript
// Only update if new value is different and non-empty
{{New Value}} && {{New Value}} !== {{Current Value}}
```

### Audit Trails

**Track enrichment activity:**
1. Create "Last Enriched Date" custom field
2. Create "Enrichment Source" field (value: "Clay")
3. Update both on every Clay push

**HubSpot example:**
```
clay_last_enriched    →    {{Today's Date}}
clay_enrichment_source →   "Clay Waterfall v2"
```

### Rollback Strategies

**Before major updates:**
1. Export current CRM data as backup
2. Store in separate Clay table or CSV
3. Test on small batch first
4. Keep rollback table for 30 days

**If errors occur:**
1. Stop Clay workflow
2. Identify affected records (by timestamp)
3. Import backup data
4. Push corrections to CRM

### Error Handling

**Common CRM sync errors:**

| Error | Cause | Solution |
|-------|-------|----------|
| "Contact already exists" | Duplicate not caught | Add lookup step |
| "Invalid property value" | Picklist mismatch | Map values before push |
| "Required field missing" | CRM validation | Ensure required fields populated |
| "Authentication failed" | Token expired | Re-authenticate connection |
| "Rate limit exceeded" | Too many API calls | Reduce batch size, add delays |

**Error notification setup:**
1. Create "Sync Status" column
2. Use formula to detect errors
3. Filter for failed rows
4. Set up Slack notification for failures
