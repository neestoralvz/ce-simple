---
contextflow:
  purpose: "Recreation protocol para eliminar sesgo información existente"
  triggers: ["staleness detectada", "bias acumulado", "arquitectura refinada"]
  requires-subagent: true
  research-driven: true
  destructive: true
---

# Comando `/clean-slate-recreation`

## Propósito Core
Recrear documentos/componentes desde cero basándose únicamente en principios actualizados y decisiones crystallized recientes, eliminando sesgo de información existente.

## Why Clean Slate Recreation?
**Problem**: Actualización incremental acumula bias de información antigua que contamina decisiones nuevas.

**Solution**: Recreación completa desde principios fundamentales + decisiones recientes, ignorando implementación anterior.

## Recreation Protocol

### 1. Backup Sistemático
**SIEMPRE via Architecture Validator subagent**:
```
/archive/[timestamp]/[component-name]-pre-recreation/
├── original-file.md
├── recreation-context.md  
└── decision-log.md
```

### 2. Context Crystallization
**SIEMPRE via Voice Preservation subagent**:
- Extract user decisions recientes relevantes
- Identify principios fundamentales actuales  
- Collect synthesis insights aplicables
- Document recreation rationale

### 3. Clean Creation
**SIEMPRE via Content Optimizer subagent**:
- Start from blank document
- Apply ONLY current principles + recent decisions
- Ignore previous implementation completely
- Build optimal structure from scratch

### 4. Validation Against Fresh Context
**SIEMPRE via Quality Assurance subagent**:
- Verify alignment con principios actuales
- Check consistency con decisiones recientes
- Validate NO contamination from old version
- Ensure optimal structure for current needs

## Recreation Triggers

### Automatic Triggers
- **Staleness detected**: File unchanged > 30 days + system evolved
- **Architecture shift**: Fundamental principles changed
- **User feedback**: "This doesn't reflect current approach"
- **Bias accumulation**: Multiple incremental changes without coherence

### Manual Triggers
- **Explicit user request**: "Recreate X from scratch"
- **Quality degradation**: File became unwieldy through incremental changes
- **Integration problems**: Component no longer fits system cleanly

## Recreation Scope

### Individual File Recreation
**Target**: Single component needs complete rebuild
**Process**: Backup → Extract context → Clean create → Validate

### System-wide Recreation  
**Target**: Multiple components with accumulated bias
**Process**: Phased recreation maintaining system integrity

### Selective Recreation
**Target**: Specific aspects while preserving others
**Process**: Hybrid approach with careful contamination prevention

## Subagent Orchestration Pattern

### Phase 1: Preparation (Parallel)
```
Task 1: Architecture Validator - "Analyze [component] for recreation readiness"
Task 2: Voice Preservation - "Extract current user decisions for [component]"
Task 3: Research Specialist - "Research current best practices for [domain]"
```

### Phase 2: Recreation (Sequential)
```
Task 1: Content Optimizer - "Create [component] from scratch using crystallized context"
Task 2: Architecture Validator - "Validate integration with current system"
Task 3: Quality Assurance - "Final quality validation against current standards"
```

## Success Criteria

### Recreation Quality
- [ ] Zero contamination from previous version
- [ ] Full alignment with current principles
- [ ] Optimal structure for current system state
- [ ] Integration seamless with current architecture

### Process Integrity  
- [ ] Complete backup of original version
- [ ] Clear documentation of recreation rationale
- [ ] Subagent orchestration used throughout
- [ ] Validation against fresh context only

## Integration with System Evolution

### Learning Capture
- Document what was improved in recreation
- Identify patterns of bias accumulation
- Refine triggers for future recreation needs
- Update recreation templates based on experience

### Continuous Evolution
- Regular staleness assessment
- Proactive recreation scheduling
- System coherence monitoring
- User satisfaction tracking

---

**Warning**: Recreation is destructive process - ALWAYS backup first and document rationale clearly.