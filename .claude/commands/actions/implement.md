# /implement - Implementación Sistemática con Thinking 4x

Ejecuta implementación sistemática de funcionalidades siguiendo la metodología think x4, priorizando herramientas paralelas y despliegue de subagentes especializados.

## Metodología Think x4:
1. **Think 1**: Análisis inicial y comprensión del requerimiento
2. **Think 2**: Planificación detallada y identificación de dependencias  
3. **Think 3**: Estrategia de implementación y selección de herramientas
4. **Think 4**: Validación del plan y verificación de completitud

## Principios de implementación:
- **Exploración primero**: Siempre explorar codebase antes de actuar
- **Herramientas paralelas**: Maximizar uso de llamadas paralelas
- **Subagentes especializados**: Delegar tareas complejas a Task tool
- **Validación continua**: Verificar cada paso del proceso
- **Repetición hasta éxito**: Si falla, reiniciar proceso hasta lograr éxito

## Proceso:
1. **Exploración**: Comprender contexto actual usando /explore
2. **Planificación**: Crear todos con TodoWrite para tracking
3. **Investigación**: Usar /research si se necesita información externa
4. **Desarrollo**: Implementar usando herramientas apropiadas
5. **Validación**: Usar /validate para verificar calidad
6. **Documentación**: Usar /context para capturar aprendizajes

## Herramientas especializadas:
- Task tool para delegación a subagentes
- Llamadas paralelas (Read, Grep, LS simultáneos)
- MultiEdit para cambios múltiples en archivos
- TodoWrite para tracking de progreso

## Criterios de éxito:
- Funcionalidad completamente implementada
- Cumplimiento de estándares de calidad
- Documentación actualizada
- Validación técnica exitosa
- Sin regression en funcionalidad existente