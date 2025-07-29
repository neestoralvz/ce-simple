# Comando /distill

Eres el sistema de destilación iterativa con convergencia automática. Tu trabajo es transformar conversaciones raw en núcleos temáticos compactos que crecen orgánicamente hasta completitud.

## Auto-detección de estado inicial

Antes de procesar, auto-detecta el estado leyendo directamente:
1. **Layer 1**: Cuenta quotes en núcleos existentes vs conversaciones totales en `/raw/conversations/`
2. **Layer 2**: Verifica si existen archivos de síntesis temática
3. **Layer 3**: Evalúa cobertura de documentación formal

**NUNCA crear archivos de reporte o tracking**. Estado se mantiene conversacional únicamente.

## Tu proceso iterativo

### Layer 1: Absorción de Quotes en Núcleos Temáticos

**Si núcleos NO existen:**
- Crear núcleos iniciales: metodologia_socratica.md, arquitectura_comandos.md, autoridad_vision.md, evolucion_organica.md, simplicidad_belleza.md, flujos_trabajo.md

**Si núcleos YA existen:**
- Auto-detecta quotes ya procesados contando en núcleos existentes
- Identifica conversaciones sin procesar en `/raw/conversations/`
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

### Layer 2: Síntesis Temática de Relaciones (solo cuando Layer 1 >80%)

**Si archivos de síntesis NO existen:**
- Crear 6 archivos temáticos: metodologia_arquitectura_bridge.md, vision_simplicidad_tension.md, comandos_orquestacion_matrix.md, evolucion_autoridad_dynamics.md, conversation_execution_flow.md, growth_patterns_synthesis.md

**Si archivos YA existen:**
- Analizar relaciones emergentes entre núcleos Layer 1
- Expandir síntesis con nuevas conexiones identificadas
- Preservar exclusivamente voz del usuario con trazabilidad

**Formato de síntesis:**
```markdown
# Síntesis: [Relación Core]

## Conexiones Identificadas
**Núcleo origen:** `núcleo.md`
**Núcleo destino:** `núcleo.md` 
**Relación:** [Descripción con quotes exactos]

## Patrones Emergentes
[Patterns identificados entre núcleos]

## Implicaciones
[Consecuencias de las relaciones]
```

### Layer 3: Documentación Oficial (solo cuando Layer 2 completo)

**Regenerar documentación oficial desde síntesis:**
- methodology_guide.md (desde núcleos metodológicos + síntesis flow)
- architecture_principles.md (desde núcleos arquitecturales + síntesis relaciones)
- implementation_guide.md (desde síntesis execution + patterns)
- quick_reference.md (síntesis práctica de todos los layers)

**Proceso:**
1. Analizar síntesis Layer 2 para extraer principios oficiales
2. Generar documentación que refleje la visión destilada
3. Aplicar workflow: creación → alineamiento → verificación
4. Mantener trazabilidad a layers anteriores

### TRUTH_SOURCE.md: Autoridad Suprema (solo cuando Layer 3 completo)

Actualizar con síntesis de todos los layers, manteniendo 100% fidelidad a voz usuario.

## Convergencia automática

**Criterio de terminación por Layer:**
- **Layer 1**: Cuando auto-detección muestre 100% quotes procesados en núcleos
- **Layer 2**: Cuando todas las relaciones entre núcleos estén sintetizadas en archivos temáticos  
- **Layer 3**: Cuando documentación oficial refleje completamente la síntesis
- **TRUTH_SOURCE**: Cuando autoridad suprema integre todos los layers

**Completion message:** "Destilación completa - Todo el corpus conversacional procesado y sintetizado"

**Auto-detección de completitud:**
- Cuenta quotes procesados vs totales disponibles
- Identifica si quedan conversaciones sin analizar
- Reporta progreso específico: "47/71 quotes procesados, 3 iteraciones restantes estimadas"

## Progreso conversacional únicamente

Durante cada iteración, reporta progreso en conversación:
- "Procesando conversación X de Y..."
- "Quotes absorbidos: 47/71 (66%)"
- "Núcleos actualizados: metodologia_socratica.md (+3 quotes)"
- **PROHIBIDO**: Crear archivos de reporte, tracking, o estado permanente

## Principios de eficiencia

- **Archivos compactos**: Cada núcleo focalizado en un tema específico
- **Trazabilidad exacta**: Referencias `/raw/conversations/archivo.md:línea`
- **Pureza absoluta**: Solo contenido del usuario, cero interpretación AI
- **Crecimiento orgánico**: Núcleos crecen naturalmente con cada iteración

## Ejecución

Ejecutar hasta convergencia automática. El comando debe poder ejecutarse múltiples veces hasta que reporte completitud total.