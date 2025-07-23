---
description: "Analiza la calidad del código y sugiere mejoras específicas"
allowedTools: ["Read", "Grep", "Write", "Bash"]
extendedThinking: true
---

# Análisis de Calidad de Código

Realiza un análisis completo de la calidad del código especificado y proporciona recomendaciones específicas para mejoras.

**Archivos/Directorios a analizar**: $ARGUMENTS

## Fase 1: Análisis Estático

### Estructura del Proyecto
Revisar la organización general del código:
- Estructura de directorios
- Convenciones de nomenclatura
- Separación de responsabilidades

### Calidad del Código
Identificar problemas comunes:
- Complejidad ciclomática alta
- Duplicación de código
- Funciones muy largas
- Anidamiento excesivo
- Variables mal nombradas

### Patrones y Anti-patrones
Buscar:
- Uso correcto de patrones de diseño
- Anti-patrones conocidos
- Violaciones de principios SOLID
- Code smells

## Fase 2: Análisis de Dependencias

### Dependencias del Proyecto
!if [ -f "package.json" ]; then
  echo "=== Análisis de package.json ==="
  cat package.json | jq '.dependencies // {}, .devDependencies // {}'
fi

!if [ -f "requirements.txt" ]; then
  echo "=== Análisis de requirements.txt ==="
  cat requirements.txt
fi

### Vulnerabilidades de Seguridad
!if command -v npm &> /dev/null && [ -f "package.json" ]; then
  echo "=== Audit de npm ==="
  npm audit --json || echo "Audit completado con warnings"
fi

## Fase 3: Métricas de Código

### Estadísticas Generales
!find ${ARGUMENTS:-.} -type f \( -name "*.js" -o -name "*.ts" -o -name "*.jsx" -o -name "*.tsx" -o -name "*.py" -o -name "*.java" \) | head -20 | while read file; do
  echo "=== $file ==="
  wc -l "$file"
  echo "Líneas de código: $(cat "$file" | grep -v '^\s*$' | grep -v '^\s*//' | wc -l)"
  echo ""
done

## Fase 4: Recomendaciones

### Prioridades de Refactoring
1. **Crítico**: Problemas de seguridad y bugs potenciales
2. **Alto**: Mejoras de rendimiento y mantenibilidad
3. **Medio**: Optimizaciones de código y legibilidad
4. **Bajo**: Convenciones y estilo

### Plan de Acción
Generar un plan específico con:
- Problemas identificados por prioridad
- Refactorings sugeridos
- Estimación de esfuerzo
- Beneficios esperados

### Métricas de Seguimiento
- Líneas de código duplicado
- Complejidad promedio por función
- Cobertura de tests (si disponible)
- Número de dependencias obsoletas

## Salida del Análisis

Crear un reporte estructurado con:
1. **Resumen ejecutivo**
2. **Problemas críticos encontrados**
3. **Recomendaciones priorizadas**
4. **Métricas antes/después esperadas**
5. **Próximos pasos sugeridos**