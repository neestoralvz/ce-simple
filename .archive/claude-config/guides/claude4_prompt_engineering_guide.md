# Guía Práctica: Prompt Engineering para Claude 4

Técnicas específicas para maximizar el rendimiento de Claude 4 (Opus 4 y Sonnet 4), modelos entrenados para seguimiento de instrucciones más preciso que generaciones anteriores.

## Principios Esenciales

### 1. Instrucciones explícitas y detalladas

Claude 4 requiere especificidad. Los comportamientos "extra" de modelos anteriores ahora deben solicitarse explícitamente.

**❌ Vago e inefectivo:**
```
Crea un dashboard de analíticas
```

**✅ Específico y efectivo:**
```
Crea un dashboard de analíticas completo. Incluye todas las características e interacciones relevantes: gráficos interactivos, filtros dinámicos, métricas en tiempo real y exportación de datos. Ve más allá de lo básico para una implementación totalmente funcional.
```

### 2. Contexto que justifica las instrucciones

Explicar el "por qué" mejora significativamente la comprensión y ejecución.

**❌ Comando sin contexto:**
```
NUNCA uses puntos suspensivos
```

**✅ Instrucción contextualizada:**
```
Tu respuesta será procesada por un motor de texto a voz, así que evita puntos suspensivos porque el sistema no puede pronunciarlos correctamente.
```

**Resultado:** Claude generaliza inteligentemente la regla a situaciones similares.

### 3. Ejemplos y detalles consistentes

Claude 4 analiza meticulosamente cada ejemplo. Asegúrate de que refuercen exactamente el comportamiento deseado.

## Técnicas Específicas por Situación

### Controlar formato de respuesta

**Estrategia 1: Instrucciones positivas**
- ❌ "No uses markdown en tu respuesta"
- ✅ "Escribe en párrafos de prosa fluida sin formato especial"

**Estrategia 2: Indicadores XML estructurales**
```
Organiza tu respuesta usando estas etiquetas:
<introduccion>Resumen ejecutivo</introduccion>
<desarrollo>Análisis detallado</desarrollo>
<conclusion>Recomendaciones finales</conclusion>
```

**Estrategia 3: Alineación estilo prompt-salida**
- Tu estilo de escritura en el prompt influye directamente en la respuesta
- Prompt formal → Respuesta formal
- Prompt casual → Respuesta casual

### Aprovechar capacidades de pensamiento

Para tareas que requieren reflexión profunda o análisis de múltiples pasos:

```
Después de recibir resultados de herramientas, dedica tiempo a reflexionar sobre:
1. Calidad y relevancia de los datos obtenidos
2. Posibles próximos pasos basados en esta información
3. Estrategia óptima antes de proceder

Usa tu capacidad de pensamiento para planificar iterativamente, luego ejecuta la mejor acción.
```

### Optimizar uso paralelo de herramientas

Claude 4 excele en ejecución paralela. Este prompt alcanza ~100% de éxito:

```
Para máxima eficiencia: cuando necesites realizar múltiples operaciones independientes, ejecuta todas las herramientas relevantes simultáneamente en lugar de una por una.
```

### Gestionar creación de archivos en desarrollo

Claude 4 usa archivos temporales como "borrador" para mejorar resultados, especialmente en Python.

**Para minimizar archivos residuales:**
```
Si necesitas crear archivos temporales, scripts o helpers durante el desarrollo, elimínalos automáticamente al completar la tarea para mantener el workspace limpio.
```

### Potenciar generación de código frontend

**Prompt base para diseños ambiciosos:**
```
Crea una implementación impresionante. No escatimes en características, interactividad o detalles visuales.
```

**Modificadores específicos:**
- "Incluye microinteracciones sofisticadas y estados hover detallados"
- "Implementa transiciones fluidas y animaciones significativas"
- "Demuestra capacidades avanzadas de desarrollo web moderno"
- "Aplica principios de diseño: jerarquía visual, contraste efectivo, equilibrio y movimiento dinámico"

### Evitar soluciones limitadas a casos de prueba

Prevenir que Claude se enfoque solo en pasar tests específicos:

```
Desarrolla una solución robusta y de propósito general que:

1. Funcione correctamente para TODAS las entradas válidas, no solo casos de prueba
2. Implemente la lógica real del problema, no soluciones hardcodeadas
3. Siga principios de ingeniería de software y mejores prácticas
4. Sea mantenible, extensible y reutilizable

Las pruebas verifican corrección, no definen la solución. Si encuentras pruebas incorrectas o requisitos irrealizables, comunícalo claramente.
```

## Guía de Migración: Sonnet 3.7 → Claude 4

### Cambio 1: Especificidad obligatoria

**Antes (Sonnet 3.7):**
```
Analiza estos datos
```

**Ahora (Claude 4):**
```
Analiza estos datos realizando: estadísticas descriptivas, identificación de patrones, detección de anomalías y recomendaciones accionables. Presenta hallazgos con visualizaciones claras.
```

### Cambio 2: Modificadores de calidad

Transforma prompts básicos añadiendo modificadores que eleven el estándar:

**Transformación tipo:**
- Base: "Crea una página web"
- Mejorado: "Crea una página web profesional con diseño responsive, interacciones pulidas y experiencia de usuario excepcional"

### Cambio 3: Solicitudes explícitas de características

**Elementos que requieren mención específica:**
- ✅ Animaciones y transiciones
- ✅ Interactividad avanzada
- ✅ Responsive design
- ✅ Accesibilidad
- ✅ Optimización de rendimiento

## Plantillas de Prompts Efectivos

### Para análisis profundo
```
Analiza [tema] considerando:
- Múltiples perspectivas y stakeholders
- Implicaciones a corto y largo plazo
- Riesgos y oportunidades
- Recomendaciones priorizadas y accionables

Proporciona insights que vayan más allá de lo obvio.
```

### Para código de calidad enterprise
```
Implementa [funcionalidad] siguiendo estándares enterprise:
- Arquitectura escalable y mantenible
- Manejo robusto de errores y casos edge
- Documentación completa y testing
- Seguridad y rendimiento optimizados
```

### Para contenido creativo excepcional
```
Crea [contenido] que destaque por:
- Originalidad y perspectiva única
- Elementos interactivos y engagement alto
- Atención meticulosa al detalle
- Experiencia memorable para el usuario final
```

### Para solución de problemas complejos
```
Resuelve [problema] mediante:
1. Análisis exhaustivo del contexto y restricciones
2. Exploración de múltiples enfoques posibles
3. Implementación de la solución más robusta
4. Validación contra diversos escenarios y edge cases
```

## Errores Críticos que Evitar

### ❌ Instrucciones ambiguas
**Problema:** "Mejora esto"
**Solución:** "Optimiza el rendimiento reduciendo tiempo de carga en 50% y mejorando accesibilidad según WCAG 2.1"

### ❌ Ejemplos contradictorios
**Problema:** Mostrar tanto buenos como malos ejemplos sin distinguir claramente
**Solución:** Etiquetar explícitamente ✅ "Hacer así" vs ❌ "Evitar esto"

### ❌ Expectativas implícitas
**Problema:** Asumir que Claude "debería saber" qué quieres
**Solución:** Especificar todos los requisitos, incluso los que parecen obvios

### ❌ Instrucciones principalmente negativas
**Problema:** Lista extensa de "no hagas esto"
**Solución:** Enfocarse en "haz esto específicamente"

## Métricas de Éxito

**Con estas prácticas deberías obtener:**
- 🎯 **90%+ precisión** en seguimiento de instrucciones
- 🚀 **Código más robusto** con menos iteraciones necesarias
- 💡 **Soluciones más creativas** que superan expectativas básicas
- ⚡ **Respuestas más eficientes** que ahorran tiempo de desarrollo
- 🔧 **Salidas más utilizables** que requieren menos refinamiento manual

---

**Recursos para profundizar:**
- [Extended Thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) - Capacidades de pensamiento avanzado
- [API Documentation](https://docs.anthropic.com) - Implementación técnica
- [Support](https://support.anthropic.com) - Asistencia técnica