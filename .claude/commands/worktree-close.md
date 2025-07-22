# Worktree Close - Session Completion

## 🎯 Purpose
Intelligent session closure with automated merge/abandon decision framework for Git work tree lifecycle completion.

## 🚀 Usage
Execute: `/worktree-close [optional: abandon|force-prompt]`

**Default Behavior**: Intelligent auto-SQUASH for successful workflows
**Override Options**: `abandon` to discard, `force-prompt` to see all options

## 🔧 Implementation

### Decision Framework Protocol
**MANDATORY**: Automated assessment with user override capabilities

```javascript
TodoWrite([
  {"content": "📊 ASSESS: Analyze session metadata and changes for completion readiness", "status": "pending", "priority": "high", "id": "wt-close-assess-1"},
  {"content": "🔍 CONFLICTS: Check for merge conflicts with parent branch", "status": "pending", "priority": "high", "id": "wt-close-conflicts-1"},
  {"content": "⚖️ DECISION: Apply auto-merge criteria or prompt user decision", "status": "pending", "priority": "high", "id": "wt-close-decision-1"},
  {"content": "🔄 EXECUTE: Perform merge/abandon action with verification", "status": "pending", "priority": "high", "id": "wt-close-execute-1"},
  {"content": "🧹 CLEANUP: Remove work tree and update session tracking", "status": "pending", "priority": "high", "id": "wt-close-cleanup-1"}
])
```

### Session Assessment Framework
**Multi-Dimensional Analysis**:

```bash
# 1. Load session metadata
SESSION_INFO="$(cat .session-info 2>/dev/null || echo '{}')"
SESSION_ID="$(echo "$SESSION_INFO" | jq -r '.session_id // "unknown"')"
COMPLEXITY_SCORE="$(echo "$SESSION_INFO" | jq -r '.complexity_score // 0')"

# 2. Analyze changes
MODIFIED_FILES="$(git diff --name-only HEAD~1..HEAD | wc -l)"
ADDED_FILES="$(git diff --name-only --diff-filter=A HEAD~1..HEAD | wc -l)"
CONFLICTS="$(git merge-tree $(git merge-base HEAD master) HEAD master | grep -c "<<<<<<< " || echo 0)"
```

### Auto-Decision Matrix
**Enhanced Intelligent Merge Criteria**:

| Condition | Score | Action |
|-----------|-------|--------|
| Zero conflicts + successful workflow | +4 | Auto-SQUASH |
| Documentation optimization | +3 | Auto-SQUASH |
| ≤5 files modified + zero conflicts | +2 | Auto-SQUASH |
| Config/CLAUDE.md + docs updates | +2 | Auto-SQUASH |
| Session >2 hours BUT successful | +1 | Auto-SQUASH |
| **NEW THRESHOLD: ≥3 points** | | **AUTO-SQUASH** |
| **Error/Conflict detected** | | **USER PROMPT** |
| **User wants to abandon** | | **USER PROMPT** |

**Smart Automation Logic**:
```bash
# Enhanced Auto-Decision Implementation
if [[ $CONFLICTS -eq 0 && $WORKFLOW_SUCCESSFUL == "true" ]]; then
    SCORE=$((SCORE + 4))  # Zero conflicts + successful workflow
fi

if [[ "$SESSION_TYPE" == "docs-reorganization" || "$SESSION_TYPE" == "optimization" ]]; then
    SCORE=$((SCORE + 3))  # Documentation optimization
fi

if [[ $MODIFIED_FILES -le 5 && $CONFLICTS -eq 0 ]]; then
    SCORE=$((SCORE + 2))  # Small changes + clean
fi

# AUTO-SQUASH if score ≥3, otherwise prompt user
if [[ $SCORE -ge 3 && "$1" != "force-prompt" ]]; then
    echo "🔀 AUTO-SQUASH: Successful workflow detected"
    execute_squash_merge
else
    prompt_user_decision
fi
```

**Manual Review Only Required For**:
- 🔴 **Conflicts detected** → Manual resolution required
- 🔴 **User requests abandonment** → Confirmation needed
- 🔴 **Force-prompt flag used** → User wants to see options

### Success Notification Framework
**Auto-SQUASH Success Message**:
```
✅ WORKTREE SESSION COMPLETED
📊 SESSION: session-20250722-170816-docs-reorganization-optimization
🎯 ACTION: Auto-SQUASH executed (score: 4/3 threshold)
📈 CHANGES: 87 files changed, +1475/-14493 lines
🔀 RESULT: Successfully merged to master branch
🧹 CLEANUP: Work tree removed, session branch deleted

⚡ AUTOMATION: Future similar workflows will auto-SQUASH
💡 OVERRIDE: Use `/worktree-close force-prompt` to see all options
```

**User Decision Interface** (only when needed):
```
🎯 SESSION: session-20250722-143045-lifecycle
📊 CHANGES: 5 files modified, 2 new files
⚠️  CONFLICTS: 0 detected
🎚️  COMPLEXITY: 6/10

AUTO-MERGE CRITERIA: 2/3 points (threshold not met)

Choose completion action:
[1] 🔀 MERGE: Integrate changes to master
[2] 🗜️  SQUASH: Squash commits and merge (RECOMMENDED)
[3] 🗑️  ABANDON: Discard work tree changes
[4] 🔍 REVIEW: Show detailed diff before deciding

Selection [1-4]:
```

### Execution Framework
**Action Implementation**:

#### Merge Strategy
```bash
# 1. Switch to parent branch
cd "${ORIGINAL_PATH}"
git checkout "${PARENT_BRANCH}"

# 2. Execute merge
case "${MERGE_TYPE}" in
  "merge")
    git merge --no-ff "${BRANCH_NAME}" -m "Merge session: ${SESSION_ID}"
    ;;
  "squash")
    git merge --squash "${BRANCH_NAME}"
    git commit -m "session: ${SESSION_ID} | ${TOPIC} | squashed"
    ;;
esac

# 3. Cleanup branch
git branch -d "${BRANCH_NAME}"
```

#### Abandon Strategy
```bash
# 1. Switch to parent branch  
cd "${ORIGINAL_PATH}"
git checkout "${PARENT_BRANCH}"

# 2. Force delete work tree branch
git branch -D "${BRANCH_NAME}"

# 3. Log abandonment
echo "$(date -Iseconds): ABANDONED session-${SESSION_ID}" >> .claude/session-abandoned.log
```

### Session Cleanup Protocol
**Complete Environment Reset**:

```bash
# 1. Remove work tree
git worktree remove "${WORKTREE_PATH}" --force

# 2. Update session tracking
jq '.status = "completed"' .session-info > .session-completed.json
mv .session-completed.json ".claude/sessions/session-${SESSION_ID}.json"

# 3. Clear current session
rm -f .claude/session-current.json

# 4. Return to original directory
cd "${ORIGINAL_PATH}"
```

### Integration with Command Ecosystem
**Post-Closure Actions**:
- **Success Notification**: Display completion summary
- **Learning Capture**: Trigger `/capture-learnings` if valuable patterns
- **System Update**: Update cross-reference matrices
- **Git Commit**: Generate standardized commit for session tracking

## ⚡ Execution Layer

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of closure logic

```javascript
// 1. SESSION ASSESSMENT (real execution)
Read(".session-info") // Load session metadata
Bash("git diff --name-only HEAD~1..HEAD") // Count modified files
Bash("git merge-tree $(git merge-base HEAD master) HEAD master") // Check conflicts

// 2. DECISION LOGIC (real execution)
// Auto-decision matrix calculation or user prompt

// 3. MERGE EXECUTION (real execution)
Bash("cd [original-path] && git checkout [parent-branch]") // Switch branch
Bash("git merge [--no-ff|--squash] [session-branch]") // Execute merge
Bash("git branch -d [session-branch]") // Cleanup branch

// 4. CLEANUP (real execution)
Bash("git worktree remove [worktree-path] --force") // Remove work tree
Write(".claude/sessions/session-[id].json", "[session-completion-data]") // Archive session
```

### Success Verification
**Completion Checklist**:
- ✅ **Work Tree Removed**: Directory deleted successfully
- ✅ **Branch Cleaned**: Session branch removed or merged
- ✅ **Environment Reset**: Back to original working directory
- ✅ **Session Archived**: Metadata stored for future reference

### Output Format
```
✅ SESSION COMPLETED: session-20250722-143045-lifecycle
🔀 ACTION: Merged with squash to master
📊 SUMMARY: 5 files modified, 2 conflicts resolved
⏱️  DURATION: 45 minutes
🎯 TOPIC: Git work tree lifecycle implementation
```

## 🔗 Integration Points

### Automatic Triggers
**Session Completion Detection**:
- **Workflow End**: Auto-trigger after main command completion
- **Idle Detection**: Prompt closure after 2+ hours inactivity
- **Error States**: Emergency closure on critical failures

### Command Chain Integration
**Closure Workflow**:
```
Main Workflow Complete → /worktree-close assessment → User decision → Merge/Abandon → Cleanup → /capture-learnings
```

### Error Recovery
**Failure Scenarios**:
- **Merge Conflicts**: Switch to manual resolution mode
- **Missing Session**: Graceful degradation with manual work tree cleanup
- **Corrupted Metadata**: Bypass metadata, continue with manual assessment

---

**CRITICAL**: This command ensures clean session lifecycle completion with intelligent decision-making and comprehensive cleanup.

**EXECUTION COMMITMENT**: All documented automations implemented with real tool calls. Complete lifecycle integrity maintained.