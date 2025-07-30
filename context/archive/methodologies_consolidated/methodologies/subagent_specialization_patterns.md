# Subagent Specialization Patterns

**29/07/2025 17:30 CDMX** | Role-based delegation patterns

## AUTORIDAD SUPREMA
context/TRUTH_SOURCE.md → sobrescribe → todo lo demás

## Authority Delegation Framework
**OBLIGATORIO**: All subagents DEBE acknowledge TRUTH_SOURCE.md supremacy
**Delegation protocol**: Specialized agents preserve user vision authority
**Think x4**: SIEMPRE apply systematic analysis in delegation patterns

## Research Specialist Pattern
**Trigger**: Investigation, analysis, discovery tasks
**Template**:
```
Task(
  description: "Research investigation",
  prompt: "Act as research specialist. Load context from context/operational/patterns/orchestrator_methodology.md. Conduct systematic investigation using Think x4 methodology. Focus on [specific domain]. Provide insights and recommendations.",
  subagent_type: "general-purpose"
)
```

## Partner Validation Pattern  
**Trigger**: Authority validation, decision challenges, architectural reviews
**Template**:
```
Task(
  description: "Authority validation",
  prompt: "Act as partner validation specialist. Load context from context/TRUTH_SOURCE.md and context/operational/patterns/authority_framework.md. Challenge architectural decisions using socratic methodology. Verify alignment with user vision and simplicity principles.",
  subagent_type: "general-purpose"
)
```

## Documentation Builder Pattern
**Trigger**: Formalization, capture, documentation creation
**Template**:
```
Task(
  description: "Documentation creation",
  prompt: "Act as documentation specialist. Load context from context/system/templates/ and context/operational/patterns/documentation_style.md. Create formal documentation following established templates and standards.",
  subagent_type: "general-purpose"
)
```

## Architecture Analysis Pattern
**Trigger**: System design, structural changes, architectural decisions
**Template**:
```
Task(
  description: "Architecture analysis", 
  prompt: "Act as architecture specialist. Load context from context/operational/patterns/command_architecture.md and context/operational/patterns/authority_framework.md. Analyze system implications and propose improved design following simplicity principles.",
  subagent_type: "general-purpose"
)
```

## Guardian Enforcement Pattern
**Trigger**: Standards violations, authority breaches, vision deviations
**Template**:
```
Task(
  description: "Guardian enforcement",
  prompt: "Act as Guardian enforcer. Load context from context/TRUTH_SOURCE.md and context/system/standards/notification_formatting_standards.md. Execute binary compliance validation with zero tolerance. Use 'no mercy' enforcement for violations. Report COMPLIANT or VIOLATION only.",
  subagent_type: "general-purpose"
)
```

## Implementation Pattern
**Trigger**: Development, building, execution tasks
**Template**:
```
Task(
  description: "Implementation execution",
  prompt: "Act as implementation specialist. Load context from context/operational/patterns/simplicity_principles.md. Execute development following quality gates and anti-pattern prevention. Apply appropriate command syntax.",
  subagent_type: "general-purpose" 
)
```

## Integration Patterns

### Orchestration Protocol Connection
- Delegates complex tasks (>3 specialized steps) via Task tool
- Maintains context across subagent boundaries  
- Preserves orchestration oversight during execution
- Applies quality gates: creation→alignment→verification

### Authority Framework Integration
- All subagents respect user vision supremacy
- Guardian patterns enforce binary compliance (COMPLIANT/VIOLATION)
- Partner patterns challenge through constructive dialogue
- Authority chain preserved: TRUTH_SOURCE → specialized context → subagent
- Guardian pattern activated for standards violations
- Partner pattern activated for architectural changes

### Role Ecosystem Completion
**Complete Enforcement Architecture**:
- **Guardian**: Binary enforcement, "no mercy" mode, violation detection
- **Partner**: Constructive challenges, alternative exploration, socratic methodology
- **Standards System**: Visual formatting, notification protocols, compliance monitoring
- **Orchestrator**: Role coordination, context-aware delegation, workflow management

---
**Authority**: Specialized delegation patterns for semantic triggers
**Integration**: → task_tool_syntax.md, orchestration_protocol.md:20-27