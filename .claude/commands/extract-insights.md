---
contextflow:
  purpose: "Extracción orgánica de insights desde conversaciones raw hacia synthesis"
  triggers: ["acumulación de conversaciones", "patterns detectados", "processing layer requerido"]
  next: ["process-layer", "docs-sync"]
  decision-tree:
    use-when: 
      - "Múltiples conversaciones sin procesar en /narratives/raw/conversations/"
      - "Necesidad de consolidar insights antes de estructuración formal"
      - "Detección de patterns emergentes que requieren synthesis"
    alternatives: ["process-layer", "analyze"]
    load-context: ["raw conversations pool", "existing synthesis files"]
---

# Comando `/extract-insights`

## Propósito Core
Procesar conversaciones raw preservando voz original del usuario mientras extrae patterns, decisiones, y metodologías emergentes hacia synthesis orgánica.

## Pipeline de Extracción

### 1. Auto-Scan + Selection
**Target Sources**: 
- `/narratives/raw/conversations/` - Raw conversation files
- Timestamp-based filtering for recent conversations
- Unprocessed conversations identification

**Criterios automáticos**:
- Conversaciones sin synthesis correspondiente
- Timestamp reciente (últimas 2 semanas default)
- Conversations con decisions/insights marcados

### 2. Semantic Analysis + Extraction
**Auto-detect via subagent orchestration**:
- **Decisions crystallized**: Decisiones explícitas usuario
- **Methodological insights**: Refinamientos proceso  
- **Architectural patterns**: Cambios estructura sistema
- **User preferences**: Patterns comportamiento emergentes
- **Gaps identificados**: Funcionalidades faltantes

### 3. Synthesis Orgánica Structure
```markdown
# Synthesis: [Tema-Principal-Detectado]

## Voz Original Usuario - Insights Clave
"[citas exactas decisiones importantes]"
"[citas exactas insights metodológicos]"

## Patterns Emergentes
- **Pattern 1**: [descripción + contexto conversacional]

## Decisiones Crystallized  
- **Decisión A**: [qué decidió] → [implicaciones]

## Próximas Iteraciones
- [acción basada en insights]
```

### 4. Anti-Duplication + Cross-Reference
- Comparar con synthesis existentes → Consolidar
- Conectar con decisiones previas → Consistency
- Mapear evolution of thinking → Traceability

## Execution Strategy
**SIEMPRE via subagent orchestration** - usar Task tools para analysis + extraction + consolidation.

## Success Criteria
- [ ] Voz original preservada en citas exactas
- [ ] Patterns identificados con evidencia conversacional
- [ ] No duplicación con synthesis existentes
- [ ] Trazabilidad completa a conversaciones source

---

**Extensions**:
- [Pipeline detallado + casos edge](./extensions/extract-insights-details.md)
- [Pattern recognition algorithms](./extensions/extract-insights-patterns.md)