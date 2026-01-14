# Escalation Procedures

Contact chains, escalation timing, and communication protocols.

## Escalation Ladder

```
Level 1: Primary On-Call
    ↓ (15 min no response or no progress)
Level 2: Secondary On-Call + Team Lead
    ↓ (30 min no resolution for SEV1/2)
Level 3: Engineering Manager + Cross-Team SMEs
    ↓ (1 hour for SEV1)
Level 4: VP/Director + Executive Notification
```

---

## Contact Templates

### On-Call Rotation

```markdown
## Order Service On-Call

**Primary:**
- Week of 01/15: @alice (slack) | +1-555-0100
- Week of 01/22: @bob (slack) | +1-555-0101

**Secondary:**
- @charlie (slack) | +1-555-0102

**Escalation:**
- Team Lead: @david | +1-555-0103
- Manager: @eve | +1-555-0104
```

### Subject Matter Experts

```markdown
## SME Directory

| Domain | Primary | Backup | Contact |
|--------|---------|--------|---------|
| Database | @dba-alice | @dba-bob | #db-support |
| Network | @net-team | — | #network-ops |
| Security | @security | — | #security-oncall |
| Payment | @pay-team | — | #payments |
| Auth | @auth-owner | @auth-backup | #auth-team |
```

---

## Escalation Timing

### SEV1 Escalation Timeline

| Time | Action | Who |
|------|--------|-----|
| 0 min | Page primary on-call | Alerting system |
| 5 min | No ack → page secondary | Alerting system |
| 10 min | No ack → phone call | Incident commander |
| 15 min | Still stuck → add SME | Primary on-call |
| 30 min | Not improving → manager | Primary on-call |
| 1 hour | Not resolved → VP/Director | Manager |

### SEV2 Escalation Timeline

| Time | Action | Who |
|------|--------|-----|
| 0 min | Page primary on-call | Alerting system |
| 15 min | No ack → page secondary | Alerting system |
| 30 min | Still stuck → add SME | Primary on-call |
| 1 hour | Not improving → manager | Primary on-call |
| 4 hours | Not resolved → escalate severity | Manager |

---

## Communication Templates

### Initial Page Message

```
🚨 [SEV1/2/3] [Service]: [Issue]

Impact: [Who/what is affected]
Started: [Time]
Dashboard: [Link]
Incident channel: #inc-YYYYMMDD-service

Page SME with: /pd trigger order-service
```

### Escalation Request

```
🔺 Escalation Request - [Incident ID]

Current Status: [Brief summary]
Duration: [Time elapsed]
Blocker: [What's preventing resolution]
Help Needed: [Specific expertise required]

Incident Channel: #inc-YYYYMMDD-service
```

### Status Update Template

```
📊 Status Update - [Incident ID] - [Time]

Status: [Investigating/Identified/Mitigating/Resolved]
Impact: [Current user/business impact]
Next Steps: [What's happening now]
ETA: [If known, otherwise "TBD"]

Timeline:
- [Time]: [Action taken]
- [Time]: [Action taken]
```

### Customer Communication (SEV1/2)

```
[Service] - Investigating [Issue Type]

We are aware of an issue affecting [description].
Our team is actively investigating.

Impact: [What users might experience]
Workaround: [If available]

We will provide updates every [15/30/60] minutes.

Posted: [Time] | Updated: [Time]
```

---

## Escalation Channels

### PagerDuty Commands

```bash
# Page a specific service
pd trigger --service order-service

# Add responder to incident
pd responder add --incident 12345 --user @alice

# Escalate to next level
pd escalate --incident 12345
```

### Slack Integration

```
# Create incident channel
/incident create [title]

# Page from Slack
/pd trigger [service] "[message]"

# Add to incident
/incident add @user
```

---

## When to Escalate

### Technical Escalation

| Condition | Escalate To |
|-----------|-------------|
| Database issues | @dba-oncall |
| Network/DNS issues | @net-oncall |
| Security concern | @security-oncall |
| Third-party API | Vendor support |
| Unknown codebase | Original author/team |

### Severity Escalation

| Condition | Action |
|-----------|--------|
| Impact spreading | Upgrade severity |
| New symptoms found | Reassess severity |
| Customer complaints increasing | Consider upgrade |
| Resolution taking 2x expected | Reassess and escalate |

### Management Escalation

| Condition | Escalate To |
|-----------|-------------|
| Need business decision | Product manager |
| Resource conflict | Engineering manager |
| External communication needed | Comms team |
| Legal/compliance concern | Legal team |
| Data breach suspected | Security + Legal |

---

## Escalation Anti-Patterns

### Don't

- **Heroics** - Struggling alone for hours
- **Assumption** - "They're probably already aware"
- **Hesitation** - "I don't want to bother anyone"
- **Blame** - Escalating to assign fault
- **Incomplete** - Escalating without context

### Do

- **Escalate early** - Better to over-escalate
- **Bring context** - Summary, timeline, attempts
- **Be specific** - What help do you need?
- **Stay engaged** - Don't hand off and disappear
- **Document** - Note escalation in incident timeline

---

## Post-Escalation

### Handoff Checklist

- [ ] Brief new responder on status
- [ ] Share incident channel
- [ ] Share relevant logs/dashboards
- [ ] Explain what's been tried
- [ ] Clarify current hypothesis
- [ ] Remain available for questions

### Return to Normalcy

When incident resolved:
1. Confirm with all responders
2. Update status page
3. Notify stakeholders
4. Schedule post-mortem (SEV1/2)
5. Return on-call to normal rotation
