# Development Workflow Standard

**Updated**: 2025-07-24 | **Authority**: Anthropic CLAUDE.md best practices | **Limit**: 100 lines

## Purpose

This file should document the team's development workflow, testing practices, git conventions, and collaboration processes. Based on official Anthropic recommendations, this guides Claude through proper development lifecycle procedures.

## Content Structure

### What Should Be Included

**Git Workflow:**
```markdown
# Git Conventions
- Branch naming: feature/description, fix/issue-number, hotfix/description
- Commit messages: Use conventional commits (feat:, fix:, docs:, etc.)
- Pull requests: Required for all changes to main branch
- Merge strategy: Squash commits vs. merge commits policy
```

**Testing Workflow:**
```markdown
# Testing Standards
- Run tests before committing: npm run test
- Prefer individual tests over full suite for performance
- Coverage requirements: minimum 80% for new code
- Integration tests: Required for API changes
```

**Code Review Process:**
```markdown
# Review Guidelines
- All code requires peer review
- Review checklist: functionality, tests, documentation
- Approval requirements: at least 1 reviewer
- CI/CD must pass before merge
```

**Release Process:**
```markdown
# Deployment Workflow
- Staging deployment: automated on develop branch
- Production deployment: tagged releases only
- Rollback procedure: documented emergency steps
- Version bumping: semantic versioning (semver)
```

## Implementation Guidelines

### Development Cycle
1. **Planning**: Issue creation and task breakdown
2. **Development**: Feature branch creation and coding
3. **Testing**: Local testing and validation  
4. **Review**: Code review and feedback integration
5. **Deployment**: Staging and production release

### Quality Gates
- **Pre-commit**: Linting, formatting, basic tests
- **Pre-push**: Full test suite, type checking
- **Pre-merge**: Code review, CI pipeline success
- **Pre-deploy**: Integration tests, performance checks

### Collaboration Standards
- **Communication**: Slack channels, meeting schedules
- **Documentation**: Update docs with code changes
- **Knowledge Sharing**: Code reviews as learning opportunities
- **Conflict Resolution**: Escalation procedures

## Benefits for AI Assistant

**Process Awareness**: Claude follows team workflows automatically
**Quality Assurance**: Integrates testing and validation steps
**Collaboration Support**: Understands review and approval processes
**Risk Reduction**: Follows established safety procedures

---

**Implementation Note**: This template should be populated with actual team workflow procedures, git branch strategies, CI/CD pipeline steps, and collaboration tools. The format follows Anthropic's guidance for comprehensive workflow documentation that enables AI assistants to participate effectively in development processes.