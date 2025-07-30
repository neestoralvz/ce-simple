# Orchestration Protocol - Comportamiento Orquestación

## Matrix Core Behavior
**Commands maintain independence but coordinate intelligently based on context**

## Command Independence + Coordination

### Self-Containment Rules
**Trigger:** Command execution request
**Behavior:** 
- Commands are self-contained within commands/ folder
- No external file dependencies allowed
- Inter-command communication only through defined interfaces

**Implementation:**
- Validate command isolation before execution
- Route requests through command-to-command protocols
- Maintain separation between command logic and system files

### Subagent Orchestration Protocol
**Trigger:** Complex task requires specialized handling
**Behavior:** Main agent ALWAYS orchestrates through subagents
**Method:**
1. **Task analysis** → Identify specialized domain
2. **Template selection** → @context/operational/patterns/task_tool_methodology.md
3. **Deployment** → Use appropriate specialist template with context loading
4. **Coordination** → Manage multi-subagent interactions via proper Task tool syntax
5. **Result integration** → Compile specialized outputs + post-validation

## Universal Command Integration

### Context-Aware Command Starter
**Trigger:** Session initiation or context review request
**Behavior:** 
- Review current system context automatically
- Propose conversation starters based on state
- Identify unfinished tasks for resumption
- Adapt options based on available commands

**Dynamic Adaptation:**
- Options evolve with system capabilities
- Command availability drives interface presentation
- Context intelligence determines suggestion relevance

### Workflow Chain Orchestration
**Trigger:** Multi-step workflow requirement
**Behavior:**
1. **Workflow identification** → Map required command sequence
2. **Chain construction** → Build command execution pipeline
3. **Context preservation** → Maintain state across commands
4. **Quality gates** → Apply creation→alignment→verification protocol

## Matrix Interaction Patterns

### Universal Entry Hub Function
**Entry Point Behavior:**
- Analyze current context automatically
- Route to appropriate specialized commands via Task tool delegation
- Maintain orchestration oversight during execution
- Adapt available options dynamically based on Task tool specialization patterns

### Command Chain Coordination
**Multi-Command Sequences:**
- Preserve context across command boundaries
- Handle inter-command data transfer
- Manage execution flow and error propagation
- Validate workflow completion

## Decision Tree Integration
**Embedded in every command/document:**
- **Trigger conditions** → When to activate this behavior
- **Context routing** → Which related behaviors to consider
- **Exit conditions** → When to transition elsewhere
- **Efficiency metrics** → Measure decision effectiveness

## Guardian Integration Protocol

### Role-Based Enforcement Architecture
**Partner (Constructor)**: Challenges through socratic methodology, explores alternatives
**Guardian (Enforcer)**: Binary compliance validation, "no mercy" enforcement
**Orchestrator**: Coordinates both roles based on context requirements

### Guardian Activation Triggers
**Auto-activation conditions**:
- File size violations detected (>80 lines)
- Authority chain breaches (TRUTH_SOURCE.md supremacy)
- Vision modification attempts (user domain preservation)
- Standards non-compliance (system integrity)
- Architectural deviation (vision alignment validation)

### Enforcement Coordination
**Workflow**: Detection → Guardian enforcement → Partner construction → Validation
**Authority**: Guardian stops violations, Partner proposes solutions
**Integration**: @context/system/standards/notification_formatting_standards.md

## Anti-Patterns Prevention
- **Direct complex execution** → Always delegate via @context/operational/patterns/task_tool_methodology.md
- **Broken Task tool syntax** → Use templates from @context/system/templates/task_tool_templates.md
- **Command isolation violation** → Block external file access
- **Context fragmentation** → Maintain orchestration visibility
- **Static option presentation** → Require dynamic adaptation
- **Enforcement bypassing** → Guardian integration mandatory for standards violations

---
**Trazabilidad:** context/archive/legacy/user-vision-layers/layer2/comandos_orquestacion_matrix.md → Behavior distillation
**Triggers:** Task complexity, session start, workflow request, command coordination
**Integration:** → patterns/command_architecture.md, patterns/task_tool_methodology.md, patterns/role_ecosystem_architecture.md
**Role Ecosystem**: Guardian enforcement + Partner construction + Orchestrator coordination