---
contextflow:
  purpose: "Sistema completo de destilación progresiva de 5 capas: Raw Conversations → Consolidated Vision"
  triggers: ["contenido acumulado", "destilación completa requerida", "consolidated vision update"]
  next: ["session-close"]
  decision-tree:
    use-when: 
      - "Múltiples conversaciones raw sin procesar requieren destilación completa"
      - "Necesidad de actualizar consolidated_vision.md con nuevo contenido"
      - "Procesamiento sistemático Layer 0 → Layer 4 requerido"
    alternatives: ["extract-insights", "process-layer"]
    load-context: ["raw conversations", "existing layers", "user_vision system"]
  research-driven: false
---

# Comando `/distill-5-layers`

## Propósito Core
Sistema completo de destilación progresiva transformando conversaciones raw en visión consolidada definitiva a través de 5 capas especializadas.

## Arquitectura de 5 Capas
```
Layer 0: Raw Conversations (44+ archivos existentes)
    ↓ Content Mining Expert
Layer 1: Quotes Importantes (preservación voz usuario)
    ↓ Relationship Analyst  
Layer 2: Relationships & Patterns (conexiones conceptuales)
    ↓ Documentation Architect
Layer 3: Documentación Estandarizada (implementación práctica)
    ↓ Vision Synthesizer
Layer 4: Consolidated Vision (fuente de verdad definitiva)
```

## Orquestación Automática

### Fase 1: Content Mining Expert
**Deploy**: Specialist para extracción de quotes importantes
**Source**: `/narratives/raw/conversations/` (todas las conversaciones)
**Target**: Extraer 25-30 quotes clave categorizadas
**Output**: Layer 1 quotes con 100% preservación voz usuario

### Fase 2: Relationship Analyst  
**Deploy**: Specialist para mapeo de conexiones conceptuales
**Source**: Layer 1 quotes extraídas
**Target**: Crear patterns, evolution chains, decision maps
**Output**: Layer 2 relationships usando lenguaje usuario exclusivamente

### Fase 3: Documentation Architect
**Deploy**: Specialist para documentación estandarizada
**Source**: Layer 2 relationships + Layer 1 quotes
**Target**: 5 documentos formales (methodology, architecture, implementation, quality, evolution)
**Output**: Layer 3 documentation en `/documentation/` optimizada para tokens

### Fase 4: Vision Synthesizer
**Deploy**: Specialist para consolidación final
**Source**: Todas las capas anteriores + `/user_vision/` existente
**Target**: Síntesis definitiva en documento único
**Output**: `/user_vision/consolidated_vision.md` actualizado (fuente de verdad suprema)

## Execution Strategy
**OBLIGATORIO**: Orquestación via Task tools - 4 specialists secuenciales con coordination

### Success Criteria Globales
- [ ] Voice preservation ≥95% mantenida en todas las capas
- [ ] Trazabilidad completa Layer 0 → Layer 4
- [ ] Consolidated vision actualizada como single source of truth
- [ ] Zero contamination AI - solo insights derivados de usuario
- [ ] Integration seamless con user_vision/ authority hierarchy

## Workflow Automático
1. **Auto-scan** conversations sin procesar en `/narratives/raw/`
2. **Sequential deployment** de 4 specialists especializados
3. **Progressive synthesis** preservando voz original
4. **Final consolidation** en `/user_vision/consolidated_vision.md`
5. **Validation** de voice preservation y traceability

---

**Extensions**:
- [Specialist coordination protocols](./extensions/distill-5-layers-coordination.md)
- [Voice preservation validation](./extensions/distill-5-layers-validation.md)