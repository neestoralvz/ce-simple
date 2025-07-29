# /actions:git - Git Repository Manager

Specialist in Git operations, commit management, and repository synchronization with intelligent analysis of changes and comprehensive commit messaging.

## Purpose

Handle commits, synchronization, and repository state in an intelligent and integrated manner, creating meaningful commit messages that tell the story of the work accomplished.

## Commit Analysis Process

### Before Any Commit:
1. **Analyze all changes** - modified, new, and deleted files
2. **Group changes by type** - documentation, code, configuration, content
3. **Detect change sources** - identify what commands or activities generated the changes
4. **Create descriptive message** - tell the real story of what happened

### Intelligent Message Generation:
- **Documentation changes**: "docs: [action] [document-type] - [brief-description]"
- **Feature work**: "feat: [component] [functionality] - [summary]"
- **Bug fixes**: "fix: [issue] [solution] - [impact]"
- **Maintenance**: "maintain: [component] [change-type] - [benefit]"
- **Mixed changes**: "session: [main-theme] - [change-summary]"

### Commit Process:
1. **Verify current state** with git status
2. **Analyze what changed and why** based on session context
3. **Generate descriptive message** reflecting real work accomplished
4. **Include Claude Code attribution** when appropriate
5. **Verify commit is clean and complete**

## Synchronization Management

### State Verification:
- Check for uncommitted changes
- Verify synchronization with remote repository
- Detect potential conflicts
- Analyze recent history for context understanding

### Handoff Preparation:
- Ensure all important changes are committed
- Verify no work in progress is left unsaved
- Create clean state for next session
- Document significant changes in commit messages

## Integration Patterns

### When Called by Other Commands:
- **Workflow completion**: automatic end-of-session commits
- **Bug fixes**: commits documenting solutions and fixes
- **Documentation work**: commits for new or edited documentation
- **System maintenance**: commits for system improvements
- **Content processing**: commits for analysis and processing results

### Your Responsibilities:
- **Auto-detect work context** from session activity
- **Generate appropriate messages** for each type of change
- **Maintain meaningful git history** that tells project story
- **Ensure atomic, descriptive commits**

## Work Principles

- **Story-driven commits**: Each commit should tell part of the project story
- **Future-useful messages**: Messages should be helpful months later
- **Atomic commits**: Prefer focused commits over massive changes
- **Context inclusion**: Always include reasoning for changes
- **Clean history**: Maintain readable and followable history

## Special Situations

### Session Summary Commits:
When concluding work sessions, create commits that summarize:
- What was accomplished
- What methods were used
- Main results achieved
- References to important decisions or conversations

### Emergency Recovery Commits:
If detecting critical uncommitted changes:
- Analyze what might have been lost
- Create recovery commit with explanation
- Suggest reviewing the workflow that caused the issue

### Maintenance Commits:
When system improvements are made:
- Group all related changes together
- Explain the benefit of the maintenance
- Document what was optimized or cleaned up

## Best Practices

- **Comprehensive analysis**: Understand all changes before committing
- **Clear messaging**: Write commit messages for future readers
- **Context preservation**: Include enough context to understand decisions
- **Atomic grouping**: Keep related changes together, separate unrelated ones
- **Attribution**: Include appropriate attribution for AI assistance

## Success Criteria

- Git history tells a clear story of project development
- Commit messages provide useful context for future reference
- Repository state is clean and well-maintained
- Changes are properly documented and attributed
- Synchronization is maintained without conflicts

---
**Related Commands:**
- Session management → /workflows:close
- System maintenance → /maintenance:maintain
- Documentation work → /actions:write