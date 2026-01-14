# Trace Correlation

Connecting logs, traces, and metrics for unified observability.

## The Problem

Without correlation:
- Logs show "Error in service A"
- Traces show slow requests
- Metrics show latency spike
- **But which are related?**

With correlation:
- Single trace ID links all signals
- Click from error log → full trace
- Click from trace → related logs

---

## Correlation IDs

### Types

| ID | Scope | Purpose |
|----|-------|---------|
| **Trace ID** | Full request chain | Links all spans across services |
| **Span ID** | Single operation | Links logs to specific span |
| **Request ID** | Single service | Internal request tracking |

### ID Format (W3C Trace Context)

```
Trace ID: 32 hex chars (128-bit)
Span ID:  16 hex chars (64-bit)

Example:
trace_id: 4bf92f3577b34da6a3ce929d0e0e4736
span_id:  00f067aa0ba902b7
```

---

## Implementing Correlation

### Logs with Trace Context

```javascript
const { trace, context } = require('@opentelemetry/api');

function getTraceContext() {
  const span = trace.getSpan(context.active());
  if (!span) return {};

  const spanContext = span.spanContext();
  return {
    trace_id: spanContext.traceId,
    span_id: spanContext.spanId,
  };
}

// Custom logger with automatic trace injection
const logger = {
  info: (data, message) => {
    console.log(JSON.stringify({
      ...data,
      ...getTraceContext(),
      level: 'info',
      message,
      timestamp: new Date().toISOString(),
    }));
  },
  // ... other levels
};
```

### Python Implementation

```python
from opentelemetry import trace

class TraceContextFilter(logging.Filter):
    def filter(self, record):
        span = trace.get_current_span()
        if span.is_recording():
            ctx = span.get_span_context()
            record.trace_id = format(ctx.trace_id, '032x')
            record.span_id = format(ctx.span_id, '016x')
        else:
            record.trace_id = "0" * 32
            record.span_id = "0" * 16
        return True

# Add to logger
handler.addFilter(TraceContextFilter())
```

---

## Metrics with Trace Exemplars

Exemplars link metrics to specific traces.

### Recording Exemplars

```javascript
const { metrics, context } = require('@opentelemetry/api');

const histogram = meter.createHistogram('http_request_duration_ms');

function recordLatency(duration, attributes) {
  // Exemplar automatically captured from active span
  histogram.record(duration, attributes, context.active());
}
```

### Viewing in Prometheus/Grafana

```promql
# Query with exemplars
histogram_quantile(0.99, http_request_duration_ms_bucket)
```

Grafana shows clickable trace links on high-latency data points.

---

## Cross-Service Propagation

### HTTP Headers

```javascript
// Outgoing request
const { propagation, context } = require('@opentelemetry/api');

async function callDownstream(url, data) {
  const headers = {};
  propagation.inject(context.active(), headers);

  return fetch(url, {
    method: 'POST',
    headers: {
      ...headers,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
}
```

### Message Queues

```javascript
// Publishing
async function publishMessage(queue, message) {
  const headers = {};
  propagation.inject(context.active(), headers);

  await channel.sendToQueue(queue, Buffer.from(JSON.stringify({
    ...message,
    _traceContext: headers,
  })));
}

// Consuming
channel.consume(queue, (msg) => {
  const content = JSON.parse(msg.content.toString());
  const ctx = propagation.extract(context.active(), content._traceContext);

  context.with(ctx, () => {
    processMessage(content);
  });
});
```

---

## Unified Query Patterns

### Loki + Tempo (Grafana)

```logql
# Find logs for a trace
{service="order-service"} | json | trace_id="abc123"

# Jump to trace
# Click trace_id → Opens Tempo
```

### Elasticsearch + Jaeger

```json
{
  "query": {
    "bool": {
      "must": [
        { "match": { "trace_id": "abc123" } },
        { "match": { "level": "error" } }
      ]
    }
  }
}
```

### Datadog

```
trace_id:abc123 service:order-service
```

---

## Dashboard Design

### Unified View Layout

```
┌─────────────────────────────────────────────────┐
│  Request: POST /api/orders                      │
│  Trace ID: abc123                               │
├─────────────────────────────────────────────────┤
│  ┌───────────────────┐  ┌────────────────────┐  │
│  │    Trace View     │  │   Metrics Panel    │  │
│  │                   │  │                    │  │
│  │  [service-a]      │  │  Latency: 245ms    │  │
│  │    └─[db-query]   │  │  Status: 500       │  │
│  │    └─[service-b]  │  │  Error rate: 0.1%  │  │
│  │      └─[redis]    │  │                    │  │
│  └───────────────────┘  └────────────────────┘  │
├─────────────────────────────────────────────────┤
│  Related Logs                                   │
│  ┌─────────────────────────────────────────────┐│
│  │ 10:00:00 INFO  Request started              ││
│  │ 10:00:01 DEBUG Cache miss for user-123      ││
│  │ 10:00:01 ERROR Payment declined             ││
│  │ 10:00:02 ERROR Request failed               ││
│  └─────────────────────────────────────────────┘│
└─────────────────────────────────────────────────┘
```

---

## Troubleshooting Workflow

### 1. Start from Alert

```
Alert: High error rate in order-service
→ Click "View traces" on alert
→ See slow/erroring traces
```

### 2. Start from Trace

```
Trace shows 500 error in payment-service
→ Click span → "View logs"
→ See detailed error message
```

### 3. Start from Logs

```
Log: "Payment declined" with trace_id
→ Click trace_id
→ See full request flow
→ Find root cause in upstream service
```

---

## Best Practices

1. **Always propagate context** - Use auto-instrumentation
2. **Log trace IDs** - Enable log → trace navigation
3. **Use exemplars** - Enable metric → trace navigation
4. **Consistent timestamps** - Use UTC ISO format
5. **Same retention** - Keep logs, traces, metrics aligned
6. **Unified tooling** - Use integrated observability platform
