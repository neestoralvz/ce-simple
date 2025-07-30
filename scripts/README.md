# PHASE_0_EMERGENCY Scripts - Hybrid Extraction System

**30/07/2025 CDMX** | Secure automation for 103 file size violations with triple backup protection

## SCRIPT ECOSYSTEM OVERVIEW

### **Security-First Architecture**
All scripts implement **Think x4** principles with multiple validation layers:
1. **Triple Backup System** - Zero data loss guarantee
2. **Manual Validation Checkpoints** - User authority preservation
3. **Automatic Rollback Capability** - Emergency recovery 
4. **Integrity Validation** - System health monitoring

## CORE SCRIPTS

### **1. backup_secure.sh - Triple Backup System**
```bash
./backup_secure.sh
```
**Purpose**: Creates comprehensive backup before any extraction
**Features**:
- ✅ Triple backup (original → backup → working copy)
- ✅ Git checkpoint creation
- ✅ Backup integrity validation
- ✅ Categorized backups (L0/L1/L2)

**SAFETY**: ALWAYS run first - no extraction without backup

### **2. analyze_violations.sh - Comprehensive Analysis**
```bash
./analyze_violations.sh
```
**Purpose**: Analyzes all 103 violations and creates extraction strategy
**Features**:
- ✅ Violation categorization (L0-EMERGENCY, L1-CRITICAL, L2-HIGH)
- ✅ File structure analysis for extraction guidance
- ✅ Pilot test candidate selection
- ✅ Comprehensive analysis report

**Output**: Complete violation breakdown with extraction recommendations

### **3. extract_assisted.sh - Semiautomated Extraction**
```bash
./extract_assisted.sh [OPTIONS] TARGET_FILE
```
**Purpose**: Hybrid extraction with manual validation checkpoints
**Modes**:
- `single` - Process individual file with full supervision
- `pilot` - Process 5 L2-HIGH test files (planned)
- `batch` - Process multiple files by category (planned)

**Safety Features**:
- ✅ Manual validation checkpoints
- ✅ Structure analysis before extraction
- ✅ Simulation mode available
- ✅ Individual file backups

### **4. validate_integrity.sh - System Health Check**
```bash
./validate_integrity.sh
```
**Purpose**: Comprehensive system validation after extraction
**Validation Areas**:
- ✅ File size compliance (≤80 lines)
- ✅ Cross-reference integrity
- ✅ Authority chain preservation
- ✅ System navigation functionality

**Result**: PASS/FAIL with detailed violation report

### **5. rollback_safe.sh - Emergency Recovery**
```bash
./rollback_safe.sh [OPTIONS] BACKUP_DIR
```
**Purpose**: Safe system recovery if extraction fails
**Capabilities**:
- ✅ Full system rollback
- ✅ Selective file rollback
- ✅ Git reset to checkpoint
- ✅ Post-rollback validation

**Emergency Usage**: `./rollback_safe.sh -fgv /path/to/backup`

## HYBRID WORKFLOW

### **Phase 1: Preparation & Safety**
```bash
# 1. Analyze current violations
./analyze_violations.sh

# 2. Create comprehensive backup
./backup_secure.sh

# 3. Review analysis results
less analysis_results_*/VIOLATION_ANALYSIS_REPORT.md
```

### **Phase 2: Pilot Testing (L2-HIGH Files)**
```bash
# Test methodology on 5 safest files (100-120 lines)
./extract_assisted.sh -m pilot

# Validate pilot results
./validate_integrity.sh

# Refine methodology based on results
```

### **Phase 3: Systematic Extraction**
```bash
# Process L2-HIGH files (80-199 lines)
./extract_assisted.sh -m batch -c L2

# Process L1-CRITICAL files (200-399 lines)  
./extract_assisted.sh -m batch -c L1

# Process L0-EMERGENCY files (≥400 lines)
./extract_assisted.sh -m batch -c L0
```

### **Phase 4: Final Validation**
```bash
# Complete system validation
./validate_integrity.sh

# Deploy Guardian prevention system
echo "TODO: Guardian deployment script"
```

## SAFETY PROTOCOLS

### **Before Every Session**
1. ✅ Run `backup_secure.sh` for triple backup
2. ✅ Run `analyze_violations.sh` for current state
3. ✅ Review analysis report thoroughly
4. ✅ Ensure git working directory is clean

### **During Extraction**
1. ✅ Use simulation mode first: `./extract_assisted.sh -s file.md`
2. ✅ Process small batches (5-10 files maximum)
3. ✅ Validate integrity after each batch
4. ✅ Manual checkpoint approval required

### **Emergency Procedures**
1. 🚨 **System Corruption**: `./rollback_safe.sh -fgv backup_dir`
2. 🚨 **Partial Failure**: `./rollback_safe.sh -s backup_dir file1.md file2.md`
3. 🚨 **Reference Breakage**: `./validate_integrity.sh` → fix → re-validate

## SUCCESS METRICS

### **Target Compliance**
- **File Size**: 103 violations → 0 violations (100% compliance)
- **Authority Preservation**: 95%+ user voice fidelity maintained
- **Functionality**: 100% system functionality through reference architecture
- **Reference Integrity**: 0 broken cross-references

### **Quality Gates**
- ✅ Every extraction: File size compliance verified
- ✅ Every batch: Reference integrity validated
- ✅ Every phase: Authority chain preserved
- ✅ Final validation: Complete system health confirmed

## CURRENT STATUS

### **Completed Components**
- ✅ **Security Scripts**: Triple backup + validation + rollback system
- ✅ **Analysis Engine**: Comprehensive violation analysis with strategy
- ✅ **Extraction Framework**: Semiautomated extraction with checkpoints
- ✅ **Safety Protocols**: Emergency recovery and integrity validation

### **Next Implementation**
- 🔄 **Pilot Testing**: L2-HIGH test candidates (5 files)
- ⏳ **Batch Processing**: Multi-file extraction modes
- ⏳ **Guardian Integration**: Automated prevention system
- ⏳ **Performance Metrics**: Extraction efficiency measurement

## TECHNICAL ARCHITECTURE

### **Script Dependencies**
```
backup_secure.sh     [Independent - run first]
     ↓
analyze_violations.sh [Independent - run second]
     ↓
extract_assisted.sh  [Depends on analysis results]
     ↓
validate_integrity.sh [Validates extraction results]
     ↓
rollback_safe.sh     [Emergency recovery if needed]
```

### **Data Flow**
```
Raw Context Files → Analysis → Backup → Extraction → Validation → Success
                                    ↓
                            Rollback ← Validation Failure
```

### **File Naming Conventions**
- **Backups**: `filename_BACKUP_lines_lines.md`
- **Analysis**: `filename_analysis.txt`
- **Modules**: `domain-name.md`
- **Hubs**: `filename_HUB.md`
- **Sessions**: `session_YYYYMMDD_HHMMSS/`

---

## EXECUTION READINESS

**SYSTEM STATUS**: ✅ **READY FOR PILOT TESTING**

All security systems validated. Triple backup architecture confirmed. 
Hybrid approach with manual checkpoints ensures user authority preservation.

**NEXT STEP**: Execute pilot testing with 5 L2-HIGH candidates to validate methodology.

---
**HYBRID SYSTEM DECLARATION**: Scripts amplify human capability while preserving user authority supremacy. Complete safety architecture prevents data loss while enabling efficient mass extraction per user vision.