# Next Action Patterns - Workflow Integration Authority

**29/07/2025** | Complete next action patterns for role command workflow integration

## AUTORIDAD SUPREMA
role_command_template.md → next-action-patterns.md implements action patterns per template authority

## CONSULTATION ROLE ACTION PATTERNS

### **Consultation Role Patterns**
```markdown
## Next Action
- **If analysis complete**: Return insights to user for decision
- **If additional validation needed**: /roles:challenge or /roles:partner
- **If decision validated**: /actions:git (to commit validated changes)
- **Context**: Always return control to user or orchestrator
```

### **Consultation Pattern Explanation**
- **Analysis Completion**: Results returned to user for final decision authority
- **Validation Escalation**: Additional consultation roles for comprehensive analysis
- **Decision Implementation**: Action execution after user validation
- **Control Return**: User or orchestrator maintains workflow authority

## EXECUTION ROLE ACTION PATTERNS

### **Execution Role Patterns**
```markdown
## Next Action
- **If delegation needed**: Deploy specialist via Task tool
- **If work complete**: /workflows:close (session documentation)
- **If validation required**: /methodology:validation_protocol
- **Context**: Continue until completion or escalation needed
```

### **Execution Pattern Explanation**
- **Delegation Logic**: Specialist deployment for complex task execution
- **Completion Protocol**: Session documentation and workflow closure
- **Validation Requirements**: Systematic validation before completion
- **Continuous Execution**: Workflow continuation until completion or escalation

## ACTION PATTERN INTEGRATION FRAMEWORK

### **Workflow Continuity Principles**
- **Clear Transitions**: Each action pattern provides clear next step logic
- **Authority Respect**: All actions respect user domain and system authority
- **Systematic Validation**: Validation protocols integrated at appropriate points
- **Escalation Logic**: Clear escalation paths for complex or blocked situations

### **Pattern Selection Logic**
- **Condition-Based**: Action selection based on specific workflow conditions
- **Role-Appropriate**: Actions align with role category and function
- **System Integration**: Actions integrate with broader workflow and command systems
- **User Control**: User maintains ultimate authority over action execution

## WORKFLOW INTEGRATION STANDARDS

### **Action Pattern Requirements**
- **Condition Clarity**: Clear conditions for action selection
- **Command Integration**: Actions integrate with existing command ecosystem
- **Authority Preservation**: All actions maintain user authority supremacy
- **System Continuity**: Actions support continuous workflow execution

---

**NEXT ACTION PATTERNS DECLARATION**: Complete action pattern framework with consultation and execution workflows, systematic validation, and authority-preserving workflow integration protocols.