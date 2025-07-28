---
contextflow:
  purpose: "Session starter universal con auto-loading de handoffs"
  triggers: ["inicio de sesión", "continuidad entre sesiones", "contexto perdido"]
  next: ["analyze", "implement", "explore", "refactor", "extract-insights", "process-layer"]
  communication-rules:
    - "NUNCA bash echo para comunicar con usuario"
    - "SIEMPRE Task tools → Main agent → Usuario"
    - "Parallel Task tools obligatorio en mismo mensaje"
    - "Subagents NUNCA comunican directamente"
  decision-tree:
    use-when: 
      - "Primera interacción de la sesión"
      - "Usuario necesita orientación sobre qué hacer"
      - "Continuidad desde sesión anterior requerida"
    alternatives: ["meta-narrative", "explore"]
    load-context: ["@/handoff/[más-reciente].md", "@/.claude/commands/"]
    semantic-triggers:
      - "empezar" / "iniciar" / "comenzar"
      - "qué sigue" / "continuar" / "seguir"
      - "contexto" / "dónde estaba" / "estado actual"
---

# Comando Universal `/start`

## Git Status Check + Context Loading
**EJECUTAR PRIMERO - Git workflow obligatorio**:

### 1. Git Repository Health Check
```bash
# Check git status para cambios uncommitted
git status

# Pull latest changes si es colaborativo
git pull origin main

# Identify any conflicts o pending changes
git log --oneline -5  # Ver commits recientes
```

## Auto-Loading Handoffs
**DESPUÉS de git check - via Task tool**:
```
Task: Research Specialist
Description: "Auto-load handoff + git analysis"
Prompt: "
1. Encontrar handoff más reciente en /handoff/ usando timestamp
2. Cargar contenido completo del handoff
3. Analizar git log reciente para context de changes
4. Identificar discrepancias entre handoff y git state
5. Preparar context summary completo para continuidad
"
```

## Análisis Contextual Inteligente

### 1. Load Último Handoff + Parse Secciones Clave
- "Próximos Pasos Inmediatos" → Tareas pendientes
- "Estado Actual Completado" → Trabajo ya hecho  
- "User Profile Refinado" → Preferencias
- "Contexto para Próxima Sesión" → Continuidad

### 2. Project Maintenance + Analysis Paralelo (EJECUTAR INMEDIATAMENTE)
**TASK TOOLS DEPLOYMENT**: 4 specialists concurrentes para comprehensive project analysis:

```python
# TASK 1: Research Specialist
Task(
    description="Project maintenance analysis with git integration",
    prompt="""Actúa como Research Specialist. PROJECT MAINTENANCE MISSION: Comprehensive analysis.

PROJECT ANALYSIS SCOPE:
- Handoff content: {latest_handoff_content}
- Git status: {current_git_status}
- Recent commits: {git_log_recent}
- System state: Current project architecture

ANALYSIS OBJECTIVES:
1. Pending Items Detection:
   - Unfulfilled commitments desde handoffs anteriores
   - Incomplete TODOs acumulados
   - Command gaps entre mentions y implementation
   - Git inconsistencies entre promises y actual commits
   - Uncommitted changes analysis

2. System Health Assessment:
   - Command ecosystem integrity
   - Rules system compliance
   - Documentation consistency
   - Architecture coherence

OUTPUT: Detailed maintenance report con priority recommendations.""",
    subagent_type="general-purpose"
)

# TASK 2: Architecture Validator
Task(
    description="Command compliance and system integrity analysis",
    prompt="""Actúa como Architecture Validator. SYSTEM INTEGRITY MISSION: Validate architectural coherence.

SYSTEM VALIDATION SCOPE:
- Command ecosystem: All commands in /.claude/commands/
- Rules system: Current rules architecture
- Git history: Recent changes and their architectural impact
- Integration points: Cross-system dependencies

VALIDATION CHECKLIST:
1. Command Compliance:
   - All commands follow established patterns
   - Contextflow metadata complete + accurate
   - Decision trees properly implemented
   - Integration patterns consistent

2. System Architecture:
   - No conflicts between commands/rules
   - Proper separation of concerns
   - Consistent naming conventions
   - Cross-reference integrity

3. Git Workflow Compliance:
   - Commit patterns follow standards
   - Branch strategy alignment
   - Change documentation completeness

OUTPUT: Architecture compliance report con specific corrections needed.""",
    subagent_type="general-purpose"
)

# TASK 3: Content Optimizer
Task(
    description="Auto-extract insights and correlate with commits",
    prompt="""Actúa como Content Optimizer. INSIGHTS EXTRACTION MISSION: Process conversation patterns.

INSIGHTS ANALYSIS SCOPE:
- Conversations pool: /narratives/raw/conversations/
- Git commits: Correlation between insights and implementations
- User voice evolution: Pattern tracking over time
- System improvements: Methodology refinements identified

EXTRACTION OBJECTIVES:
1. Pattern Recognition:
   - Emergent user preferences
   - Methodology evolution patterns
   - System usage optimization opportunities
   - Architecture improvement insights

2. Git Correlation Analysis:
   - Match insights to actual implementations
   - Identify implementation gaps
   - Track promise fulfillment rates
   - Measure system evolution effectiveness

3. User Voice Tracking:
   - Evolution in user communication patterns
   - Preference refinements over time
   - Feedback integration effectiveness

OUTPUT: Insights summary con implementation correlation + recommendations.""",
    subagent_type="general-purpose"
)

# TASK 4: Quality Assurance
Task(
    description="System evolution opportunities assessment",
    prompt="""Actúa como Quality Assurance Specialist. EVOLUTION OPPORTUNITIES MISSION: Identify improvements.

QUALITY ASSESSMENT SCOPE:
- System performance: Current efficiency metrics
- User experience: Workflow effectiveness
- Git workflow: Compliance and optimization opportunities
- Architecture evolution: Next-level improvements

QUALITY ANALYSIS:
1. Performance Optimization:
   - Token economy efficiency
   - Context loading optimization
   - Command execution efficiency
   - Workflow automation opportunities

2. User Experience Enhancement:
   - Navigation improvements
   - Workflow simplification opportunities
   - Error handling optimization
   - Documentation accessibility

3. System Architecture Evolution:
   - Next-generation architecture patterns
   - Integration simplification opportunities
   - Maintenance burden reduction
   - Scalability improvements

OUTPUT: Evolution roadmap con prioritized improvement opportunities.""",
    subagent_type="general-purpose"
)
```

### 3. Project Health Assessment
**MAIN AGENT CONSOLIDATION**: Receive outputs from 4 specialists → Synthesize comprehensive project status → Generate intelligent priority-based options:

#### A. Pending Items Tracking
- **Unfulfilled commitments** desde handoffs anteriores
- **Incomplete TODOs** acumulados  
- **Command gaps** entre menciones y implementation
- **System drift** detectado por `/supervise-alignment`
- **Git inconsistencies** entre handoff promises y actual commits
- **Uncommitted changes** que pueden indicate work in progress

#### B. Insights Processing
- **Patterns emergentes** de conversations pool
- **User voice evolution** tracking
- **Methodology refinements** identificados
- **Architecture improvements** sugeridos

### 4. Intelligent Options Generation
**Based on maintenance + insights analysis**:
- **Priority 1**: Critical gaps/commitments que requieren attention inmediata
- **Priority 2**: System evolution opportunities basados en insights
- **Priority 3**: Optimization improvements para efficiency

## Casos Edge
- **Sin handoff**: Análisis proyecto + opciones básicas
- **Handoff antiguo**: Combinar contexto + actualización
- **Múltiples handoffs**: Priorizar más reciente

## Success Criteria
- [ ] Handoff más reciente cargado automáticamente
- [ ] Opciones basadas en contexto real + comandos disponibles
- [ ] Continuidad preservada entre sesiones
- [ ] Processing pendiente detectado automáticamente

---

**Extensions**: 
- [Casos edge detallados](./extensions/start-edge-cases.md)
- [Context loading strategy](./extensions/start-context-loading.md)