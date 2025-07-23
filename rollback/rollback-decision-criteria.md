# Rollback Decision Criteria

**System**: ce-simple Migration Rollback Framework  
**Purpose**: Decision matrix and trigger conditions for automated and manual rollback execution

## Decision Framework Overview

This document defines the criteria, thresholds, and procedures for determining when to execute rollback operations during migration processes. The framework provides both automated triggers and manual decision support.

## Severity Classification

### Critical (Immediate Rollback Required)
**Automatic Trigger**: Yes  
**Human Override**: No (safety override only)

**Conditions**:
- System corruption detected (git repository, core files)
- Critical files missing (CLAUDE.md, commands directory)
- Command system completely non-functional (0 commands)
- Git repository integrity compromised
- Rollback system itself compromised
- Data loss events detected
- Security violations detected

**Response Time**: Immediate (< 30 seconds)  
**Rollback Type**: Complete system rollback  
**Approval Required**: None (automatic execution)

### High (Evaluation Required)
**Automatic Trigger**: Conditional  
**Human Override**: Yes

**Conditions**:
- Multiple validation failures (>5 failed tests)
- Significant functionality loss (>50% commands missing)
- Performance degradation >50%
- User workflow severely disrupted
- Documentation system compromised
- Migration batch failure rate >25%
- Rollback validation failures

**Response Time**: Within 5 minutes  
**Rollback Type**: Complete or incremental  
**Approval Required**: System administrator or automated decision engine

### Medium (Monitoring Continue)
**Automatic Trigger**: No  
**Human Override**: Yes

**Conditions**:
- Minor validation failures (2-5 failed tests)
- Non-critical file issues
- Performance degradation 20-50%
- Cosmetic problems affecting user experience
- Documentation inconsistencies
- Single batch failures
- Warning threshold breaches

**Response Time**: Within 30 minutes  
**Rollback Type**: Incremental or selective  
**Approval Required**: Migration supervisor

### Low (Continue Migration)
**Automatic Trigger**: No  
**Human Override**: Yes (manual decision)

**Conditions**:
- Single file formatting issues
- Minor documentation inconsistencies
- Performance degradation <20%
- Non-blocking warnings
- Reference link issues
- Minor git status anomalies

**Response Time**: No immediate action required  
**Rollback Type**: Selective repairs  
**Approval Required**: Optional

## Automated Decision Matrix

### File System Integrity

| Condition | Severity | Action |
|-----------|----------|--------|
| Critical files missing (>2) | Critical | Immediate complete rollback |
| Commands directory missing | Critical | Immediate complete rollback |
| Commands reduced >75% | High | Evaluate for rollback |
| Commands reduced 25-75% | Medium | Monitor and repair |
| Commands reduced <25% | Low | Continue with monitoring |

### Git Repository Health

| Condition | Severity | Action |
|-----------|----------|--------|
| Repository corruption | Critical | Immediate complete rollback |
| Cannot execute git commands | Critical | Immediate complete rollback |
| Massive deletions (>500 files) | High | Evaluate for rollback |
| Significant deletions (100-500 files) | Medium | Monitor progress |
| Normal deletions (<100 files) | Low | Continue migration |

### Validation Test Results

| Failed Tests | Severity | Action |
|--------------|----------|--------|
| >10 failures | Critical | Immediate complete rollback |
| 6-10 failures | High | Evaluate for rollback |
| 3-5 failures | Medium | Monitor and repair |
| 1-2 failures | Low | Continue with fixes |
| 0 failures | - | Continue migration |

### Performance Metrics

| Degradation Level | Severity | Action |
|-------------------|----------|--------|
| >75% slower | Critical | Immediate rollback |
| 50-75% slower | High | Evaluate for rollback |
| 20-50% slower | Medium | Monitor performance |
| <20% slower | Low | Continue migration |

## Decision Engine Algorithm

### Automated Decision Flow

```
1. Collect current system metrics
2. Compare against baseline thresholds
3. Calculate composite risk score
4. Apply decision matrix rules
5. Execute automatic actions if triggered
6. Generate decision report
7. Alert appropriate stakeholders
```

### Risk Score Calculation

**Composite Risk Score = (File_Score × 0.3) + (Git_Score × 0.25) + (Validation_Score × 0.25) + (Performance_Score × 0.2)**

**Scoring Scale**: 0-100 (higher = more risk)

**Thresholds**:
- 0-25: Low risk (continue)
- 26-50: Medium risk (monitor)
- 51-75: High risk (evaluate rollback)
- 76-100: Critical risk (immediate rollback)

### File System Score (0-100)
- Missing critical files: +30 per file
- Commands missing: +25 if >75%, +15 if 25-75%, +5 if <25%
- Documentation missing: +10 if >50%, +5 if <50%
- Permission issues: +2 per affected file

### Git Repository Score (0-100)
- Repository corruption: +100
- Command failures: +50
- Massive deletions: +40
- Significant changes: +20
- Minor anomalies: +10

### Validation Score (0-100)
- Failed critical tests: +15 per failure
- Failed major tests: +10 per failure
- Failed minor tests: +5 per failure
- Warnings: +2 per warning

### Performance Score (0-100)
- >75% degradation: +100
- 50-75% degradation: +60
- 20-50% degradation: +30
- <20% degradation: +10

## Manual Decision Support

### Decision Checklist

**Pre-Rollback Assessment**:
- [ ] Are critical system functions affected?
- [ ] Is data loss possible or detected?
- [ ] Can issues be resolved with targeted repairs?
- [ ] Is rollback technically feasible?
- [ ] Are snapshots available and validated?
- [ ] What is the estimated recovery time?
- [ ] What are the business impact considerations?

**Risk vs. Benefit Analysis**:
- [ ] Cost of continuing vs. rollback
- [ ] Probability of successful repair vs. rollback
- [ ] Time to resolution comparison
- [ ] Impact on ongoing operations
- [ ] Learning and improvement opportunities

### Escalation Matrix

**Level 1**: Automated System
- Authority: Execute critical rollbacks
- Scope: Immediate safety responses
- Reporting: Real-time alerts

**Level 2**: Migration Supervisor
- Authority: High and medium severity decisions
- Scope: Operational rollback decisions
- Reporting: Decision logs and rationale

**Level 3**: System Administrator
- Authority: Policy exceptions and overrides
- Scope: Strategic rollback decisions
- Reporting: Management briefings

**Level 4**: Emergency Response Team
- Authority: Disaster recovery scenarios
- Scope: Business continuity decisions
- Reporting: Incident reports and post-mortems

## Trigger Implementation

### Automated Triggers

**File System Monitors**:
```bash
# Monitor critical files
inotifywait -m -e delete,moved_from CLAUDE.md commands/ &

# Check commands count
CMD_COUNT=$(find commands -name "*.md" | wc -l)
[[ $CMD_COUNT -eq 0 ]] && trigger_critical_rollback
```

**Git Repository Monitors**:
```bash
# Monitor git operations
git status || trigger_critical_rollback

# Monitor deletion patterns
DELETED_COUNT=$(git status --porcelain | grep -c "^ D")
[[ $DELETED_COUNT -gt 500 ]] && trigger_high_rollback
```

**Validation Monitors**:
```bash
# Run validation and check results
validation-suite.sh quick
VALIDATION_EXIT=$?
[[ $VALIDATION_EXIT -eq 2 ]] && trigger_critical_rollback
```

### Manual Trigger Points

**Pre-Migration Checkpoints**:
- After state capture completion
- Before each migration batch
- After critical system modifications

**Runtime Checkpoints**:
- Every 10 migration operations
- After each major component migration
- When warnings accumulate

**Post-Migration Checkpoints**:
- After batch completion
- Before final validation
- Before system handover

## Rollback Execution Decision

### Complete Rollback Criteria
- Critical severity conditions met
- Multiple system components affected
- Repair complexity exceeds rollback complexity
- Time pressure requires fast resolution
- High confidence in rollback success

### Incremental Rollback Criteria
- Single component primarily affected
- Partial functionality preservation desired
- Migration partially successful
- Targeted repair possible
- Learning value in partial preservation

### Selective Rollback Criteria
- Specific functionality affected
- Most system components healthy
- Surgical repair preferred
- Minimal disruption desired
- High repair success probability

## Decision Documentation

### Decision Record Template
```json
{
  "timestamp": "2025-07-23T10:30:00Z",
  "decision_id": "rollback-decision-001",
  "trigger_type": "automated|manual",
  "severity_level": "critical|high|medium|low",
  "risk_score": 85,
  "conditions_detected": [
    "commands directory missing",
    "git repository errors"
  ],
  "decision": "execute_complete_rollback",
  "rollback_type": "complete|incremental|selective",
  "target_snapshot": "pre-migration-20250723",
  "decision_maker": "automated_system|user_name",
  "rationale": "Critical system components missing, automated trigger activated",
  "estimated_recovery_time": "5 minutes",
  "approval_required": false,
  "executed": true,
  "execution_result": "success|failure",
  "post_rollback_validation": "passed|failed"
}
```

### Reporting Requirements

**Real-Time Alerts**:
- Critical rollback executions
- High severity decision points
- System health status changes

**Daily Reports**:
- Rollback decision summary
- Risk score trends
- Migration progress vs. rollback rate

**Weekly Analysis**:
- Decision pattern analysis
- Threshold effectiveness review
- Process improvement recommendations

## Continuous Improvement

### Decision Accuracy Metrics
- False positive rollback rate
- False negative (missed rollback) rate
- Time to correct decision
- Rollback success rate
- Recovery time accuracy

### Threshold Tuning
- Monthly review of trigger thresholds
- Analysis of decision outcomes
- Adjustment based on system evolution
- Integration of lessons learned

### Process Refinement
- Decision criteria effectiveness
- Automation improvement opportunities
- Manual decision support enhancement
- Training and documentation updates

---

**Implementation**: Use `rollback-manager.sh validate` to assess current conditions against these criteria, or `recovery-procedures.sh assess` for comprehensive damage evaluation and automated decision support.