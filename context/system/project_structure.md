# Project Structure - Arquitectura Sistema

**29/07/2025 11:00 CDMX** | Conocimiento arquitectural navegación

## Jerarquía autoridad

user-vision/TRUTH_SOURCE.md → CLAUDE.md → context/ → .claude/commands/ → docs/

### Authority flow
user-vision/: Fuente verdad absoluta, visión usuario, decisiones cristalizadas
CLAUDE.md: Dispatcher inteligente con decision logic integrada  
context/: Módulos técnicos, patterns, templates, información contextual
.claude/commands/: 9 comandos especializados autocontenidos
docs/: Documentación complementaria (lower priority)

## Comandos disponibles (9 workflows)

### Estructura categórica
.claude/commands/workflows/: /workflows:start /workflows:close
.claude/commands/actions/: /actions:docs /actions:git /workflows:debug /workflows:explore /expand /workflows:distill /write /roles:research  
.claude/commands/roles/: /roles:partner /roles:challenge /roles:orchestrator
.claude/commands/validations/: Quality checklists (empty - future)
.claude/commands/maintenance/: /maintain

### Función comandos
Autocontenidos: Cada comando workflow independiente completo
Delegación target: Task tool calls específicos para cada comando
Context integration: Referencias markdown según necesidades condicionales
Post-validation: Verification automática post-ejecución

## Context/ arquitectura

### Módulos core
context/patterns/: orchestrator_methodology.md, simplicity.md, documentation_style.md
context/principles/: authority.md, methodology.md, vision.md
context/templates/: template_command.md, template_context_module.md, template_decision.md, template_research.md
context/project_structure.md: Este archivo - conocimiento arquitectural

### Módulos especializados
context/decisions/: Decisiones arquitecturales cristalizadas
context/roles:research/: Investigation results, domain-specific analyses
context/examples/: Usage patterns, concurrent patterns
context/raw/: Conversaciones raw para destilación futura

## Context loading patterns

### Loading condicional (markdown links)
Research: context/roles:research/ + context/patterns/orchestrator_methodology.md
Documentation: context/templates/ + context/patterns/documentation_style.md  
Architecture: user-vision/TRUTH_SOURCE.md + context/principles/authority.md
Commands: context/templates/template_command.md + .claude/commands/
Validation: context/decisions/ + domain-specific patterns

### Loading efficiency
Just-in-time: Solo módulos relevantes para situación específica
**ANTI-PATTERN:** Preventive loading, cargar context/ completo innecesariamente
**CORRECTO:** Dynamic references via CLAUDE.md decision logic según pattern recognition

## Git worktrees multi-conversación

### Architecture support
Parallel conversations: Via git worktrees para isolation
State coordination: Shared via context/ + user-vision/
Background processes: Inter-conversation tickets system
User ultra-orchestration: N parallel agents coordinados por usuario

### Integration patterns
Shared authority: user-vision/TRUTH_SOURCE.md consistent across worktrees
Context sync: context/ updates propagate across conversations
Command isolation: Each conversation puede usar commands/ independently
Result consolidation: Via shared_state/ + handoff/ mechanisms

## System evolution

### Organic growth patterns
Context expansion: New modules según necessidades emergentes
Command evolution: 9 comandos pueden grow functionality dentro autocontained principle
Template evolution: Based on usage patterns y user feedback
Decision crystallization: New decisions → context/decisions/ automatically

### Maintenance patterns  
Regular validation: Via /maintain command systemic health checks
Template updates: Según context/patterns/documentation_style.md changes
Decision review: Periodic alignment con user-vision/TRUTH_SOURCE.md
Simplicity enforcement: Via /roles:partner + /roles:challenge systematic review

---

## Enlaces → información complementaria
**Si necesitas orchestrator role**: → .claude/commands/roles/roles:orchestrator.md
**Si requieres command details**: → .claude/commands/ (specific directories)
**Si necesitas authority**: → user-vision/TRUTH_SOURCE.md
**Si requieres patterns**: → context/patterns/