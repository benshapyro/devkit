# Common Scenarios

Standard runbook patterns for frequent incidents.

## Database Scenarios

### Database Connection Pool Exhausted

**Symptoms:**
- "Connection pool exhausted" in logs
- Slow/failing API requests
- Database connections at limit

**Quick Diagnosis:**
```bash
# Check active connections
psql -c "SELECT count(*) FROM pg_stat_activity WHERE state = 'active';"

# Find long-running queries
psql -c "SELECT pid, now() - query_start AS duration, query
         FROM pg_stat_activity
         WHERE state = 'active' AND now() - query_start > interval '1 minute'
         ORDER BY duration DESC LIMIT 10;"

# Check connection sources
psql -c "SELECT client_addr, count(*)
         FROM pg_stat_activity
         GROUP BY client_addr ORDER BY count DESC;"
```

**Remediation:**
1. Kill long-running queries if safe
   ```bash
   psql -c "SELECT pg_terminate_backend(PID);"
   ```
2. Restart application pods (releases connections)
   ```bash
   kubectl rollout restart deployment/app
   ```
3. Temporarily increase pool size if DB can handle it

**Root Cause Investigation:**
- Missing query timeouts
- Connection leak in code
- N+1 query pattern
- Missing indexes

---

### Database Replication Lag

**Symptoms:**
- Read replicas returning stale data
- Replication lag alerts
- Inconsistent read-after-write

**Quick Diagnosis:**
```bash
# PostgreSQL
psql -c "SELECT client_addr, state, sent_lsn, replay_lsn,
         pg_wal_lsn_diff(sent_lsn, replay_lsn) AS lag_bytes
         FROM pg_stat_replication;"

# MySQL
mysql -e "SHOW SLAVE STATUS\G" | grep -E "Seconds_Behind|Slave_IO|Slave_SQL"
```

**Remediation:**
1. Check if replica is overwhelmed (CPU, I/O)
2. Check network between primary and replica
3. If severe lag, redirect traffic to primary temporarily

---

## API Scenarios

### High Latency / Slow Requests

**Symptoms:**
- p99 latency spikes
- Timeout errors increasing
- User reports of slowness

**Quick Diagnosis:**
```bash
# Check recent slow endpoints
cat /var/log/app/access.log | awk '$NF > 1.0 {print $7}' | sort | uniq -c | sort -rn | head

# Check external dependency latency
curl -w "DNS: %{time_namelookup}s | Connect: %{time_connect}s | Total: %{time_total}s\n" \
     -o /dev/null -s https://api.external.com/health

# Check database query times
psql -c "SELECT query, mean_time, calls
         FROM pg_stat_statements
         ORDER BY mean_time DESC LIMIT 10;"
```

**Remediation:**
1. Scale horizontally if CPU-bound
   ```bash
   kubectl scale deployment/api --replicas=10
   ```
2. Add caching if DB-bound
3. Enable circuit breaker if external dependency slow

---

### 5xx Error Spike

**Symptoms:**
- Error rate increasing
- 500/502/503/504 responses
- Error budget burning

**Quick Diagnosis:**
```bash
# Check error distribution
grep -E " 5[0-9]{2} " /var/log/nginx/access.log | \
  awk '{print $9}' | sort | uniq -c | sort -rn

# Check application logs
kubectl logs -l app=api --tail=500 | grep -i error | tail -20

# Check recent deployments
kubectl rollout history deployment/api | tail -5
```

**Remediation:**
```
500 → Application error → Check logs, rollback if recent deploy
502 → Backend down → Check upstream pods
503 → Overloaded → Scale or rate limit
504 → Timeout → Check slow dependencies
```

---

## Infrastructure Scenarios

### Pod CrashLoopBackOff

**Symptoms:**
- Pod status: CrashLoopBackOff
- Service unavailable
- Restart count increasing

**Quick Diagnosis:**
```bash
# Get pod status
kubectl get pods -l app=service-name

# Check pod events
kubectl describe pod POD_NAME | grep -A 20 Events

# Get previous container logs
kubectl logs POD_NAME --previous
```

**Remediation:**
1. Check logs for startup error
2. Check resource limits (OOMKilled)
3. Check config/secrets mounted correctly
4. Rollback if recent deployment
   ```bash
   kubectl rollout undo deployment/service-name
   ```

---

### Memory Pressure / OOMKilled

**Symptoms:**
- Pods restarting with OOMKilled
- Node memory pressure
- Evicted pods

**Quick Diagnosis:**
```bash
# Check pod memory usage
kubectl top pods -l app=service-name

# Check if OOMKilled
kubectl describe pod POD_NAME | grep -i oom

# Check node memory
kubectl top nodes
kubectl describe node NODE_NAME | grep -A5 "Allocated resources"
```

**Remediation:**
1. Increase memory limits (if available)
   ```yaml
   resources:
     limits:
       memory: "2Gi"
   ```
2. Fix memory leak if present
3. Add horizontal scaling instead of larger pods

---

### Disk Space Full

**Symptoms:**
- "No space left on device" errors
- Write failures
- Application crashes

**Quick Diagnosis:**
```bash
# Check disk usage
df -h

# Find large files
du -sh /* 2>/dev/null | sort -hr | head -20

# Find large log files
find /var/log -type f -size +100M -exec ls -lh {} \;
```

**Remediation:**
1. Clean old logs
   ```bash
   find /var/log -name "*.log" -mtime +7 -delete
   ```
2. Clean docker images
   ```bash
   docker system prune -a
   ```
3. Expand volume if persistent issue

---

## Network Scenarios

### DNS Resolution Failure

**Symptoms:**
- "Could not resolve host" errors
- Intermittent connection failures
- All external calls failing

**Quick Diagnosis:**
```bash
# Check DNS resolution
nslookup api.external.com
dig api.external.com

# Check DNS pods (Kubernetes)
kubectl get pods -n kube-system -l k8s-app=kube-dns

# Check /etc/resolv.conf
cat /etc/resolv.conf
```

**Remediation:**
1. Restart CoreDNS pods
   ```bash
   kubectl rollout restart deployment/coredns -n kube-system
   ```
2. Check upstream DNS servers
3. Use IP temporarily if critical

---

### SSL Certificate Expiry

**Symptoms:**
- HTTPS connections failing
- SSL handshake errors
- Browser showing "Not Secure"

**Quick Diagnosis:**
```bash
# Check certificate expiry
echo | openssl s_client -connect domain.com:443 2>/dev/null | \
  openssl x509 -noout -dates

# Days until expiry
echo | openssl s_client -connect domain.com:443 2>/dev/null | \
  openssl x509 -noout -enddate | cut -d= -f2 | \
  xargs -I{} date -d {} +%s | xargs -I{} expr {} - $(date +%s) | \
  xargs -I{} expr {} / 86400
```

**Remediation:**
1. Renew certificate
2. Update certificate in load balancer/ingress
3. Restart services if needed

---

## Quick Reference

| Scenario | First Command | Likely Fix |
|----------|---------------|------------|
| DB connections | `pg_stat_activity` | Restart app, kill queries |
| High latency | Check external deps | Scale or cache |
| 5xx errors | Check app logs | Rollback |
| CrashLoop | `kubectl logs --previous` | Fix config or rollback |
| OOMKilled | `kubectl top pods` | Increase limits |
| Disk full | `df -h` | Clean logs |
| DNS failure | `nslookup` | Restart CoreDNS |
| SSL expiry | `openssl s_client` | Renew cert |
