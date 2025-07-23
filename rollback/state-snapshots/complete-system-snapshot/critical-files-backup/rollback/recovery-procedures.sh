#!/bin/bash

# Emergency Recovery Procedures
# Automated emergency recovery and repair system
# Usage: ./recovery-procedures.sh [recovery-type] [options]

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
STATE_DIR="$SCRIPT_DIR/state-snapshots"
LOG_DIR="$SCRIPT_DIR/logs"
RECOVERY_LOG="$LOG_DIR/recovery-$(date +%Y%m%d_%H%M%S).log"

mkdir -p "$LOG_DIR"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

# Logging
exec 1> >(tee -a "$RECOVERY_LOG")
exec 2> >(tee -a "$RECOVERY_LOG" >&2)

log_info() {
    echo -e "${BLUE}[INFO]${NC} $(date '+%H:%M:%S') - $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $(date '+%H:%M:%S') - $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $(date '+%H:%M:%S') - $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $(date '+%H:%M:%S') - $1"
}

log_critical() {
    echo -e "${MAGENTA}[CRITICAL]${NC} $(date '+%H:%M:%S') - $1"
}

log_section() {
    echo -e "${CYAN}[RECOVERY]${NC} $1"
    echo "=================================================="
}

# Emergency assessment
assess_damage() {
    log_section "Emergency Damage Assessment"
    
    cd "$PROJECT_ROOT"
    
    local damage_score=0
    local critical_issues=()
    local major_issues=()
    local minor_issues=()
    
    # Critical system files
    local critical_files=("CLAUDE.md" "README.md" "commands")
    for file in "${critical_files[@]}"; do
        if [[ ! -e "$file" ]]; then
            critical_issues+=("Critical file missing: $file")
            ((damage_score += 20))
        fi
    done
    
    # Git repository health
    if ! git rev-parse --git-dir >/dev/null 2>&1; then
        critical_issues+=("Git repository corrupted or missing")
        ((damage_score += 25))
    elif ! git status >/dev/null 2>&1; then
        major_issues+=("Git repository errors detected")
        ((damage_score += 10))
    fi
    
    # Command system integrity
    local cmd_count=0
    if [[ -d "commands" ]]; then
        cmd_count=$(find commands -name "*.md" -type f 2>/dev/null | wc -l)
    fi
    
    if [[ $cmd_count -eq 0 ]]; then
        critical_issues+=("Command system completely missing")
        ((damage_score += 30))
    elif [[ $cmd_count -lt 10 ]]; then
        major_issues+=("Command system severely reduced: $cmd_count commands")
        ((damage_score += 15))
    elif [[ $cmd_count -lt 20 ]]; then
        minor_issues+=("Command system partially affected: $cmd_count commands")
        ((damage_score += 5))
    fi
    
    # Documentation integrity
    local doc_count=0
    if [[ -d "docs" ]]; then
        doc_count=$(find docs -name "*.md" -type f 2>/dev/null | wc -l)
    fi
    
    if [[ $doc_count -eq 0 ]]; then
        major_issues+=("Documentation system missing")
        ((damage_score += 10))
    elif [[ $doc_count -lt 5 ]]; then
        minor_issues+=("Documentation system reduced: $doc_count files")
        ((damage_score += 3))
    fi
    
    # File system permissions
    local permission_errors=0
    while IFS= read -r file; do
        if [[ -f "$file" && ! -r "$file" ]]; then
            ((permission_errors++))
        fi
    done < <(find . -name "*.md" -o -name "*.sh" | grep -v ".git/" | head -20)
    
    if [[ $permission_errors -gt 0 ]]; then
        minor_issues+=("File permission issues: $permission_errors files")
        ((damage_score += $permission_errors))
    fi
    
    # Rollback system availability
    if [[ ! -d "$STATE_DIR" ]]; then
        major_issues+=("No state snapshots available for rollback")
        ((damage_score += 20))
    else
        local snapshot_count=$(find "$STATE_DIR" -maxdepth 1 -type d | wc -l)
        if [[ $snapshot_count -le 1 ]]; then
            major_issues+=("Limited rollback options available")
            ((damage_score += 10))
        fi
    fi
    
    # Report assessment
    log_info "Damage Assessment Complete"
    log_info "Damage Score: $damage_score/100"
    
    if [[ ${#critical_issues[@]} -gt 0 ]]; then
        log_critical "Critical Issues Detected:"
        printf '%s\n' "${critical_issues[@]}" | sed 's/^/  - /'
    fi
    
    if [[ ${#major_issues[@]} -gt 0 ]]; then
        log_error "Major Issues Detected:"
        printf '%s\n' "${major_issues[@]}" | sed 's/^/  - /'
    fi
    
    if [[ ${#minor_issues[@]} -gt 0 ]]; then
        log_warning "Minor Issues Detected:"
        printf '%s\n' "${minor_issues[@]}" | sed 's/^/  - /'
    fi
    
    # Determine recovery strategy
    if [[ $damage_score -ge 50 ]]; then
        log_critical "SEVERE DAMAGE - Full system recovery required"
        return 3
    elif [[ $damage_score -ge 25 ]]; then
        log_error "MAJOR DAMAGE - Significant recovery required"
        return 2
    elif [[ $damage_score -ge 10 ]]; then
        log_warning "MODERATE DAMAGE - Targeted recovery required"
        return 1
    else
        log_success "MINOR DAMAGE - Simple repairs sufficient"
        return 0
    fi
}

# Emergency rollback to latest known good state
emergency_rollback() {
    log_section "Emergency Rollback Procedure"
    
    # Find latest snapshot
    local latest_snapshot=""
    if [[ -d "$STATE_DIR" ]]; then
        latest_snapshot=$(ls -t "$STATE_DIR" | head -1)
    fi
    
    if [[ -z "$latest_snapshot" ]]; then
        log_critical "No snapshots available for emergency rollback"
        return 1
    fi
    
    log_info "Attempting emergency rollback to: $latest_snapshot"
    
    # Create emergency backup of current state
    local emergency_backup="emergency-$(date +%Y%m%d_%H%M%S)"
    log_info "Creating emergency backup: $emergency_backup"
    
    mkdir -p "$STATE_DIR/$emergency_backup"
    cd "$PROJECT_ROOT"
    
    # Backup what we can
    [[ -f "CLAUDE.md" ]] && cp "CLAUDE.md" "$STATE_DIR/$emergency_backup/" 2>/dev/null || true
    [[ -f "README.md" ]] && cp "README.md" "$STATE_DIR/$emergency_backup/" 2>/dev/null || true
    [[ -d "commands" ]] && cp -r "commands" "$STATE_DIR/$emergency_backup/" 2>/dev/null || true
    [[ -d "docs" ]] && cp -r "docs" "$STATE_DIR/$emergency_backup/" 2>/dev/null || true
    
    git status > "$STATE_DIR/$emergency_backup/git-status.txt" 2>/dev/null || echo "Git not functional" > "$STATE_DIR/$emergency_backup/git-status.txt"
    
    # Execute rollback
    if "$SCRIPT_DIR/rollback-manager.sh" rollback "$latest_snapshot" complete; then
        log_success "Emergency rollback completed successfully"
        return 0
    else
        log_critical "Emergency rollback failed - manual intervention required"
        return 1
    fi
}

# Repair critical system files
repair_critical_files() {
    log_section "Critical File Repair"
    
    cd "$PROJECT_ROOT"
    local repairs_made=0
    
    # Find latest snapshot with critical files
    local source_snapshot=""
    if [[ -d "$STATE_DIR" ]]; then
        for snapshot in $(ls -t "$STATE_DIR"); do
            if [[ -d "$STATE_DIR/$snapshot/critical-files-backup" ]]; then
                source_snapshot="$snapshot"
                break
            fi
        done
    fi
    
    if [[ -z "$source_snapshot" ]]; then
        log_error "No snapshots with critical files backup found"
        return 1
    fi
    
    local backup_dir="$STATE_DIR/$source_snapshot/critical-files-backup"
    log_info "Using backup from snapshot: $source_snapshot"
    
    # Repair CLAUDE.md
    if [[ ! -f "CLAUDE.md" && -f "$backup_dir/CLAUDE.md" ]]; then
        log_info "Restoring CLAUDE.md"
        cp "$backup_dir/CLAUDE.md" "CLAUDE.md"
        ((repairs_made++))
    fi
    
    # Repair README.md
    if [[ ! -f "README.md" && -f "$backup_dir/README.md" ]]; then
        log_info "Restoring README.md"
        cp "$backup_dir/README.md" "README.md"
        ((repairs_made++))
    fi
    
    # Repair commands directory
    if [[ ! -d "commands" && -d "$backup_dir/commands" ]]; then
        log_info "Restoring commands directory"
        cp -r "$backup_dir/commands" "commands"
        ((repairs_made++))
    elif [[ -d "commands" && -d "$backup_dir/commands" ]]; then
        # Check if commands directory is severely damaged
        local current_cmd_count=$(find commands -name "*.md" -type f 2>/dev/null | wc -l)
        local backup_cmd_count=$(find "$backup_dir/commands" -name "*.md" -type f 2>/dev/null | wc -l)
        
        if [[ $current_cmd_count -lt $((backup_cmd_count / 2)) ]]; then
            log_warning "Commands directory severely damaged, restoring from backup"
            rm -rf "commands" 2>/dev/null || true
            cp -r "$backup_dir/commands" "commands"
            ((repairs_made++))
        fi
    fi
    
    # Repair docs directory
    if [[ ! -d "docs" && -d "$backup_dir/docs" ]]; then
        log_info "Restoring docs directory"
        cp -r "$backup_dir/docs" "docs"
        ((repairs_made++))
    fi
    
    log_info "Critical file repairs completed: $repairs_made repairs made"
    return 0
}

# Git repository repair
repair_git_repository() {
    log_section "Git Repository Repair"
    
    cd "$PROJECT_ROOT"
    
    # Check if git directory exists
    if [[ ! -d ".git" ]]; then
        log_warning "Git repository missing - attempting to reinitialize"
        
        # Try to restore from snapshot
        local latest_snapshot=""
        if [[ -d "$STATE_DIR" ]]; then
            latest_snapshot=$(ls -t "$STATE_DIR" | head -1)
        fi
        
        if [[ -n "$latest_snapshot" && -f "$STATE_DIR/$latest_snapshot/git-detailed.txt" ]]; then
            local original_remote=$(grep "Remote URL:" "$STATE_DIR/$latest_snapshot/git-detailed.txt" | cut -d: -f2- | xargs)
            
            if [[ "$original_remote" != "no origin" ]]; then
                log_info "Attempting to clone from original remote: $original_remote"
                if git clone "$original_remote" temp_clone 2>/dev/null; then
                    mv temp_clone/.git .git
                    rm -rf temp_clone
                    log_success "Git repository restored from remote"
                    return 0
                fi
            fi
        fi
        
        # Fallback: initialize new repository
        log_warning "Initializing new git repository"
        git init
        git add .
        git commit -m "Emergency recovery - repository reinitialized"
        return 0
    fi
    
    # Try to repair existing repository
    log_info "Attempting git repository repair"
    
    # Check git fsck
    if git fsck --full 2>/dev/null; then
        log_success "Git repository integrity check passed"
        return 0
    fi
    
    # Try git gc with aggressive cleanup
    log_info "Running git garbage collection"
    if git gc --aggressive --prune=now 2>/dev/null; then
        log_success "Git garbage collection completed"
    else
        log_warning "Git garbage collection failed"
    fi
    
    # Try to fix refs
    log_info "Repairing git references"
    if git update-ref -d HEAD 2>/dev/null && git symbolic-ref HEAD refs/heads/master 2>/dev/null; then
        log_success "Git references repaired"
    fi
    
    # Final check
    if git status >/dev/null 2>&1; then
        log_success "Git repository repair completed"
        return 0
    else
        log_error "Git repository repair failed"
        return 1
    fi
}

# Command system repair
repair_command_system() {
    log_section "Command System Repair"
    
    cd "$PROJECT_ROOT"
    
    # Check current state
    local current_commands=0
    if [[ -d "commands" ]]; then
        current_commands=$(find commands -name "*.md" -type f 2>/dev/null | wc -l)
    fi
    
    log_info "Current command count: $current_commands"
    
    # Find best snapshot for restoration
    local best_snapshot=""
    local max_commands=0
    
    if [[ -d "$STATE_DIR" ]]; then
        for snapshot in $(ls -t "$STATE_DIR"); do
            local metadata_file="$STATE_DIR/$snapshot/metadata.json"
            if [[ -f "$metadata_file" ]]; then
                local cmd_count=$(jq -r '.total_commands // 0' "$metadata_file" 2>/dev/null || echo "0")
                if [[ $cmd_count -gt $max_commands ]]; then
                    max_commands=$cmd_count
                    best_snapshot="$snapshot"
                fi
            fi
        done
    fi
    
    if [[ -z "$best_snapshot" ]]; then
        log_error "No suitable snapshot found for command system repair"
        return 1
    fi
    
    log_info "Best snapshot for restoration: $best_snapshot ($max_commands commands)"
    
    # Selective restoration
    if [[ $current_commands -lt $((max_commands / 2)) ]]; then
        log_info "Command system severely damaged - full restoration required"
        
        local backup_commands="$STATE_DIR/$best_snapshot/critical-files-backup/commands"
        if [[ -d "$backup_commands" ]]; then
            # Backup current commands if any exist
            if [[ -d "commands" && $current_commands -gt 0 ]]; then
                mv "commands" "commands-damaged-$(date +%Y%m%d_%H%M%S)" 2>/dev/null || true
            fi
            
            cp -r "$backup_commands" "commands"
            log_success "Command system restored from snapshot"
            return 0
        fi
    else
        log_info "Command system partially intact - selective repair"
        
        # Repair only missing critical commands
        local core_commands=("start.md" "explore-codebase.md" "capture-learnings.md")
        local backup_commands="$STATE_DIR/$best_snapshot/critical-files-backup/commands"
        
        if [[ -d "$backup_commands" ]]; then
            for core_cmd in "${core_commands[@]}"; do
                if ! find commands -name "$core_cmd" -type f | grep -q .; then
                    local backup_file=$(find "$backup_commands" -name "$core_cmd" -type f | head -1)
                    if [[ -f "$backup_file" ]]; then
                        local target_dir="commands/$(dirname "$(find "$backup_commands" -name "$core_cmd" -type f | head -1 | sed "s|$backup_commands/||")")"
                        mkdir -p "$target_dir"
                        cp "$backup_file" "$target_dir/"
                        log_info "Restored critical command: $core_cmd"
                    fi
                fi
            done
        fi
    fi
    
    log_success "Command system repair completed"
    return 0
}

# System consistency repair
repair_system_consistency() {
    log_section "System Consistency Repair"
    
    cd "$PROJECT_ROOT"
    
    # Fix file permissions
    log_info "Fixing file permissions"
    find . -name "*.md" -type f -exec chmod 644 {} \; 2>/dev/null || true
    find . -name "*.sh" -type f -exec chmod 755 {} \; 2>/dev/null || true
    find . -type d -exec chmod 755 {} \; 2>/dev/null || true
    
    # Fix line endings (ensure Unix style)
    log_info "Standardizing line endings"
    find . -name "*.md" -type f -exec dos2unix {} \; 2>/dev/null || true
    
    # Remove temporary/backup files
    log_info "Cleaning temporary files"
    find . -name "*~" -delete 2>/dev/null || true
    find . -name "*.bak" -delete 2>/dev/null || true
    find . -name ".DS_Store" -delete 2>/dev/null || true
    
    # Verify essential directory structure
    local essential_dirs=("commands" "docs" "docs/core" "docs/standards")
    for dir in "${essential_dirs[@]}"; do
        if [[ ! -d "$dir" ]]; then
            log_info "Creating missing directory: $dir"
            mkdir -p "$dir"
        fi
    done
    
    log_success "System consistency repair completed"
    return 0
}

# Complete system rebuild from snapshots
rebuild_system() {
    log_section "Complete System Rebuild"
    
    # Find the best complete snapshot
    local best_snapshot=""
    local max_score=0
    
    if [[ -d "$STATE_DIR" ]]; then
        for snapshot in $(ls -t "$STATE_DIR"); do
            local metadata_file="$STATE_DIR/$snapshot/metadata.json"
            if [[ -f "$metadata_file" ]]; then
                local total_files=$(jq -r '.total_files // 0' "$metadata_file" 2>/dev/null || echo "0")
                local total_commands=$(jq -r '.total_commands // 0' "$metadata_file" 2>/dev/null || echo "0")
                local score=$((total_files + total_commands * 2))
                
                if [[ $score -gt $max_score ]]; then
                    max_score=$score
                    best_snapshot="$snapshot"
                fi
            fi
        done
    fi
    
    if [[ -z "$best_snapshot" ]]; then
        log_critical "No suitable snapshot found for system rebuild"
        return 1
    fi
    
    log_info "Rebuilding system from snapshot: $best_snapshot (score: $max_score)"
    
    # Create pre-rebuild backup
    local pre_rebuild_backup="pre-rebuild-$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$STATE_DIR/$pre_rebuild_backup"
    cp -r . "$STATE_DIR/$pre_rebuild_backup/" 2>/dev/null || true
    
    # Execute complete rollback
    if "$SCRIPT_DIR/rollback-manager.sh" rollback "$best_snapshot" complete; then
        log_success "System rebuild completed successfully"
        
        # Run post-rebuild repairs
        repair_system_consistency
        
        # Validate rebuilt system
        if "$SCRIPT_DIR/validation-suite.sh" quick; then
            log_success "Rebuilt system validation passed"
            return 0
        else
            log_warning "Rebuilt system validation failed - may need manual attention"
            return 1
        fi
    else
        log_critical "System rebuild failed"
        return 1
    fi
}

# Interactive recovery wizard
recovery_wizard() {
    log_section "Interactive Recovery Wizard"
    
    echo "Emergency Recovery Wizard"
    echo "========================="
    echo
    
    # Assessment
    log_info "Performing damage assessment..."
    assess_damage
    local damage_level=$?
    
    echo
    echo "Recovery Options:"
    echo "1. Emergency rollback (fastest)"
    echo "2. Repair critical files only"
    echo "3. Comprehensive repair"
    echo "4. Complete system rebuild"
    echo "5. Custom recovery (expert mode)"
    echo "6. Exit without recovery"
    echo
    
    read -p "Select recovery option (1-6): " choice
    
    case "$choice" in
        1)
            emergency_rollback
            ;;
        2)
            repair_critical_files
            ;;
        3)
            repair_critical_files
            repair_git_repository
            repair_command_system
            repair_system_consistency
            ;;
        4)
            rebuild_system
            ;;
        5)
            echo "Custom recovery mode - select individual repairs:"
            echo "a. Critical files"
            echo "b. Git repository"
            echo "c. Command system"
            echo "d. System consistency"
            echo "e. All of the above"
            read -p "Select repairs (a,b,c,d,e): " repairs
            
            [[ "$repairs" == *"a"* || "$repairs" == *"e"* ]] && repair_critical_files
            [[ "$repairs" == *"b"* || "$repairs" == *"e"* ]] && repair_git_repository
            [[ "$repairs" == *"c"* || "$repairs" == *"e"* ]] && repair_command_system
            [[ "$repairs" == *"d"* || "$repairs" == *"e"* ]] && repair_system_consistency
            ;;
        6)
            log_info "Recovery cancelled by user"
            exit 0
            ;;
        *)
            log_error "Invalid choice"
            exit 1
            ;;
    esac
    
    # Final validation
    echo
    log_info "Running post-recovery validation..."
    if "$SCRIPT_DIR/validation-suite.sh" quick; then
        log_success "Recovery completed successfully!"
    else
        log_warning "Recovery completed but validation failed - manual inspection recommended"
    fi
}

# Main dispatcher
main() {
    case "${1:-wizard}" in
        "assess"|"assessment")
            assess_damage
            ;;
        "emergency"|"rollback")
            emergency_rollback
            ;;
        "repair-files")
            repair_critical_files
            ;;
        "repair-git")
            repair_git_repository
            ;;
        "repair-commands")
            repair_command_system
            ;;
        "repair-consistency")
            repair_system_consistency
            ;;
        "rebuild")
            rebuild_system
            ;;
        "wizard"|"interactive")
            recovery_wizard
            ;;
        "auto")
            # Automatic recovery based on damage assessment
            assess_damage
            local damage_level=$?
            
            case $damage_level in
                0)
                    log_info "Minor damage detected - running consistency repair"
                    repair_system_consistency
                    ;;
                1)
                    log_info "Moderate damage detected - running comprehensive repair"
                    repair_critical_files && repair_git_repository && repair_command_system && repair_system_consistency
                    ;;
                2)
                    log_info "Major damage detected - attempting system rebuild"
                    rebuild_system
                    ;;
                3)
                    log_info "Severe damage detected - attempting emergency rollback"
                    emergency_rollback || rebuild_system
                    ;;
            esac
            ;;
        "help"|"-h"|"--help")
            cat << 'EOF'
Emergency Recovery Procedures

Usage: ./recovery-procedures.sh [recovery-type] [options]

Recovery Types:
  assess          Perform damage assessment only
  emergency       Emergency rollback to latest snapshot
  repair-files    Repair critical system files
  repair-git      Repair git repository
  repair-commands Repair command system
  repair-consistency System consistency repairs
  rebuild         Complete system rebuild from snapshots
  wizard          Interactive recovery wizard (default)
  auto            Automatic recovery based on damage level

Examples:
  ./recovery-procedures.sh wizard
  ./recovery-procedures.sh auto
  ./recovery-procedures.sh emergency
  ./recovery-procedures.sh assess
EOF
            ;;
        *)
            log_error "Unknown recovery type: $1"
            echo "Use './recovery-procedures.sh help' for usage information"
            exit 1
            ;;
    esac
}

# Execute main function
main "$@"