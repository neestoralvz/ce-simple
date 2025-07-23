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

## Enhanced Auto-Decision Matrix

### Auto-SQUASH Criteria (≥3 Points Threshold)
**Zero conflicts + successful workflow**: +4 points → Auto-SQUASH
**Documentation optimization**: +3 points → Auto-SQUASH  
**≤5 files modified + zero conflicts**: +2 points → Auto-SQUASH
**Config/CLAUDE.md + docs updates**: +2 points → Auto-SQUASH
**Session >2 hours BUT successful**: +1 point → Auto-SQUASH

### Manual Review Requirements
**Conflicts Detected**: Manual resolution required with user intervention
**User Requests Abandonment**: Confirmation needed with abandon workflow
**Force-Prompt Flag Used**: User wants to see all options with decision interface

## Session Completion Framework

### Success Notification (Auto-SQUASH)
```
✅ WORKTREE SESSION COMPLETED
📊 SESSION: session-[timestamp]-[topic]
🎯 ACTION: Auto-SQUASH executed (score: X/3 threshold)
📈 CHANGES: N files changed, +additions/-deletions lines
🔀 RESULT: Successfully merged to master branch
🧹 CLEANUP: Worktree removed, session branch deleted
```

### User Decision Interface (When Manual Review Required)
Present clear options with session metrics, change summary, and conflict status
Options: MERGE, SQUASH (recommended), ABANDON, REVIEW with detailed analysis

### Execution Strategies
**Merge Strategy**: Switch to parent branch, execute merge type, cleanup branch
**Abandon Strategy**: Switch to parent, force delete branch, log abandonment
**Cleanup Protocol**: Remove worktree, archive session metadata, clear current session

## Integration Architecture

### Post-Closure Actions
**Success Notification**: Display comprehensive completion summary with metrics
**Learning Capture**: Trigger `/capture-learnings` when valuable patterns identified
**System Update**: Update cross-reference matrices and session tracking
**Git Commit**: Generate standardized commit message for session tracking

### Automatic Triggers
**Workflow End**: Auto-trigger after main command completion with assessment
**Idle Detection**: Prompt closure after 2+ hours inactivity with notification
**Error States**: Emergency closure on critical failures with recovery options

---

**Single Responsibility**: Session completion engine ensuring clean worktree lifecycle completion with intelligent auto-decision making, comprehensive cleanup, and seamless integration with command ecosystem.