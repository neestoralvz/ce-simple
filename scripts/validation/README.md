# Validation Scripts

**Category**: System Integrity & Quality Assurance
**Scripts**: 5 scripts for comprehensive validation

## Scripts Overview

### **validate_integrity.sh**
**Purpose**: Complete system health validation after changes
**Usage**: `./validate_integrity.sh`
**Validates**: File sizes, cross-references, authority chains, navigation

### **authority-validator.sh**
**Purpose**: Authority chain integrity verification  
**Usage**: `./authority-validator.sh [file]`
**Validates**: User authority preservation, reference chains

### **validate-context-coherence.sh**
**Purpose**: CLAUDE.md conditional links coherence validation
**Usage**: `./validate-context-coherence.sh`
**Validates**: Semantic triggers, context loading patterns

### **validate-script-communication.sh**
**Purpose**: Script communication protocol validation
**Usage**: `./validate-script-communication.sh`
**Validates**: Silent script protocols, error handling

### **validation_suite.sh**
**Purpose**: Complete validation suite orchestration
**Usage**: `./validation_suite.sh`
**Runs**: All validation scripts with comprehensive reporting

### **quality-gate.sh**
**Purpose**: Quality assurance gates for workflow checkpoints
**Usage**: `./quality-gate.sh`
**Validates**: Quality standards before workflow continuation

## Integration Points

- **Post-Extraction Validation**: Validates system health after L2-modular operations
- **Authority Preservation**: Ensures user voice fidelity throughout changes
- **Workflow Gates**: Provides pass/fail gates for automated workflows

## Dependencies

- **Input**: Modified files, system state, authority references
- **Output**: PASS/FAIL status with detailed violation reports