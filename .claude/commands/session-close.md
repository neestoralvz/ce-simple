---
contextflow:
  purpose: "Cierre inteligente de sesión con captura narrative y handoff generation"
  triggers: ["final sesión", "cambio contexto", "handoff requerido"]
  workflow-final: true
  execution-modes:
    - subagent: "4 Task tools concurrentes para comprehensive analysis"
    - direct: "Orchestrator direct execution manteniendo funcionalidad completa"
  communication-rules:
    - "NUNCA bash file generation directo"
    - "Mode detection: Si caller es orchestrator → direct execution"
    - "Mode detection: Si caller es standard user → subagent deployment"
    - "Direct mode: Main agent ejecuta full workflow internamente"
---

# Comando `/session-close`

## Propósito Core
Cerrar sesión conversacional capturando narrativa completa como fuente de verdad + generar handoff para continuidad.

## Execution Mode Detection

**ORCHESTRATOR DETECTION LOGIC**:
```python
if context.contains(["ORCHESTRATOR_HUB", "orchestrator-hub-coordinator", "orquestador de orquestadores"]):
    execution_mode = "direct"
    # Direct execution manteniendo funcionalidad completa
else:
    execution_mode = "subagent"
    # 4 Task tools deployment for comprehensive analysis
```

## Proceso Automático

### MODE A: Direct Execution (Orchestrator)
**INTEGRATED WORKFLOW**: Main agent ejecuta complete analysis + capture + handoff + git internally:

#### 1. Conversation Analysis (Internal)
- **Theme Identification**: Extract primary topic, secondary themes, decision points
- **Category Classification**: Document creation, implementation, planning, optimization
- **Commands Detection**: Explicit mentions, implied commands, modifications discussed
- **Decision Inventory**: System changes, command updates, architecture impacts
- **Voice Preservation**: Exact user quotes with attribution, commitments made
- **Command Change Scanning**: New commands, modifications, implementation specs

#### 2. Command Updates Application (Direct)
- **Change Detection**: Commands mentioned, modifications required, commitments made
- **Auto-Apply Updates**: Create/modify commands directly, update CLAUDE.md if needed
- **Implementation**: Direct execution without Task tool overhead

#### 3. File Generation (Integrated)
**DIRECT EXECUTION WORKFLOW**:

```python
# Phase 1: Conversation Capture
conversation_content = capture_full_conversation()
session_context = extract_session_metadata()
timestamp_mx = generate_mexico_timestamp()

# Phase 2: Integrated Analysis
analysis_results = {
    'theme': identify_conversation_theme(conversation_content),
    'category': classify_conversation_type(conversation_content),
    'commands_detected': scan_command_mentions(conversation_content),
    'decisions_made': extract_user_decisions(conversation_content),
    'voice_quotes': preserve_exact_user_voice(conversation_content),
    'command_changes': detect_command_modifications(conversation_content),
    'commitments': extract_implementation_commitments(conversation_content)
}

# Phase 3: Command Updates (Direct)
if analysis_results['command_changes']:
    apply_command_updates_directly(analysis_results['command_changes'])
    update_claude_md_if_needed(analysis_results['decisions_made'])

# Phase 4: File Generation (Integrated)
create_narrative_file(conversation_content, analysis_results, timestamp_mx)
execute_smart_handoff_consolidation(analysis_results, timestamp_mx)

# Phase 5: Git Workflow (Automated)
execute_enhanced_git_commit(analysis_results, timestamp_mx)
```

**IMPLEMENTATION BENEFITS**:
- **Zero Task Tool Overhead**: Direct execution elimina spawning conversaciones
- **Maintained Functionality**: Identical output compared to subagent mode
- **Orchestrator Optimized**: Diseñado para orquestador de orquestadores
- **Performance Gain**: Significant reduction in execution time + resource usage

### MODE B: Subagent Deployment (Standard User)
**TASK TOOLS DEPLOYMENT**: 4 specialists concurrentes para comprehensive conversation analysis:

```python
# TASK 1: Research Specialist
Task(
    description="Identify theme, category, and commands mentioned",
    prompt="""Actúa como Research Specialist. CONVERSATION ANALYSIS MISSION: Extract key elements.

CONVERSATION INPUT:
- Complete conversation: {full_conversation_content}
- Participants: {conversation_participants}
- Timestamps: {conversation_timeline}
- Context: {session_context}

ANALYSIS OBJECTIVES:
1. Theme Identification:
   - Primary topic/focus of conversation
   - Secondary themes discussed
   - Evolution of topics throughout session
   - Key decision points reached

2. Category Classification:
   - Document creation, architecture discussion, implementation
   - Planning, analysis, troubleshooting, optimization
   - User feedback, system evolution, methodology refinement

3. Commands Detection:
   - Commands explicitly mentioned or requested
   - Implied commands from user requests
   - Command modifications discussed
   - New command requirements identified

OUTPUT: Structured analysis con theme, category, commands inventory.""",
    subagent_type="general-purpose"
)

# TASK 2: Architecture Validator
Task(
    description="Detect decisions and command changes required",
    prompt="""Actúa como Architecture Validator. DECISION DETECTION MISSION: Identify system changes.

DECISION ANALYSIS SCOPE:
- Conversation content: {conversation_content}
- System context: Current architecture state
- Command ecosystem: Existing commands structure
- User commitments: Promises made during session

DECISION DETECTION:
1. Explicit Decisions Made:
   - User decisions about system behavior
   - Architecture changes approved
   - Methodology updates decided
   - Command modifications agreed upon

2. Command Changes Required:
   - New commands to be created
   - Existing commands to be modified
   - Commands to be deprecated/removed
   - Command integration updates needed

3. System Architecture Impact:
   - Core system changes required
   - Rules system updates needed
   - Documentation updates required
   - Integration points affected

OUTPUT: Decision inventory con specific command change requirements.""",
    subagent_type="general-purpose"
)

# TASK 3: Voice Preservation Specialist
Task(
    description="Extract user voice quotes and command commitments",
    prompt="""Actúa como Voice Preservation Specialist. VOICE EXTRACTION MISSION: Preserve user voice exactly.

VOICE PRESERVATION SCOPE:
- Conversation content: {complete_conversation}
- User statements: All user messages in conversation
- Commitment tracking: Promises and decisions made
- Voice evolution: Changes in user preferences

VOICE EXTRACTION REQUIREMENTS:
1. Exact User Quotes:
   - All significant user statements (ZERO paraphrasing)
   - Complete source attribution with message timestamps
   - Context preservation for each quote
   - Intent clarification where needed

2. Command Commitments:
   - Explicit commitments made about commands
   - Implementation promises given
   - Timeline commitments stated
   - Scope agreements reached

3. User Voice Evolution:
   - Changes in preferences during session
   - New insights about user workflow
   - Methodology preference updates
   - System usage pattern changes

OUTPUT: Exact user voice quotes con complete attribution + commitment inventory.""",
    subagent_type="general-purpose"
)

# TASK 4: Content Optimizer
Task(
    description="Scan conversation for command modifications and creations",
    prompt="""Actúa como Content Optimizer. COMMAND CHANGE SCANNING MISSION: Identify all command impacts.

COMMAND SCANNING SCOPE:
- Full conversation: {conversation_content}
- Existing commands: Current command ecosystem state
- User requests: All command-related requests made
- Implementation context: Technical feasibility assessment

COMMAND CHANGE DETECTION:
1. New Command Requirements:
   - Commands explicitly requested
   - Workflow gaps requiring new commands
   - User needs indicating missing functionality
   - Integration commands needed

2. Existing Command Modifications:
   - Specific changes requested to existing commands
   - Behavior modifications discussed
   - Integration updates needed
   - Optimization opportunities identified

3. Command Creation Specifications:
   - Detailed requirements for new commands
   - Integration points with existing system
   - User workflow integration needs
   - Technical implementation considerations

OUTPUT: Complete command change specification con implementation details.""",
    subagent_type="general-purpose"
)
```

### MODE B CONTINUATION: Command Updates Application
**MAIN AGENT CONSOLIDATION**: Receive outputs from 4 specialists → Identify all command changes → Apply updates immediately → Execute git workflow:

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

### Universal Git Commit Workflow
**EJECUTAR SIEMPRE después de command updates** (both modes):

#### Git Commit Pattern
```bash
# Check git status para archivos modificados
git status

# Add archivos relacionados con session changes
git add .claude/commands/[comandos-modificados]
git add CLAUDE.md  # si fue modificado

# ENHANCED: Smart handoff git handling
if [ -f "handoff/$(TZ='America/Mexico_City' date +'%Y-%m-%d')_master-consolidated.md" ]; then
    git add handoff/$(TZ='America/Mexico_City' date +'%Y-%m-%d')_master-consolidated.md
    git add handoff/archive/$(TZ='America/Mexico_City' date +'%Y-%m-%d')/ # if created
else
    git add handoff/[nuevo-handoff-individual]
fi

git add narratives/raw/conversations/[nueva-narrativa]

# Enhanced commit message for consolidation tracking
git commit -m "Session $(TZ='America/Mexico_City' date +'%Y-%m-%d %H:%M'): [tema-sesion]

Handoff Management:
- Master consolidated: $([ -f handoff/$(TZ='America/Mexico_City' date +'%Y-%m-%d')_master-consolidated.md ] && echo 'Updated' || echo 'Created')
- Sessions archived: [number] individual handoffs consolidated
- Archive status: Clean handoff directory maintained

Command updates applied:
- [comando1]: [cambio realizado]
- [comando2]: [cambio realizado]

User decisions implemented:
- [decision1]
- [decision2]

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

### MODE B CONTINUATION: File Generation
**Después de git commit completado** (subagent mode only - direct mode handles internally):

#### A. Narrativa Raw Generation
```python
Task(
    description="Create narrative with command changes documented",
    prompt="""Generate conversation narrative con complete command changes documentation.

NARRATIVE GENERATION:
- Target: /narratives/raw/conversations/{timestamp_mx}_{tema}.md
- Content: Complete conversation preserving exact formatting
- Command changes: All modifications documented
- User voice: Preserved exactly with attribution
- Context: Session context and outcomes included

NARRATIVE STRUCTURE:
- Conversation transcript (exact formatting preserved)
- Command changes summary
- User decisions crystallized
- Implementation commitments made
- Context for next session

EXECUTE: Create narrative file with complete documentation.""",
    subagent_type="general-purpose"
)
```

#### B. Smart Handoff Consolidation
```python
Task(
    description="Generate or update handoff using smart consolidation logic",
    prompt="""Execute SMART HANDOFF CONSOLIDATION with proliferation prevention.

CONSOLIDATION LOGIC:
PHASE 1: Check for existing daily master handoff
- Current date: $(TZ='America/Mexico_City' date +'%Y-%m-%d')
- Master handoff path: /handoff/{date}_master-consolidated.md
- IF master exists: APPEND new session to existing file
- IF master missing: CREATE new master handoff

PHASE 2: Session consolidation format
- Add session entry to SESSION INDEX (Chronological)
- Session format: "**{time}** - {theme} → {summary}"
- Preserve chronological ordering within daily timeline
- Update consolidated context sections automatically

PHASE 3: Archive management
- Check for individual handoffs in /handoff/ directory
- IF individual handoffs exist for current date:
  - CREATE /handoff/archive/{date}/ directory
  - MOVE individual handoffs to archive with session numbering
  - CREATE archive README.md with index
  - CLEAN main handoff directory

EXECUTION TARGETS:
- Master: /handoff/{date}_master-consolidated.md
- Archive: /handoff/archive/{date}/session-{nn}_{original-name}.md
- Index: /handoff/archive/{date}/README.md

CONSOLIDATION BENEFITS:
- Single daily handoff for easy tracking
- Complete session history preserved
- Clean handoff directory maintenance
- Zero information loss during consolidation

EXECUTE: Create or update master handoff with session consolidation.""",
    subagent_type="general-purpose"
)
```
Task: Architecture Validator - Crear handoff con applied changes
/handoff/[timestamp-mx]_[tema]-handoff.md
Incluyendo: changes aplicados + pending items + próximos pasos
```

#### C. Update Índices
- Conversations index updated
- Handoffs registry updated  
- Cross-references established

## Usage Patterns

### Standard User Invocation
```bash
/session-close --tema "nombre-tema"
/session-close --categoria "tecnico|personal|planning"  
/session-close --continue  # Indica continuación planeada
```

### Orchestrator Direct Execution
```bash
# Context detection automatico - no parameters needed
/session-close
# System detecta orchestrator context → direct execution mode
# Mantiene funcionalidad completa sin Task tools overhead
```

### Execution Mode Selection
- **Auto-Detection**: System detecta caller context para mode selection
- **Direct Mode**: Orchestrator context → integrated workflow execution
- **Subagent Mode**: Standard user → 4 Task tools deployment
- **Functionality**: Identical output both modes, different execution path

## Success Criteria (Both Modes)
- [ ] Conversación capturada completamente
- [ ] Command changes detected y aplicados
- [ ] Handoff generado con context preservation
- [ ] Git commit ejecutado con trazabilidad
- [ ] Índices actualizados automáticamente
- [ ] Próxima sesión setup preparado

## Mode-Specific Validation

### Direct Mode (Orchestrator)
- [ ] Context detection successful
- [ ] Integrated analysis completed
- [ ] Direct file operations executed
- [ ] No Task tool overhead

### Subagent Mode (Standard)
- [ ] 4 Task tools deployed successfully
- [ ] Specialist outputs consolidated
- [ ] Main agent coordination completed
- [ ] Full parallel analysis achieved

---

**Extensions**:
- [Proceso detallado + casos edge](./extensions/session-close-details.md)
- [Metadata extraction algorithms](./extensions/session-close-metadata.md)