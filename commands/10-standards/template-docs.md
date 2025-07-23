# Documentation Template - Progressive Disclosure

**Purpose**: Standard template for documentation following progressive disclosure principles

## Template Structure

```markdown
# Document Title - Concise Description

**Purpose**: Single line describing document function and scope

**Context**: Brief statement of when/why to use this document

## Overview

**Core Concept**: 1-2 sentences explaining the fundamental idea

**Key Benefits**:
- Benefit 1: specific value provided
- Benefit 2: specific value provided  
- Benefit 3: specific value provided

**Quick Start**: Immediate action reader can take

## Implementation

### Basic Approach
Step-by-step instructions for standard implementation:

1. **Step 1**: Action with clear outcome
2. **Step 2**: Action with clear outcome
3. **Step 3**: Action with clear outcome

### Advanced Features
Additional capabilities for complex scenarios:

**Feature 1**: Description with usage example
**Feature 2**: Description with usage example

## Reference

### Key Components
- Component 1: brief description
- Component 2: brief description

### Related Documents
- [Document 1](path): relationship description
- [Document 2](path): relationship description

**Detailed Implementation**: See [detailed-doc.md](path) for comprehensive guide
```

## Usage Examples

### Technical Documentation
```markdown
# Task Orchestration - Parallel Execution Patterns

**Purpose**: Guide for implementing parallel task execution in command workflows

**Context**: Use when designing commands that can benefit from concurrent operations

## Overview

**Core Concept**: Orchestrate multiple tasks simultaneously to achieve 3-5x performance gains

**Key Benefits**:
- Reduced execution time through parallelization
- Better resource utilization across operations
- Improved user experience with faster results

**Quick Start**: Add `orchestration: parallel` to command implementation
```

### Process Documentation  
```markdown
# Command Creation - Development Workflow

**Purpose**: Step-by-step process for creating new system commands

**Context**: Follow when adding new slash commands to the system

## Overview

**Core Concept**: Systematic approach ensuring consistency and quality standards

**Key Benefits**:
- Standardized command structure and behavior
- Reduced development time through templates
- Guaranteed integration with orchestration system

**Quick Start**: Copy template-command.md and customize for specific use case
```

## Guidelines

**Progressive Disclosure Principles**:
- Start with overview and quick start
- Layer details from general to specific
- Reference detailed documents for deep implementation
- Keep main content ≤200 lines

**Content Organization**:
- Overview: What and why (conceptual understanding)
- Implementation: How (practical application)  
- Reference: Where and when (supporting information)

**Writing Standards**:
- ≤15 words per instruction
- Natural language for clarity
- Absolute file paths for references
- Action-oriented headings

## Validation Checklist

- [ ] Document ≤200 lines
- [ ] Progressive disclosure structure used
- [ ] Overview provides conceptual understanding
- [ ] Implementation gives practical steps
- [ ] Reference section includes related documents
- [ ] Quick start enables immediate action
- [ ] Clear purpose statement included