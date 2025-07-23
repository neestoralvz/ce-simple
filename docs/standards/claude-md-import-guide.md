# CLAUDE.md Import Strategies Guide

**Purpose**: Comprehensive guide for implementing @ import strategies in CLAUDE.md files for maximum efficiency and context utilization.

## Overview

CLAUDE.md files support native @ import syntax that automatically includes complete file contents when Claude Code CLI starts sessions, enabling dynamic context management and eliminating duplication.

## Import Syntax

### Basic @ Import
```markdown
@docs/core/project-structure.md
@docs/commands/command-index.md
@docs/standards/command-standards.md
```

### File Path Rules
- **Relative paths**: From CLAUDE.md location
- **Absolute paths**: From project root
- **Nested directories**: Full path specification required
- **Extensions**: .md files automatically processed

## Strategic Implementation

### Phase 1: Core Content Imports
```markdown
# CLAUDE.md - Optimized with Imports

## System Overview
Brief system description (keep essential info here)

## Project Structure
@docs/core/project-structure.md

## Command System
@docs/commands/command-index.md

## Development Standards
@docs/standards/command-standards.md
```

**Result**: ~40 lines CLAUDE.md + complete imported content availability

### Phase 2: Selective Content Organization
```markdown
# Import high-value, frequently referenced content
@docs/core/principles.md           # Core architectural principles
@docs/frameworks/execution-patterns.md # Common execution patterns
@10-standards/template-command.md  # Command development template
```

### Phase 3: Dynamic Content Management
```markdown
# Use # during sessions to add content automatically
# Claude incorporates improvements into relevant CLAUDE.md files
# Team benefits through git commits
```

## File Organization Strategy

### Import Hierarchy
1. **Essential Context** (Always import)
   - Project structure
   - Core principles  
   - Command index
   - Development standards

2. **Functional Context** (Import as needed)
   - Framework specifications
   - Pattern libraries
   - Template structures

3. **Reference Material** (Keep as links)
   - Detailed implementation guides
   - Historical documentation
   - External resources

### Content Distribution
```
CLAUDE.md (40-50 lines)
├── @docs/core/project-structure.md     # Complete directory tree
├── @docs/commands/command-index.md     # All command listings  
├── @docs/standards/command-standards.md # Development requirements
└── Brief overview and navigation
```

## Best Practices

### Content Organization
- **Single source of truth**: Define content once, import everywhere
- **Progressive disclosure**: Core info in CLAUDE.md, details in imports
- **Logical grouping**: Organize imports by functional area
- **Update efficiency**: Changes in imported files automatically reflected

### File Structure
```markdown
# CLAUDE.md Template with Imports

**Last Updated**: [Date]

## System Overview
[Essential system description - 3-5 lines]

## Project Structure  
@docs/core/project-structure.md

## Command System
@docs/commands/command-index.md

## Development Standards
@docs/standards/command-standards.md

## Quick Start
[Essential entry points - 3-5 lines]

---
**System Principle**: [Core philosophy]
```

### Import Selection Criteria
✅ **Include**: Frequently referenced, stable content  
✅ **Include**: Core architectural information  
✅ **Include**: Standards and requirements  
❌ **Exclude**: Highly dynamic content  
❌ **Exclude**: Implementation-specific details  
❌ **Exclude**: Experimental documentation  

## Performance Optimization

### Token Budget Management
- **Before**: 196 lines with duplication
- **After**: ~40 lines + imported content (no duplication)
- **Benefit**: More context available within same token budget

### Context Quality
- **Complete information**: All imported content available to Claude
- **No navigation required**: User doesn't need to manually access files
- **Consistent updates**: Changes automatically reflected in all sessions

## Team Collaboration

### Dynamic Content Addition
```bash
# During Claude Code session
# Press # to add instructions that Claude incorporates automatically
# Example workflow:
User: # Remember to run npm run typecheck after code changes
Claude: Added to CLAUDE.md - team will benefit from this guideline
```

### Git Integration  
```bash
# Include CLAUDE.md changes in commits
git add CLAUDE.md docs/
git commit -m "docs: add typecheck reminder to development workflow"
```

### Shared Context Benefits
- **Team consistency**: All developers get same context
- **Knowledge capture**: Best practices automatically documented
- **Onboarding efficiency**: New team members get complete project context

## Migration Strategy

### From References to Imports
```markdown
# Before (Reference)
[Ver estructura completa →](docs/core/project-structure.md)

# After (Import)  
@docs/core/project-structure.md
```

### Validation Process
1. **Test imports**: Verify all @ paths resolve correctly
2. **Measure efficiency**: Compare token usage and context quality
3. **Team feedback**: Ensure improved development experience
4. **Iterate**: Adjust import selections based on usage patterns

## Advanced Patterns

### Conditional Imports (Future)
```markdown
# Development vs Production context
@docs/dev/debug-guidelines.md     # Development only
@docs/prod/deployment-checklist.md # Production only
```

### Hierarchical Organization
```markdown
# Global context
@~/.claude/global-standards.md

# Project context  
@docs/core/project-context.md

# Local context
@CLAUDE.local.md
```

## Success Metrics

### Quantitative
- **File size reduction**: CLAUDE.md <50 lines
- **Context completeness**: 100% essential info available
- **Maintenance efficiency**: Single-point updates
- **Token optimization**: More context per token

### Qualitative  
- **Developer experience**: Faster onboarding, better AI assistance
- **Team consistency**: Shared understanding and practices
- **Knowledge management**: Automatic capture and distribution

---

**Implementation Priority**: High - Transform CLAUDE.md from static reference to dynamic context engine for maximum AI development efficiency.