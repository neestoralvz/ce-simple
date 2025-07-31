# HANDOFF: Diseño de 6 Subcomandos Especializados Autocontenidos

**Handoff ID**: H-SUBCOMMANDS-DESIGN  
**Fecha**: 31/07/2025  
**Contexto**: Factorización de /core en subcomandos ligeros con conditional loading

## OBJETIVO ESPECÍFICO

Diseñar 6 subcomandos especializados completamente autocontenidos en `.claude/commands/` que factorizen la funcionalidad del comando `/core` actual con context loading condicional.

## ESTADO ACTUAL

- **Comando /core actual**: 103 líneas con protocolo híbrido completo
- **Componentes identificados**: 6 bloques funcionales principales
- **Restricción crítica**: Zero referencias fuera de `.claude/commands/`
- **Objetivo**: Subcomandos ligeros (≤40 líneas cada uno) con context embedding

## TAREAS ESPECÍFICAS

### 1. Arquitectura de Subcomandos Propuesta

**SUBCOMANDO 1: /core-workspace**
- **Función**: Workspace resiliente setup + automation layer
- **Context embedded**: Workspace setup protocols + hook integration basics
- **Script integration**: conversation-workspace.sh integration o fallback manual
- **Tamaño objetivo**: ≤35 líneas

**SUBCOMANDO 2: /core-decision**
- **Función**: Decision matrix inteligente + routing logic
- **Context embedded**: SCOPE/RESEARCH/COMPLEJIDAD evaluation criteria
- **Logic embedded**: Matriz de decisión completa sin referencias externas
- **Tamaño objetivo**: ≤40 líneas

**SUBCOMANDO 3: /core-orchestrate**
- **Función**: Hybrid orchestration protocol + subagent coordination
- **Context embedded**: L4-Pure Orchestration + delegation templates
- **Integration**: parallel-tool-manager.sh integration o fallback
- **Tamaño objetivo**: ≤40 líneas

**SUBCOMANDO 4: /core-scope**
- **Función**: GitHub issues + scope management enhanced
- **Context embedded**: Issue creation templates + scope expansion logic
- **Script integration**: issue-detector.sh + batch-issue-create.sh integration
- **Tamaño objetivo**: ≤35 líneas

**SUBCOMANDO 5: /core-validate**
- **Función**: Post-delegation validation + quality gates
- **Context embedded**: Validation criteria + quality assurance protocols
- **Script integration**: quality-gate.sh + validate-context-coherence.sh integration
- **Tamaño objetivo**: ≤35 líneas

**SUBCOMANDO 6: /core-finalize**
- **Función**: Complete conversation finalization + context extraction
- **Context embedded**: Finalization protocols + conversation preservation
- **Script integration**: context-extract.sh integration o manual alternatives
- **Tamaño objetivo**: ≤40 líneas

### 2. Context Embedding Strategy
- **Authority principles**: Embedded Think x4, Research-first, Continuous execution
- **Core templates**: Delegation templates embebidos sin referencias
- **Fallback procedures**: Manual alternatives cuando scripts fallan
- **Validation criteria**: Quality gates embebidos en cada subcomando

### 3. Script Integration Design
- **Discovery mechanism**: Buscar scripts en `scripts/` directory
- **Fallback creation**: Auto-creation de stub scripts cuando faltan
- **Graceful degradation**: Continue workflow si scripts fallan
- **Manual alternatives**: Procedimientos manuales embebidos

### 4. Autocontención Requirements
- **Zero external references**: No `@context/` references permitidas
- **Self-contained templates**: All templates embebidos en subcomandos
- **Embedded decision logic**: Complete logic sin dependencies
- **Fallback protocols**: Manual procedures para todas las dependencies

## ENTREGABLES ESPERADOS

1. **6 subcomandos especializados** con specifications detalladas
2. **Context embedding strategy** para cada subcomando
3. **Script integration architecture** con fallback mechanisms
4. **Autocontención validation** checklist para cada subcomando

## CRITERIOS DE ÉXITO

- ✅ 6 subcomandos diseñados con boundaries claros y funcionalidad específica
- ✅ Cada subcomando ≤40 líneas con context embedding completo
- ✅ Zero referencias externas - complete autocontención
- ✅ Script integration con graceful degradation cuando fallan

## SIGUIENTES HANDOFFS

- **H-CORE-DISPATCHER**: Diseño de /core dispatcher ligero
- **H-FALLBACK-COMMAND**: Comando fallback para scripts faltantes

---

**CONTEXTO PARA SIGUIENTE CONVERSACIÓN**: Este diseño debe preservar 100% de la funcionalidad actual de /core mientras achieving modularization y conditional loading. Cada subcomando debe ser independiente pero coordinable via dispatcher.