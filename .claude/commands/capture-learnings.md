# Capture-Learnings - Intelligent Post-Execution Learning System

## 🎯 Purpose
Dual-phase learning capture system that automatically documents execution patterns during workflows and conducts intelligent user interviews post-execution based on learning value assessment.

## 🚀 Usage
**Auto-Triggered**: Activates automatically during analysis phase and post-execution
**Manual**: Execute `/capture-learnings [phase: process|results]`

## 🔧 Implementation

### Dual-Phase Learning Architecture

#### Phase 1: Process Learning (Auto-Triggered During Analysis)
**WHEN**: Activated parallel to `/explore-codebase` and `/think-layers`
**WHAT**: Automatic pattern detection and decision documentation
**OUTPUT**: Enhanced context files with discovered patterns

**Auto-Capture Elements**:
- **Architectural Decisions**: Why specific approaches chosen over alternatives
- **Pattern Recognition**: New patterns discovered vs existing patterns applied
- **Problem Resolution**: Issues encountered and resolution strategies
- **Discovery Documentation**: Previously unknown aspects of codebase/domain
- **Decision Trees**: Alternative paths considered and rationale for choices

#### Phase 2: Results Learning (Post-Execution Decision Point)
**WHEN**: After workflow execution completion
**WHAT**: Intelligent assessment of interview necessity + dynamic user feedback
**OUTPUT**: Experience documentation and system improvement insights

### Intelligent Interview Decision Matrix

#### Learning Value Assessment (Conservative Bias)
**Historical Context Weighting**:
- Days since last interview: +1 point (max +3)
- Consecutive simple executions: +1 point per 3 executions
- Novel domain interactions: +2 points

**Execution Complexity Scoring**:
```
Sequential commands (>2): +2 points
Error resolution occurred: +2 points  
New patterns discovered: +2 points
Alternative strategies evaluated: +1 point
Unexpected execution time: +1 point
Novel tool combinations: +1 point
Context switching required: +1 point
```

**Decision Logic**: ≥4 points OR historical factor present → Activate Interview

#### Dynamic Interview Generation
**Adaptive Question Count** (3-6 questions based on learning density):
- **Core Set (Always)**: 3 high-value questions based on execution patterns
- **Extended Set (Conditional)**: +1-3 questions when novel patterns detected
- **Quality Gate**: Stop when diminishing value detected or user certainty confirmed

**Context-Driven Question Pool**:
- **Process Effectiveness**: "¿El workflow siguió la secuencia que esperabas?"
- **Result Quality**: "¿Los resultados coinciden con tu visión inicial?"
- **Friction Points**: "¿Hubo algún momento donde te sentiste perdido o confundido?"
- **Discovery Value**: "¿Aprendiste algo inesperado sobre tu código/dominio?"
- **Efficiency Assessment**: "¿Qué cambiarías del proceso para la próxima vez?"
- **System Evolution**: "¿El resultado sugiere mejoras al sistema mismo?"

**Adaptive Selection Logic**:
- Select 3 highest-value questions based on execution patterns detected
- Add extended questions only when multiple novel patterns found
- Prioritize density over quantity for cognitive load optimization

### Learning Documentation Framework

#### Pattern Storage Enhancement
**Extend Existing Context Architecture**:
```
context/patterns/
├── execution-patterns-[domain].md      # How workflows typically execute
├── decision-patterns-[domain].md       # Why certain choices made repeatedly  
├── friction-patterns-[domain].md       # Common obstacles and solutions
└── discovery-patterns-[domain].md      # Learning insights and breakthroughs
```

#### Experience Integration
**User Feedback Integration**:
```
context/experience/
├── workflow-effectiveness-[month].md   # Process efficiency insights
├── expectation-reality-[month].md      # Outcome vs prediction analysis
└── improvement-suggestions-[month].md  # User-driven enhancement ideas
```

### Parallel Agent Integration

#### Process Learning Agent (During Analysis)
**Deploy Parallel To**:
- `/explore-codebase` → Capture structural discovery patterns
- `/think-layers` → Document analysis decision progression  
- Web research → Record external pattern validation insights

**Agent Objectives**:
1. **Decision Documentation**: Record why specific approaches chosen
2. **Pattern Classification**: Identify if discoveries are novel vs familiar
3. **Alternative Assessment**: Document considered but rejected options
4. **Context Enhancement**: Enrich existing context with meta-insights

#### Results Learning Agent (Post-Execution)
**Trigger Conditions**:
- Workflow execution marked complete
- Context files generated and consolidated
- Learning value assessment ≥4 points OR historical trigger active

**Agent Workflow**:
1. **Execution Analysis**: Review full workflow trace and outcomes
2. **Interview Generation**: Create dynamic questions based on execution patterns
3. **User Engagement**: Conduct structured feedback interview
4. **Insight Integration**: Enhance existing patterns with experience data

### Learning Quality Assurance

#### Anti-Bias Learning Processing
**Neutral Pattern Documentation**:
- Focus on evidence-based observations over interpretations
- Document multiple perspectives when applicable  
- Separate factual patterns from subjective preferences
- Validate patterns through multiple execution instances

#### Progressive Learning Disclosure
**Context File Enhancement** (≤200 lines max):
- Append insights to existing context files rather than creating new ones
- Cross-reference related patterns across domains
- Maintain maximum information density principles
- Enable pattern evolution tracking over time

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
✅ COMPLETION: Learning captured → [pattern-count] patterns enhanced
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
**Pattern Evolution**: Cross-reference updates and trend identification

### Success Patterns
**Process Learning**: Novel patterns documented, decisions traced, alternatives recorded
**Results Learning**: User insights captured, experience-reality gaps identified, improvement opportunities documented
**System Enhancement**: Learning patterns influence future workflow optimization

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

**CRITICAL**: This command operates in dual-phase mode and requires integration with existing workflow orchestration. Process learning must not interfere with execution efficiency while results learning should maximize user insight value through intelligent interview activation.