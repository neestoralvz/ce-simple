# q-recreate - Quick Clean Slate Recreation

**31/07/2025 00:00 CDMX** | Clean slate recreation para prevenir sesgos

## Propósito Command
**Input:** Archivo/sistema desalineado con lineamientos actualizados  
**Output:** Recreación limpia desde cero siguiendo guidelines actuales
**Authority:** @context/architecture/core/truth-source.md + context/vision/simplicity.md

## Filosofía Ejecución
**DEBE ser:** Clean slate recreation sin contamination de información previa
**SIEMPRE produce:** Archivo completamente alineado con lineamientos actuales
**NUNCA requiere:** Construcción incremental sobre versiones anteriores sesgadas

## Protocol Execution

### Phase 1: Desalineación Detection
**Trigger:** Archivo no sigue lineamientos actualizados del sistema
**Process:** 
- Analizar archivo actual vs @context/architecture/core/truth-source.md
- Identificar divergencias específicas con context/vision/simplicity.md
- Detectar sesgo acumulativo de información obsoleta
- Validar necesidad clean slate vs edit incremental
**Validation:** Sesgo detectado > threshold || structural misalignment identificado

### Phase 2: Context Fresh Loading
**Input:** Lineamientos actuales del sistema (TRUTH_SOURCE + patterns)
**Process:**
- Load @context/architecture/core/truth-source.md para supreme authority
- Reference context/vision/simplicity.md para recreation guidelines
- Apply context/architecture/core/methodology.md metodologías
- Clear mental model del archivo anterior (bias prevention)
**Output:** Context limpio con guidelines actuales únicamente

### Phase 3: Clean Slate Recreation
**Trigger:** Context fresh loaded + archivo original eliminado conceptualmente
**Process:**
- **ELIMINAR** archivo existente (conceptual clean slate)
- **RECREAR** desde cero usando ÚNICAMENTE lineamientos actuales
- **APLICAR** Think x4 para optimal structure según guidelines
- **VALIDAR** alignment completo con @context/architecture/core/truth-source.md
**Validation:** Archivo nuevo 100% aligned + zero contamination anterior

### Phase 4: Integration Verification
**Input:** Archivo recreado limpiamente
**Process:**
- Verificar coherencia con ecosystem actual
- Validar references no apuntan a información obsoleta
- Confirmar autocontained principle maintained
- Test integration con comandos relacionados
**Output:** Sistema completamente coherent post-recreation

## Integration Points
**Coordinates with:**
- q-context → Para documentación que requiere recreation
- r-orchestrator → Para delegation recreation multi-archivo  
- w-start → Para detection desalinaación en session start

**Authority chain:** user-vision/@context/architecture/core/truth-source.md → context/vision/simplicity.md → recreation limpia

## Error Handling
**Si archivo crítico:** → Backup conceptual + user confirmation antes recreation
**OBLIGATORIO verificar:** @context/architecture/core/truth-source.md authority suprema maintained
**Fallback mode:** Edit incremental si recreation imposible técnicamente

## Core Function
Clean slate recreation to prevent bias accumulation and ensure complete alignment with current guidelines

**Features**: Desalineación detection + context fresh loading + anti-bias methodology + integration verification