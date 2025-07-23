# 09-git - Git & Version Control Commands

## Purpose
Advanced Git operations and version control orchestration. These commands provide intelligent Git workflows, automated branching strategies, and seamless integration with development processes.

## Commands
- `/worktree-start` - Initialize isolated development environment
- `/worktree-close` - Complete session with merge decisions
- `/worktree-cleanup` - Automated maintenance and cleanup
- `/branch-orchestrate` - Intelligent branching and merging
- `/commit-intelligent` - Smart commit generation and optimization

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
- **Worktree Management**: Isolated development environments
- **Intelligent Branching**: Automated branch creation and naming
- **Smart Commits**: Context-aware commit message generation
- **Merge Orchestration**: Conflict resolution and merge strategies
- **Repository Health**: Automated cleanup and maintenance

## Version Control Patterns
- Feature branch workflows with automatic cleanup
- Commit message standardization and automation
- Merge conflict prevention and resolution
- Repository organization and maintenance
- Integration with CI/CD and quality gates

## Integration Points
- Seamless integration with execution workflows
- Automatic documentation updates and commits
- Quality gate integration before merges
- Learning capture from Git history analysis
- Performance tracking through commit metrics

---
*Category 09: Version control orchestration and automation*