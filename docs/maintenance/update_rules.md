# Reglas Estrictas para Actualización de CLAUDE.md

## AUTORIDAD SUPREMA

**JERARQUÍA ABSOLUTA**: `user-vision/TRUTH_SOURCE.md` → SOBRESCRIBE → CLAUDE.md → docs/ → todo lo demás

**PRINCIPIO FUNDAMENTAL**: CLAUDE.md debe ser **ultra-denso, sin sesgo, modular** y **100% alineado con la visión original**.

## REGLAS INMUTABLES

### 1. REGENERACIÓN SIN SESGO (OBLIGATORIO)
- **NUNCA** editar CLAUDE.md incrementalmente
- **SIEMPRE** regenerar desde cero usando LLM que lee:
  - `user-vision/TRUTH_SOURCE.md` (autoridad suprema)
  - Layer 3 completo (methodology, architecture, implementation, reference)
  - Contexto completo del sistema
- **PROCESO**: LLM procesa todo → genera CLAUDE.md limpio sin sesgo acumulativo

### 2. ULTRA-DENSIDAD (TAMAÑO CONTROLADO)
- **MÁXIMO**: 200 líneas efectivas (excluyendo espacios y comentarios)
- **PRINCIPIO**: Máximo impacto, mínimas palabras
- **TÉCNICA**: Referencias modulares vs duplicación de contenido
- **VALIDACIÓN**: Si excede límite → modularizar más agresivamente

### 3. MODULARIZACIÓN OBLIGATORIA
- **CONTENIDO TÉCNICO** → docs/core/, docs/workflows/, docs/maintenance/
- **CLAUDE.md CONTIENE**:
  - Autoridad y jerarquía (user-vision/)
  - Principios fundamentales (ultra-densos)
  - Referencias a módulos docs/
  - Prohibiciones sistémicas
  - Filosofía esencial
- **NO CONTIENE**: Detalles técnicos, procedimientos específicos, ejemplos extensos

### 4. PRESERVACIÓN DE VISIÓN ORIGINAL
- **VALIDACIÓN OBLIGATORIA**: Cada regeneración debe pasar checker de alineación
- **CRITERIOS DE VALIDACIÓN**:
  - ¿Respeta metodología socrática expansiva?
  - ¿Preserva jerarquía user-vision/ como autoridad suprema?
  - ¿Mantiene enfoque en simplicidad y anti-over-engineering?
  - ¿Refleja decisiones cristalizadas del usuario?
- **RECHAZO AUTOMÁTICO**: Si no alinea con TRUTH_SOURCE.md

### 5. ESTRUCTURA FIJA OBLIGATORIA

```markdown
# CLAUDE.md - Sistema de Inteligencia Simple

## AUTORIDAD SUPREMA: user-vision/
**JERARQUÍA DE VERDAD**: user-vision/ → SOBRESCRIBE → Este documento
**VALIDACIÓN OBLIGATORIA**: → Referencia a docs/maintenance/validation.md

## PRINCIPIOS FUNDAMENTALES
→ Referencias ultra-densas a docs/core/

## METODOLOGÍA CORE
→ Referencias a docs/workflows/

## ARQUITECTURA MINIMALISTA
→ Referencias a docs/core/architecture.md

## FILOSOFÍA DE COMANDOS
→ Referencias a docs/workflows/commands.md

## PROHIBICIONES SISTÉMICAS
→ Referencias a docs/maintenance/

## EVOLUCIÓN ORGÁNICA
→ Principios de crecimiento sin complejidad acumulativa
```

### 6. FLUJO DE ACTUALIZACIÓN AUTOMÁTICA

**CUANDO SE EJECUTA**: Automáticamente al final de `/distill`

**PROCESO OBLIGATORIO**:
1. LLM lee contexto completo (TRUTH_SOURCE.md + Layer 3 + docs/)
2. Valida alineación con visión original
3. Regenera CLAUDE.md desde cero (sin sesgo)
4. Aplica validación de estructura y tamaño
5. Solo se acepta si pasa todas las validaciones

**CRITERIO DE FALLA**: Si regeneración no alinea → mantener versión anterior + alertar

### 7. ANTI-DERIVA SISTÉMICA

**PROHIBICIONES ABSOLUTAS**:
- Nunca agregar contenido sin eliminar equivalente
- Nunca crecer sin justificación en TRUTH_SOURCE.md
- Nunca duplicar información que existe en docs/
- Nunca contradecir decisiones cristalizadas del usuario
- Nunca eliminar referencias a user-vision/ como autoridad suprema

**DETECCIÓN AUTOMÁTICA**: Sistema debe detectar cuando CLAUDE.md deriva de principios originales

### 8. COORDINACIÓN CON COMANDO /distill

**INTEGRACIÓN OBLIGATORIA**: `/distill` DEBE culminar con actualización de CLAUDE.md

**FLUJO INTEGRADO**:
- `/distill` realiza destilación Layer 1 → Layer 2 → Layer 3
- **NUEVA FASE FINAL**: Layer 3 → CLAUDE.md regeneración automática
- Validación completa contra TRUTH_SOURCE.md
- Commit solo si pasa todas las validaciones

## VALIDACIONES DE CALIDAD

### Pre-Regeneración
- [ ] TRUTH_SOURCE.md está actualizado
- [ ] Layer 3 está completo y validado
- [ ] docs/ contiene módulos requeridos

### Post-Regeneración
- [ ] CLAUDE.md ≤ 200 líneas efectivas
- [ ] Todas las referencias modulares funcionan
- [ ] Alineación 100% con TRUTH_SOURCE.md
- [ ] Preserva user-vision/ como autoridad suprema
- [ ] No duplica contenido de docs/

### Validación de Deriva
- [ ] No contradice decisiones cristalizadas anteriores
- [ ] Mantiene simplicidad como principio fundamental
- [ ] No agrega complejidad innecesaria
- [ ] Respeta prohibiciones sistémicas establecidas

---

**CUMPLIMIENTO OBLIGATORIO**: Estas reglas NO son sugerencias. Son requisitos sistémicos inmutables que garantizan la integridad del sistema y la preservación de la visión del usuario.