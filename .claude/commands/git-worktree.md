# Git-Worktree - Parallel Development Environment Manager

## 🎯 Purpose
Automate git worktree creation, management, and coordination for parallel AI development workflows.

## 🚀 Usage
Execute: `/git-worktree [quick|batch|cleanup|sync|status|exec] [parameters]`

## 🔧 Implementation

### Autocontained Notification System
```bash
#!/bin/bash
readonly B='\e[34m' G='\e[32m' R='\e[31m' Y='\e[33m' C='\e[36m' M='\e[35m' GB='\e[32;1m' N='\e[0m'
info()     { echo -e "${B}🔵 INFO${N}: $1"; }
success()  { echo -e "${G}🟢 SUCCESS${N}: $1"; }  
error()    { echo -e "${R}🔴 ERROR${N}: $1"; }
warn()     { echo -e "${Y}🟡 WARNING${N}: $1"; }
process()  { echo -e "${C}⚡ PROCESS${N}: $1"; }
data()     { echo -e "${M}📊 DATA${N}: $1"; }
complete() { echo -e "${GB}✅ COMPLETE${N}: $1"; }
```

### Git Worktree Management Protocol
**Automated Worktree Operations**:
```javascript
// 1. WORKTREE CREATION (real execution)
Bash("git worktree list") // List existing worktrees
Bash("git branch -r") // List remote branches for worktree options

// 2. WORKTREE SETUP AND COORDINATION (real execution)
Bash("git worktree add ../worktree-${BRANCH_NAME} ${BRANCH_NAME}") // Create new worktree
Bash("cd ../worktree-${BRANCH_NAME} && git status") // Verify worktree status

// 3. PARALLEL DEVELOPMENT COORDINATION (real execution)
Task("Worktree coordination", "coordinate multiple worktrees for parallel development workflows")
```

### Worktree Lifecycle Management
**Intelligent Worktree Operations**:
- **Quick Setup**: Rapid worktree creation for feature branches
- **Batch Operations**: Manage multiple worktrees simultaneously
- **Cleanup**: Remove orphaned and completed worktrees
- **Sync**: Coordinate changes across worktrees
- **Status**: Monitor all active worktrees

### Integration with Development Workflow
**Cross-Command Coordination**:
```javascript
// Integration with other development commands
Task("Development integration", "coordinate worktree management with monitoring and performance tracking")
```

## ⚡ Triggers

### Input Triggers
**Context**: Parallel development, feature isolation, branch management
**Keywords**: worktree, parallel, branch, isolation, development

### Output Triggers
**When**: New feature development → Create isolated worktree
**When**: Multiple features → Setup parallel worktrees
**Chain**: git-worktree → monitor-dev (for tracking) → track-performance (for metrics)

## 🔗 Module Integration

### Command Dependencies
**Development Workflow Integration**:
- `/monitor-dev` → Real-time monitoring of worktree activities
- `/track-performance` → Performance metrics for worktree operations
- `/analyze-parallel` → Optimization of parallel development workflows

### Success Indicators
**Setup Success**: Worktree created and functional within 30 seconds
**Coordination Success**: Multiple worktrees operating without conflicts
**Management Success**: Clean worktree lifecycle with proper cleanup

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
```javascript
// 1. WORKTREE MANAGEMENT (real execution)
Bash("git worktree list | wc -l") // Count active worktrees
Bash("git status --porcelain") // Check working tree status

// 2. PARALLEL COORDINATION (real execution)
Task("Worktree orchestration", "manage parallel development environments with intelligent coordination")

// 3. LIFECYCLE TRACKING (real execution)
Bash("echo 'Worktree session: $(date)' >> .git/worktree-sessions.log") // Log worktree operations
```

---

**CRITICAL**: This command provides intelligent git worktree management for parallel development workflows with real automation and coordination capabilities.