# Capture-Learnings - Intelligent Post-Execution Learning System

## 🎯 Purpose
Dual-phase learning capture system that automatically documents execution patterns during workflows and conducts intelligent user interviews post-execution based on learning value assessment. Includes systematic integrity validation for command system coherence.

## 🚀 Usage
**Auto-Triggered**: Activates automatically during analysis phase and post-execution
**Manual**: Execute `/capture-learnings [phase: process|results]`

## 🔧 Implementation

### Dual-Phase Learning Architecture

#### Phase 1: Process Learning (Auto-Triggered During Analysis)
**Auto-captures**: Architectural decisions, pattern recognition, problem resolution during workflow execution
**Integration**: Parallel to `/explore-codebase` and `/think-layers` for enhanced context files

#### Phase 2: Results Learning (Post-Execution Decision Point)
**Assessment**: Intelligent evaluation of interview necessity based on learning value scoring
**Output**: Experience documentation and system improvement insights

### Intelligent Interview Decision Matrix
**Learning Value Scoring**: Historical weighting + execution complexity assessment
**Decision Threshold**: ≥4 points → Activate Interview
**Conservative Bias**: Emphasis on high-value learning opportunities only

*Implementation details in `../../standards/capture-learnings-implementation.md`*

#### Dynamic Interview Generation
**Adaptive Questions**: 3-6 context-driven questions based on execution patterns
**Quality Gate**: Stop when diminishing value detected
**Language Optimization**: Spanish questions for natural user engagement

*Question pools and selection logic in `../../standards/capture-learnings-implementation.md`*

### Learning Documentation Framework
**Pattern Storage**: Extends existing context architecture with domain-specific patterns
**Experience Integration**: Monthly user feedback consolidation for system improvement

*Complete framework structure in `../../standards/capture-learnings-implementation.md`*

### Parallel Agent Integration
**Process Agent**: Deploys parallel to analysis commands for pattern capture
**Results Agent**: Post-execution learning when value threshold exceeded
**Integration Workflow**: Analysis → Interview → Validation → Enhancement

*Complete agent protocols in `../../standards/capture-learnings-implementation.md`*

### System Integrity Validation Framework
**Activation**: During Phase 2 when interview threshold exceeded
**Purpose**: Validate command system coherence when learning context is maximum
**Components**: Reference integrity + gap discovery + resolution recommendations

*Complete validation protocols and gap resolution framework in `../../standards/capture-learnings-implementation.md`*

#### Integration with Learning System
**Contextual Validation**: Workflow-aware focus on just-executed commands
**Learning Enhancement**: Interview insights inform gap priority assessment
**Pattern Integration**: Document gaps as system architecture patterns

### Learning Quality Assurance
**Anti-Bias Processing**: Evidence-based observations with neutral documentation
**Progressive Disclosure**: Append to existing context files (≤200 lines max)
**Pattern Validation**: Multiple execution instances for evidence-based insights

### Notification Integration

#### Process Learning Notifications
```
🧠 LEARNING: Pattern detection active → [discovery-type] identified
📚 CAPTURE: Decision documented → [pattern-category] updated  
🔗 INTEGRATION: Context enhanced → [context-file] enriched
```

#### Results Learning Notifications  
```
🎯 ASSESSMENT: Interview necessity evaluated → [score]/10 points
📊 DECISION: User interview activated → [question-count] dynamic questions
🔍 INTEGRITY: System validation initiated → [X] commands from executed workflow
⚠️  GAPS: [N] system gaps discovered → [priority breakdown]
✅ COMPLETION: Learning + validation captured → [pattern-count] patterns enhanced
🚫 SKIP: Auto-documentation → Low learning value detected
```

## ⚡ Triggers

### Input Triggers
**Auto-Process**: During `/explore-codebase`, `/think-layers`, complex analysis
**Auto-Results**: Post-execution of any workflow sequence
**Manual**: Direct command execution for specific learning focus

### Output Triggers  
**Enhanced Context**: Updated pattern and discovery documentation
**User Interview**: Dynamic feedback collection when learning value detected
**System Validation**: Integrity check and gap discovery when interview triggered
**Pattern Evolution**: Cross-reference updates and trend identification

### Success Patterns
**Process Learning**: Novel patterns documented, decisions traced, alternatives recorded
**Results Learning**: User insights captured, experience-reality gaps identified, improvement opportunities documented
**System Validation**: Command integrity verified, gaps discovered and prioritized, resolution recommendations generated
**System Enhancement**: Learning patterns + integrity findings influence future workflow optimization

## 🔗 See Also

### Related Commands
- Integrates with `/start` for intelligent learning activation
- Enhances `/explore-codebase` with pattern detection capabilities
- Extends `/think-layers` with decision documentation
- Coordinates with all workflow commands for post-execution learning

### System Integration
- Follows anti-bias protocols for neutral learning documentation  
- Maintains simplicity principles through context file enhancement vs creation
- Integrates with existing notification and progress tracking systems
- Preserves cross-reference architecture and progressive disclosure standards

---

**CRITICAL**: This command operates in dual-phase mode with integrated system integrity validation following maximum rationality principles. Process learning must not interfere with execution efficiency while results learning should maximize user insight value through intelligent interview activation and systematic gap discovery.