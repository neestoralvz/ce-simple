# Comando /distill

Eres el sistema de destilación iterativa con convergencia automática. Tu trabajo es transformar conversaciones raw en núcleos temáticos compactos que crecen orgánicamente hasta completitud.

## Estado inicial: Leer reportes de progreso

Antes de procesar, SIEMPRE lee:
1. `/user-vision/layer1/_distillation_report.md` - Estado de absorción actual
2. `/user-vision/layer2/_synthesis_report.md` - Estado de síntesis
3. `/user-vision/layer3/_documentation_report.md` - Estado documentación

Estos reportes te dicen exactamente qué falta por procesar.

## Tu proceso iterativo

### Layer 1: Absorción de Quotes en Núcleos Temáticos

**Si núcleos NO existen:**
- Crear núcleos iniciales: metodologia_socratica.md, arquitectura_comandos.md, autoridad_vision.md, evolucion_organica.md, simplicidad_belleza.md, flujos_trabajo.md

**Si núcleos YA existen:**
- Lee el reporte de estado actual
- Identifica quotes pendientes de absorción  
- Agrega quotes relacionados a núcleos existentes
- Usa formato exacto:
  ```markdown
  ## Quote Original
  > "texto exacto del usuario"
  **Ref:** `/raw/conversations/archivo.md:línea`
  
  ### Contexto Conversacional
  [Contexto específico]
  ---
  ```

### Layer 2: Síntesis de Relaciones (solo cuando Layer 1 >80%)

Despliega especialista que:
- Cree archivos de dominio: metodologia_arquitectura_bridge.md, vision_simplicidad_tension.md, etc.
- Mapee conexiones entre núcleos de Layer 1
- Preserve exclusivamente voz del usuario

### Layer 3: Documentación Formal (solo cuando Layer 2 >80%)

Despliega especialista que:
- Valide documentos existentes contra núcleos Layer 1
- Cree documentos faltantes según gaps detectados
- Aplique workflow: creación → alineamiento → verificación

### TRUTH_SOURCE.md: Autoridad Suprema (solo cuando Layer 3 completo)

Actualizar con síntesis de todos los layers, manteniendo 100% fidelidad a voz usuario.

## Convergencia automática

**Criterio de terminación:** 
Cuando el reporte de Layer 1 muestre 71/71 quotes procesados (100%), el comando reporta "Destilación completa - No hay más información que absorber"

**Auto-detección de completitud:**
- Cuenta quotes procesados vs totales disponibles
- Identifica si quedan conversaciones sin analizar
- Reporta progreso específico: "47/71 quotes procesados, 3 iteraciones restantes estimadas"

## Actualización de reportes

Al finalizar cada iteración, SIEMPRE actualiza:
- `_distillation_report.md` con nuevo estado de absorción
- Contadores de progreso precisos
- Próximas acciones específicas

## Principios de eficiencia

- **Archivos compactos**: Cada núcleo focalizado en un tema específico
- **Trazabilidad exacta**: Referencias `/raw/conversations/archivo.md:línea`
- **Pureza absoluta**: Solo contenido del usuario, cero interpretación AI
- **Crecimiento orgánico**: Núcleos crecen naturalmente con cada iteración

## Ejecución

Ejecutar hasta convergencia automática. El comando debe poder ejecutarse múltiples veces hasta que reporte completitud total.