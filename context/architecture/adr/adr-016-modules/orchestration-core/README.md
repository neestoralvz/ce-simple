# Orchestration Core - Orquestador Level Authority

**30/07/2025 17:15 CDMX** | Core orchestration responsibilities and technical capabilities

## AUTORIDAD SUPREMA
@context/architecture/adr/ADR-016-hybrid-orchestration-execution-protocol.md → orchestration-core/ implements orchestration level per ADR-016 authority

## NIVEL ORQUESTADOR (Claude Principal)

### **Capacidades Técnicas**
- ✅ Puede usar Task tools
- ✅ Puede coordinar múltiples subagentes paralelos
- ✅ Puede tomar decisiones arquitectónicas
- ✅ Tiene acceso a WebSearch + MCP Context7
- ✅ Puede gestionar TodoWrite para planificación general

### **Responsabilidades Obligatorias**
- Orquestación sistemática para tareas multi-componente
- Coordinación de research paralelo
- Decisiones arquitectónicas y de diseño
- Planificación y validación general de calidad
- Gestión de scope y alineación con requisitos

## EVALUACIÓN INICIAL PROTOCOL

### **Evaluación Inicial (Orquestador)**
```
1. ANALIZA scope y complejidad de la solicitud
2. IDENTIFICA si requiere coordinación multi-componente
3. DETERMINA si necesita research paralelo externo
4. EVALÚA si involucra decisiones arquitectónicas
5. DECIDE: Orquestar vs Delegar con autonomía de ejecución
```

## ORQUESTACIÓN SISTEMÁTICA

### **Casos que Requieren Orquestación**
```
CUANDO mantener orquestación:
- Scope multi-componente o sistema-wide
- Requiere research externo (WebSearch + MCP Context7)
- Involucra decisiones arquitectónicas
- Necesita coordinación de múltiples especialistas
- Impacto en múltiples stakeholders o sistemas

PROCESO SISTEMÁTICO:
1. EXPLORA codebase completamente
2. INVESTIGA soluciones paralelas (WebSearch + MCP Context7)
3. COORDINA múltiples subagentes especializados
4. VALIDA con stakeholders antes de implementación
5. ORQUESTA ejecución con validación continua
```

## ACTUALIZACIÓN INSTRUCCIÓN OPERACIONAL

### **Protocolo Híbrido de Orquestación Inteligente**
```
NIVEL ORQUESTADOR (Claude Principal):
6a. ORQUESTA OBLIGATORIAMENTE tareas multi-componente, research paralelo, decisiones arquitectónicas
6b. EVALÚA scope/complejidad antes de decidir nivel de delegación
6c. DELEGA con autonomía ejecutora para subtareas específicas y focalizadas
```

---

**ORCHESTRATION CORE DECLARATION**: This module implements core orchestration capabilities and responsibilities preserving systematic excellence for complex multi-component tasks per ADR-016 authority.