# q-context - Quick Context Extraction & Documentation

**31/07/2025 00:00 CDMX**

Analiza ÚNICAMENTE la conversación actual (no historial previo) y extrae contexto genuinamente nuevo para documentarlo en el directorio `/context` siguiendo la arquitectura factorizada del proyecto.

## Objetivos Optimizados:
- Identificar patrones, decisiones e insights ÚNICAMENTE de la sesión actual
- Categorizar información nueva según estructura organizacional
- Documentar solo si aporta valor incremental vs contexto existente
- Crear ADRs solo para decisiones arquitecturales genuinamente importantes
- Actualizar workflows únicamente si hay cambios materiales

## Criterios de Filtrado (OBLIGATORIOS):
### INCLUIR:
- Insights técnicos novedosos no documentados previamente
- Decisiones arquitecturales que afecten múltiples componentes
- Patrones emergentes identificados durante implementación
- Soluciones a problemas específicos no cubiertas en base existente

### EXCLUIR:
- Información ya documentada en /context/
- Conversaciones sobre navegación o consulta de archivos existentes
- Repetición de patrones ya establecidos
- Análisis de contexto previo (anti-recursión)

## Estructura de Documentación:
- `/context/architecture/` - Solo nuevas decisiones arquitecturales
- `/context/data/` - Solo nueva información empresarial/mercado
- `/@context/architecture/claude_code/` - Solo nuevas metodologías o insights de sesión
- `/context/handoffs/` - Solo si hay transferencia real de conocimiento

## Proceso Optimizado con Performance Constraints:
1. **OBLIGATORIO**: Usar TodoWrite para planificar análisis antes de ejecutar
2. **Scope Check**: Verificar que hay contenido genuinamente nuevo vs recursión
3. **Batch Processing**: Analizar máximo 3 categorías por ejecución
4. **Incremental Verification**: Solo verificar archivos relacionados al tema específico
5. **Timeout Constraint**: Completar en máximo 10 minutos de procesamiento
6. **Value Validation**: Documentar solo si aporta >20% valor incremental

## Anti-Recursión Protocol:
- **NUNCA** analizar conversaciones que ya contienen análisis `/context`
- **NUNCA** procesar outputs previos de comandos `/context`
- **SIEMPRE** verificar si el insight ya existe antes de documentar
- **LIMITAR** a insights de implementación técnica actual únicamente

## Execution Pattern:
```
q-context → TodoWrite planning → Task tools orchestration → Parallel analysis → Validation → Documentation → Archive completion
```