# Command Structure Standard

## Overview

Standardized structure for all slash commands in ce-simple system based on enhanced-start pattern with granular, low-density instructions for maximum clarity and executability.

**Foundation**: Enhanced-start structure with 4-section organization  
**Density**: Low-density, granular instructions for easy execution  
**Tool Integration**: Explicit tool calls when necessary with specific usage patterns

## Required Structure

### Section 1: Purpose
**Content**: Single, clear statement of command's primary responsibility
**Format**: One paragraph defining what the command does
**Requirements**: 
- Maps to single taxonomy type from 12-type system
- Clear boundary definition
- No overlap with other command purposes

### Section 2: Principles and Guidelines
**Content**: Core principles governing command execution
**Format**: 4 key principles in bullet format
**Requirements**:
- Single Responsibility emphasis
- Granular approach specification  
- Dependency management approach
- Error handling philosophy

**Standard Template**:
```markdown
**Single Responsibility**: Focus exclusively on [primary responsibility] without [other areas]
**Granular [Approach]**: Break [process] into small, manageable [units]
**[Domain] Management**: Clear [domain-specific] dependencies with explicit [requirements]
**Error Recovery**: Built-in [failure type] handling and recovery protocols
```

### Section 3: Execution Process
**Content**: Phase-based execution with granular, low-density tasks
**Format**: 3-4 phases with specific TodoWrite integration and tool calls
**Requirements**:
- Each phase has clear completion criteria
- TodoWrite updates at every phase transition
- Specific tool calls with explicit parameters
- Granular tasks that are easy to follow
- Error handling integrated within phases

**Phase Template**:
```markdown
### Phase N: [Phase Name]
Update TodoWrite: Mark "[specific task description]" as in_progress

[First granular task]:
- [Specific action item 1]
- [Specific action item 2] 
- [Specific action item 3]
- [Specific action item 4]

[Tool usage when needed]:
Use [ToolName] to [specific action]:
- [Specific parameter/usage 1]
- [Specific parameter/usage 2]

[Second granular task group]:
- [Next specific action]
- [Validation step]
- [Documentation step]

### Error Handling (within phases)
If [specific condition occurs]:
- Add TodoWrite task: "[specific error resolution description]"
- [Specific recovery action]
- [Validation of recovery]
- [Continue/retry instruction]

Update TodoWrite: Complete previous, mark "[next phase]" as in_progress
```

### Section 4: Single Responsibility Statement (Footer)
**Content**: Reinforcement of single responsibility principle
**Format**: Standardized closing statement
**Template**: `**Single Responsibility**: [Primary type] focused exclusively on [specific responsibility] [without other areas].`

## Documentation Standards Integration

### Length Requirements
- **Total Command**: ≤150 lines maximum
- **Purpose Section**: 1 paragraph (3-5 lines)
- **Principles Section**: 4 bullet points (8-12 lines)
- **Execution Process**: 3-4 phases (120-130 lines)
- **Footer**: 1 line single responsibility statement

### Instruction Density
**Low-Density Requirement**: Each instruction should be:
- Single, specific action
- Easy to understand and execute
- No complex multi-part instructions
- Clear validation criteria
- Explicit tool usage when needed

**Granular Task Guidelines**:
- Break complex operations into 3-4 simple steps
- Each step has clear completion criteria
- Validation built into each step
- No assumptions about prior knowledge

### Tool Integration Standards
**Explicit Tool Calls**: When tools are needed, specify:
- Tool name and specific usage
- Required parameters
- Expected outcomes
- Validation of tool results

**TodoWrite Integration**: Required at:
- Phase start: Mark new phase as in_progress
- Phase completion: Complete current, mark next as in_progress
- Error conditions: Add specific error resolution tasks
- Command completion: Complete all tasks, add follow-ups

## Implementation Requirements

### All Commands Must:
1. **Follow 4-section structure exactly**
2. **Maintain ≤150 line limit**
3. **Use granular, low-density instructions**
4. **Integrate TodoWrite at every phase transition**
5. **Include explicit tool calls when needed**
6. **Have built-in error handling within phases**
7. **End with single responsibility statement**

### Quality Gates
**Structure Compliance**: All 4 sections present and properly formatted
**Density Compliance**: Instructions are granular and easy to follow
**Length Compliance**: ≤150 lines total
**Tool Integration**: Proper tool usage with explicit parameters
**Single Responsibility**: Clear focus on primary taxonomy type

### Validation Checklist
- [ ] Purpose section clearly defines single responsibility
- [ ] Principles section has 4 standardized guidelines
- [ ] Execution process has 3-4 phases with TodoWrite integration
- [ ] Instructions are granular and low-density
- [ ] Tool calls are explicit with specific usage
- [ ] Error handling integrated within phases
- [ ] Single responsibility footer statement present
- [ ] Total length ≤150 lines
- [ ] Command maps to single taxonomy type

## Migration Plan for Existing Commands

### Phase 1: Document Current State (27 commands)
Review all existing commands for structure compliance and identify required changes.

### Phase 2: Apply Structure Standard
Convert all commands to 4-section structure with granular instructions.

### Phase 3: Validate and Test
Ensure all commands meet structure standard and maintain functionality.

---

**This standard ensures consistent, executable, maintainable commands across the entire ce-simple system with maximum clarity and usability.**