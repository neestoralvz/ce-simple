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
    load-context: ["@/narratives/raw/conversations/", "@/narratives/synthesis/"]
---

# Comando `/extract-insights`

## Propósito
Procesar conversaciones raw preservando voz original del usuario mientras extrae patterns, decisiones, y metodologías emergentes hacia synthesis orgánica.

## Pipeline de Extracción

### 1. **Scan Conversaciones Raw**
```import
@/narratives/raw/conversations/[últimas-N-conversaciones]
```

**Criterios de selección**:
- Conversaciones no procesadas (sin synthesis correspondiente)
- Timestamp reciente (últimas 2 semanas por defecto)
- Conversaciones marcadas para procesamiento

### 2. **Análisis Semántico Automático**

**Detectar automáticamente**:
- **Decisions crystallized**: Decisiones explícitas tomadas por usuario
- **Methodological insights**: Refinamientos de proceso o metodología
- **Architectural patterns**: Cambios o insights sobre estructura sistema
- **User preferences**: Patrones de comportamiento o preferencias emergentes
- **Gaps identificados**: Funcionalidades faltantes o necesidades detectadas

### 3. **Extracción Preservando Voz**

**Estructura de synthesis orgánica**:
```markdown
# Synthesis: [Tema-Principal-Detectado]

## Voz Original Usuario - Insights Clave
"[citas exactas con decisiones importantes]"
"[citas exactas con insights metodológicos]"
"[citas exactas con preferencias expresadas]"

## Patterns Emergentes Identificados
- **Pattern 1**: [descripción + contexto conversacional]
- **Pattern 2**: [descripción + evidencia en conversaciones]

## Decisiones Crystallized
- **Decisión A**: [qué se decidió] → [implicaciones]
- **Decisión B**: [qué se decidió] → [próximos pasos]

## Metodologías Refinadas
- **Refinamiento X**: [cambio metodológico detectado]
- **Approach Y**: [nuevo approach validado conversacionalmente]

## Gaps y Necesidades Identificadas
- **Gap 1**: [funcionalidad faltante] → [evidencia conversacional]
- **Necesidad 2**: [mejora requerida] → [contexto de origen]

## Próximas Iteraciones Sugeridas
- [acción 1 basada en insights]
- [acción 2 basada en patterns]
```

### 4. **Consolidación Inteligente**

**Evitar duplicación**:
- Comparar con synthesis existentes
- Consolidar insights similares
- Referenciar conversaciones específicas como fuente

**Cross-reference automático**:
- Conectar con decisiones previas
- Identificar evolución de thinking
- Mapear consistency vs cambios de dirección

## Execution Flow

### Input Analysis
1. **Scan `/narratives/raw/conversations/`** por archivos nuevos
2. **Identificar themes principales** via análisis semántico
3. **Agrupar conversaciones** por tema o proyecto relacionado

### Processing Strategy
1. **Una synthesis por tema principal** detectado
2. **Preservar voz exacta** del usuario en secciones clave  
3. **Extraer patterns** sin interpretación excesiva
4. **Mantener trazabilidad** a conversaciones específicas

### Output Generation
1. **Crear archivos** en `/narratives/synthesis/[tema-timestamp].md`
2. **Update index** de synthesis para navegación
3. **Generar summary** de insights extraídos para handoff

## Casos de Uso Principales

### Consolidación Periódica
**Trigger**: Acumulación de 5+ conversaciones sin procesar
**Output**: Synthesis orgánica consolidando insights principales

### Pre-Estructuración  
**Trigger**: Antes de `/process-layer` para documentación formal
**Output**: Material limpio preservando voz para estructuración

### Pattern Recognition
**Trigger**: Detección automática de themes repetidos
**Output**: Synthesis enfocada en patterns específicos identificados

## Criterios de Éxito

### Para Cada Ejecución:
- [ ] Voz original usuario preservada exactamente en citas
- [ ] Patterns identificados con evidencia conversacional clara
- [ ] Decisiones crystallized extraídas sin interpretación
- [ ] Trazabilidad completa a conversaciones fuente
- [ ] No duplicación con synthesis existentes

### Calidad de Synthesis:
- [ ] Balance entre preservación y consolidación
- [ ] Insights actionables identificados claramente
- [ ] Continuidad con synthesis previas mantenida
- [ ] Gaps y necesidades específicas documentadas

## Integration con Pipeline

### Pre-Requisitos:
- Conversaciones en `/narratives/raw/conversations/`
- Metadata de procesamiento (opcional)

### Post-Processing:
- Output disponible para `/process-layer`
- Index de synthesis actualizado
- Handoff summary generado

### Automation Triggers:
- Nuevas conversaciones detectadas automáticamente
- Threshold de conversaciones no procesadas alcanzado
- Request explícito de consolidación

---

**Este comando es el primer paso del pipeline de procesamiento por capas - extrae y preserva sin perder la esencia orgánica de las conversaciones originales.**