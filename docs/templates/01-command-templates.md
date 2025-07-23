# Command Templates - Unified Template System

## Purpose
Consolidated command templates providing standardized structure, P55/P56 compliance, and enforcement patterns for all ce-simple command development.

## Template Categories

### 1. Basic Command Template
```markdown
# /command-name - Command Title

## Purpose
[Single sentence describing what this command accomplishes]

## Principles and Guidelines
- **Self-Contained Design**: Embed complete execution requirements without external dependencies
- **Parallel Optimization**: Design for concurrent execution using Task Tool orchestration
- **Natural Language Instructions**: Use ≤15 words per instruction for clarity
- **Standards Compliance**: Maintain ≤150 lines total command length

## Execution Process

### Phase 1: [Discovery/Setup Phase]
Update TodoWrite mark "[task name]" as in_progress

[Phase description with specific actions]
- [Action 1 with concrete deliverable]
- [Action 2 with measurable outcome]
- [Action 3 with validation criteria]

### Phase 2: [Analysis/Design Phase]
Update TodoWrite complete previous, mark "[task name]" as in_progress

[Phase description with orchestration strategy]
- [Action 1 using parallel/sequential patterns]
- [Action 2 with context requirements]
- [Action 3 with integration points]

### Phase 3: [Execution/Implementation Phase]
Update TodoWrite complete previous, mark "[task name]" as in_progress

[Phase description with implementation details]
- [Action 1 with specific techniques]
- [Action 2 with quality assurance]
- [Action 3 with performance criteria]

### Phase 4: [Completion/Validation Phase]
Update TodoWrite complete previous, mark "[task name]" as in_progress

[Phase description with validation and handoff]
- [Action 1 with success criteria]
- [Action 2 with documentation updates]
- [Action 3 with next steps preparation]

### Phase 5: [Intelligent Routing/Handoff Phase]
Update TodoWrite complete previous, mark "[task name]" as in_progress

**Command Routing Protocol**: Analyze execution results and recommend next commands
- **Context Analysis**: Review completion state and identify continuation opportunities
- **Priority Assessment**: Evaluate recommended commands using mathematical priority scoring
- **Handoff Protocol**: Format recommendations as "Next: /command (priority) - rationale"
- **Integration**: Coordinate with /handoff-manager and /notify-manager for seamless transitions
- **Documentation**: Record routing decisions and rationale for learning extraction

**Routing Format**: "Next: /[category]/[command] ([high/medium/low]) - [execution rationale]"

Update TodoWrite complete all [command name] tasks

**Error Handling**: [Specific error scenarios and resolution approaches]

---

@./docs/core/README.md
@./docs/core/system-principles.md
```

### 2. P55/P56 Compliant Command Template
```markdown
# /command-name - Command Title

## Purpose
[Command description with P55/P56 compliance integration]

## 🛡️ P55/P56 Compliance Framework
**Inherits from**: Universal P55/P56 compliance standards

### Tool Call Execution Protocol
**MANDATORY**: This command executes:
- Real tool calls (never simulation)
- Mathematical calculations via script execution
- Visual announcements before each tool execution
- Complete transparency of all operations
- Evidence trail maintenance for compliance verification

### Mathematical Integration Pattern
```bash
# Load script foundation
source scripts/core/path-helper.sh
source scripts/formulas/context_engineering_formulas.sh

# Execute calculations with ≥4 decimal precision
confidence_score=$(calculate_confidence $param1 $param2 $param3)
threshold_compliance=$(calculate_threshold_compliance $score $threshold "gte")

# Validate P55/P56 compliance
echo "P55_COMPLIANCE: $(tool_calls_executed)/$(required_tool_calls) = 100%"
echo "P56_TRANSPARENCY: All operations visible with mathematical precision"
```

## Execution Process
[Standard 4-phase process with P55/P56 integration points]

### Phase 1: Script Foundation Loading
- Load mathematical formula library via tool calls
- Validate script availability and function access
- Initialize compliance tracking and evidence collection

### Phase 2: Execution with Mathematical Validation
- Execute core functionality with tool call integration
- Perform mathematical calculations with ≥4 decimal precision
- Maintain visual transparency throughout execution

### Phase 3: Compliance Verification
- Validate 100% tool call execution rate
- Verify mathematical precision and accuracy
- Document execution evidence for audit trail

### Phase 4: Transparent Reporting
- Display execution metrics and compliance status
- Report performance measurements and success criteria
- Update documentation with execution evidence

### Phase 5: P55/P56 Compliant Routing
**Mathematical Command Routing**: Calculate optimal next command using precision algorithms
- **Performance Analysis**: Use mathematical formulas to assess completion metrics
- **Compliance Routing**: Ensure next command recommendations maintain P55/P56 standards
- **Tool Call Integration**: Execute routing calculations via real tool calls (never simulation)
- **Handoff Protocol**: "Next: /command ([calculated_priority]) - [mathematical_rationale]"
- **Evidence Trail**: Document routing calculations with ≥4 decimal precision

```bash
# Calculate routing priority with mathematical precision
routing_score=$(calculate_routing_priority $completion_metrics $context_factors)
echo "ROUTING_DECISION: Priority=$(printf "%.4f" $routing_score) Command=/[recommended]"
```

## Success Metrics
- **P55 Compliance**: 100% tool call execution (0% simulation)
- **P56 Transparency**: ≥95% execution visibility
- **Mathematical Precision**: ≥4 decimal places accuracy
- **Performance**: ≤2.0s execution time

---

@./docs/core/README.md
@./docs/core/system-principles.md
```

### 3. Enforcement Command Template
```markdown
# [Command Type]: `/command-name`

## **🚨 BLOCKING [Command Category]: [Command Title]**
**🚨 MANDATORY: Sistema WILL [core functionality] with AUTOMATIC blocking of [violations] and REQUIRED [verification type]**

## Purpose
🚨 BLOCKING: Sistema WILL [execute core function] with AUTOMATIC [blocking mechanism] and REQUIRED [compliance verification]. BLOCKING of [specific violations] and MANDATORY [enforcement protocols].

## 🚨 ENFORCEMENT MECHANISMS

### **🚨 MANDATORY Execution Requirements**
- 🚨 REQUIRED: [Function] with AUTOMATIC [enforcement mechanism]
- 🚨 BLOCKING: [Function] with real-time [monitoring/detection]  
- 🚨 CRITICAL: [Function] with immediate [correction/activation]

### **🚨 ERROR PROTOCOL ENFORCEMENT**
**🚨 ZERO TOLERANCE Error Enforcement**:
- **🚨 CRITICAL Error Detection**: IMMEDIATE activation of 8-step resolution protocol
- **🚨 BLOCKING Continuation**: NO execution continues without protocol completion
- **🚨 MANDATORY Protocol Steps**: Steps 1-4 AUTOMATIC, Steps 5-8 MANUAL with verification

## Execution Process

### Phase 1: **🚨 MANDATORY [Phase Name]**
- **🚨 BLOCKING [Action]**: [Description] with ZERO tolerance enforcement
- **🚨 AUTOMATIC [Action]**: [Description] with real-time monitoring
- **🚨 CRITICAL [Action]**: [Description] with immediate validation

### Phase 2: **🚨 REQUIRED [Phase Name]**
- **🚨 MANDATORY [Action]**: [Description] with systematic enforcement
- **🚨 BLOCKING [Action]**: [Description] with violation prevention
- **🚨 AUTOMATIC [Action]**: [Description] with continuous operation

### Phase 3: **🚨 CRITICAL [Phase Name]**
- **🚨 MAXIMUM [Action]**: PRIORIDAD ABSOLUTA with strictest enforcement
- **🚨 BLOCKING [Action]**: [Description] with immediate correction
- **🚨 REQUIRED [Action]**: [Description] with compliance verification

### Phase 4: **🚨 MAXIMUM [Phase Name]**
- **🚨 ZERO TOLERANCE**: [Action] with absolute priority enforcement
- **🚨 REAL-TIME**: [Action] with continuous monitoring and correction
- **🚨 UNIVERSAL**: [Action] with cross-domain application

### Phase 5: **🚨 MANDATORY Routing Enforcement**
**🚨 BLOCKING Command Routing**: AUTOMATIC next command determination with ZERO tolerance
- **🚨 CRITICAL Priority Calculation**: MANDATORY mathematical assessment of routing decisions
- **🚨 BLOCKING Handoff Protocol**: REQUIRED format "Next: /command (🚨priority) - rationale"
- **🚨 AUTOMATIC Integration**: Sistema WILL coordinate with /handoff-manager enforcement
- **🚨 MANDATORY Documentation**: BLOCKING execution without routing decision recording
- **🚨 REAL-TIME Monitoring**: Continuous validation of routing compliance and effectiveness

**🚨 ENFORCEMENT**: Sistema WILL calculate routing with MAXIMUM priority and BLOCKING validation

## Enforcement Validation
- **Sistema WILL/MUST patterns**: ≥3 per command
- **🚨 enforcement symbols**: ≥5 per command  
- **BLOCKING/MANDATORY designations**: ≥70% coverage
- **Real-time monitoring**: ≥2 specifications per command

---

@./docs/core/README.md
@./docs/core/system-principles.md
```

## Implementation Guidelines

### Choosing the Right Template
1. **Basic Command**: Standard functionality without special compliance needs
2. **P55/P56 Compliant**: Commands requiring mathematical validation and tool call execution
3. **Enforcement Command**: Commands requiring blocking mechanisms and strict compliance

### Phase 5 Integration Pattern
**Universal Routing Protocol**: All commands now include Phase 5 for intelligent command routing

**Routing Format Standards**:
- **Basic**: "Next: /[category]/[command] ([priority]) - [rationale]"
- **P55/P56**: Mathematical priority calculation with ≥4 decimal precision
- **Enforcement**: 🚨 MANDATORY routing with BLOCKING validation

**Integration Requirements**:
- **handoff-manager**: Coordinate seamless transitions between commands
- **notify-manager**: Transparent delegation and state tracking
- **Mathematical Assessment**: Priority scoring using context_engineering_formulas.sh
- **Documentation**: Record all routing decisions for learning extraction

### Customization Instructions
1. **Replace all bracketed placeholders** with command-specific content
2. **Adapt phase descriptions** to match command functionality
3. **Maintain structural consistency** across all commands
4. **Preserve enforcement patterns** when using enforcement template
5. **Implement Phase 5 routing** according to template variant requirements

### Quality Standards
- **Line Limit**: ≤150 lines per command (including Phase 5)
- **Instruction Clarity**: ≤15 words per instruction
- **Self-Containment**: All dependencies explicitly stated
- **TodoWrite Integration**: Consistent progress tracking throughout all 5 phases
- **Phase 5 Compliance**: ≤15 lines maximum for routing implementation
- **Routing Format**: Standardized handoff protocol across all template variants

## Cross-References
- [Documentation Templates](./02-documentation-templates.md) - For command documentation
- [Validation Templates](./03-validation-templates.md) - For command testing
- [Integration Templates](./04-integration-templates.md) - For system integration

---

**Template Category**: Command development templates
**Consolidation**: 4 templates → 3 variants (Basic, P55/P56, Enforcement)
**Usage**: All command development in ce-simple system
**Authority**: Unified command template system