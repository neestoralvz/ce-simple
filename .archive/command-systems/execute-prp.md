Comando: /execute-prp
Ubicación: .claude/commands/execute-prp.md

Ejecuta el PRP con disciplina estricta: $ARGUMENTS

PROTOCOLO DE EJECUCIÓN
PASO 1: CARGA Y VALIDACIÓN
LEER el PRP completo desde: $ARGUMENTS

VALIDAR que contiene:

 Objetivo claro
 Plan de implementación detallado
 Criterios de éxito definidos
 Investigación requerida especificada
SI falta algo crítico:

❌ ERROR: PRP incompleto
Falta: [sección faltante]
Acción: Completar PRP antes de ejecutar
PASO 2: INVESTIGACIÓN INICIAL
EJECUTAR toda la investigación especificada en el PRP:

bash
# Para cada ítem en "INVESTIGACIÓN REQUERIDA"
1. EXPLORAR archivos mencionados
2. BUSCAR información externa listada  
3. RESPONDER preguntas planteadas
4. APLICAR hints de exploración
5. DOCUMENTAR hallazgos relevantes
SI encuentras información que contradice el PRP:

DOCUMENTAR la discrepancia
EVALUAR impacto
DECIDIR si continuar o escalar
PASO 3: PLAN DE TAREAS DETALLADO
CREAR checklist granular desde el PRP:

markdown
## Plan de Ejecución

### Fase 1: [Nombre]
- [ ] Tarea 1.1: [descripción específica]
- [ ] Tarea 1.2: [descripción específica]
- [ ] Validación: [cómo verificar fase completa]

### Fase 2: [Nombre]
- [ ] Tarea 2.1: [descripción específica]
[...]
ESTIMAR tiempo para cada tarea

PASO 4: EJECUCIÓN DISCIPLINADA
Para CADA fase del plan:

4.1 IMPLEMENTAR
Seguir el plan EXACTAMENTE como está escrito
NO improvisar sin justificación documentada
SI algo no está claro → FALLAR, no adivinar
4.2 VALIDAR
Ejecutar validaciones especificadas para la fase
Correr tests relevantes
Verificar criterios de éxito parciales
NO proceder si la validación falla
4.3 COMMIT (si apropiado)
bash
git add [archivos de esta fase]
git commit -m "[tipo]: [descripción de la fase]

- Implementado: [qué se hizo]
- Validado: [qué se verificó]
- Siguiente: [próxima fase]"
PASO 5: TESTING EXHAUSTIVO
IMPLEMENTAR todos los tests especificados:

bash
# Tests unitarios
- Cobertura completa de nueva funcionalidad
- Edge cases identificados en PRP
- Validaciones de entrada/salida

# Tests de integración  
- Flujos end-to-end completos
- Interacciones entre componentes
- Escenarios reales de uso

# Tests de regresión
- Verificar funcionalidad existente
- Confirmar no breaking changes
IMPORTANTE:

NO usar mocks para "hacer pasar" tests
Tests deben validar comportamiento REAL
Si un test falla, arreglar código, NO el test
PASO 6: VALIDACIÓN DE CRITERIOS
Para CADA criterio en "CRITERIOS DE ÉXITO":

markdown
### Criterio: [nombre]
Estado: ✅ CUMPLIDO / ❌ NO CUMPLIDO
Evidencia: [cómo se verificó]
AUTOMATIZAR verificaciones donde sea posible:

bash
# Ejemplo para performance
npm run benchmark
# Expected: <200ms response time ✅
PASO 7: DOCUMENTACIÓN
ACTUALIZAR según el PRP:

README.md: Nueva funcionalidad y uso
CHANGELOG.md: Entry descriptivo
Código: Comentarios en lógica compleja
API Docs: Si hay nuevos endpoints
Migration Guide: Si hay breaking changes
PASO 8: REPORTE FINAL
GENERAR resumen de ejecución:

markdown
# Reporte de Ejecución PRP

**PRP:** [nombre]  
**Inicio:** [timestamp]  
**Fin:** [timestamp]  
**Duración:** [total]

## Progreso
- Fases completadas: X/Y
- Tareas completadas: N/M  
- Tests: [pasando/total]
- Cobertura: XX%

## Criterios de Éxito
✅ [Criterio 1]: Cumplido
✅ [Criterio 2]: Cumplido
❌ [Criterio 3]: No cumplido - [razón]

## Commits
- [sha1]: Fase 1 - Descripción
- [sha2]: Fase 2 - Descripción

## Observaciones
[Cualquier desviación del plan y justificación]

## Siguiente Paso
[Si algo quedó pendiente o recomendaciones]
MANEJO DE EXCEPCIONES
Si encuentras un BLOCKER:
markdown
🚨 BLOCKER ENCONTRADO

**Fase:** [dónde ocurrió]
**Issue:** [descripción precisa]
**Intentos:** [qué se probó]
**Impacto:** [qué no se puede continuar]

**Opciones:**
1. [Posible solución 1]
2. [Posible solución 2]

**Recomendación:** [tu análisis]

⏸️ EJECUCIÓN PAUSADA - Esperando decisión
Si necesitas DESVIAR del plan:
markdown
📝 DESVIACIÓN PROPUESTA

**Original:** [qué decía el PRP]
**Propuesto:** [qué quieres hacer]
**Razón:** [justificación detallada]
**Impacto:** [qué cambia]

¿Proceder con desviación? [ESPERANDO CONFIRMACIÓN]
PRINCIPIOS RECTORES
El PRP es la fuente de verdad - No lo contradigas
Disciplina > Creatividad - Sigue el plan
Validar > Asumir - Siempre verifica
Comunicar > Improvisar - Escala dudas
Completitud > Velocidad - Hazlo bien
RECORDATORIO FINAL
Un PRP bien ejecutado resulta en:

✅ Implementación que funciona al primer intento
✅ Cero sorpresas durante desarrollo
✅ Todos los criterios cumplidos
✅ Código mantenible y documentado
✅ Confianza en el resultado
