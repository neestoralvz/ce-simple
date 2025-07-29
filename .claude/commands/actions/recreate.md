# /actions:recreate - Clean Slate Recreation Para Prevenir Sesgos

**29/07/2025 11:45 CDMX** | Comando workflow autocontenido

## Propósito Command
**Input:** Archivo/sistema desalineado con lineamientos actualizados  
**Output:** Recreación limpia desde cero siguiendo guidelines actuales
**Authority:** context/user-vision/TRUTH_SOURCE.md + context/patterns/simplicity.md

## Filosofía Ejecución
**DEBE ser:** Clean slate recreation sin contamination de información previa
**SIEMPRE produce:** Archivo completamente alineado con lineamientos actuales
**NUNCA requiere:** Construcción incremental sobre versiones anteriores sesgadas

## Protocol Execution

### Phase 1: Desalineación Detection
**Trigger:** Archivo no sigue lineamientos actualizados del sistema
**Process:** 
- Analizar archivo actual vs context/user-vision/TRUTH_SOURCE.md
- Identificar divergencias específicas con context/patterns/simplicity.md
- Detectar sesgo acumulativo de información obsoleta
- Validar necesidad clean slate vs edit incremental
**Validation:** Sesgo detectado > threshold || structural misalignment identificado

### Phase 2: Context Fresh Loading
**Input:** Lineamientos actuales del sistema (TRUTH_SOURCE + patterns)
**Process:**
- Load context/user-vision/TRUTH_SOURCE.md para supreme authority
- Reference context/patterns/simplicity.md para recreation guidelines
- Apply context/enforcement/core_reminders.md metodologías
- Clear mental model del archivo anterior (bias prevention)
**Output:** Context limpio con guidelines actuales únicamente

### Phase 3: Clean Slate Recreation
**Trigger:** Context fresh loaded + archivo original eliminado conceptualmente
**Process:**
- **ELIMINAR** archivo existente (conceptual clean slate)
- **RECREAR** desde cero usando ÚNICAMENTE lineamientos actuales
- **APLICAR** Think x4 para optimal structure según guidelines
- **VALIDAR** alignment completo con TRUTH_SOURCE.md
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
- /actions:docs → Para documentación que requiere recreation
- /roles:orchestrator → Para delegation recreation multi-archivo  
- /workflows:start → Para detection desalinaación en session start

**Authority chain:** user-vision/TRUTH_SOURCE.md → context/patterns/simplicity.md → recreation limpia

## Error Handling
**Si archivo crítico:** → Backup conceptual + user confirmation antes recreation
**OBLIGATORIO verificar:** TRUTH_SOURCE.md authority suprema maintained
**Fallback mode:** Edit incremental si recreation imposible técnicamente

## Metodología Anti-Sesgo

### Principio Clean Slate Absolute
> "es importante eliminar archivos y crealos desde cero bajo los lineamientos que vamos actualizando, pues si solo vamos construyendo sobre los anteriores existe demasiado sesgo por la informacion que ya esta"

### Contamination Prevention Protocol
**NUNCA leer** archivo anterior durante recreation process
**ÚNICAMENTE usar** lineamientos actuales como source
**MENTAL MODEL** debe ser tabula rasa para información nueva
**BIAS DETECTION** sistemático post-recreation

### Think x4 Para Recreation
**Think 1:** ¿Qué function/purpose debe cumplir archivo según guidelines actuales?
**Think 2:** ¿Cuál es optimal structure según TRUTH_SOURCE + simplicity patterns?
**Think 3:** ¿Cómo prevenir contamination de versiones anteriores sesgadas?
**Think 4:** ¿Cómo validar 100% alignment con lineamientos actualizados?

## State Management
**Persists:** User vision y lineamientos actuales únicamente
**Clears:** Toda información de archivo anterior (mental contamination prevention)
**Handoff to:** Archivo recreado limpio + integration verification

## Usage Examples
1. /actions:recreate context/patterns/obsolete_pattern.md
   → Detecta desalineación → Elimina conceptualmente → Recrea desde cero con TRUTH_SOURCE

2. /actions:recreate .claude/commands/legacy_command.md  
   → Identifica sesgo acumulativo → Clean slate recreation → Comando aligned 100%

3. /actions:recreate context/decisions/outdated_framework.md
   → Authority validation → Recreation completa → Integration verification

## Detection Triggers Automáticos
**File divergence** > 30% from current guidelines
**Metadata obsoleto** detectado in headers/references  
**Structural misalignment** con simplicity principles
**Sesgo acumulativo** por edits incrementales repetidos
**Authority conflicts** con TRUTH_SOURCE.md supremacy

---
## Enlaces → Información Complementaria
**Si necesitas authority validation:** → context/user-vision/TRUTH_SOURCE.md:93-94
**Si requieres simplicity guidelines:** → context/patterns/simplicity.md:40-50  
**Si authority conflict:** → context/principles/authority.md:15-25