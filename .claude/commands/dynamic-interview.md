---
contextflow:
  purpose: "Dynamic intelligent user interview for requirement gathering"
  triggers: ["dynamic interview", "user interview", "requirement gathering"]
  next: ["analyze", "implement", "create-doc", "meta-narrative"]
  requires-subagent: true
  auto-chain: false
  research-driven: true
  communication-rules:
    - "NUNCA bash echo para comunicar con usuario"
    - "SIEMPRE Task tools → Main agent → Usuario"
    - "Interactive interview methodology"
    - "Adaptive questioning based on responses"
  decision-tree:
    use-when:
      - "User objectives unclear or complex"
      - "Requirement gathering session needed"
      - "Strategic planning input required"
    alternatives: ["analyze", "explore", "meta-narrative"]
    semantic-triggers:
      - "interview" / "questions" / "gather requirements"
      - "dynamic interview" / "user analysis"
      - "objective clarification" / "preference gathering"
---

# Dynamic User Interview Command

Realiza una entrevista dinámica e inteligente al usuario para entender completamente qué quiere hacer, sus objetivos, restricciones y preferencias.

## Objective
Recopilar información detallada sobre los objetivos del usuario a través de preguntas estratégicas que se adapten a las respuestas previas.

## Instructions

### 1. Análisis de Contexto Inicial
Primero, analiza cualquier información ya disponible sobre el proyecto o contexto actual:
- Revisa archivos existentes en docs/context/insights/
- Examina la estructura del proyecto
- Identifica temas ya documentados vs áreas que necesitan exploración

### 2. Estrategia de Entrevista Dinámica
Conduce la entrevista siguiendo estos principios:

**Inicio Abierto:**
- Comienza con: "Cuéntame qué quieres lograr o en qué necesitas ayuda"
- Escucha activamente y identifica palabras clave y conceptos principales

**Preguntas de Profundización Adaptativas:**
Basándote en la respuesta inicial, formula preguntas que exploren:
- **Objetivos específicos:** ¿Cuál es el resultado final que buscas?
- **Contexto:** ¿En qué situación o proyecto se enmarca esto?
- **Restricciones:** ¿Qué limitaciones de tiempo, recursos o tecnología tienes?
- **Experiencia previa:** ¿Has intentado algo similar antes?
- **Criterios de éxito:** ¿Cómo sabrás que has logrado tu objetivo?
- **Urgencia:** ¿Qué tan prioritario es esto?

**Técnicas de Indagación:**
- Haz preguntas abiertas que inviten a la elaboración
- Usa preguntas de seguimiento como "¿Puedes dar un ejemplo?" o "¿Qué quieres decir exactamente con...?"
- Reformula y confirma entendimiento: "Entonces, si entiendo bien..."
- Explora el "por qué" detrás de los requisitos

### 3. Categorización de Temas
Durante la entrevista, identifica y categoriza los temas emergentes:
- **Técnicos:** Implementación, arquitectura, herramientas
- **Funcionales:** Características, comportamientos, casos de uso
- **No funcionales:** Performance, seguridad, usabilidad
- **Contextuales:** Stakeholders, cronograma, ambiente
- **Estratégicos:** Visión, objetivos de negocio, ROI

### 4. Documentación de Insights
Al finalizar la entrevista:

**Análisis de Temas:**
- Identifica si los temas discutidos ya existen en docs/context/insights/
- Para temas existentes: consolida y actualiza la información
- Para temas nuevos: crea nuevos archivos de insight

**Estructura de Documentación:**
Cada insight debe incluir:
```markdown
# [Tema del Insight]

## Contexto de la Entrevista
- Fecha: [fecha]
- Usuario: [identificador si aplicable]
- Sesión: [número de sesión]

## Resumen Ejecutivo
[1-2 párrafos con los puntos clave]

## Objetivos Identificados
- [objetivo 1]
- [objetivo 2]
- ...

## Requisitos Específicos
- [requisito 1]
- [requisito 2]
- ...

## Restricciones y Limitaciones
- [restricción 1]
- [restricción 2]
- ...

## Criterios de Éxito
- [criterio 1]
- [criterio 2]
- ...

## Notas Adicionales
[Observaciones, ideas, conexiones con otros temas]

## Próximos Pasos Sugeridos
- [acción 1]
- [acción 2]
- ...

## Historial de Actualizaciones
- [fecha]: Insight inicial
- [fecha]: [descripción de actualización]
```

### 5. Consolidación Inteligente
Cuando actualices insights existentes:
- Mantén la información previa relevante
- Integra nueva información sin duplicar
- Actualiza fechas y versiones
- Nota conflictos o cambios en requisitos
- Sugiere reconciliación si hay inconsistencias

### 6. Seguimiento y Próximos Pasos
Al finalizar:
- Resume los insights capturados
- Sugiere próximos pasos o áreas para explorar
- Identifica si se necesitan entrevistas de seguimiento
- Propón un plan de acción basado en la información recopilada

## Output
Genera automáticamente los archivos de insight en docs/context/insights/ usando nomenclatura clara y descriptiva (ej: `frontend-requirements.md`, `api-architecture.md`, `user-experience-goals.md`).

## Tips para Entrevistas Efectivas
- Mantén un tono conversacional y amigable
- No asumas conocimiento técnico del usuario
- Haz una pregunta a la vez
- Da tiempo para pensar antes de la siguiente pregunta
- Confirma entendimiento antes de continuar
- Toma notas de palabras clave y frases exactas del usuario