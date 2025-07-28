# Documentation System

Este directorio contiene el sistema de documentación del proyecto, diseñado para capturar, organizar y mantener todo el conocimiento crítico del proyecto de manera estructurada y accesible.

## Arquitectura del Sistema

### `/context/` - Sistema de Gestión de Contexto
El núcleo del sistema de documentación, enfocado en capturar y mantener el contexto del proyecto:

#### `/context/insights/` - User Insights
- **Propósito:** Capturar información directa de usuarios através de entrevistas dinámicas
- **Contenido:** Objetivos, requisitos, restricciones, criterios de éxito
- **Proceso:** Uso del comando `/dynamic-interview` con consolidación automática
- **Organización:** Por temas, con consolidación inteligente para evitar fragmentación

## Filosofía de Documentación

### Principios Core

#### 1. Documentation-as-Knowledge-Management
La documentación no es solo información estática, sino un sistema vivo de gestión del conocimiento que:
- **Evoluciona** conforme el proyecto crece y cambia
- **Consolida** información relacionada para evitar fragmentación
- **Facilita** la toma de decisiones basada en contexto completo
- **Preserva** el razonamiento detrás de las decisiones

#### 2. Context-Driven Documentation
Toda documentación está impulsada por el contexto real del proyecto:
- **User-Centric:** Se origina en necesidades reales capturadas de usuarios
- **Purpose-Driven:** Cada documento tiene un propósito claro y medible
- **Living Documents:** Se actualiza continuamente conforme evoluciona el contexto
- **Interconnected:** Los documentos se referencian y apoyan mutuamente

#### 3. Consolidation Over Fragmentation
Se prioriza la consolidación inteligente sobre la creación de múltiples documentos fragmentados:
- **Theme-Based Organization:** Agrupación por temas coherentes
- **Intelligent Merging:** Combinación automática de información relacionada
- **Version Evolution:** Los documentos crecen y se refinan en lugar de multiplicarse
- **Single Source of Truth:** Cada tema tiene una ubicación autoritativa

## Flujo de Trabajo de Documentación

### 1. Captura (Capture)
```
Real Need → Dynamic Interview → Structured Documentation
```
- **Origen:** Necesidades reales identificadas en conversación con usuarios
- **Método:** Entrevistas dinámicas usando `/dynamic-interview`
- **Output:** Insights estructurados en `/context/insights/`

### 2. Consolidación (Consolidate)
```
New Information → Theme Analysis → Merge or Create → Update Cross-references
```
- **Análisis:** Determinación de temas existentes vs nuevos
- **Decisión:** Consolidar en documento existente o crear nuevo
- **Integración:** Incorporación manteniendo coherencia y eliminando duplicación

### 3. Evolución (Evolve)
```
Changing Context → Impact Analysis → Selective Updates → Validation
```
- **Monitoreo:** Identificación de cambios en el contexto del proyecto
- **Análisis:** Evaluación del impacto en documentación existente
- **Actualización:** Modificaciones selectivas manteniendo integridad del sistema

### 4. Aplicación (Apply)
```
Development Need → Context Lookup → Information Extraction → Decision Support
```
- **Consulta:** Búsqueda de información relevante para decisiones de desarrollo
- **Extracción:** Obtención de información específica y contextualizada
- **Aplicación:** Uso de la información para guiar implementación y diseño

## Herramientas y Comandos

### Sistema de Entrevistas
- **`/dynamic-interview`** - Conduce entrevistas estructuradas para capturar insights del usuario
  - Preguntas adaptativas basadas en respuestas previas
  - Identificación automática de temas
  - Consolidación inteligente con información existente

### Gestión de Documentación (Futuro)
- **`/consolidate-docs`** - Analiza y consolida documentación fragmentada
- **`/search-context`** - Búsqueda inteligente en toda la documentación
- **`/validate-completeness`** - Verifica completitud de documentación por área
- **`/generate-summary`** - Crea resúmenes ejecutivos de áreas específicas

## Estructura de Archivos

### Nomenclatura Estándar
```
[categoria]-[tema-principal]-[subtema].md
```

**Ejemplos:**
- `frontend-requirements.md` - Requisitos de frontend
- `api-architecture-design.md` - Diseño de arquitectura de API
- `user-experience-goals.md` - Objetivos de UX
- `business-objectives-roi.md` - Objetivos de negocio y ROI

### Templates y Formatos
Cada tipo de documento sigue templates específicos para mantener consistencia:

#### User Insights Template
```markdown
# [Título del Insight]
## Contexto de la Entrevista
## Resumen Ejecutivo  
## Objetivos Identificados
## Requisitos Específicos
## Restricciones y Limitaciones
## Criterios de Éxito
## Notas Adicionales
## Próximos Pasos Sugeridos
## Historial de Actualizaciones
```

## Casos de Uso por Rol

### Product Owners / Project Managers
- **Captura de Requirements:** Usar `/dynamic-interview` para documentar requisitos completos
- **Tracking de Evolución:** Monitorear cambios en objetivos y prioridades
- **Comunicación con Stakeholders:** Referenciar documentación autoritativa
- **Planning y Roadmapping:** Basar decisiones en contexto documentado

### Developers
- **Context Understanding:** Consultar `/context/insights/` antes de implementar
- **Requirement Validation:** Verificar implementaciones contra criterios documentados
- **Architecture Decisions:** Referenciar restricciones y objetivos técnicos
- **Code Reviews:** Validar alineación con requisitos capturados

### Designers
- **User Understanding:** Consultar insights sobre objetivos de experiencia
- **Constraint Awareness:** Conocer limitaciones técnicas y de negocio
- **Success Criteria:** Alinear diseños con criterios de éxito definidos
- **Iteration Planning:** Basar iteraciones en feedback capturado

### QA/Testing
- **Test Case Development:** Crear casos basados en criterios de éxito
- **Scenario Understanding:** Conocer contextos de uso críticos
- **Acceptance Criteria:** Validar completitud contra requisitos documentados
- **Bug Prioritization:** Entender impacto basado en objetivos del usuario

## Métricas de Calidad

### Completitud
- ¿Están documentados todos los aspectos críticos del proyecto?
- ¿Se capturó suficiente contexto para tomar decisiones informadas?
- ¿Hay gaps obvios en la información disponible?

### Actualidad
- ¿La documentación refleja el estado actual del proyecto?
- ¿Se actualizan los documentos cuando cambia el contexto?
- ¿Hay información obsoleta que necesita limpieza?

### Accesibilidad
- ¿Es fácil encontrar información específica cuando se necesita?
- ¿La organización es intuitiva para todos los roles?
- ¿Los templates facilitan la consulta rápida?

### Utilidad
- ¿La documentación realmente ayuda en la toma de decisiones?
- ¿Se consulta regularmente durante el desarrollo?
- ¿Facilita la incorporación de nuevos miembros del equipo?

## Evolución del Sistema

### Adaptación Continua
El sistema de documentación evoluciona basado en:
- **Feedback de Uso:** Cómo se usa realmente la documentación
- **Nuevas Necesidades:** Qué información adicional se requiere
- **Eficiencia:** Dónde se pueden optimizar procesos
- **Calidad:** Cómo mejorar la utilidad y accesibilidad

### Expansión Futura
Áreas planificadas para expansión:
- **Technical Architecture:** Documentación de decisiones técnicas
- **Process Documentation:** Workflows y procedimientos
- **Decision Records:** ADRs (Architecture Decision Records)
- **Lessons Learned:** Captura de aprendizajes y mejores prácticas

Este sistema de documentación está diseñado para crecer orgánicamente con el proyecto, manteniendo siempre la relevancia y utilidad para todos los miembros del equipo.