# Template System - Simple and Direct

**Updated**: 2025-07-26 | **Authority**: Template standards | **Navigation**: [System Hub](../README.md)  
**Vision**: [Command Philosophy](../vision/command-philosophy.md) | [Development Methodology](../vision/development-methodology.md)  
**Implementation**: [PTS Framework](../core/pts-framework.md) | [Development Standards](../rules/development-standards.md) | [Command Structure](../rules/command-structure-standard.md)

## Overview

The ce-simple template system provides essential templates for system components, emphasizing simplicity and direct implementation over complex composition frameworks.

## Available Templates

### Core Templates
- **command-template.md** - Standard command structure template
- **claude-md-template.md** - Four-section CLAUDE.md architecture template
- **claude-rules-template.md** - Partnership protocol template

### Documentation Templates  
- **foundation-command-patterns.md** - Common command patterns
- **three-layer-methodology-template.md** - Foundation/Implementation/Validation structure
- **cognitive-load-guidelines.md** - Information density optimization

### Context Economy Templates
- **context-economy-template.md** - File optimization using Context Economy Framework
- **system-rule-template.md** - System protocols and rules standardization

### Specialized Templates
- **architecture-decision-template.md** - Architecture Decision Records (ADRs)
- **methodology-template.md** - Methodology definition and documentation
- **framework-template.md** - Framework definition and component structure

## Template Standards

### Line Limits
- **Commands**: ≤80 lines maximum
- **Documentation**: ≤100 lines maximum  
- **CLAUDE.md**: ≤50 lines maximum
- **Concepts**: ≤50 lines for cognitive optimization

### Quality Requirements
- **PTS Compliance**: All templates must meet 12/12 PTS component validation
- **English Only**: Zero non-English content
- **Self-Contained**: No external dependencies
- **Single Responsibility**: Each template serves one specific purpose

## Usage Guidelines

### Command Templates
Use `command-template.md` as the base for all new commands. Follow the established pattern:
1. **Purpose** - Single sentence problem definition
2. **Principles** - PTS compliance specifications  
3. **Execution Process** - Phase-based implementation
4. **Error Handling** - Specific fallback procedures

### Documentation Templates
Follow three-layer architecture:
1. **Foundation** (≤50 lines) - Essential concepts
2. **Implementation** (≤100 lines) - Detailed procedures
3. **Validation** (≤100 lines) - Quality gates

### CLAUDE.md Templates
Use four-section architecture:
1. **Essential Context** - @ imports for immediate loading
2. **Conditional Instructions** - Task-based loading with READ syntax
3. **Context Navigation** - Directory references
4. **Practical Development** - Anthropic best practices integration

---

**Principle**: Simple, direct templates that eliminate complexity while maintaining functionality.