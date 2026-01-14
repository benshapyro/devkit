# Automation Patterns

Evolving runbooks from manual to automated remediation.

## Automation Maturity Model

```
Level 0: No Runbook
    ↓
Level 1: Documented Runbook
    ↓
Level 2: Copy-Paste Commands
    ↓
Level 3: Semi-Automated Scripts
    ↓
Level 4: Auto-Remediation with Approval
    ↓
Level 5: Fully Automated Self-Healing
```

---

## Level 2: Copy-Paste Commands

### From Manual to Script

**Before:**
```markdown
1. SSH to server
2. Check disk usage with `df -h`
3. Find large logs with `find /var/log...`
4. Delete old logs
```

**After:**
```bash
#!/bin/bash
# cleanup_logs.sh - Run when disk > 80%

set -e

echo "Current disk usage:"
df -h /

echo "Finding large log files..."
find /var/log -type f -name "*.log" -size +100M -exec ls -lh {} \;

echo "Cleaning logs older than 7 days..."
find /var/log -type f -name "*.log" -mtime +7 -delete

echo "New disk usage:"
df -h /
```

---

## Level 3: Semi-Automated Scripts

### Scripts with Safety Checks

```bash
#!/bin/bash
# restart_service.sh - Safe service restart

SERVICE=$1
NAMESPACE=${2:-default}

# Safety checks
if [ -z "$SERVICE" ]; then
    echo "Usage: $0 <service-name> [namespace]"
    exit 1
fi

# Pre-check: Is service actually unhealthy?
UNHEALTHY=$(kubectl get pods -n "$NAMESPACE" -l "app=$SERVICE" \
    -o jsonpath='{.items[*].status.containerStatuses[*].ready}' | grep -c false || true)

if [ "$UNHEALTHY" -eq 0 ]; then
    echo "⚠️  All pods appear healthy. Continue anyway? (y/N)"
    read -r response
    if [ "$response" != "y" ]; then
        exit 0
    fi
fi

# Take action
echo "Restarting $SERVICE in $NAMESPACE..."
kubectl rollout restart deployment/"$SERVICE" -n "$NAMESPACE"

# Wait and verify
echo "Waiting for rollout to complete..."
kubectl rollout status deployment/"$SERVICE" -n "$NAMESPACE" --timeout=300s

# Post-check
echo "Verifying pods are healthy..."
kubectl get pods -n "$NAMESPACE" -l "app=$SERVICE"
```

---

## Level 4: Auto-Remediation with Approval

### Slack-Integrated Remediation

```python
#!/usr/bin/env python3
"""
Auto-remediation with Slack approval.
Triggered by alert, asks for confirmation, then executes.
"""

import os
import subprocess
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack = WebClient(token=os.environ["SLACK_TOKEN"])
CHANNEL = "#sre-alerts"

def request_approval(incident_id: str, action: str, details: str) -> bool:
    """Post to Slack and wait for approval."""

    message = slack.chat_postMessage(
        channel=CHANNEL,
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"🤖 *Auto-Remediation Request*\n\n"
                            f"*Incident:* {incident_id}\n"
                            f"*Action:* {action}\n"
                            f"*Details:* {details}"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "✅ Approve"},
                        "style": "primary",
                        "action_id": f"approve_{incident_id}"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "❌ Deny"},
                        "style": "danger",
                        "action_id": f"deny_{incident_id}"
                    }
                ]
            }
        ]
    )

    # In practice, wait for webhook callback
    # This is simplified - real implementation uses Slack interactivity

    return True  # Assume approved for example


def remediate_high_memory(pod_name: str, namespace: str):
    """Restart pod with high memory usage."""

    action = f"Restart pod {pod_name}"
    details = f"Memory usage exceeded threshold in namespace {namespace}"

    if request_approval("INC-001", action, details):
        result = subprocess.run(
            ["kubectl", "delete", "pod", pod_name, "-n", namespace],
            capture_output=True, text=True
        )

        slack.chat_postMessage(
            channel=CHANNEL,
            text=f"✅ Remediation complete: {action}\n```{result.stdout}```"
        )
    else:
        slack.chat_postMessage(
            channel=CHANNEL,
            text=f"⏸️ Remediation denied for {pod_name}"
        )
```

---

## Level 5: Fully Automated Self-Healing

### Kubernetes-Native Auto-Healing

```yaml
# Horizontal Pod Autoscaler - Auto-scale on CPU
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api
  minReplicas: 3
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70

---
# Pod Disruption Budget - Safe during updates
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: api-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: api
```

### Alert-Driven Automation

```yaml
# Prometheus + Alertmanager webhook
alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']

# Alertmanager routes to auto-remediation
route:
  receiver: 'auto-remediation'
  routes:
    - match:
        auto_remediate: "true"
      receiver: 'remediation-webhook'

receivers:
  - name: 'remediation-webhook'
    webhook_configs:
      - url: 'http://remediation-service/webhook'
        send_resolved: true
```

---

## Automation Checklist

### Before Automating

- [ ] Runbook is stable (no changes in 30+ days)
- [ ] Action is safe (reversible, no data loss)
- [ ] Detection is reliable (low false positive rate)
- [ ] Action is well-tested (run manually 10+ times)
- [ ] Timeout/circuit breaker in place

### Automation Safety

```python
# Always include safety limits
MAX_EXECUTIONS_PER_HOUR = 5
MIN_INTERVAL_SECONDS = 300
REQUIRE_APPROVAL_AFTER = 2  # Auto first 2, then ask

# Always have an escape hatch
if os.path.exists("/tmp/disable-auto-remediation"):
    log("Auto-remediation disabled by flag file")
    return

# Always notify
slack.post(f"🤖 Auto-remediation triggered: {action}")

# Always log
logger.info(f"Auto-remediation: action={action}, trigger={trigger}")
```

---

## Metrics for Automation

### Track Automation Effectiveness

| Metric | Good Target |
|--------|-------------|
| Auto-remediation success rate | > 90% |
| False positive rate | < 5% |
| Mean time to remediate | < 2 minutes |
| Human escalation rate | < 20% |
| Incidents prevented | Track monthly |

```promql
# Success rate
sum(auto_remediation_success_total) / sum(auto_remediation_attempts_total)

# Escalation rate
sum(auto_remediation_escalated_total) / sum(auto_remediation_attempts_total)
```

---

## Common Auto-Remediation Actions

| Trigger | Safe Auto-Action | Requires Approval |
|---------|------------------|-------------------|
| Pod unhealthy | Restart pod | Scale down |
| Memory > 90% | Restart pod | Increase limits |
| CPU > 90% | Scale up HPA | - |
| Disk > 80% | Clean old logs | Clean data |
| Connection pool exhausted | Restart app | Increase pool |
| Certificate expiring | Renew (Let's Encrypt) | Manual certs |
| Config drift | Reconcile | - |

---

## Evolution Path

1. **Start simple** - Automate the most common, safest actions
2. **Measure first** - Track success/failure before expanding
3. **Require approval initially** - Remove after proven safe
4. **Add circuit breakers** - Prevent runaway automation
5. **Iterate** - Continuously improve based on metrics
