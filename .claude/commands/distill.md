# Comando /distill

Eres el sistema de destilación iterativa con convergencia automática. Tu trabajo es transformar conversaciones raw en núcleos temáticos compactos que crecen orgánicamente hasta completitud.

## Auto-detección de estado inicial

Antes de procesar, auto-detecta el estado leyendo directamente:
1. **Layer 1**: 
   - Listar archivos en `/raw/conversations/` por timestamp
   - Verificar secciones "Conversations Processed" en nuclei existentes  
   - Identificar conversations sin procesar mediante cross-reference
2. **Layer 2**: Verifica si existen archivos de síntesis temática
3. **Layer 3**: Evalúa cobertura de documentación formal

**Método de auto-detección híbrida**:
```bash
# Primary: Compare timestamps
newest_conversation=$(ls -t /raw/conversations/*.md | head -1)
newest_nuclei=$(ls -t /layer1/*.md | head -1)

# Secondary: Check processed lists in nuclei
grep -h "^- " /layer1/*/## Conversations Processed | sort -u > processed.tmp
ls /raw/conversations/*.md | basename -s .md > available.tmp
comm -23 available.tmp processed.tmp = pending_conversations

# Tertiary: Sample validation if timestamps match
```

**NUNCA crear archivos de reporte o tracking**. Estado se mantiene conversacional únicamente.

**NOTA CRÍTICA**: No usar métricas de completitud basadas en conteo de quotes - conversaciones raw mezclan voz auténtica con interpretaciones AI.

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

- **Mantener tracking de completitud**: Al final de cada núcleo, agregar/actualizar:
  ```markdown
  ## Conversations Processed
  - archivo1.md
  - archivo2.md
  ```

### Layer 2: Concentración en Insights Ultra-Densos (solo cuando Layer 1 >80%)

**OBJETIVO CRÍTICO**: Fusionar múltiples quotes en insights concentrados y poderosos

**Proceso de Concentración:**
- Tomar 10+ quotes relacionados de Layer 1
- Extraer el insight CORE que conecta todos
- Crear declaración densa que concentre máximo valor
- Eliminar redundancia y dispersión

**Formato de concentración:**
```markdown
# Insight Concentrado: [Principio Core]

## Síntesis Ultra-Densa
[UN párrafo que concentra 10+ quotes en insight poderoso]

## Evidence Base (Layer 1 sources)
[Solo referencias, no repetir contenido]

## Implicaciones Ejecutables
[Consecuencias directas y actionables]
```

**CRITERIO**: Cada archivo Layer 2 debe concentrar 10x más valor que suma de sus quotes fuente

### Layer 3: Documentación ULTRA-DENSA Ejecutable (solo cuando Layer 2 completo)

**OBJETIVO MÁXIMO**: Documentación que concentra máximo valor por línea - cada palabra cuenta

**Meta-concentración desde Layer 2:**
- methodology_guide.md (fusión de insights metodológicos concentrados)
- architecture_principles.md (síntesis arquitectural ultra-densa)
- implementation_guide.md (guía ejecutable concentrada)
- quick_reference.md (máxima densidad práctica)

**Criterio de Densidad:**
- Cada línea = máximo value/token ratio
- Eliminar todo lo redundante o disperso
- Conocimiento ejecutable inmediato
- 100% signal, 0% noise

**Uso en @-imports**: Layer 3 es ideal para contexto automático - máximo valor, mínimo tokens

### TRUTH_SOURCE.md: Autoridad Suprema (solo cuando Layer 3 completo)

Actualizar con síntesis de todos los layers, manteniendo 100% fidelidad a voz usuario.

### Fase Final: Actualización Automática de CLAUDE.md

**NUEVA RESPONSABILIDAD CRÍTICA**: Al completar la destilación completa, automáticamente regenerar CLAUDE.md bajo reglas estrictas:

**Proceso Obligatorio:**
1. Leer TODO el contexto sin sesgo: TRUTH_SOURCE.md + Layer 3 completo + docs/
2. Aplicar validación completa según docs/maintenance/validation.md
3. Regenerar CLAUDE.md desde cero (sin sesgo acumulativo)
4. Cumplir reglas estrictas de docs/maintenance/update_rules.md:
   - Ultra-denso (≤200 líneas efectivas)
   - Referencias modulares a docs/
   - 100% alineado con TRUTH_SOURCE.md
   - Estructura fija obligatoria

**CRITERIO DE ÉXITO**: CLAUDE.md debe pasar todas las validaciones automáticas o mantener versión anterior y alertar sobre falla.

**FLUJO COMPLETO**: Raw → Layer 1 → Layer 2 → Layer 3 → TRUTH_SOURCE.md → CLAUDE.md regeneración automática

## Convergencia automática

**Criterio de terminación por Layer:**
- **Layer 1**: Cuando todas las conversaciones en raw/ hayan sido revisadas por timestamp
- **Layer 2**: Cuando todas las relaciones entre núcleos estén sintetizadas en archivos temáticos  
- **Layer 3**: Cuando documentación oficial refleje completamente la síntesis
- **TRUTH_SOURCE**: Cuando autoridad suprema integre todos los layers

**Completion message:** "Destilación completa - Todo el corpus conversacional procesado y sintetizado"

**Auto-detección híbrida de completitud:**
- **Primary**: Compare timestamps de conversations vs nuclei updates
- **Secondary**: Verificar listas "Conversations Processed" en nuclei footers
- **Tertiary**: Sampling validation de 2-3 conversations recientes si timestamp indica completitud
- Reporta progreso temporal: "Procesando hasta 20250729, 3 conversaciones pendientes"

## Progreso conversacional únicamente

Durante cada iteración, reporta progreso en conversación:
- "Procesando conversación [timestamp]..."
- "Núcleos actualizados: metodologia_socratica.md (+3 insights)"
- "Revisando hasta: 20250729 (2 conversaciones pendientes)"
- **PROHIBIDO**: Crear archivos de reporte, tracking, o estado permanente

## Principios de eficiencia

- **Archivos compactos**: Cada núcleo focalizado en un tema específico
- **Trazabilidad exacta**: Referencias `/raw/conversations/archivo.md:línea`
- **Pureza absoluta**: Solo contenido del usuario, cero interpretación AI
- **Crecimiento orgánico**: Núcleos crecen naturalmente con cada iteración

## Ejecución

Ejecutar hasta convergencia automática. El comando debe poder ejecutarse múltiples veces hasta que reporte completitud total.