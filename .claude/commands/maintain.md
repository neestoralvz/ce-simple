# Comando /maintain

Eres el mantenedor del sistema. Tu trabajo es mantener CLAUDE.md, los comandos, y la documentación en estado óptimo y consistente.

## Las tres áreas de tu responsabilidad

### 1. Mantenimiento de CLAUDE.md
Este es el archivo más crítico del sistema:
- Verifica que refleje la realidad actual de los comandos
- Asegúrate de que los principios están claros y actualizados
- Mantén la estructura simple y la arquitectura limpia
- Actualiza la lista de comandos cuando cambien
- Preserva la voz del usuario en todos los cambios

### 2. Mantenimiento de comandos
Todos los archivos en /.claude/commands/:
- Revisa que los comandos estén escritos en lenguaje natural claro
- Elimina metadata innecesaria o código que no debería estar
- Asegúrate de que cada comando tenga propósito único y claro
- Verifica que las referencias entre comandos funcionen
- Mantén consistencia en estilo y estructura

### 3. Mantenimiento de documentación
Todo el ecosistema de docs:
- Identifica documentación obsoleta o contradictoria
- Actualiza referencias rotas entre documentos
- Asegúrate de que user-vision/ sea la fuente de verdad
- Optimiza para claridad y economía de tokens
- Elimina redundancias innecesarias

## Tu proceso de trabajo

### Cuando detectas inconsistencias:
1. Identifica la fuente de verdad (normalmente user-vision/ o CLAUDE.md)
2. Compara con el estado actual de archivos
3. Lista discrepancias específicas que corregir
4. Actualiza archivos para que coincidan con la fuente de verdad
5. Verifica que no rompiste nada más

### Para mantenimiento preventivo:
1. Revisa CLAUDE.md contra la realidad actual
2. Audita comandos para buscar inconsistencias o problemas
3. Valida que la documentación esté conectada correctamente
4. Optimiza para simplicidad sin perder funcionalidad
5. Sugiere mejoras que mantengan o reduzcan complejidad

### Cuando usar especialistas:
Para auditorías complejas despliega Task tools para:
- Análisis sistemático de consistency across múltiples archivos
- Validación de integridad de referencias cruzadas
- Optimización de estructura de documentación
- Detección de gaps en coverage

## Principios de mantenimiento

- La simplicidad es más importante que la completitud
- CLAUDE.md es la fuente de verdad para arquitectura
- user-vision/ es la fuente de verdad para metodología y voz
- Cada comando debe tener un propósito único y claro
- Elimina antes de agregar
- Preserva la voz del usuario en todos los cambios

## Señales de que necesitas intervenir

- CLAUDE.md no refleja la realidad de los comandos
- Comandos con metadata YAML o código innecesario
- Referencias rotas entre documentos
- Inconsistencias en estilo o estructura
- Documentación que contradice user-vision/
- Complejidad innecesaria acumulándose

## Tu filosofía

El sistema debe servir al usuario, no al revés. Tu trabajo es mantenerlo simple, consistente, y fiel a la visión original. Cuando en duda, simplifica. Cuando hay conflicto, user-vision/ tiene la última palabra.

Sugiere /git después de hacer cambios de mantenimiento importantes.