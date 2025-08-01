# w-start - Discovery & Exploration Workflow

**31/07/2025 00:00 CDMX** | Automated discovery + exploration workflow

## Command Purpose
Execute discovery workflow (socratic dialogue) + exploration workflow (codebase investigation) automatically to gather complete context before planning.

**LOAD:** @context/architecture/core/methodology.md

## Execution Protocol

### Phase 1: Discovery Activation
**Authority**: @context/architecture/core/methodology.md
**Behavior**: Unlimited socratic dialogue for complete user context
**Method**: 
- Activate mayeutic questioning without token constraints
- Apply "no quiero que perdamos de vista el dialogo mayeutico" principle
- Continue until user intent crystallized completely
- Apply Think x4 analysis on gathered information
- Validate discovery completeness before proceeding

### Phase 2: Exploration Integration
**Authority**: @context/architecture/core/methodology.md
**Behavior**: Systematic codebase + context investigation
**Method**:
- **Parallel tools OBLIGATORIO**: Multiple searches simultaneously 
- Search existing codebase for relevant patterns/solutions
- Investigate context/ directory (contains ONLY historical user information)
- Identify gaps for enhanced questioning
- Generate better-informed questions based on technical exploration

### Phase 3: Integration Synthesis
**Method**:
- Discovery insights + Exploration findings → Enhanced understanding
- Gap identification → Additional targeted questions
- Complete context validation → Ready for planning phase
- Think x4 analysis on complete information gathered

## Task Tool Integration
**When to delegate**: If exploration requires >3 specialized searches or complex analysis
**Template**: Use @context/architecture/claude_code/orchestration_protocols.md templates
**Authority preservation**: All subagents must respect @context/architecture/core/truth-source.md

## Usage Pattern
```
w-start [user request description]
```

User describes their need → System executes discovery + exploration → Complete context achieved → Ready for `w-plan`

## Success Criteria
- **Complete user intent understanding** through mayeutic dialogue
- **Relevant codebase context identified** through systematic exploration  
- **Enhanced questions asked and answered** based on technical investigation
- **Foundation ready for planning phase** with complete information

## Integration Points
- **Input**: User request/need description
- **Process**: Discovery + Exploration + Synthesis
- **Output**: Complete context ready for `w-plan`
- **Next phase**: Transition to investigation + planning workflow