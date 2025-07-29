# CLAUDE.md - Sistema de Inteligencia Simple

## AUTORIDAD SUPREMA: user-vision/

**JERARQUÍA DE VERDAD**: user-vision/TRUTH_SOURCE.md → SOBRESCRIBE → Este documento
**VALIDACIÓN OBLIGATORIA**: Alinearse con docs/maintenance/validation.md

## PRINCIPIOS FUNDAMENTALES

**Socrática expansiva** + **Preservación de voz** + **Detección sistémica proactiva**
→ Ver docs/core/principles.md para metodología completa

**MISIÓN**: Conversación libre → Comprensión profunda → Ejecución optimizada
**AUTORIDAD**: user-vision/ = fuente de verdad absoluta con citas exactas

## COMANDOS INDEPENDIENTES (9)

`/start` `/distill` `/docs` `/explore` `/debug` `/maintain` `/git` `/partner` `/close`
→ Ver docs/workflows/commands.md para filosofía y coordinación completa

**Cada comando**: Instrucciones puras + Sin metadata + Propósito único + Independiente
**Coordinación**: docs/workflows/coordination.md

**ENFORCEMENT CRÍTICO**: Slash commands (`/start`, `/git`, etc.) SIEMPRE son Claude Code workflows, NUNCA bash commands

## ARQUITECTURA MINIMALISTA

```
/.claude/commands/     (9 workflows)
/user-vision/         (autoridad suprema)  
/docs/               (módulos técnicos)
/handoff/            (continuidad)
```
→ Ver docs/core/architecture.md para estructura completa

**Imports condicionales**: TRUTH_SOURCE.md (siempre) + layer3/ (contextual)

## FILOSOFÍA ESENCIAL

### Conversación Primera
"la idea por ahora no debe ser la de hacer cosas, sino la de seguir conversando"
**Flujo**: Conversación natural → Insights → Decisiones del usuario

### Simplicidad Rector  
"la belleza va a estar en la simplicidad"
**Principio**: Menos partes móviles = Mayor confiabilidad + enfoque claro

### Evolución Orgánica
Conversación → raw/ → /distill → Layer destilación → TRUTH_SOURCE.md → Sistema adaptación

## PROHIBICIONES SISTÉMICAS

### Anti-Creación Archivos
- **NUNCA** crear reportes/tracking automático
- **SOLO** cuando usuario solicita explícitamente  
- **PREFERIR** editar existentes vs crear nuevos
- **RESISTIR** sesgo AI de "documentar todo"

### Anti-Over-Engineering
- **DETECTAR** complejidad acumulativa automáticamente
- **SIMPLIFICAR** continuamente vs crecer sin control
- **VALIDAR** necesidad real antes de agregar

## SISTEMA MODULAR

**CLAUDE.md**: Ultra-denso (≤200 líneas) + Referencias modulares
**docs/**: Contenido técnico especializado  
**Regeneración**: LLM lee TODO → genera limpio sin sesgo

→ Ver docs/maintenance/update_rules.md para proceso completo

## AUTORIDAD FINAL

**user-vision/TRUTH_SOURCE.md** = Autoridad suprema que sobrescribe todo
**Cuando conflicto**: La visión del usuario siempre gana
**Evolución**: Solo por conversación → destilación → cristalización

---

**SISTEMA SIMPLE** que preserva voz del usuario + habilita evolución orgánica conversacional