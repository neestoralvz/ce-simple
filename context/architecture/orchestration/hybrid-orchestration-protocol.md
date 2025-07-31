# Hybrid Orchestration Protocol - Intelligent Coordination Framework

**31/07/2025 14:30 CDMX** | Hybrid protocol with orchestrator and executor levels

## AUTORIDAD SUPREMA
@context/architecture/orchestration.md → hybrid-orchestration-protocol.md implements intelligent coordination per L4-Pure Orchestration authority

## PRINCIPIO FUNDAMENTAL
**"Two-level intelligent coordination maximizes capability multiplication"** - Strategic orchestrator level coordinates specialized executor level for exponential capability expansion.

## PROTOCOLO HÍBRIDO DE ORQUESTACIÓN INTELIGENTE

### Nivel Orquestador (Claude Principal) - CAPACIDADES
**Task tools, coordinación, WebSearch+MCP Context7**:

1. **DESPLIEGA TodoWrite task planning OBLIGATORIO** como PRIMER PASO de TODA tarea
2. **DESPLIEGA subagente especializado** para explorar codebase ANTES de cualquier acción
3. **ORQUESTA búsqueda paralela** de soluciones via múltiples Task tools SIMULTÁNEAMENTE
4. **DELEGA análisis Think x4** de información recopilada a subagente analítico
5. **COORDINA planificación** con múltiples subagentes especializados en PARALELO
6. **DELEGA validación de scope** - CONSULTA al usuario si propone cambios fuera scope

### Decisión Inteligente de Nivel (Matriz ADR-016)
- **ORQUESTA OBLIGATORIAMENTE**: tareas multi-componente, research paralelo, decisiones arquitectónicas
- **EVALÚA scope/complejidad** ANTES de decidir nivel de delegación
- **DELEGA con autonomía ejecutora**: subtareas específicas, análisis técnico puntual

### Nivel Ejecutor (Subagentes) - CAPACIDADES
**Read/Edit/Bash/Grep/Glob, análisis técnico**:
- **EJECUTA DIRECTAMENTE** subtareas específicas dentro de scope delegado
- **USA herramientas implementación** según necesario para completar objetivos
- **VALIDA criterios específicos** establecidos antes de reportar completado

## TEMPLATE OBLIGATORIO PARA TASK TOOLS
```
description: [ESPECIALIZACIÓN ESPECÍFICA] para [OBJETIVO TÉCNICO PRECISO] (3-5 palabras)
prompt: "ROL: Actúa como [EXPERTISE ESPECÍFICA] experto en [DOMINIO].
CONTEXTO: [CONTEXTO RELEVANTE COMPLETO + @referencias necesarias].
INSTRUCCIONES OPERACIONALES: DESPLIEGA TodoWrite OBLIGATORIO + Think x4 OBLIGATORIO + WebSearch + MCP context7 paralelo + herramientas paralelas + validación sistemática.
TAREA ESPECÍFICA: [OBJETIVO DETALLADO CON CRITERIOS DE ÉXITO]."
subagent_type: general-purpose
```

### Herencia Operacional Obligatoria para Subagentes
**CADA SUBAGENTE DEBE HEREDAR**:
- Protocolo Think x4 sistemático OBLIGATORIO
- WebSearch + MCP context7 búsqueda paralela SIEMPRE
- Uso de herramientas paralelas y batch operations
- Validación sistemática post-ejecución
- Compliance con estándares profesionales
- TodoWrite OBLIGATORIO para planificación de subtareas

---

**HYBRID PROTOCOL DECLARATION**: Two-level intelligent coordination framework implementing L4-Pure Orchestration through strategic orchestrator and specialized executor coordination.