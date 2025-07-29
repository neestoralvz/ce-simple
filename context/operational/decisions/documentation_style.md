# Documentation Style - Estilo LLM Optimizado

**29/07/2025 10:50 CDMX** | Documentation style guide for LLMs

## Principios Fundamentales

### Vocabulario Reforzamiento
Documentation vocabulary standards
Usar DEBE, SIEMPRE, NUNCA, OBLIGATORIO, FUNDAMENTAL, ESENCIAL; ser verboso, redundante, duplicativo; lenguaje natural puro, directo, técnico

### Header Compacto Obligatorio
**Formato:** `**DD/MM/YYYY HH:MM CDMX | Actualizado: DD/MM/YYYY HH:MM CDMX** | Propósito`
**DEBE incluir:** Fecha creación + última fecha actualización
**Ubicación:** Primera línea después título

### Regla Regeneración 10%
**OBLIGATORIO:** Si cambios >10% del documento → escribir desde cero
**NUNCA:** Editar incremental en cambios mayores
**SIEMPRE:** Preservar solo información esencial en regeneración

## Símbolos Navegación
**→** para: entonces, conduce a, siguiente
**←** para: proviene de, fuente  
**↓** para: detalles abajo
**↑** para: referencia anterior

## Técnicas Compactación

### DEBE eliminar:
- Verbosidad innecesaria
- Duplicaciones contenido
- Redundancias entre secciones
- Texto filler
- Explicaciones obvias
- **Codeboxes/code blocks** - NUNCA usar

### DEBE optimizar:
- Densidad información máxima
- Claridad técnica directa
- Estructura funcional únicamente
- **Texto directo** vs visual containers

## Anti-Pattern Crítico: Codeboxes

### NUNCA Usar Codeboxes
Codeboxes usage
vs Texto directo, listas numeradas, referencias inline
Visual bloat sin valor añadido - contenido debe ser autoexplicativo

### Reemplazos Codeboxes
**En lugar de code block** → Lista con bullets o numeración
**En lugar de syntax highlighting** → Texto directo con formatting mínimo
**En lugar de containers** → Secciones estructuradas con headers
**En lugar de examples boxes** → Ejemplos inline integrados

## Footer Enlaces Obligatorio
**SIEMPRE incluir:**
## Enlaces → Información Complementaria
**Si necesitas X:** → archivo.md:líneas

---
## Enlaces → Información Complementaria
**Si necesitas metodología:** → context/principles/methodology.md:48-65
**Si requieres todowrite:** → context/decisions/todowrite_methodology.md
**Si requieres ejemplos:** → context/examples/