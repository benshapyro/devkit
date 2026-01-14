# Collector Deployment

OpenTelemetry Collector deployment patterns and configuration.

## Deployment Modes

### Agent Mode

Collector runs on each host/pod.

```
┌─────────────────┐
│   Application   │
│  └── SDK ───────┼──→ [Collector Agent] ──→ Backend
│                 │      (sidecar/daemon)
└─────────────────┘
```

**Pros:**
- Low latency export
- Local processing (filtering, sampling)
- Reduced network traffic

**Cons:**
- More resources per node
- More instances to manage

### Gateway Mode

Centralized collector cluster.

```
┌─────────────────┐
│   Application   │
│  └── SDK ───────┼──→ [Collector Gateway] ──→ Backend
│                 │         (cluster)
└─────────────────┘
```

**Pros:**
- Centralized configuration
- Tail sampling possible
- Fewer instances to manage

**Cons:**
- Network dependency
- Potential bottleneck

### Hybrid Mode (Recommended)

Agents for collection, gateway for processing.

```
┌─────────────────┐
│   Application   │
│  └── SDK ───────┼──→ [Agent] ──→ [Gateway] ──→ Backend
│                 │   (filter)    (process)
└─────────────────┘
```

---

## Kubernetes Deployment

### DaemonSet (Agent)

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: otel-collector-agent
spec:
  selector:
    matchLabels:
      app: otel-collector-agent
  template:
    metadata:
      labels:
        app: otel-collector-agent
    spec:
      containers:
        - name: collector
          image: otel/opentelemetry-collector-contrib:0.91.0
          args: ["--config=/etc/otel/config.yaml"]
          ports:
            - containerPort: 4317  # OTLP gRPC
            - containerPort: 4318  # OTLP HTTP
          resources:
            limits:
              cpu: 200m
              memory: 256Mi
          volumeMounts:
            - name: config
              mountPath: /etc/otel
      volumes:
        - name: config
          configMap:
            name: otel-agent-config
```

### Deployment (Gateway)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector-gateway
spec:
  replicas: 3
  selector:
    matchLabels:
      app: otel-collector-gateway
  template:
    metadata:
      labels:
        app: otel-collector-gateway
    spec:
      containers:
        - name: collector
          image: otel/opentelemetry-collector-contrib:0.91.0
          args: ["--config=/etc/otel/config.yaml"]
          ports:
            - containerPort: 4317
            - containerPort: 4318
          resources:
            limits:
              cpu: 1
              memory: 2Gi
          volumeMounts:
            - name: config
              mountPath: /etc/otel
      volumes:
        - name: config
          configMap:
            name: otel-gateway-config
---
apiVersion: v1
kind: Service
metadata:
  name: otel-collector-gateway
spec:
  selector:
    app: otel-collector-gateway
  ports:
    - name: otlp-grpc
      port: 4317
    - name: otlp-http
      port: 4318
```

---

## Collector Configuration

### Agent Config

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 1s
    send_batch_size: 1024
  memory_limiter:
    check_interval: 1s
    limit_mib: 200
  resource:
    attributes:
      - key: k8s.node.name
        value: ${env:K8S_NODE_NAME}
        action: upsert

exporters:
  otlp:
    endpoint: otel-collector-gateway:4317
    tls:
      insecure: true

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, batch, resource]
      exporters: [otlp]
    metrics:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [otlp]
```

### Gateway Config

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 5s
    send_batch_size: 8192
  memory_limiter:
    check_interval: 1s
    limit_mib: 1500
  tail_sampling:
    decision_wait: 10s
    policies:
      - name: errors
        type: status_code
        status_code:
          status_codes: [ERROR]
      - name: slow
        type: latency
        latency:
          threshold_ms: 500
      - name: sample
        type: probabilistic
        probabilistic:
          sampling_percentage: 10

exporters:
  otlp/jaeger:
    endpoint: jaeger:4317
  prometheus:
    endpoint: 0.0.0.0:9090
  loki:
    endpoint: http://loki:3100/loki/api/v1/push

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, tail_sampling, batch]
      exporters: [otlp/jaeger]
    metrics:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [prometheus]
    logs:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [loki]
```

---

## Scaling Patterns

### Horizontal Scaling

```yaml
# Gateway HPA
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: otel-collector-gateway
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: otel-collector-gateway
  minReplicas: 3
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Load Balancing

```yaml
# Trace-aware load balancing
exporters:
  loadbalancing:
    protocol:
      otlp:
        endpoint: gateway:4317
    resolver:
      dns:
        hostname: otel-collector-gateway-headless
        port: 4317
```

---

## Resource Sizing

### Agent Resources

| Traffic | CPU | Memory |
|---------|-----|--------|
| Low (< 100 span/s) | 50m | 64Mi |
| Medium (100-1000 span/s) | 100m | 128Mi |
| High (> 1000 span/s) | 200m | 256Mi |

### Gateway Resources

| Traffic | Replicas | CPU | Memory |
|---------|----------|-----|--------|
| Low | 2 | 500m | 512Mi |
| Medium | 3 | 1 | 1Gi |
| High | 5+ | 2 | 2Gi |

---

## Health Monitoring

### Collector Metrics

```yaml
# Enable telemetry
service:
  telemetry:
    metrics:
      address: 0.0.0.0:8888
    logs:
      level: info
```

### Key Metrics

| Metric | Description |
|--------|-------------|
| `otelcol_receiver_accepted_spans` | Spans received |
| `otelcol_exporter_sent_spans` | Spans exported |
| `otelcol_processor_dropped_spans` | Spans dropped |
| `otelcol_exporter_queue_size` | Export queue depth |

### Health Check

```yaml
livenessProbe:
  httpGet:
    path: /
    port: 13133
readinessProbe:
  httpGet:
    path: /
    port: 13133
```

---

## Common Issues

### Memory Pressure

```yaml
processors:
  memory_limiter:
    check_interval: 1s
    limit_mib: 400       # Hard limit
    spike_limit_mib: 100 # Spike allowance
```

### Queue Backpressure

```yaml
exporters:
  otlp:
    sending_queue:
      enabled: true
      num_consumers: 10
      queue_size: 5000
    retry_on_failure:
      enabled: true
      initial_interval: 5s
      max_interval: 30s
```

---

## Best Practices

1. **Start with hybrid** - Agents + Gateway
2. **Use memory limiter** - Prevent OOM
3. **Enable batching** - Reduce network overhead
4. **Monitor collectors** - They're infrastructure too
5. **Size conservatively** - Scale up as needed
6. **Use contrib image** - More receivers/exporters
