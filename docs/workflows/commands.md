# Filosofía y Documentación de los 9 Comandos

## Filosofía de Comandos

### Cada Comando Es:
- **Instrucciones puras**: Solo lenguaje natural dirigido al LLM
- **Sin metadata**: Cero YAML, código, o estructuras técnicas  
- **Propósito único**: Una responsabilidad clara y específica
- **Independiente**: Funciona solo pero se coordina con otros
- **Conversacional**: Escrito como si hablaras con el LLM directamente

### Principio de Separación Clara de Responsabilidades
**FUNDAMENTAL**: Un comando = Una responsabilidad inequívoca

**Criterios de Diseño**:
- **Responsabilidad única**: Cada comando tiene un propósito específico y limitado
- **Límites bien definidos**: Fronteras claras sobre qué hace y qué NO hace
- **Sin scope creep**: Resistir agregar "solo una funcionalidad más"
- **Composabilidad limpia**: Comandos se combinan sin conflicto de responsabilidades

**Anti-Patrones Prohibidos**:
- Comandos que hacen "un poquito de todo"
- Funciones mezcladas sin límites claros
- Expansión sistémica sin justificación específica

### Principio de Independencia
Los comandos son autocontenidos entre ellos y solo pueden conectarse con otros comandos. Cada uno debe ser capaz de ejecutarse sin dependencias complejas.

## Los 9 Comandos Independientes

### `/start` - Activación de Sesión
**Propósito**: Activación de sesión con carga de contexto
**Responsabilidad**: Orientar y preparar el contexto para la conversación
**Coordina con**: Todos los comandos (punto de entrada)

### `/distill` - Destilación Completa  
**Propósito**: Destilación completa de 5 capas: Raw → Visión Consolidada
**Responsabilidad**: Procesar conversaciones raw hacia insights cristalizados
**Coordina con**: `/close` para captura, todos los comandos para evolución

**NUEVA FUNCIONALIDAD**: Culmina con actualización automática de CLAUDE.md bajo reglas estrictas

### `/docs` - Workflow de Documentos
**Propósito**: Workflow de creación y edición de documentos  
**Responsabilidad**: Manejo inteligente de documentación del sistema
**Coordina con**: `/maintain` para consistencia, `/git` para commits

### `/explore` - Navegación del Codebase
**Propósito**: Navegación y comprensión del codebase
**Responsabilidad**: Investigación y análisis de código existente
**Coordina con**: `/debug` para resolución, `/docs` para documentación

### `/debug` - Resolución Sistemática
**Propósito**: Resolución sistemática de problemas
**Responsabilidad**: Diagnóstico y solución de issues técnicos  
**Coordina con**: `/explore` para investigación, `/git` para fixes

### `/maintain` - Mantenimiento del Sistema
**Propósito**: Mantenimiento del sistema (CLAUDE.md + comandos + docs)
**Responsabilidad**: Asegurar consistencia del ecosistema completo
**Coordina con**: Todos los comandos para salud sistémica

### `/git` - Workflow Git Integrado
**Propósito**: Workflow Git integrado con otros comandos  
**Responsabilidad**: Manejo inteligente de versionado y commits
**Coordina con**: Todos los comandos para commits contextuales

### `/partner` - Socio Constructor
**Propósito**: Agente socio constructor para enfoque y simplicidad
**Responsabilidad**: Validar decisiones arquitecturales y mantener simplicidad
**Coordina con**: Todos los comandos como validator de decisiones

### `/close` - Captura y Commit
**Propósito**: Captura de conversación y commit de cambios
**Responsabilidad**: Cerrar sesión preservando insights y cambios
**Coordina con**: `/git` para commits, `/distill` para procesamiento futuro  

## Coordinación Entre Comandos

### Flujo Principal
```
/start → orienta y carga contexto
otros comandos → ejecutan tareas específicas
/close → captura conversación y commit cambios
```

### Integraciones Clave
```  
/git → se integra con todos para commits inteligentes
/partner → valida decisiones arquitecturales en cualquier momento
/maintain → asegura consistencia del ecosistema completo
/distill → actualiza CLAUDE.md automáticamente al final
```

### Orquestación de Subagentes
El agente principal SIEMPRE debe comportarse como orquestador de subagentes, no como ejecutor directo de todas las tareas.

## Características Técnicas

### Solo Instrucciones de Lenguaje Natural
Cada comando es un archivo de texto puro con instrucciones dirigidas al LLM. Sin código, sin metadata, sin estructuras técnicas complejas.

### Conversacional y Directo
Los comandos están escritos como si le hablaras directamente al LLM, usando lenguaje natural y conversacional.

### Autocontenidos pero Coordinados
Cada comando puede ejecutarse independientemente, pero sabe cómo coordinar con otros cuando es necesario.

### Evolución Orgánica
Los comandos evolucionan a través del proceso de conversación → destilación → cristalización, manteniendo simplicidad.

## Principios de Mantenimiento

### Anti-Complejidad
- Resistir agregar metadata o estructuras técnicas
- Mantener instrucciones claras y directas
- Evitar interdependencias complejas
- Preservar independencia funcional

### Enforcement de Separación de Responsabilidades
- **Validación en diseño**: Todo nuevo comando debe pasar test de responsabilidad única
- **Challenger automático**: /partner debe validar que comandos mantengan su scope original
- **Revisión periódica**: Comandos existentes deben ser evaluados bajo principio de separación
- **Rechazo de expansión**: "Solo una funcionalidad más" debe ser rechazado automáticamente

### Coherencia Sistémica  
- Todos siguen el mismo patrón de instrucciones puras
- Coordinación explícita pero simple
- Alineación con principios fundamentales del sistema
- Validación regular contra deriva de propósito y scope creep

---

**FILOSOFÍA RECTOR**: Comandos simples, independientes, conversacionales que se coordinan orgánicamente para crear un sistema poderoso pero mantenible.