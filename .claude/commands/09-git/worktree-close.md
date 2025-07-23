# Worktree Close - Session Completion

## Purpose
Intelligent session closure with automated merge/abandon decision framework for Git worktree lifecycle completion using enhanced auto-decision criteria.

## Principles and Guidelines
- **Automated Assessment**: Multi-dimensional analysis with session metadata and change evaluation for completion readiness
- **Enhanced Auto-Decision Matrix**: ≥3 points threshold for auto-SQUASH with zero conflicts + successful workflow scoring
- **Smart Automation Logic**: Auto-SQUASH for documentation optimization, small changes, and successful workflows
- **Manual Review Triggers**: Only required for conflicts, abandonment requests, or force-prompt usage

## Execution Process

### Phase 1: Session Assessment and Metadata Analysis
```javascript
TodoWrite([
  {"content": "Analyze session metadata and changes for completion readiness", "status": "pending", "priority": "high", "id": "wt-close-assess-1"},
  {"content": "Load session information and calculate complexity metrics", "status": "pending", "priority": "high", "id": "wt-close-load-1"}
])
```

### Phase 2: Conflict Detection and Decision Framework
```javascript
TodoWrite([
  {"content": "Check for merge conflicts with parent branch", "status": "pending", "priority": "high", "id": "wt-close-conflicts-1"},
  {"content": "Apply auto-merge criteria using enhanced decision matrix (≥3 points)", "status": "pending", "priority": "high", "id": "wt-close-decision-1"}
])
```

### Phase 3: Merge Execution and Action Implementation
```javascript
TodoWrite([
  {"content": "Execute auto-SQUASH or prompt user based on decision matrix", "status": "pending", "priority": "high", "id": "wt-close-execute-1"},
  {"content": "Perform merge/abandon action with comprehensive verification", "status": "pending", "priority": "high", "id": "wt-close-action-1"}
])
```

### Phase 4: Session Cleanup and Environment Reset
```javascript
TodoWrite([
  {"content": "Remove worktree and update session tracking", "status": "pending", "priority": "high", "id": "wt-close-cleanup-1"},
  {"content": "Generate completion summary and trigger learning capture if valuable", "status": "pending", "priority": "medium", "id": "wt-close-summary-1"}
])
```


---

**Single Responsibility**: Session completion engine ensuring clean worktree lifecycle completion with intelligent auto-decision making, comprehensive cleanup, and seamless integration with command ecosystem.