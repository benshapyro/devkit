# Alerting Patterns

SLO-based alerting, error budgets, and alert design.

## SLO Fundamentals

### Terminology

| Term | Definition | Example |
|------|------------|---------|
| **SLI** | Service Level Indicator | Request latency p99 |
| **SLO** | Service Level Objective | p99 latency < 200ms |
| **SLA** | Service Level Agreement | 99.9% uptime (contractual) |
| **Error Budget** | Allowable failure | 0.1% of requests can fail |

### SLO Formula

```
SLO = (Good events / Total events) × 100

Error Budget = 1 - SLO
Monthly Budget = Error Budget × Minutes in month

Example:
99.9% SLO → 0.1% error budget
0.1% × 43,200 min = 43.2 minutes of downtime allowed
```

---

## SLI Types

### Availability SLI

```promql
# Successful requests / Total requests
sum(rate(http_requests_total{status!~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
```

### Latency SLI

```promql
# Requests under threshold / Total requests
sum(rate(http_request_duration_seconds_bucket{le="0.2"}[5m]))
/
sum(rate(http_request_duration_seconds_count[5m]))
```

### Quality SLI

```promql
# Correct responses / Total responses
sum(rate(responses_correct_total[5m]))
/
sum(rate(responses_total[5m]))
```

---

## Error Budget Alerting

### Multi-Window, Multi-Burn-Rate

Alert when burning budget faster than sustainable.

```yaml
# Fast burn (high urgency)
# Exhausts 2% of budget in 1 hour
- alert: ErrorBudgetFastBurn
  expr: |
    (
      1 - (sum(rate(http_requests_success[1h])) / sum(rate(http_requests_total[1h])))
    ) > 14.4 * (1 - 0.999)  # 14.4x burn rate
  for: 2m
  labels:
    severity: critical

# Slow burn (lower urgency)
# Exhausts 10% of budget in 6 hours
- alert: ErrorBudgetSlowBurn
  expr: |
    (
      1 - (sum(rate(http_requests_success[6h])) / sum(rate(http_requests_total[6h])))
    ) > 1 * (1 - 0.999)  # 1x burn rate sustained
  for: 30m
  labels:
    severity: warning
```

### Burn Rate Reference

| Window | Burn Rate | Budget Consumed | Alert Type |
|--------|-----------|-----------------|------------|
| 1h | 14.4x | 2% | Page immediately |
| 6h | 6x | 5% | Page |
| 24h | 3x | 10% | Ticket |
| 3d | 1x | 10% | Ticket |

---

## Alert Rules

### Good Alert Criteria

| Criterion | Description |
|-----------|-------------|
| **Actionable** | On-call can fix it |
| **Specific** | Clear what's wrong |
| **Relevant** | Affects users |
| **Timely** | Not too early, not too late |
| **Unique** | Not duplicating other alerts |

### Anti-Patterns

```yaml
# Bad: Symptom without context
- alert: HighCPU
  expr: cpu_usage > 80

# Good: Business impact with context
- alert: OrderProcessingDegraded
  expr: |
    rate(orders_processed_total[5m]) < rate(orders_received_total[5m]) * 0.9
  annotations:
    description: "Order processing falling behind by {{ $value | humanize }}%"
    runbook: "https://wiki/runbooks/orders"
```

---

## Alert Fatigue Prevention

### Grouping

```yaml
# Prometheus Alertmanager
route:
  group_by: ['service', 'alertname']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
```

### Inhibition

```yaml
# Suppress downstream alerts when upstream is down
inhibit_rules:
  - source_match:
      alertname: DatabaseDown
    target_match:
      alertname: APIErrors
    equal: ['cluster']
```

### Silencing

```yaml
# Maintenance window
silences:
  - matchers:
      - name: service
        value: order-service
    startsAt: "2024-01-15T00:00:00Z"
    endsAt: "2024-01-15T02:00:00Z"
    comment: "Planned maintenance"
```

---

## Alert Severity Levels

| Level | Response | Examples |
|-------|----------|----------|
| **Critical** | Immediate page | Complete outage, data loss risk |
| **Warning** | Page during hours | Degraded performance, approaching limits |
| **Info** | Ticket | Non-urgent issues |

### Severity Decision Tree

```
Is there user impact right now?
├─ Yes → Is revenue/data at risk?
│        ├─ Yes → CRITICAL (page immediately)
│        └─ No  → WARNING (page during hours)
└─ No  → Will there be impact if not addressed?
         ├─ Within hours → WARNING
         └─ Within days  → INFO (ticket)
```

---

## Alert Templates

### Prometheus Alert

```yaml
- alert: HighLatency
  expr: |
    histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service)) > 0.5
  for: 5m
  labels:
    severity: warning
    team: platform
  annotations:
    summary: "High latency in {{ $labels.service }}"
    description: "p99 latency is {{ $value | humanizeDuration }} (threshold: 500ms)"
    dashboard: "https://grafana/d/latency?service={{ $labels.service }}"
    runbook: "https://wiki/runbooks/latency"
```

### PagerDuty Integration

```yaml
receivers:
  - name: 'pagerduty-critical'
    pagerduty_configs:
      - service_key: <key>
        severity: critical
        description: '{{ .CommonAnnotations.summary }}'
        details:
          firing: '{{ .Alerts.Firing | len }}'
          resolved: '{{ .Alerts.Resolved | len }}'
```

---

## Dashboards for Alerts

### Alert Overview

```
┌─────────────────────────────────────────────────┐
│  Active Alerts                                  │
│  🔴 2 Critical  🟡 5 Warning  ℹ️ 12 Info        │
├─────────────────────────────────────────────────┤
│  Error Budget Status (30 day)                   │
│  ├─ API Service: ████████░░ 82% remaining       │
│  ├─ Auth Service: ███████░░░ 71% remaining      │
│  └─ Payment: █████░░░░░ 45% remaining ⚠️        │
├─────────────────────────────────────────────────┤
│  Burn Rate (1h)                                 │
│  [Graph showing current vs sustainable rate]    │
└─────────────────────────────────────────────────┘
```

---

## Best Practices

1. **Alert on symptoms, not causes** - "High error rate" not "High CPU"
2. **Include runbook links** - Make alerts actionable
3. **Use error budgets** - Align with SLOs
4. **Review regularly** - Delete unused alerts
5. **Track noise** - Measure alert:incident ratio
6. **On-call health** - Monitor page volume and response times
