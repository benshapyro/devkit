# Incident Classification

Severity levels, impact criteria, and response expectations.

## Severity Levels

### SEV1 - Critical

**Impact:** Complete service outage or critical data loss risk

**Criteria (any one):**
- Primary revenue stream blocked
- All users affected
- Data corruption or loss occurring
- Security breach in progress
- SLA breach imminent (< 1 hour)

**Response:**
- Immediate all-hands response
- Page entire on-call rotation
- Establish incident commander
- Status page update within 5 minutes
- Executive notification

**Target Resolution:** < 1 hour

### SEV2 - High

**Impact:** Major feature unavailable, significant user impact

**Criteria (any one):**
- Major feature completely broken
- > 25% of users affected
- Performance degraded > 50%
- Payment/checkout impaired
- Critical integration failing

**Response:**
- Page primary on-call immediately
- Secondary on-call available
- Status page update within 15 minutes
- Customer support notified

**Target Resolution:** < 4 hours

### SEV3 - Medium

**Impact:** Feature degraded, workaround available

**Criteria (any one):**
- Feature partially broken
- < 25% of users affected
- Performance degraded < 50%
- Non-critical integration failing
- Elevated error rate (< 5%)

**Response:**
- Primary on-call during business hours
- Next business day if overnight
- No status page (unless customer-facing)

**Target Resolution:** < 24 hours

### SEV4 - Low

**Impact:** Minor issue, minimal user impact

**Criteria:**
- Cosmetic issues
- Edge case failures
- Internal tooling issues
- Warning alerts (not errors)

**Response:**
- Create ticket
- Address in next sprint
- No immediate response needed

**Target Resolution:** < 1 week

---

## Severity Decision Matrix

```
                    User Impact
                    None    Some    Most    All
Business     High   SEV3    SEV2    SEV1    SEV1
Impact       Med    SEV4    SEV3    SEV2    SEV2
             Low    SEV4    SEV4    SEV3    SEV3
```

---

## Impact Assessment

### User Impact

| Level | Description | Examples |
|-------|-------------|----------|
| All | 100% of users | Complete outage |
| Most | > 50% | Region outage, major feature |
| Some | 10-50% | Subset of functionality |
| Few | < 10% | Edge cases, specific flows |
| None | 0% | Internal only |

### Business Impact

| Level | Description | Examples |
|-------|-------------|----------|
| Critical | Revenue/data at immediate risk | Checkout down, data breach |
| High | Significant revenue impact | Search broken, slow checkout |
| Medium | Measurable impact | Minor feature, degraded UX |
| Low | Minimal/no impact | Cosmetic, internal tooling |

---

## Escalation Thresholds

### Time-Based Escalation

| Duration | Action |
|----------|--------|
| 15 min | No progress → Add second responder |
| 30 min | SEV2+ not improving → Escalate to SEV1 procedures |
| 1 hour | SEV1 not resolved → Executive notification |
| 4 hours | Any SEV ongoing → Manager review |

### Condition-Based Escalation

| Condition | Action |
|-----------|--------|
| Unknown root cause after 30 min | Bring in subject matter expert |
| Multiple services affected | Declare cross-team incident |
| External dependency failure | Engage vendor support |
| Data integrity concerns | Involve data team immediately |

---

## Severity Changes

### Upgrading Severity

**Triggers:**
- Impact spreading
- Resolution taking longer than expected
- New symptoms discovered
- Business context changed (e.g., now peak hours)

**Process:**
1. Announce in incident channel
2. Update incident record
3. Page additional responders
4. Notify stakeholders

### Downgrading Severity

**Triggers:**
- Workaround deployed
- Impact contained
- User impact reduced
- Fix deployed, monitoring

**Process:**
1. Confirm with incident commander
2. Update incident record
3. Release non-essential responders
4. Continue monitoring

---

## Classification Examples

### SEV1 Examples

```
❌ "Checkout page returns 500 for all users"
   Impact: All, Revenue: Critical → SEV1

❌ "Database corruption detected, writes failing"
   Impact: All, Data Risk: Critical → SEV1

❌ "Auth service completely down"
   Impact: All, Revenue: Critical → SEV1
```

### SEV2 Examples

```
⚠️ "Search returns no results for 30% of queries"
   Impact: Some, Revenue: High → SEV2

⚠️ "Payment processing slow, 10% of transactions timing out"
   Impact: Some, Revenue: High → SEV2

⚠️ "Mobile app crashes on launch for Android 13"
   Impact: Some, Revenue: Medium → SEV2
```

### SEV3 Examples

```
📋 "Product images not loading for Safari users"
   Impact: Some, Revenue: Low → SEV3

📋 "Email notifications delayed by 30 minutes"
   Impact: Most, Revenue: Low → SEV3

📋 "Admin dashboard slow during peak hours"
   Impact: None (internal), Revenue: None → SEV3
```

### SEV4 Examples

```
📝 "Footer alignment off on mobile"
   Impact: None, Revenue: None → SEV4

📝 "Internal metrics dashboard showing stale data"
   Impact: None, Revenue: None → SEV4
```

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────┐
│  SEVERITY QUICK REFERENCE                       │
├─────────────────────────────────────────────────┤
│                                                 │
│  SEV1: CRITICAL                                 │
│  • Complete outage / data loss                  │
│  • Response: Immediate all-hands               │
│  • Target: < 1 hour                             │
│                                                 │
│  SEV2: HIGH                                     │
│  • Major feature down / >25% users              │
│  • Response: Page on-call                       │
│  • Target: < 4 hours                            │
│                                                 │
│  SEV3: MEDIUM                                   │
│  • Degraded / <25% users / workaround exists    │
│  • Response: Business hours                     │
│  • Target: < 24 hours                           │
│                                                 │
│  SEV4: LOW                                      │
│  • Minor / cosmetic / internal                  │
│  • Response: Ticket                             │
│  • Target: < 1 week                             │
│                                                 │
└─────────────────────────────────────────────────┘
```
