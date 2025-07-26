# Known Issues & Warnings Standard

**Updated**: 2025-07-24 | **Authority**: Anthropic CLAUDE.md best practices | **Limit**: 100 lines

## Purpose

This file should document project-specific quirks, limitations, known bugs, workarounds, and important warnings that Claude needs to be aware of when working on the project. Based on official Anthropic recommendations, this prevents AI from running into predictable issues.

## Content Structure

### What Should Be Included

**System Limitations:**
```markdown
# Known Limitations
- Memory usage: Large datasets cause performance degradation
- Browser compatibility: IE11 not supported, Safari requires polyfills
- Mobile responsiveness: Layout issues on screens <320px
- File uploads: 10MB maximum size limit
```

**Common Issues & Workarounds:**
```markdown
# Frequent Problems
- Build fails on Windows: Use WSL2 or update line endings to LF
- Hot reload broken: Clear node_modules and restart dev server
- Types not updating: Restart TypeScript server in IDE
- Tests flaky: Run individually rather than full suite
```

**Deprecated/Legacy Code:**
```markdown
# Legacy Warnings
- AuthService.old.js: Deprecated, use AuthManager instead
- /api/v1/* endpoints: Use /api/v2/* for new features
- jQuery components: Migrate to React when modifying
- CSS classes .old-*: Replace with .new-* variants
```

**Environment-Specific Issues:**
```markdown
# Platform Problems
- macOS: Requires Xcode command line tools for native dependencies
- Windows: Python 2.7 needed for node-gyp compilation
- Linux: libvips installation required for image processing
- Docker: Volumes don't sync properly on Windows containers
```

## Implementation Guidelines

### Issue Classification
- **Critical**: Breaks functionality, needs immediate attention
- **Major**: Significant impact on development or user experience
- **Minor**: Inconvenience or cosmetic issues
- **Informational**: Good to know, doesn't block work

### Documentation Format
- **Problem Description**: Clear explanation of the issue
- **Reproduction Steps**: How to encounter the problem
- **Workaround**: Temporary solution or mitigation
- **Permanent Fix**: Long-term resolution if known

### Update Procedures
- **Regular Review**: Monthly check for resolved issues
- **Version Tracking**: Link issues to specific software versions
- **Resolution Status**: Mark when issues are fixed
- **Historical Context**: Keep resolved issues for reference

## Benefits for AI Assistant

**Issue Avoidance**: Claude can prevent known problems proactively
**Faster Resolution**: Immediate access to documented workarounds
**Context Awareness**: Understands project-specific constraints
**User Support**: Can guide users through common issues

---

**Implementation Note**: This template should be populated with actual project issues, documented bugs from issue tracker, common support questions, and platform-specific problems. The format follows Anthropic's guidance for proactive issue documentation that enables AI assistants to provide better technical support and avoid known pitfalls.