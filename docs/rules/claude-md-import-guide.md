# CLAUDE.md Import Strategies Guide

**Purpose**: Comprehensive @ import strategies in CLAUDE.md for maximum efficiency and context utilization in Claude Code.

## Overview | Import Syntax Rules

CLAUDE.md supports @ syntax that includes complete file contents when Claude Code starts, creating dynamic context without duplication.

### Basic Syntax Examples
- `@docs/core/project-structure.md` - Relative from CLAUDE.md location
- `@/Users/project/docs/standards.md` - Absolute path from root
- `@docs/nested/deep/content.md` - Full nested path support
- All .md files are auto-processed with full content inclusion

### Path Resolution Rules
1. **Relative paths**: Start from CLAUDE.md directory
2. **Absolute paths**: Start from filesystem root
3. **Nested support**: Unlimited directory depth
4. **Auto-extension**: .md assumed if not specified

## Strategic Implementation | 3 Phases

### Phase 1: Core Architecture Imports (~40 lines + complete content)
```markdown
# CLAUDE.md - Optimized Structure
## System Overview
Brief 3-5 line project summary with key objectives and approach.

## Project Structure
@docs/core/project-structure.md

## Command System
@docs/commands/command-index.md

## Development Standards  
@docs/standards/command-standards.md

## Quality Framework
@docs/frameworks/pts-framework.md
```

### Phase 2: Selective Content Organization (High-value additions)
- `@docs/core/system-principles.md` - Core architectural principles
- `@docs/frameworks/execution-patterns.md` - Proven implementation patterns
- `@export/commands/10-standards/template-command.md` - Command templates
- `@docs/patterns/validated-approaches.md` - Successful pattern library

### Phase 3: Dynamic Content Management
Claude automatically adds content during sessions:
```bash
# Session workflow
Claude identifies missing context → Adds @import to CLAUDE.md → 
git add CLAUDE.md → commit "docs: add import for [context]"
```

## File Organization | Import Hierarchy

### Essential Imports (Always Include)
- **Structure**: Project layout, directory organization
- **Core Principles**: Foundational development guidelines  
- **Command Standards**: Implementation requirements and templates
- **Quality Framework**: Validation and compliance standards

### Functional Imports (Context-Dependent)
- **Execution Frameworks**: When implementing complex workflows
- **Pattern Libraries**: When applying proven solutions
- **Template Systems**: When creating new components

### Reference Links (Not Imported)
- **Historical Documentation**: Archived decisions and evolution
- **External Guides**: Third-party documentation and tutorials
- **Implementation Details**: Specific code examples and snippets

### Content Distribution Strategy
- **CLAUDE.md**: 40-50 lines with strategic imports
- **Imported Files**: Detailed content (50-200 lines each)
- **Total Context**: Complete information without navigation overhead

## Best Practices | Content Organization

### Single Source of Truth (SSOT)
- Define content once in dedicated files
- Import everywhere needed via @ syntax
- Automatic updates reflect across all contexts
- Eliminate duplication and synchronization issues

### Progressive Disclosure
- Core concepts in CLAUDE.md overview
- Detailed implementation in imported files
- Advanced patterns in specialized imports
- Logical information hierarchy maintained

### Import Selection Criteria
✅ **Include**: Frequently referenced content; Core architecture decisions; Development standards; Quality frameworks; Proven patterns

❌ **Exclude**: Dynamic session content; Implementation-specific details; Experimental approaches; Temporary documentation

## Performance | Token Management Optimization

### Before Import Strategy
- CLAUDE.md: 196 lines with duplicated content
- Multiple file references requiring navigation
- Context switching overhead for complete information
- Redundant content across multiple files

### After Import Strategy  
- CLAUDE.md: ~40 lines + complete imported content
- Immediate access to all essential information
- Higher context density per token consumed
- No navigation required for comprehensive understanding

### Efficiency Metrics
- **Token Efficiency**: 3x more context per token
- **Access Speed**: Immediate vs. multi-step navigation
- **Information Completeness**: 100% essential content available
- **Maintenance Overhead**: Single-point updates vs. multiple file sync

## Team Collaboration | Dynamic Content Addition

### Session-Based Enhancement
```bash
# During development session
Claude identifies knowledge gap → 
Adds relevant @import to CLAUDE.md →
git add CLAUDE.md →
git commit -m "docs: add import for [specific context]"
```

### Collaboration Benefits
- **Team Consistency**: Everyone works with same context
- **Knowledge Capture**: Automatic documentation of discovered patterns
- **Efficient Onboarding**: New team members get complete context immediately
- **Context Evolution**: Documentation grows organically with project needs

### Workflow Examples
```markdown
# Developer A discovers pattern
Session adds: @docs/patterns/error-handling.md

# Developer B encounters same scenario  
Pattern automatically available via import

# Team meeting reviews additions
Validates and refines imported content
```

## Migration Strategy | References to Imports

### Current State Analysis
```markdown
# Before: Static references
[Ver estructura →](docs/structure.md)
[Command patterns →](docs/commands/)
[Quality standards →](docs/standards/)
```

### Target State Implementation
```markdown  
# After: Dynamic imports
@docs/structure.md
@docs/commands/patterns.md
@docs/standards/quality.md
```

### Migration Steps
1. **Audit Current**: Identify all reference links in CLAUDE.md
2. **Prioritize Content**: Rank by frequency and importance of access
3. **Convert Incrementally**: Replace references with imports in priority order
4. **Validate Functionality**: Test import paths and content accessibility
5. **Measure Efficiency**: Compare token usage and access patterns
6. **Team Feedback**: Gather developer experience improvements
7. **Iterate Optimization**: Refine based on usage patterns

## Advanced Patterns | Complex Scenarios

### Conditional Context Imports
```markdown
# Development environment
@docs/dev/debug-patterns.md
@docs/dev/testing-frameworks.md

# Production environment  
@docs/prod/deployment-procedures.md
@docs/prod/monitoring-standards.md
```

### Hierarchical Import Chains
```markdown
# Global Claude configuration
@~/.claude/global-standards.md

# Project-specific overrides
@docs/core/project-standards.md  

# Local development customizations
@CLAUDE.local.md
```

### Domain-Specific Import Sets
```markdown
# Frontend development
@docs/frontend/react-patterns.md
@docs/frontend/styling-standards.md

# Backend development
@docs/backend/api-patterns.md
@docs/backend/database-standards.md
```

## Error Handling | Troubleshooting

### Common Import Issues
- **Path Resolution Errors**: Verify relative/absolute path accuracy
- **Content Not Found**: Check file existence and permissions
- **Circular Dependencies**: Avoid imports that reference each other
- **Performance Impact**: Monitor token consumption with large imports

### Debugging Strategies
1. **Path Validation**: Test import paths in isolation
2. **Content Verification**: Confirm imported content renders correctly
3. **Performance Monitoring**: Track token usage before/after imports
4. **Incremental Testing**: Add imports one at a time to identify issues

## Success Metrics

### Quantitative Measurements
- **CLAUDE.md Size**: <50 lines core content
- **Context Completeness**: 100% essential information accessible
- **Update Efficiency**: Single-point changes propagate automatically
- **Token Optimization**: >3x context density improvement
- **Access Speed**: Immediate vs. multi-step navigation eliminated

### Qualitative Improvements  
- **Developer Experience**: Faster onboarding with complete context
- **Team Consistency**: Everyone works with identical information
- **Knowledge Evolution**: Automatic capture of discovered patterns
- **Documentation Quality**: Higher accuracy through SSOT principle
- **Maintenance Efficiency**: Reduced synchronization overhead

---
**Implementation Priority**: High - Transform CLAUDE.md from static reference to dynamic context engine for maximum development efficiency.