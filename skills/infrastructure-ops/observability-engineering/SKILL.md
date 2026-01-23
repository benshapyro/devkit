# Observability Engineering

OpenTelemetry implementation, structured logging, distributed tracing, and alerting patterns.

## When to Use

Activate when:
- Setting up observability infrastructure
- Implementing OpenTelemetry tracing or metrics
- Designing logging strategies
- Creating alerts and SLOs
- Debugging distributed systems
- Deploying collectors or agents

## Command Routing

| User Request | Action | Reference |
|--------------|--------|-----------|
| "add tracing" or "opentelemetry" | Instrument application | opentelemetry-guide.md |
| "logging" or "log format" | Structured logging setup | structured-logging.md |
| "connect logs and traces" | Correlation patterns | trace-correlation.md |
| "sampling" or "reduce trace volume" | Sampling strategies | sampling-strategies.md |
| "alerts" or "SLO" | Define alerting rules | alerting-patterns.md |
| "collector" or "agent deployment" | Deployment patterns | collector-deployment.md |

## Quick Reference

### Three Pillars of Observability

1. **Traces** - Request flow across services
2. **Metrics** - Aggregated measurements over time
3. **Logs** - Discrete events with context

### OpenTelemetry Core Concepts

```
Trace → Span → Attributes
       ├─ TraceId (shared across spans)
       ├─ SpanId (unique to span)
       ├─ ParentSpanId (links spans)
       └─ Context propagation (W3C traceparent)
```

### Key Metrics to Track

| Category | Metrics |
|----------|---------|
| **RED** | Rate, Errors, Duration |
| **USE** | Utilization, Saturation, Errors |
| **Golden Signals** | Latency, Traffic, Errors, Saturation |

### Log Levels

| Level | Use For |
|-------|---------|
| ERROR | Failures requiring attention |
| WARN | Degraded state, approaching limits |
| INFO | Normal operations, key events |
| DEBUG | Development troubleshooting |

## Reference Files

| File | Content |
|------|---------|
| opentelemetry-guide.md | SDK setup, instrumentation, exporters |
| structured-logging.md | Log formats, context, best practices |
| trace-correlation.md | Linking logs, traces, and metrics |
| sampling-strategies.md | Head, tail, adaptive sampling |
| alerting-patterns.md | SLOs, error budgets, alert design |
| collector-deployment.md | Agent vs gateway, scaling |
