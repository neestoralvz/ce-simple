# ADR-020: TodoWrite Mandatory Task Initiation Protocol

**30/07/2025 16:45 CDMX** | Systematic TodoWrite integration as first step of all operational protocols

## Status
ACCEPTED - Implemented in CLAUDE.md operational instructions

## Context
User explicitly mandated that TodoWrite task planning must be integrated into the operational instructions of CLAUDE.md from the beginning, ensuring all tasks are loaded into TodoWrite before any other action.

## Problem Statement
Previous TodoWrite implementation was optional and mentioned only in specific contexts (orchestration and subagent inheritance), leading to inconsistent task management and potential oversight in comprehensive task tracking.

## Decision
Integrate TodoWrite as OBLIGATORIO (mandatory) first step in ALL operational protocols:

1. **Primary Protocol Integration**: Added as step 1 in NIVEL ORQUESTADOR protocol
2. **Orchestration Enhancement**: Strengthened from optional to mandatory in protocol continuation
3. **Subagent Inheritance**: Updated from "cuando aplicable" to "OBLIGATORIO - SIEMPRE activar desde inicio"  
4. **Task Tools Template**: Added TodoWrite requirement to all subagent operational instructions

## Rationale
- **User Authority**: Direct operational mandate from user vision
- **Systematic Consistency**: Ensures comprehensive task tracking across all workflows
- **L4-Pure Orchestration Support**: Aligns with expert delegation methodology requiring systematic planning
- **Vision Alignment**: Supports conversation-first development through structured task management

## Implementation Details

### CLAUDE.md Changes Made:
```markdown
Line 17: "DESPLIEGA TodoWrite task planning OBLIGATORIO como PRIMER PASO de TODA tarea antes de cualquier otra acción"
Line 42: "USA TodoWrite OBLIGATORIO para planificar TODA orquestación y tareas complejas - DESPLIEGA desde inicio de conversación"
Line 95: "TodoWrite OBLIGATORIO para planificación de subtareas - SIEMPRE activar desde inicio"
Line 83: "DESPLIEGA TodoWrite OBLIGATORIO como primer paso + [operational instructions]"
```

### Authority Chain Validation:
- **Supreme Authority**: User explicit mandate → TRUTH_SOURCE.md → CLAUDE.md implementation
- **Methodology Integration**: Aligns with L4-Pure Orchestration methodology framework
- **Standards Compliance**: Maintains OBLIGATORIO/MANDATORIO enforcement language consistency

## Consequences

### Positive:
- **Systematic Task Management**: All tasks begin with comprehensive planning
- **Authority Compliance**: Implements user vision for systematic task tracking
- **Orchestration Optimization**: Supports expert delegation with proper task structure
- **Consistency**: Eliminates optional/inconsistent task management approaches

### Neutral:
- **Operational Change**: All future workflows must adapt to TodoWrite-first protocol
- **Template Updates**: All Task tools inherit TodoWrite requirement automatically

### Monitoring:
- **Compliance Validation**: Ensure all tasks follow TodoWrite-first protocol
- **Effectiveness Measurement**: Monitor impact on task completion and organization
- **User Satisfaction**: Validate that systematic task management improves outcomes

## Related ADRs
- ADR-016: Hybrid Orchestration Execution Protocol (TodoWrite supports orchestration framework)
- ADR-003: Pure Orchestrator Transformation (TodoWrite enables systematic expert delegation)

## Authority References
- **User Authority**: Direct operational mandate conversation 30/07/2025
- **TRUTH_SOURCE.md**: Context architecture dispatcher validation  
- **methodology.md**: L4-Pure Orchestration methodology integration
- **CLAUDE.md**: Operational protocol implementation

---

**ADR AUTHORITY**: User explicit mandate → systematic operational enhancement → authority-compliant implementation per TRUTH_SOURCE.md validation protocols.