# Troubleshooting

Common Clay errors and their solutions.

## Table of Contents
1. [General Debug Workflow](#general-debug-workflow)
2. [Common Error Messages](#common-error-messages)
3. [Claygent Issues](#claygent-issues)
4. [Waterfall Failures](#waterfall-failures)
5. [Integration Problems](#integration-problems)
6. [Performance Issues](#performance-issues)
7. [When to Contact Support](#when-to-contact-support)

---

## General Debug Workflow

**When something fails, follow this sequence:**

1. **Check Run Info** - Click on failed cell, view "Run Info" panel for exact error
2. **Isolate to Single Row** - Run column on just one failed row
3. **Review Input Data** - Are inputs populated and formatted correctly?
4. **Test Simplified** - For AI columns, reduce prompt to minimum
5. **Check Credits/Limits** - Verify credit balance and API limits
6. **Hard Refresh** - Cmd+Shift+R (Mac) or Ctrl+F5 (Windows)

---

## Common Error Messages

### "Missing inputs"
**Cause:** Required column is empty for that row.
**Fix:** Add fallback `{{Column||"default"}}` or conditional run.

### "Failed to parse body"
**Cause:** JSON formatting issue.
**Fix:** Check for unescaped quotes, simplify output format.

### "Run condition not met"
**Cause:** "Only run if" condition is false.
**Fix:** Verify condition logic and referenced column values.

### "Error evaluating formula"
**Cause:** JavaScript syntax error.
**Fix:** Check typos, add null checks `({{Col}}||"").method()`.

### "Failed to update waterfall"
**Cause:** Loop detection or circular reference.
**Fix:** Check for self-references, rebuild waterfall.

### "Authentication failed"
**Cause:** API key or token expired.
**Fix:** Re-authenticate in Settings → Connections.

### "Rate limit exceeded"
**Cause:** Too many API calls.
**Fix:** Reduce batch size, upgrade API tier, add delays.

---

## Claygent Issues

### Timeouts
**Cause:** API rate limits, complex prompts, slow websites.
**Fixes:**
- BYOK: Upgrade to OpenAI Tier 4+ (450,000 TPM)
- Simplify prompt
- Use Navigator for slow pages
- Reduce batch size

### Hallucinations
**Cause:** Vague prompt, data not on page.
**Fixes:**
- Add rule: "If not found, return 'Not Found'"
- Specify source: "Only use data from {{URL}}"
- Add verification column

### Wrong Page Sections
**Cause:** Homepage too broad, dynamic content.
**Fixes:**
- Use specific URL (/about, /team)
- Add section guidance in prompt
- Use Navigator for interaction-required pages

### "Failed to load page"
**Cause:** Bot blocking, login required.
**Fixes:**
- Try Navigator mode
- Verify URL works manually
- Try alternative URLs (news mentions, etc.)

---

## Waterfall Failures

### Low Hit Rates
**Cause:** Bad input data, hard-to-reach personas, international contacts.
**Fixes:**
- Verify input quality
- Try different provider combinations
- Add Claygent as fallback
- Accept lower coverage for some segments

### Provider-Specific Issues

**Apollo `email_not_unlocked@domain.com`:**
- Contact found but requires Apollo unlock
- Add secondary enrichment or skip to next provider

**Catch-all domains:**
- Enable "Continue on catch-all" or accept catch-all

**Outdated data:**
- Add recency check
- Use multiple providers for verification

---

## Integration Problems

### HubSpot

**"Found 0 objects":**
- Re-authenticate, verify list ID, check object type

**"Invalid property value":**
- Picklist mismatch - map to exact values or use text field

**"Required field missing":**
- Check HubSpot required fields, add defaults

### Salesforce

**"Update failed - record not found":**
- Use Lookup first for Salesforce ID, or use Upsert

**"SOQL query error":**
- Validate syntax, use API field names, check permissions

### Sequencer

**Variables not populating:**
- Check exact name match (case-sensitive)
- Verify column mapping

---

## Performance Issues

### Slow Table Loading
**Fixes:** Archive unused columns, split large tables, use views.

### Stuck Columns
**Fixes:** Hard refresh, cancel and re-run, force restart via column menu.

### Queue Delays
**Fixes:** Check credits, reduce concurrent columns, spread processing.

---

## When to Contact Support

**Contact for:** Platform outages, billing issues, account access, consistent provider errors.

**Before contacting:** Check status.clay.com, search Community, try troubleshooting above.

**Include:** Table URL, column name, row IDs, error message, screenshots.

**Channels:** In-app Intercom chat, support@clay.com, community.clay.com
