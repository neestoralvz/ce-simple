# Worktree Cleanup - Maintenance & Orphan Management

## Purpose
Automated maintenance system for Git worktree lifecycle with intelligent detection of abandoned sessions, system integrity verification, and proactive cleanup protocols.

## Principles and Guidelines
- **Multi-Layer Orphan Discovery**: Comprehensive detection using worktree inventory, session age analysis, and directory validation
- **Safety-First Assessment**: Eligibility matrix with ≥4 points threshold for auto-cleanup and user prompts for <4 points
- **Graduated Response Protocol**: Auto-cleanup for clear orphans, interactive mode for stale sessions, dry-run preview option
- **System Integrity Verification**: Health check protocol with registry consistency, metadata integrity, and branch cleanup validation

## Execution Process

### Phase 1: Comprehensive System Scanning and Orphan Detection
```javascript
TodoWrite([
  {"content": "Detect all worktrees and analyze their status with comprehensive inventory", "status": "pending", "priority": "high", "id": "wt-cleanup-scan-1"},
  {"content": "Identify abandoned sessions and stale branches using age analysis", "status": "pending", "priority": "high", "id": "wt-cleanup-orphan-1"}
])
```

### Phase 2: Cleanup Eligibility Assessment and Risk Evaluation
```javascript
TodoWrite([
  {"content": "Evaluate cleanup eligibility using safety criteria and scoring matrix", "status": "pending", "priority": "high", "id": "wt-cleanup-assess-1"},
  {"content": "Classify cleanup candidates: auto-cleanup (≥4 points) vs interactive prompt (<4 points)", "status": "pending", "priority": "high", "id": "wt-cleanup-classify-1"}
])
```

### Phase 3: Interactive Assessment and User Decision Framework
```javascript
TodoWrite([
  {"content": "Present maintenance report with detected worktrees and cleanup candidates", "status": "pending", "priority": "high", "id": "wt-cleanup-report-1"},
  {"content": "Execute user-selected cleanup actions with verification protocols", "status": "pending", "priority": "high", "id": "wt-cleanup-execute-1"}
])
```

### Phase 4: System Integrity Verification and Health Validation
```javascript
TodoWrite([
  {"content": "Verify worktree registry consistency and session metadata integrity", "status": "pending", "priority": "medium", "id": "wt-cleanup-verify-1"},
  {"content": "Generate cleanup summary with disk savings and system status", "status": "pending", "priority": "medium", "id": "wt-cleanup-summary-1"}
])
```

## Cleanup Eligibility Matrix

### Auto-Cleanup Criteria (≥4 Points Threshold)
**Directory missing**: +5 points → Auto-cleanup (safe removal)
**>24h inactive + no changes**: +4 points → Auto-cleanup (abandoned)
**Session marked abandoned**: +4 points → Auto-cleanup (explicitly abandoned)

### Interactive Prompt Criteria (<4 Points)
**No session metadata**: +3 points → Interactive prompt (uncertain state)
**>7 days old**: +3 points → Interactive prompt (potentially stale)

## Maintenance Framework Architecture

### Detection Protocol Components
**Worktree Inventory**: Comprehensive listing with status analysis and age calculation
**Session Age Analysis**: 24-hour threshold for inactivity with change detection
**Directory Validation**: Missing directory detection for orphan identification

### Interactive Assessment Interface
**Maintenance Report**: Detected worktrees with status indicators (active, stale, orphaned)
**Cleanup Options**: AUTO-CLEANUP, INTERACTIVE, DRY-RUN, CANCEL with clear descriptions
**Per-Candidate Review**: Age display, change count, and action options (merge, abandon, skip)

### Automated Maintenance Schedule
**Daily**: Auto-cleanup orphaned worktrees (>24h + missing directory)
**Weekly**: Interactive review of stale sessions (>7 days)
**Monthly**: Complete system integrity verification
**On-Demand**: User-triggered comprehensive cleanup

## Safety Protocols Framework

### Data Protection Measures
**Backup Creation**: Archive session metadata before deletion with recovery capability
**Confirmation Prompts**: Multi-step verification for destructive actions
**Rollback Capability**: Maintain cleanup logs for potential recovery operations
**Dry-Run Mode**: Preview all actions before execution with impact assessment

### System Health Verification
**Registry Consistency**: Worktree list vs session directory count validation
**Metadata Integrity**: JSON validation for all session metadata files
**Branch Cleanup**: Session branch count verification and cleanup confirmation

### Emergency Recovery Protocol
**Force Cleanup Mode**: Nuclear option for emergency situations (use with extreme caution)
**Complete System Reset**: Remove all session worktrees and branches when required
**Recovery Documentation**: Maintain logs for post-cleanup analysis and recovery

---

**Single Responsibility**: Maintenance system ensuring Git worktree lifecycle health through intelligent orphan detection, safety-first cleanup protocols, and comprehensive system integrity verification.