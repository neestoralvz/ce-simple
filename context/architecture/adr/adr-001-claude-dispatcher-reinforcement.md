# ADR-001: CLAUDE.md Dispatcher Optimization Through Reinforcement Vocabulary

**Date**: 30/07/2025  
**Status**: Implemented  
**Authority**: User vision → TRUTH_SOURCE.md → architecture decision

## CONTEXT
User requested conversion of CLAUDE.md "PROTOCOLO OPERACIONAL PRINCIPAL" to direct instruction format, followed by systematic application of reinforcement vocabulary throughout dispatcher logic.

## DECISION
Transform CLAUDE.md from passive protocol documentation to active behavioral programming through:
1. **Imperative Command Architecture**: Convert all instructions to direct commands (EJECUTA, APLICA, VALIDA)
2. **Criticality-Based Escalation**: Apply vocabulary hierarchy (OBLIGATORIO → MANDATORIO → CRÍTICO)
3. **Auto-Activation Reinforcement**: Enhance semantic triggers with action-specific vocabulary

## RATIONALE
**User Authority**: 
- "convierte el protocolo operacional principal en una instrucción directa"
- "de que manera podemos utilizar instrucciones y vocabulario de refuerzo?"
- "hazlo" → preference for direct action over extended analysis

**System Benefits**:
- Eliminates instruction ambiguity through imperative language
- Creates automatic behavioral compliance through linguistic authority
- Improves system responsiveness by reducing decision paralysis

## IMPLEMENTATION
**Primary Changes**:
- SIEMPRE ejecuta → EJECUTA OBLIGATORIAMENTE
- Auto-activation → Auto-activation [CRITICALITY LEVEL]
- Execute → EJECUTA, Validate → VALIDA [INTENSITY LEVEL]
- Template reinforcement with OBLIGATORIO/MANDATORIO modifiers

## CONSEQUENCES
**Positive**: Enhanced system compliance, reduced ambiguity, stronger behavioral programming
**Monitoring**: System responsiveness measurement, instruction effectiveness validation
**Evolution**: Vocabulary can be further refined based on behavioral effectiveness metrics

## INTEGRATION AUTHORITY
**← methodology.md**: Reinforcement vocabulary as core methodology pattern
**→ standards.md**: Vocabulary hierarchy as system standard
**↔ reinforcement-vocabulary-methodology.md**: Detailed methodology implementation

---
**ARCHITECTURAL DECISION**: Linguistic authority drives behavioral authority - CLAUDE.md optimized as behavioral programming system through systematic reinforcement vocabulary implementation.