#!/bin/bash

# Migration Rollback Manager
# Comprehensive rollback orchestration system for ce-simple migration
# Usage: ./rollback-manager.sh [command] [options]

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ROLLBACK_DIR="$SCRIPT_DIR"
STATE_DIR="$ROLLBACK_DIR/state-snapshots"
BACKUP_DIR="$ROLLBACK_DIR/backups"
LOG_DIR="$ROLLBACK_DIR/logs"
CONFIG_FILE="$ROLLBACK_DIR/rollback-config.json"

# Create directories
mkdir -p "$STATE_DIR" "$BACKUP_DIR" "$LOG_DIR"

# Logging
LOG_FILE="$LOG_DIR/rollback-$(date +%Y%m%d_%H%M%S).log"
exec 1> >(tee -a "$LOG_FILE")
exec 2> >(tee -a "$LOG_FILE" >&2)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Utility functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Initialize rollback system
initialize_rollback() {
    log_info "Initializing rollback system..."
    
    # Create configuration file
    cat > "$CONFIG_FILE" << 'EOF'
{
  "rollback_version": "1.0.0",
  "created": "$(date -Iseconds)",
  "project_root": "$(pwd)",
  "critical_files": [
    "CLAUDE.md",
    "README.md",
    ".gitignore",
    ".session-info",
    "commands/",
    "docs/core/",
    "docs/standards/"
  ],
  "validation_thresholds": {
    "critical_errors": 0,
    "high_errors": 2,
    "medium_errors": 5,
    "performance_degradation_percent": 20
  },
  "backup_retention_days": 30,
  "auto_rollback_enabled": true
}
EOF
    
    # Initialize git hooks for monitoring
    setup_git_hooks
    
    # Create initial state capture
    capture_current_state "initial"
    
    log_success "Rollback system initialized successfully"
}

# Capture current system state
capture_current_state() {
    local snapshot_name="${1:-$(date +%Y%m%d_%H%M%S)}"
    local snapshot_dir="$STATE_DIR/$snapshot_name"
    
    log_info "Capturing system state: $snapshot_name"
    mkdir -p "$snapshot_dir"
    
    # File inventory with checksums
    log_info "Creating file inventory..."
    find "$PROJECT_ROOT" -type f -name "*.md" -o -name "*.sh" -o -name "*.json" | \
        grep -v ".git/" | \
        sort > "$snapshot_dir/file-list.txt"
    
    # Generate checksums
    log_info "Computing file checksums..."
    while IFS= read -r file; do
        if [[ -f "$file" ]]; then
            echo "$(sha256sum "$file" 2>/dev/null || echo "ERROR: $file")"
        fi
    done < "$snapshot_dir/file-list.txt" > "$snapshot_dir/checksums.txt"
    
    # Git state
    log_info "Capturing git state..."
    cd "$PROJECT_ROOT"
    git status --porcelain > "$snapshot_dir/git-status.txt" 2>/dev/null || echo "No git repository" > "$snapshot_dir/git-status.txt"
    git log --oneline -10 > "$snapshot_dir/git-history.txt" 2>/dev/null || echo "No git history" > "$snapshot_dir/git-history.txt"
    git branch -a > "$snapshot_dir/git-branches.txt" 2>/dev/null || echo "No git branches" > "$snapshot_dir/git-branches.txt"
    
    # Directory structure
    log_info "Mapping directory structure..."
    tree "$PROJECT_ROOT" -a -I ".git" > "$snapshot_dir/directory-tree.txt" 2>/dev/null || \
        find "$PROJECT_ROOT" -type d | grep -v ".git" | sort > "$snapshot_dir/directory-tree.txt"
    
    # Critical files backup
    log_info "Backing up critical files..."
    local critical_backup="$snapshot_dir/critical-files"
    mkdir -p "$critical_backup"
    
    # Backup critical files
    [[ -f "$PROJECT_ROOT/CLAUDE.md" ]] && cp "$PROJECT_ROOT/CLAUDE.md" "$critical_backup/"
    [[ -f "$PROJECT_ROOT/README.md" ]] && cp "$PROJECT_ROOT/README.md" "$critical_backup/"
    [[ -f "$PROJECT_ROOT/.gitignore" ]] && cp "$PROJECT_ROOT/.gitignore" "$critical_backup/"
    [[ -f "$PROJECT_ROOT/.session-info" ]] && cp "$PROJECT_ROOT/.session-info" "$critical_backup/"
    
    # Backup command directory
    if [[ -d "$PROJECT_ROOT/commands" ]]; then
        cp -r "$PROJECT_ROOT/commands" "$critical_backup/"
    fi
    
    # System metadata
    cat > "$snapshot_dir/metadata.json" << EOF
{
  "snapshot_name": "$snapshot_name",
  "timestamp": "$(date -Iseconds)",
  "total_files": $(wc -l < "$snapshot_dir/file-list.txt"),
  "git_commit": "$(cd "$PROJECT_ROOT" && git rev-parse HEAD 2>/dev/null || echo 'no-git')",
  "project_root": "$PROJECT_ROOT",
  "rollback_version": "1.0.0"
}
EOF
    
    log_success "State captured successfully: $snapshot_name"
    echo "$snapshot_dir"
}

# Validate system integrity
validate_system() {
    local reference_snapshot="${1:-}"
    local validation_report="$LOG_DIR/validation-$(date +%Y%m%d_%H%M%S).json"
    
    log_info "Starting system validation..."
    
    local errors=0
    local warnings=0
    local validation_results=()
    
    # Check critical files exist
    log_info "Validating critical files..."
    local critical_files=("CLAUDE.md" "README.md" "commands" "docs/core" "docs/standards")
    
    for file in "${critical_files[@]}"; do
        if [[ ! -e "$PROJECT_ROOT/$file" ]]; then
            log_error "Critical file missing: $file"
            validation_results+=("CRITICAL: Missing critical file: $file")
            ((errors++))
        else
            validation_results+=("OK: Critical file exists: $file")
        fi
    done
    
    # Validate git repository
    log_info "Validating git repository..."
    cd "$PROJECT_ROOT"
    if git status >/dev/null 2>&1; then
        validation_results+=("OK: Git repository is functional")
    else
        log_error "Git repository is corrupted or missing"
        validation_results+=("CRITICAL: Git repository corruption detected")
        ((errors++))
    fi
    
    # Check file integrity if reference snapshot provided
    if [[ -n "$reference_snapshot" && -f "$STATE_DIR/$reference_snapshot/checksums.txt" ]]; then
        log_info "Comparing file integrity against reference snapshot..."
        
        while IFS= read -r line; do
            if [[ "$line" =~ ^([a-f0-9]+)\ \ (.+)$ ]]; then
                local expected_hash="${BASH_REMATCH[1]}"
                local file_path="${BASH_REMATCH[2]}"
                
                if [[ -f "$file_path" ]]; then
                    local current_hash=$(sha256sum "$file_path" | cut -d' ' -f1)
                    if [[ "$current_hash" != "$expected_hash" ]]; then
                        log_warning "File modified: $file_path"
                        validation_results+=("WARNING: File changed since snapshot: $file_path")
                        ((warnings++))
                    fi
                else
                    log_warning "File removed: $file_path"
                    validation_results+=("WARNING: File removed since snapshot: $file_path")
                    ((warnings++))
                fi
            fi
        done < "$STATE_DIR/$reference_snapshot/checksums.txt"
    fi
    
    # Test command system functionality
    log_info "Testing command system functionality..."
    if [[ -d "$PROJECT_ROOT/commands" ]]; then
        local command_count=$(find "$PROJECT_ROOT/commands" -name "*.md" -type f | wc -l)
        if [[ $command_count -gt 0 ]]; then
            validation_results+=("OK: Command system has $command_count commands")
        else
            log_error "No commands found in command system"
            validation_results+=("CRITICAL: Command system appears empty")
            ((errors++))
        fi
    else
        log_error "Commands directory missing"
        validation_results+=("CRITICAL: Commands directory not found")
        ((errors++))
    fi
    
    # Create validation report
    cat > "$validation_report" << EOF
{
  "timestamp": "$(date -Iseconds)",
  "reference_snapshot": "$reference_snapshot",
  "total_errors": $errors,
  "total_warnings": $warnings,
  "status": "$([ $errors -eq 0 ] && echo "PASS" || echo "FAIL")",
  "results": [
    $(printf '"%s"' "${validation_results[@]}" | paste -sd ',' -)
  ]
}
EOF
    
    if [[ $errors -eq 0 ]]; then
        log_success "System validation passed ($warnings warnings)"
        return 0
    else
        log_error "System validation failed ($errors errors, $warnings warnings)"
        return 1
    fi
}

# Execute rollback to specific snapshot
execute_rollback() {
    local snapshot_name="$1"
    local rollback_scope="${2:-complete}"  # complete, incremental, selective
    
    log_info "Starting rollback to snapshot: $snapshot_name (scope: $rollback_scope)"
    
    local snapshot_dir="$STATE_DIR/$snapshot_name"
    if [[ ! -d "$snapshot_dir" ]]; then
        log_error "Snapshot not found: $snapshot_name"
        return 1
    fi
    
    # Create pre-rollback snapshot
    local pre_rollback_snapshot="pre-rollback-$(date +%Y%m%d_%H%M%S)"
    capture_current_state "$pre_rollback_snapshot"
    
    cd "$PROJECT_ROOT"
    
    case "$rollback_scope" in
        "complete")
            execute_complete_rollback "$snapshot_dir"
            ;;
        "incremental")
            execute_incremental_rollback "$snapshot_dir"
            ;;
        "selective")
            execute_selective_rollback "$snapshot_dir" "${3:-}"
            ;;
        *)
            log_error "Unknown rollback scope: $rollback_scope"
            return 1
            ;;
    esac
    
    # Validate rollback success
    if validate_system "$snapshot_name"; then
        log_success "Rollback completed successfully"
        return 0
    else
        log_error "Rollback validation failed - system may be in inconsistent state"
        return 1
    fi
}

# Complete system rollback
execute_complete_rollback() {
    local snapshot_dir="$1"
    
    log_info "Executing complete rollback..."
    
    # Restore critical files
    if [[ -d "$snapshot_dir/critical-files" ]]; then
        log_info "Restoring critical files..."
        cp -r "$snapshot_dir/critical-files"/* "$PROJECT_ROOT/" 2>/dev/null || true
    fi
    
    # Reset git state if applicable
    if [[ -f "$snapshot_dir/git-status.txt" ]] && grep -q "^[AMD]" "$snapshot_dir/git-status.txt"; then
        log_info "Resetting git state..."
        git reset --hard HEAD 2>/dev/null || true
        git clean -fd 2>/dev/null || true
    fi
    
    log_success "Complete rollback executed"
}

# Incremental rollback (restore specific files)
execute_incremental_rollback() {
    local snapshot_dir="$1"
    
    log_info "Executing incremental rollback..."
    
    # Restore only critical system files
    local critical_files=("CLAUDE.md" "README.md" ".gitignore" ".session-info")
    
    for file in "${critical_files[@]}"; do
        if [[ -f "$snapshot_dir/critical-files/$file" ]]; then
            log_info "Restoring critical file: $file"
            cp "$snapshot_dir/critical-files/$file" "$PROJECT_ROOT/"
        fi
    done
    
    log_success "Incremental rollback executed"
}

# Selective rollback (restore specific components)
execute_selective_rollback() {
    local snapshot_dir="$1"
    local target="${2:-commands}"
    
    log_info "Executing selective rollback for: $target"
    
    case "$target" in
        "commands")
            if [[ -d "$snapshot_dir/critical-files/commands" ]]; then
                log_info "Restoring commands directory..."
                rm -rf "$PROJECT_ROOT/commands" 2>/dev/null || true
                cp -r "$snapshot_dir/critical-files/commands" "$PROJECT_ROOT/"
            fi
            ;;
        "docs")
            if [[ -d "$snapshot_dir/critical-files/docs" ]]; then
                log_info "Restoring docs directory..."
                cp -r "$snapshot_dir/critical-files/docs"/* "$PROJECT_ROOT/docs/" 2>/dev/null || true
            fi
            ;;
        *)
            log_warning "Unknown selective target: $target"
            ;;
    esac
    
    log_success "Selective rollback executed for: $target"
}

# Setup git hooks for monitoring
setup_git_hooks() {
    local hooks_dir="$PROJECT_ROOT/.git/hooks"
    
    if [[ -d "$hooks_dir" ]]; then
        log_info "Setting up git monitoring hooks..."
        
        # Pre-commit hook for validation
        cat > "$hooks_dir/pre-commit" << 'EOF'
#!/bin/bash
# Rollback system pre-commit validation
ROLLBACK_DIR="$(git rev-parse --show-toplevel)/rollback"
if [[ -x "$ROLLBACK_DIR/rollback-manager.sh" ]]; then
    "$ROLLBACK_DIR/rollback-manager.sh" validate
fi
EOF
        chmod +x "$hooks_dir/pre-commit" 2>/dev/null || true
    fi
}

# List available snapshots
list_snapshots() {
    log_info "Available snapshots:"
    
    if [[ ! -d "$STATE_DIR" ]]; then
        log_warning "No snapshots directory found"
        return 1
    fi
    
    for snapshot in "$STATE_DIR"/*; do
        if [[ -d "$snapshot" ]]; then
            local name=$(basename "$snapshot")
            local metadata_file="$snapshot/metadata.json"
            
            if [[ -f "$metadata_file" ]]; then
                local timestamp=$(jq -r '.timestamp // "unknown"' "$metadata_file" 2>/dev/null || echo "unknown")
                local file_count=$(jq -r '.total_files // "unknown"' "$metadata_file" 2>/dev/null || echo "unknown")
                printf "  %-30s %s (%s files)\n" "$name" "$timestamp" "$file_count"
            else
                printf "  %-30s %s\n" "$name" "(metadata missing)"
            fi
        fi
    done
}

# Main command dispatcher
main() {
    case "${1:-}" in
        "initialize"|"init")
            initialize_rollback
            ;;
        "capture"|"snapshot")
            capture_current_state "${2:-}"
            ;;
        "validate"|"check")
            validate_system "${2:-}"
            ;;
        "rollback"|"restore")
            if [[ -z "${2:-}" ]]; then
                log_error "Snapshot name required for rollback"
                exit 1
            fi
            execute_rollback "$2" "${3:-complete}" "${4:-}"
            ;;
        "list"|"ls")
            list_snapshots
            ;;
        "help"|"-h"|"--help")
            cat << 'EOF'
Migration Rollback Manager

Usage: ./rollback-manager.sh [command] [options]

Commands:
  initialize          Initialize rollback system
  capture [name]      Capture current system state
  validate [snapshot] Validate system integrity
  rollback <snapshot> [scope] [target]
                     Execute rollback (scope: complete|incremental|selective)
  list               List available snapshots
  help               Show this help message

Examples:
  ./rollback-manager.sh initialize
  ./rollback-manager.sh capture pre-migration
  ./rollback-manager.sh validate
  ./rollback-manager.sh rollback pre-migration complete
  ./rollback-manager.sh rollback backup-001 selective commands
EOF
            ;;
        *)
            log_error "Unknown command: ${1:-}"
            echo "Use './rollback-manager.sh help' for usage information"
            exit 1
            ;;
    esac
}

# Execute main function
main "$@"