# Decisión: Arquitectura Core Loading CLAUDE.md

**29/07/2025 10:15 CDMX** | Decisión @-syntax vs referencias condicionales

## Problema Arquitectural

Usuario identificó necesidad clarificar qué archivos deben estar SIEMPRE cargados (@-syntax) vs disponibles condicionalmente (markdown links) en CLAUDE.md.

### Criterios Decisión Aplicados

**Para @-syntax (Auto-carga)**:
- Información que SIEMPRE se necesita para funcionamiento correcto
- Prevención errores críticos operacionales  
- Autoridad fundamental nunca puede faltar
- Comportamientos obligatorios para todas las decisiones

**Para referencias condicionales**:
- Información técnica específica usada ocasionalmente
- Knowledge base navegacional disponible just-in-time
- Frameworks complejos para situaciones específicas
- Información ya cubierta en archivos @-syntax

## Decisión Arquitectural Implementada

### 4 Archivos @-syntax CRÍTICOS (siempre cargados)

**@user-vision/TRUTH_SOURCE.md**
- Autoridad suprema absoluta con 95% fidelidad quotes usuario
- SOBRESCRIBE todo lo demás - jerarquía explícita
- Principios fundamentales nunca pueden faltar
- Framework autoridad previene deriva sistémica

**@context/patterns/orchestrator_methodology.md**  
- Metodología operacional fundamental - CÓMO debe comportarse agente
- Principio Core "Delegar, No Ejecutar" - comportamiento crítico obligatorio
- Anti-patterns críticos - prevención errores operacionales graves
- Ejecución continua obligatoria - flujo trabajo fundamental

**@context/principles/authority.md**
- Marco decisional presente en TODAS las decisiones
- Golden Authority Rule - división clara Usuario/AI domains
- Challenge system validation - balance automático
- Jerarquía suprema autoridad - navegación crítica

**@context/patterns/simplicity.md**
- Principio arquitectural fundamental usuario
- "Simplicidad como belleza" - filosofía core guía todas decisiones
- Balance information vs simplification - criterio crítico
- Anti-over-engineering - prevención deriva sistémica

### Referencias Condicionales (markdown links)

**context/patterns/documentation_style.md**: Solo cuando documenting/writing
**context/project_structure.md**: Solo cuando navigating arquitectura
**context/templates/**: Solo cuando creating new content
**docs/**: Solo para consulta técnica específica

## Balance Logrado

**400 líneas críticas siempre cargadas** vs **1000+ líneas disponibles just-in-time**

### Beneficios Arquitecturales
- Autoridad siempre presente: TRUTH_SOURCE.md alineamiento continuo
- Operación sin errores: orchestrator_methodology.md previene anti-patterns críticos  
- Decisiones correctas: authority.md + simplicity.md guían todas elecciones
- Eficiencia contextual: Información técnica disponible cuando se necesita

### Principio Fundamental
Agente principal tiene fundamentos críticos siempre presentes + acceso información especializada just-in-time, manteniendo balance capabilities vs economy.

## Sintaxis Diferenciación

**@-syntax**: Auto-carga contexto inmediatamente
**Slash command reference**: Para ejecutar/cargar comando específico (/roles:orchestrator)
**Markdown links**: Referencias condicionales cargadas según patrón decision

---

## Enlaces → información complementaria
**Si necesitas implementation**: → CLAUDE.md (archivo actualizado con esta arquitectura)
**Si requieres methodology**: → context/patterns/orchestrator_methodology.md
**Si necesitas authority framework**: → context/principles/authority.md