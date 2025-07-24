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

---

**Single Responsibility**: Maintenance system ensuring Git worktree lifecycle health through intelligent orphan detection, safety-first cleanup protocols, and comprehensive system integrity verification.