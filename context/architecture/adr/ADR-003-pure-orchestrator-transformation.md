# ADR-003: Pure Orchestrator Transformation

**Date**: 30/07/2025 17:30 CDMX  
**Status**: ACCEPTED  
**Authority**: @context/architecture/core/truth-source.md → architectural transformation per user vision

## Context
System initially designed with agent as both executor and coordinator. User feedback identified fundamental architectural flaw: agent should NEVER execute directly, only orchestrate specialized subagents.

## User Authority Statements
> "el rol de orquestado se debe de aplicar desde el inicio de las instrucciones como la base de todas sus acciones"

> "el agente principal no ejecuta solo delega a subagentes especializados utilizando tasktools y priorizando el uso paralelo"

> "debe de asegurarse de dar al agente el rol, contexto, y prompt adecuado para hacer sus tareas como un experto en la orquestacion de agentes de IA"

## Decision
**PURE ORCHESTRATOR TRANSFORMATION** with specialized subagent delegation.

### Architectural Changes

#### Pure Orchestrator Behavior
**ROL FUNDAMENTAL**: Director de orquesta puro - NUNCA ejecuta, SOLO coordina subagentes especializados  
**MÉTODO**: Coordinar múltiples subagentes especializados en PARALELO simultáneamente  
**OBJETIVO**: Multiplicar capacidades exponencialmente through intelligent orchestration

#### Expert Delegation Protocol
→ **Template Authority**: @context/architecture/claude_code/orchestration_protocols.md

**Template Obligatorio**:
```
description: [ESPECIALIZACIÓN] para [OBJETIVO] (3-5 palabras)
prompt: "ROL: [EXPERTISE] experto en [DOMINIO].
CONTEXTO: [CONTEXTO + @referencias].
INSTRUCCIONES: Think x4 + WebSearch + MCP context7 + validación.
TAREA: [OBJETIVO CON CRITERIOS]."
subagent_type: general-purpose
```

#### AI Agent Orchestration Expertise
**ANÁLISIS DE DEPENDENCIAS**: Evaluar interdependencias entre subagentes  
**OPTIMIZACIÓN PARALELO vs SECUENCIAL**: Determinar ejecución simultánea óptima  
**COORDINACIÓN DE RESULTADOS**: Integrar resultados interdependientes coherentemente  
**ESCALAMIENTO INTELIGENTE**: Aumentar subagentes según complejidad

#### User Notification Protocol
**Template**: "ORQUESTANDO: [X] subagentes paralelos → PROGRESO: [SUBAGENTE]: [ESTADO] → RESULTADO INTEGRADO: [SÍNTESIS]"

## Consequences

### Positive
- **Exponential Capability Multiplication**: N specialized subagents > 1 generalist agent
- **True Parallel Execution**: Multiple specialized tasks simultaneously
- **Expert Configuration**: Each subagent optimally configured for specific expertise
- **User Authority Compliance**: Perfect alignment with user vision

### Considerations
- **Coordination Complexity**: Managing multiple parallel subagents requires expertise
- **Communication Overhead**: More notification and coordination required

## Implementation References
→ CLAUDE.md (operational implementation)  
→ @context/architecture/core/methodology.md (orchestration methodology)  
→ @context/architecture/claude_code/orchestration_protocols.md (protocol authority)

---
**EVOLUTION**: Pure AI agent orchestration with expert director coordinating multiple specialized subagents in parallel execution per user explicit authority.