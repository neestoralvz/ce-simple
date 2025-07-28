---
contextflow:
  purpose: "Estructuración formal de synthesis orgánica hacia documentación optimizada"
  triggers: ["synthesis acumulada", "documentación formal requerida", "optimización estructura"]
  next: ["docs-sync", "refactor", "implement"]
  prev: ["extract-insights"]
  decision-tree:
    use-when: 
      - "Synthesis orgánica disponible en /narratives/synthesis/"
      - "Necesidad de documentación formal estructurada"
      - "Optimización de context loading y token economy"
    alternatives: ["docs-sync", "refactor"]
    load-context: ["@/narratives/synthesis/", "@/docs/", "@/rules/"]
---

# Comando `/process-layer`

## Propósito Core
Transformar synthesis orgánica (preservando voz original) en documentación formal optimizada para token economy y context loading eficiente.

## Pipeline Esencial

### 1. Load Synthesis → Análisis → Distribución
```import
@/narratives/synthesis/[archivos-no-procesados]
```

**Auto-detect content type** → Route to appropriate structure:
- Commands → `/claude/commands/`
- Rules → `/rules/always/` o `/rules/when/`  
- Methodologies → `/docs/core/`
- Templates → `/tools/templates/`

### 2. Context Optimization
```markdown
---
context-metadata:
  source-synthesis: "[archivo-origen]"
  user-voice-preserved: "[sección-citas]"
  decision-tree: {use-when, alternatives, load-context}
---

# [Título]

## User Voice Original
> "[cita exacta decision usuario]"

## Structured Content
[Optimizado token economy]
```

### 3. Integration + No-Duplication
- Verify vs existing docs
- Consolidate overlaps
- Update references/navigation
- Preserve traceability

## Workflow Execution
**SIEMPRE via subagent orchestration** - usar Task tools con especialistas apropiados.

## Success Criteria
- [ ] Synthesis transformed preservando user voice
- [ ] Token economy optimized (50-80 líneas core)
- [ ] No duplication con documentación existente
- [ ] Integration seamless con sistema

---

**Extensions disponibles**:
- [Pipeline detallado y casos edge](./extensions/process-layer-details.md)
- [Routing automático y examples](./extensions/process-layer-routing.md)
- [Integration protocols](./extensions/process-layer-integration.md)