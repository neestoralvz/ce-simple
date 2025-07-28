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

## Propósito
Transformar synthesis orgánica (preservando voz original) en documentación formal optimizada para token economy y context loading eficiente.

## Pipeline de Estructuración

### 1. **Load Synthesis Orgánica**
```import
@/narratives/synthesis/[archivos-no-procesados]
```

**Criterios de selección**:
- Synthesis sin documentación formal correspondiente
- Insights que requieren estructuración para referencia eficiente
- Decisiones crystallized que necesitan formalización

### 2. **Análisis de Estructuración**

**Detectar automáticamente**:
- **Comandos nuevos**: Funcionalidades identificadas → `/claude/commands/`
- **Reglas arquitecturales**: Principios → `/rules/always/` o `/rules/when/`
- **Metodologías**: Processes refinados → `/docs/core/`
- **Patterns repetibles**: Templates → `/tools/templates/`
- **Decisiones formales**: ADRs → `/docs/decisions/`

### 3. **Optimización para Context Loading**

**Estructura optimizada**:
```markdown
---
context-metadata:
  source-synthesis: "[archivo-synthesis-origen]"
  user-voice-preserved: "[sección-con-citas-originales]"
  decision-tree:
    use-when: ["criterio-1", "criterio-2"]
    alternatives: ["opción-A", "opción-B"]
  load-context: ["@/archivo-relacionado-1", "@/archivo-relacionado-2"]
---

# [Título Estructurado]

## Esencia (Voz Original Preservada)
> "[cita exacta decisión usuario]"
> "[cita exacta insight usuario]"

## Estructuración Formal
[Contenido optimizado para token economy]

## Referencias Inteligentes
[Enlaces condicionales vs imports automáticos según contexto]
```

### 4. **Distribución por Tipo**

**Routing automático**:

#### → `/claude/commands/` 
**Si synthesis contiene**:
- Funcionalidad nueva identificada
- Workflow específico definido
- Process ejecutable validado

#### → `/rules/always/` o `/rules/when/`
**Si synthesis contiene**:
- Principio arquitectural decidido
- Constraint operacional definido
- Behavior pattern establecido

#### → `/docs/core/`
**Si synthesis contiene**:
- Metodología refinada
- Framework conceptual
- Guía de implementación

#### → `/tools/templates/`
**Si synthesis contiene**:
- Pattern repetible identificado
- Template structure validado
- Reusable component definido

## Execution Strategy

### 1. **Análisis Semántico de Synthesis**
```
PARA cada archivo en /narratives/synthesis/:
  - Identificar tipo de contenido principal
  - Detectar decisiones que requieren formalización  
  - Mapear a estructura de documentación apropiada
  - Preservar trazabilidad a voz original
```

### 2. **Context Optimization**
```
PARA cada documento a crear:
  - Definir árbol de decisiones (cuándo usar)
  - Identificar imports automáticos (@/) vs enlaces condicionales
  - Optimizar densidad de información
  - Mantener sección de voz original usuario
```

### 3. **Integration con Sistema Existente**
```
PARA cada nuevo documento:
  - Verificar no duplicación con contenido existente
  - Consolidar si overlap detectado
  - Actualizar imports/referencias en documentos relacionados
  - Update índices y navigation paths
```

## Output Format Examples

### Nuevo Comando Detectado:
```markdown
---
contextflow:
  purpose: "[propósito extraído de synthesis]"
  source-synthesis: "/narratives/synthesis/[archivo].md"
  user-decision: "[cita exacta decisión usuario]"
---

# Comando `/[nombre]`

## Voz Original Usuario
> "[cita exacta de lo que usuario pidió]"

## Implementación Optimizada
[Comando estructurado para token economy]
```

### Nueva Regla Arquitectural:
```markdown
---
source-synthesis: "/narratives/synthesis/[archivo].md"  
user-voice: "[cita decisión usuario]"
applies-when: ["contexto-1", "contexto-2"]
---

# [Nombre Regla]

## Decisión Original Usuario
> "[palabras exactas usuario sobre esta regla]"

## Formalización
[Regla estructurada y aplicable]
```

### Documentación Core:
```markdown
---
methodology-source: "/narratives/synthesis/[archivo].md"
user-insights: "[sección con citas usuario]"
---

# [Metodología/Framework]

## Insights Originales Usuario
> "[citas preservadas de conversación original]"

## Framework Estructurado
[Documentación optimizada manteniendo esencia]
```

## Criterios de Éxito

### Para Cada Procesamiento:
- [ ] Voz original usuario preservada en sección específica
- [ ] Contenido optimizado para token economy
- [ ] Árbol de decisiones definido para context loading
- [ ] Trazabilidad completa a synthesis origin
- [ ] No duplicación con documentación existente

### Calidad de Estructuración:
- [ ] Balance entre preservación y optimización
- [ ] Context loading eficiente implementado
- [ ] Routing correcto según tipo de contenido
- [ ] Integration seamless con sistema existente

## Integration con ContextFlow

### Pre-Processing:
- Validar que synthesis está lista para estructuración
- Identificar conflicts potenciales con documentación existente
- Planificar distribution strategy

### Durante Processing:
- Mantener links bidireccionales synthesis ↔ docs estructuradas
- Preserve decision context para future referencias
- Update system navigation y context loading

### Post-Processing:
- Update handoffs con nuevos documentos disponibles
- Trigger actualizaciones en comandos que referencien nuevo contenido
- Generate summary de cambios para próxima sesión

---

**Este comando completa el pipeline de procesamiento por capas - toma la riqueza orgánica de synthesis y la estructura para máxima utilidad práctica sin perder la fuente de verdad original.**