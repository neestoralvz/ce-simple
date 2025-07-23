Comando: /generate-prp
Ubicación: .claude/commands/generate-prp.md

Genera un PRP (Product Requirement Prompt) inteligente para: $ARGUMENTS

PROTOCOLO DE GENERACIÓN
PASO 1: ANÁLISIS DEL REQUEST
ENTENDER qué se quiere construir:

Extraer el tipo de feature del request
Identificar complejidad estimada
Detectar áreas del código que se verán afectadas
Inferir requisitos implícitos
PASO 2: INVESTIGACIÓN EXHAUSTIVA
EXPLORAR el proyecto para entender:

bash
# Arquitectura actual
- Estructura de carpetas relacionadas
- Patrones existentes similares  
- Decisiones técnicas previas

# Dominio del negocio
- Entidades involucradas
- Reglas de negocio aplicables
- Flujos de trabajo existentes

# Stack técnico
- Tecnologías que se usarán
- Librerías disponibles
- Limitaciones conocidas
BUSCAR información externa:

Web: mejores prácticas para [tecnología/patrón]
Documentación oficial de APIs/librerías necesarias
Casos de estudio similares
Problemas comunes y soluciones
PASO 3: ULTRAPENSAR LA SOLUCIÓN
REFLEXIONAR profundamente sobre:

¿Cuál es la arquitectura óptima dado el contexto?
¿Qué decisiones tendrán impacto a largo plazo?
¿Dónde están los mayores riesgos?
¿Cómo hacerlo mantenible y extensible?
¿Qué trade-offs estamos haciendo?
PASO 4: SELECCIÓN DE TEMPLATE
ELEGIR el template apropiado de PRPs/templates/:

api-feature.md → Nuevos endpoints/servicios
ui-component.md → Interfaces complejas
integration.md → Servicios externos
refactoring.md → Mejoras de código existente
migration.md → Cambios de esquema/datos
performance.md → Optimizaciones
_base.md → Si no encaja en ninguna
PASO 5: GENERAR EL PRP
CREAR el documento siguiendo esta estructura:

markdown
# PRP: [Nombre Descriptivo del Feature]

## 🎯 OBJETIVO
[1-2 líneas claras del resultado final esperado]

## 📋 CONTEXTO
### Por qué lo necesitamos
[Problema que resuelve]

### Restricciones
- DEBE [restricción dura]
- NO PUEDE [limitación importante]
- DEBERÍA [preferencia si es posible]

### Stakeholders
[Quién se beneficia y qué espera]

## 🔍 INVESTIGACIÓN REQUERIDA
[Todo lo que debe explorarse ANTES de implementar]

## 🏗️ PLAN DE IMPLEMENTACIÓN
[Fases detalladas con tareas específicas]

## 📊 CRITERIOS DE ÉXITO
[Medibles y automatizables]

## ⚡ HINTS DE EXPLORACIÓN
[Guías y gotchas descubiertos en la investigación]

## 🚨 RIESGOS Y MITIGACIONES
[Tabla de riesgos identificados]
PASO 6: VALIDACIÓN Y CALIFICACIÓN
VERIFICAR que el PRP:

✅ Tiene objetivo claro y alcanzable
✅ Include contexto suficiente
✅ Define plan paso a paso sin ambigüedad
✅ Establece criterios medibles
✅ Identifica riesgos reales
✅ Proporciona hints útiles
ASIGNAR SCORE de confianza (1-10):

9-10: Listo para ejecución directa
7-8: Sólido con detalles menores a resolver
5-6: Necesita más investigación específica
<5: Recomendar más análisis antes de proceder
PASO 7: GUARDAR Y REPORTAR
GUARDAR en: PRPs/[feature-name].md

REPORTAR:

✅ PRP generado: PRPs/[feature-name].md
📊 Score de confianza: X/10
⏱️ Estimación: [tiempo estimado]
📝 Siguiente paso: /execute-prp PRPs/[feature-name].md
RECORDATORIOS
Un buen PRP elimina TODAS las preguntas durante implementación
Mejor sobre-especificar que sub-especificar
Los hints de exploración son oro - no los omitas
Si el score es <7, investiga más antes de continuar
