# CLAUDE.md - Dispatcher Inteligente

## AUTORIDAD SUPREMA
context/TRUTH_SOURCE.md → sobrescribe → todo lo demás

## PROJECT CONFIGURATION

**Important**: After installation, customize these paths for your project:

- Update `context/TRUTH_SOURCE.md` with your project vision
- Customize context loading patterns in REFERENCIAS CONDICIONALES
- Adjust semantic triggers for your domain requirements
- Configure enforcement rules in context/enforcement/

## CONTEXT LOADING STRUCTURE

The system expects this basic structure:
```
context/
├── TRUTH_SOURCE.md           # Project vision and authority
├── patterns/
│   ├── orchestrator_methodology.md
│   ├── simplicity.md
│   └── documentation_style.md
├── principles/
│   └── authority.md
├── templates/
│   └── template_command.md
└── enforcement/
    ├── core_reminders.md
    ├── anti_patterns.md
    ├── behavioral_enforcement.md
    └── quality_gates.md
```

---



## CONTEXTO CORE SIEMPRE CARGADO
@context/TRUTH_SOURCE.md
@context/patterns/socratic_methodology.md
@context/patterns/authority_framework.md
@context/patterns/simplicity_principles.md
@context/behaviors/orchestration_protocol.md

## COMPORTAMIENTO ORQUESTADOR
/roles:orchestrator

## DECISION LOGIC CON TRIGGERS SEMÁNTICOS

### Research/Investigation Pattern
**Semantic triggers**: Intent to understand, investigate, analyze, discover + Scope multi-source/pattern analysis + Domain technical/architectural + Output insights/recommendations
**Auto-activation**: Date-sensitive info → $(date) validation, new domain → WebSearch + MCP context 7 simultáneamente
**Execute**: Task tool → /actions:research + context/patterns/orchestrator_methodology.md
**Validate**: Task tool → alignment verification con context/TRUTH_SOURCE.md

### Documentation Pattern  
**Semantic triggers**: Intent to capture, formalize, record + Scope single doc/system-wide + Domain technical/procedural + Output formal documentation
**Auto-activation**: Decision made → auto-generate documentation, system change → update related docs
**Execute**: Task tool → /actions:build + context/templates/ + context/patterns/documentation_style.md
**Validate**: Task tool → standards compliance verification

### Architecture/System Pattern
**Semantic triggers**: Intent to change structure, improve organization + Scope system-wide implications + Domain architectural decisions + Output improved system design
**Auto-activation**: System-wide changes → context/TRUTH_SOURCE.md consultation mandatory, architecture discussion → /roles:partner validation
**Execute**: Task tool → /roles:partner + context/TRUTH_SOURCE.md + context/principles/authority.md
**Validate**: Task tool → authority alignment + simplicity preservation verification

### Development/Implementation Pattern
**Semantic triggers**: Intent to build, develop, execute + Scope multi-file operations + Domain technical implementation + Output working systems
**Auto-activation**: Code complexity >3 pasos → Task tool delegation, quality standards → template application
**Execute**: Task tool → comando apropiado (/actions:debug, /actions:explore, /actions:write) + context/patterns/simplicity.md
**Validate**: Task tool → quality standards + simplicity principles verification

### Workflow/Command Pattern
**Semantic triggers**: Intent to automate, process + Scope workflow creation + Domain procedural + Output structured commands
**Auto-activation**: "/comando" mentioned → template loading, process automation → command structure
**Execute**: Task tool → comando específico con /{folder}:{command} syntax + context/templates/template_command.md
**Validate**: Task tool → system coherence + autocontained principle verification

### Multi-Conversación Pattern
**Semantic triggers**: Intent to coordinate, orchestrate + Scope parallel execution + Domain multi-agent coordination + Output coordinated progress
**Auto-activation**: "paralelo", "múltiple" → múltiples Task tools, >5 independent tasks → parallel consideration
**Execute**: Múltiples Task tools simultáneas + usuario ultra-orchestrator coordination
**Validate**: Task tool → coordination effectiveness + background process verification

### Session Management Pattern
**Semantic triggers**: Intent to conclude, capture progress + Scope session-wide summary + Domain progress documentation + Output handoff preparation
**Auto-activation**: "cierre conversación", "handoff" → /workflows:close activation, work completion → session documentation
**Execute**: Task tool → /workflows:close + session consolidation protocol
**Validate**: Task tool → completeness + continuity preparation verification

## METODOLOGÍA ENFORCEMENT INTEGRADA

### Continuous Execution OBLIGATORIO
**Template**: "Completado [SUBTAREA] → [RESULTADO]. Continuando automáticamente con [SIGUIENTE] (progreso: X/Y)."
**NUNCA pausar** tras notificaciones esperando confirmación
**Continuar automáticamente** hasta lista tareas vacía O usuario indica STOP

### Think x4 SIEMPRE
**OBLIGATORIO aplicar** Think x4 en análisis y proposals
**NUNCA usar** "instinto", "intuition" sin systematic analysis
**Template**: Think 1-4 perspectives explícitas antes conclusión

### Parallel Tools OBLIGATORIO
**Web searches** SIEMPRE concurrentes cuando research
**Batch operations** para información independiente obligatorio
**Múltiples tools simultáneos** en single message cuando posible

### Post-Validation Sistemática
**Después cada delegación** → automatic second Task tool
**Verify alignment** context/TRUTH_SOURCE.md
**Verify compliance** context/patterns/simplicity_principles.md
**Verify standards** según context apropiado

## REFERENCIAS CONDICIONALES

**Context loading según patterns**:
- Research: context/behaviors/discovery_execution_flow.md + context/operations/methodology_protocol.md
- Documentation: context/templates/ + context/patterns/documentation_style.md  
- Architecture: context/TRUTH_SOURCE.md + context/patterns/authority_framework.md
- Implementation: context/patterns/simplicity_principles.md + context/behaviors/
- Commands: context/templates/template_command.md + context/operations/workflow_execution.md
- Validation: context/operations/quick_operations_reference.md + context/behaviors/

**Enforcement references**:
- Anti-patterns: context/enforcement/anti_patterns.md
- Behavioral: context/enforcement/behavioral_enforcement.md
- Quality gates: context/enforcement/quality_gates.md
- Semantic triggers: context/enforcement/triggers_semanticos.md

**Complete enforcement**: @context/enforcement/

---

**PRINCIPIO ESENCIAL**: Semantic recognition + Think x4 + delegation + continuous execution + systematic validation = Maximum completitud con zero friction.
