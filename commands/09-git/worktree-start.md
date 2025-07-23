# Worktree Start - Session Initialization

## Purpose
Initialize new Git worktree for isolated session development with automated lifecycle management, metadata tracking, and seamless environment preparation.

## Principles and Guidelines
- **Session Metadata Framework**: Generate unique session IDs with topic context and comprehensive tracking information
- **Auto-Validation Protocol**: Pre-flight checks ensuring repository clean state and path availability
- **Session Creation Framework**: Automated worktree generation with branch creation and metadata population
- **Integration Points**: Seamless handoff to existing command ecosystem with lifecycle tracking

## Execution Process

### Phase 1: Pre-Validation and Repository Assessment
```javascript
TodoWrite([
  {"content": "Check git repository status and ensure clean state", "status": "pending", "priority": "high", "id": "wt-validate-1"},
  {"content": "Verify current branch and staged changes status", "status": "pending", "priority": "high", "id": "wt-branch-1"},
  {"content": "Confirm target worktree path availability", "status": "pending", "priority": "high", "id": "wt-path-1"}
])
```

### Phase 2: Session Generation and Worktree Creation
```javascript
TodoWrite([
  {"content": "Generate new worktree with unique session branch", "status": "pending", "priority": "high", "id": "wt-create-1"},
  {"content": "Create session tracking file with comprehensive metadata", "status": "pending", "priority": "high", "id": "wt-metadata-1"}
])
```

### Phase 3: Environment Setup and Verification
```javascript
TodoWrite([
  {"content": "Switch to worktree directory for isolated development", "status": "pending", "priority": "high", "id": "wt-switch-1"},
  {"content": "Verify worktree setup and session activation", "status": "pending", "priority": "medium", "id": "wt-verify-1"}
])
```

### Phase 4: Session State Management and Integration
```javascript
TodoWrite([
  {"content": "Update session registry and active session tracking", "status": "pending", "priority": "medium", "id": "wt-registry-1"},
  {"content": "Prepare environment for main workflow command integration", "status": "pending", "priority": "medium", "id": "wt-integrate-1"}
])
```

## Session Framework Architecture

### Metadata Generation
**Session ID**: Timestamp-based unique identifier with topic context
**Branch Naming**: `session-[timestamp]-[topic]` pattern for clear identification
**Path Structure**: `../ce-session-[session-id]` for consistent organization
**Tracking File**: Comprehensive JSON metadata with status, complexity score, and modification tracking

### Auto-Validation Components
**Repository State**: Git status verification with clean working tree requirement
**Branch Verification**: Current branch and staged changes assessment
**Path Availability**: Target worktree path collision prevention
**Worktree Registry**: Existing worktree conflict detection

### Error Handling Framework
**Failure Recovery**: Abort with clear error messaging for repository issues
**Path Conflicts**: Auto-generate alternative paths with timestamp suffixes
**Branch Conflicts**: Append additional timestamp for uniqueness guarantee
**Metadata Failures**: Continue without metadata in degraded mode

## Integration Architecture

### Command Chain Integration
**Pre-Start Execution**: Execute before main workflow commands for isolation setup
**Auto-Trigger Activation**: Activate when `/start` detects complex workflow requirements
**Manual Override**: Direct invocation for explicit session control and management

### Success Indicators
**Worktree Created**: New directory with independent git state and proper branch checkout
**Branch Active**: Session branch checked out in worktree with clean status
**Metadata Generated**: Session tracking file created with comprehensive information
**Environment Ready**: Worktree ready for isolated development with full integration

---

**Single Responsibility**: Session initialization engine establishing isolated development environment for session-based workflows with comprehensive lifecycle management and seamless integration capabilities.