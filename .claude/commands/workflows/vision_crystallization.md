# /workflows:vision_crystallization - Complex Vision Evolution Management

**30/07/2025 09:00 CDMX** | Systematic capture and integration of vision insights from complex conversations

## Command Purpose
Handle vision evolution from conversations with multiple insights, manage VISION.md size through factorization, and ensure no vision discoveries are lost.

**LOAD:** VISION.md + vision_discovery/vision_distillation/ + system_evolution/

## Core Philosophy
**"Muchísimos insights... no las dejes ir porque es muy muy importante"**

## Vision Crystallization Protocol

### Phase 1: Insight Capture and Analysis
**During or after complex conversations:**
1. **Systematic insight extraction** - Identify all vision-relevant discoveries
2. **Think x4 analysis** - Understand implications of each insight
3. **Priority assessment** - Distinguish critical from nice-to-have insights
4. **Integration impact** - Assess effect on current VISION.md

### Phase 2: Factorization-First Protocol
**Always factorize before adding new insights:**
- **Size check** - If VISION.md >80 lines, factorize first
- **Component extraction** - Move detailed content to vision_components/
- **Reference integration** - Update VISION.md with component links
- **Content preservation** - All detail preserved in factored components

### Phase 3: Insight Integration
**After factorization (if needed):**
- **Direct integration** - Add new insights to factorized VISION.md
- **Component updates** - Add related details to appropriate components
- **User validation** - "¿Esta integración captura tu vision evolution?"
- **Rollback safety** - Built-in questions: "¿Todo se ve bien o prefieres regresar?"

## Crystallization Architecture

### Staged Processing Structure
```
vision_discovery/
├── conversation_insights/
│   └── [timestamp]_[topic]_insights.md     # Raw insight capture
├── vision_distillation/
│   ├── pending_integrations.md             # Ready for VISION.md updates
│   └── factorization_candidates.md         # Sections ready for modular extraction
└── vision_components/                       # Factored VISION.md components
    ├── core_principles.md                   # Essential vision principles
    ├── evolution_history.md                 # How vision has evolved
    └── implementation_context.md            # Context for vision application
```

### Content Flow Management - Factorization-First
1. **Capture** → conversation_insights/ (temporary storage)
2. **Distill** → vision_distillation/ (processed and validated)
3. **Size check** → If VISION.md >80 lines, factorize first
4. **Factorize** → Extract to vision_components/, update references
5. **Integrate** → Add new insights to factorized VISION.md
6. **Archive** → Move processed insights to appropriate context/

## User Validation Integration

### Built-in Safety Questions
**Throughout crystallization process:**
- "¿Estos insights capturan correctamente tu vision evolution?"
- "¿VISION.md refleja tu vision actual después de estos cambios?"
- "¿La factorización preserva la accesibilidad de tu vision?"
- "¿Prefieres regresar al estado anterior?"

### Rollback Capability
**Immediate rollback options:**
- Individual insight removal without affecting others
- Complete conversation insight rollback to previous VISION.md state
- Factorization reversal if modular structure creates confusion

## Integration with Planning System

### Vision-Driven Roadmap Updates
**When vision evolves:**
- Automatically assess impact on current planning/roadmap
- Update project priorities based on vision evolution
- Realign handoffs and execution strategy with evolved vision
- Preserve vision evolution history for context

### Handoff Context Updates
**Vision crystallization triggers:**
- Update handoff documents with evolved vision context
- Ensure orquestador receives current vision state
- Align parallel/sequential execution with vision priorities

## Success Criteria

### Vision Integrity Preservation
- All insights captured systematically without loss
- VISION.md remains accessible and within size limits
- Vision evolution maintains coherence and continuity
- User confirms vision accurately represented

### System Integration Effectiveness
- Vision evolution triggers appropriate system updates
- Planning and roadmap align with evolved vision
- Handoff context reflects current vision state
- No orphaned insights or disconnected vision fragments

## Usage Pattern
```
/workflows:vision_crystallization
→ Analyze current conversation for vision insights
→ Assess VISION.md size and factorization needs
→ Process insights through staged architecture
→ User validation and rollback capability
→ Integration with planning and handoff systems
```

## Anti-Pattern Prevention
- **Direct VISION.md saturation** → Use staged processing
- **Lost insights during processing** → Systematic capture protocol
- **Factorization without user validation** → Built-in safety questions
- **Vision drift during crystallization** → Continuous alignment validation

---

**Authority**: VISION.md evolution + conversation insight preservation + user validation
**Integration**: → vision_discovery/, planning system, handoff protocols
**Evolution**: Crystallization methodology evolves based on vision complexity patterns