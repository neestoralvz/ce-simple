# Shared Patterns - Modular Components for Command Excellence

**Last Updated: 2025-07-23**

## Overview

Extracted shared patterns from ce-simple commands to achieve excellent principle compliance through modular design. These patterns eliminate duplication while maintaining command independence and simplicity.

## Core Shared Patterns

### 1. TodoWrite Orchestration Pattern

**Purpose**: Standardized task tracking across all commands
**Principle Compliance**: DRY, Modular Design, Progressive Disclosure

```markdown
# Standard TodoWrite Pattern
Update TodoWrite: Mark "[Phase Name]" as in_progress
Execute [phase workflow]: [specific actions]
If [phase] failures occur:
  - Add TodoWrite task: "Resolve [error type]: [fallback strategy]"
  - Execute fallback: [specific fallback actions]
  - Continue with [degraded functionality] and [status reporting]
Update TodoWrite: Complete previous, mark "[Next Phase]" as in_progress
```

**Usage Examples**:
- `/init-project`: 5-phase orchestration with git, structure, docs, validation, routing
- `/start`: 3-phase analysis with assessment, guidance, routing  
- `/explore-codebase`: 5-phase exploration with discovery, analysis, validation, synthesis, handoff

### 2. Error Recovery and Fallback Pattern

**Purpose**: Graceful degradation with clear user guidance
**Principle Compliance**: Fail Fast, Graceful Degradation, Principle of Least Surprise

```markdown
# Standard Error Recovery Pattern
If [operation] failures occur:
  - Add TodoWrite task: "Resolve [error]: [specific fallback]"
  - Execute fallback: [degraded functionality description]
  - [Provide manual instructions/alternative paths]
  - Continue with [minimum viable functionality] and [clear status reporting]
```

**Variations**:
- **Permission Errors**: Fallback to manual instructions with step-by-step guidance
- **Tool Failures**: Alternative approaches with reduced functionality
- **Validation Errors**: Partial completion with clear remaining steps

### 3. Phase-Based Execution Pattern

**Purpose**: Structured workflow with clear boundaries
**Principle Compliance**: Separation of Concerns, Single Responsibility, Progressive Enhancement

```markdown
# Standard Phase Pattern
### Phase N: [Phase Name]
Update TodoWrite: Mark "[Phase Name]" as in_progress

Execute [phase type] workflow: [specific operations]
- [Primary operation 1] with [validation/safety measures]
- [Primary operation 2] with [error handling]
- [Primary operation 3] with [quality checks]

Use [Tool] to [accomplish phase goal]:
- [Tool operation] achieving [specific outcome]
- [Validation step] with [safety measure]

[Error handling block using Error Recovery Pattern]

Update TodoWrite: Complete previous, mark "[Next Phase]" as in_progress
```

### 4. Tool Integration Pattern

**Purpose**: Consistent tool usage with error handling
**Principle Compliance**: Convention over Configuration, Fail Fast, Information Hiding

```markdown
# Standard Tool Usage Pattern
Use [Tool] to [accomplish goal]:
- [Tool operation] achieving [specific measurable outcome]
- [Validation/safety measure] with [error detection]

# For complex operations requiring multiple tools
Execute [operation type] using [Primary Tool]:
- [Tool 1]: [Specific task with clear outcome]
- [Tool 2]: [Complementary task with validation]
- [Tool 3]: [Support task with error handling]
```

### 5. Context Reference Pattern

**Purpose**: Single source of truth integration
**Principle Compliance**: SSOT, DRY, Dependency Inversion

```markdown
# Standard Reference Pattern
@./docs/core/README.md
@./docs/core/system-principles.md

**Single Responsibility**: [Command-specific responsibility statement that references but doesn't duplicate system principles]
```

### 6. Command Routing Pattern

**Purpose**: Intelligent handoff between commands
**Principle Compliance**: Loose Coupling, Orthogonality, Progressive Enhancement

```markdown
# Standard Routing Pattern
Route to [related command category] based on [decision criteria]:
- Next: /[command-name] ([priority]) - [specific condition requiring this command]
- Next: /[command-name] ([priority]) - [alternative condition]
- [Continue with 3-5 routing options based on command complexity]

Generate [handoff type] context:
- [Context type 1] for [specific command category]
- [Context type 2] for [specific use case]
- [Quality/validation metrics] for [downstream validation]
```

## Pattern Usage Guidelines

### Implementation Checklist

**Before using patterns**:
- [ ] Identify which patterns apply to your command's workflow
- [ ] Customize pattern variables for your specific use case
- [ ] Ensure pattern usage aligns with command's single responsibility
- [ ] Verify patterns don't add unnecessary complexity (KISS principle)

**During implementation**:
- [ ] Use TodoWrite Pattern for all multi-phase commands
- [ ] Apply Error Recovery Pattern for all potential failure points
- [ ] Implement Phase-Based Pattern for structured workflows
- [ ] Follow Tool Integration Pattern for consistent tool usage
- [ ] Include Context Reference Pattern for authority alignment

**After implementation**:
- [ ] Verify all patterns contribute to principle compliance
- [ ] Ensure patterns don't create unnecessary coupling between commands
- [ ] Test fallback scenarios defined in Error Recovery Patterns
- [ ] Validate TodoWrite orchestration provides clear user visibility

### Pattern Customization Guidelines

**TodoWrite Orchestration**:
- Adapt phase names to match command's specific workflow
- Customize error types to reflect command's potential failure modes
- Adjust fallback strategies based on command's minimum viable functionality

**Error Recovery**:
- Define fallbacks that preserve command's core value proposition
- Provide manual alternatives that don't require technical expertise
- Ensure error messages guide users toward successful completion

**Phase-Based Execution**:
- Organize phases around natural workflow boundaries
- Ensure each phase has clear completion criteria
- Balance phase granularity with overall simplicity

**Tool Integration**:
- Select tools appropriate for command's specific needs
- Validate tool availability before use
- Provide clear success criteria for tool operations

**Context Reference**:
- Reference authoritative documents without duplicating content
- Ensure references remain accurate as system evolves
- Use references to support, not replace, command-specific guidance

**Command Routing**:
- Base routing decisions on objective criteria
- Provide multiple pathways for different user needs
- Preserve user choice while offering intelligent suggestions

## Quality Metrics

### Pattern Effectiveness Indicators

**DRY Compliance**: 
- Reduction in duplicated code across commands
- Consistent behavior patterns across similar operations
- Single definition of common workflows

**Modular Design Excellence**:
- Patterns can be used independently
- Clear interfaces between pattern components
- Reusable across different command types

**Progressive Enhancement**:
- Basic functionality works without advanced patterns
- Advanced patterns add value without complexity
- User can understand command behavior at appropriate detail level

### Success Measurements

**Command Independence**: Commands using shared patterns remain fully functional when other commands are unavailable

**Principle Compliance**: Shared patterns contribute positively to all 20 development principles

**User Experience**: Pattern usage creates predictable, reliable command behavior

**System Maintenance**: Pattern updates improve all consuming commands simultaneously

---

**Status**: Modular pattern extraction complete - ready for integration across all commands to achieve excellent principle compliance while maintaining simplicity and independence.