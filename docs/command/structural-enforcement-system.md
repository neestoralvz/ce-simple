# Structural Enforcement System - Executable Automation Framework

## 🎯 Purpose
Define executable automation protocols that use available tools (Bash, LS, Read, Edit, Glob, Grep) to automatically detect and correct structural violations during command execution.

## 🔧 EXECUTABLE VALIDATION PROTOCOL

### Automatic Structural Validation
**MANDATORY for all commands with structural intelligence**:

```markdown
### Structural Validation (EXECUTABLE)
**PRE-EXECUTION AUTOMATION**:

1. **🏗️ STRUCTURE-VALIDATION**:
   ```
   # Check canonical structure exists
   LS path="/" → Verify docs/, context/, .claude/ exist
   LS path="/docs" → Verify subdirectories (structure/, command/, etc.)
   LS path="/context" → Verify subdirectories (discoveries/, patterns/, etc.)
   ```

2. **🔍 VIOLATION-DETECTION**:
   ```
   # Find misplaced files
   Glob pattern="*.md" path="/" → Identify files in wrong locations
   Grep pattern="standards/" path=".claude/commands" → Find old references
   ```

3. **⚡ AUTO-CORRECTION-EXECUTION**:
   ```
   # Execute corrections automatically
   Bash command="mkdir -p docs/structure" → Create missing directories
   Bash command="mv misplaced.md docs/appropriate-dir/" → Move files
   Edit old_string="standards/" new_string="docs/" → Fix references
   ```

4. **✅ VALIDATION-VERIFICATION**:
   ```
   # Verify corrections completed
   LS path="/docs" → Confirm structure compliance
   Grep pattern="docs/" path=".claude/commands" → Verify reference updates
   ```
```

## 🚀 AUTOMATIC CORRECTION TRIGGERS

### Level 1: Silent Auto-Correction (Execute Immediately)
```bash
# Detect and fix broken references
find .claude/commands -name "*.md" -exec grep -l "standards/" {} \; | while read file; do
    sed -i 's|standards/|docs/|g' "$file"
done

# Move misplaced files to correct structure
if [ -d "standards" ] && [ ! -d "docs" ]; then
    mv standards docs
fi

# Create missing directories
mkdir -p docs/{structure,command,documentation,implementation,quality,workflow}
mkdir -p context/{discoveries,experience,patterns,research,workflows}
```

### Level 2: Validation + Auto-Correction (Notify + Execute)
```markdown
**DETECTION PROTOCOL**:
- Use Glob to find files in wrong locations
- Use Grep to identify structural violations
- Use LS to validate directory compliance

**CORRECTION PROTOCOL**:  
- Use Bash to move files automatically
- Use Edit to fix references in batches
- Use Write to create missing structure files
```

### Level 3: Major Restructuring (Notify + Recommend + Execute with confirmation)
```markdown
**MAJOR CHANGES REQUIRING CONFIRMATION**:
- Directory tree restructuring (standards/ → docs/)
- Batch reference updates across multiple files
- File consolidation or extraction operations

**EXECUTION AFTER CONFIRMATION**:
- Use MultiEdit for batch reference corrections
- Use Bash for complex file operations
- Use Write for creating new organizational files
```

## 📋 ENFORCEMENT IMPLEMENTATION MATRIX

### Command Integration Requirements

#### `/start` - Master Structural Enforcer:
```markdown
### Structural Enforcement Protocol (EXECUTABLE)
**MANDATORY PRE-EXECUTION**:

# 1. Validate Structure
LS path="/" → Check docs/, context/, .claude/ exist

# 2. Detect Violations  
Glob pattern="standards" → Detect old structure
Grep pattern="standards/" path=".claude/commands" → Find old references

# 3. Execute Corrections
IF standards/ exists:
    Bash command="mv standards docs" → Migrate structure
    Edit pattern: Replace "standards/" with "docs/" in all .claude/commands/*.md files

# 4. Verify Compliance
LS path="/docs" → Confirm structure exists
Grep pattern="docs/" path=".claude/commands" → Verify references updated
```

#### `/explore-codebase` - Structure Analysis + Correction:
```markdown
### Structural Analysis and Enforcement (EXECUTABLE)
**DURING EXPLORATION**:

# 1. Analyze Project Structure
LS path="/" → Document current structure
Glob pattern="*.md" → Find all documentation files

# 2. Identify Structural Violations
Find files in wrong locations, detect missing directories, identify broken references

# 3. Execute Structure Corrections
Bash: Create missing directories
Bash: Move misplaced files  
Edit: Fix broken references automatically

# 4. Document Structure Analysis
Write structured analysis to context/discoveries/structure-analysis-[date].md
```

#### `/docs-workflow` - Documentation Structure Guardian:
```markdown
### Documentation Structure Enforcement (EXECUTABLE)
**STRUCTURAL PREPROCESSING**:

# 1. Validate Documentation Structure
LS path="/docs" → Verify all required subdirectories
Glob pattern="**/*.md" path="/docs" → Inventory all documentation files

# 2. Enforce Size Compliance
Read each file → Check line counts
IF file > 200 lines: Extract oversized content to appropriate docs/ subdirectory

# 3. Fix Reference Integrity
Grep broken references across documentation
Edit: Batch fix all broken references automatically

# 4. Verify Documentation Health
Generate compliance report with automatic corrections applied
```

## 🔄 EXECUTION WORKFLOW

### Automatic Execution Flow:
```
Command Invocation → 
  Structural Validation (LS/Glob) →
    Violation Detection (Grep/Read) →
      Auto-Correction (Bash/Edit) →
        Verification (LS/Grep) →
          Command Logic Execution
```

### Decision Tree for Corrections:
```
Violation Detected?
├─ YES → Determine Severity Level
│   ├─ Level 1 (Minor) → Execute silently (Bash/Edit)
│   ├─ Level 2 (Moderate) → Notify + Execute (Bash/MultiEdit)  
│   └─ Level 3 (Major) → Request confirmation + Execute
└─ NO → Proceed with command logic
```

## 📊 ENFORCEMENT VERIFICATION

### Success Metrics (Automatically Measured):
- **Structure Compliance**: LS verification of canonical directory structure
- **Reference Integrity**: Grep verification of 100% working references  
- **File Placement**: Glob verification of files in correct locations
- **Size Compliance**: Read verification of file size limits

### Automatic Reporting:
```markdown
**STRUCTURAL HEALTH REPORT** (Auto-Generated):
✅ Directory Structure: [COMPLIANT/VIOLATIONS]
✅ Reference Integrity: [X% functional]  
✅ File Placement: [X files moved to correct locations]
✅ Size Compliance: [X files within limits]
⚡ Auto-Corrections Applied: [X violations fixed]
```

## 🎯 IMPLEMENTATION PROTOCOLS

### Required Tool Usage Patterns:
- **LS**: Structure validation, directory verification
- **Bash**: File operations, directory creation, structure corrections  
- **Glob**: File discovery, pattern matching, violation detection
- **Grep**: Reference validation, broken link detection
- **Read**: Content analysis, size compliance checking
- **Edit/MultiEdit**: Reference corrections, batch updates
- **Write**: Structure documentation, compliance reports

### Command Enhancement Template:
```markdown
### Structural Enforcement Protocol (EXECUTABLE)
**MANDATORY PRE-EXECUTION**:

1. **Structure Validation**: [LS commands for verification]
2. **Violation Detection**: [Glob/Grep commands for finding issues]  
3. **Auto-Correction**: [Bash/Edit commands for fixing violations]
4. **Verification**: [LS/Grep commands for confirming fixes]

[Continue with original command logic...]
```

---

**CRITICAL**: This system provides REAL automation using available tools. Commands will automatically detect and correct structural violations without manual intervention, making the system truly self-maintaining and intelligent.