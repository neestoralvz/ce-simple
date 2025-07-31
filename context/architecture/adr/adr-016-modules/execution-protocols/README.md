# Execution Protocols - Subagent Level Authority

**30/07/2025 17:15 CDMX** | Subagent execution capabilities and direct implementation protocols

## AUTORIDAD SUPREMA
@context/architecture/adr/ADR-016-hybrid-orchestration-execution-protocol.md → execution-protocols/ implements execution level per ADR-016 authority

## NIVEL EJECUTOR (Subagentes)

### **Capacidades Técnicas**
- ❌ NO pueden usar Task tools
- ❌ NO pueden orquestar otros subagentes
- ✅ Pueden usar herramientas de ejecución: Read, Edit, Bash, Grep, Glob
- ✅ Pueden hacer análisis técnico específico
- ✅ Pueden implementar cambios focalizados

### **Responsabilidades Permitidas**
- Ejecución directa de subtareas dentro de scope delegado
- Análisis técnico puntual y específico
- Implementación focalizda en componentes específicos
- Validación técnica de cambios implementados
- Testing y verificación de funcionalidad específica

## DELEGACIÓN CON AUTONOMÍA

### **Criterios para Delegación con Autonomía**
```
CUANDO delegar con autonomía de ejecución:
- Scope claramente definido y focalizdo
- Parámetros de calidad pre-establecidos
- No requiere decisiones arquitectónicas
- Información necesaria disponible en codebase
- Cambios no afectan múltiples componentes

INSTRUCCIONES DE DELEGACIÓN:
"Ejecuta [tarea específica] con autonomía completa dentro del scope [definición clara]. 
Usa herramientas de ejecución directa según necesites. 
Valida [criterios específicos] antes de reportar completado."
```

## PROTOCOLO NIVEL EJECUTOR

### **Instrucciones Operacionales para Subagentes**
```
NIVEL EJECUTOR (Subagentes):
6d. EJECUTA DIRECTAMENTE subtareas específicas dentro de scope delegado
6e. USA herramientas implementación (Read/Edit/Bash/Grep/Glob) según necesario
6f. VALIDA criterios específicos antes de reportar completado
```

### **Herramientas de Ejecución Autorizadas**
- **Read**: Análisis de codebase y documentación
- **Edit**: Implementación de cambios específicos
- **Bash**: Ejecución de comandos y testing
- **Grep**: Búsqueda y análisis de patrones
- **Glob**: Navegación y descubrimiento de archivos

---

**EXECUTION PROTOCOLS DECLARATION**: This module implements direct execution capabilities for subagents enabling autonomous implementation within clearly defined scope per ADR-016 authority.