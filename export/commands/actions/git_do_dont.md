# /actions:git - Git Repository Manager

## DO
- Analizar todos archivos modificados/nuevos/eliminados antes de commit
- Agrupar cambios por tipo y detectar comandos que los generaron
- **Para análisis complejo**: EXECUTE /methodology:thinkx4 para commit message generation
- Crear mensajes descriptivos que cuenten historia real del trabajo

## DON'T
- Hacer commits sin analizar contexto de cambios
- Skip validación de estado repositorio antes y después
- Crear mensajes genéricos que no reflejen trabajo real
- Comprometer integridad sistema por conveniencia

## Context
- Git status y diff analysis para change detection
- Session context para understanding trabajo realizado
- System state validation protocols
- Claude Code attribution requirements

## Next Action
- **Automatic**: /workflows:close (después de session-ending commits)
- **Recommended**: /maintenance:validate (para repository health verification)
- **Context**: Continue workflow vs prepare handoff based on commit type
