# Framework de Validación para CLAUDE.md

## PROPÓSITO

Garantizar que toda actualización de CLAUDE.md mantiene **100% fidelidad** a la visión original del usuario y previene deriva sistémica.

## VALIDACIONES OBLIGATORIAS

### 1. AUTORIDAD SUPREMA (CRÍTICO)

**VALIDACIÓN**: ¿CLAUDE.md preserva user-vision/ como autoridad suprema?

**CRITERIOS ESPECÍFICOS**:
- [ ] **Jerarquía explícita**: user-vision/ → SOBRESCRIBE → CLAUDE.md declarada
- [ ] **Referencias directas**: Menciona user-vision/TRUTH_SOURCE.md como autoridad
- [ ] **Validación obligatoria**: Instruye verificar alineamiento con user-vision/
- [ ] **Sin usurpación**: CLAUDE.md NO se declara como autoridad final

**AUTO-RECHAZO**: Si falla cualquier criterio → regeneración automática requerida

### 2. ALINEACIÓN CON VISIÓN ORIGINAL (CRÍTICO)

**VALIDACIÓN**: ¿Respeta los principios fundamentales del TRUTH_SOURCE.md?

**CRITERIOS METODOLÓGICOS**:
- [ ] **Socrática expansiva**: Conversación libre → comprensión → ejecución
- [ ] **Preservación de voz**: Usuario = fuente de verdad con citas exactas
- [ ] **Trabajo directo habilitado**: Claude puede investigar/implementar directamente
- [ ] **Detección sistémica proactiva**: Mantiene flujo detección → challenge → absorción

**CRITERIOS ARQUITECTURALES**:
- [ ] **Simplicidad como belleza**: Sistema se siente conversación natural
- [ ] **Comandos independientes**: 9 workflows autocontenidos pero coordinados
- [ ] **Orquestación de subagentes**: Agente principal orquesta vs hace todo
- [ ] **Regeneración slate limpio**: Eliminar archivos y recrear sin sesgo

**AUTO-RECHAZO**: Si falla >2 criterios → regeneración requerida

### 3. DENSIDAD Y MODULARIZACIÓN (CRÍTICO)

**VALIDACIÓN TAMAÑO**:
- [ ] **≤ 200 líneas efectivas** (excluyendo espacios/comentarios)
- [ ] **Máximo impacto**: Cada línea debe ser esencial
- [ ] **Sin redundancia**: No duplica contenido de docs/ o user-vision/

**VALIDACIÓN MODULAR**:
- [ ] **Referencias funcionales**: Todas las referencias a docs/ son válidas
- [ ] **Delegación correcta**: Detalles técnicos en docs/, esencia en CLAUDE.md
- [ ] **Sin over-detail**: No incluye procedimientos específicos o ejemplos extensos

**AUTO-RECHAZO**: Si excede límites → modularización forzada requerida

### 4. ESTRUCTURA Y CONSISTENCIA (IMPORTANTE)

**VALIDACIÓN ESTRUCTURAL**:
- [ ] **Estructura fija**: Sigue template obligatorio de update_rules.md
- [ ] **Secciones requeridas**: Autoridad, Principios, Metodología, Arquitectura, Prohibiciones
- [ ] **Flujo lógico**: Información organizada progresivamente
- [ ] **Formato consistente**: Markdown estándar, enlaces funcionales

**VALIDACIÓN CONTENIDO**:
- [ ] **Prohibiciones sistémicas**: Mantiene anti-creación archivos y anti-over-engineering
- [ ] **Filosofía comandos**: Preserva independencia e instrucciones puras
- [ ] **Evolución orgánica**: Mantiene principio de simplicidad continua

### 5. ANTI-DERIVA SISTÉMICA (CRÍTICO)

**VALIDACIÓN HISTÓRICA**:
- [ ] **Sin contradicciones**: No contradice decisiones cristalizadas anteriores
- [ ] **Preservación decisiones**: Mantiene puntos clave del usuario intactos
- [ ] **Sin feature creep**: No agrega complejidad innecesaria
- [ ] **Sin scope creep**: Mantiene enfoque en objetivos originales

**VALIDACIÓN FUTURO**:
- [ ] **Principios preventivos**: Incluye mecanismos anti-complejidad
- [ ] **Balance checker**: Mantiene simplificación vs funcionalidad esencial
- [ ] **Evolución controlada**: Crecimiento solo por conversación → destilación

### 6. SEPARACIÓN CLARA DE RESPONSABILIDADES (CRÍTICO)

**VALIDACIÓN DE RESPONSABILIDAD ÚNICA**:
- [ ] **Propósito inequívoco**: CLAUDE.md mantiene una responsabilidad específica
- [ ] **Límites bien definidos**: Fronteras claras sobre qué hace y qué delega
- [ ] **Sin scope creep**: No agrega "solo una funcionalidad más"
- [ ] **Composabilidad limpia**: Referencias modulares sin conflicto

**VALIDACIÓN ANTI-PATRÓN**:
- [ ] **No hace "un poquito de todo"**: Evita funciones mezcladas sin límites
- [ ] **No duplica contenido**: Referencias a docs/ vs repetir información
- [ ] **No usurpa autoridad**: Mantiene user-vision/ como autoridad suprema
- [ ] **No agrega interdependencias complejas**: Mantiene independencia modular

**VALIDACIÓN DE COMANDOS REFERENCIADOS**:
- [ ] **Cada comando mantiene responsabilidad única**: /workflows:distill, /expand, /roles:partner, etc.
- [ ] **Enforcement de separación**: Referencias a challenger automático para validar scope
- [ ] **Coordinación sin conflicto**: Comandos se combinan sin invasión de responsabilidades

## PROCESO DE VALIDACIÓN AUTOMÁTICA

### Fase 1: Pre-Validación (Antes de Regenerar)
```
1. Verificar TRUTH_SOURCE.md actualizado
2. Confirmar Layer 3 completo
3. Validar docs/ contiene módulos requeridos
4. Verificar contexto completo disponible
```

### Fase 2: Validación Post-Regeneración
```
1. EJECUTAR: Validación Autoridad Suprema
2. EJECUTAR: Validación Alineación Visión Original  
3. EJECUTAR: Validación Densidad y Modularización
4. EJECUTAR: Validación Estructura y Consistencia
5. EJECUTAR: Validación Anti-Deriva Sistémica
```

### Fase 3: Criterios de Aceptación/Rechazo
```
ACEPTAR SI:
- Todas las validaciones CRÍTICO = PASS
- ≥80% validaciones IMPORTANTE = PASS
- Tamaño ≤ 200 líneas efectivas

RECHAZAR SI:
- Cualquier validación CRÍTICO = FAIL
- Tamaño > 200 líneas efectivas
- <60% validaciones IMPORTANTE = PASS

ACCIÓN RECHAZO: 
- Mantener versión anterior de CLAUDE.md
- Alertar sobre validación fallida
- Requerir corrección manual si auto-regeneración falla 3x
```

## MÉTRICAS DE CALIDAD

### Métricas Cuantitativas
- **Líneas efectivas**: Target ≤ 200
- **Referencias modulares**: Target ≥ 80% contenido técnico en docs/
- **Ratio esencia/detalle**: Target 70% esencia, 30% referencias
- **Tiempo regeneración**: Target ≤ 5 minutos completo

### Métricas Cualitativas
- **Fidelidad visión**: Escala 1-10, target ≥ 9
- **Claridad estructura**: Escala 1-10, target ≥ 8  
- **Utilidad práctica**: Escala 1-10, target ≥ 8
- **Simplicidad percibida**: Escala 1-10, target ≥ 9

## ESCALAMIENTO DE PROBLEMAS

### Problema Nivel 1: Validación Individual Falla
- **Acción**: Auto-regeneración con ajustes específicos
- **Límite**: 2 intentos automáticos
- **Escalamiento**: Si persiste → Nivel 2

### Problema Nivel 2: Múltiples Validaciones Fallan
- **Acción**: Revisar contexto de entrada (TRUTH_SOURCE.md, Layer 3)
- **Límite**: 1 intento con contexto corregido
- **Escalamiento**: Si persiste → Nivel 3

### Problema Nivel 3: Falla Sistémica de Validación
- **Acción**: Mantener versión anterior, alertar usuario
- **Requerimiento**: Revisión manual del sistema de validación
- **Consideración**: Posible problema en TRUTH_SOURCE.md o reglas de update

## LOGS Y TRAZABILIDAD

**REQUERIMIENTO**: Cada validación debe generar log estructurado:
```
timestamp: [ISO-8601]
validation_type: [autoridad|alineacion|densidad|estructura|anti-deriva]
status: [PASS|FAIL|WARNING]
details: [criterios específicos evaluados]
metrics: [métricas cuantitativas medidas]
action_taken: [acción tomada basada en resultado]
```

**RETENCIÓN**: Logs de validación se mantienen en user-vision/raw/validation/ para análisis de patrones de deriva.

---

**ENFORCEMENT**: Este framework es OBLIGATORIO para toda actualización de CLAUDE.md. No es opcional, es requisito sistémico para mantener integridad del sistema.