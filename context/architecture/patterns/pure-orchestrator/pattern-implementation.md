# Pattern Implementation - Anti-Patterns & Resolution Guidance

**30/07/2025 CDMX** | Implementation guidance with anti-pattern prevention

## AUTORIDAD SUPREMA
← pure-orchestrator-patterns.md (orchestration patterns authority) → pattern-implementation.md implements implementation guidance per orchestration authority

## ORCHESTRATION ANTI-PATTERNS

### Anti-Pattern 1: Direct Execution Fallback
**Problem**: Orchestrator executing tasks directly instead of delegating
**Detection**: Use of direct tools (Read, Edit, Bash) without Task tool delegation
**Resolution**: Transform all direct execution to Task tool delegation with expert configuration

### Anti-Pattern 2: Generic Subagent Deployment
**Problem**: Subagents deployed without specialized role or expert configuration
**Detection**: Task tool usage without ROL + CONTEXTO + INSTRUCCIONES template
**Resolution**: Apply obligatory expert delegation template to all subagent deployments

### Anti-Pattern 3: Sequential Default Execution
**Problem**: Default sequential subagent execution without parallel consideration
**Detection**: Single Task tool deployment when multiple independent tasks available
**Resolution**: Systematic parallel deployment analysis and implementation

### Anti-Pattern 4: Operational Instructions Neglect
**Problem**: Subagents operating without systematic methodology inheritance
**Detection**: Subagent outputs not demonstrating Think x4, WebSearch, parallel tools usage
**Resolution**: Explicit operational instructions transfer in every Task tool prompt

## INTEGRATION REFERENCES

### ← orchestration-core.md
**Connection**: Core orchestration patterns requiring anti-pattern prevention
**Protocol**: Implementation guidance prevents anti-patterns in core pattern application

### → coordination-protocols.md
**Connection**: Integration framework ensuring implementation effectiveness
**Protocol**: Implementation guidance validated through coordination protocols

### ← pure-orchestrator-patterns.md
**Authority Source**: Pure orchestrator patterns authority for implementation guidance
**Protocol**: Implementation patterns serve validated orchestration authority

---

**PATTERN IMPLEMENTATION DECLARATION**: Anti-pattern prevention and resolution guidance preserving validated orchestration authority through systematic implementation protocols.