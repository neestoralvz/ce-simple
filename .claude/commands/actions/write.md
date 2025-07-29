# Comando /write

**29/07/2025 09:00 CDMX | Actualizado: 29/07/2025 09:00 CDMX** | Acción escritura documentación

## Función Core
Crear documentación siguiendo estilo LLM-optimizado definido en context/patterns/documentation_style.md

## Context Import Automático
**DEBE consultar:** → context/patterns/documentation_style.md
**DEBE usar:** Templates apropiados según tipo documento
**OBLIGATORIO:** Aplicar regla regeneración 10%

## Execution
**SIEMPRE:**
1. Consultar estilo documentación
2. Identificar tipo documento (context/roles:research/command/decision)
3. Aplicar template correspondiente
4. Incluir header con fechas creación + actualización
5. Agregar footer enlaces condicionados
6. Validar referencias líneas exactas

## Tipos Documento
- **Context modules:** → principles/, patterns/, decisions/
- **Research:** → context/roles:research/
- **Commands:** → .claude/commands/categorías/
- **Decisions:** → context/decisions/

---
## Enlaces → Información Complementaria  
**Si necesitas estilo:** → context/patterns/documentation_style.md:1-50
**Si requieres estructura:** → context/organization.md:15-40