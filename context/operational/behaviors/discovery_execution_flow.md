# Discovery Execution Flow - Workflow System Completo Usuario

**29/07/2025 22:45 CDMX** | Complete workflow system según especificación usuario

## DISCOVERY WORKFLOW
**Propósito**: Diálogo mayéutico para contexto completo del usuario
**Trigger**: Solicitud inicial del usuario

### Protocol Discovery
1. **Solicitud recibida** → Activar diálogo mayéutico obligatorio
2. **Conversación exploratoria** → Preguntas socráticas para clarificar intent real
3. **Contexto completo** → Usuario proporciona toda información necesaria
4. **Decision point** → Proceder a exploración o continuar discovery si incompleto

### Elementos Discovery Esenciales
- **Diálogo sin restricciones** de tokens en fase discovery
- **Metodología mayéutica** para true intent discovery según socratic_methodology.md
- **Crystallización de vision** antes de proceder a action
- **No assumptions** - descubrir todo a través conversación natural

## EXPLORATION WORKFLOW  
**Propósito**: Investigación codebase + análisis contexto para preguntas informadas
**Trigger**: Discovery base completo → necesidad exploración técnica

### Protocol Exploration
1. **Codebase investigation** → Búsqueda sistemática en código existente
2. **Context analysis** → Investigación específica en context/ (contiene SOLO información usuario histórica)
3. **Gap identification** → Identificar información faltante para enhanced questions
4. **Enhanced discovery** → Preguntas mejor informadas basadas en exploración técnica

### Integration Discovery + Exploration
- Context/ = información pura que usuario ha proporcionado historically
- Exploración técnica → permite preguntas más específicas y relevantes
- Better questions → better discovery → better outcomes

## INVESTIGATION WORKFLOW
**Propósito**: Research online + MCP integration para soluciones externas
**Trigger**: Clarity interna obtenida → necesidad research external solutions

### Protocol Investigation  
1. **Online research** → WebSearch para soluciones, best practices, success cases
2. **MCP TextEven integration** → Búsqueda especializada cuando available
3. **Solution synthesis** → Compilación opciones y recommendations informadas
4. **Conversational guidance** → Continuar conversación con research-informed suggestions

### Investigation Integration Points
- **Parallel research execution** → Multiple WebSearch calls simultaneously
- **MCP tools optimization** → Use specialized search when available
- **Evidence-based suggestions** → Research informa conversational guidance

## PLANNING WORKFLOW
**Propósito**: Think x4 analysis + diseño step-by-step systematic
**Trigger**: Investigation completa → necesidad structured execution plan

### Protocol Planning
1. **Information analysis** → Think x4 OBLIGATORIO systematic analysis sobre toda información
2. **Step-by-step design** → Plan detallado con pasos específicos y measurable
3. **Conversation division analysis** → Dividir plan en conversaciones paralelas/secuenciales  
4. **Prompt generation** → Generar conversation starters específicos para usuario

### Think x4 Planning Integration
- **4 perspectives analysis** obligatorio antes decisions
- **Systematic approach** vs intuitive/assumption-based decisions
- **Evidence-based methodology** para all planning decisions

## MULTI-CONVERSATION EXECUTION
**Propósito**: Maximum orchestration power através conversaciones paralelas
**Trigger**: Plan dividido → conversaciones múltiples provide exponential benefit

### Protocol Multi-Conversation
1. **Conversation breakdown** → Analysis cuáles parts pueden ser parallel vs sequential
2. **Prompt crafting** → Conversation starters específicos para cada execution thread
3. **Orchestrator deployment** → Cada conversación puede deploy orchestrators independientes
4. **Subagent coordination** → Orchestrators deploy subagents según specialized necessities

### Power Multiplication Architecture
- **Conversation → Orchestrator → Subagents** hierarchical deployment
- **Parallel execution** para independent tasks maximizes efficiency
- **Sequential coordination** para dependent workflows maintains coherence
- **Exponential capability** through multi-layer agent deployment

## TDD EXECUTION WORKFLOW
**Propósito**: Test-driven implementation con recursive validation until success
**Trigger**: Execution phase → implementation required with success criteria

### Protocol TDD Recursive
1. **Objective establishment** → Clear, measurable goal definition
2. **Success criteria definition** → Specific, testable completion metrics
3. **Implementation loop** → Agent/subagent systematic execution
4. **Validation cycle** → Test against established success criteria
5. **Recursive retry** → IF criteria not met → restart implementation process until success OR declare impossible

### Git WorkTree Integration
- **Conversation-level branching** → Cada conversación inicia en Git WorkTree (disposable option)
- **Experimental control** → Safe experimentation without main branch contamination
- **Granular change management** → Control específico de each implementation attempt

## MAINTENANCE WORKFLOW
**Propósito**: Systematic maintenance de sistema, comandos, contexto, implementación
**Trigger**: Regular intervals OR degradation detected OR evolution requirements

### Maintenance Areas Comprehensive
- **System maintenance** → Overall system health y performance
- **Command maintenance** → Command updates, optimization, evolution
- **Context maintenance** → Information organization, reference validation, utility preservation  
- **Implementation maintenance** → Code quality, technical debt, architecture consistency
- **CLAUDE.md maintenance** → Central dispatcher updates y semantic trigger evolution
- **README maintenance** → Documentation currency y project overview accuracy
- **Reference maintenance** → Cross-link validation y context utility verification
- **Directory cleanup** → Structure organization y file lifecycle management
- **Project structure tracking** → Architecture consistency y evolution monitoring

### Maintenance Integration Protocol
- **Proactive monitoring** → Detect issues before degradation affects user experience
- **Systematic methodology** → Apply consistent approach across all maintenance areas
- **Evolution-driven updates** → Adapt maintenance based on system learning y growth

## SESSION CLOSURE WORKFLOW
**Propósito**: Learning integration + context updates + knowledge persistence
**Trigger**: Conversación completion → mandatory knowledge capture protocol

### Protocol Session Closure Mandatory
1. **Learning extraction** → Identify key insights, patterns, improvements discovered
2. **Context integration** → Knowledge integration en appropriate context files via SEMANTIC_ORGANIZATION.md
3. **System improvement** → Updates to methodology/patterns based on session experience
4. **Reference updating** → Link validation, cross-reference maintenance, utility verification
5. **Knowledge persistence** → Ensure all learning preserved y accessible for future sessions

### Context Utility Maintenance Critical
- **Reference relationship preservation** → Maintain cross-link integrity
- **Context effectiveness validation** → Verify information remains useful y accessible
- **Knowledge accessibility optimization** → Ensure easy retrieval for future sessions
- **Continuous improvement integration** → System learns y evolves from each session

### Session-to-Session Continuity
- **Handoff preparation** → Clear state documentation for next session
- **Progress preservation** → Ensure no important work or insights lost
- **Context evolution** → System knowledge grows systematically through sessions

---
**Authority**: Complete user workflow specification implemented
**Integration**: → orchestration_protocol.md, socratic_methodology.md, SEMANTIC_ORGANIZATION.md
**Implementation Ready**: Systematic workflows para command development y system execution