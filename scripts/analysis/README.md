# Analysis Scripts

**Category**: File & System Analysis Tools
**Scripts**: 4 scripts for violation detection and system analysis

## Scripts Overview

### **analyze_violations.sh**
**Purpose**: Comprehensive file size violation analysis for PHASE_0_EMERGENCY
**Usage**: `./analyze_violations.sh`
**Output**: Categorized violation reports (L0-EMERGENCY, L1-CRITICAL, L2-HIGH)

### **analyze_real_violations.sh** 
**Purpose**: Real-time violation detection with filtering
**Usage**: `./analyze_real_violations.sh`
**Output**: Current violations excluding archived content

### **enhanced_analyze_violations.sh**
**Purpose**: Advanced analysis with structure breakdown
**Usage**: `./enhanced_analyze_violations.sh`
**Output**: Detailed structure analysis per file

### **domain-classifier.sh**
**Purpose**: Content domain classification for organization
**Usage**: `./domain-classifier.sh [file]`
**Output**: Domain classification with placement recommendations

## Integration Points

- **PHASE_0_EMERGENCY Workflow**: Provides violation detection for extraction planning
- **L2-Modular System**: Identifies candidates for modular extraction
- **Quality Gates**: Analysis results feed into validation systems

## Dependencies

- **Input**: Context files, git repository state
- **Output**: Analysis reports consumed by extraction and validation scripts