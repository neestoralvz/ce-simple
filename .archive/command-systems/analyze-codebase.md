# Comando: /analyze-codebase

> **Ubicación:** `.claude/commands/analyze-codebase.md`

Analiza el proyecto actual desde múltiples perspectivas usando subagentes paralelos

## PROTOCOLO DE EJECUCIÓN

### FASE 1: PREPARACIÓN

IDENTIFICAR el alcance del análisis:
- Directorio raíz del proyecto
- Archivos y carpetas a incluir/excluir
- Nivel de profundidad requerido

### FASE 2: DESPLIEGUE DE SUBAGENTES PARALELOS

DESPLEGAR 6 SUBAGENTES ESPECIALIZADOS SIMULTÁNEAMENTE:

```bash
# USAR TASK TOOL PARA EJECUCIÓN PARALELA

TASK 1 - 📁 Analizador de Estructura:
EXPLORAR: Toda la estructura de directorios
IDENTIFICAR: 
- Organización y propósito de cada carpeta
- Módulos principales y sus responsabilidades
- Puntos de entrada (main, index, app)
- Archivos de configuración y su función
ENTREGAR: Mapa mental de la arquitectura

TASK 2 - 📦 Analizador de Dependencias:
EXAMINAR: package.json, requirements.txt, go.mod, etc.
ANALIZAR:
- Stack tecnológico completo
- Versiones de dependencias
- Dependencias dev vs producción
- Vulnerabilidades conocidas (npm audit)
ENTREGAR: Informe de stack y riesgos

TASK 3 - 📊 Analizador de Complejidad:
MEDIR:
- Líneas de código por módulo/archivo
- Complejidad ciclomática
- Profundidad de anidamiento
- Duplicación de código
CALCULAR:
- Archivos más complejos (top 10)
- Funciones más largas
- Mayor acoplamiento
ENTREGAR: Métricas de calidad

TASK 4 - 🎨 Detector de Patrones:
BUSCAR:
- Patrones de diseño utilizados
- Convenciones de naming
- Estructura de componentes/clases
- Patrones de testing
IDENTIFICAR:
- Anti-patterns comunes
- Inconsistencias de estilo
- Code smells
ENTREGAR: Catálogo de patrones

TASK 5 - 🧪 Analizador de Testing:
EVALUAR:
- Frameworks de testing usados
- Cobertura actual (si está disponible)
- Tipos de tests (unit, integration, e2e)
- Estructura de tests
IDENTIFICAR:
- Áreas sin tests
- Tests rotos o skippeados
- Oportunidades de mejora
ENTREGAR: Estado del testing

TASK 6 - 📝 Analizador de Documentación:
REVISAR:
- README.md y documentación principal
- Comentarios en código (JSDoc, etc.)
- Documentación de APIs
- Guías de contribución
EVALUAR:
- Completitud de la documentación
- Actualización vs código actual
- Áreas sin documentar
ENTREGAR: Gaps de documentación

# CRÍTICO: TODAS LAS TASKS SE EJECUTAN EN PARALELO
```

### FASE 3: SÍNTESIS Y CONSOLIDACIÓN

CONSOLIDAR resultados de todos los subagentes:

```markdown
## 📊 ANÁLISIS CONSOLIDADO DEL PROYECTO

### Resumen Ejecutivo
- **Tamaño**: [LOC total, archivos, módulos]
- **Stack Principal**: [tecnologías core]
- **Salud General**: [score 1-10 con justificación]
- **Madurez**: [MVP/Crecimiento/Maduro]

### Arquitectura Detectada
[Síntesis del subagente de estructura]
- Patrón arquitectónico: [MVC/Microservicios/etc]
- Organización: [por features/por capas/híbrido]
- Puntos de entrada: [listar principales]

### Stack Tecnológico
[Síntesis del subagente de dependencias]
- Frontend: [si aplica]
- Backend: [si aplica]
- Base de datos: [si aplica]
- Herramientas: [testing, build, etc.]

### Calidad del Código
[Síntesis del subagente de complejidad]
- Complejidad promedio: [número]
- Archivos problemáticos: [top 5]
- Deuda técnica estimada: [baja/media/alta]

### Patrones y Convenciones
[Síntesis del subagente de patrones]
- Patrones dominantes: [listar]
- Anti-patterns detectados: [listar con ubicación]
- Consistencia: [porcentaje estimado]

### Estado del Testing
[Síntesis del subagente de testing]
- Cobertura: [porcentaje si disponible]
- Tipos de tests: [unit/integration/e2e]
- Áreas críticas sin tests: [listar]

### Documentación
[Síntesis del subagente de documentación]
- Completitud: [porcentaje estimado]
- Actualizada: [sí/no/parcial]
- Prioridades: [qué documentar primero]

### 🚨 Alertas Críticas
1. [Vulnerabilidades de seguridad si hay]
2. [Dependencias obsoletas críticas]
3. [Anti-patterns peligrosos]
4. [Falta de tests en áreas críticas]

### 💡 Recomendaciones Priorizadas
1. **Inmediato**: [acciones urgentes]
2. **Corto plazo**: [mejoras importantes]
3. **Largo plazo**: [refactoring/arquitectura]

### 📈 Métricas Clave para Dashboard
- Líneas de código: [número]
- Complejidad promedio: [número]
- Cobertura de tests: [porcentaje]
- Deuda técnica: [horas estimadas]
- Salud de dependencias: [score]
```

### FASE 4: ALMACENAMIENTO OPCIONAL

SI se especifica --save:
```bash
# Guardar análisis para referencia futura
mkdir -p .claude/analysis
echo "[timestamp] - [resultado]" > .claude/analysis/codebase-analysis-[fecha].md
```

## VARIANTES DEL COMANDO

### Análisis Enfocado
```bash
/analyze-codebase --focus=security
# Solo despliega subagentes relacionados con seguridad

/analyze-codebase --focus=performance
# Solo métricas de rendimiento y complejidad

/analyze-codebase --path=src/components
# Analiza solo un subdirectorio
```

### Análisis Comparativo
```bash
/analyze-codebase --compare-with=main
# Compara branch actual con main

/analyze-codebase --compare-with=last-analysis
# Compara con análisis previo guardado
```

## INTEGRACIÓN CON OTROS COMANDOS

Este comando puede ser invocado por:

- **`/create-claude`**: Para entender proyecto existente
- **`/generate-prp`**: Para contexto antes de planificar
- **`/update-core`**: Para detectar cambios
- **`/refactor-smart`**: Para identificar oportunidades

## OUTPUT EJEMPLO

```markdown
📊 Análisis completado en 45 segundos

PROYECTO: E-commerce Platform
TAMAÑO: 34,567 LOC en 234 archivos
STACK: Next.js 13, Node.js 18, PostgreSQL

✅ FORTALEZAS:
- Arquitectura modular bien definida
- TypeScript con strict mode
- 78% cobertura de tests

⚠️ ÁREAS DE MEJORA:
- 5 componentes con complejidad > 20
- API sin rate limiting
- 12 dependencias desactualizadas

🎯 ACCIÓN RECOMENDADA:
Ejecutar `/generate-prp security-hardening.md` para 
abordar las vulnerabilidades detectadas.
```

## BENEFICIOS DE ESTE APPROACH

1. **Velocidad**: Análisis en paralelo ~6x más rápido
2. **Completitud**: Ningún aspecto se pasa por alto
3. **Contexto Limpio**: Solo información relevante
4. **Reutilizable**: Otros comandos pueden invocarlo
5. **Modular**: Fácil agregar nuevos subagentes