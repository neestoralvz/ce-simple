# CE-Simple: Context-Enabled Development System

Un sistema inteligente de desarrollo que prioriza la captura y gestión de contexto para crear soluciones que realmente cumplan las necesidades del usuario.

## 🎯 Visión del Proyecto

Este proyecto implementa un enfoque revolucionario al desarrollo de software donde **el contexto del usuario es el punto de partida** de toda decisión técnica. En lugar de asumir requisitos o implementar funcionalidades genéricas, el sistema captura sistemáticamente qué quiere lograr el usuario, por qué lo necesita, y bajo qué restricciones opera.

## 🚀 Características Principales

### Sistema de Entrevistas Dinámicas
- **Comando `/dynamic-interview`**: Conduce entrevistas inteligentes que se adaptan a las respuestas del usuario
- **Captura Contextual**: No solo QUÉ quiere el usuario, sino POR QUÉ y PARA QUÉ
- **Consolidación Automática**: Organiza información por temas, evitando fragmentación

### Gestión Inteligente de Documentación
- **Documentation-as-Knowledge**: La documentación evoluciona como un sistema vivo de gestión del conocimiento
- **Consolidación vs Fragmentación**: Se prioriza agrupar información relacionada en lugar de crear múltiples documentos
- **Context-Driven**: Toda documentación nace de necesidades reales capturadas del usuario

### Insights Organizados
- **Por Temas**: Frontend, backend, UX, restricciones técnicas, objetivos de negocio
- **Evolutivos**: Los documentos crecen y se refinan conforme se obtiene más contexto
- **Accionables**: Cada insight incluye próximos pasos y criterios de éxito claros

## 📁 Estructura del Proyecto

```
ce-simple/
├── .claude/
│   └── commands/
│       └── dynamic-interview.md     # Comando principal de entrevistas
├── docs/
│   ├── README.md                    # Sistema de documentación
│   └── context/
│       ├── README.md                # Gestión de contexto
│       └── insights/
│           └── README.md            # Documentación de insights
└── README.md                        # Este archivo
```

### Directorios Clave

#### `/actions:docs/context/insights/`
Aquí se almacenan todos los insights capturados de usuarios:
- `frontend-requirements.md` - Requisitos de interfaz
- `api-architecture.md` - Arquitectura de APIs
- `user-experience-goals.md` - Objetivos de UX
- `technical-constraints.md` - Limitaciones técnicas
- `business-objectives.md` - Objetivos de negocio

#### `/.claude/commands/`
Comandos personalizados para facilitar el flujo de trabajo:
- `dynamic-interview.md` - Sistema de entrevistas dinámicas

## 🎨 Filosofía de Desarrollo

### 1. Usuario Primero (User-First)
- Toda funcionalidad nace de una necesidad real del usuario
- Se captura el contexto completo antes de implementar
- Los criterios de éxito se definen desde la perspectiva del usuario

### 2. Contexto sobre Código (Context over Code)
- Se invierte más tiempo en entender el problema que en codificar la solución
- Cada decisión técnica se basa en contexto documentado
- El código es la manifestación del contexto, no el punto de partida

### 3. Evolución Orgánica (Organic Evolution)
- El sistema crece basado en necesidades reales, no en especulaciones
- La documentación evoluciona junto con el entendimiento del problema
- Se prioriza refinamiento sobre reescritura

### 4. Consolidación Inteligente (Intelligent Consolidation)
- Se evita la fragmentación de información relacionada
- Los insights se consolidan por temas coherentes
- Se mantiene una fuente única de verdad para cada área

## 🛠️ Cómo Usar el Sistema

### Para Capturar Nuevos Requisitos
1. **Ejecuta una entrevista dinámica:**
   ```
   /dynamic-interview
   ```
2. **El sistema automáticamente:**
   - Hace preguntas adaptativas basadas en tus respuestas
   - Identifica temas principales
   - Consolida la información en archivos existentes o crea nuevos según corresponda

### Para Consultar Información Existente
1. **Navega a `/actions:docs/context/insights/`**
2. **Busca el archivo relevante por tema**
3. **Consulta criterios de éxito y restricciones**
4. **Úsalo como referencia para desarrollo**

### Para Desarrolladores
1. **Antes de implementar:** Consulta insights relevantes en `/actions:docs/context/insights/`
2. **Durante desarrollo:** Valida que tu implementación cumple los criterios de éxito
3. **Al finalizar:** Actualiza insights si descubres nuevos requisitos

## 🎯 Casos de Uso

### Proyectos Nuevos
- Capturar requisitos completos antes de escribir código
- Entender restricciones y limitaciones desde el inicio
- Definir criterios de éxito claros y medibles

### Proyectos Existentes
- Documentar el contexto actual para nuevos miembros del equipo
- Capturar requisitos de nuevas funcionalidades
- Consolidar conocimiento fragmentado en diferentes fuentes

### Consultorías y Freelancing
- Entender completamente qué necesita el cliente
- Documentar acuerdos y expectativas claramente
- Facilitar comunicación continua durante el desarrollo

## 🔄 Flujo de Trabajo Típico

1. **Usuario solicita funcionalidad/proyecto**
2. **Se ejecuta `/dynamic-interview`**
3. **Sistema captura contexto completo:**
   - Objetivos específicos
   - Restricciones técnicas/temporales/presupuestarias
   - Criterios de éxito
   - Contexto de negocio
4. **Se documenta automáticamente en insights organizados**
5. **Desarrollo se basa en contexto capturado**
6. **Validación contra criterios de éxito documentados**

## 📈 Beneficios del Enfoque

### Para Usuarios/Clientes
- **Seguridad** de que sus necesidades reales fueron capturadas
- **Transparencia** en el proceso de desarrollo
- **Alineación** entre lo que necesitan y lo que se construye

### Para Desarrolladores
- **Claridad** sobre qué construir y por qué
- **Contexto completo** para tomar decisiones técnicas
- **Criterios objetivos** para validar completitud

### Para el Proyecto
- **Reducción de retrabajo** por malentendidos
- **Mejor calidad** al construir exactamente lo que se necesita
- **Documentación viva** que evoluciona con el proyecto

## 🚀 Próximos Pasos

Para empezar a usar el sistema:

1. **Ejecuta tu primera entrevista:**
   ```
   /dynamic-interview
   ```

2. **Explora los insights generados en:**
   ```
   docs/context/insights/
   ```

3. **Úsalos como referencia para tu desarrollo**

Este sistema está diseñado para evolucionar contigo y tu proyecto, capturando y organizando el conocimiento crítico que hace la diferencia entre construir software genérico y crear soluciones que realmente resuelven problemas reales.

---

**¿Listo para empezar?** Ejecuta `/dynamic-interview` y comienza a capturar el contexto que transformará tu desarrollo.