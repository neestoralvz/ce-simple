# Command Creation - Complete Development Framework

## Purpose
Systematic methodology for creating self-contained slash commands with single responsibility principle, optimized for parallel orchestration through Task Tool deployment.

## Core Principles
- **Foundation**: Interview-Driven Development with intelligent task orchestration  
- **Single Responsibility**: One primary purpose from 12-type taxonomy with clear boundaries
- **Progressive Disclosure**: Main document + detailed implementation files for complex specifications
- **Self-Containment**: 100% embedded requirements, no external dependencies

## Command Taxonomy (12 Types)

### Discovery & Analysis
1. **Exploration**: Internal codebase analysis through Task Tool orchestration
2. **Search**: External research via WebSearch coordination  
3. **Discovery**: Combined exploration + search + dynamic questioning
4. **Analysis**: Deep synthesis and pattern recognition

### Workflow & Planning
5. **Planning**: Strategy development and workflow design
6. **Mathematical**: Embedded algorithms with 4-decimal precision calculations
7. **Maintenance**: System-wide operations and health monitoring
8. **Git**: Version control workflow management

### Development & Meta
9. **Modular**: Core system information containers
10. **Specialized Execution**: Domain-specific task automation
11. **Documentation**: Knowledge capture and organization
12. **Meta**: Dynamic adaptation and self-modification

## Execution Mechanisms (3 Types)

### Agent Orchestrators
**Pattern**: Deploy multiple Task Tools for parallel execution  
**Use**: Complex discovery, exploration, analysis requiring distributed processing  
**Trigger**: Complexity score ≥6.0 or scope breadth >3 domains

### Command Orchestrators  
**Pattern**: Sequential invocation of other slash commands  
**Use**: Multi-step workflows combining different command responsibilities  
**Application**: Refactoring god commands into single-purpose components

### Self-Contained Executors
**Pattern**: Direct tool usage without orchestration  
**Use**: Single-purpose tasks with embedded implementation  
**Application**: Mathematical calculations, simple maintenance operations

## Implementation Patterns

### Task Tool Orchestration
```markdown
Deploy Task Tools for [specific purpose]:
- Agent A: [specific responsibility and tool usage]
- Agent B: [specific responsibility and tool usage]
- Agent N: [specific responsibility and tool usage]

Coordinate through TodoWrite updates and result synthesis
Trigger: [complexity threshold or scope criteria]
```

### Mathematical Calculations
```bash
# Embedded calculation with 4-decimal precision
calculate_complexity() {
    local scope=$1 breadth=$2 interdep=$3
    complexity=$(echo "scale=4; ($scope + $breadth + $interdep) / 3" | bc)
    
    if (( $(echo "$complexity > 7.0000" | bc -l) )); then
        echo "high"
    elif (( $(echo "$complexity > 4.0000" | bc -l) )); then
        echo "medium"  
    else
        echo "low"
    fi
}
```

### TodoWrite Integration
Update TodoWrite at key points:
1. **Command Start**: Mark primary responsibility as in_progress
2. **Phase Transitions**: Complete current phase, start next
3. **Error Handling**: Add error resolution tasks when needed
4. **Command Completion**: Mark all tasks completed, add follow-ups

## Creation Process (4 Phases)

### Phase 1: Type Selection & Design
- Choose primary type from 12-type taxonomy
- Define single responsibility scope
- Select execution mechanism (agent/command/self-contained)
- Design tool usage pattern

### Phase 2: Implementation
- Apply type-specific patterns from pattern library
- Embed technical requirements with natural language instructions
- Implement parallel optimization where applicable
- Add TodoWrite behavioral reinforcement

### Phase 3: Standards Compliance
- Verify ≤150 lines main command
- Ensure ≤15 words per instruction
- Extract technical details to separate `-implementation.md` files
- Validate complete self-containment

### Phase 4: Quality Validation
- Test executability and completeness
- Verify type-specific characteristics
- Validate orchestration patterns
- Confirm error handling coverage

## Quality Standards

### Technical Requirements
- **Size**: ≤150 lines main command
- **Instructions**: ≤15 words each, natural language only
- **Self-Containment**: 100% embedded requirements, no external dependencies
- **Parallelization**: ≥70% operations parallel where applicable

### Behavioral Standards
- **TodoWrite Integration**: 3-4 updates per command for progress tracking
- **Error Handling**: Explicit recovery strategies for all failure modes
- **Progressive Disclosure**: Main command + detailed implementation files
- **Dynamic Questioning**: Built-in clarification protocols when needed

## Single Responsibility Enforcement

### Violation Indicators
- Multiple types within single command
- Sequential unrelated operations
- Embedded sub-responsibilities
- Complex branching logic

### Separation Strategy
1. **Identify Responsibilities**: Map current command to multiple taxonomy types
2. **Extract Single-Purpose Commands**: Create specific commands for each responsibility
3. **Convert to Orchestrator**: Transform original to command orchestrator
4. **Validate Independence**: Ensure each new command is self-contained

## Error Handling Framework

### Quality Check Pattern
```markdown
Execute [primary operation]
Validate results using [specific criteria]

If validation fails:
- Document failure mode in TodoWrite
- Implement recovery strategy: [specific approach]
- Retry original operation with modifications
- Re-validate results
- If still failing: escalate to manual intervention
```

### Fallback Strategy
- **Primary approach**: [main method]
- **Secondary approach**: [alternative method] if primary fails
- **Tertiary approach**: [backup method] if secondary fails
- **Manual intervention**: Document failure context if all approaches fail

## Anti-Patterns & Solutions

### God Commands
**Problem**: Single command handling multiple responsibilities  
**Solution**: Decompose to single-purpose commands + orchestrator

### Hidden Dependencies
**Problem**: External setup requirements not embedded  
**Solution**: Self-contained design with embedded prerequisites

### Vague Instructions
**Problem**: Abstract concepts without executable details  
**Solution**: Specific tool calls with technical implementation

### Poor Orchestration
**Problem**: Sequential execution when parallel possible  
**Solution**: Task Tool batching and competitive redundancy

## System Integration

### Command Registry Maintenance
Maintain registry preventing duplication and ensuring single responsibility compliance across all commands.

### Cross-Reference Matrix
Map command relationships, dependencies, and orchestration patterns for system integrity.

### Evolution Protocol
Systematic approach for adapting existing commands to methodology standards through refactoring phases.

---

**Single Responsibility**: Complete command creation framework ensuring systematic development of self-contained, optimized slash commands with embedded quality standards and behavioral reinforcement.