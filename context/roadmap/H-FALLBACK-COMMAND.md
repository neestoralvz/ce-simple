# HANDOFF: Diseño de Comando Fallback para Scripts Faltantes

**Handoff ID**: H-FALLBACK-COMMAND  
**Fecha**: 31/07/2025  
**Contexto**: Auto-creation system para scripts faltantes con return to main workflow

## OBJETIVO ESPECÍFICO

Diseñar comando `/script-fallback` que detecte scripts faltantes, los cree automáticamente con stub functionality, y regrese al flujo principal sin interrumpir el workflow del usuario.

## ESTADO ACTUAL

- **Scripts identificados**: 8+ scripts con diferentes integration strategies
- **Scripts existentes**: Algunos ya creados, otros referenced pero missing
- **Problema**: Comandos fallan cuando scripts no existen
- **Objetivo**: Auto-creation con graceful degradation y return to workflow

## TAREAS ESPECÍFICAS

### 1. Script Detection Logic

**Missing Script Detection**:
- **Scan command references**: Buscar todas las referencias a `scripts/` en comandos
- **Verify script existence**: Check si script existe y es executable
- **Dependency analysis**: Identificar scripts que dependen de otros scripts
- **External dependency check**: Verificar herramientas externas (gh, git, etc.)

**Detection Triggers**:
- **Command execution failure**: Cuando comando falla por script missing
- **Proactive scanning**: Periodic check de script availability
- **User request**: Manual invocation para script validation
- **Hook failure**: Cuando Claude hooks fallan por script missing

### 2. Stub Script Creation Strategy

**Auto-Creation Templates por Tipo**:

**Template 1: Analysis Scripts** (analyze_violations.sh style):
```bash
#!/bin/bash
# AUTO-GENERATED STUB - Replace with actual implementation
echo "STUB: Analysis script placeholder"
echo "TODO: Implement actual analysis logic"
# Graceful exit allowing workflow continuation
exit 0
```

**Template 2: Validation Scripts** (validate-context-coherence.sh style):
```bash
#!/bin/bash
# AUTO-GENERATED STUB - Replace with actual validation
echo "STUB: Validation passed (placeholder)"
# Return success to allow workflow continuation
exit 0
```

**Template 3: Management Scripts** (conversation-workspace.sh style):
```bash
#!/bin/bash
# AUTO-GENERATED STUB - Replace with actual management logic
echo "STUB: Management operation simulated"
echo "Manual alternative: [provide manual steps]"
exit 0
```

**Template 4: Batch Processing Scripts** (batch-issue-create.sh style):
```bash
#!/bin/bash
# AUTO-GENERATED STUB - Replace with actual batch processing
echo "STUB: Batch operation placeholder"
echo "TODO: Implement actual batch processing"
exit 0
```

### 3. Fallback Command Architecture

**Command Structure** (`/script-fallback`):
```
1. Detect missing script from error context
2. Identify script type y function expected
3. Create appropriate stub script con proper permissions
4. Log creation para user awareness
5. Return success to continue main workflow
6. Provide manual alternative instructions
```

**Integration with Main Commands**:
- **Error handling**: Commands invoke /script-fallback cuando script fails
- **Transparent operation**: User workflow continues uninterrupted
- **Logging**: Track stub creations para later implementation
- **Manual alternatives**: Provide instructions cuando automation unavailable

### 4. Graceful Degradation Protocol

**Workflow Continuation**:
- **No blocking**: Script creation failure doesn't stop main workflow
- **Alternative paths**: Manual procedures embedded in stubs
- **User notification**: Inform about stub creation y needed manual steps
- **Recovery procedures**: Steps to implement actual script functionality

**Return to Main Workflow**:
- **Seamless integration**: Fallback command returns control to calling command
- **State preservation**: Maintain conversation state across fallback operation
- **Progress continuation**: Resume main workflow donde se quedó
- **Quality tracking**: Log what operations were stubbed para follow-up

### 5. Implementation Specifications

**File Structure**:
```
.claude/commands/script-fallback.md    # Main fallback command
scripts/templates/                     # Stub templates por script type
scripts/logs/                          # Creation logs
scripts/generated_stubs/               # Auto-generated stub scripts
```

**Command Interface**:
- **Input**: Script name y expected function
- **Processing**: Template selection y stub creation
- **Output**: Success status y manual alternatives
- **Logging**: Track stub creations y replacement needs

## ENTREGABLES ESPERADOS

1. **Comando /script-fallback** autocontenido y functional
2. **4 stub templates** para different script types
3. **Integration protocol** con main commands
4. **Graceful degradation strategy** preserving workflow continuity

## CRITERIOS DE ÉXITO

- ✅ Comando fallback que auto-creates missing scripts
- ✅ Workflow continuation sin interruption cuando scripts faltan
- ✅ Manual alternatives provided cuando automation unavailable
- ✅ Integration seamless con main command workflow

## SIGUIENTES HANDOFFS

- **H-HOOK-INTEGRATION**: Hook system integration
- **H-AUTOCONTAINMENT-VALIDATION**: Validación de autocontención

---

**CONTEXTO PARA SIGUIENTE CONVERSACIÓN**: Este comando es critical para system reliability. Debe ensure que missing scripts never block workflow while providing path to implement actual functionality later.