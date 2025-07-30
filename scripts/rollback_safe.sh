#!/bin/bash
# rollback_safe.sh - Emergency rollback system for PHASE_0_EMERGENCY
# 30/07/2025 CDMX | Safe system recovery with integrity validation

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${RED}EMERGENCY ROLLBACK SYSTEM${NC}"
echo "Safe system recovery for PHASE_0_EMERGENCY"

# Function: Show usage
show_usage() {
    cat << EOF
Usage: $0 [OPTIONS] BACKUP_DIR

Options:
  -f, --full          Full system rollback (all files)
  -s, --selective     Selective rollback (specify files)
  -c, --check         Check rollback availability only
  -g, --git           Include git reset to checkpoint
  -v, --verify        Verify integrity after rollback
  -h, --help          Show this help message

Examples:
  $0 -c /path/to/backup_dir                    # Check rollback availability
  $0 -f /path/to/backup_dir                    # Full system rollback
  $0 -s /path/to/backup_dir file1.md file2.md # Selective rollback
  $0 -fgv /path/to/backup_dir                 # Full rollback + git reset + verify

EMERGENCY: If system is corrupted, run with -fgv for complete recovery.
EOF
}

# Function: Validate backup directory
validate_backup_dir() {
    local backup_dir="$1"
    
    if [[ ! -d "$backup_dir" ]]; then
        echo -e "${RED}❌ ERROR: Backup directory not found: $backup_dir${NC}"
        return 1
    fi
    
    if [[ ! -d "$backup_dir/original" ]]; then
        echo -e "${RED}❌ ERROR: Original backup directory not found: $backup_dir/original${NC}"
        return 1
    fi
    
    if [[ ! -f "$backup_dir/BACKUP_REPORT.md" ]]; then
        echo -e "${YELLOW}⚠️  WARNING: Backup report not found, proceeding with caution${NC}"
    fi
    
    echo -e "${GREEN}✅ Backup directory validated${NC}"
    return 0
}

# Function: Check rollback availability
check_rollback_availability() {
    local backup_dir="$1"
    
    echo -e "${YELLOW}Checking rollback availability...${NC}"
    
    # Count available backups by category
    local l0_count=$(find "$backup_dir/original/L0-EMERGENCY" -name "*.md" 2>/dev/null | wc -l || echo "0")
    local l1_count=$(find "$backup_dir/original/L1-CRITICAL" -name "*.md" 2>/dev/null | wc -l || echo "0")  
    local l2_count=$(find "$backup_dir/original/L2-HIGH" -name "*.md" 2>/dev/null | wc -l || echo "0")
    local total_count=$((l0_count + l1_count + l2_count))
    
    echo -e "${BLUE}ROLLBACK AVAILABILITY:${NC}"
    echo -e "  L0-EMERGENCY: $l0_count files"
    echo -e "  L1-CRITICAL: $l1_count files"
    echo -e "  L2-HIGH: $l2_count files"
    echo -e "  ${GREEN}TOTAL: $total_count files available for rollback${NC}"
    
    # Check git checkpoint
    if [[ -f "$backup_dir/git_checkpoint/pre_extraction_log.txt" ]]; then
        echo -e "${GREEN}✅ Git checkpoint available${NC}"
    else
        echo -e "${YELLOW}⚠️  Git checkpoint not found${NC}"
    fi
    
    return 0
}

# Function: Perform selective rollback
selective_rollback() {
    local backup_dir="$1"
    shift
    local files_to_rollback=("$@")
    
    echo -e "${YELLOW}Performing selective rollback for ${#files_to_rollback[@]} files...${NC}"
    
    local context_dir="/Users/nalve/ce-simple/context"
    local success_count=0
    local fail_count=0
    
    for target_file in "${files_to_rollback[@]}"; do
        # Find the backup file
        local backup_file=$(find "$backup_dir/original" -name "*${target_file%.*}*" -type f | head -1)
        
        if [[ -f "$backup_file" ]]; then
            # Determine target location in context
            local target_path="$context_dir/$target_file"
            
            # Create directory if needed
            mkdir -p "$(dirname "$target_path")"
            
            # Restore file
            cp "$backup_file" "$target_path"
            
            echo -e "${GREEN}✅ Restored: $target_file${NC}"
            success_count=$((success_count + 1))
        else
            echo -e "${RED}❌ Backup not found for: $target_file${NC}"
            fail_count=$((fail_count + 1))
        fi
    done
    
    echo -e "${BLUE}Selective rollback completed: $success_count restored, $fail_count failed${NC}"
    return $fail_count
}

# Function: Perform full rollback
full_rollback() {
    local backup_dir="$1"
    
    echo -e "${YELLOW}Performing FULL SYSTEM ROLLBACK...${NC}"
    echo -e "${RED}⚠️  This will overwrite ALL extracted files with original backups${NC}"
    
    read -p "Are you sure you want to proceed? (yes/no): " confirm
    if [[ "$confirm" != "yes" ]]; then
        echo "Rollback cancelled."
        return 1
    fi
    
    local context_dir="/Users/nalve/ce-simple/context"
    local success_count=0
    local fail_count=0
    
    # Rollback all categories
    for category in "L0-EMERGENCY" "L1-CRITICAL" "L2-HIGH"; do
        echo -e "${YELLOW}Rolling back $category files...${NC}"
        
        find "$backup_dir/original/$category" -name "*.md" 2>/dev/null | while read -r backup_file; do
            if [[ -f "$backup_file" ]]; then
                # Extract original filename from backup name
                local backup_filename=$(basename "$backup_file")
                local original_name=$(echo "$backup_filename" | sed 's/_BACKUP_[0-9]*_lines\.md$/.md/')
                
                # Find target location (search for file in context)
                local target_file=$(find "$context_dir" -name "$original_name" -type f | head -1)
                
                if [[ -f "$target_file" ]]; then
                    cp "$backup_file" "$target_file"
                    echo -e "  ${GREEN}✅${NC} Restored: $original_name"
                    success_count=$((success_count + 1))
                else
                    # Create at expected location if not found
                    local expected_path="$context_dir/$original_name"
                    mkdir -p "$(dirname "$expected_path")"
                    cp "$backup_file" "$expected_path"
                    echo -e "  ${YELLOW}⚠️${NC}  Created: $original_name (file was missing)"
                    success_count=$((success_count + 1))
                fi
            fi
        done
    done
    
    echo -e "${GREEN}Full rollback completed: $success_count files restored${NC}"
    return 0
}

# Function: Perform git reset
git_reset() {
    local backup_dir="$1"
    
    if [[ ! -f "$backup_dir/git_checkpoint/pre_extraction_log.txt" ]]; then
        echo -e "${YELLOW}⚠️  Git checkpoint not available, skipping git reset${NC}"
        return 0
    fi
    
    echo -e "${YELLOW}Performing git reset to checkpoint...${NC}"
    
    cd "/Users/nalve/ce-simple"
    
    # Show current status
    echo -e "${BLUE}Current git status:${NC}"
    git status --short
    
    read -p "Reset git to pre-extraction state? (yes/no): " confirm
    if [[ "$confirm" == "yes" ]]; then
        # Reset to the checkpoint commit
        local checkpoint_commit=$(git log --oneline --grep="CHECKPOINT: Before PHASE_0_EMERGENCY" -1 --format="%H")
        
        if [[ -n "$checkpoint_commit" ]]; then
            git reset --hard "$checkpoint_commit"
            echo -e "${GREEN}✅ Git reset to checkpoint: $checkpoint_commit${NC}"
        else
            echo -e "${RED}❌ Checkpoint commit not found${NC}"
            return 1
        fi
    else
        echo "Git reset skipped."
    fi
    
    return 0
}

# Function: Verify system after rollback
verify_after_rollback() {
    echo -e "${YELLOW}Verifying system integrity after rollback...${NC}"
    
    local script_dir="$(dirname "$0")"
    
    if [[ -f "$script_dir/validate_integrity.sh" ]]; then
        echo -e "${BLUE}Running integrity validation...${NC}"
        bash "$script_dir/validate_integrity.sh"
        local validation_result=$?
        
        if [[ $validation_result -eq 0 ]]; then
            echo -e "${GREEN}✅ System integrity verified after rollback${NC}"
        else
            echo -e "${RED}❌ System integrity issues detected after rollback${NC}"
        fi
        
        return $validation_result
    else
        echo -e "${YELLOW}⚠️  Validation script not found, skipping verification${NC}"
        return 0
    fi
}

# Parse command line arguments
FULL_ROLLBACK=false
SELECTIVE_ROLLBACK=false
CHECK_ONLY=false
GIT_RESET=false
VERIFY=false
BACKUP_DIR=""
SELECTIVE_FILES=()

while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--full)
            FULL_ROLLBACK=true
            shift
            ;;
        -s|--selective)
            SELECTIVE_ROLLBACK=true
            shift
            ;;
        -c|--check)
            CHECK_ONLY=true
            shift
            ;;
        -g|--git)
            GIT_RESET=true
            shift
            ;;
        -v|--verify)
            VERIFY=true
            shift
            ;;
        -h|--help)
            show_usage
            exit 0
            ;;
        -*)
            echo "Unknown option: $1"
            show_usage
            exit 1
            ;;
        *)
            if [[ -z "$BACKUP_DIR" ]]; then
                BACKUP_DIR="$1"
            else
                SELECTIVE_FILES+=("$1")
            fi
            shift
            ;;
    esac
done

# Validate arguments
if [[ -z "$BACKUP_DIR" ]]; then
    echo -e "${RED}ERROR: Backup directory required${NC}"
    show_usage
    exit 1
fi

# Validate backup directory
if ! validate_backup_dir "$BACKUP_DIR"; then
    exit 1
fi

# Execute requested operation
if [[ "$CHECK_ONLY" == true ]]; then
    check_rollback_availability "$BACKUP_DIR"
    exit 0
fi

if [[ "$SELECTIVE_ROLLBACK" == true ]]; then
    if [[ ${#SELECTIVE_FILES[@]} -eq 0 ]]; then
        echo -e "${RED}ERROR: No files specified for selective rollback${NC}"
        exit 1
    fi
    selective_rollback "$BACKUP_DIR" "${SELECTIVE_FILES[@]}"
elif [[ "$FULL_ROLLBACK" == true ]]; then
    full_rollback "$BACKUP_DIR"
else
    echo -e "${RED}ERROR: Must specify either --full or --selective${NC}"
    show_usage
    exit 1
fi

# Optional git reset
if [[ "$GIT_RESET" == true ]]; then
    git_reset "$BACKUP_DIR"
fi

# Optional verification
if [[ "$VERIFY" == true ]]; then
    verify_after_rollback
fi

echo -e "${GREEN}🎉 ROLLBACK OPERATION COMPLETED${NC}"
echo -e "${BLUE}Backup directory: $BACKUP_DIR${NC}"
echo -e "${YELLOW}Remember to run validate_integrity.sh to confirm system health${NC}"