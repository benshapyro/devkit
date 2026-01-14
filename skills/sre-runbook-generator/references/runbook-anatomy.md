# Runbook Anatomy

Complete structure and components of effective runbooks.

## Runbook Template

```markdown
# [Service Name]: [Issue Title]

**Last Updated:** YYYY-MM-DD
**Owner:** @team-name
**Severity Guide:** See incident-classification.md

---

## Overview

**Service:** [Service name and brief description]
**Purpose:** [What this runbook addresses]
**Impact:** [What happens if not resolved]

---

## Detection

### Alerting
- **Alert Name:** [Prometheus/PagerDuty alert]
- **Threshold:** [When alert fires]
- **Dashboard:** [Link to dashboard]

### Symptoms
- [ ] [Observable symptom 1]
- [ ] [Observable symptom 2]
- [ ] [Observable symptom 3]

---

## Quick Checks (< 5 minutes)

1. **Check service health**
   ```bash
   kubectl get pods -l app=service-name
   curl -s http://service:8080/health | jq .
   ```

2. **Check recent deployments**
   ```bash
   kubectl rollout history deployment/service-name
   ```

3. **Check logs for errors**
   ```bash
   kubectl logs -l app=service-name --tail=100 | grep -i error
   ```

---

## Diagnostic Steps

### Step 1: [First diagnostic action]

**Purpose:** [Why we're doing this]

```bash
# Command to run
command --with-flags
```

**Expected output:**
```
What you should see if things are working
```

**If abnormal:** Proceed to [section/step]

### Step 2: [Second diagnostic action]

...continue pattern...

---

## Remediation

### Option A: [Most common fix]

**When to use:** [Conditions that indicate this fix]

1. [Step 1]
   ```bash
   command
   ```

2. [Step 2]
   ```bash
   command
   ```

3. **Verify:**
   ```bash
   verification-command
   ```

### Option B: [Alternative fix]

**When to use:** [Different conditions]

...steps...

### Option C: Rollback

**When to use:** Recent deployment suspected

```bash
kubectl rollout undo deployment/service-name
```

---

## Escalation

| Condition | Action | Contact |
|-----------|--------|---------|
| [Condition 1] | [Action] | @team |
| [Condition 2] | [Action] | @manager |
| [After X minutes] | [Action] | @on-call |

---

## Post-Incident

- [ ] Verify service recovered
- [ ] Check error rates returned to baseline
- [ ] Document what happened in incident channel
- [ ] Create follow-up ticket if needed
- [ ] Update runbook if gaps found

---

## Related Resources

- [Architecture doc]
- [Dependency map]
- [Previous incidents]
```

---

## Section Details

### Overview Section

Must answer:
- What service/component does this cover?
- What problem does this runbook solve?
- What's the business impact?

```markdown
## Overview

**Service:** Order Processing Service (order-service)
**Purpose:** Handles customer order creation, validation, and fulfillment triggers
**Impact:** Orders cannot be placed; revenue loss of ~$50k/hour during peak
```

### Detection Section

Include:
- Exact alert names (copy-paste from alerting system)
- Threshold values
- Dashboard links
- Observable symptoms (what users see)

### Quick Checks

Time-boxed initial investigation:
- Should take < 5 minutes total
- Copy-paste commands
- Common causes first
- If negative, move to full diagnostics

### Diagnostic Steps

Structured troubleshooting:
- One action per step
- Explain WHY (helps responder learn)
- Include expected output
- Branch on results

### Remediation

Multiple options ranked by:
1. Safety (safest first)
2. Frequency (most common first)
3. Speed (quickest first)

Always include:
- Rollback option
- Verification steps

---

## Writing Guidelines

### Commands Must Be Copy-Pasteable

```bash
# Bad - requires substitution
kubectl logs -l app=$SERVICE_NAME

# Good - complete command
kubectl logs -l app=order-service --tail=100
```

### Use Checklists for Multi-Step

```markdown
- [ ] Stop traffic to service
- [ ] Take database backup
- [ ] Run migration
- [ ] Verify data integrity
- [ ] Restore traffic
```

### Include Time Estimates

```markdown
### Option A: Restart Pod (~2 min)
### Option B: Scale Down/Up (~5 min)
### Option C: Full Rollback (~15 min)
```

### Link Don't Duplicate

```markdown
For database connection issues, see:
[Database Runbook: Connection Pool Exhaustion](./db-connection-pool.md)
```

---

## Runbook Review Checklist

- [ ] Title clearly describes the issue
- [ ] Last updated date is current (< 90 days)
- [ ] Owner is assigned
- [ ] All commands are tested and work
- [ ] Expected outputs are accurate
- [ ] Escalation contacts are current
- [ ] Links to dashboards work
- [ ] No sensitive credentials included
- [ ] Rollback procedure tested
- [ ] Post-incident steps included
