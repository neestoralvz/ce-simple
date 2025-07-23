# Mejores Prácticas de Prompt Engineering para Claude 4

Esta guía presenta técnicas específicas para optimizar el rendimiento de los modelos Claude 4 (Opus 4 y Sonnet 4), diseñados para un seguimiento de instrucciones más preciso que las generaciones anteriores.

## Principios Fundamentales

### Sé explícito con tus instrucciones

Claude 4 responde mejor a instrucciones claras y específicas. Detallar exactamente lo que deseas puede mejorar significativamente los resultados.

**❌ Menos efectivo:**
```text
Crea un dashboard de analíticas
```

**✅ Más efectivo:**
```text
Crea un dashboard de analíticas. Incluye todas las características e interacciones relevantes posibles. Ve más allá de lo básico para crear una implementación completamente funcional.
```

### Proporciona contexto para mejorar rendimiento

Explicar el "por qué" detrás de tus instrucciones ayuda a Claude 4 a entender mejor tus objetivos y entregar respuestas más precisas.

**❌ Menos efectivo:**
```text
NUNCA uses puntos suspensivos
```

**✅ Más efectivo:**
```text
Tu respuesta será leída en voz alta por un motor de texto a voz, así que nunca uses puntos suspensivos ya que el motor no sabrá cómo pronunciarlos.
```

**Beneficio:** Claude generaliza inteligentemente a partir de la explicación.

### Mantén vigilancia con ejemplos y detalles

Claude 4 presta atención meticulosa a detalles y ejemplos. Asegúrate de que tus ejemplos refuercen los comportamientos deseados y minimicen los no deseados.

## Guías para Situaciones Específicas

### Controlar el formato de respuestas

**Estrategias más efectivas:**

1. **Di qué hacer, no qué evitar**
   - ❌ "No uses markdown en tu respuesta"
   - ✅ "Tu respuesta debe componerse de párrafos de prosa fluida"

2. **Usa indicadores de formato XML**
   ```text
   Escribe las secciones de prosa en etiquetas <parrafos_prosa_fluida>
   ```

3. **Alinea el estilo del prompt con la salida deseada**
   - El formato de tu prompt influye en el estilo de respuesta de Claude
   - Remover markdown del prompt reduce markdown en la salida

### Aprovechar capacidades de pensamiento

Claude 4 ofrece capacidades de pensamiento especialmente útiles para:
- Reflexión después del uso de herramientas
- Razonamiento complejo de múltiples pasos

**Ejemplo de prompt:**
```text
Después de recibir resultados de herramientas, reflexiona cuidadosamente sobre su calidad y determina los próximos pasos óptimos antes de proceder. Usa tu pensamiento para planificar e iterar basándote en esta nueva información, luego toma la mejor acción siguiente.
```

### Optimizar llamadas paralelas de herramientas

Claude 4 excele en ejecución paralela de herramientas. Aunque tiene alta tasa de éxito sin prompting, este prompt alcanza ~100% de éxito:

```text
Para máxima eficiencia, cuando necesites realizar múltiples operaciones independientes, invoca todas las herramientas relevantes simultáneamente en lugar de secuencialmente.
```

### Reducir creación de archivos en codificación agéntica

Claude 4 puede crear archivos temporales para pruebas e iteración, especialmente con código Python como "borrador temporal".

**Para minimizar creación de archivos:**
```text
Si creas archivos temporales, scripts o archivos auxiliares para iteración, limpia estos archivos eliminándolos al final de la tarea.
```

### Mejorar generación de código visual y frontend

**Prompt base para diseños complejos:**
```text
No te contengas. Da todo de ti.
```

**Modificadores específicos para mejor rendimiento:**
- "Incluye todas las características e interacciones relevantes posibles"
- "Agrega detalles como estados hover, transiciones y micro-interacciones"
- "Crea una demostración impresionante que muestre capacidades de desarrollo web"
- "Aplica principios de diseño: jerarquía, contraste, equilibrio y movimiento"

### Evitar enfoque excesivo en pasar pruebas

Los modelos avanzados pueden enfocarse demasiado en hacer que las pruebas pasen a expensas de soluciones generales.

**Prompt para soluciones robustas:**
```text
Escribe una solución de alta calidad y propósito general. Implementa una solución que funcione correctamente para todas las entradas válidas, no solo los casos de prueba. No hardcodees valores ni crees soluciones que solo funcionen para entradas específicas de prueba. Implementa la lógica real que resuelve el problema de manera general.

Enfócate en entender los requisitos del problema e implementar el algoritmo correcto. Las pruebas están ahí para verificar corrección, no para definir la solución. Proporciona una implementación con principios que siga mejores prácticas y principios de diseño de software.

Si la tarea es irrazonable o inviable, o si alguna prueba es incorrecta, por favor dímelo. La solución debe ser robusta, mantenible y extensible.
```

## Consideraciones de Migración

### Migrar de Sonnet 3.7 a Claude 4

**1. Sé específico sobre el comportamiento deseado**
- Describe exactamente lo que quieres ver en la salida
- No asumas comportamientos implícitos

**2. Enmarca instrucciones con modificadores**
- Agrega modificadores que alienten a Claude a aumentar calidad y detalle
- Transforma prompts básicos en solicitudes completas

**Ejemplo de transformación:**
- ❌ "Crea un dashboard de analíticas"
- ✅ "Crea un dashboard de analíticas. Incluye todas las características e interacciones relevantes posibles. Ve más allá de lo básico para crear una implementación completamente funcional."

**3. Solicita características específicas explícitamente**
- Animaciones deben solicitarse explícitamente
- Elementos interactivos requieren mención específica
- Funcionalidades avanzadas no se asumen automáticamente

## Patrones de Prompts Efectivos

### Para Análisis y Reflexión
```text
Analiza [tema] considerando múltiples perspectivas. Reflexiona sobre las implicaciones y proporciona insights profundos con razonamiento claro.
```

### Para Código de Calidad
```text
Implementa [funcionalidad] siguiendo mejores prácticas de desarrollo. Prioriza legibilidad, mantenibilidad y rendimiento. Incluye manejo de errores apropiado.
```

### Para Contenido Creativo
```text
Crea [contenido] que sea engaging y original. Incluye detalles ricos, elementos interactivos y considera la experiencia del usuario final.
```

### Para Solución de Problemas
```text
Resuelve [problema] paso a paso. Explica tu razonamiento, considera casos edge y valida tu solución contra diferentes escenarios.
```

## Errores Comunes a Evitar

❌ **Instrucciones vagas o ambiguas**
- "Hazlo mejor" → "Mejora la legibilidad del código agregando comentarios descriptivos"

❌ **Ejemplos contradictorios**
- Verificar que todos los ejemplos refuercen el comportamiento deseado

❌ **Expectativas implícitas**
- "Claude debería saber qué quiero" → Especificar claramente requisitos

❌ **Prompts negativos excesivos**
- "No hagas X, Y, Z" → "Haz A, enfócate en B, prioriza C"

## Resultados Esperados

**Con estas prácticas, deberías obtener:**
- ✅ Respuestas más precisas y alineadas con objetivos
- ✅ Código de mayor calidad y funcionalidad
- ✅ Contenido más detallado y completo
- ✅ Mejor seguimiento de instrucciones específicas
- ✅ Soluciones más robustas y generalizables

---

**Recursos adicionales:**
- Documentación de Extended Thinking: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
- API de Claude: https://docs.anthropic.com
- Soporte: https://support.anthropic.com