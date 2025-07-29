# Error Detection Protocol

**29/07/2025 12:15 CDMX** | Detection patterns y identification methodology para errores sistémicos

## Error Detection Framework

### Detection Triggers
```markdown
## Pre-Status Report Validation
- **Before reporting progress**: Validate todo list reflects actual work state
- **During continuous execution**: Update todo list after cada completion
- **When user questions status**: Cross-validate todo list con actual progress
- **Periodic consistency check**: System-wide state validation
```

### Detection Methods
```markdown
## Consistency Validation Patterns
- **Todo list vs work artifacts**: Compare list status with actual files created/modified
- **Progress reporting accuracy**: Verify reported progress matches actual completion
- **State synchronization check**: Ensure internal state matches external reporting
- **User feedback integration**: Use user corrections as error detection signal
```

## Systematic Error Categories

### State Management Errors
**Pattern**: Internal system state inconsistent with external reporting
**Examples**: Todo list desynchronization, progress tracking errors, status reporting inaccuracies
**Detection**: State validation protocols, consistency checks, real-time updates

### Communication Accuracy Errors  
**Pattern**: Information provided to user doesn't match actual system state
**Examples**: Incorrect status reports, outdated progress information, misleading capability claims
**Detection**: Pre-communication validation, accuracy verification, truth checking

### Workflow Continuity Errors
**Pattern**: Process flow breaks due to state inconsistencies or missing information
**Examples**: Commands referencing non-existent files, broken workflow chains, missing dependencies
**Detection**: Dependency validation, workflow testing, continuity verification

### Documentation Synchronization Errors
**Pattern**: Documentation doesn't reflect actual system behavior or current state
**Examples**: Outdated command descriptions, incorrect reference links, obsolete procedures
**Detection**: Documentation validation, synchronization protocols, accuracy maintenance

## Error Pattern Recognition

### Specific Error Instance Example
**Error**: Todo list reportaba tareas como "pending" cuando ya estaban completadas
**Impact**: Usuario recibió información incorrecta sobre work status
**Root Cause**: Agent no mantuvo todo list synchronized con actual work progress
**Detection**: Usuario identified discrepancy between reported status y actual completions

### Systematic Pattern Recognition
**Pattern**: State management inconsistency between internal work progress y external status reporting
**Frequency**: Critical - impacts user trust and workflow coordination
**Domain**: Task management, progress tracking, communication accuracy
**Prevention Need**: Systematic protocol to prevent recurrence

---
**Authority Source**: Systematic error prevention design + detection methodology analysis
**Related Modules**: → error_prevention_methodology.md, recovery_procedures.md
**Integration**: All workflow protocols, communication patterns, state management systems

## Enlaces → Información Complementaria
**Si necesitas prevention strategies:** → error_prevention_methodology.md
**Si requieres recovery procedures:** → recovery_procedures.md
**Si buscas todo list protocols:** → context/enforcement/core_reminders.md:38-48