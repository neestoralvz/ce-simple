---
contextflow:
  purpose: "Documentation synchronization across system components"
  triggers: ["docs sync", "documentation sync", "sync documents"]
  next: ["maintain-docs", "align-doc", "verify-doc"]
  requires-subagent: true
  auto-chain: false
  communication-rules:
    - "NUNCA bash echo para comunicar con usuario"
    - "SIEMPRE Task tools → Main agent → Usuario"
    - "Parallel Task tools obligatorio en mismo mensaje"
    - "Subagents NUNCA comunican directamente"
  decision-tree:
    use-when:
      - "Documentation synchronization required"
      - "Cross-system document alignment needed"
      - "Batch document consistency validation"
    alternatives: ["maintain-docs", "supervise-alignment"]
    semantic-triggers:
      - "sync" / "synchronize" / "align documents"
      - "docs sync" / "documentation sync"
      - "batch alignment" / "system sync"
---

# /docs-sync - Actualización Automática de Documentación

Comando para sincronizar y actualizar toda la documentación del proyecto basándose en nuevas narrativas, cambios en código y evolución del sistema.

## Funcionalidad

Este comando ejecuta un ciclo completo de actualización documentaria:

1. **Analiza cambios recientes** en:
   - Nuevas narrativas en `/narratives/raw/`
   - Actualizaciones en código y estructura
   - Planes completados en `/plans/`
   - Evolución de principios y patrones

2. **Actualiza automáticamente**:
   - `CLAUDE.md` con nuevos principios identificados
   - `/docs/context/` con insights consolidados
   - `README.md` con estado actual del proyecto
   - Índices y referencias cruzadas

3. **Valida coherencia** entre:
   - Documentación vs implementación actual
   - Principios declarados vs patrones observados
   - Planes vs estado real del proyecto

## Uso

```bash
/docs-sync
```

### Parámetros opcionales:
```bash
/docs-sync --full          # Regenera toda la documentación desde cero
/docs-sync --validate-only # Solo valida coherencia, no actualiza
/docs-sync --narratives    # Enfoque solo en nuevas narrativas
```

## Proceso Automático

### Fase 1: Detección de Cambios
- Escanea timestamps de archivos modificados
- Identifica nuevas narrativas no procesadas
- Detecta cambios en estructura del proyecto
- Marca discrepancias en documentación existente

### Fase 2: Análisis y Síntesis
- Usa Task tools para análisis paralelo de cambios
- Extrae nuevos principios y patrones emergentes
- Identifica evolución en el pensamiento del usuario
- Genera síntesis consolidada de actualizaciones

### Fase 3: Actualización Inteligente
- Actualiza CLAUDE.md preservando estructura
- Agrega nuevos insights a `/docs/context/`
- Mantiene trazabilidad hacia narrativas origen
- Preserva historial de evolución

### Fase 4: Validación de Coherencia
- Verifica que documentación refleje realidad
- Identifica contradicciones entre documentos
- Valida que principios se implementen en código
- Genera reporte de estado del proyecto

## Criterios de Actualización

### CLAUDE.md
- **Nuevos principios** identificados en narrativas
- **Cambios en workflow** basados en uso real
- **Actualizaciones tecnológicas** (nuevas herramientas/métodos)
- **Refinamientos de comportamiento** solicitados por usuario

### /docs/context/
- **Insights consolidados** de múltiples narrativas
- **Patrones emergentes** en uso del sistema
- **Lecciones aprendidas** de implementación
- **Mejores prácticas** identificadas

### Planes
- **Estado actualizado** de planes en progreso
- **Nuevos planes** derivados de conversaciones
- **Completion tracking** de objetivos
- **Archiving** de planes completados

## Automatización Inteligente

### Triggers Automáticos
- Nuevo archivo en `/narratives/raw/`
- Cambios significativos en estructura de proyecto
- Completion de planes en `/plans/`
- Solicitud explícita del usuario

### Inteligencia de Contenido
- **No duplica** información ya documentada
- **Preserva** estructura y formato existente
- **Integra** nueva información en contexto apropiado
- **Mantiene** coherencia de estilo y tone

### Human-in-the-Loop
- **Preview** de cambios antes de aplicar
- **Validación** de nuevos principios extraídos
- **Confirmación** de actualizaciones mayores
- **Option** para ajustes manuales

## Salidas Generadas

```
docs-sync-report-YYYY-MM-DD-HH-MM.md
├── Cambios detectados
├── Nuevos principios identificados  
├── Actualizaciones aplicadas
├── Discrepancias encontradas
└── Próximas acciones recomendadas
```

## Principios del Comando

1. **Preservación**: Nunca destruye información existente
2. **Integración**: Agrega sin duplicar
3. **Trazabilidad**: Mantiene origen de cada actualización
4. **Coherencia**: Asegura consistencia entre documentos
5. **Automatización Inteligente**: Minimiza intervención manual necesaria

Este comando asegura que la documentación evolucione orgánicamente con el proyecto sin volverse inmanejable de mantener.