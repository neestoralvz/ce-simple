# System Naming Conventions - Unified Standards

**31/07/2025 CDMX** | Complete file system naming standardization

## AUTORIDAD SUPREMA
User explicit authority: "English naming for all files and directories" → NAMING_CONVENTIONS.md implements unified naming system

## PRINCIPIO FUNDAMENTAL
**"Single clear English naming convention per file type"** - Eliminate español/inglés mixing and standardize separation patterns for maximum system coherence.

## UNIFIED NAMING SYSTEM

### **Language Standard (MANDATORY)**
- **ENGLISH ONLY**: All files, directories, and identifiers
- **NO SPANISH**: Complete migration from Spanish names required
- **USER AUTHORITY**: "English naming for all files and directories" (architecture/README.md)
- **CLARITY PRIORITY**: "Single words when clear" per user simplicity preference

### **Separation Conventions by File Type**
```
File Type               Convention          Example
---------------------------------------------------
Markdown Files         kebab-case.md       socratic-methodology.md
Python Scripts         snake_case.py       system_health.py
Shell Scripts          kebab-case.sh       think-x4-validator.sh
Directories           kebab-case/         simplicity-system/
JSON/Config           kebab-case.json     claude-config.json
Text Files            kebab-case.txt      system-log.txt
```

### **Special Pattern Exceptions (PRESERVED)**
- **ADRs**: `ADR-###-descriptive-name.md` (existing pattern validated)
- **Timestamps**: `YYYYMMDD_HHMM_descriptive-name.md` (processed conversations)
- **Handoffs**: `HANDOFF_#_DESCRIPTIVE_NAME.md` (existing pattern validated)
- **Backup Files**: `filename_BACKUP_###_lines.md` (temporary - should be eliminated)

## CRITICAL MIGRATION TARGETS

### **Phase 1: Spanish → English Core Files (HIGH PRIORITY)**
```
Current Spanish Name              → Proposed English Name
---------------------------------------------------------------
metodologia_socratica.md         → socratic-methodology.md  
flujos_trabajo.md                → workflow-patterns.md
simplicidad_belleza.md           → simplicity-principles.md
```

### **Phase 2: Directory Standardization (MEDIUM PRIORITY)**
```
Current Mixed Convention         → Standard Convention
---------------------------------------------------------------
simplicidad-system/             → simplicity-system/ (already correct)
context/vision/                 → context/vision/ (already correct)  
tools/automation/               → tools/automation/ (already correct)
```

### **Phase 3: Cleanup Massive Temporary Files (HIGH PRIORITY)**
- **Target**: 200+ `*_BACKUP_*lines*` files → DELETE (temporary accumulation)
- **Target**: Excessive `scripts/validation_results_*` directories → ARCHIVE
- **Impact**: ~80% file count reduction, massive system simplification

## VALIDATION RULES

### **Compliance Checks**
1. **Language**: No Spanish words in file/directory names
2. **Convention**: Correct separator for file type (kebab vs snake)
3. **Clarity**: Single words when meaning is clear
4. **Consistency**: Same pattern applied across similar files

### **Anti-Patterns (PROHIBITED)**
- ❌ Mixed language: `metodologia-system.md`
- ❌ Wrong separator: `socratic_methodology.md` (should be kebab for .md)
- ❌ Excessive verbosity: `user-vision-simplicity-beauty-principles.md`
- ❌ Temporary accumulation: Multiple `*_BACKUP_*` files

### **Quality Gates**
- **Pre-Migration**: Complete cross-reference mapping
- **Post-Migration**: Automated reference validation  
- **Authority Verification**: 95%+ user voice fidelity preserved
- **System Functionality**: 100% functionality maintained

## IMPLEMENTATION PROTOCOL

### **Migration Safety Requirements**
1. **Cross-Reference Mapping**: Document all references before renaming
2. **Batch Updates**: Update all references simultaneously with renaming
3. **Rollback Capability**: Full system backup before major changes
4. **Validation Testing**: Verify system functionality post-migration

### **Priority Execution Order**
1. **IMMEDIATE**: Cleanup temporary/backup files (safe deletion)
2. **HIGH**: Spanish→English core files (requires reference updates)
3. **MEDIUM**: Directory standardization (path updates required)  
4. **LOW**: Tool script standardization (mostly cosmetic)

---

**NAMING SYSTEM DECLARATION**: This unified naming convention eliminates system inconsistencies while preserving user authority supremacy and enabling maximum system coherence through English-only standardization.

**EVOLUTION PATHWAY**: Current inconsistencies → systematic migration → unified standards → maintenance automation