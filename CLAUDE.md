# CLAUDE.md - Sistema de Inteligencia Simple

## AUTORIDAD SUPREMA: user-vision/

**JERARQUÍA DE VERDAD**: user-vision/TRUTH_SOURCE.md → SOBRESCRIBE → Este documento
**VALIDACIÓN OBLIGATORIA**: Alinearse con docs/maintenance/validation.md

**MISIÓN**: "lo que quiero construir es un sistema de comandos que represente el workflow que quiero, que mejor me pueda funcionar para trabajar con Claude Code"

## FILOSOFÍA FUNDAMENTAL

### Transformación Humana-AI
"Una nueva forma de trabajar con inteligencia artificial que sea más humana"
**Principio**: Conversación natural → comprensión profunda → ejecución manifestada

### Evolución Orgánica  
"Quiero que todo sea como de una manera muy orgánica"
**Flujo**: Narrativa humana → metasistema adaptativo → realidad contextual

### Simplicidad Como Belleza
"la belleza va a estar en la simplicidad"
**Balance**: Preservación granular + estructura minimalista

## METODOLOGÍA SOCRATICA

### Fase 1: Descubrimiento Sin Restricciones
"no quiero que perdamos de vista el dialogo mayeutico que al final es la manera en la que se descubre lo que es la solicitud del usuario"

**PRINCIPIO ABSOLUTO**: "La conversación socratica debe ser sin restricciones para verdadero descubrimiento"
**LIBERACIÓN**: "La economía de tokens no debería estar en la conversación"

### Fase 2: Ejecución Comandos
"Los comandos son solo la ejecución después del descubrimiento conversacional"
**Orden**: Conversación primera → comprensión → decisión usuario → comando

## COMANDOS INDEPENDIENTES (9)

`/start` `/distill` `/docs` `/explore` `/debug` `/maintain` `/git` `/partner` `/close`
→ Ver docs/workflows/commands.md para coordinación completa

**Arquitectura**: Autocontenidos + independientes + orquestación de subagentes
**ENFORCEMENT**: Slash commands SIEMPRE son Claude Code workflows, NUNCA bash

## ARQUITECTURA MODULAR

```
/.claude/commands/     (9 workflows puros)
/user-vision/         (autoridad suprema - TRUTH_SOURCE.md)  
/docs/               (módulos técnicos especializados)
/handoff/            (continuidad sesiones)
```

**Regeneración Sin Sesgo**: LLM lee TODO → genera limpio (docs/maintenance/update_rules.md)

## SISTEMA DESTILACIÓN ORGÁNICA

### Flujo Natural
Conversación → raw/ → Layer 1 (quotes) → Layer 2 (síntesis) → Layer 3 (docs) → TRUTH_SOURCE.md

### Absorción Incremental
- **Layer 1**: 6 núcleos temáticos con quotes exactos + trazabilidad
- **Layer 2**: 6 síntesis de relaciones emergentes entre núcleos  
- **Layer 3**: 4 documentos oficiales generados desde síntesis
- **TRUTH_SOURCE.md**: Autoridad suprema consolidada

**Detección**: Híbrida timestamps + listas procesadas + sampling validation

## PROHIBICIONES SISTÉMICAS

### Anti-Over-Engineering
- **DETECTAR** complejidad acumulativa proactivamente
- **SIMPLIFICAR** vs crecer sin control
- **VALIDAR** necesidad real antes de agregar

### Anti-Creación Archivos
- **NUNCA** crear reportes/tracking automático
- **PREFERIR** editar existentes vs nuevos
- **RESISTIR** sesgo AI de "documentar todo"

### Preservación Informacional
- **MANTENER** granularidad vs simplificación agresiva
- **BALANCE**: "no estoy de acuerdo, creo que de esa manera se pierde mucha informacion"

## PRINCIPIOS ARQUITECTURALES

### Comando Universal
"comando para inciiar cualqueir conversacion y que fucnione como comando universal"
**Objetivo**: Punto de entrada sin restricciones

### Orquestación Subagentes  
"la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes"

### Regeneración Limpia
"eliminar archivos y crealos desde cero bajo los lineamientos que vamos actualizando, pues si solo vamos construyendo sobre los anteriores existe demasiado sesgo"

### Calidad Workflow
"creacion, alineamiento y verificacion" para toda creación de documentos

## ENFORCEMENT CRÍTICO

**AUTHORITY VALIDATION**: User feedback shapes final approach, not AI recommendations
- Challenge system works correctly by questioning decisions
- Balance needed between simplicity and information preservation  
- Accepts structural complexity if it preserves content density
- Granular nuclei have value for organic growth and context efficiency

**AUTORIDAD FINAL**: user-vision/TRUTH_SOURCE.md sobrescribe todo conflicto
**EVOLUCIÓN**: Solo por conversación → destilación → cristalización orgánica
**VALIDACIÓN**: docs/maintenance/validation.md para toda actualización

---

**SISTEMA SIMPLE** que preserva voz del usuario + habilita evolución orgánica conversacional