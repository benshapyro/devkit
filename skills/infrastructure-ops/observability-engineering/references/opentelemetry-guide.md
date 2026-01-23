# OpenTelemetry Guide

Complete guide to instrumenting applications with OpenTelemetry.

## Core Concepts

### Signal Types

| Signal | Purpose | Examples |
|--------|---------|----------|
| **Traces** | Request flow | API call → DB query → response |
| **Metrics** | Aggregated measurements | Request count, latency histogram |
| **Logs** | Discrete events | Error messages, audit logs |

### Trace Components

```
Trace (TraceId: abc123)
├── Span A (SpanId: 001, root)
│   ├── Span B (SpanId: 002, parent: 001)
│   │   └── Span C (SpanId: 003, parent: 002)
│   └── Span D (SpanId: 004, parent: 001)
```

---

## SDK Setup

### Node.js

```javascript
// tracing.js - Load before application code
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http');
const { OTLPMetricExporter } = require('@opentelemetry/exporter-metrics-otlp-http');
const { PeriodicExportingMetricReader } = require('@opentelemetry/sdk-metrics');

const sdk = new NodeSDK({
  serviceName: 'my-service',
  traceExporter: new OTLPTraceExporter({
    url: 'http://localhost:4318/v1/traces',
  }),
  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter({
      url: 'http://localhost:4318/v1/metrics',
    }),
    exportIntervalMillis: 10000,
  }),
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();

process.on('SIGTERM', () => {
  sdk.shutdown().then(() => process.exit(0));
});
```

### Python

```python
# tracing.py
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

resource = Resource.create({
    "service.name": "my-service",
    "service.version": "1.0.0",
})

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317"))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)
```

---

## Manual Instrumentation

### Creating Spans

```javascript
const { trace } = require('@opentelemetry/api');

const tracer = trace.getTracer('my-component');

async function processOrder(orderId) {
  return tracer.startActiveSpan('process-order', async (span) => {
    try {
      span.setAttribute('order.id', orderId);

      await validateOrder(orderId);
      await chargePayment(orderId);

      span.setStatus({ code: SpanStatusCode.OK });
      return { success: true };
    } catch (error) {
      span.setStatus({ code: SpanStatusCode.ERROR, message: error.message });
      span.recordException(error);
      throw error;
    } finally {
      span.end();
    }
  });
}
```

### Adding Attributes

```javascript
span.setAttribute('user.id', userId);
span.setAttribute('db.statement', query);
span.setAttribute('http.status_code', 200);

// Semantic conventions
span.setAttribute('http.method', 'GET');
span.setAttribute('http.url', '/api/users');
span.setAttribute('http.status_code', 200);
span.setAttribute('db.system', 'postgresql');
span.setAttribute('db.name', 'users');
```

### Recording Events

```javascript
span.addEvent('cache_hit', {
  'cache.key': cacheKey,
  'cache.ttl': 3600,
});

span.addEvent('retry_attempt', {
  'attempt.number': 2,
  'retry.reason': 'timeout',
});
```

---

## Auto-Instrumentation

### Node.js Libraries

```javascript
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');

// Instruments: http, express, pg, mysql, redis, mongodb, etc.
instrumentations: [
  getNodeAutoInstrumentations({
    '@opentelemetry/instrumentation-fs': { enabled: false },
    '@opentelemetry/instrumentation-http': {
      ignoreIncomingPaths: ['/health', '/metrics'],
    },
  }),
]
```

### Python Libraries

```python
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor

FlaskInstrumentor().instrument_app(app)
SQLAlchemyInstrumentor().instrument(engine=engine)
RedisInstrumentor().instrument()
```

---

## Context Propagation

### W3C Trace Context

```
traceparent: 00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01
            │  │                                │                 │
            │  │                                │                 └─ flags (sampled)
            │  │                                └─ parent span id
            │  └─ trace id
            └─ version
```

### Propagating Context

```javascript
const { propagation, context } = require('@opentelemetry/api');

// Inject into outgoing request
const headers = {};
propagation.inject(context.active(), headers);
// headers now contains traceparent

// Extract from incoming request
const extractedContext = propagation.extract(context.active(), request.headers);
context.with(extractedContext, () => {
  // Spans created here are linked to the trace
});
```

---

## Metrics

### Counter

```javascript
const { metrics } = require('@opentelemetry/api');

const meter = metrics.getMeter('my-service');

const requestCounter = meter.createCounter('http_requests_total', {
  description: 'Total HTTP requests',
});

requestCounter.add(1, { 'http.method': 'GET', 'http.route': '/api/users' });
```

### Histogram

```javascript
const latencyHistogram = meter.createHistogram('http_request_duration_ms', {
  description: 'HTTP request latency',
  unit: 'ms',
});

const start = Date.now();
await handleRequest();
latencyHistogram.record(Date.now() - start, { 'http.method': 'GET' });
```

### Gauge

```javascript
const queueSize = meter.createObservableGauge('queue_size', {
  description: 'Current queue size',
});

queueSize.addCallback((result) => {
  result.observe(getQueueSize(), { 'queue.name': 'orders' });
});
```

---

## Exporters

| Exporter | Protocol | Use Case |
|----------|----------|----------|
| OTLP | gRPC/HTTP | Standard, recommended |
| Jaeger | Thrift/gRPC | Legacy Jaeger |
| Zipkin | HTTP | Legacy Zipkin |
| Console | stdout | Development |
| Prometheus | Pull | Metrics only |

### OTLP Configuration

```javascript
// HTTP (port 4318)
new OTLPTraceExporter({
  url: 'http://collector:4318/v1/traces',
});

// gRPC (port 4317)
new OTLPTraceExporter({
  url: 'grpc://collector:4317',
});
```

---

## Best Practices

1. **Start with auto-instrumentation** - Add manual spans later
2. **Use semantic conventions** - Standard attribute names
3. **Set service.name** - Essential for filtering
4. **Sample appropriately** - 100% sampling is expensive
5. **Batch exports** - Don't export every span immediately
6. **Graceful shutdown** - Flush spans before exit
