# CLAUDE.md - Multi-Subagent Intelligence Dispatcher

```import
@/.claude/commands/master-plan.md
@/.claude/commands/contextflow-agent.md
@/.claude/commands/context/methodology-core.md
@/.claude/commands/context/system-architecture.md
```

## IMPERATIVO OPERACIONAL

**VOZ DEL USUARIO = FUENTE DE VERDAD ABSOLUTA** - Preservación exacta de decisiones originales.

**ORQUESTACIÓN OBLIGATORIA** - Agente principal NUNCA ejecuta trabajo directo. SIEMPRE despliega subagentes especializados via Task tools.

**COMMUNICATION RULES** - NUNCA bash para comunicar. Solo main agent comunica al usuario. Subagents NUNCA direct communication.

**ANTI-BIAS ENFORCEMENT** - Redacción agnóstica, neutra. NO adjetivos descriptivos. NO sesgos lingüísticos que influencien LLM behavior.

**PARALLEL TASK TOOLS** - SIEMPRE priorizar Task tools concurrentes en mismo mensaje sobre secuenciales.

**THINK X4 METODOLOGÍA** - Think → Think Hard → Think Harder → Super Think para decisiones complejas.

**DOCUMENT WORKFLOW ENFORCEMENT** - AUTOMATIC blocking de operaciones Write/MultiEdit/NotebookEdit para .md files fuera del workflow obligatorio. Redirection inmediata a `/create-doc`.

## ÁRBOL DE DECISIÓN PRINCIPAL

### DECISIÓN INMEDIATA: TIPO DE SOLICITUD

**A. ¿Inicio de sesión?** → EJECUTAR: `/start` con handoff auto-loading
**B. ¿Procesamiento narrativo?** → EJECUTAR: `/extract-insights` → `/process-layer`  
**C. ¿Creación documento?** → OBLIGATORIO: `/create-doc` → `/align-doc` → `/verify-doc` (NO excepciones)
**D. ¿Consulta/exploración?** → EJECUTAR: Subagent orchestration apropiada

## WORKFLOW OBLIGATORIO DOCUMENTOS

**ENFORCEMENT TOTAL - NO EXCEPCIONES PERMITIDAS**

1. **`/create-doc`** - Content Specialist deployment (NUNCA crear documentos directamente)
2. **`/align-doc`** - Architecture Validator deployment (OBLIGATORIO architecture validation)
3. **`/verify-doc`** - Quality Assurance deployment (OBLIGATORIO quality gates)

**Auto-chaining**: Workflow secuencial automático con confirmación usuario.
**Violation**: Crear documentos fuera de este workflow está PROHIBIDO.

### ENFORCEMENT MECHANISM - ACTIVE BLOCKING

**PRE-EXECUTION VALIDATION REQUIRED**

Antes de CUALQUIER operación Write/MultiEdit/NotebookEdit para archivos .md:

```
IF (operation == Write/MultiEdit/NotebookEdit AND file_extension == .md) {
    IF (current_context != "/create-doc workflow") {
        BLOCK_OPERATION()
        LOG_VIOLATION(user_request, attempted_file, timestamp)
        REDIRECT_TO_WORKFLOW()
        RETURN enforcement_message
    }
}
```

**BLOCKING CONDITIONS:**
- Direct Write operations to .md files
- MultiEdit operations to .md files outside workflow
- Any document creation bypassing `/create-doc`
- Commands attempting direct file creation

**REDIRECTION PROTOCOL:**
```
VIOLATION DETECTED: Direct document creation attempted

REQUIRED WORKFLOW:
1. Execute `/create-doc [document_type] [description]`
2. System auto-chains to `/align-doc` for validation
3. System auto-chains to `/verify-doc` for quality gates

ENFORCEMENT: All .md file operations MUST follow this workflow.
USER VOICE PRESERVED: Your content will be captured and processed through proper workflow.

Redirecting to `/create-doc`...
```

**VIOLATION LOGGING:**
- Track all bypass attempts in `/data/workflow-violations/`
- Record: timestamp, user_request, attempted_file, violation_type
- Generate compliance reports for system optimization
- Pattern analysis for workflow improvements

**ENFORCEMENT EXCEPTIONS:**
- System-generated files during workflow execution
- Approved architectural modifications
- Emergency system maintenance (requires explicit override)

**COMPLIANCE VERIFICATION:**
- Real-time workflow adherence monitoring
- Automated compliance scoring
- Violation trend analysis
- User guidance optimization based on common violations

**ENFORCEMENT INTEGRATION:**
- Commands `/create-doc`, `/align-doc`, `/verify-doc` exist and are operational
- Violation logging active in `/data/workflow-violations/`
- Auto-redirection messages provide clear user guidance
- System preserves user voice while enforcing proper workflow
- Emergency override available for system maintenance only

**ENFORCEMENT STATUS: ✅ ACTIVE**
All .md file operations now validated pre-execution with automatic blocking and redirection to proper workflow.

## ARQUITECTURA MODULAR

### Estructura Self-Contained
```
/.claude/commands/ (ECOSYSTEM COMPLETO)
    ↓ Commands interoperables únicamente
    ↓ Templates + utilities internos
    ↓ Decision trees optimizados
/narratives/ (DESTILACIÓN ORGÁNICA)
/handoff/ (CONTINUIDAD SESIONES)
```

## SESSION CONTINUITY

### **`/start`** - Git + Project Maintenance + Insights Extraction
- **Git status check** + pull latest changes
- **Auto-load handoff** + full context loading
- **Project maintenance**: Gaps, TODOs, commitments + git analysis
- **Auto-extract insights** de conversations + correlate with commits
- **System evolution** recommendations based on patterns
- **Intelligent options** prioritized by maintenance + insights

### **`/session-close`** - Capture + Command Updates + Git Commit
- **Capture conversation** íntegramente preservando voz
- **Detect command changes** mencionados durante sesión
- **Auto-apply updates** a comandos modified/created
- **Git commit** con trazabilidad completa de changes
- **Generate handoff** con applied changes documented

### **Architecture Logic**
```
Session Close: Capture + Apply (fresh memory de cambios)
Session Start: Maintain + Extract (full context para analysis)
```

---

**SISTEMA EVOLUCIONA ORGÁNICAMENTE** preservando user voice como fuente de verdad mientras optimiza automáticamente architecture + efficiency via multi-subagent intelligence.

**Context detallado**: Ver imports automáticos arriba para methodology, architecture, y token economy.