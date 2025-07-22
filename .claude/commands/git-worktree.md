# Git-Worktree - Parallel Development Environment Manager

## 🎯 Purpose
Automate git worktree creation, management, and coordination for parallel AI development workflows

## 🚀 Usage  
Execute: `/git-worktree [quick|batch|cleanup|sync|status|exec] [parameters]`

## 🔧 Implementation

### Parallel WorkTree Creation Protocol
1. **CREATE**: Generate multiple worktrees for independent development streams
2. **COORDINATE**: Sync essential files (CLAUDE.md, .cursorrules) across environments  
3. **MONITOR**: Track worktree status and resource utilization
4. **CLEANUP**: Remove merged/completed worktrees automatically
5. **EXECUTE**: Run parallel commands across all environments

### Automated Coordination Framework
**Quick Creation**:
```bash
Bash("./tools/automation-suite.sh quick [feature-name]") // Single worktree
```

**Batch Creation**:
```bash
Bash("./tools/automation-suite.sh batch [feature1 feature2 ...]") // Multiple parallel worktrees
```

**Status Overview**:
```bash
Bash("./tools/automation-suite.sh status") // Development status overview
```

### Integration Protocol
**Pre-Creation Validation**: Verify git repository status and available space
**Post-Creation Sync**: Distribute coordination files to all worktrees
**Cross-Environment Commands**: Execute commands in parallel across worktrees

## ⚡ Triggers

### Input Triggers
**Context**: Need for parallel development streams or AI agent coordination
**Previous**: `/start` → complex feature development requiring isolation
**Keywords**: parallel, worktree, development, isolation, concurrent

### Output Triggers
**When**: Worktrees created → `/monitor-dev` for real-time tracking
**When**: Development complete → `/analyze-parallel` for performance assessment
**Chain**: git-worktree → monitor-dev → analyze-parallel → track-performance

### Success Patterns
**Creation Success**: Multiple worktrees available → Begin parallel development
**Coordination Success**: Files synced across environments → Consistent AI behavior
**Management Success**: Clean worktree state maintained → Optimal resource usage

---

**CRITICAL**: Manages git worktree infrastructure for aggressive parallelization workflows with automatic coordination file distribution