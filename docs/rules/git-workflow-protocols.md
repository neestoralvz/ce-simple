# Git Workflow Protocols

**Last Updated: 2025-07-24**
**Authority**: Git workflow standards implementing Partnership Protocol

## Commit Excellence Standards

### Claude Code Commit Protocol
**All commits must include Claude signature**:
- **Signature Format**: Every commit message ends with:
```
🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```
- **Required Implementation**: Use heredoc format for proper formatting
- **No Exceptions**: Every commit requires Claude attribution
- **Automated Integration**: Build into git hooks and automation tools

### Commit Message Structure
**Clear, actionable commit messages**:
- **Format**: `<type>: <description>` followed by signature
- **Types**: feat, fix, docs, refactor, test, style, chore
- **Description**: Clear action and outcome (≤72 characters)
- **Context**: Include why the change was made, not just what

### Commit Scope and Atomicity
- **Single Purpose**: One logical change per commit
- **Complete Changes**: All related files included in single commit
- **Functional Units**: Commits represent working states
- **Rollback Safety**: Each commit can be safely reverted

## Branch Management Excellence

### Git Worktree Strategy
**Mandatory parallel development approach**:
- **Worktree Requirement**: Use git worktrees for parallel feature development
- **Isolation Benefits**: Independent working directories for different features
- **Context Switching**: Seamless transition between feature contexts
- **Resource Efficiency**: Shared .git directory with multiple working trees

### Branch Naming Conventions
- **Feature Branches**: `feature/descriptive-name`
- **Bugfix Branches**: `fix/issue-description`
- **Documentation**: `docs/section-update`
- **Maintenance**: `chore/task-description`

### Integration Patterns
- **Fast-Forward Preferred**: Keep linear history when possible
- **Merge Commits**: For complex feature integration
- **Rebase Strategy**: Clean up local history before integration
- **Conflict Resolution**: Immediate resolution with team coordination

## Advanced Git Operations

### Pre-Commit Quality Gates
**Automated validation before commits**:
- **PTS Compliance**: Validate all changes against 12-component framework
- **File Size Limits**: Enforce line limits (commands ≤150, docs ≤200)
- **Cross-Reference Validation**: Check documentation links and references
- **Quality Metrics**: Run automated quality checks

### Repository State Management
- **Status Monitoring**: Regular git status checks before operations
- **Diff Analysis**: Review changes before commit with git diff
- **Log Analysis**: Understand commit history and patterns
- **Branch Hygiene**: Regular cleanup of merged branches

### Conflict Resolution Protocol
- **Immediate Resolution**: Address merge conflicts immediately
- **Context Preservation**: Maintain both sides' intent when possible
- **Documentation Updates**: Update related documentation for resolved conflicts
- **Pattern Learning**: Document resolution patterns for similar future conflicts

## Tool Integration and Automation

### Git Integration with Development Tools
**Seamless workflow integration**:
- **Editor Integration**: Git status and operations visible in development environment
- **Automated Hooks**: Pre-commit, pre-push, and post-merge automation
- **CI/CD Integration**: Automated testing and deployment triggers
- **Monitoring Tools**: Real-time repository health monitoring

### Version Control Best Practices
- **Regular Commits**: Frequent commits with meaningful progress
- **Backup Strategy**: Regular pushes to remote repositories
- **Tag Management**: Version tagging for stable releases
- **Archive Strategy**: Systematic archiving of obsolete branches

## Cross-Module Integration

### Git + Tool Usage Protocols
- **Parallel Git Operations**: Multiple git operations in different worktrees
- **Version Control Agents**: Dedicated sub-agents for git operations
- **State Coordination**: Git state consistency across parallel development
- **Change Aggregation**: Coordinate changes from multiple development streams

### Git + Development Standards
- **Commit Quality**: Every commit meets PTS 12-component requirements
- **File Organization**: Git operations respect project structure authority
- **Documentation Sync**: Commits include documentation updates when needed
- **Change Validation**: All git operations validated against development standards

### Git + Project Governance
- **Structure Integrity**: Git operations preserve project structure
- **Authority Respect**: Git changes align with directory authority hierarchy
- **File Management**: Git operations follow file management protocols
- **System Integration**: Git workflow supports overall project governance

---

**Application**: These protocols ensure git operations maintain system quality while supporting efficient collaborative development. Reference for all version control decisions and workflow optimization.