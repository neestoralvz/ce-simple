# Decisión Arquitectural - Redefinición Sistema Context/

**29/07/2025 09:05 CDMX | Actualizado: 29/07/2025 09:05 CDMX** | Decisión arquitectural

## Arquitectura Central Redefinida

### Context/ Como Fuente Central
**DECISIÓN:** context/ en raíz → fuente única verdad arquitectural
**OBLIGATORIO:** commands/ SIEMPRE referencia context/ para coherencia
**NUNCA:** Duplicar información entre context/ y commands/

### Commands/ Reorganización Categórica
**ESTRUCTURA NUEVA:**
- workflows/ → Flujos proceso multi-step
- actions/ → Operaciones atómicas específicas  
- roles/ → Comportamientos agent especializado
- validations/ → Checks calidad/coherencia
- maintenance/ → Operaciones sistema

**DEBE eliminar:** Comandos redundantes o overlapping
**OBLIGATORIO:** Cada comando referencia context/ patterns

## Metodología Orquestador

### Agente Principal = Ultra-Orquestador
**FUNDAMENTAL:** Agente principal NUNCA ejecuta directamente
**SIEMPRE:** Delega vía Task tool → subagentes especializados
**RESPONSABILIDAD:** Coordinación + validación + synthesis únicamente

### Think x4 Obligatorio
**REQUIREMENT:** 4 niveles pensamiento antes propuestas:
1. Análisis contexto actual
2. Evaluación opciones alternativas  
3. Consecuencias decisión
4. Validación coherencia sistema

**NUNCA:** Propuestas reactivas sin análisis profundo

## Estilo Documentación LLM-Optimizado

### Principios Reforzamiento Textual
**VOCABULARIO OBLIGATORIO:** DEBE, SIEMPRE, NUNCA, OBLIGATORIO, FUNDAMENTAL
**ELIMINACIÓN:** Verbosidad, redundancia, text filler
**DENSIDAD:** Información máxima por token

### Headers Temporales Únicamente
**FORMATO:** `**DD/MM/YYYY HH:MM CDMX | Actualizado: DD/MM/YYYY HH:MM CDMX** | Propósito`
**EVOLUCIÓN:** Versiones posteriores solo fecha actualización
**NUNCA:** Headers complejos en docs maduros

## Separación Responsabilidades

### Usuario Define QUÉ
**AUTORIDAD:** Visión, objetivos, requirements
**VALIDACIÓN:** Override cualquier optimización AI
**NUNCA:** Especifica implementación técnica

### AI Define CÓMO  
**RESPONSABILIDAD:** Decisiones técnicas + implementación
**OBLIGATORIO:** Pensamiento profundo antes ejecución
**DEBE alinearse:** Siempre con visión usuario

### Boundary Enforcement
**FUNDAMENTAL:** Respeto absoluto domain separation
**VALIDACIÓN:** context/principles/methodology.md como arbitro

---
## Enlaces → Información Complementaria
**Si necesitas metodología:** → context/principles/methodology.md:1-25
**Si requieres patterns:** → context/patterns/documentation_style.md:5-20