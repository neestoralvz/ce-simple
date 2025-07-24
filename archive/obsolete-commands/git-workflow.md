# Git Workflow - Integrated Version Control

## Purpose
Comprehensive git integration for workflow management with automated commits, branch coordination, and session tracking. Supports worktree sessions and collaborative development patterns.

## Principles and Guidelines
- **Descriptive Commits**: Every commit tells the story of what and why
- **Workflow Integration**: Git operations seamlessly integrated with development flow
- **Session Coordination**: Support for parallel development via worktrees
- **Recovery Protocols**: Error handling with commit-based recovery points

## Execution Process

### Phase 1: Workflow Git Initialization
```javascript
TodoWrite([
  {"content": "Check git repository status and working tree cleanliness", "status": "pending", "priority": "high", "id": "git-status-1"},
  {"content": "Create workflow start commit with baseline state", "status": "pending", "priority": "high", "id": "git-start-1"},
  {"content": "Initialize git session tracking metadata", "status": "pending", "priority": "high", "id": "git-session-1"}
])
```

### Phase 2: Worktree Session Management
```javascript
TodoWrite([
  {"content": "Evaluate if worktree session needed for complex workflows", "status": "pending", "priority": "high", "id": "git-worktree-eval-1"},
  {"content": "Create isolated worktree session if required (/worktree-start)", "status": "pending", "priority": "medium", "id": "git-worktree-create-1"},
  {"content": "Coordinate session metadata and tracking systems", "status": "pending", "priority": "medium", "id": "git-worktree-track-1"}
])
```

### Phase 3: Progress Commit Strategy
```javascript
TodoWrite([
  {"content": "Execute incremental commits at major workflow milestones", "status": "pending", "priority": "medium", "id": "git-progress-1"},
  {"content": "Generate descriptive commit messages following convention", "status": "pending", "priority": "medium", "id": "git-messages-1"},
  {"content": "Maintain clean commit history with logical progression", "status": "pending", "priority": "medium", "id": "git-history-1"}
])
```

### Phase 4: Error Recovery and Commit Points
```javascript
TodoWrite([
  {"content": "Create error recovery commits with diagnostic information", "status": "pending", "priority": "high", "id": "git-error-1"},
  {"content": "Implement rollback strategies for failed workflow steps", "status": "pending", "priority": "high", "id": "git-rollback-1"},
  {"content": "Document error resolution in commit messages", "status": "pending", "priority": "medium", "id": "git-error-doc-1"}
])
```

### Phase 5: Completion and Session Closure
```javascript
TodoWrite([
  {"content": "Create comprehensive success commit with workflow summary", "status": "pending", "priority": "high", "id": "git-success-1"},
  {"content": "Close worktree session if used (/worktree-close)", "status": "pending", "priority": "medium", "id": "git-worktree-close-1"},
  {"content": "Update git session tracking and cleanup metadata", "status": "pending", "priority": "low", "id": "git-cleanup-1"}
])
```

## Commit Message Conventions

### Workflow Start Commits
```bash
git commit -m "workflow: initialize [workflow-name] - [brief-description]

Context: [Current project state and goals]
Scope: [Areas of codebase that will be modified]
Strategy: [High-level approach being taken]

Generated with Claude Code"
```

### Progress Commits
```bash
git commit -m "workflow: [phase-name] complete - [key-achievements]

Completed:
- [Achievement 1]
- [Achievement 2]
- [Achievement 3]

Next: [Next phase or milestone]

Generated with Claude Code"
```

### Success Commits
```bash
git commit -m "workflow: [workflow-name] complete - [comprehensive-summary]

Summary:
- [Major outcome 1]
- [Major outcome 2]
- [Major outcome 3]

Files Modified: [List of key files changed]
Quality: [PTS compliance status]
Tests: [Testing status if applicable]

Generated with Claude Code"
```

### Error Recovery Commits
```bash
git commit -m "workflow: error recovery - [issue-description]

Issue: [What went wrong]
Root Cause: [Why it happened]
Resolution: [How it was fixed]
Prevention: [Steps to avoid in future]

Generated with Claude Code"
```

## Worktree Integration Patterns

### Simple Workflows (Single Branch)
- Use main branch with descriptive commits
- Suitable for: documentation updates, small fixes, simple features
- Commit frequency: Start, major milestones, completion

### Complex Workflows (Worktree Sessions)
- Create isolated worktree for development
- Use `/worktree-start` and `/worktree-close` commands
- Suitable for: major features, experimental changes, parallel development
- Merge back to main branch when complete

### Collaborative Workflows
- Coordinate with existing git workflows
- Respect branch protection and review requirements
- Generate pull request descriptions from commit history
- Maintain compatibility with team conventions

## Session Tracking Metadata

### Session File Structure
```json
{
  "session_id": "workflow-[timestamp]",
  "workflow_type": "[master-execute|specific-workflow]",
  "start_time": "[ISO-timestamp]",
  "start_commit": "[commit-hash]",
  "worktree_path": "[path-if-applicable]",
  "milestones": [
    {
      "phase": "[phase-name]",
      "commit": "[commit-hash]",
      "timestamp": "[ISO-timestamp]",
      "status": "success|error|pending"
    }
  ],
  "completion_status": "active|success|error|aborted",
  "end_time": "[ISO-timestamp]",
  "final_commit": "[commit-hash]"
}
```

### Metadata Operations
- **Create**: Initialize session tracking on workflow start
- **Update**: Add milestone commits and status changes
- **Query**: Check session status and progress
- **Cleanup**: Archive completed sessions and remove temporary data

## Git Command Integration

### Status and Validation
```bash
# Check repository status
git status --porcelain
git diff --cached --name-only
git branch --show-current

# Validate clean state
git stash list
git log --oneline -5
```

### Commit Operations
```bash
# Stage workflow changes
git add [specific-files]
git add -A  # Only when explicitly needed

# Create descriptive commits
git commit -m "$(cat <<'EOF'
[Commit message with proper formatting]
EOF
)"

# Push to remote (only when explicitly requested)
git push origin [branch-name]
```

### Worktree Operations
```bash
# Create worktree session
git worktree add [path] -b [session-branch]
cd [worktree-path]

# Session development
[workflow execution]

# Session completion
git checkout main
git merge [session-branch]
git worktree remove [path]
git branch -d [session-branch]
```

## Error Handling and Recovery

### Common Git Issues
- **Dirty Working Tree**: Stash or commit changes before proceeding
- **Merge Conflicts**: Provide clear resolution guidance
- **Branch Protection**: Respect repository policies and workflows
- **Permission Issues**: Escalate to user for authentication

### Recovery Strategies
- **Soft Reset**: Undo commits while preserving changes
- **Hard Reset**: Return to last known good state (with user confirmation)
- **Stash Recovery**: Restore accidentally stashed work
- **Branch Recovery**: Recreate branches from reflog

### Escalation Protocols
- **Authentication**: Request user to handle git credentials
- **Policy Conflicts**: Ask user about repository-specific workflows
- **Data Loss Risk**: Always confirm destructive operations
- **Complex Merges**: Escalate merge conflicts to user resolution

## Success Metrics

### Commit Quality
- **Descriptive Messages**: Clear what and why for every commit
- **Logical Progression**: Commits tell coherent development story
- **Clean History**: No unnecessary or confusing commits
- **Proper Attribution**: All commits properly attributed to Claude Code

### Workflow Integration
- **Seamless Operation**: Git operations don't disrupt workflow
- **Error Recovery**: ≥95% of git errors resolved automatically
- **Session Management**: 100% of worktree sessions properly closed
- **Metadata Accuracy**: Complete tracking of all workflow progress

### Repository Health
- **No Corruption**: Zero git repository integrity issues
- **Branch Cleanliness**: Temporary branches properly cleaned up
- **Conflict Resolution**: All merge conflicts properly resolved
- **Policy Compliance**: 100% adherence to repository workflows

---

**Single Responsibility**: Comprehensive git integration providing workflow-aware version control with automated commits, session tracking, error recovery, and seamless collaboration support.