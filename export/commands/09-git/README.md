# 09-git - Git & Version Control Commands

## Purpose
Advanced Git operations and version control orchestration. These commands provide intelligent Git workflows, automated branching strategies, and seamless integration with development processes.

## Commands
- `/worktree-start` - Initialize isolated development environment with session metadata framework
- `/worktree-close` - Complete session with enhanced auto-decision matrix and merge orchestration
- `/worktree-cleanup` - Automated maintenance with intelligent orphan detection and safety protocols
- `/git-worktree` - Parallel development environment manager with lifecycle tracking
- `/branch-orchestrate` - Intelligent branching and merging (planned)
- `/commit-intelligent` - Smart commit generation and optimization (planned)

## Category Relations
- **Triggered by**: 00-core for environment setup
- **Coordinates with**: 04-execution for implementation tracking
- **Uses**: 14-utils for Git utilities and automation
- **Reports to**: 07-maintenance for repository health

## Usage Patterns
```
00-core/start → 09-git/worktree-start → 04-execution/implement
04-execution/complete → 09-git/commit → 05-validation/verify
05-validation/pass → 09-git/worktree-close → 08-learning/capture
```

## Git Workflow Features
- **Session-Based Worktrees**: Isolated development with unique session IDs and metadata tracking
- **Auto-Decision Matrix**: ≥3 points threshold for automated merge decisions with zero conflicts
- **Lifecycle Management**: Comprehensive worktree creation, coordination, and intelligent cleanup
- **Parallel Development**: Multi-worktree coordination with conflict prevention and health monitoring
- **Safety-First Cleanup**: Orphan detection with ≥4 points auto-cleanup threshold and interactive prompts
- **Intelligent Automation**: Auto-SQUASH for documentation, small changes, and successful workflows
- **Repository Health**: Proactive maintenance with system integrity verification

## Version Control Patterns
- **Session Workflows**: `session-[timestamp]-[topic]` branching with automated lifecycle
- **Auto-Merge Logic**: Zero conflicts + successful workflow → Auto-SQUASH execution
- **Maintenance Schedules**: Daily orphan cleanup, weekly stale session review
- **Safety Protocols**: Multi-layer validation with backup and rollback capabilities
- **Integration Triggers**: Auto-trigger from `/start` for complex workflows
- **Learning Integration**: Automatic `/capture-learnings` trigger for valuable patterns

## Integration Points
- Seamless integration with execution workflows
- Automatic documentation updates and commits
- Quality gate integration before merges
- Learning capture from Git history analysis
- Performance tracking through commit metrics

---
*Category 09: Version control orchestration and automation*