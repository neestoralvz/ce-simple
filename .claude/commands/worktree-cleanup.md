# Worktree Cleanup - Maintenance & Orphan Management

## 🎯 Purpose
Automated maintenance system for Git work tree lifecycle with intelligent detection of abandoned sessions and system integrity verification.

## 🚀 Usage
Execute: `/worktree-cleanup [optional: --force|--dry-run|--interactive]`

## 🔧 Implementation

### Maintenance Assessment Framework
**MANDATORY**: Comprehensive system health evaluation

```javascript
TodoWrite([
  {"content": "📊 SCAN: Detect all work trees and analyze their status", "status": "pending", "priority": "high", "id": "wt-cleanup-scan-1"},
  {"content": "🔍 ORPHAN: Identify abandoned sessions and stale branches", "status": "pending", "priority": "high", "id": "wt-cleanup-orphan-1"},
  {"content": "⚖️ ASSESS: Evaluate cleanup eligibility using safety criteria", "status": "pending", "priority": "high", "id": "wt-cleanup-assess-1"},
  {"content": "🧹 EXECUTE: Perform cleanup actions with verification", "status": "pending", "priority": "high", "id": "wt-cleanup-execute-1"},
  {"content": "📋 REPORT: Generate cleanup summary and recommendations", "status": "pending", "priority": "medium", "id": "wt-cleanup-report-1"}
])
```

### Detection Protocol
**Multi-Layer Orphan Discovery**:

```bash
# 1. Work Tree Inventory
WORKTREES="$(git worktree list --porcelain)"
ACTIVE_SESSIONS="$(ls .claude/sessions/ 2>/dev/null | grep -c session- || echo 0)"

# 2. Session Age Analysis  
CURRENT_TIME="$(date +%s)"
OLD_THRESHOLD="$((CURRENT_TIME - 86400))" # 24 hours

# 3. Directory Validation
for WORKTREE_PATH in $(echo "$WORKTREES" | grep worktree | cut -d' ' -f2); do
  if [[ ! -d "$WORKTREE_PATH" ]]; then
    echo "ORPHAN: Missing directory $WORKTREE_PATH"
  fi
done
```

### Cleanup Eligibility Matrix
**Safety-First Assessment**:

| Condition | Weight | Action |
|-----------|---------|---------|
| Directory missing | +5 | Auto-cleanup |
| >24h inactive + no changes | +4 | Auto-cleanup |
| Session marked abandoned | +4 | Auto-cleanup |
| No session metadata | +3 | Interactive prompt |
| >7 days old | +3 | Interactive prompt |
| **Threshold: ≥4 points** | | **AUTO-CLEANUP** |
| **Threshold: <4 points** | | **PROMPT USER** |

### Interactive Assessment Mode
**User Decision Framework**:
```
🧹 WORKTREE MAINTENANCE REPORT

📊 DETECTED WORK TREES:
  ✅ session-20250722-143045-lifecycle (active, 1h ago)
  ⚠️  session-20250721-091234-features (stale, 25h ago, 0 changes)
  🔴 session-20250720-154321-experiment (orphan, directory missing)

🎯 CLEANUP CANDIDATES:

[1] 🗑️  AUTO-CLEANUP (2 orphaned work trees)
[2] 🔍 INTERACTIVE (review each stale work tree)  
[3] 📊 DRY-RUN (show what would be cleaned)
[4] ❌ CANCEL (keep all work trees)

Selection [1-4]:
```

### Cleanup Execution Framework
**Graduated Response Protocol**:

#### Auto-Cleanup Actions
```bash
# 1. Remove orphaned work trees
for ORPHAN in "${ORPHAN_WORKTREES[@]}"; do
  git worktree remove "${ORPHAN}" --force 2>/dev/null || true
  git branch -D "$(basename "${ORPHAN}")" 2>/dev/null || true
done

# 2. Archive stale sessions
for STALE_SESSION in "${STALE_SESSIONS[@]}"; do
  if [[ -f "${STALE_SESSION}/.session-info" ]]; then
    mv "${STALE_SESSION}/.session-info" ".claude/sessions/archived-$(basename "${STALE_SESSION}").json"
  fi
done
```

#### Interactive Cleanup Mode
```bash
for CANDIDATE in "${CLEANUP_CANDIDATES[@]}"; do
  echo "🔍 REVIEWING: ${CANDIDATE}"
  echo "📊 AGE: $(stat -f %Sm -t %Y-%m-%d\ %H:%M "${CANDIDATE}")"
  echo "📁 CHANGES: $(cd "${CANDIDATE}" && git status --porcelain | wc -l) files modified"
  
  read -p "Action [m=merge, a=abandon, s=skip]: " ACTION
  case "$ACTION" in
    m) merge_worktree "${CANDIDATE}" ;;
    a) abandon_worktree "${CANDIDATE}" ;;
    s) echo "Skipped ${CANDIDATE}" ;;
  esac
done
```

### System Integrity Verification
**Health Check Protocol**:

```bash
# 1. Verify work tree registry consistency
git worktree list --porcelain | grep -c worktree
ls -1d ../ce-session-* 2>/dev/null | wc -l

# 2. Check session metadata integrity  
find .claude/sessions/ -name "session-*.json" -exec jq -e . {} \; >/dev/null

# 3. Validate branch cleanup
git branch | grep -c "session-" || echo "0"
```

### Automated Maintenance Schedule
**Proactive Cleanup Integration**:
- **Daily**: Auto-cleanup orphaned work trees (>24h + missing directory)
- **Weekly**: Interactive review of stale sessions (>7 days)
- **Monthly**: Complete system integrity verification
- **On-Demand**: User-triggered comprehensive cleanup

### Emergency Recovery Protocol
**Force Cleanup Mode**:
```bash
# Nuclear option: Clean ALL session work trees
# WARNING: Use only in emergency situations
git worktree list | grep session- | awk '{print $3}' | xargs -I {} git worktree remove {} --force
git branch | grep session- | xargs -I {} git branch -D {}
rm -rf ../ce-session-*
```

## ⚡ Execution Layer

### Mandatory Tool Executions
**CRITICAL**: Real cleanup implementation

```javascript
// 1. WORK TREE DISCOVERY (real execution)
Bash("git worktree list --porcelain") // List all work trees
Bash("ls -la ../ce-session-* 2>/dev/null || echo 'No session directories'") // Find session dirs

// 2. ORPHAN DETECTION (real execution)
Bash("find ../ce-session-* -maxdepth 1 -name '.session-info' -exec cat {} \\;") // Check metadata
Bash("git branch | grep session-") // List session branches

// 3. CLEANUP EXECUTION (real execution)  
Bash("git worktree remove [orphan-path] --force") // Remove orphaned work trees
Bash("git branch -D [orphan-branch]") // Delete orphaned branches

// 4. VERIFICATION (real execution)
Bash("git worktree list") // Verify cleanup results
```

### Safety Protocols
**Data Protection**:
- **Backup Creation**: Archive session metadata before deletion
- **Confirmation Prompts**: Multi-step verification for destructive actions
- **Rollback Capability**: Maintain cleanup logs for recovery
- **Dry-Run Mode**: Preview all actions before execution

### Output Format
```
🧹 WORKTREE CLEANUP COMPLETED

📊 SUMMARY:
  🗑️  Removed: 2 orphaned work trees
  📁 Archived: 1 stale session metadata  
  🌿 Active: 1 work tree (session-20250722-143045-lifecycle)
  ✅ Status: System integrity verified

⏱️  Duration: 15 seconds
💾 Disk saved: 245 MB
```

## 🔗 Integration Points

### Automatic Triggers
**Maintenance Automation**:
- **System Startup**: Quick orphan scan on first command
- **Weekly Schedule**: Comprehensive cleanup assessment
- **Error Recovery**: Auto-trigger on work tree corruption detection
- **User Request**: Manual maintenance mode

### Integration with Lifecycle
**Maintenance Workflow**:
```
System Health Check → Orphan Detection → Cleanup Assessment → User Decision → Cleanup Execution → Verification
```

### Performance Optimization
**Efficiency Measures**:
- **Incremental Scanning**: Only check changed work trees
- **Parallel Processing**: Concurrent analysis of multiple work trees
- **Cache Results**: Store cleanup state for faster subsequent runs
- **Background Mode**: Non-blocking maintenance operations

---

**CRITICAL**: This command maintains system health and prevents work tree accumulation while preserving data integrity.

**EXECUTION COMMITMENT**: All maintenance protocols implemented with real tool executions. Zero orphan tolerance maintained.