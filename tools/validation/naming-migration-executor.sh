#!/bin/bash

# Naming Migration Executor
# Executes systematic file renaming per NAMING_MIGRATION_PLAN.md

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
REPO_ROOT="/Users/nalve/ce-simple"
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
BACKUP_DIR="$REPO_ROOT/tools/validation/backups/naming_migration_$TIMESTAMP"
LOG_FILE="$REPO_ROOT/tools/validation/migration_log_$TIMESTAMP.txt"

# Phase selection
PHASE="${1:-interactive}"

echo -e "${BLUE}🔄 NAMING MIGRATION EXECUTOR${NC}"
echo "Backup: $BACKUP_DIR"
echo "Log: $LOG_FILE"
echo "========================================"

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Initialize log
echo "Naming Migration Log - $(date)" > "$LOG_FILE"
echo "Phase: $PHASE" >> "$LOG_FILE"
echo "=======================================" >> "$LOG_FILE"

# Function to log and echo
log_echo() {
    echo -e "$1"
    echo -e "$1" | sed 's/\x1b\[[0-9;]*m//g' >> "$LOG_FILE"
}

# Function to create backup
create_backup() {
    local source_file="$1"
    local backup_file="$BACKUP_DIR/$(basename "$source_file")"
    cp "$source_file" "$backup_file"
    log_echo "📋 Backed up: $(basename "$source_file")"
}

# Function to update references
update_references() {
    local old_ref="$1"
    local new_ref="$2"
    
    log_echo "${YELLOW}🔄 Updating references: $old_ref → $new_ref${NC}"
    
    # Find and update references
    find "$REPO_ROOT/context" -name "*.md" -not -path "*/archive/*" -exec grep -l "$old_ref" {} \; 2>/dev/null | while read -r file; do
        create_backup "$file"
        sed -i "" "s|$old_ref|$new_ref|g" "$file"
        log_echo "  ✅ Updated: $(echo "$file" | sed "s|$REPO_ROOT/||")"
    done
}

# Phase 1: Cleanup temporary files
execute_phase1() {
    log_echo "\n${BLUE}📋 PHASE 1: CLEANUP TEMPORARY FILES${NC}"
    
    # Count files to be deleted
    backup_count=$(find "$REPO_ROOT" -name "*_BACKUP_*lines*" -type f | wc -l)
    validation_dirs=$(find "$REPO_ROOT/scripts" -name "validation_results_*" -type d | wc -l)
    
    if [ $backup_count -gt 0 ] || [ $validation_dirs -gt 5 ]; then
        log_echo "${YELLOW}Found $backup_count backup files and $validation_dirs validation directories${NC}"
        
        if [ "$PHASE" = "interactive" ]; then
            echo -n "Proceed with cleanup? [y/N]: "
            read -r response
            if [[ ! "$response" =~ ^[Yy]$ ]]; then
                log_echo "Phase 1 cancelled by user"
                return
            fi
        fi
        
        # Delete backup files
        if [ $backup_count -gt 0 ]; then
            find "$REPO_ROOT" -name "*_BACKUP_*lines*" -type f -delete
            log_echo "${GREEN}✅ Deleted $backup_count backup files${NC}"
        fi
        
        # Keep only latest 5 validation directories
        if [ $validation_dirs -gt 5 ]; then
            find "$REPO_ROOT/scripts" -name "validation_results_*" -type d | sort | head -n -5 | xargs rm -rf
            log_echo "${GREEN}✅ Cleaned up old validation directories${NC}"
        fi
        
        log_echo "${GREEN}🎉 Phase 1 completed successfully${NC}"
    else
        log_echo "${GREEN}✅ No cleanup needed - system already clean${NC}"
    fi
}

# Phase 2: Spanish to English migration
execute_phase2() {
    log_echo "\n${BLUE}📋 PHASE 2: SPANISH → ENGLISH MIGRATION${NC}"
    
    # Check if target files exist
    OLD_DIR="$REPO_ROOT/context/vision/simplicidad-system"
    NEW_DIR="$REPO_ROOT/context/vision/simplicity-system"
    OLD_FILE="$OLD_DIR/simplicidad-belleza-consolidated.md"
    NEW_FILE="$NEW_DIR/simplicity-beauty-consolidated.md"
    
    if [ ! -d "$OLD_DIR" ] && [ ! -f "$OLD_FILE" ]; then
        log_echo "${GREEN}✅ Spanish files already migrated or not found${NC}"
        return
    fi
    
    if [ "$PHASE" = "interactive" ]; then
        echo -n "Proceed with Spanish → English migration? [y/N]: "
        read -r response
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            log_echo "Phase 2 cancelled by user"
            return
        fi
    fi
    
    # Step 1: Rename directory if it exists
    if [ -d "$OLD_DIR" ]; then
        log_echo "${YELLOW}🔄 Renaming directory: simplicidad-system → simplicity-system${NC}"
        
        # Create new directory
        mkdir -p "$NEW_DIR"
        
        # Move all files
        if [ "$(ls -A "$OLD_DIR")" ]; then
            mv "$OLD_DIR"/* "$NEW_DIR"/
        fi
        
        # Remove old directory
        rmdir "$OLD_DIR"
        
        # Update directory references
        update_references "simplicidad-system" "simplicity-system"
        
        log_echo "${GREEN}✅ Directory renamed successfully${NC}"
    fi
    
    # Step 2: Rename specific file if it exists
    if [ -f "$NEW_DIR/simplicidad-belleza-consolidated.md" ]; then
        log_echo "${YELLOW}🔄 Renaming file: simplicidad-belleza-consolidated.md → simplicity-beauty-consolidated.md${NC}"
        
        # Create backup
        create_backup "$NEW_DIR/simplicidad-belleza-consolidated.md"
        
        # Rename file
        mv "$NEW_DIR/simplicidad-belleza-consolidated.md" "$NEW_FILE"
        
        # Update file references
        update_references "simplicidad-belleza-consolidated.md" "simplicity-beauty-consolidated.md"
        
        log_echo "${GREEN}✅ File renamed successfully${NC}"
    fi
    
    log_echo "${GREEN}🎉 Phase 2 completed successfully${NC}"
}

# Validation function
validate_migration() {
    log_echo "\n${BLUE}📋 VALIDATION${NC}"
    
    # Check for remaining Spanish names
    spanish_files=$(find "$REPO_ROOT/context" -name "*.md" -not -path "*/archive/*" | xargs grep -l -E "(metodologia|flujos|simplicidad)" 2>/dev/null | wc -l)
    
    if [ $spanish_files -eq 0 ]; then
        log_echo "${GREEN}✅ No Spanish names detected in active files${NC}"
    else
        log_echo "${RED}❌ $spanish_files files still contain Spanish names${NC}"
    fi
    
    # Check system functionality (basic test)
    if [ -f "$REPO_ROOT/CLAUDE.md" ] && [ -d "$REPO_ROOT/context" ]; then
        log_echo "${GREEN}✅ Core system files accessible${NC}"
    else
        log_echo "${RED}❌ Core system files missing${NC}"
    fi
}

# Main execution logic
case "$PHASE" in
    "1" | "phase1" | "cleanup")
        execute_phase1
        ;;
    "2" | "phase2" | "spanish")
        execute_phase2
        validate_migration
        ;;
    "all")
        execute_phase1
        execute_phase2
        validate_migration
        ;;
    "interactive")
        echo -e "${YELLOW}Select migration phase:${NC}"
        echo "1) Phase 1: Cleanup temporary files"
        echo "2) Phase 2: Spanish → English migration"
        echo "3) All phases"
        echo "4) Exit"
        echo -n "Choice [1-4]: "
        
        read -r choice
        case "$choice" in
            1) execute_phase1 ;;
            2) execute_phase2; validate_migration ;;
            3) execute_phase1; execute_phase2; validate_migration ;;
            4) log_echo "Migration cancelled"; exit 0 ;;
            *) log_echo "Invalid choice"; exit 1 ;;
        esac
        ;;
    *)
        echo "Usage: $0 [1|2|all|interactive]"
        echo "  1/phase1/cleanup: Execute Phase 1 (cleanup)"
        echo "  2/phase2/spanish: Execute Phase 2 (Spanish→English)"
        echo "  all: Execute all phases"
        echo "  interactive: Interactive mode (default)"
        exit 1
        ;;
esac

log_echo "\n${GREEN}🏁 Migration execution completed${NC}"
log_echo "Full log available at: $LOG_FILE"
log_echo "Backup available at: $BACKUP_DIR"