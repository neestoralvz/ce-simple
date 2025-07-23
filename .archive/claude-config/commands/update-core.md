# Comando: /update-core

> **Ubicación:** `.claude/commands/update-core.md`

Actualiza CLAUDE.md y examples/ basándose en la evolución del proyecto

## PROTOCOLO DE EJECUCIÓN

### FASE 1: ANÁLISIS DE CAMBIOS

DETECTAR qué ha cambiado desde la última actualización:

```bash
# Analizar commits recientes
git log --oneline -20

# Identificar nuevos archivos
find . -type f -newer CLAUDE.md

# Buscar nuevos patrones
- Nuevas carpetas o módulos
- Nuevas dependencias en package.json
- Nuevos tipos de archivos (.proto, .graphql, etc)
```

### FASE 2: EVALUACIÓN DE CLAUDE.md

PENSAR sobre el estado actual:

1. **Verificar relevancia**:
   - ¿La visión sigue siendo correcta?
   - ¿Las features core se implementaron?
   - ¿El roadmap necesita actualización?

2. **Detectar obsolescencia**:
   - Comandos que ya no se usan
   - Estructura que cambió
   - Decisiones arquitectónicas superadas

3. **Medir tamaño**:
   ```
   Si CLAUDE.md > 200 líneas:
      REFACTORIZAR: Mover detalles a docs/
   Si CLAUDE.md < 100 líneas:
      EXPANDIR: Agregar contexto faltante
   ```

### FASE 3: ACTUALIZACIÓN INTELIGENTE

ULTRAPENSAR sobre qué mantener, qué actualizar, qué eliminar:

#### Actualizar CLAUDE.md:

```markdown
# Secciones a revisar:

## 🧠 PROTOCOLO DE PENSAMIENTO
- Verificar que esté presente
- Actualizar si han surgido nuevos patrones de pensamiento
- Asegurar que niveles sean los correctos

## 🔍 HERRAMIENTAS DE INVESTIGACIÓN
- Agregar hallazgos de Context7/Web a examples/research/
- Actualizar protocolo si se descubren mejores prácticas
- Documentar nuevas fuentes útiles

## 🏗️ ARQUITECTURA
- Agregar nuevas tecnologías adoptadas
- Actualizar decisiones si cambiaron
- Documentar por qué se cambió

## 📁 ESTRUCTURA Y REFERENCIAS
- Actualizar referencias a examples/patterns/
- Verificar que PRPs completados estén listados
- Actualizar roadmap-features.md si existe

## 📋 CONVENCIONES
- Nuevos patrones que emergieron
- Anti-patrones descubiertos
- Lecciones aprendidas

## 🚀 FEATURES IMPLEMENTADAS
- Mover de ROADMAP a IMPLEMENTADAS
- Referenciar PRPs completados
- Agregar enlaces a documentación

## 🛠️ COMANDOS
- Agregar nuevos scripts útiles
- Eliminar obsoletos
- Verificar que todos los comandos Claude estén listados
```

### FASE 4: EVOLUCIÓN DE EXAMPLES

ANALIZAR código para detectar:

1. **Nuevos patrones exitosos**:
   ```bash
   # Buscar archivos más editados (probables patrones)
   git log --format=format: --name-only | sort | uniq -c | sort -rg | head -20
   ```

2. **Problemas recurrentes**:
   ```bash
   # Buscar fixes y correcciones
   git log --grep="fix\|Fix\|bug\|Bug" --oneline
   ```

3. **Conocimiento de investigación**:
   ```bash
   # Revisar si hay nuevos hallazgos en research
   ls examples/research/
   ```

4. **Mejores prácticas emergentes**:
   - Código que se copia frecuentemente
   - Soluciones elegantes a problemas complejos
   - Refactors exitosos
   - Patrones descubiertos via Context7/Web

GENERAR/ACTUALIZAR examples:

```typescript
// examples/patterns/[nuevo-patron].ts
/**
 * PATRÓN: [Nombre]
 * DESCUBIERTO: [Fecha/Contexto]
 * 
 * PROBLEMA: [Qué resolvía]
 * SOLUCIÓN: [Por qué funciona]
 * 
 * FUENTE: [Si viene de investigación externa]
 */
```

### FASE 5: SINCRONIZACIÓN DE TIPOS

VERIFICAR consistencia de tipos TypeScript/Prisma:

```bash
# Generar tipos actualizados de Prisma
npx prisma generate

# Buscar discrepancias comunes
grep -r "any\|unknown" --include="*.ts" | grep -v "node_modules"

# Verificar imports de tipos Prisma
grep -r "import.*from.*@prisma/client" --include="*.ts"
```

SINCRONIZAR tipos si hay problemas:

1. **Verificar single source of truth**:
   ```typescript
   // ✅ CORRECTO: Usar tipos de Prisma
   import { User, Prisma } from '@prisma/client'
   
   // ❌ EVITAR: Tipos manuales que se desincronizan
   interface User { /* ... */ }
   ```

2. **Actualizar examples con patrones de tipos**:
   ```typescript
   // examples/type-safety/prisma-sync.ts
   export const userFactory = (
     data: Prisma.UserCreateInput
   ): Prisma.UserCreateInput => ({ ...data })
   ```

3. **Corregir tests con tipos incorrectos**:
   - Actualizar mocks para usar tipos Prisma
   - Verificar factories de tests
   - Asegurar type safety en assertions

### FASE 6: LIMPIEZA Y OPTIMIZACIÓN

REFACTORIZAR si necesario:

1. **CLAUDE.md demasiado grande**:
   ```markdown
   # CLAUDE.md (mantener < 150 líneas)
   - Visión y arquitectura core
   - Comandos frecuentes
   - Enlaces a docs/ para detalles
   
   # docs/conventions.md
   - Convenciones detalladas
   
   # docs/architecture.md
   - Decisiones arquitectónicas profundas
   ```

2. **Examples redundantes**:
   - Consolidar patterns similares
   - Eliminar examples obsoletos
   - Mantener solo los más valiosos

### FASE 6: COMMIT Y REPORTE

GENERAR commit con cambios:

```bash
git add CLAUDE.md examples/ docs/
git commit -m "chore: update core documentation

- Updated CLAUDE.md with recent architectural changes
- Added examples for [new patterns]
- Refactored docs for better organization
- Removed obsolete conventions"
```

REPORTAR:

```markdown
📊 Core Update Complete

**CLAUDE.md**:
- Líneas: antes [X] → después [Y]
- Secciones actualizadas: [lista]
- Refactoring: [Sí/No]

**Examples**:
- Nuevos: [cantidad]
- Actualizados: [cantidad]
- Eliminados: [cantidad]

**Insights**:
- [Patrón emergente notable]
- [Anti-patrón a evitar]
- [Siguiente evolución recomendada]
```

## TRIGGERS RECOMENDADOS

Ejecutar `/update-core` cuando:
- Han pasado varias iteraciones de desarrollo
- Se completó una feature mayor
- Antes de onboarding de nuevo desarrollador
- Se detectan muchas preguntas repetidas
- El proyecto cambió de dirección

## CRITERIOS DE CALIDAD

- CLAUDE.md sigue siendo escaneable en < 5 minutos
- Examples reflejan el código actual, no el ideal
- Documentación ayuda, no estorba
- Todo lo obsoleto se elimina sin piedad
- Lo nuevo importante se captura