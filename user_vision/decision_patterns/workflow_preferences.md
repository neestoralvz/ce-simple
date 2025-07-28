# User Vision: Workflow Decision Patterns

## Decision Authority Declaration

**ULTIMATE AUTHORITY**: User workflow preferences from actual conversations  
**OVERRIDE POWER**: All system workflows must align with these patterns  
**SOURCE**: Narratives/raw/conversations/ - user voice preservation

## Core Workflow Patterns

### 1. Research-First Protocol Universally
**User Voice**:
> "yo te doy mi solicitud, tú exploras en tu codebase para ver si tienes algo de información, haces una búsqueda en internet sobre lo que estoy diciendo para tener más contexto, buscas soluciones, buscas casos de éxito, buscas buenas prácticas, sintetizas"

**Pattern Implementation**:
- EVERY task begins with $(date) for timestamp
- WebSearch with current date for best practices  
- MCP Context7 for pattern analysis
- Systematization of findings before execution
- NO exceptions to research-first approach

### 2. 10-Step Universal Workflow
**User Voice** (Complete Workflow Definition):
> "el workflow que quiero que sigamos siempre es, yo te doy mi solicitud, tú exploras [...] haces una búsqueda en internet [...] sintetizas [...] la analizas [...] desplegando a un subagente especializado, para utilizar, pensar, por cuatro, y entonces, obtienes el plan, paso a paso, y de ese plan, lo vuelves a analizar [...] desplegues, a estos subagentes especializados, para que puedan realizar las tareas, y en ese plan, tienes que integrar [...] la verificación, validación, pruebas"

**Canonical Workflow Steps**:
1. Usuario da solicitud
2. Explorar codebase para información existente
3. Búsquedas web paralelas para contexto + best practices  
4. Síntesis + archivo contexto guardado
5. Análisis con subagente "pensar por cuatro"
6. Plan paso a paso generado
7. Análisis de delegación con subagente especializado
8. Ejecución con subagentes especializados desplegados
9. Verificación/validación/pruebas integradas
10. Bucle hasta éxito (máximo 5 ciclos)

### 3. Obligation Document Creation Workflow
**User Voice**:
> "una de las cosas que siempre siempre se haga al momento de crear un documento es pasarlo por el workflow siguiente: creación, alineamiento y verificación"

**Mandatory Document Workflow**:
- `/create-doc` - Content Specialist deployment (NUNCA crear directamente)
- `/align-doc` - Architecture Validator deployment (OBLIGATORIO)  
- `/verify-doc` - Quality Assurance deployment (OBLIGATORIO)
- Auto-chaining secuencial automático con confirmación usuario
- VIOLATION: Crear documentos fuera de este workflow está PROHIBIDO

### 4. Intent Detection + Auto-Triggers
**User Voice**:
> "el comando de create doc debería de utilizarse automáticamente al momento en que el sistema detecta que hay que crear un documento"

**Auto-Detection Patterns**:
- Semantic analysis paralelo durante conversación
- Auto-trigger `/create-doc` si detecta patterns: "necesito plan", "documentar", "crear reporte"
- Seamless integration sin interrumpir flujo conversacional
- Background processing document creation mientras continúa diálogo

## Specialization Patterns

### 5 Core Specialist Types
**From Multi-Subagent Architecture**:
- **Research Specialist**: Investigation + benchmarking + best practices
- **Architecture Validator**: System consistency + integration verification
- **Content Optimizer**: Token economy + structure optimization  
- **Voice Preservation**: User intent exactitude + authenticity validation
- **Quality Assurance**: Final validation + standards compliance

### Task Tools Parallel Deployment
**User Preference**: SIEMPRE priorizar Task tools concurrentes en mismo mensaje sobre secuenciales

**Implementation**:
- Multiple specialists deployed simultaneously when possible
- Parallel processing for independent concerns
- Coordination through notification system
- Efficiency optimization through concurrent execution

## Decision Tree Patterns

### Universal Command Decision Logic
**User Voice**:
> "la idea es que prácticamente cualquier archivo, documento, comando, tenga como una de sus secciones esta parte de árbol de decisiones para que el contexto se utilice de manera más eficiente"

**Metadata Requirements**:
- Every command includes decision tree metadata
- Context usage optimization through intelligent routing
- When-to-use criteria clearly defined
- Semantic triggers for automatic activation

### Session Start Intelligence
**User Voice**:
> "cuando digo comando universal me refiero al comando que puedo utilizar recién iniciada la conversación para que el agente revise el contexto y proponga iniciar una conversación, el diálogo mayéutico, tomar alguna actividad que no esté terminada"

**Start Command Behavior**:
- Context review automatic
- Mayeutic dialogue activation
- Pending activities identification
- Intelligent options generation
- Adaptive based on available commands and project state

## Simplicity + Efficiency Patterns

### Lean System Philosophy
**User Voice**:
> "Sistema simple, lean, fácil de utilizar"
> "nos debemos de mantener simples, pragmáticos, funcionales, lean, ligero"

**Implementation Patterns**:
- Minimal complexity for maximum utility
- Pragmatic over theoretical solutions
- Functional over aesthetic considerations
- Lean processing with maximum efficiency
- Ligero (lightweight) system behavior

### Research Protocol Optimization
**User Voice**:
> "pero, no necesitaría hacerlo cuando va a hacer la implementación? porque en ese momento solo se está activando, no está haciendo modificaciones"

**Tiered Research Application**:
- **TIER 1 (research: true)**: Implementation/creation/modification commands
- **TIER 2 (research: conditional)**: Complex workflows with user impact
- **TIER 3 (research: false)**: Activation/routine operations/status checks

## Communication Patterns

### Mayeutic Dialogue Preservation
**User Voice**:  
> "no quiero que perdamos de vista el diálogo mayéutico que al final es la manera en la que se descubre lo que es la solicitud del usuario"

**Discovery Protocol**:
- Progressive questioning to reveal true intent
- Natural conversation flow maintenance
- Discovery-driven rather than assumption-driven
- Socratic method as core interaction pattern

### Voice + Anti-Bias Standards
**User Voice**:
> "no me gusta la idea de que el hecho de que sea CEO sea algo que se mencione [...] no podemos producir este sesgo"

**Communication Requirements**:
- Redacción agnóstica, neutra
- NO adjetivos descriptivos que influencien behavior
- Sistema escalable para múltiples usuarios
- Clear separation between user voice and AI interpretation

## Evolution Patterns

### Systematic Changes Protocol
**User Voice**:
> "esto debe ser un criterio para todos los comandos, esto debería de estar documentado o guardado en algún lugar donde produzca cambios sistémicos"

**Evolution Mechanism**:
- User feedback → Systematic changes across ALL commands
- Learning Pattern: Aciertos + errores → Updates sistemáticos permanentes
- Pattern Propagation: Discoveries → Automatic integration across ecosystem
- Documentation of criteria for systematic application

### Organic Growth Philosophy
**User Voice**:
> "Quiero que todo sea como de una manera muy orgánica [...] El poder crear un metaproceso [...] Un metasistema que se pueda adaptar a muchas cosas"

**Organic Evolution Requirements**:
- System grows naturally from usage patterns
- Adaptation capability for diverse use cases
- Meta-process creation rather than rigid procedures
- Flexibility while maintaining core principles

## Authority + Enforcement

**WORKFLOW AUTHORITY**: SUPREME
**VIOLATION PROTOCOL**: Any workflow contradicting these patterns must be corrected immediately
**ENFORCEMENT**: Active blocking of non-compliant workflows
**UPDATE AUTHORITY**: Only user voice in actual conversations can modify these patterns

---

**Generated**: 2025-07-28  
**Source**: User workflow preferences from narrative conversations  
**Status**: AUTHORITATIVE WORKFLOW PATTERNS  
**Authority**: ULTIMATE - All system workflows must conform to these patterns