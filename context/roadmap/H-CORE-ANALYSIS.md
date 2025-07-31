# HANDOFF: Análisis Completo del Comando /core

**Handoff ID**: H-CORE-ANALYSIS  
**Fecha**: 31/07/2025  
**Contexto**: Factorización de /core en subcomandos especializados

## OBJETIVO ESPECÍFICO

Realizar análisis exhaustivo del comando `/core` actual para identificar estructura factorizable, árboles de decisión, y componentes que pueden separarse en subcomandos especializados.

## ESTADO ACTUAL

- **Comando actual**: `.claude/commands/core.md` (103 líneas)
- **Restricción crítica**: Comandos NO pueden referenciar fuera de `.claude/commands/`
- **Objetivo**: Crear subcomandos ligeros con conditional loading
- **Arquitectura actual**: Protocolo híbrido de orquestación con 29 pasos

## TAREAS ESPECÍFICAS

### 1. Mapeo Estructural Completo
- **Analizar línea por línea** el comando `/core` actual
- **Identificar bloques funcionales** principales y sus responsabilidades
- **Mapear dependencias** entre diferentes secciones
- **Documentar flujo de ejecución** paso a paso

### 2. Identificación de Árboles de Decisión
- **Localizar puntos de bifurcación** en la lógica de decisión
- **Mapear conditional logic** y routing patterns
- **Identificar semantic triggers** embedded en el comando
- **Documentar decision matrices** y sus criterios

### 3. Componentes Factorizables
- **Workspace Setup** (líneas estimadas 5-15)
- **Decision Matrix** (líneas estimadas 25-50)  
- **Orchestration Protocol** (líneas estimadas 15-30)
- **Scope Management** (líneas estimadas 10-20)
- **Finalization Protocol** (líneas estimadas 20-35)
- **Automation Layer** (líneas estimadas 10-15)

### 4. Análisis de Referencias Externas
- **Identificar referencias @context/** que deben eliminarse
- **Mapear dependencias de scripts/** que necesitan hook integration
- **Documentar contexto mínimo** que debe embeberse en cada subcomando

## ENTREGABLES ESPERADOS

1. **Mapa estructural detallado** del comando `/core` actual
2. **Identificación de 6 componentes factorizables** con boundaries claros
3. **Análisis de árboles de decisión** y puntos de bifurcación
4. **Lista de dependencias externas** que requieren refactoring
5. **Contexto mínimo por componente** para autocontención

## CRITERIOS DE ÉXITO

- ✅ Estructura completa del comando documentada y analizada
- ✅ Componentes factorizables identificados con boundaries claros
- ✅ Árboles de decisión mapeados con oportunidades de optimización
- ✅ Plan claro para eliminación de referencias externas

## SIGUIENTES HANDOFFS

- **H-SCRIPTS-INVENTORY**: Inventario completo de scripts referenciados
- **H-SUBCOMMANDS-DESIGN**: Diseño de subcomandos autocontenidos

---

**CONTEXTO PARA SIGUIENTE CONVERSACIÓN**: Este handoff debe completarse con análisis exhaustivo de `/core` antes de proceder con diseño de subcomandos. El análisis determinará la estrategia exacta de factorización.