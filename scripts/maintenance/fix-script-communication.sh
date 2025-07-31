#!/bin/bash
# fix-script-communication.sh - Automated correction of script communication protocol violations
# 31/07/2025 CDMX | Systematic correction of 305 communication violations

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
SCRIPTS_DIR="$PROJECT_ROOT/scripts"
BACKUP_DIR="$PROJECT_ROOT/scripts/communication_fix_backup_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$BACKUP_DIR/transformation_log.txt"

# Silent script - no user notifications (Claude Code communicates results)

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Initialize log
{
    echo "$(date)"
    echo "$PROJECT_ROOT"
    echo "communication_fix_start"
} > "$LOG_FILE"

# Backup function
backup_script() {
    local script_path="$1"
    local script_name=$(basename "$script_path")
    cp "$script_path" "$BACKUP_DIR/$script_name.backup"
    echo "backup|$script_path|$BACKUP_DIR/$script_name.backup" >> "$LOG_FILE"
}

# Pattern detection and transformation functions
remove_color_codes() {
    local file="$1"
    # Remove ANSI color variable definitions
    sed -i.tmp '/^RED=.*033/d; /^GREEN=.*033/d; /^YELLOW=.*033/d; /^BLUE=.*033/d; /^PURPLE=.*033/d; /^CYAN=.*033/d; /^NC=.*033/d' "$file"
    # Remove echo statements with color codes
    sed -i.tmp '/echo.*-e.*\${.*}.*NC}/d' "$file"
    rm -f "$file.tmp"
}

convert_descriptive_messages() {
    local file="$1"
    # Convert common descriptive echo patterns to comments or remove them
    sed -i.tmp '
        /echo.*"Purpose:/d
        /echo.*"Target:/d
        /echo.*"Processing:/d
        /echo.*"Files processed:/d
        /echo.*"Classification Summary:/d
        /echo.*"Results:/d
        /echo.*"Success/d
        /echo.*"Complete/d
        /echo.*"Started/d
        /echo.*"Finished/d
    ' "$file"
    rm -f "$file.tmp"
}

remove_visual_separators() {
    local file="$1" 
    # Remove visual separator lines
    sed -i.tmp '
        /echo.*"===\+"/d
        /echo.*"---\+"/d
        /echo.*"___\+"/d
        /echo.*"||||"/d
    ' "$file"
    rm -f "$file.tmp"
}

remove_emoji_messages() {
    local file="$1"
    # Remove echo statements with emojis
    sed -i.tmp '/echo.*[🔍📈✅❌🎯🔄📋🛠⚡📁📄🤖]/d' "$file"
    rm -f "$file.tmp"
}

convert_progress_messages() {
    local file="$1"
    # Convert progress messages to technical logging
    sed -i.tmp '
        s/echo "Processing.*/# Processing start/g
        s/echo "Analyzing.*/# Analysis phase/g  
        s/echo "Generating.*/# Generation phase/g
        s/echo "Validating.*/# Validation phase/g
        s/echo "Done"/# Processing complete/g
    ' "$file"
    rm -f "$file.tmp"
}

convert_summary_sections() {
    local file="$1"
    # Replace summary echo blocks with technical data output
    sed -i.tmp '
        /# Summary/,/^[[:space:]]*$/{
            /echo.*Summary/d
            /echo.*"[A-Za-z]/d
        }
    ' "$file"
    rm -f "$file.tmp"
}

add_silent_header() {
    local file="$1"
    # Add silent script comment if not present
    if ! grep -q "Silent script" "$file"; then
        # Find the line after the shebang and initial comments
        local insert_line=$(grep -n "^set -euo pipefail" "$file" | cut -d: -f1)
        if [[ -n "$insert_line" ]]; then
            sed -i.tmp "${insert_line}a\\
\\
# Silent script - no user notifications (Claude Code communicates results)" "$file"
            rm -f "$file.tmp"
        fi
    fi
}

validate_syntax() {
    local file="$1"
    if bash -n "$file" 2>/dev/null; then
        echo "syntax_valid|$file" >> "$LOG_FILE"
        return 0
    else
        echo "syntax_error|$file" >> "$LOG_FILE"
        return 1
    fi
}

transform_script() {
    local script_path="$1"
    local script_name=$(basename "$script_path")
    
    # Skip if already processed or not a shell script
    if [[ ! "$script_name" =~ \.sh$ ]] || [[ "$script_name" == "fix-script-communication.sh" ]] || [[ "$script_name" == "validate-script-communication.sh" ]]; then
        return 0
    fi
    
    echo "transform_start|$script_path" >> "$LOG_FILE"
    
    # Backup original
    backup_script "$script_path"
    
    # Apply transformations in order
    remove_color_codes "$script_path"
    convert_descriptive_messages "$script_path"
    remove_visual_separators "$script_path"
    remove_emoji_messages "$script_path"
    convert_progress_messages "$script_path"
    convert_summary_sections "$script_path"
    add_silent_header "$script_path"
    
    # Validate syntax
    if validate_syntax "$script_path"; then
        echo "transform_success|$script_path" >> "$LOG_FILE"
        return 0
    else
        # Rollback on syntax error
        cp "$BACKUP_DIR/$script_name.backup" "$script_path"
        echo "transform_rollback|$script_path" >> "$LOG_FILE"
        return 1
    fi
}

# Process critical scripts first
CRITICAL_SCRIPTS=(
    "domain-classifier.sh"
    "batch-l2-modular.sh" 
    "validate_integrity.sh"
    "authority-validator.sh"
    "enhanced_analyze_violations.sh"
)

# Transform critical scripts
critical_processed=0
critical_success=0

for script_name in "${CRITICAL_SCRIPTS[@]}"; do
    script_path="$SCRIPTS_DIR/$script_name"
    if [[ -f "$script_path" ]]; then
        if transform_script "$script_path"; then
            ((critical_success++))
        fi
        ((critical_processed++))
    fi
done

# Process all other scripts
other_processed=0
other_success=0

while IFS= read -r -d '' script_path; do
    script_name=$(basename "$script_path")
    
    # Skip critical scripts (already processed)
    skip=false
    for critical in "${CRITICAL_SCRIPTS[@]}"; do
        if [[ "$script_name" == "$critical" ]]; then
            skip=true
            break
        fi
    done
    
    if [[ "$skip" == false ]]; then
        if transform_script "$script_path"; then
            ((other_success++))
        fi
        ((other_processed++))
    fi
done < <(find "$SCRIPTS_DIR" -name "*.sh" -type f -print0)

# Generate final summary (technical data only)
{
    echo "$(date)"
    echo "critical_processed|$critical_processed|$critical_success"
    echo "other_processed|$other_processed|$other_success"
    echo "total_processed|$((critical_processed + other_processed))|$((critical_success + other_success))"
    echo "backup_dir|$BACKUP_DIR"
} >> "$LOG_FILE"

# Output final results for Claude Code to interpret
echo "$((critical_processed + other_processed))|$((critical_success + other_success))|$BACKUP_DIR|$(date)"