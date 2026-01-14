# Sampling Strategies

Reduce observability costs while maintaining visibility.

## Why Sample?

At scale, 100% trace collection is:
- Expensive (storage, processing)
- Often unnecessary (most requests are normal)
- Potentially overwhelming (too much data)

Sampling captures representative data at lower cost.

---

## Sampling Types

### Head Sampling

Decision made at trace start (before any spans exist).

```
Request arrives → Random decision → Keep or drop entire trace
```

**Pros:**
- Simple implementation
- Low overhead
- Consistent (all spans in trace sampled)

**Cons:**
- May miss important traces
- No visibility into request importance

### Tail Sampling

Decision made after trace completes.

```
Request completes → Analyze trace → Keep interesting, drop boring
```

**Pros:**
- Keep errors, slow requests
- Context-aware decisions
- Better signal-to-noise ratio

**Cons:**
- Higher resource usage
- Requires collector buffering
- More complex setup

---

## Head Sampling Strategies

### Probabilistic (Rate-Based)

```yaml
# OpenTelemetry Collector
processors:
  probabilistic_sampler:
    sampling_percentage: 10  # Keep 10% of traces
```

```javascript
// SDK configuration
const sampler = new TraceIdRatioBased(0.1); // 10%
```

### Parent-Based

Child spans inherit parent's sampling decision.

```javascript
const sampler = new ParentBased({
  root: new TraceIdRatioBased(0.1),
  remoteParentSampled: new AlwaysOnSampler(),
  remoteParentNotSampled: new AlwaysOffSampler(),
});
```

### Rule-Based

Different rates for different conditions.

```javascript
const sampler = new CompositeSampler([
  // Always sample errors
  { condition: (span) => span.attributes['error'], sampler: AlwaysOn },
  // Sample 50% of specific endpoints
  { condition: (span) => span.name === '/api/checkout', sampler: TraceIdRatioBased(0.5) },
  // Sample 1% of everything else
  { condition: () => true, sampler: TraceIdRatioBased(0.01) },
]);
```

---

## Tail Sampling Strategies

### OpenTelemetry Collector Config

```yaml
processors:
  tail_sampling:
    decision_wait: 10s              # Wait for trace completion
    num_traces: 100000              # Buffer size
    expected_new_traces_per_sec: 1000
    policies:
      # Keep all errors
      - name: errors
        type: status_code
        status_code:
          status_codes: [ERROR]

      # Keep slow requests
      - name: slow-requests
        type: latency
        latency:
          threshold_ms: 1000

      # Sample 10% of normal requests
      - name: probabilistic
        type: probabilistic
        probabilistic:
          sampling_percentage: 10

      # Always keep specific routes
      - name: important-routes
        type: string_attribute
        string_attribute:
          key: http.route
          values: ["/api/checkout", "/api/payment"]
```

### Policy Evaluation Order

```
Trace completes
    ↓
Evaluate policy 1 → Keep? Done
    ↓ (no)
Evaluate policy 2 → Keep? Done
    ↓ (no)
... continue until match or drop
```

---

## Adaptive Sampling

Adjust rates based on conditions.

### Load-Based

```python
def get_sample_rate():
    current_load = get_request_rate()

    if current_load < 100:
        return 1.0    # 100% during low traffic
    elif current_load < 1000:
        return 0.1    # 10% during normal traffic
    else:
        return 0.01   # 1% during high traffic
```

### Error-Budget Based

```python
def should_sample(error_occurred):
    if error_occurred:
        return True  # Always sample errors

    error_budget_remaining = get_error_budget()

    if error_budget_remaining < 0.1:  # Budget nearly exhausted
        return True  # Sample everything, we need visibility
    else:
        return random.random() < 0.1  # Normal 10% sampling
```

---

## Sampling Patterns

### Priority Sampling

```javascript
const PRIORITY = {
  CRITICAL: { rate: 1.0, reason: 'critical-path' },
  HIGH: { rate: 0.5, reason: 'important' },
  MEDIUM: { rate: 0.1, reason: 'normal' },
  LOW: { rate: 0.01, reason: 'background' },
};

function getPriority(request) {
  if (request.path.includes('/checkout')) return PRIORITY.CRITICAL;
  if (request.path.includes('/api')) return PRIORITY.HIGH;
  if (request.path.includes('/static')) return PRIORITY.LOW;
  return PRIORITY.MEDIUM;
}
```

### Debug Sampling

```javascript
// Force sample via header
if (request.headers['x-debug-trace'] === 'true') {
  span.setAttribute('debug', true);
  // Tail sampler keeps all debug traces
}
```

---

## Sampling Metrics

Track sampling to understand data loss.

```javascript
const sampledCounter = meter.createCounter('traces_sampled_total');
const droppedCounter = meter.createCounter('traces_dropped_total');

function recordSamplingDecision(sampled, reason) {
  if (sampled) {
    sampledCounter.add(1, { reason });
  } else {
    droppedCounter.add(1, { reason });
  }
}
```

### Key Metrics to Monitor

| Metric | Description |
|--------|-------------|
| `traces_sampled_total` | Traces kept |
| `traces_dropped_total` | Traces discarded |
| `sampling_rate` | Current sample rate |
| `trace_buffer_size` | Tail sampling buffer usage |

---

## Cost Optimization

### Calculation

```
Daily traces = requests_per_second × 86400
Sampled traces = Daily traces × sample_rate
Storage = Sampled traces × avg_trace_size
Cost = Storage × price_per_GB
```

### Example

```
100,000 req/s × 86400 = 8.64B traces/day
8.64B × 0.01 (1%) = 86.4M sampled traces
86.4M × 10KB = 864TB/day (unsampled)
86.4M × 10KB × 0.01 = 8.64TB/day (1% sampled)
```

---

## Recommendations

| Traffic Level | Head Sample | Tail Sample |
|---------------|-------------|-------------|
| < 1K req/s | 100% | Optional |
| 1K - 10K req/s | 10-50% | Errors + slow |
| 10K - 100K req/s | 1-10% | Errors + slow + 1% |
| > 100K req/s | 0.1-1% | Errors + slow + 0.1% |

### Best Practices

1. **Start high, reduce gradually** - Understand baseline first
2. **Always keep errors** - Never sample away problems
3. **Keep slow traces** - Performance issues need visibility
4. **Use consistent parent-based** - Don't fragment traces
5. **Monitor dropped traces** - Know what you're missing
6. **Debug headers** - Allow forcing full traces
