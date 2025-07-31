# Hybrid Coordination - Decision Matrix Authority

**30/07/2025 17:15 CDMX** | Intelligent coordination between orchestration and execution levels

## AUTORIDAD SUPREMA
@context/architecture/adr/ADR-016-hybrid-orchestration-execution-protocol.md → hybrid-coordination/ implements coordination logic per ADR-016 authority

## MATRIZ DE DECISIÓN ORQUESTACIÓN VS EJECUCIÓN

### **Decision Matrix Framework**
| Criterio | Orquestación Obligatoria | Ejecución Directa Permitida |
|----------|-------------------------|----------------------------|
| **Scope** | Multi-componente, sistema-wide, afecta múltiples archivos | Componente específico, archivo único, cambio focalizdo |
| **Complejidad** | Requiere research paralelo, decisiones arquitectónicas | Análisis técnico directo, implementación específica |
| **Impacto** | Cambios estructurales, nuevas features, refactoring mayor | Bug fixes, optimizaciones puntuales, validación técnica |
| **Research** | WebSearch + MCP Context7 necesarios | Información contenida en codebase existente |
| **Coordinación** | Múltiples especialistas requeridos | Expertise único suficiente |
| **Stakeholder** | Validación usuario requerida | Dentro de parámetros pre-aprobados |

## PROTOCOLO DE TRANSICIÓN INTELIGENTE

### **Problema Identificado (Contexto)**
**Conflicto Técnico Fundamental**:
- **Protocolo Actual**: "ORQUESTA EXCLUSIVAMENTE a través de Task tools - NUNCA ejecutes directamente"
- **Realidad Técnica**: Los subagentes NO pueden usar Task tools
- **Resultado**: Bloqueo operacional cuando se delegan tareas que requieren subtareas

### **Casos Problemáticos Documentados**
1. **Análisis Complejo**: Orquestador delega "analizar codebase" → Subagente necesita leer múltiples archivos pero no puede orquestar
2. **Implementación Feature**: Orquestador delega "implementar funcionalidad" → Subagente necesita research pero no puede usar Task tools  
3. **Validación Calidad**: Orquestador delega "validar estándares" → Subagente necesita ejecutar tests pero protocolo prohíbe ejecución directa

## BENEFICIOS DE ARQUITECTURA HÍBRIDA

### **Beneficios Técnicos**
- **Elimina Bloqueos Operacionales**: Subagentes pueden ejecutar subtareas sin re-orquestación
- **Optimiza Eficiencia**: Ejecución directa para tareas apropiadas
- **Mantiene Calidad Sistemática**: Orquestación obligatoria donde es necesaria
- **Aprovecha Capacidades**: Cada nivel opera según sus capacidades técnicas

### **Beneficios de Proceso**
- **Flexibilidad Inteligente**: Protocolo se adapta a complejidad real de la tarea
- **Reducción Overhead**: Menos orquestación innecesaria para tareas simples
- **Escalabilidad**: Sistema funciona eficientemente a cualquier nivel de complejidad
- **Claridad Operacional**: Criterios específicos para decisiones de nivel

---

**HYBRID COORDINATION DECLARATION**: This module implements intelligent coordination logic enabling efficient task delegation while preserving systematic excellence per ADR-016 authority.