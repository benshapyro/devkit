# Production Migration Checklist

Pre-deployment verification for database migrations.

## Pre-Migration (Day Before)

### Planning
- [ ] Migration script reviewed by team
- [ ] Rollback script tested on staging
- [ ] Estimated duration calculated
- [ ] Maintenance window scheduled (if needed)
- [ ] Team notified of migration

### Staging Verification
- [ ] Migration tested on staging with prod-like data
- [ ] Performance impact measured
- [ ] Application tested against new schema
- [ ] Rollback procedure verified

### Backup
- [ ] Full database backup taken
- [ ] Backup verified (test restore)
- [ ] Point-in-time recovery enabled
- [ ] Backup retention confirmed

---

## Pre-Migration (1 Hour Before)

### Communication
- [ ] Status page updated (if public)
- [ ] Team in migration channel
- [ ] On-call engineer notified
- [ ] Stakeholders informed

### Monitoring
- [ ] Database dashboards open
- [ ] Query performance baseline captured
- [ ] Error rate baseline captured
- [ ] Connection pool status verified

### Final Checks
- [ ] No other deployments in progress
- [ ] Traffic at acceptable level
- [ ] Recent backup confirmed
- [ ] Rollback script ready

---

## Migration Execution

### Start
```bash
# Log start time
echo "Migration started at $(date)" >> migration.log

# Run migration with timeout
timeout 30m npm run migrate:production 2>&1 | tee -a migration.log
```

### Monitor During Migration
- [ ] Lock wait time < threshold
- [ ] Replication lag < threshold
- [ ] Connection count stable
- [ ] Error rate stable
- [ ] Response time stable

### Lock Monitoring Query
```sql
SELECT
  blocked.pid AS blocked_pid,
  blocked.query AS blocked_query,
  blocking.pid AS blocking_pid,
  blocking.query AS blocking_query,
  now() - blocked.query_start AS blocked_duration
FROM pg_stat_activity blocked
JOIN pg_locks blocked_locks ON blocked.pid = blocked_locks.pid
JOIN pg_locks blocking_locks ON blocked_locks.transactionid = blocking_locks.transactionid
JOIN pg_stat_activity blocking ON blocking_locks.pid = blocking.pid
WHERE NOT blocked_locks.granted;
```

---

## Post-Migration Verification

### Immediate (First 5 Minutes)
- [ ] Migration completed without errors
- [ ] Application health checks passing
- [ ] No increase in error rate
- [ ] Response times normal
- [ ] Database connections stable

### Validation Queries
```sql
-- Verify schema changes
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'affected_table';

-- Verify indexes
SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'affected_table';

-- Verify constraints
SELECT conname, contype
FROM pg_constraint
WHERE conrelid = 'affected_table'::regclass;
```

### Short-Term (First Hour)
- [ ] Key business queries performing well
- [ ] No unexpected slow queries
- [ ] No data integrity issues
- [ ] Cron jobs running successfully
- [ ] Reports generating correctly

---

## Rollback Triggers

### Immediate Rollback If:
- Migration fails with error
- Application cannot start
- Data corruption detected
- Critical functionality broken

### Consider Rollback If:
- Response times degraded >50%
- Error rate increased >10%
- Replication lag >10 minutes
- Customer reports issues

### Rollback Procedure
```bash
# 1. Stop application traffic (if needed)
kubectl scale deployment app --replicas=0

# 2. Run rollback
npm run migrate:rollback

# 3. Verify rollback
psql -c "\d affected_table"

# 4. Restore traffic
kubectl scale deployment app --replicas=3
```

---

## Post-Migration Cleanup

### Immediate
- [ ] Migration log saved
- [ ] Status page updated
- [ ] Team notified of completion

### Within 24 Hours
- [ ] Backup retention policy applied
- [ ] Temporary tables/columns scheduled for removal
- [ ] Documentation updated
- [ ] Monitoring thresholds adjusted if needed

### Within 1 Week
- [ ] Deprecated code paths removed
- [ ] Old columns/tables dropped (if expand-contract)
- [ ] Performance report generated
- [ ] Lessons learned documented

---

## Emergency Contacts

| Role | Contact | When to Call |
|------|---------|--------------|
| DBA On-Call | @dba-oncall | Lock issues, performance |
| App On-Call | @app-oncall | Application errors |
| Manager | @manager | Major incident |
| Vendor Support | support@db.com | Database-level issues |

---

## Quick Reference Commands

```bash
# Check migration status
npm run migrate:status

# Run migration
npm run migrate:production

# Rollback last migration
npm run migrate:rollback

# Force rollback all
npm run migrate:rollback --all

# Check database size
psql -c "SELECT pg_size_pretty(pg_database_size('mydb'));"

# Check active queries
psql -c "SELECT pid, now() - query_start AS duration, query
         FROM pg_stat_activity WHERE state = 'active';"

# Kill long-running query
psql -c "SELECT pg_terminate_backend(<pid>);"
```

---

## Success Criteria

| Metric | Target | Actual |
|--------|--------|--------|
| Migration duration | < 30 min | |
| Error rate change | < 1% | |
| Response time change | < 10% | |
| Rollback required | No | |
| Data integrity | 100% | |
