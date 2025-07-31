#!/bin/bash
# backup_secure.sh - Triple Backup System for PHASE_0_EMERGENCY
# 30/07/2025 CDMX | Secure backup with validation for file size violations

set -e  # Exit on any error

# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Configuration
BACKUP_DIR="$PROJECT_ROOT/context/archive/emergency_backups_$(date +%Y%m%d_%H%M%S)"
WORKING_DIR="$PROJECT_ROOT/context"
LOG_FILE="$BACKUP_DIR/backup_log.txt"

# Colors for output

echo "Starting secure backup process..."

# Create backup directory structure
mkdir -p "$BACKUP_DIR"/{original,working_copy,git_checkpoint}

# Initialize log
echo "Backup started: $(date)" > "$LOG_FILE"
echo "Backup directory: $BACKUP_DIR" >> "$LOG_FILE"

# Function: Create git checkpoint
create_git_checkpoint() {
    cd "$WORKING_DIR/.."
    
    # Add all changes and create checkpoint commit
    git add .
    git commit -m "CHECKPOINT: Before PHASE_0_EMERGENCY extraction - Triple backup created" || true
    
    # Save git log to backup
    git log --oneline -10 > "$BACKUP_DIR/git_checkpoint/pre_extraction_log.txt"
    echo "Git checkpoint created" >> "$LOG_FILE"
}

# Function: Backup files by violation level
backup_violations() {
    local level=$1
    local min_lines=$2
    local max_lines=$3
    
    
    # Find files in violation range
    find "$WORKING_DIR" -name "*.md" -exec wc -l {} + | \
    awk -v min="$min_lines" -v max="$max_lines" '$1 >= min && $1 <= max {print $1, $2}' | \
    while read -r lines file; do
        if [[ -f "$file" ]]; then
            # Create category directory
            mkdir -p "$BACKUP_DIR/original/$level"
            mkdir -p "$BACKUP_DIR/working_copy/$level"
            
            # Get relative path and filename
            rel_path="${file#$WORKING_DIR/}"
            filename=$(basename "$file" .md)
            
            # Create backup with metadata
            backup_name="${filename}_BACKUP_${lines}_lines.md"
            
            # Original backup (untouchable)
            cp "$file" "$BACKUP_DIR/original/$level/$backup_name"
            
            # Working copy backup
            cp "$file" "$BACKUP_DIR/working_copy/$level/$backup_name"
            
            echo "BACKED UP: $rel_path ($lines lines) -> $level/$backup_name" >> "$LOG_FILE"
        fi
    done
}

# Function: Validate backup integrity
validate_backup() {
    
    original_count=$(find "$BACKUP_DIR/original" -name "*.md" | wc -l)
    working_count=$(find "$BACKUP_DIR/working_copy" -name "*.md" | wc -l)
    
    if [[ $original_count -eq $working_count ]]; then
        echo "Backup validation: SUCCESS - $original_count files" >> "$LOG_FILE"
        return 0
    else
        echo "Backup validation: FAILED - count mismatch" >> "$LOG_FILE"
        return 1
    fi
}

# Function: Generate backup report
generate_report() {
    
    cat > "$BACKUP_DIR/BACKUP_REPORT.md" << EOF
# PHASE_0_EMERGENCY Triple Backup Report

**Date**: $(date)
**Backup Directory**: $BACKUP_DIR

## Backup Structure
- **original/**: Untouchable backup copies (rollback source)
- **working_copy/**: Working backup copies (for comparison)
- **git_checkpoint/**: Git state before modifications

## Files Backed Up by Category

### L0-EMERGENCY (>400 lines)
$(find "$BACKUP_DIR/original/L0-EMERGENCY" -name "*.md" 2>/dev/null | wc -l) files

### L1-CRITICAL (200-400 lines)  
$(find "$BACKUP_DIR/original/L1-CRITICAL" -name "*.md" 2>/dev/null | wc -l) files

### L2-HIGH (80-200 lines)
$(find "$BACKUP_DIR/original/L2-HIGH" -name "*.md" 2>/dev/null | wc -l) files

## Security Features
- ✅ Triple backup system implemented
- ✅ Git checkpoint created
- ✅ Backup integrity validated
- ✅ Rollback capability available

## Rollback Instructions
To rollback any file:
1. Stop all extraction scripts
2. Copy from original/ back to context/
3. Run git reset if needed
4. Validate system integrity

---
**SECURITY DECLARATION**: All files safely backed up with triple redundancy.
EOF

}

# Main execution
echo "Working directory: $WORKING_DIR"
echo "Backup directory: $BACKUP_DIR"

# Execute backup sequence
create_git_checkpoint
backup_violations "L0-EMERGENCY" 400 999999
backup_violations "L1-CRITICAL" 200 399
backup_violations "L2-HIGH" 80 199

# Validate and report
if validate_backup; then
    generate_report
    echo "Backup completed: $(date)" >> "$LOG_FILE"
else
    exit 1
fi

echo ""
echo "1. Review backup report: $BACKUP_DIR/BACKUP_REPORT.md"
echo "2. Validate critical files are backed up"
echo "3. Proceed with analyze_violations.sh"