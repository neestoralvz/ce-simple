# CLAUDE.md - Multi-Subagent Intelligence Dispatcher

## SEMANTIC DECISION MAP

**VOZ DEL USUARIO = FUENTE DE VERDAD ABSOLUTA** - Preservación exacta de decisiones originales.

## DECISION TREE: REQUEST TYPE ROUTING

### IMMEDIATE CLASSIFICATION (Research-First Always)

**A. Session Management?**
- `¿Inicio?` → Execute: `/start` 
- `¿Cierre?` → Execute: `/session-close`
- **Reference**: [session-continuity.md](/.claude/modules/session-continuity.md)

**B. Document Operations?**
- `¿Crear documento?` → ENFORCE: `/create-doc` → `/align-doc` → `/verify-doc`
- `¿Editar documento?` → ENFORCE: `/edit-doc` → `/align-edit` → `/verify-edit`
- **Reference**: [document-workflow-enforcement.md](/.claude/modules/document-workflow-enforcement.md)

**C. Narrative Processing?**
- `¿Extract insights?` → Execute: `/extract-insights` → `/process-layer`
- **Research Integration**: Apply tier classification
- **Reference**: [research-protocols.md](/.claude/modules/research-protocols.md)

**D. Exploratory Dialogue?**
- Execute: Diálogo mayéutico + Intent detection automático
- **Auto-trigger**: `/create-doc` si detecta necesidad documento
- **Patterns**: "necesito plan", "documentar", "crear reporte"
- **Reference**: [orchestration-protocols.md](/.claude/modules/orchestration-protocols.md)

**E. Multi-Conversation Concurrency?**
- Execute: `/start-concurrent-worktrees` con coordination
- **Reference**: [system-evolution.md](/.claude/modules/system-evolution.md)

## ORCHESTRATION IMPERATIVES

### Core Rules
- **MULTI-SUBAGENT OBLIGATORIO**: Todo trabajo via Task tools especializados
- **RESEARCH-FIRST**: Apply tier classification per request type
- **DOCUMENT ENFORCEMENT**: Blocking automático + redirection workflows
- **PARALLEL TASK TOOLS**: Concurrent over sequential
- **ANTI-BIAS**: Redacción agnóstica, neutra

### Implementation References
- **Orchestration Details**: [orchestration-protocols.md](/.claude/modules/orchestration-protocols.md)
- **Research Protocols**: [research-protocols.md](/.claude/modules/research-protocols.md)
- **Document Enforcement**: [document-workflow-enforcement.md](/.claude/modules/document-workflow-enforcement.md)
- **Session Management**: [session-continuity.md](/.claude/modules/session-continuity.md)
- **System Evolution**: [system-evolution.md](/.claude/modules/system-evolution.md)

## ENFORCEMENT STATUS

**DOCUMENT WORKFLOWS**: ✅ ACTIVE - Complete coverage create/edit/maintenance
**RESEARCH TIERS**: ✅ ACTIVE - Selective criteria applied
**MULTI-SUBAGENT**: ✅ ACTIVE - Task tools orchestration
**SESSION CONTINUITY**: ✅ ACTIVE - Auto handoff + insights extraction

---

**SISTEMA EVOLUCIONA ORGÁNICAMENTE** preservando user voice como fuente de verdad mientras optimiza automáticamente architecture + efficiency via multi-subagent intelligence + research-first methodology.

**Detailed implementations**: All functionality preserved in modular references above.