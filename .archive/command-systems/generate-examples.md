# Comando: /generate-examples

> **Ubicación:** `.claude/commands/generate-examples.md`

Genera examples/ investigando mejores prácticas con Context7 y búsqueda web

## PROTOCOLO DE EJECUCIÓN

### FASE 1: ANÁLISIS DEL PROYECTO

EXPLORAR el código actual identificando:

1. **Stack tecnológico real**:
   ```bash
   # Detectar tecnologías
   - package.json dependencies
   - Extensiones de archivos únicas
   - Frameworks detectados
   ```

2. **Patrones existentes**:
   ```bash
   # Archivos más modificados (candidatos a patrones)
   git log --format=format: --name-only | sort | uniq -c | sort -rg | head -20
   
   # Estructuras que se repiten
   find . -name "*.ts" -o -name "*.js" | xargs grep -l "class\|function" | head -20
   ```

3. **Problemas recurrentes**:
   ```bash
   # Commits de fixes
   git log --grep="fix\|Fix" --oneline | head -20
   
   # TODOs sobre problemas
   grep -r "TODO.*fix\|FIXME" --include="*.ts"
   ```

### FASE 2: INVESTIGACIÓN EXTERNA

PENSAR MÁS sobre qué investigar basándose en el stack:

#### Usar Context7 MCP para documentación profunda:

```markdown
BUSCAR en Context7:
- "[tecnología principal] best practices 2024"
- "[framework] common pitfalls"
- "[lenguaje] design patterns"
- "[base de datos] optimization patterns"

EXTRAER:
- Patrones recomendados por la comunidad
- Anti-patrones a evitar
- Casos de estudio relevantes
```

#### Búsqueda web para ejemplos reales:

```markdown
BUSCAR en web:
- "[tecnología] production ready examples"
- "[framework] real world patterns"
- "[problema específico] solution github"
- "[stack] architecture examples"

FILTRAR:
- Solo fuentes confiables (docs oficiales, repos populares)
- Ejemplos con >100 stars en GitHub
- Publicaciones recientes (último año)
```

### FASE 3: SÍNTESIS DE PATRONES

ULTRAPENSAR sobre cómo adaptar lo aprendido al proyecto:

1. **Fusionar conocimiento**:
   ```
   Patrón del proyecto + Mejor práctica externa = Example mejorado
   ```

2. **Contextualizar**:
   ```
   - No copiar ciegamente ejemplos externos
   - Adaptar al estilo y necesidades del proyecto
   - Mantener consistencia con código existente
   ```

3. **Priorizar**:
   ```
   1° Patrones que resuelven problemas actuales
   2° Patrones que previenen problemas comunes
   3° Patrones que mejoran mantenibilidad
   4° Optimizaciones y mejoras nice-to-have
   ```

### FASE 4: GENERACIÓN DE ESTRUCTURA

CREAR estructura inteligente basada en hallazgos:

```
examples/
├── README.md                      # Mapa navegable
├── core-patterns/                 # Los más importantes
│   ├── error-handling.ts         # Siempre crítico
│   ├── data-validation.ts        # Siempre necesario
│   └── [3-4 más del proyecto]
├── [tecnología]-patterns/        # Específicos del stack
│   ├── [framework]-component.tsx
│   ├── [database]-query.ts
│   └── [library]-integration.ts
├── anti-patterns/                # Basado en investigación
│   ├── AVOID-[problema-comun].ts
│   └── WRONG-vs-RIGHT.ts
├── testing/                      # Patterns de tests
│   └── [test-framework]-patterns.test.ts
└── advanced/                     # Patterns sofisticados
    └── [optimización].ts
```

### FASE 5: CONTENIDO ENRIQUECIDO

Para cada example, INCLUIR conocimiento investigado:

```typescript
/**
 * PATRÓN: [Nombre]
 * 
 * BASADO EN:
 * - Práctica interna: [dónde se usa en el proyecto]
 * - Mejor práctica: [fuente externa, URL]
 * - Documentación: [referencia oficial]
 * 
 * POR QUÉ FUNCIONA:
 * [Explicación que combina experiencia local + conocimiento externo]
 * 
 * CUÁNDO USAR:
 * - [Caso específico del proyecto]
 * - [Caso general de la industria]
 * 
 * ADVERTENCIAS:
 * - [Gotcha descubierto localmente]
 * - [Pitfall conocido en la comunidad]
 */

// Código que fusiona lo mejor de ambos mundos
export const pattern = () => {
  // Implementación que refleja aprendizajes
}

// 💡 INSIGHTS DE LA INVESTIGACIÓN:
// - [Dato interesante de Context7/Web]
// - [Optimización no obvia]
// - [Trade-off a considerar]
```

### FASE 6: VALIDACIÓN Y DOCUMENTACIÓN

CREAR README.md comprehensivo:

```markdown
# 📚 Examples - Mejores Prácticas

> Generado con investigación de Context7 y mejores prácticas de la industria

## 🎯 Guía Rápida

### Por Problema
- Error handling → `core-patterns/error-handling.ts`
- Type safety → `typescript-patterns/type-guards.ts`
- Performance → `advanced/memoization.ts`

### Por Tecnología
- React patterns → `react-patterns/`
- Node.js patterns → `node-patterns/`
- [Stack específico] → `[carpeta]/`

## 📖 Fuentes de Conocimiento

### Internas
- Análisis de [N] archivos del proyecto
- [X] patrones identificados
- [Y] anti-patrones descubiertos

### Externas  
- Context7: [lista de búsquedas útiles]
- Documentación oficial: [enlaces]
- Casos de estudio: [referencias]

## 🔄 Mantenimiento

Estos examples combinan:
1. **Experiencia local** - Lo que funciona aquí
2. **Mejores prácticas** - Lo que funciona globalmente
3. **Lecciones aprendidas** - Lo que no funcionó

Actualizar cuando:
- Se descubren nuevos patrones internos
- Cambian las mejores prácticas de la industria
- Se encuentran mejores soluciones
```

### FASE 7: REPORTE FINAL

```markdown
✅ Examples generados con investigación completa

📊 Resumen:
- Patrones core: [N]
- Anti-patrones: [N]  
- Fuentes consultadas: [N]
- Insights externos aplicados: [N]

🔍 Hallazgos clave:
1. [Patrón más valioso descubierto]
2. [Anti-patrón más peligroso a evitar]
3. [Optimización no obvia encontrada]

📚 Referencias útiles guardadas:
- [URL a documentación clave]
- [Búsqueda Context7 más valiosa]
- [Ejemplo de código excepcional]

🎯 Siguiente paso:
Usar estos patterns en el desarrollo diario
```

## NOTAS DE IMPLEMENTACIÓN

- La investigación externa enriquece pero no reemplaza el conocimiento local
- Siempre adaptar al contexto del proyecto
- Citar fuentes cuando sea valioso
- No sobrecargar con demasiados examples
- Calidad > Cantidad