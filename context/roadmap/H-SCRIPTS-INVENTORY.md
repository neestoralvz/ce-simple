# HANDOFF: Inventario Completo de Scripts Referenciados

**Handoff ID**: H-SCRIPTS-INVENTORY  
**Fecha**: 31/07/2025  
**Contexto**: Hook Integration Strategy para subcomandos /core

## OBJETIVO ESPECÍFICO

Realizar inventario exhaustivo de todos los scripts referenciados en `.claude/commands/` para entender su funcionalidad y determinar estrategia de hook integration.

## ESTADO ACTUAL

- **Scripts identificados**: 8+ scripts en `scripts/` directory
- **Scripts recientemente modificados**: analyze_violations.sh, validate-context-coherence.sh, context-extract.sh, parallel-tool-manager.sh, conversation-workspace.sh, quality-gate.sh, issue-detector.sh, batch-issue-create.sh
- **Objetivo**: Convertir scripts apropiados en Claude hooks o git hooks
- **Restricción**: Comandos deben ser autocontenidos en `.claude/commands/`

## TAREAS ESPECÍFICAS

### 1. Inventario Completo de Scripts
- **Buscar todas las referencias a scripts/** en `.claude/commands/`
- **Catalogar cada script** y su función específica
- **Documentar dependencias** y parámetros de cada script
- **Identificar scripts faltantes** que están referenciados pero no existen

### 2. Análisis Funcional por Script
- **analyze_violations.sh**: File size violation analysis para PHASE_0_EMERGENCY
- **validate-context-coherence.sh**: Context coherence validation para CLAUDE.md protocol step 28.5
- **context-extract.sh**: Conversation insights extraction para system evolution
- **parallel-tool-manager.sh**: Coordination system para parallel tool execution
- **conversation-workspace.sh**: Git worktree-based conversation isolation
- **quality-gate.sh**: Quality assurance validation (requiere análisis)
- **issue-detector.sh**: Automatic GitHub issue detection and creation
- **batch-issue-create.sh**: Parallel GitHub issue creation

### 3. Clasificación por Tipo de Integración
**Claude Hooks Candidates**:
- Scripts que deben ejecutarse en lifecycle events (pre/post conversation)
- Scripts de validation que deben ejecutarse automáticamente
- Scripts de context management

**Git Hooks Candidates**:
- Scripts de validation que deben ejecutarse en git operations
- Scripts de quality gates para commits

**Utility Scripts**:
- Scripts que deben permanecer como utilities invocados por comandos
- Scripts de batch processing

### 4. Análisis de Dependencias
- **Identificar scripts que dependen de otros scripts**
- **Mapear external dependencies** (gh, git, etc.)
- **Documentar fallback strategies** cuando scripts fallan
- **Identificar scripts que pueden ser embebidos en comandos**

## ENTREGABLES ESPERADOS

1. **Catálogo completo de scripts** con funcionalidad detallada
2. **Clasificación por tipo de hook integration** (Claude/Git/Utility)
3. **Mapa de dependencias** entre scripts y external tools
4. **Lista de scripts faltantes** que necesitan crearse
5. **Estrategia de fallback** para cada script

## CRITERIOS DE ÉXITO

- ✅ Todos los scripts catalogados con función clara documentada
- ✅ Clasificación clara para hook integration strategy
- ✅ Dependencias mapeadas con fallback strategies
- ✅ Scripts faltantes identificados con especificaciones

## SIGUIENTES HANDOFFS

- **H-SCRIPTS-CLASSIFICATION**: Clasificación detallada de scripts para hooks
- **H-HOOK-INTEGRATION**: Implementación de hook system

---

**CONTEXTO PARA SIGUIENTE CONVERSACIÓN**: Este inventario es crítico para entender qué scripts pueden convertirse en hooks automáticos vs cuáles deben permanecer como utilities. La clasificación determinará la arquitectura final del sistema.