# /modules:claude_core_integration - Core Command Embedding Logic

This module handles the integration of the complete /core command functionality within generated CLAUDE.md files.

## Core Integration Framework

### Core Command Embedding Protocol

The /core command content is embedded directly within the CLAUDE.md structure as follows:

#### 1. Protocol Definition Section
```markdown
### /core - SLASH COMMAND OBLIGATORIO UNIVERSAL
**DEFINICIÓN**: Protocolo completo de orquestación inteligente con 29 pasos sistemáticos ejecutado como slash command

**CONTENIDO DEL COMANDO**:
[FULL_CORE_COMMAND_STEPS_EMBEDDED]
```

#### 2. Complete 29-Step Protocol Embedding

Embed the complete core.md content within CLAUDE.md:

```markdown
**PROTOCOLO COMPLETO EMBEBIDO**:

🌳 WORKSPACE CONVERSACIONAL RESILIENTE:
0a. VERIFICA: mkdir -p ./.conversation-workspaces (create if missing)
0b. EJECUTA: git worktree add ./.conversation-workspaces/conv-[TIMESTAMP] HEAD
0c. FALLBACK: Si GitWorktree falla → CONTINÚA en branch actual + warning usuario
1. CAMBIA: cd ./.conversation-workspaces/conv-[TIMESTAMP] (if successful)
2. ACTIVA: export CONVERSATION_WORKSPACE=true

🪝 AUTOMATION LAYER INTEGRATION:
- PRE-TASK: Ejecutar Claude Code hooks (workspace-init, dependency-check) | FALLBACK manual si falla
- DURANTE: parallel-tool-manager.sh coordina herramientas | FALLBACK coordinación manual si falla
- POST-COMPLETION: quality-gate.sh + context-extract.sh + issue-detector.sh | FALLBACK validación manual si falla
- GIT-HOOKS: pre-commit validation, post-commit monitoring | CONTINÚA si hooks fallan

📋 PROTOCOLO HÍBRIDO DE ORQUESTACIÓN INTELIGENTE:

⚠️ NIVEL ORQUESTADOR (Claude Principal) - CAPACIDADES: Task tools, coordinación, WebSearch+MCP Context7:
1. DESPLIEGA TodoWrite task planning OBLIGATORIO como PRIMER PASO SIEMPRE
2. ACTUALIZA TodoWrite CONTINUAMENTE durante ejecución OBLIGATORIO
3. DESPLIEGA subagente especializado para explorar codebase OBLIGATORIO ANTES de cualquier acción
4. ORQUESTA búsqueda paralela via múltiples Task tools SIMULTÁNEAMENTE OBLIGATORIO
5. DELEGA análisis Think x4 de información a subagente analítico OBLIGATORIO
6. COORDINA planificación con múltiples subagentes especializados OBLIGATORIO

[... COMPLETE 29 STEPS CONTINUE ...]

🎯 CONVERSATION COMPLETION ASSESSMENT:
29a. VERIFICA: TodoWrite 100% completado - no pending/in_progress tasks OBLIGATORIO
29b. CONFIRMA: Contexto capturado exitosamente + patrones identificados OBLIGATORIO  
29c. VALIDA: Todas las tareas fuera scope convertidas a issues OBLIGATORIO
29d. EVALÚA: No errores críticos pendientes de resolución OBLIGATORIO
29e. NOTIFICA: Si 4 criterios ✅ → "🎯 CONVERSACIÓN COMPLETADA - Lista para cierre" OBLIGATORIO
29f. REPORTA: Summary metrics (tasks completed, issues created, context captured) OBLIGATORIO
```

### Project-Specific Core Adaptations

#### Path Customization Logic
```markdown
**PROJECT PATH SUBSTITUTIONS**:
- ./.conversation-workspaces/ → [PROJECT_WORKSPACE_PATH]
- context/conversations/ → [PROJECT_CONVERSATION_PATH]  
- context/data/performance/ → [PROJECT_PERFORMANCE_PATH]
- context/patterns/ → [PROJECT_PATTERNS_PATH]
```

#### Automation Layer Adaptation
```markdown
**PROJECT AUTOMATION CUSTOMIZATION**:
- workspace-init → [PROJECT_WORKSPACE_INIT_SCRIPT]
- parallel-tool-manager.sh → [PROJECT_TOOL_MANAGER]
- quality-gate.sh → [PROJECT_QUALITY_GATE]
- context-extract.sh → [PROJECT_CONTEXT_EXTRACTOR]
```

#### Workflow Integration Points
```markdown
**PROJECT WORKFLOW INTEGRATION**:
- Git workflow → Adapt to project's git strategy
- Issue creation → Integrate with project's issue tracking
- Context extraction → Match project's documentation structure
- Performance metrics → Align with project's KPIs
```

## Integration Quality Assurance

### Embedding Validation Protocol

1. **Completeness Check**: All 29 steps included in embedded version
2. **Path Resolution**: All embedded paths resolve to project structure  
3. **Command Functionality**: /core command works when called from CLAUDE.md
4. **Context Integration**: Embedded core integrates with project's @context/ architecture
5. **Fallback Verification**: All fallback mechanisms function properly

### Integration Testing Framework

```markdown
**TESTING CHECKLIST**:
□ /core command callable from generated CLAUDE.md
□ All 29 steps execute in sequence
□ TodoWrite integration functional
□ Subagent orchestration works
□ Context loading operates correctly
□ Path substitutions resolve properly
□ Automation layer integrates successfully
□ Fallback mechanisms activate when needed
□ Conversation completion assessment functions
□ Performance metrics capture works
```

## Error Handling & Fallbacks

### Integration Failure Protocols

1. **Missing Context Structure**: Generate minimal required @context/ structure
2. **Path Resolution Failure**: Use fallback paths with user notification
3. **Automation Integration Issues**: Provide manual execution alternatives
4. **Git Worktree Unavailable**: Continue in current branch with workspace isolation
5. **Hook System Missing**: Continue with manual validation checkpoints

### Graceful Degradation Strategy

```markdown
**DEGRADATION LEVELS**:
Level 1: Full automation + orchestration (optimal)
Level 2: Manual automation + full orchestration  
Level 3: Basic orchestration + manual processes
Level 4: Minimal core functionality only
```

## Usage Integration Examples

### Basic Project Integration
```markdown
# Generated CLAUDE.md includes:
- Complete embedded /core command
- Project-specific path mappings
- Appropriate semantic patterns
- Integrated automation layer
```

### Advanced Project Integration  
```markdown
# Generated CLAUDE.md includes:
- Full 29-step protocol with project customizations
- Advanced semantic pattern library
- Complex automation workflow integration
- Multi-conversation orchestration setup
```

## Success Metrics

- **✅ Protocol Completeness**: All 29 steps embedded correctly
- **✅ Path Integration**: All paths resolve to project structure
- **✅ Functionality Verification**: /core command executes successfully
- **✅ Context Coherence**: Integration maintains project context integrity
- **✅ Performance Validation**: Embedded core performs equivalently to standalone

## Evolution Capability

The embedded /core command maintains full evolution capability:
- **Organic Adaptation**: Core protocol adapts to project evolution
- **Methodology Integration**: Supports methodology refinement over time
- **Authority Preservation**: Maintains user authority supremacy throughout evolution
- **Quality Assurance**: Continuous validation of integration effectiveness

**Module Function**: Complete /core command functionality embedded within generated CLAUDE.md files with project-specific adaptations and full quality assurance.