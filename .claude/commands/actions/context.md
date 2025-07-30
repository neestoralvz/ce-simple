# /context - Extracción y Documentación de Contexto (Optimizado)

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

## Performance Optimization Specifications:
### Cache Management:
- Mantener lista de archivos ya verificados en sesión actual
- Evitar re-lectura de archivos consultados en últimos 5 comandos
- Cache de patrones ya identificados para evitar re-análisis

### Resource Limits:
- **Máximo 5 archivos** de verificación por categoría
- **Máximo 2 nuevos archivos** creados por ejecución
- **Máximo 1000 líneas** de contenido procesado total
- **Timeout forzado** a los 8 minutos de ejecución

### Batch Processing Strategy:
- Procesar categorías en orden: `architecture` → `claude_code` → `data`
- Si 1 categoría falla, continuar con siguientes (no abort total)
- Reportar progreso cada 2 minutos de procesamiento

### Memory Management:
- Liberar contexto de análisis después de cada categoría
- No mantener historial completo en memoria
- Usar referencias a archivos vs contenido completo en memoria

## Protocolo Híbrido Integration (ADR-016 Compliance):
### Nivel Orquestador (Claude Principal):
1. **DESPLIEGA TodoWrite**: Planning obligatorio como PRIMER PASO antes de análisis
2. **ORQUESTA Task tools**: Delegar análisis de categorías específicas a subagentes especializados
3. **COORDINA batch operations**: Ejecutar análisis paralelo de múltiples categorías SIMULTÁNEAMENTE
4. **DELEGA validation**: Task tool validador para verificar scope y valor incremental
5. **CONSULTA usuario**: Si propone documentar cambios fuera de scope conversación actual

### Nivel Ejecutor (Subagentes especializados):
- **Subagente Análisis Técnico**: Procesar insights arquitecturales y patrones
- **Subagente Metodología**: Extraer workflows y estándares de desarrollo
- **Subagente Validación**: Verificar duplicación y valor incremental vs base existente

### Decision Matrix para Delegación:
- **ORQUESTA**: Si >3 categorías afectadas O >5 archivos para verificar
- **DELEGA directo**: Si 1-2 categorías específicas O <3 archivos verificación
- **EVALÚA scope**: Siempre verificar antes de decidir nivel delegación

## Anti-Recursión Protocol:
- **NUNCA** analizar conversaciones que ya contienen análisis `/context`
- **NUNCA** procesar outputs previos de comandos `/context`
- **SIEMPRE** verificar si el insight ya existe antes de documentar
- **LIMITAR** a insights de implementación técnica actual únicamente

## Execution Pattern:
```
/context → TodoWrite planning → Task tools orchestration → Parallel analysis → Validation → Documentation → Archive completion
```