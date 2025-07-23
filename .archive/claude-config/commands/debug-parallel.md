# Comando: /debug-parallel

> **Ubicación:** `.claude/commands/debug-parallel.md`

Debug problema complejo usando análisis paralelo multi-agente: $ARGUMENTS

## PROTOCOLO DE EJECUCIÓN

### FASE 1: COMPRENSIÓN DEL PROBLEMA

ANALIZAR la descripción del problema:
- Síntomas reportados
- Contexto donde ocurre
- Frecuencia (siempre/a veces/raro)
- Impacto en el sistema

### FASE 2: DESPLIEGUE DE SUBAGENTES

PENSAR MUCHO MÁS sobre qué especialistas necesitas:

```markdown
DESPLEGAR [4-6] SUBAGENTES ESPECIALIZADOS EN PARALELO:

🔍 SUBAGENTE 1 - Detective de Logs:
ANALIZAR: Todos los logs relevantes
BUSCAR: Patrones, errores, warnings, timestamps
ENTREGAR: Timeline de eventos y anomalías

🏗️ SUBAGENTE 2 - Arquitecto de Sistema:
ANALIZAR: Flujo de datos y dependencias
BUSCAR: Cuellos de botella, puntos de falla
ENTREGAR: Diagrama de dónde puede estar el problema

📊 SUBAGENTE 3 - Analista de Estado:
ANALIZAR: Estado de BD, cache, memoria
BUSCAR: Inconsistencias, datos corruptos
ENTREGAR: Snapshot del estado en momento del error

🔄 SUBAGENTE 4 - Historiador de Cambios:
ANALIZAR: Commits recientes, deploys
BUSCAR: Qué cambió antes del problema
ENTREGAR: Cambios sospechosos correlacionados

🧪 SUBAGENTE 5 - Reproductor:
INTENTAR: Reproducir el error
VARIAR: Diferentes condiciones/entornos
ENTREGAR: Pasos exactos para reproducir

🔒 SUBAGENTE 6 - Auditor de Seguridad:
ANALIZAR: Permisos, auth, accesos
BUSCAR: Violaciones de seguridad
ENTREGAR: Posibles vectores de ataque

[EJECUTAR TODOS SIMULTÁNEAMENTE - NO SECUENCIAL]
```

### FASE 3: SÍNTESIS DE HALLAZGOS

CONSOLIDAR resultados de todos los subagentes:

```markdown
## 🎯 Hallazgos Consolidados

### Timeline Completo
[Fusionar timelines de logs + cambios + estado]

### Causa Más Probable
[Basado en convergencia de evidencias]

### Causas Alternativas
1. [Segunda más probable]
2. [Tercera opción]

### Evidencia Clave
- Subagente 1 encontró: [hallazgo]
- Subagente 2 identificó: [patrón]
- Subagente 3 detectó: [anomalía]
```

### FASE 4: PLAN DE ACCIÓN

GENERAR estrategia de solución:

```markdown
## 🛠️ Plan de Resolución

### Solución Inmediata (Hotfix)
```bash
# Mitigación rápida
[comandos específicos]
```

### Solución Completa
1. [Paso 1: qué hacer]
2. [Paso 2: cómo validar]
3. [Paso 3: prevención futura]

### Validación
- [ ] Error no se reproduce
- [ ] Tests pasan
- [ ] No hay regresiones
- [ ] Logs limpios
```

### FASE 5: IMPLEMENTACIÓN Y PREVENCIÓN

EJECUTAR la solución:

1. **Aplicar fix**:
   ```typescript
   // Código específico del fix
   ```

2. **Agregar test preventivo**:
   ```typescript
   // Test que hubiera detectado este bug
   test('prevents [error específico]', () => {
     // Reproducir condiciones
     // Verificar que no falla
   })
   ```

3. **Mejorar logging**:
   ```typescript
   // Agregar logs estratégicos para futuro debugging
   logger.debug('State before operation:', { ... })
   ```

4. **Documentar lección aprendida**:
   ```markdown
   // En docs/debugging-notes.md
   ## Issue: [nombre]
   - Síntomas: [qué pasaba]
   - Causa: [por qué pasaba]
   - Solución: [cómo se arregló]
   - Prevención: [cómo evitarlo]
   ```

## REPORTE FINAL

```markdown
# 🐛 Debug Report: $ARGUMENTS

## Problema Original
[Descripción]

## Causa Raíz
[Explicación técnica]

## Solución Aplicada
[Qué se hizo]

## Cambios
- Fixed: [archivos modificados]
- Tests: [tests agregados]
- Docs: [documentación actualizada]

## Tiempo Total
- Análisis: [X] minutos
- Implementación: [Y] minutos
- Validación: [Z] minutos

## Lecciones Aprendidas
[Qué aprendimos para el futuro]
```

## CASOS DE USO

Usar `/debug-parallel` cuando:
- El error es intermitente o difícil de reproducir
- Involucra múltiples sistemas o servicios
- Los logs no muestran causa obvia
- Necesitas diferentes perspectivas
- El debugging secuencial no funciona

## VENTAJAS DEL PARALELISMO

- **Velocidad**: 6 análisis en tiempo de 1
- **Comprehensión**: No se escapa ningún ángulo
- **Correlación**: Patrones emergen de múltiples fuentes
- **Objetividad**: Diferentes perspectivas reducen bias