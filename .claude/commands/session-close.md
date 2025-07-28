---
contextflow:
  purpose: "Cierre inteligente de sesión con captura narrative y handoff generation"
  triggers: ["final sesión", "cambio contexto", "handoff requerido"]
  workflow-final: true
  requires-subagent: true
  communication-rules:
    - "NUNCA bash file generation directo"
    - "SIEMPRE Task tools paralelos → Main agent consolida → Execution"
    - "Subagents generan content, main agent ejecuta writes"
    - "4 Task tools concurrentes obligatorio"
---

# Comando `/session-close`

## Propósito Core
Cerrar sesión conversacional capturando narrativa completa como fuente de verdad + generar handoff para continuidad.

## Proceso Automático

### 1. Captura Conversación Completa
**SIEMPRE via Task tool - Content Specialist**:
- Conversación íntegra preservando formato exacto
- Timestamps + participantes identificados
- User voice quotes destacadas

### 2. Análisis Paralelo + Command Detection
**EJECUTAR simultáneamente en mismo mensaje**:
```
Task 1: Research Specialist - "Identificar tema + categoría + commands mencionados"
Task 2: Architecture Validator - "Detectar decisions + command changes requeridos"  
Task 3: Voice Preservation - "Extraer user voice quotes + command commitments"
Task 4: Content Optimizer - "Scan conversación para command modifications/creations"
```

### 3. Command Updates Application
**Main agent identifica y aplica command changes inmediatamente**:

#### A. Command Change Detection
- **Commands mencionados**: Nuevos comandos solicitados
- **Modifications requeridas**: Changes a comandos existentes  
- **Commitments made**: Promesas de implementation hechas durante sesión
- **TODOs generated**: Action items específicos identificados

#### B. Auto-Apply Command Updates
```
IF command_changes_detected:
  EXECUTE: Apply updates automáticamente
  - Create new commands via /create-doc workflow
  - Modify existing commands directly
  - Update CLAUDE.md si decisiones core cambiaron
  - Generate TODO items para próxima sesión
  
  POST-UPDATE: Git workflow obligatorio
  - git add [archivos modificados]
  - git commit con mensaje descriptivo
  - Preserve trazabilidad de session changes
```

### 4. Git Commit Workflow
**EJECUTAR SIEMPRE después de command updates**:

#### Git Commit Pattern
```bash
# Check git status para archivos modificados
git status

# Add archivos relacionados con session changes
git add .claude/commands/[comandos-modificados]
git add CLAUDE.md  # si fue modificado
git add handoff/[nuevo-handoff]
git add narratives/raw/conversations/[nueva-narrativa]

# Commit con mensaje descriptivo
git commit -m "Session $(TZ='America/Mexico_City' date +'%Y-%m-%d %H:%M'): [tema-sesion]

Command updates applied:
- [comando1]: [cambio realizado]
- [comando2]: [cambio realizado]

User decisions implemented:
- [decision1]
- [decision2]

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

### 5. File Generation
**Después de git commit completado**:

#### A. Narrativa Raw Generation
```
Task: Content Optimizer - Crear narrative con command changes documentados
/narratives/raw/conversations/[timestamp-mx]_[tema].md
```

#### B. Handoff Generation  
```
Task: Architecture Validator - Crear handoff con applied changes
/handoff/[timestamp-mx]_[tema]-handoff.md
Incluyendo: changes aplicados + pending items + próximos pasos
```

#### C. Update Índices
- Conversations index updated
- Handoffs registry updated  
- Cross-references established

## Parámetros Opcionales
```bash
/session-close --tema "nombre-tema"
/session-close --categoria "tecnico|personal|planning"  
/session-close --continue  # Indica continuación planeada
```

## Success Criteria
- [ ] Conversación capturada completamente
- [ ] Handoff generado con context preservation
- [ ] Índices actualizados automáticamente
- [ ] Próxima sesión setup preparado

---

**Extensions**:
- [Proceso detallado + casos edge](./extensions/session-close-details.md)
- [Metadata extraction algorithms](./extensions/session-close-metadata.md)