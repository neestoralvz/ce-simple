# /session-close - Cierre y Captura de Conversación

Comando para cerrar una sesión conversacional y capturar la narrativa completa como fuente de verdad para el sistema de destilación.

## Funcionalidad

Este comando ejecuta el proceso completo de cierre de sesión:

1. **Captura la conversación completa** de la sesión actual
2. **Genera metadatos** de contexto y categorización
3. **Guarda la narrativa raw** en estructura organizada
4. **Prepara handoff** para próxima sesión
5. **Actualiza índices** y referencias

## Uso

```bash
/session-close
```

### Parámetros opcionales:
```bash
/session-close --tema "nombre-tema"           # Especifica tema principal
/session-close --categoria "tecnico|personal|planning"  # Categoriza tipo
/session-close --continue                     # Indica que habrá continuación
```

## Proceso de Ejecución

### Fase 1: Extracción de Conversación
- **Captura íntegra** de la conversación actual
- **Preserva formato** exacto de intercambios
- **Mantiene timestamps** implícitos por orden
- **Identifica participantes** (usuario vs Claude)

### Fase 2: Análisis de Metadatos
Usando Task tool para análisis paralelo:

**Identificación temática:**
- Tema principal de la conversación
- Subtemas y tangentes importantes
- Decisiones tomadas o diferidas
- Insights clave emergentes

**Categorización automática:**
- **Técnico**: Implementación, código, arquitectura
- **Estratégico**: Planes, visión, objetivos
- **Operacional**: Procesos, workflows, herramientas
- **Exploratorio**: Ideas, brainstorming, preguntas abiertas

**Extracción de entidades:**
- Proyectos mencionados
- Herramientas/tecnologías referenciadas
- Personas o roles involucrados
- Fechas y cronogramas
- Decisiones arquitectónicas (ADRs potenciales)

### Fase 3: Generación de Archivo Raw
Crea archivo en `/narratives/raw/conversations/` con formato:

```markdown
# Conversación: [Tema Principal]

## Metadatos
- **Fecha**: YYYY-MM-DD HH:MM (Ciudad de México)
- **Duración estimada**: [duración basada en contenido]
- **Tema principal**: [tema identificado]
- **Categoría**: [técnico|estratégico|operacional|exploratorio]
- **Estado**: [completa|para_continuar|interrumpida]
- **Proyectos relacionados**: [lista]
- **Tecnologías mencionadas**: [lista]

## Resumen Ejecutivo
[2-3 párrafos con esencia de la conversación]

## Decisiones Tomadas
- [decisión 1] → [contexto]
- [decisión 2] → [contexto]

## Decisiones Diferidas
- [decisión pendiente] → [por qué diferida] → [cuándo revisar]

## Insights Clave
- [insight 1] → [implicaciones]
- [insight 2] → [implicaciones]

## Próximos Pasos Identificados
- [acción 1] → [responsable] → [cuándo]
- [acción 2] → [responsable] → [cuándo]

## Referencias Cruzadas
- **Conversaciones relacionadas**: [archivos previos relevantes]
- **Documentos impactados**: [qué docs necesitan actualización]
- **Planes afectados**: [planes que requieren modificación]

---

## Transcripción Completa

[CONVERSACIÓN ÍNTEGRA - PRESERVANDO FORMATO EXACTO]

**Usuario**: [mensaje exacto]

**Claude**: [respuesta exacta]

[... conversación completa ...]

---

## Análisis Post-Conversación (Auto-generado)

### Evolución del Pensamiento
[Cómo evolucionaron las ideas durante la conversación]

### Patrones Identificados
[Patrones en preferencias usuario, métodos de resolución, etc.]

### Conexiones con Conversaciones Previas
[Enlaces semánticos con narrativas anteriores]

### Recomendaciones para Síntesis
[Qué partes son candidatas para síntesis/consolidación]
```

### Fase 4: Actualización de Índices
- **Actualiza** `/narratives/index/` con nueva conversación
- **Crea referencias cruzadas** con conversaciones relacionadas
- **Actualiza categorías** y tags temáticos
- **Identifica patterns** emergentes para síntesis futura

### Fase 5: Preparación de Handoff
Genera contexto condensado para próxima sesión:

```markdown
## Handoff Context para Próxima Sesión

### Estado Actual del Proyecto
[Situación después de esta conversación]

### Compromisos Pendientes
[Qué quedó de hacer o revisar]

### Contexto Crítico a Preservar
[Información esencial para continuidad]

### Próxima Conversación Sugerida
[Temas prioritarios para seguir]
```

## Automatización Inteligente

### Triggers de Cierre
- Usuario dice "terminamos", "hasta aquí", "handoff"
- Conversación excede 100 intercambios
- Se detecta shift mayor de tema
- Solicitud explícita de cierre

### Inteligencia de Contenido
- **Extrae decisiones** implícitas y explícitas
- **Identifica compromisos** del usuario
- **Detecta insights** que impactan documentación
- **Sugiere acciones** de seguimiento

### Validación Pre-Guardado
- **Confirma tema principal** identificado
- **Valida categorización** con usuario
- **Verifica próximos pasos** extraídos
- **Permite ajustes** antes de guardar

## Criterios de Éxito

### Para la Narrativa Raw
- **Preservación completa** de la conversación
- **Metadatos precisos** y útiles para búsqueda
- **Trazabilidad** hacia documentos impactados
- **Context suficiente** para retomar conversación

### Para el Sistema
- **Alimenta pipeline** de síntesis automáticamente
- **Mantiene continuidad** entre sesiones
- **Preserva voz original** sin interpretación
- **Facilita búsqueda** y recuperación posterior

## Salidas Generadas

```
/narratives/raw/conversations/
├── YYYY-MM-DD_HH-MM_[tema-slug].md
├── /narratives/index/conversations-index.md (actualizado)
└── /handoff/YYYY-MM-DD_context-next-session.md
```

## Principios del Comando

1. **Preservación Absoluta**: Conversación íntegra sin edición
2. **Metadatos Ricos**: Contexto suficiente para recuperación
3. **Trazabilidad Completa**: Enlaces a impactos en sistema
4. **Handoff Inteligente**: Continuidad para próxima sesión
5. **Zero Loss**: Ninguna información conversacional se pierde

Este comando asegura que cada conversación se convierta en narrativa estructurada que alimente el sistema de destilación orgánica.
