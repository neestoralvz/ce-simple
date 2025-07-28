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

### 2. Project Maintenance + Analysis Paralelo
**EJECUTAR simultáneamente en mismo mensaje**:
```
Task 1: Research Specialist - "Project maintenance - gaps, TODOs, commitments + git status analysis"
Task 2: Architecture Validator - "Command compliance + system integrity + git history review"  
Task 3: Content Optimizer - "Auto-extract insights de conversations + correlate with git commits"
Task 4: Quality Assurance - "System evolution opportunities + git workflow compliance"
```

### 3. Project Health Assessment
**Main agent evalúa project status basado en subagent analysis**:

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