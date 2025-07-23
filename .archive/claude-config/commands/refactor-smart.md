# Comando: /refactor-smart

> **Ubicación:** `.claude/commands/refactor-smart.md`

Refactoriza código con análisis profundo previo: $ARGUMENTS

## PROTOCOLO DE EJECUCIÓN

### FASE 1: ANÁLISIS EXHAUSTIVO

EXPLORAR el código objetivo identificando:

```bash
# Métricas de complejidad
- Complejidad ciclomática
- Profundidad de anidamiento  
- Líneas por función/clase
- Acoplamiento entre módulos

# Code smells comunes
- Duplicación (DRY violations)
- Clases/funciones muy grandes
- Nombres poco descriptivos
- Comentarios que explican código malo
- Dead code

# Violaciones de principios
- SOLID violations
- Separación de responsabilidades
- Abstracción inadecuada
- Dependencias circulares
```

### FASE 2: IDENTIFICACIÓN DE OPORTUNIDADES

PENSAR MÁS sobre qué refactorizar y por qué:

```markdown
## 🔍 Oportunidades Detectadas

### Alta Prioridad
1. **[Nombre del problema]**
   - Ubicación: [archivo:líneas]
   - Problema: [descripción específica]
   - Impacto: [mantenibilidad/performance/claridad]
   - Solución propuesta: [técnica de refactoring]

### Media Prioridad
[Lista similar]

### Baja Prioridad (nice to have)
[Lista similar]
```

### FASE 3: PLAN DE REFACTORING

ULTRAPENSAR sobre el orden y estrategia:

```markdown
## 📋 Plan de Ejecución

### Preparación
1. **Asegurar cobertura de tests**
   ```bash
   npm test -- --coverage [módulo]
   # Si < 80%, escribir tests primero
   ```

2. **Crear branch de refactoring**
   ```bash
   git checkout -b refactor/[nombre-descriptivo]
   ```

3. **Establecer baseline**
   - Screenshot de métricas actuales
   - Performance benchmarks si aplica

### Secuencia de Refactoring
[Ordenar por dependencias y riesgo]

1. **Extract Method/Class**
   - De: [código grande]
   - A: [múltiples funciones cohesivas]
   - Validar: Tests siguen pasando

2. **Rename Variables**
   - De: `x, temp, data`
   - A: `userEmail, validationResult, orderItems`
   - Validar: No hay referencias rotas

3. **Simplify Conditionals**
   - De: Nested if-else hell
   - A: Early returns, guard clauses
   - Validar: Lógica idéntica

[Continuar con otros refactorings]
```

### FASE 4: IMPLEMENTACIÓN INCREMENTAL

Para CADA refactoring:

```typescript
// ANTES (documentar código original)
function processData(input: any) {
  // código complejo, anidado, poco claro
  if (input) {
    if (input.type === 'user') {
      // 50 líneas de lógica
    }
  }
}

// DESPUÉS (código refactorizado)
function processData(input: DataInput) {
  if (!input) return handleEmptyInput();
  
  const processor = getProcessorForType(input.type);
  return processor.process(input);
}

// VALIDACIÓN
- [ ] Tests pasan
- [ ] No hay warnings nuevos
- [ ] Comportamiento idéntico
- [ ] Métricas mejoradas
```

### FASE 5: TÉCNICAS ESPECÍFICAS

Aplicar técnicas según el caso:

#### Extract Method
```typescript
// Detectar código que hace múltiples cosas
// Extraer cada responsabilidad a su método
```

#### Replace Conditional with Polymorphism
```typescript
// Si hay switch/if largos sobre types
// Crear clases/estrategias por tipo
```

#### Introduce Parameter Object
```typescript
// Si función tiene > 3 parámetros
// Agrupar en objeto con interfaz clara
```

#### Remove Dead Code
```typescript
// Código comentado o nunca ejecutado
// Eliminar sin piedad (git lo tiene)
```

### FASE 6: VALIDACIÓN Y MÉTRICAS

MEDIR mejoras objetivamente:

```markdown
## 📊 Resultados del Refactoring

### Métricas Antes vs Después
| Métrica | Antes | Después | Mejora |
|---------|-------|---------|---------|
| Complejidad ciclomática | 15 | 5 | -67% |
| Líneas por función | 120 | 25 | -79% |
| Cobertura de tests | 45% | 85% | +40% |
| Duplicación | 23% | 5% | -78% |

### Performance (si aplica)
- Tiempo ejecución: [antes] → [después]
- Memoria usada: [antes] → [después]

### Mantenibilidad
- Tiempo para entender código: [estimado]
- Facilidad para agregar features: [mejorada]
```

### FASE 7: DOCUMENTACIÓN Y COMMIT

DOCUMENTAR cambios significativos:

```typescript
/**
 * Refactored: [fecha]
 * Razón: [por qué se cambió]
 * Mejoras: [qué se logró]
 */
```

COMMIT con mensaje descriptivo:

```bash
git add .
git commit -m "refactor: improve [módulo] readability and performance

- Extracted business logic into dedicated services
- Simplified complex conditionals with early returns  
- Reduced cyclomatic complexity from 15 to 5
- Improved test coverage to 85%
- No functional changes"
```

## CUÁNDO USAR

`/refactor-smart` es ideal cuando:
- El código funciona pero es difícil de mantener
- Antes de agregar nueva funcionalidad a código legacy
- Las métricas de calidad están bajas
- El equipo se queja de un módulo específico
- Preparación para escalar

## PRINCIPIOS GUÍA

1. **Refactoring ≠ Reescribir**: Mejoras incrementales
2. **Tests primero**: Nunca refactorizar sin safety net
3. **Un paso a la vez**: Commit frecuente
4. **Medir impacto**: Datos objetivos, no opiniones
5. **Preservar funcionalidad**: Si cambia comportamiento, no es refactoring