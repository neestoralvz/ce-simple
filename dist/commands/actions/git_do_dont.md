# /actions:git - Git Repository Manager

## DO
- Analyze all modified/new/deleted files before committing
- Group changes by type and identify what generated the changes
- **For complex analysis**: Apply systematic thinking to commit message generation
- Create descriptive messages that tell the real story of the work

## DON'T
- Make commits without analyzing the context of changes
- Skip validation of repository state before and after operations
- Create generic messages that don't reflect actual work performed
- Compromise system integrity for convenience

## Context
- Git status and diff analysis for change detection
- Session context for understanding work accomplished
- System state validation protocols
- Proper attribution requirements when using AI assistance

## Next Action
- **Automatic**: /workflows:close (after session-ending commits)
- **Recommended**: /maintenance:maintain (for repository health verification)
- **Context**: Continue workflow vs prepare handoff based on commit type