# ContextFlow - ADRs

## ADR-001: Slash Commands Auto-Contenidos
**Estado**: Decidido  
**Decisión**: Comandos auto-contenidos con auto-sugerencia vs workflows centralizados

**Rationale**: 
- Token economy: Evita contexto sobrecargado
- Portabilidad: Reutilización entre proyectos  
- Escalabilidad: Nuevos comandos sin modificar base

**Template**:
```markdown
[Acción]: $ARGUMENTS
EXECUTE: [pasos]
OUTPUT: [formato específico]  
SUGGEST: [próximo comando]
```

---

## ADR-002: Prompt Engineering > Implementación Programática
**Estado**: Decidido  
**Decisión**: ContextFlow como sistema prompts sofisticado para LLMs

**Rationale**:
- Claude Code ejecuta prompts markdown, no código
- Vocabulario reforzado fuerza acciones específicas
- Token optimization crítico para costo-efectividad

**Implementación**: Comandos markdown con metadata para auto-sugerencia

---

## ADR-003: Metodología Socrática Concisa
**Estado**: Decidido  
**Decisión**: Preguntas estratégicas pero imperativas, no verbosas

**Rationale**:
- Extracción eficiente intención usuario
- Validación comprensión antes ejecución
- Token economy aplicada a conversación

**Pattern**: "¿Objetivo core?" vs "Me gustaría entender mejor qué intentas lograr..."

---

## ADR-004: Claude Code Exclusivo
**Estado**: Decidido  
**Decisión**: Diseño específico para Claude Code, no herramientas genéricas

**Rationale**:
- CLAUDE.md integración nativa
- Slash commands estructura específica
- MCP servers + hooks disponibles

**Consecuencia**: No portabilidad directa otras plataformas AI