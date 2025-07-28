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

### 2. Análisis Paralelo + Command Detection (EJECUTAR INMEDIATAMENTE)
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

### 3. Command Updates Application
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

#### B. Handoff Generation  
```python
Task(
    description="Generate handoff with applied changes documented",
    prompt="""Create comprehensive handoff con all session outcomes.

HANDOFF GENERATION:
- Target: /handoff/{timestamp_mx}_{tema}_handoff.md
- Content: Session summary + command changes applied
- Context preservation: Complete state for next session
- User voice: Key quotes and decisions preserved
- Implementation status: What was completed vs pending

HANDOFF STRUCTURE:
- Session summary and outcomes
- Command changes applied during session
- User decisions and voice preservation
- Next steps and priorities
- Context for session continuation

EXECUTE: Create handoff file with complete session documentation.""",
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