# HANDOFF: Desarrollo de /core Dispatcher Ligero

**Handoff ID**: H-CORE-DISPATCHER  
**Fecha**: 31/07/2025  
**Contexto**: Core dispatcher con routing inteligente a subcomandos especializados

## OBJETIVO ESPECÍFICO

Desarrollar un nuevo comando `/core` ligero (≤30 líneas) que funcione como dispatcher inteligente, detectando semantic patterns y routing a subcomandos especializados apropiados.

## ESTADO ACTUAL

- **/core actual**: 103 líneas monolíticas con protocolo completo
- **6 subcomandos diseñados**: /core-workspace, /core-decision, /core-orchestrate, /core-scope, /core-validate, /core-finalize
- **Objetivo**: Dispatcher que preserve funcionalidad con routing inteligente
- **Restricción**: Autocontenido en `.claude/commands/` sin referencias externas

## TAREAS ESPECÍFICAS

### 1. Diseño del Dispatcher Architecture

**CORE DISPATCHER LOGIC** (≤30 líneas):
```
1. Semantic pattern detection (embedded logic)
2. Context analysis para routing decision
3. Subcommand invocation con parameters
4. Fallback a protocolo completo si routing falla
5. Error handling con graceful degradation
```

**Routing Decision Matrix**:
- **Simple tasks** (1 archivo, basic edits) → Direct execution embedded
- **Workspace setup needed** → /core-workspace
- **Complex decision making** → /core-decision → /core-orchestrate
- **Scope expansion detected** → /core-scope
- **Validation required** → /core-validate
- **Conversation finalization** → /core-finalize

### 2. Semantic Pattern Recognition (Embedded)

**Pattern Detection Logic**:
- **Keywords analysis**: "research", "implement", "create", "analyze", etc.
- **Context clues**: File count, complexity indicators, scope keywords
- **User intent analysis**: Question vs task vs exploration patterns
- **Fallback routing**: Default a /core-orchestrate para complex cases

**Routing Examples**:
- "Analyze /core command" → /core-decision (analysis focus)
- "Implement feature X" → /core-orchestrate (implementation focus)
- "Create GitHub issues" → /core-scope (scope management focus)
- "Setup workspace" → /core-workspace (workspace focus)

### 3. Subcommand Integration Protocol

**Invocation Strategy**:
- **Parameter passing**: Pass relevant context/parameters a subcomandos
- **State preservation**: Maintain conversation state across subcommands
- **Error propagation**: Handle subcommand failures gracefully
- **Fallback execution**: Execute original protocol si subcommands fallan

**Integration Requirements**:
- **Subcommand discovery**: Check for subcommand existence
- **Auto-creation**: Create missing subcommands con stub functionality
- **Graceful degradation**: Continue con embedded logic si subcommands unavailable

### 4. Fallback Protocol Embedded

**Complete Fallback Logic** (embedded en dispatcher):
- **Minimal protocol**: TodoWrite + basic orchestration + Think x4
- **Essential operations**: Core functionality sin dependencies
- **Manual alternatives**: User-guided execution cuando automation falla
- **Recovery procedures**: Reset y restart mechanisms

### 5. Dispatcher Specifications

**Input Processing**:
- Analyze user request for routing cues
- Detect complexity level y scope requirements
- Identify primary workflow type (research/implement/analyze/create)

**Output Coordination**:
- Invoke appropriate subcommand with context
- Monitor subcommand execution
- Coordinate multi-subcommand workflows when needed
- Handle final result synthesis

## ENTREGABLES ESPERADOS

1. **Dispatcher ligero** (≤30 líneas) con routing inteligente
2. **Pattern recognition logic** embedded sin external dependencies
3. **Subcommand integration protocol** con parameter passing
4. **Complete fallback protocol** embedded para reliability

## CRITERIOS DE ÉXITO

- ✅ Dispatcher ≤30 líneas preservando funcionalidad completa
- ✅ Routing inteligente basado en semantic pattern recognition
- ✅ Integration seamless con 6 subcomandos especializados
- ✅ Fallback completo cuando subcommands unavailable

## SIGUIENTES HANDOFFS

- **H-FALLBACK-COMMAND**: Comando fallback para scripts faltantes
- **H-HOOK-INTEGRATION**: Hook system integration

---

**CONTEXTO PARA SIGUIENTE CONVERSACIÓN**: Este dispatcher debe ser el entry point único que preserve toda la funcionalidad de /core actual mientras enabling modular execution. El routing debe ser inteligente pero simple, con fallback robusto.