# Compacted: ContextFlow v3 Architecture - Semantic Retrieval System
**Original**: 2025-07-28 refinamiento-ce-simple-contextflow técnico
**Compacted**: $(date)
**Focus**: Architectural decisions + semantic context retrieval implementation

## Núcleos Temáticos Principales

### Breakthrough: Semantic Analysis > Pattern Matching
**Decisión arquitectónica central**: Context loading basado en análisis conversacional semántico > pattern matching keywords - sistema detecta intención actual y mapea a contexto histórico relevante.

### Arquitecura Three-Tier Confidence System
**Estrategia confidence-based loading**:
- **>85% confidence**: Automático, invisible al usuario
- **50-85% confidence**: Sugerencia opciones múltiples  
- **<50% confidence**: Validación explícita requerida

**Template validación shifts**:
```
"Veo que pasamos de concern técnico a UX. 
¿Recontextualizo o mantengo ambos threads?"
```

## Decisiones Técnicas Cristalizadas

### Separación Conversación-Ejecución
- **Conversación socrática**: Expansiva, sin restricciones token
- **Comandos**: Ejecutivos optimizados, post-descubrimiento únicamente
- **Token economy**: Solo documentación/artefactos, invisible al usuario

### CLAUDE.md Architecture Pattern
**Insight validado**: CLAUDE.md como project-specific system instructions - actúa como constitution elevando Claude de generic tool a specialized, project-aware developer.

**Características técnicas**:
- Living document actualizable
- Hierarchical loading: ~/.claude/ → project root → per-directory
- Version controlled, shared team artifact

### Self-Contained Commands ADR
**Template confirmado**:
```markdown
[Acción]: $ARGUMENTS
EXECUTE: [pasos]
OUTPUT: [formato específico]  
SUGGEST: [próximo comando]
```

**Rationale**: Token economy + portabilidad + escalabilidad

### Semantic Analysis Core
**Pattern architecture**: Análisis conversacional > embeddings
- Intent detection tiempo real
- Context mapping histórico relevante
- Shift detection con validación explícita

## Authority Statements & Implementation Status

### ✅ Decisiones Confirmadas
1. **Hybrid retrieval strategy**: Three-tier confidence-based approach
2. **Conversational validation**: Preguntar > asumir en shifts ambiguos  
3. **Semantic analysis**: Conversational intent > keyword matching
4. **System architecture**: Socrática expansiva + comandos ejecutivos

### 🔄 Implementation Pipeline
1. **Prototipo semantic analyzer**: Intent detection patterns
2. **Context mapping system**: Historical knowledge → current conversation
3. **Validation interface**: User confirmation flows
4. **A/B testing**: Semantic vs keyword context loading

## Technical Context Validado

### Claude Code Integration
**Architecture**: Functions as both MCP server and client
- Custom slash commands: `.claude/commands/` folder
- Team-shared commands via git check-in
- MCP servers: `.mcp.json` configuration
- Headless automation: `-p` flag

### Claude 4 Prompt Engineering
**Optimization patterns confirmados**:
- Clear, explicit instructions más efectivas
- Examples aligned con desired behaviors  
- XML tags para structure (<instructions>, <example>)
- Context/motivation mejora instruction targeting

## Implementation Roadmap

### Phase 1: Semantic Analysis (1-2 semanas)
1. **Intent detection prototyping**: Conversational pattern recognition
2. **Context relevance scoring**: Four-factor weighting system
3. **Shift detection algorithms**: Conversation evolution patterns

### Phase 2: UX Validation (2-3 semanas)
1. **Validation interface**: User confirmation flows
2. **A/B testing**: Semantic vs traditional approaches
3. **Metrics**: Context relevance accuracy, user satisfaction

### Phase 3: Production (1 mes)
1. **Claude Code integration**: Native MCP server development
2. **Team collaboration**: Shared context management
3. **Performance optimization**: Token usage efficiency

## Session Outcome

### Architecture Status
- **Completado**: Semantic retrieval architecture three-tier
- **Next**: Prototipo semantic analyzer implementation
- **Target**: Intent detection accuracy + user experience fluida

### User Methodology Confirmed
- **Metodología preferida**: Socrática expansiva + semantic intelligence
- **Decision pattern**: Conversational validation > automated assumptions
- **Technical approach**: Híbrido inteligente con user control explícito

### System Deliverables
1. **ContextFlow System Instructions v3.1** - Semantic retrieval integrado
2. **Three-tier Context Strategy** - Confidence-based loading specified
3. **Implementation Roadmap** - Timeline + validation targets defined

**Status**: Architecture solidified → Ready for semantic analysis implementation