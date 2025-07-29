# Error Detection Categories - Specific Error Types & Patterns

**29/07/2025** | State management + workflow + documentation error detection

## State Management Error Detection

### Todo List Synchronization Validation
```markdown
## Detection Triggers
- **Before progress reporting**: Validate todo list matches actual work state
- **After task completion**: Verify todo list updated to reflect completion
- **During continuous execution**: Monitor todo list accuracy in real-time
- **User status inquiry**: Cross-validate reported status with actual progress
```

### Progress Tracking Consistency
```markdown
## Validation Points
- **Work completion vs reporting**: Ensure reported progress matches actual completion
- **Multi-task progress tracking**: Validate progress across parallel tasks stays synchronized
- **Status persistence**: Verify progress state maintained across session boundaries
- **Completion acknowledgment**: Ensure completion signals properly integrated
```

### Pre-Communication Validation
```markdown
## Communication Accuracy Checks
- **Status report accuracy**: Cross-validate all reported status with actual state
- **Progress claim verification**: Verify claimed progress matches actual completion
- **Next step appropriateness**: Validate suggested next steps reflect real state
- **Error acknowledgment**: Ensure errors reported accurately without minimization
```

## Workflow Error Detection

### Feedback Processing Patterns
```markdown
## User Correction Integration
- **Acknowledge correction explicitly**: Never ignore or minimize user corrections
- **Apply correction immediately**: Update state to reflect user-provided accuracy
- **Learn from correction pattern**: Identify systematic issues causing user corrections
- **Prevent correction repetition**: Implement detection to prevent similar errors
```

### Dependency Verification Points
```markdown
## Prerequisite Validation
- **Command dependency satisfaction**: Verify all dependencies met before command execution
- **Resource availability**: Ensure required resources accessible before starting work
- **State prerequisite verification**: Validate system state meets command requirements
- **Integration point validation**: Verify integration dependencies satisfied
```

### Workflow Chain Integrity
```markdown
## Chain Validation Patterns
- **Next action validity**: Verify suggested next actions are executable and appropriate
- **Command dependency satisfaction**: Ensure command prerequisites are met
- **Workflow state consistency**: Validate workflow state transitions are correct
- **Error recovery paths**: Verify error handling routes to appropriate resolution commands
```

## Documentation Error Detection

### Content Accuracy Validation
```markdown
## Documentation Verification
- **Reference link accuracy**: Verify all documentation links point to existing content
- **Information currency**: Ensure documentation reflects current system behavior
- **Template compliance**: Validate documents follow current template standards
- **Cross-reference integrity**: Verify bidirectional links maintain accuracy
```

### System Reflection Validation
```markdown
## System Behavior Alignment
- **Command behavior documentation**: Ensure documentation matches actual command behavior
- **Template accuracy**: Verify templates reflect current usage patterns
- **Process documentation**: Ensure documented processes match actual implementation
- **Integration documentation**: Validate documented integrations work as described
```

---
**Referencias:** → context/operational/enforcement/error_detection_principles.md (framework purpose)
→ context/operational/enforcement/error_detection_automation.md (automation integration)