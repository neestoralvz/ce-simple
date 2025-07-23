# Worktree Start - Session Initialization

## 🎯 Purpose
Initialize new Git work tree for isolated session development with automated lifecycle management.

## 🚀 Usage
Execute: `/worktree-start [optional: topic-description]`

## 🔧 Implementation

### Session Metadata Framework
```bash
# Session ID generation with topic context
SESSION_ID="$(date +%Y%m%d-%H%M%S)"
TOPIC_HASH="${1:-general}"
BRANCH_NAME="session-${SESSION_ID}-${TOPIC_HASH}"
WORKTREE_PATH="../ce-session-${SESSION_ID}"
```

### Lifecycle Initialization Protocol
**MANDATORY**: Session tracking with metadata creation

```javascript
TodoWrite([
  {"content": "🏗️ VALIDATE: Check git repository status and ensure clean state", "status": "pending", "priority": "high", "id": "wt-validate-1"},
  {"content": "🌿 CREATE: Generate new work tree with unique session branch", "status": "pending", "priority": "high", "id": "wt-create-1"},
  {"content": "📊 METADATA: Create session tracking file with comprehensive info", "status": "pending", "priority": "high", "id": "wt-metadata-1"},
  {"content": "🔄 SWITCH: Change to work tree directory for isolated development", "status": "pending", "priority": "high", "id": "wt-switch-1"},
  {"content": "✅ VERIFY: Confirm work tree setup and session activation", "status": "pending", "priority": "medium", "id": "wt-verify-1"}
])
```

### Auto-Validation Protocol
**Pre-Flight Checks**:
1. **Git Status**: Ensure repository is in clean state
2. **Branch Verification**: Check current branch and staged changes
3. **Work Tree List**: Verify no conflicting work trees exist
4. **Path Availability**: Confirm target work tree path is available

### Session Creation Framework
**Work Tree Generation**:
```bash
# 1. Create work tree with new branch
git worktree add "${WORKTREE_PATH}" -b "${BRANCH_NAME}"

# 2. Generate session metadata
cat > "${WORKTREE_PATH}/.session-info" << EOF
{
  "session_id": "${SESSION_ID}",
  "branch_name": "${BRANCH_NAME}",
  "topic": "${TOPIC_HASH}",
  "created": "$(date -Iseconds)",
  "status": "active",
  "parent_branch": "$(git branch --show-current)",
  "complexity_score": 0,
  "files_modified": [],
  "auto_close_eligible": true
}
EOF

# 3. Switch to work tree
cd "${WORKTREE_PATH}"
```

### Session State Management
**Active Session Tracking**:
- **Current Session**: Store in `.claude/session-current.json`
- **Session Registry**: Append to `.claude/session-registry.log`
- **Work Tree List**: Update active work tree tracking

### Integration Points
**Command Chain Integration**:
- **Pre-Start**: Execute before main workflow commands
- **Auto-Trigger**: Activate when `/start` detects complex workflow
- **Manual Override**: Direct invocation for explicit session control

### Error Handling Framework
**Failure Recovery**:
- **Repository Issues**: Abort with clear error messaging
- **Path Conflicts**: Auto-generate alternative paths
- **Branch Conflicts**: Append timestamp for uniqueness
- **Metadata Failures**: Continue without metadata (degraded mode)

## ⚡ Execution Layer

### Mandatory Tool Executions
**CRITICAL**: Actual tool calls implementing session initialization

```javascript
// 1. PRE-VALIDATION (real execution)
Bash("git status --porcelain && git branch --show-current") // Check repo state
Bash("git worktree list") // List existing work trees

// 2. SESSION CREATION (real execution)  
Bash("git worktree add ../ce-session-[session-id] -b session-[session-id]-[topic]") // Create work tree
Write(".session-info", "[session-metadata-json]") // Create metadata

// 3. ENVIRONMENT SWITCH (real execution)
Bash("cd ../ce-session-[session-id] && pwd") // Switch to work tree

// 4. VERIFICATION (real execution)
Bash("git status && git branch") // Verify work tree state
```

### Success Indicators
- **Work Tree Created**: New directory with independent git state
- **Branch Active**: Session branch checked out in work tree
- **Metadata Generated**: Session tracking file created
- **Environment Ready**: Work tree ready for isolated development

### Output Format
```
🌿 WORKTREE: session-20250722-143045-lifecycle created
📍 LOCATION: /Users/nalve/ce-session-20250722-143045
🌿 BRANCH: session-20250722-143045-lifecycle
📊 STATUS: Active session ready for development
```

## 🔗 Integration Points

### Command Dependencies
**Pre-Requisites**: Clean git repository, valid branch state
**Post-Actions**: Ready for main workflow commands
**Integration**: Seamless handoff to existing command ecosystem

### Lifecycle Integration
**Session Start**: Initialize → `/worktree-start` → main workflow
**Session Management**: Ongoing work in isolated environment
**Session Completion**: Use `/worktree-close` for merge/abandon decision

---

**CRITICAL**: This command establishes isolated development environment for session-based workflows. All subsequent work occurs in work tree until session closure.

**EXECUTION COMMITMENT**: Every automation above implemented with actual tool calls. No documentation theater.