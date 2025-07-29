# Decisión: Metodología Compactación Conversaciones

**29/07/2025 10:30 CDMX** | Conversation compacting methodology

## Proceso Compactación Identificado

### Metodología 5-Stage Process

**1. Identificar núcleos temáticos principales**
- Mapear threads conversacionales dominantes
- Agrupar intercambios relacionados por tema
- Priorizar según impacto decisional y técnico

**2. Extraer quotes exactas usuario**
- Preservar voz auténtica usuario con fidelidad máxima
- Identificar declaraciones de autoridad y principios
- Capturar decisiones cristalizadas sin interpretación

**3. Mapear decisiones técnicas tomadas**
- Documentar cambios arquitecturales y rationale
- Identificar problemas resueltos y metodología aplicada
- Preservar context decisional para futura referencia

**4. Preservar contexto esencial sin redundancia**
- Eliminar repeticiones y confirmaciones innecesarias
- Mantener información crítica para comprensión
- Balance entre completitud y concisión

**5. Estructurar cronológicamente con agrupación temática**
- Mantener flow temporal de decisiones
- Agrupar temas relacionados para coherencia
- Preservar causalidad entre decisiones

## Criterios Calidad Compactación

### Signal vs Noise Ratio
**Preservar**:
- Quotes directas usuario con autoridad decisional
- Cambios arquitecturales con justificación técnica
- Problemas identificados y soluciones implementadas
- Context crítico para decisiones futuras

**Eliminar**:
- Confirmaciones repetitivas ("Sí", "Correcto", etc.)
- Exploraciones que no llegaron a decisión
- Redundancias entre intercambios similares
- Tangents que no afectaron resultado final

### Fidelidad User Voice
**OBLIGATORIO:** Mantener 95%+ fidelidad quotes usuario originales
**PROHIBIDO:** Parafrasear o interpretar declaraciones de autoridad
**REQUERIDO:** Preservar context decisional y rationale original

## Aplicación Futura

### Como Comando /actions:compact
**Función**: Análisis conversacional sistemático para destilación
**Input**: Conversación raw o session transcription
**Output**: Summary compacto con núcleos temáticos + decisions + quotes preservation
**Integration**: Con /workflows:distill para layer progression

### Template Output Structure
**Núcleos Temáticos**: Major themes con quotes supporting
**Decisiones Técnicas**: Changes implemented con rationale
**Authority Statements**: Direct user quotes con context
**Implementation Results**: What was built/changed/resolved
**Pending Items**: Unresolved issues para future sessions

---

## Enlaces → información complementaria
**Si necesitas destilación**: → .claude/commands/actions/workflows:distill.md
**Si requieres templates**: → context/templates/template_research.md
**Si necesitas authority**: → user-vision/TRUTH_SOURCE.md