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

**DIÁLOGO MAYÉUTICO + INTENT DETECTION** - Durante conversación exploratoria, semantic analysis automático detecta necesidad documentos y auto-trigger `/create-doc` seamlessly sin interrumpir flujo conversacional.

**COMMUNICATION RULES** - NUNCA bash para comunicar. Solo main agent comunica al usuario. Subagents NUNCA direct communication.

**ANTI-BIAS ENFORCEMENT** - Redacción agnóstica, neutra. NO adjetivos descriptivos. NO sesgos lingüísticos que influencien LLM behavior.

**PARALLEL TASK TOOLS** - SIEMPRE priorizar Task tools concurrentes en mismo mensaje sobre secuenciales.

**THINK X4 METODOLOGÍA** - Think → Think Hard → Think Harder → Super Think para decisiones complejas.

**RESEARCH-FIRST PROTOCOL OBLIGATORIO** - TODA decisión/tarea DEBE iniciar con:
1. `$(date)` para timestamp actualizado
2. WebSearch con fecha actual para best practices
3. MCP Context7 para análisis de patrones 
4. Sistematización automática de findings

### RESEARCH INTEGRATION REQUIREMENTS:
- **Pre-Task Research**: OBLIGATORIO para cada Task tool deployment
- **Context Updates**: Research findings deben actualizarse sistemáticamente
- **Pattern Recognition**: MCP Context7 para identificar patterns emergentes
- **Best Practice Adoption**: WebSearch findings integrados automáticamente
- **Temporal Accuracy**: Siempre usar fecha actual $(date) para relevancia

**DOCUMENT WORKFLOW ENFORCEMENT** - AUTOMATIC blocking de operaciones Write/MultiEdit/NotebookEdit para .md files fuera del workflow obligatorio. Redirection inmediata a `/create-doc`.

## ÁRBOL DE DECISIÓN PRINCIPAL

### DECISIÓN INMEDIATA: TIPO DE SOLICITUD (RESEARCH-FIRST ALWAYS)

**A. ¿Inicio de sesión?** → RESEARCH + EJECUTAR: `/start` con WebSearch + MCP Context7 + handoff auto-loading
**B. ¿Procesamiento narrativo?** → RESEARCH + EJECUTAR: `/extract-insights` → `/process-layer` con research integration  
**C. ¿Creación documento?** → RESEARCH + OBLIGATORIO: `/create-doc` → `/align-doc` → `/verify-doc` (NO excepciones)
**D. ¿Consulta/exploración?** → RESEARCH + EJECUTAR: Diálogo mayéutico + Intent detection automático
  - **Semantic analysis** paralelo durante conversación
  - **Auto-trigger** `/create-doc` si detecta necesidad documento (patterns: "necesito plan", "documentar", "crear reporte")
  - **Seamless integration** sin interrumpir flujo conversacional
  - **Background processing** document creation mientras continúa diálogo
**E. ¿Multi-conversation concurrency?** → RESEARCH + EJECUTAR: `/start-concurrent-worktrees` con coordination

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

REQUIRED RESEARCH-FIRST WORKFLOW:
1. RESEARCH PHASE: WebSearch + MCP Context7 con fecha $(date)
2. Execute `/create-doc [document_type] [description]`
3. System auto-chains to `/align-doc` for validation
4. System auto-chains to `/verify-doc` for quality gates

ENFORCEMENT: All .md file operations MUST follow research-first workflow.
USER VOICE PRESERVED: Your content will be captured and processed through proper workflow.

Redirecting to research-first `/create-doc`...
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

### **`/start`** - Research-First Git + Project Maintenance + Insights Extraction
- **RESEARCH PROTOCOL**: WebSearch + MCP Context7 con $(date) para current best practices
- **Git status check** + pull latest changes con research-driven analysis
- **Auto-load handoff** + full context loading + research integration
- **Project maintenance**: Gaps, TODOs, commitments + git analysis + research findings
- **Auto-extract insights** de conversations + correlate with commits + research patterns
- **System evolution** recommendations based on patterns + research-driven optimization
- **Intelligent options** prioritized by maintenance + insights + research findings

### **`/session-close`** - Research-Enhanced Capture + Command Updates + Git Commit
- **RESEARCH INTEGRATION**: Consolidate WebSearch + MCP Context7 findings from session
- **Capture conversation** íntegramente preservando voz + research patterns learned
- **Detect command changes** mencionados durante sesión + research-driven updates
- **Auto-apply updates** a comandos modified/created
- **Git commit** con trazabilidad completa de changes
- **Generate handoff** con applied changes documented

### **Architecture Logic**
```
Session Close: Capture + Apply (fresh memory de cambios)
Session Start: Maintain + Extract (full context para analysis)
```

## SYSTEMATIC EVOLUTION PROTOCOL

### Research-Driven Evolution (NEW PARADIGM):
**SYSTEMATIC INTEGRATION IMPERATIVE**: User feedback → Systematic changes across ALL commands
- **Learning Pattern**: Aciertos + errores → Updates sistemáticos permanentes
- **Research Integration**: WebSearch + MCP Context7 → Knowledge base evolutiva
- **Temporal Accuracy**: $(date) usage → Always current best practices
- **Pattern Propagation**: Discoveries → Automatic integration across ecosystem

### Evolution Triggers:
1. **User Feedback**: "hacer cambios sistemáticos" → Update ALL relevant commands
2. **Research Findings**: WebSearch discoveries → Systematic pattern updates  
3. **MCP Insights**: Context7 analysis → Architecture improvements
4. **Best Practice Evolution**: New patterns → Automatic adoption

---

**SISTEMA EVOLUCIONA ORGÁNICAMENTE** preservando user voice como fuente de verdad mientras optimiza automáticamente architecture + efficiency via multi-subagent intelligence + research-first methodology.

**Context detallado**: Ver imports automáticos arriba para methodology, architecture, token economy + research-first protocol integration.