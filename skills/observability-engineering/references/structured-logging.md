# Structured Logging

Best practices for structured, queryable logs.

## Why Structured Logging

```
# Unstructured (bad)
[2024-01-13 10:00:00] ERROR Failed to process order 12345 for user john@example.com

# Structured (good)
{
  "timestamp": "2024-01-13T10:00:00Z",
  "level": "error",
  "message": "Failed to process order",
  "order_id": "12345",
  "user_email": "john@example.com",
  "error": "payment_declined"
}
```

**Benefits:**
- Machine-parseable
- Filterable by any field
- Easy to aggregate
- Consistent format

---

## Log Levels

| Level | When to Use | Examples |
|-------|-------------|----------|
| **FATAL** | App cannot continue | Missing config, DB unreachable at startup |
| **ERROR** | Operation failed | Payment failed, external API error |
| **WARN** | Degraded state | Retry succeeded, approaching limits |
| **INFO** | Normal operations | Request handled, user logged in |
| **DEBUG** | Development detail | Function entry/exit, variable values |
| **TRACE** | Verbose debugging | Loop iterations, fine-grained flow |

### Level Guidelines

```javascript
// ERROR - Something broke, needs attention
logger.error('Payment processing failed', { orderId, error: err.message });

// WARN - Not broken, but concerning
logger.warn('Retry succeeded after 3 attempts', { orderId, attempts: 3 });

// INFO - Normal, notable events
logger.info('Order completed', { orderId, total: 99.99 });

// DEBUG - Development troubleshooting
logger.debug('Cache miss, fetching from DB', { userId });
```

---

## Standard Fields

### Required Fields

```json
{
  "timestamp": "2024-01-13T10:00:00.000Z",
  "level": "info",
  "message": "Human readable description",
  "service": "order-service"
}
```

### Recommended Fields

```json
{
  "trace_id": "abc123def456",
  "span_id": "789ghi",
  "request_id": "req-001",
  "user_id": "user-123",
  "environment": "production",
  "version": "1.2.3"
}
```

### Context-Specific Fields

```json
{
  "http.method": "POST",
  "http.path": "/api/orders",
  "http.status": 201,
  "duration_ms": 45,
  "db.query": "SELECT...",
  "db.duration_ms": 12
}
```

---

## Implementation

### Node.js (Pino)

```javascript
const pino = require('pino');

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => ({ level: label }),
  },
  timestamp: pino.stdTimeFunctions.isoTime,
  base: {
    service: 'order-service',
    version: process.env.APP_VERSION,
    environment: process.env.NODE_ENV,
  },
});

// Usage
logger.info({ orderId: '123', total: 99.99 }, 'Order created');

// With child logger for request context
const reqLogger = logger.child({
  requestId: req.id,
  userId: req.user?.id,
});
reqLogger.info('Processing request');
```

### Python (structlog)

```python
import structlog

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
)

logger = structlog.get_logger()

# Usage
logger.info("order_created", order_id="123", total=99.99)

# With bound context
log = logger.bind(request_id=request_id, user_id=user_id)
log.info("processing_request")
```

---

## Request Context

### Middleware Pattern

```javascript
// Express middleware
app.use((req, res, next) => {
  const requestId = req.headers['x-request-id'] || uuid();

  req.log = logger.child({
    requestId,
    method: req.method,
    path: req.path,
    userAgent: req.headers['user-agent'],
  });

  req.log.info('Request started');

  res.on('finish', () => {
    req.log.info({
      status: res.statusCode,
      duration: Date.now() - req.startTime,
    }, 'Request completed');
  });

  next();
});
```

### Async Context Propagation

```javascript
const { AsyncLocalStorage } = require('async_hooks');

const logContext = new AsyncLocalStorage();

function withLogContext(context, fn) {
  return logContext.run(context, fn);
}

function getLogger() {
  const context = logContext.getStore() || {};
  return logger.child(context);
}

// Usage
app.use((req, res, next) => {
  withLogContext({ requestId: req.id }, () => next());
});

// Anywhere in the request
getLogger().info('Processing order');
```

---

## Error Logging

### Do

```javascript
logger.error({
  error: {
    message: err.message,
    name: err.name,
    stack: err.stack,
    code: err.code,
  },
  orderId,
  userId,
}, 'Order processing failed');
```

### Don't

```javascript
// Missing context
logger.error(err.message);

// Too much data
logger.error({ request, response, fullError: err });

// Inconsistent format
console.log('Error: ' + err);
```

---

## Sensitive Data

### Never Log

- Passwords / tokens
- Full credit card numbers
- Social security numbers
- API keys

### Redact or Mask

```javascript
function maskPII(obj) {
  const masked = { ...obj };
  if (masked.email) masked.email = masked.email.replace(/(.{2}).*@/, '$1***@');
  if (masked.phone) masked.phone = masked.phone.replace(/\d(?=\d{4})/g, '*');
  return masked;
}

logger.info(maskPII({ email: 'john@example.com', phone: '555-123-4567' }), 'User data');
// { email: 'jo***@example.com', phone: '***-***-4567' }
```

---

## Log Aggregation

### Common Patterns

```
Application → stdout → Container runtime → Log shipper → Aggregator
                                              │
                                    (Fluentd, Vector, Filebeat)
                                              ↓
                                   (Elasticsearch, Loki, CloudWatch)
```

### Indexing Strategy

| Field | Index | Reason |
|-------|-------|--------|
| timestamp | Yes | Time-based queries |
| level | Yes | Filter by severity |
| service | Yes | Multi-service filtering |
| trace_id | Yes | Trace correlation |
| user_id | Yes | User debugging |
| message | Full-text | Search |
| http.status | Yes | Error analysis |

---

## Best Practices

1. **One event per line** - JSON lines format
2. **Consistent field names** - Use conventions
3. **Include trace IDs** - Enable correlation
4. **Log at boundaries** - Request start/end, external calls
5. **Avoid high-cardinality** - Don't log unique IDs as field names
6. **Rate limit** - Prevent log flooding
7. **Review regularly** - Remove stale logs, add missing context
