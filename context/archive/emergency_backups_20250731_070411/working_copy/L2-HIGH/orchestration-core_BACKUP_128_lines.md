# Orchestration Core - Validated AI Agent Coordination Patterns

**30/07/2025 CDMX** | Core orchestration patterns with validation authority

## AUTORIDAD SUPREMA
← pure-orchestrator-patterns.md (orchestration patterns authority) → orchestration-core.md implements core patterns per validated orchestration authority

## PATTERN VALIDATION AUTHORITY

> "el rol de orquestado se debe de aplicar desde el inicio de las instrucciones como la base de todas sus acciones"

**Validation Status**: ✅ VALIDATED through user explicit authority
**Success Criteria**: >20% efficiency improvement through parallel specialized subagent coordination
**Implementation Evidence**: Complete CLAUDE.md transformation to pure orchestration protocol

## CORE ORCHESTRATION PATTERNS

### Pattern 1: Expert Delegation Template
**Problem**: Subagents deployed without proper role, context, or expertise configuration
**Solution**: Obligatory template ensuring expert-level subagent configuration

```yaml
Pattern: Expert Delegation
Template: 
  description: "[ESPECIALIZACIÓN ESPECÍFICA] para [OBJETIVO TÉCNICO PRECISO] (3-5 palabras)"
  prompt: |
    ROL: Actúa como [EXPERTISE ESPECÍFICA] experto en [DOMINIO].
    CONTEXTO: [CONTEXTO RELEVANTE COMPLETO + @referencias necesarias].
    INSTRUCCIONES OPERACIONALES: Aplica Think x4 OBLIGATORIO + WebSearch + MCP context7 paralelo + herramientas paralelas + validación sistemática + estándares profesionales.
    TAREA ESPECÍFICA: [OBJETIVO DETALLADO CON CRITERIOS DE ÉXITO].
  subagent_type: general-purpose
Success_Metrics: Expert-level output from specialized subagents
Anti_Pattern: Generic task delegation without role/context specification
```

### Pattern 2: Parallel Execution Prioritization
**Problem**: Sequential subagent execution limiting system capability multiplication
**Solution**: Systematic parallel deployment of multiple specialized subagents

```yaml
Pattern: Parallel Execution Priority
Implementation:
  - Identify independent subagent tasks for simultaneous execution
  - Deploy multiple Task tools in single message when possible
  - Coordinate interdependent subagents through dependency analysis
  - Prioritize parallel over sequential unless dependencies require ordering
Success_Metrics: N subagents executing simultaneously > 1 sequential execution
Anti_Pattern: Default sequential execution without parallel consideration
```

### Pattern 3: Operational Instructions Inheritance
**Problem**: Subagents not inheriting systematic methodology from main orchestrator
**Solution**: Complete operational instructions transfer to every subagent

```yaml
Pattern: Operational Inheritance
Mandatory_Transfer:
  - Think x4 systematic analysis OBLIGATORIO
  - WebSearch + MCP context7 parallel research SIEMPRE
  - Herramientas paralelas y batch operations usage
  - Validación sistemática post-execution
  - Compliance con estándares profesionales
  - TodoWrite para subtareas cuando aplicable
Success_Metrics: Subagents demonstrate systematic methodology compliance
Anti_Pattern: Subagents operating without methodology inheritance
```

### Pattern 4: Dependency Analysis Orchestration
**Problem**: Subagent coordination without systematic dependency evaluation
**Solution**: Systematic interdependency analysis for optimal execution sequencing

```yaml
Pattern: Dependency Analysis
Process:
  1. Map all subagent task interdependencies before deployment
  2. Identify critical path for dependent task sequences
  3. Optimize parallel execution for independent tasks
  4. Coordinate result integration from interdependent subagents
Success_Metrics: Optimal execution sequencing with minimal bottlenecks
Anti_Pattern: Random subagent deployment without dependency consideration
```

### Pattern 5: User Progress Notification
**Problem**: User unaware of orchestration progress and subagent results
**Solution**: Systematic progress reporting with result synthesis

```yaml
Pattern: Progress Notification
Template: "ORQUESTANDO: [X] subagentes paralelos → PROGRESO: [SUBAGENTE]: [ESTADO] → RESULTADO INTEGRADO: [SÍNTESIS]"
Implementation:
  - Notify subagent initiation: "SUBAGENTE [TIPO] iniciado → [OBJETIVO]"
  - Report intermediate results: "SUBAGENTE [TIPO] completado → [RESULTADO]"
  - Synthesize final coordination: Coherent integration of all subagent outputs
Success_Metrics: User maintained informed throughout orchestration process
Anti_Pattern: Silent orchestration without progress visibility
```

### Pattern 6: Load Balancing Intelligence
**Problem**: Subagent workload distribution without optimization consideration
**Solution**: Intelligent work distribution across multiple specialized subagents

```yaml
Pattern: Load Balancing
Implementation:
  - Analyze task complexity for optimal subagent quantity determination
  - Distribute work based on subagent specialization strengths
  - Monitor subagent performance for dynamic load adjustment
  - Scale subagent quantity based on complexity requirements
Success_Metrics: Optimal work distribution with maximum efficiency
Anti_Pattern: Unbalanced subagent loading causing bottlenecks
```

## INTEGRATION REFERENCES

### → pattern-implementation.md
**Connection**: Anti-patterns and implementation guidance for core orchestration patterns
**Protocol**: Core patterns validated through implementation and anti-pattern prevention

### → coordination-protocols.md
**Connection**: Integration framework and evolution protocols for core patterns
**Protocol**: Core patterns integrated through systematic coordination protocols

### ← pure-orchestrator-patterns.md
**Authority Source**: Pure orchestrator patterns authority for core orchestration
**Protocol**: Core patterns implement validated orchestration authority

---

**ORCHESTRATION CORE DECLARATION**: Validated core patterns implementing user explicit authority for pure AI agent orchestration through expert specialized subagent coordination with exponential capability multiplication.