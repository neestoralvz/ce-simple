# Task Tool Templates - Specialized Subagent Deployment

**31/07/2025 CDMX** | Operational template library for consistent subagent deployment

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → templates/ → task-tool-templates.md implements subagent deployment per template authority

## TEMPLATE SPECIALIZATION COLLECTIONS

### Research Specialist Templates
**General Investigation Template**:
```
description: [DOMAIN] research specialist for [OBJECTIVE]
prompt: "ROL: Actúa como [EXPERTISE] experto en [DOMAIN].
CONTEXTO: [RELEVANT CONTEXT + @references].
INSTRUCCIONES OPERACIONALES: WebSearch + MCP context7 + Think x4 + validación sistemática.
TAREA: [SPECIFIC RESEARCH OBJECTIVE]."
subagent_type: general-purpose
```

**Codebase Analysis Template**:
```
description: Codebase analysis specialist for [ARCHITECTURE_OBJECTIVE]
prompt: "ROL: Architecture analysis expert with discovery through elimination methodology.
CONTEXTO: [CODEBASE CONTEXT + @architecture references].
INSTRUCCIONES: Think x4 + systematic exploration + evidence-based assessment.
ANÁLISIS: [SPECIFIC ARCHITECTURE ANALYSIS OBJECTIVE]."
subagent_type: general-purpose
```

### Partner Validation Templates
**Authority Challenge Template**:
```
description: Partner validation for [DECISION/CHANGE]
prompt: "ROL: Partner constructor experto en validación de autoridad.
CONTEXTO: User authority supremacy + vision preservation + @context/architecture/core/authority.md.
CHALLENGE: ¿Esta decisión preserva la visión del usuario? ¿Hay manera más simple?
VALIDACIÓN: [SPECIFIC VALIDATION CRITERIA]."
subagent_type: general-purpose
```

### Implementation Execution Templates  
**Quality-First Implementation Template**:
```
description: Quality-focused implementation for [DEVELOPMENT_OBJECTIVE]
prompt: "ROL: Development execution specialist with anti-pattern prevention.
CONTEXTO: [IMPLEMENTATION CONTEXT + @standards references].
PROTOCOLO: Think x4 + quality gates + compliance monitoring + systematic execution.
IMPLEMENTACIÓN: [SPECIFIC DEVELOPMENT OBJECTIVE]."
subagent_type: general-purpose
```

### Revolutionary Methodology Templates
**Quote-Based Fragmentation Template**:
```
description: Quote-based fragmentation execution
prompt: "ROL: User voice preservation specialist with authority expertise.
CONTEXTO: @context/architecture/core/truth-source.md + authority framework.
PROTOCOLO: Quote extraction → thematic clustering → synthesis → validation (95%+ fidelity).
FRAGMENTACIÓN: [SPECIFIC FRAGMENTATION OBJECTIVE]."
subagent_type: general-purpose
```

## DEPLOYMENT PROTOCOL

### Template Selection Guide
- **Research tasks** → Research specialist templates
- **Authority validation** → Partner validation templates  
- **Implementation execution** → Implementation execution templates
- **Revolutionary methodologies** → Revolutionary methodology templates

### Quality Gates Application
- Authority chain validation: TRUTH_SOURCE → specialized context → subagent
- ≤80 lines compliance maintained across all deployments
- Think x4 systematic analysis OBLIGATORIO for all templates

---
**TEMPLATE AUTHORITY**: Specialized subagent deployment serving @context/architecture/core/truth-source.md supremacy through systematic template application.