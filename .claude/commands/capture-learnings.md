# Capture-Learnings - Intelligent Post-Execution Learning System

## 🎯 Purpose
Dual-phase learning capture: automatic pattern documentation during workflows and intelligent post-execution interviews based on learning value assessment.

## 🚀 Usage
**Auto-Triggered**: Activates automatically during analysis phase and post-execution
**Manual**: Execute `/capture-learnings [phase: process|results]`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at learning capture initialization**:

```javascript
TodoWrite([
  {"content": "📊 SCORING: Calculate learning value using intelligent assessment framework (≥4 points threshold)", "status": "pending", "priority": "high", "id": "learn-score-1"},
  {"content": "🎤 INTERVIEW: Conduct dynamic user interview via intelligent question generation", "status": "pending", "priority": "medium", "id": "learn-interview-1"},
  {"content": "📝 PATTERNS: Document discovered patterns with evidence-based analysis", "status": "pending", "priority": "medium", "id": "learn-patterns-1"},
  {"content": "🔄 ORCHESTRATION: Coordinate learning capture via /agent-orchestration for efficiency", "status": "pending", "priority": "medium", "id": "learn-orchestration-1"},
  {"content": "🔧 INTEGRITY: Execute /matrix-maintenance validation for system coherence", "status": "pending", "priority": "low", "id": "learn-integrity-1"},
  {"content": "🎯 EVOLUTION: Update command network based on learning patterns and insights", "status": "pending", "priority": "low", "id": "learn-evolution-1"}
])
```

**Intelligence-Driven Todos**: Add conditional todos based on learning value threshold and interview outcomes

### Structural Validation Protocol
**PRE-EXECUTION**:
1. 🏗️ **STRUCTURE**: Validate organization compliance
2. 🔗 **REFERENCES**: Check cross-reference integrity  
3. 📏 **SIZE**: Ensure context/ files within limits
4. ⚡ **CORRECT**: Fix structural violations

**Pattern Evolution**: Detect successful patterns → Update standards → Optimize structure → Maintain integrity

### Dual-Phase Learning Architecture

#### Phase 1: Process Learning (Auto-Capture During Execution)
**Activation**: Parallel deployment during `/explore-codebase`, `/think-layers`, and complex analysis workflows
**Coordination**: Via `/agent-orchestration` for non-intrusive pattern detection
**Capture Scope**:
- **Architectural Decisions**: Document design choices and rationale during execution
- **Pattern Recognition**: Identify emerging patterns and successful approaches
- **Problem Resolution**: Record solution strategies and decision points
- **Alternative Evaluation**: Track considered approaches and selection criteria

#### Phase 2: Results Learning (Intelligent Post-Execution Assessment)
**Learning Value Scoring Framework**:
```
📊 COMPLEXITY ASSESSMENT:
• Progressive disclosure mastery (+2 points)
• System health optimization (+2 points)
• Alternative strategies evaluated (+1 point)
• Cross-domain insights generated (+1 point)
• Workflow complexity indicators (+1 point)

🎯 THRESHOLD EVALUATION: ≥4 points → Interview activation
🎤 DYNAMIC INTERVIEW: 3-6 context-driven questions in Spanish
```

#### Integration & Validation Protocol
**Contextual Validation**: Workflow-aware focus on just-executed commands and patterns
**Learning Enhancement**: Interview insights inform system improvement priorities
**Pattern Documentation**: Systematic capture in context/ directories with structured organization
**System Evolution**: Learning patterns influence future workflow optimization and command enhancement

### Learning Quality Assurance & Documentation Framework

#### Evidence-Based Documentation Standards
**Anti-Bias Processing**: Neutral observation documentation with evidence-based conclusions only
**Progressive Disclosure**: Context file appending with size limits (≤200 lines maximum)
**Pattern Validation**: Multi-execution validation for evidence-based pattern identification
**Cross-Reference Integrity**: Systematic validation via `/matrix-maintenance` integration

#### Intelligent Documentation Organization
**File Placement Strategy**:
- `context/experience/session-[timestamp].md` → User interview responses and insights
- `context/patterns/learning-[domain].md` → Documented patterns and approaches
- `context/discoveries/workflow-[session].md` → Process learning and decision documentation

#### System Integrity Validation Framework
**Activation Protocol**: When interview threshold (≥4 points) exceeded
**Validation Scope**: Command system coherence at maximum learning context
**Gap Discovery**: Reference integrity, missing connections, resolution recommendations
**Enhancement Integration**: Learning insights inform gap priority assessment and system evolution

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

## 🔗 Module Integration

### Command Module Dependencies
**Core Integration**:
- `/agent-orchestration` → Non-intrusive learning coordination during workflow execution
- `/matrix-maintenance` → System integrity validation and cross-reference gap discovery

**Execution Integration**:
- `/start` → Intelligent learning activation based on workflow complexity
- `/explore-codebase` → Pattern detection enhancement during codebase analysis
- `/think-layers` → Decision documentation and analytical insight capture
- `/problem-solving` → Solution pattern documentation and learning integration
- **All Workflow Commands** → Post-execution learning assessment and pattern capture

### Success Patterns & Performance Metrics
**Process Learning Success**: Novel patterns documented → Decisions traced → Alternatives recorded
**Results Learning Success**: User insights captured → Experience-reality gaps identified → Improvement opportunities documented
**Orchestration Success**: Learning capture efficiency >95% → Zero workflow interference
**System Validation Success**: Command integrity verified → Gaps discovered and prioritized → Resolution recommendations generated

### Integration Success Indicators
**Learning Value Accuracy**: Threshold-based activation prevents noise while capturing high-value insights
**User Engagement Quality**: Dynamic Spanish questions generate meaningful feedback and insights
**System Enhancement Impact**: Learning patterns and integrity findings influence future workflow optimization
**Documentation Quality**: Evidence-based pattern documentation with structured organization and cross-validation

### Context Documentation Locations
**Primary Output Directories**:
- `context/experience/` → User interview responses and behavioral insights
- `context/patterns/` → Documented patterns, approaches, and best practices
- `context/discoveries/` → Process learning, decisions, and workflow insights
- **Anti-Fragmentation**: Consolidated documentation with maximum density and cross-reference integrity

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of dual-phase learning capture system

```javascript
// LEARNING VALUE ASSESSMENT (scoring framework)
Bash("echo 'scale=1; ([novelty_score] + [reusability_score] + [importance_score] + [complexity_score]) / 4' | bc")

// THRESHOLD CHECK (≥4 points triggers learning capture)
// If learning_value >= 4.0, proceed with learning capture

// PHASE 1: PROCESS LEARNING (during execution)
// Pattern detection during workflow execution
Grep("TODO|FIXME|PATTERN|DECISION", {glob: "context/**/*.md", output_mode: "content"})
Grep("successful|failure|alternative|tradeoff", {glob: "context/**/*.md", output_mode: "content"})

// PHASE 2: RESULTS LEARNING (post-execution assessment)
// Dynamic user interview generation (Spanish)
Write("context/experience/interview-[timestamp].md", `# Entrevista de Aprendizaje Post-Ejecución

## Preguntas Dinámicas
1. ¿Qué aspectos de esta sesión fueron más útiles para ti?
2. ¿Hubo algún momento donde el sistema no se comportó como esperabas?
3. ¿Qué información adicional habrías necesitado durante el proceso?
4. ¿Los resultados coinciden con lo que buscabas inicialmente?
5. ¿Qué mejorarías del workflow que acabamos de ejecutar?

## Responses
[User responses to be captured]

## Learning Insights
[Insights derived from user responses]
`)

// PATTERN DOCUMENTATION  
Write("context/patterns/learning-pattern-[timestamp].md", `# Learning Pattern Documentation

## Discovered Patterns
[Pattern identification from execution]

## Decision Points
[Key decisions made during execution]

## Alternative Approaches
[Considered but not selected approaches]

## Success Factors
[What made this approach work]

## Areas for Improvement  
[Identified optimization opportunities]
`)

// SYSTEM INTEGRITY VALIDATION
Task("Matrix Maintenance", "Execute /matrix-maintenance to validate system integrity and cross-reference coherence")

// CONTEXT ORGANIZATION
Bash("find context/ -name '*.md' | wc -l") // Count context files
Bash("find context/ -name '*.md' -exec wc -l {} + | tail -1 | awk '{print $1}'") // Total lines

// DISCOVERY DOCUMENTATION
Write("context/discoveries/learning-session-[timestamp].md", `# Learning Session Discovery

## Session Analysis
- Learning Value Score: [calculated_score]/10
- Patterns Identified: [pattern_count]
- User Insights: [insight_count]
- System Improvements: [improvement_count]

## Key Discoveries
[Major insights from this learning session]

## Action Items
[Specific improvements to implement]
`)
```

### Learning Value Calculation
**SCORING LOGIC**:
- **Novelty** (1-3): How new/innovative was this approach?
- **Reusability** (1-3): How applicable to future workflows?  
- **Importance** (1-2): How critical to system/user success?
- **Complexity** (1-2): How challenging was the problem solved?
- **Threshold**: ≥4.0 triggers full learning capture

### Dynamic Interview System
**SPANISH INTERVIEW QUESTIONS**:
- Generated based on workflow complexity and outcomes
- Focus on experience-reality gaps
- Capture improvement opportunities
- Document user satisfaction and friction points

### Session Completion Protocol  
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with learning metrics (no Claude attribution)
Bash("git add . && git commit -m \"capture-learnings: [session-type] | value: [score]/10 | patterns: [N] | session-[N]\"")
```

### Execution Verification
**TOOL CALL AUDIT**:
- **Learning assessment**: 1 Bash calculation using bc
- **Pattern detection**: 2 Grep operations on context files
- **File generation**: 3 Write operations for different outputs
- **System validation**: 1 Task call to matrix-maintenance
- **Context analysis**: 2 Bash operations for metrics
- **Ratio**: 9 tool calls to ~200 documentation lines = 4.5% (HEALTHY)

---

**CRITICAL**: This command operates in dual-phase mode with integrated system integrity validation following maximum rationality principles. Process learning must not interfere with execution efficiency while results learning should maximize user insight value through intelligent interview activation and systematic gap discovery.

**EXECUTION COMMITMENT**: Dual-phase learning capture with scoring framework, Spanish interviews, and system integrity validation are NOW implemented with actual tool calls.