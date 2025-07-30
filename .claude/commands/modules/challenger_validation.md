# Challenger Validation Module

## Auto-Challenger Questions Template
Before creating any content, auto-pregúntate:
- **"¿Esto contradice la visión del usuario?"** → Si sí, RECHAZAR
- **"¿Es realmente necesario para implementación?"** → Si no, RECHAZAR  
- **"¿Agrega complejidad innecesaria?"** → Si sí, RECHAZAR
- **"¿Estoy inventando nueva filosofía?"** → Si sí, RECHAZAR
- **"¿Puedo justificar esto con citas de TRUTH_SOURCE.md?"** → Si no, RECHAZAR

## Anti-Deriva Protections
### Validación Pre-Expansión Obligatoria
1. **Verificar** que `/workflows:distill` fue ejecutado recientemente
2. **Confirmar** que CLAUDE.md esté actualizado con última visión
3. **Validar** que no hay conflictos pendientes con TRUTH_SOURCE.md
4. **Auto-rechazo** si no puede justificar alineación perfecta con visión existente

**Usage**: Standard validation protocol for expansion commands