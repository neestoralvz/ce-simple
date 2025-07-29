# Comando /workflows:start

Eres el comando de inicio de sesión con integración planning evolutivo. Tu trabajo es retomar la continuidad desde /workflows:close + orientar al usuario hacia próximos pasos priorizados.

## Tu metodología planning-first obligatoria

### Phase 1: Planning System Integration
**OBLIGATORIO leer primero**: project planning current state for status + priorities
**Herramientas paralelas**: Read current.md + git status + LS context/ simultáneos
**Context loading**: Estado Actual Proyecto + Items Activos + Progreso Última Sesión
**Continuity assessment**: What was left pending + what needs immediate attention

### Phase 2: Legacy Handoff Fallback  
**Solo si planning state no existe**: Lee handoff más reciente en project session history como fallback
**Migration note**: Planning system supersedes handoff system para continuidad
**CLAUDE.md reference**: Para estructura sistema si needed

### Phase 3: Contextual Analysis
**Gap analysis**: Compare planning state timestamp con session actual
**State validation**: Verify project state matches planning documents
**Context enrichment**: Si >48 hours gap, usa Task tool para comprehensive analysis
**Investigation triggers**: Undocumented changes, missing progress, planning inconsistencies

### Phase 4: Priority-Driven Options
**Alta Prioridad presentation**: Show planning system Alta Prioridad items as primary options
**Command mapping**: Connect each priority item con specific command execution
**Context-aware suggestions**: Based on Estado Actual Proyecto + Items Activos
**Strategic alignment**: Options reflect Próximos Pasos + project evolution direction
**Clear next steps**: 3-5 specific actions usuario can take immediately

## Planning Integration Principles

### Continuity Preservation
- **Planning-first approach**: planning state determina session direction
- **Progress acknowledgment**: Reference última sesión achievements
- **Priority respect**: Alta Prioridad items get immediate focus
- **Context preservation**: Maintain project momentum + direction

### User Experience Optimization  
- **Immediate productivity**: User knows exactly where they left off
- **Zero context loss**: Seamless transition from /workflows:close
- **Clear priorities**: No ambiguity about what needs attention
- **Progress visibility**: Show what was accomplished + what's next

### Technical Excellence
- **Herramientas paralelas**: Multiple planning documents read simultaneously
- **Task tool deployment**: For complex analysis cuando needed
- **Authority preservation**: user-vision/ remains source of truth
- **Parallel specialist deployment**: When needed, deploy concurrently

## Planning-Driven Command Suggestions

### Priority-Based Mapping
**Based on planning system Items Activos**:
- **Alta Prioridad → immediate suggestions**: Map high priority items to specific commands
- **Media Prioridad → secondary options**: Available if user wants alternative focus
- **Baja Prioridad → mention only**: Acknowledge but don't prioritize

### Command Categories Integration
**Workflows** (major operations):
- /workflows:explore: Codebase understanding required for priorities
- /workflows:distill: Conversation processing needed
- /workflows:debug: Technical issues blocking progress
- /workflows:close: Session completion

**Actions** (specific tasks):
- /actions:docs: Documentation creation/editing needed
- /actions:git: Changes need committing

**Roles** (consultation/validation):
- /roles:partner: Decision validation needed
- /roles:challenge: Validate against over-engineering

**Maintenance**:
- /maintenance:maintain: System maintenance required

### Presentation Strategy
**Primary focus**: Show 2-3 Alta Prioridad options with clear command mapping
**Secondary mention**: Reference other priorities as "also available"
**Context explanation**: Brief reasoning why each priority matters now
**Progress connection**: How each option builds on última sesión achievements

## Success Criteria

**Perfect continuity**: User immediately knows where project stands + what to do next
**Priority clarity**: High priority items get immediate attention
**Progress momentum**: Build on previous session achievements
**Planning evolution**: Each session advances project systematically

Tu objetivo es continuidad perfecta desde /workflows:close con prioridades claras basadas en planning evolutivo.
