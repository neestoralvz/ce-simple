# CLAUDE.md - Multi-Subagent Intelligence Dispatcher

## CONTEXT CORE - Self-Contained Architecture

### Metodología Fundamental
- **Socrática expansiva**: Conversación libre → Comprensión rica → Ejecución optimizada  
- **Multi-subagent obligatorio**: Especialización + parallel orchestration via Task tools
- **Think x4**: Think → Think Hard → Think Harder → Super Think para decisiones complejas
- **Voice preservation**: User voice = source of truth absoluta con citas exactas

### Multi-Subagent Orchestration
**OBLIGATORIO**: Todo trabajo via Task tools con subagentes especializados:
- **Research Specialist**: Investigation + benchmarking + best practices
- **Architecture Validator**: System consistency + integration verification  
- **Content Optimizer**: Token economy + structure optimization
- **Voice Preservation**: User intent exactitude + authenticity validation
- **Quality Assurance**: Final validation + standards compliance

### System State & Evolution
**Master Plan Auto-Evolution**: Multi-Subagent Intelligence System que evoluciona orgánicamente preservando user voice como fuente de verdad while optimizing efficiency via specialized orchestration.

**Current Focus**: Command Self-Containment Architecture completion enabling ecosystem independence + inter-command protocols + internal template management + decision tree optimization.

### Architecture Self-Containment
- Commands ecosystem independence: NO external dependencies fuera de /.claude/commands/
- Interoperabilidad SOLO via command chaining between commands
- Templates + utilities internos dentro del ecosystem  
- Decision trees optimizados within command structure

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
IF (operation == Write/MultiEdit/NotebookEdit/Edit AND file_extension == .md) {
    IF (current_context NOT IN ["/create-doc workflow", "/edit-doc workflow"]) {
        BLOCK_OPERATION()
        LOG_VIOLATION(user_request, attempted_file, timestamp, operation_type)
        IF (file_exists) {
            REDIRECT_TO_EDIT_WORKFLOW()
        } ELSE {
            REDIRECT_TO_CREATE_WORKFLOW()
        }
        RETURN enforcement_message
    }
}
```

**BLOCKING CONDITIONS:**
- Direct Write operations to .md files outside approved workflows
- MultiEdit operations to .md files outside workflow
- Edit operations to .md files outside `/edit-doc` workflow
- Any document creation bypassing `/create-doc`
- Any document editing bypassing `/edit-doc`
- Commands attempting direct file creation or modification

**REDIRECTION PROTOCOL:**

**For New Document Creation:**
```
VIOLATION DETECTED: Direct document creation attempted

REQUIRED RESEARCH-FIRST CREATE WORKFLOW:
1. RESEARCH PHASE: WebSearch + MCP Context7 con fecha $(date)
2. Execute `/create-doc [document_type] [description]`
3. System auto-chains to `/align-doc` for validation
4. System auto-chains to `/verify-doc` for quality gates

Redirecting to research-first `/create-doc`...
```

**For Existing Document Editing:**
```
VIOLATION DETECTED: Direct document editing attempted

REQUIRED RESEARCH-FIRST EDIT WORKFLOW:
1. RESEARCH PHASE: WebSearch + MCP Context7 con fecha $(date)
2. Execute `/edit-doc [file_path] [edit_description]`
3. System auto-chains to `/align-edit` for validation
4. System auto-chains to `/verify-edit` for quality gates

Redirecting to research-first `/edit-doc`...
```

**Universal Enforcement:**
```
ENFORCEMENT: All .md file operations MUST follow approved workflows.
USER VOICE PRESERVED: Your content will be captured and processed through proper workflow.
CHOICE AUTOMATIC: System detects file existence and routes to appropriate workflow.
```

**VIOLATION LOGGING:**
- Track all bypass attempts in `/data/workflow-violations/`
- Record: timestamp, user_request, attempted_file, violation_type, operation_type
- Generate compliance reports for system optimization
- Pattern analysis for both create and edit workflow improvements
- Separate tracking for creation vs edit violations

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
- **CREATE WORKFLOW**: `/create-doc`, `/align-doc`, `/verify-doc` fully operational
- **EDIT WORKFLOW**: `/edit-doc`, `/align-edit`, `/verify-edit` fully operational  
- **MAINTENANCE WORKFLOW**: `/maintain-docs` for proactive document health
- Violation logging active in `/data/workflow-violations/`
- Auto-redirection messages provide clear user guidance
- System preserves user voice while enforcing proper workflow
- Intelligent routing based on file existence (create vs edit)
- Emergency override available for system maintenance only

**ENFORCEMENT STATUS: ✅ ACTIVE - ENHANCED WITH EDIT WORKFLOW**
All .md file operations validated pre-execution with intelligent routing:
- **NEW FILES**: Auto-redirect to `/create-doc` workflow
- **EXISTING FILES**: Auto-redirect to `/edit-doc` workflow  
- **MAINTENANCE**: `/maintain-docs` for proactive document health
- **COMPLETE COVERAGE**: Create, Edit, and Maintenance workflows fully integrated

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