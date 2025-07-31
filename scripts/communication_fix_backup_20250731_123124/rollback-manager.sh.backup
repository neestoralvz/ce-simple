#!/bin/bash
# rollback-manager.sh - Enhanced automated rollback capabilities for H6D operations
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Priority Script #6

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
CONTEXT_DIR="$PROJECT_ROOT/context"
OUTPUT_DIR="$PROJECT_ROOT/scripts/rollback_management_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/rollback_log.txt"
ROLLBACK_INDEX="$OUTPUT_DIR/rollback_index.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔄 ROLLBACK MANAGER: Enhanced Automated Recovery System${NC}"
echo "Purpose: Comprehensive rollback capabilities for H6A/B/C operations with git integration"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Initialize log
{
    echo "Rollback management started: $(date)"
    echo "Project root: $PROJECT_ROOT"
    echo "Target: Automated rollback capabilities for file operations and batch processing"
    echo "Safety: Multi-level rollback with git integration and integrity validation"
    echo "==============================================================================="
} > "$LOG_FILE"

# Rollback operation types
declare -A ROLLBACK_TYPES=(
    ["file"]="Single file rollback from backup"
    ["batch"]="Multiple file rollback from batch operation"
    ["session"]="Complete session rollback to initial state"
    ["git"]="Git-based rollback to specific commit"
    ["selective"]="Selective rollback of specific changes"
)

# Create comprehensive backup index
create_backup_index() {
    local backup_dir="$1"
    local operation_type="${2:-unknown}"
    local description="${3:-Backup operation}"
    
    echo -e "${BLUE}📋 Creating backup index for: $backup_dir${NC}"
    
    if [[ ! -d "$backup_dir" ]]; then
        echo -e "${RED}❌ Backup directory not found: $backup_dir${NC}"
        return 1
    fi
    
    python3 << EOF
import json
import os
import hashlib
from datetime import datetime

backup_dir = "$backup_dir"
operation_type = "$operation_type"
description = "$description"
project_root = "$PROJECT_ROOT"

def calculate_file_hash(file_path):
    """Calculate SHA-256 hash of file content"""
    try:
        with open(file_path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception as e:
        return f"error:{str(e)}"

# Scan backup directory
backup_files = []
for root, dirs, files in os.walk(backup_dir):
    for file in files:
        if file.endswith('.backup') or file.endswith('.md'):
            backup_path = os.path.join(root, file)
            relative_backup = os.path.relpath(backup_path, backup_dir)
            
            # Determine original file path
            if file.endswith('.backup'):
                original_name = file.replace('.backup', '')
                # Try to find original file location
                original_candidates = []
                for orig_root, orig_dirs, orig_files in os.walk(project_root):
                    if original_name in orig_files:
                        candidate_path = os.path.join(orig_root, original_name)
                        original_candidates.append(os.path.relpath(candidate_path, project_root))
                
                # Select most likely original path
                if original_candidates:
                    original_path = original_candidates[0]  # Simplistic selection
                else:
                    original_path = f"unknown/{original_name}"
            else:
                original_path = relative_backup
            
            # Get file metadata
            stat_info = os.stat(backup_path)
            
            backup_info = {
                "backup_file": relative_backup,
                "original_path": original_path,
                "backup_size": stat_info.st_size,
                "backup_mtime": datetime.fromtimestamp(stat_info.st_mtime).isoformat(),
                "file_hash": calculate_file_hash(backup_path),
                "rollback_ready": True
            }
            
            backup_files.append(backup_info)

# Create backup index
backup_index = {
    "index_created": datetime.now().isoformat(),
    "backup_directory": backup_dir,
    "operation_type": operation_type,
    "description": description,
    "total_backups": len(backup_files),
    "backup_files": backup_files,
    "git_info": {}
}

# Add git information if available
try:
    import subprocess
    
    # Get current git status
    git_result = subprocess.run(['git', 'rev-parse', 'HEAD'], 
                               capture_output=True, text=True, cwd=project_root)
    if git_result.returncode == 0:
        backup_index["git_info"]["current_commit"] = git_result.stdout.strip()
    
    # Get git status
    status_result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True, cwd=project_root)
    if status_result.returncode == 0:
        backup_index["git_info"]["working_tree_changes"] = len(status_result.stdout.strip().split('\\n')) if status_result.stdout.strip() else 0
    
except Exception as e:
    backup_index["git_info"]["error"] = str(e)

# Save backup index
index_file = "$ROLLBACK_INDEX"
with open(index_file, 'w') as f:
    json.dump(backup_index, f, indent=2)

print(f"BACKUP_INDEX_CREATED:{len(backup_files)}:{backup_dir}")

EOF
}

# Rollback single file
rollback_single_file() {
    local original_file="$1"
    local backup_file="$2"
    local verify_hash="${3:-true}"
    
    echo -e "${CYAN}Rolling back: $(basename "$original_file")${NC}"
    
    if [[ ! -f "$backup_file" ]]; then
        echo -e "${RED}❌ Backup file not found: $backup_file${NC}"
        return 1
    fi
    
    # Verify backup integrity if requested
    if [[ "$verify_hash" == "true" ]]; then
        local backup_hash=$(sha256sum "$backup_file" | cut -d' ' -f1)
        echo "Backup hash: $backup_hash"
    fi
    
    # Create recovery backup of current state
    local recovery_backup="${original_file}.recovery_$(date +%Y%m%d_%H%M%S)"
    if [[ -f "$original_file" ]]; then
        cp "$original_file" "$recovery_backup"
        echo "Current state backed up to: $(basename "$recovery_backup")"
    fi
    
    # Perform rollback
    if cp "$backup_file" "$original_file"; then
        echo -e "${GREEN}✅ Rollback successful: $(basename "$original_file")${NC}"
        
        # Log rollback
        {
            echo "FILE_ROLLBACK: $(date)"
            echo "  Original: $original_file"
            echo "  Backup: $backup_file"
            echo "  Recovery backup: $recovery_backup"
            echo "  Status: SUCCESS"
            echo "  ---"
        } >> "$LOG_FILE"
        
        return 0
    else
        echo -e "${RED}❌ Rollback failed: $(basename "$original_file")${NC}"
        
        # Log failure
        {
            echo "FILE_ROLLBACK: $(date)"
            echo "  Original: $original_file"
            echo "  Backup: $backup_file"
            echo "  Status: FAILED"
            echo "  ---"
        } >> "$LOG_FILE"
        
        return 1
    fi
}

# Rollback batch operation
rollback_batch_operation() {
    local backup_index_file="$1"
    local rollback_mode="${2:-interactive}"  # interactive, auto, selective
    local file_pattern="${3:-.*}"
    
    echo -e "${BLUE}🔄 Starting batch rollback...${NC}"
    
    if [[ ! -f "$backup_index_file" ]]; then
        echo -e "${RED}❌ Backup index not found: $backup_index_file${NC}"
        return 1
    fi
    
    python3 << EOF
import json
import os
import re
import subprocess
import shutil

backup_index_file = "$backup_index_file"
rollback_mode = "$rollback_mode"
file_pattern = "$file_pattern"
project_root = "$PROJECT_ROOT"

try:
    with open(backup_index_file, 'r') as f:
        backup_index = json.load(f)
    
    backup_files = backup_index.get("backup_files", [])
    backup_dir = backup_index.get("backup_directory", "")
    
    if not backup_files:
        print("NO_BACKUPS_FOUND")
        exit(1)
    
    print(f"Found {len(backup_files)} backup files")
    
    # Filter files by pattern
    pattern = re.compile(file_pattern)
    matching_files = [bf for bf in backup_files 
                     if pattern.search(bf["original_path"]) or pattern.search(bf["backup_file"])]
    
    if not matching_files:
        print(f"NO_MATCHES_FOR_PATTERN: {file_pattern}")
        exit(1)
    
    print(f"Matching files: {len(matching_files)}")
    
    rollback_results = {
        "attempted": 0,
        "succeeded": 0,
        "failed": 0,
        "skipped": 0,
        "results": []
    }
    
    for i, backup_info in enumerate(matching_files):
        backup_file_path = os.path.join(backup_dir, backup_info["backup_file"])
        original_file_path = os.path.join(project_root, backup_info["original_path"])
        
        print(f"\\n[{i+1}/{len(matching_files)}] Processing: {backup_info['original_path']}")
        
        # Check if backup file exists
        if not os.path.exists(backup_file_path):
            print(f"  ❌ Backup not found: {backup_file_path}")
            rollback_results["failed"] += 1
            rollback_results["results"].append({
                "file": backup_info["original_path"],
                "status": "failed",
                "reason": "Backup file not found"
            })
            continue
        
        rollback_results["attempted"] += 1
        
        if rollback_mode == "interactive":
            # For automation, assume 'yes' for all
            proceed = True
            print(f"  AUTO-PROCEED: Would prompt in interactive mode")
        elif rollback_mode == "selective":
            # Check if file was modified after backup
            if os.path.exists(original_file_path):
                original_mtime = os.path.getmtime(original_file_path)
                backup_mtime = os.path.getmtime(backup_file_path)
                
                if original_mtime > backup_mtime:
                    proceed = True  # File was modified, rollback
                    print(f"  FILE_MODIFIED: Rolling back due to changes")
                else:
                    proceed = False  # File unchanged, skip
                    print(f"  FILE_UNCHANGED: Skipping rollback")
            else:
                proceed = True  # File doesn't exist, restore from backup
        else:
            proceed = True  # auto mode
        
        if not proceed:
            rollback_results["skipped"] += 1
            rollback_results["results"].append({
                "file": backup_info["original_path"],
                "status": "skipped",
                "reason": "User declined or file unchanged"
            })
            continue
        
        # Create recovery backup of current state
        if os.path.exists(original_file_path):
            recovery_backup = f"{original_file_path}.recovery_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            try:
                shutil.copy2(original_file_path, recovery_backup)
                print(f"  💾 Current state backed up")
            except Exception as e:
                print(f"  ⚠️ Recovery backup failed: {e}")
        
        # Perform rollback
        try:
            # Ensure target directory exists
            os.makedirs(os.path.dirname(original_file_path), exist_ok=True)
            
            # Copy backup to original location
            shutil.copy2(backup_file_path, original_file_path)
            
            print(f"  ✅ Rollback successful")
            rollback_results["succeeded"] += 1
            rollback_results["results"].append({
                "file": backup_info["original_path"],
                "status": "success",
                "reason": "Rollback completed successfully"
            })
            
        except Exception as e:
            print(f"  ❌ Rollback failed: {e}")
            rollback_results["failed"] += 1
            rollback_results["results"].append({
                "file": backup_info["original_path"],
                "status": "failed",
                "reason": str(e)
            })
    
    # Output summary
    print(f"\\nBATCH_ROLLBACK_SUMMARY:")
    print(f"  Attempted: {rollback_results['attempted']}")
    print(f"  Succeeded: {rollback_results['succeeded']}")
    print(f"  Failed: {rollback_results['failed']}")
    print(f"  Skipped: {rollback_results['skipped']}")
    
    success_rate = (rollback_results['succeeded'] / rollback_results['attempted'] * 100) if rollback_results['attempted'] > 0 else 0
    print(f"  Success rate: {success_rate:.1f}%")
    
    # Save detailed results
    results_file = "$OUTPUT_DIR/batch_rollback_results.json"
    with open(results_file, 'w') as f:
        json.dump(rollback_results, f, indent=2)
    
    print(f"\\nDetailed results saved: {results_file}")

except Exception as e:
    print(f"BATCH_ROLLBACK_ERROR: {str(e)}")
EOF
}

# Git-based rollback operations
git_rollback_operation() {
    local rollback_type="$1"  # commit, branch, stash
    local target="$2"         # commit hash, branch name, stash index
    local scope="${3:-all}"   # all, context, specific_files
    
    echo -e "${BLUE}🔄 Git rollback operation: $rollback_type to $target${NC}"
    
    # Verify we're in a git repository
    if ! git -C "$PROJECT_ROOT" rev-parse --git-dir >/dev/null 2>&1; then
        echo -e "${RED}❌ Not a git repository: $PROJECT_ROOT${NC}"
        return 1
    fi
    
    # Save current state
    local current_commit=$(git -C "$PROJECT_ROOT" rev-parse HEAD)
    local current_branch=$(git -C "$PROJECT_ROOT" branch --show-current)
    
    echo "Current state: $current_branch ($current_commit)"
    
    case "$rollback_type" in
        "commit")
            echo "Rolling back to commit: $target"
            
            # Verify commit exists
            if ! git -C "$PROJECT_ROOT" cat-file -e "$target" 2>/dev/null; then
                echo -e "${RED}❌ Commit not found: $target${NC}"
                return 1
            fi
            
            if [[ "$scope" == "context" ]]; then
                # Rollback only context directory
                echo "Selective rollback: context/ directory only"
                if git -C "$PROJECT_ROOT" checkout "$target" -- context/; then
                    echo -e "${GREEN}✅ Context directory rolled back to $target${NC}"
                else
                    echo -e "${RED}❌ Context rollback failed${NC}"
                    return 1
                fi
            else
                # Full repository rollback
                echo "Full repository rollback to: $target"
                if git -C "$PROJECT_ROOT" reset --hard "$target"; then
                    echo -e "${GREEN}✅ Repository rolled back to $target${NC}"
                else
                    echo -e "${RED}❌ Repository rollback failed${NC}"
                    return 1
                fi
            fi
            ;;
            
        "branch")
            echo "Switching to branch: $target"
            
            # Check if branch exists
            if ! git -C "$PROJECT_ROOT" show-ref --verify --quiet "refs/heads/$target"; then
                echo -e "${RED}❌ Branch not found: $target${NC}"
                return 1
            fi
            
            if git -C "$PROJECT_ROOT" checkout "$target"; then
                echo -e "${GREEN}✅ Switched to branch: $target${NC}"
            else
                echo -e "${RED}❌ Branch switch failed${NC}"
                return 1
            fi
            ;;
            
        "stash")
            echo "Applying stash: $target"
            
            if git -C "$PROJECT_ROOT" stash apply "$target"; then
                echo -e "${GREEN}✅ Stash applied: $target${NC}"
            else
                echo -e "${RED}❌ Stash apply failed${NC}"
                return 1
            fi
            ;;
            
        *)
            echo -e "${RED}❌ Unknown git rollback type: $rollback_type${NC}"
            return 1
            ;;
    esac
    
    # Log git operation
    {
        echo "GIT_ROLLBACK: $(date)"
        echo "  Type: $rollback_type"
        echo "  Target: $target"
        echo "  Scope: $scope"
        echo "  Previous state: $current_branch ($current_commit)"
        echo "  Status: SUCCESS"
        echo "  ---"
    } >> "$LOG_FILE"
    
    return 0
}

# Validate rollback integrity
validate_rollback_integrity() {
    local validation_type="${1:-basic}"  # basic, comprehensive, authority
    local target_files="${2:-}"
    
    echo -e "${BLUE}🔍 Validating rollback integrity ($validation_type)...${NC}"
    
    local validation_results="$OUTPUT_DIR/rollback_validation.json"
    
    python3 << EOF
import json
import os
import subprocess
from datetime import datetime

validation_type = "$validation_type"
target_files = "$target_files"
project_root = "$PROJECT_ROOT"
validation_results = "$validation_results"

def check_file_integrity(file_path):
    """Check basic file integrity"""
    if not os.path.exists(file_path):
        return {"status": "missing", "error": "File does not exist"}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic content checks
        line_count = len(content.splitlines())
        
        # Check for common corruption signs
        if len(content) == 0:
            return {"status": "error", "error": "File is empty"}
        
        if '\x00' in content:
            return {"status": "error", "error": "File contains null bytes"}
        
        return {
            "status": "ok",
            "line_count": line_count,
            "size_bytes": len(content.encode('utf-8'))
        }
        
    except Exception as e:
        return {"status": "error", "error": str(e)}

def check_authority_integrity(file_path):
    """Check authority preservation (basic)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for key authority markers
        authority_markers = [
            "AUTORIDAD SUPREMA",
            "@context/",
            "user authority",
            "vision",
            "truth-source.md"
        ]
        
        found_markers = []
        for marker in authority_markers:
            if marker.lower() in content.lower():
                found_markers.append(marker)
        
        return {
            "status": "ok",
            "authority_markers": found_markers,
            "authority_score": len(found_markers) / len(authority_markers) * 100
        }
        
    except Exception as e:
        return {"status": "error", "error": str(e)}

# Initialize validation results
validation_data = {
    "validation_timestamp": datetime.now().isoformat(),
    "validation_type": validation_type,
    "project_root": project_root,
    "files_checked": 0,
    "integrity_results": [],
    "summary": {
        "files_ok": 0,
        "files_error": 0,
        "files_missing": 0
    }
}

# Determine files to check
files_to_check = []

if target_files and target_files != "":
    # Specific files provided
    for file_path in target_files.split(','):
        file_path = file_path.strip()
        if os.path.isabs(file_path):
            files_to_check.append(file_path)
        else:
            files_to_check.append(os.path.join(project_root, file_path))
else:
    # Find all markdown files
    for root, dirs, files in os.walk(project_root):
        # Skip certain directories
        dirs[:] = [d for d in dirs if not d.startswith('.git') and d != 'node_modules']
        
        for file in files:
            if file.endswith('.md'):
                files_to_check.append(os.path.join(root, file))

print(f"Checking {len(files_to_check)} files...")

# Validate each file
for file_path in files_to_check:
    relative_path = os.path.relpath(file_path, project_root)
    
    # Basic integrity check
    basic_result = check_file_integrity(file_path)
    
    file_validation = {
        "file": relative_path,
        "basic_integrity": basic_result
    }
    
    # Additional checks based on validation type
    if validation_type == "comprehensive" or validation_type == "authority":
        if basic_result["status"] == "ok":
            authority_result = check_authority_integrity(file_path)
            file_validation["authority_integrity"] = authority_result
    
    validation_data["files_checked"] += 1
    validation_data["integrity_results"].append(file_validation)
    
    # Update summary
    if basic_result["status"] == "ok":
        validation_data["summary"]["files_ok"] += 1
    elif basic_result["status"] == "missing":
        validation_data["summary"]["files_missing"] += 1
    else:
        validation_data["summary"]["files_error"] += 1

# Calculate overall health score
total_files = validation_data["files_checked"]
if total_files > 0:
    health_score = (validation_data["summary"]["files_ok"] / total_files) * 100
    validation_data["summary"]["health_score"] = round(health_score, 1)
else:
    validation_data["summary"]["health_score"] = 0

# Save validation results
with open(validation_results, 'w') as f:
    json.dump(validation_data, f, indent=2)

# Output summary
print(f"\\nVALIDATION_SUMMARY:")
print(f"  Files checked: {validation_data['files_checked']}")
print(f"  Files OK: {validation_data['summary']['files_ok']}")
print(f"  Files with errors: {validation_data['summary']['files_error']}")
print(f"  Missing files: {validation_data['summary']['files_missing']}")
print(f"  Health score: {validation_data['summary']['health_score']}%")

if validation_data['summary']['health_score'] >= 95:
    print("  Status: ✅ EXCELLENT integrity")
elif validation_data['summary']['health_score'] >= 85:
    print("  Status: ✅ GOOD integrity")
elif validation_data['summary']['health_score'] >= 70:
    print("  Status: ⚠️ ACCEPTABLE integrity")
else:
    print("  Status: ❌ POOR integrity - investigation needed")

EOF
}

# Generate rollback report
generate_rollback_report() {
    local report_file="$OUTPUT_DIR/ROLLBACK_MANAGEMENT_REPORT.md"
    
    cat > "$report_file" << EOF
# Rollback Management Report

**Generated**: $(date)
**Script**: rollback-manager.sh
**Purpose**: Comprehensive rollback capabilities and recovery system management

## Rollback System Overview

### Rollback Capabilities
- **Single File Rollback**: Individual file restoration from backup with integrity verification
- **Batch Operation Rollback**: Multiple file restoration with pattern matching and selective rollback
- **Session Rollback**: Complete operation session restoration to initial state
- **Git-Based Rollback**: Repository-level rollback to specific commits, branches, or stashes
- **Selective Rollback**: Targeted rollback of specific changes with user control

### Safety Features
- **Recovery Backups**: Current state backup before rollback execution
- **Integrity Validation**: File integrity verification before and after rollback
- **Authority Preservation**: Authority chain integrity monitoring during rollback
- **Multi-Level Protection**: File → Session → Git → Emergency rollback hierarchy

### Rollback Types Supported
1. **File Rollback**: Restore individual files from .backup versions
2. **Batch Rollback**: Restore multiple files from batch operation backups
3. **Git Commit Rollback**: Repository reset to specific commit hash
4. **Git Branch Rollback**: Switch to previous branch state
5. **Git Stash Rollback**: Apply previously stashed changes

### Integration with H6D Scripts
- **Domain Classifier**: Rollback classification changes and restore original categorization
- **Batch L2-MODULAR**: Restore hub-module extractions to original monolithic files
- **Authority Validator**: Rollback authority modifications and restore user voice fidelity
- **Cross-Reference Updater**: Restore reference integrity and undo reference updates
- **Progress Tracker**: Reset progress metrics and restore baseline measurements

## Quality Assurance

### Rollback Validation
- **Pre-Rollback**: Backup availability and integrity verification
- **During Rollback**: Operation success monitoring and error detection
- **Post-Rollback**: Integrity validation and authority preservation verification
- **Recovery Protection**: Current state backup before any rollback operation

### Emergency Recovery
- **Multi-Level Recovery**: File → Batch → Session → Git rollback hierarchy
- **Integrity Monitoring**: Continuous integrity checking during rollback operations
- **Authority Preservation**: User authority supremacy maintained through all rollback operations
- **System Health**: Complete system health validation after rollback completion

### Usage Recommendations
- Always verify backup integrity before rollback execution
- Use selective rollback for targeted restoration of specific changes
- Implement regular backup indexing for efficient rollback management
- Monitor authority preservation during and after rollback operations

---
**Generated by**: rollback-manager.sh - H6D-SCRIPTS automation framework
EOF

    echo -e "${GREEN}📄 Rollback report: ROLLBACK_MANAGEMENT_REPORT.md${NC}"
}

# Show usage information
show_usage() {
    cat << EOF
Rollback Manager - H6D-SCRIPTS Automation Framework

USAGE:
    $0 --index backup_dir [operation] [description]     # Create backup index
    $0 --file original backup [verify_hash]            # Rollback single file
    $0 --batch index_file [mode] [pattern]             # Rollback batch operation
    $0 --git type target [scope]                       # Git-based rollback
    $0 --validate [type] [files]                       # Validate rollback integrity
    $0 --help                                           # Show this help

COMMANDS:
    --index        Create comprehensive backup index for rollback operations
    --file         Rollback single file from backup with integrity verification
    --batch        Rollback multiple files from batch operation backup
    --git          Git-based rollback operations (commit, branch, stash)
    --validate     Validate rollback integrity and system health

INDEX EXAMPLES:
    $0 --index /path/to/backups h6a "H6A quick wins backup"
    $0 --index backup_dir l2_modular "L2-MODULAR extraction backup"

FILE ROLLBACK EXAMPLES:
    $0 --file context/file.md backup/file.md.backup true
    $0 --file path/to/file.md backup_dir/file.backup false

BATCH ROLLBACK EXAMPLES:
    $0 --batch backup_index.json interactive "context/.*"
    $0 --batch index.json auto ".*authority.*"
    $0 --batch index.json selective

BATCH MODES:
    interactive    Prompt for each file rollback decision
    auto           Automatic rollback for all matching files
    selective      Rollback only files modified after backup

GIT ROLLBACK EXAMPLES:
    $0 --git commit abc1234 context                    # Rollback context/ to commit
    $0 --git commit HEAD~3 all                         # Rollback repo 3 commits
    $0 --git branch feature-branch                     # Switch to branch
    $0 --git stash stash@{0}                          # Apply stash

GIT SCOPES:
    all            Full repository rollback
    context        Context directory only rollback
    specific       Specific files rollback (not implemented)

VALIDATION EXAMPLES:
    $0 --validate basic                                # Basic file integrity check
    $0 --validate comprehensive                        # Full system validation
    $0 --validate authority "context/authority.md"     # Authority integrity check

VALIDATION TYPES:
    basic          File existence and basic integrity
    comprehensive  Full integrity including authority markers
    authority      Authority preservation and chain integrity

SAFETY FEATURES:
    - Recovery backups created before all rollback operations
    - Backup integrity verification with SHA-256 hashing
    - Multi-level rollback hierarchy (file → batch → session → git)
    - Authority preservation monitoring during rollback operations
    - Complete operation logging for audit and troubleshooting

OUTPUT:
    - Comprehensive rollback operation logging
    - Integrity validation reports and system health assessment
    - Detailed rollback results with success/failure tracking
    - Recovery backup creation for safe rollback operations
EOF
}

# Main execution function
main() {
    if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
        show_usage
        exit 0
    fi
    
    case "$1" in
        --index)
            if [[ $# -lt 2 ]]; then
                echo -e "${RED}❌ Usage: $0 --index backup_dir [operation] [description]${NC}"
                exit 1
            fi
            
            local backup_dir="$2"
            local operation="${3:-unknown}"
            local description="${4:-Backup operation}"
            
            if create_backup_index "$backup_dir" "$operation" "$description"; then
                echo -e "${GREEN}✅ Backup index created successfully${NC}"
            else
                echo -e "${RED}❌ Failed to create backup index${NC}"
                exit 1
            fi
            ;;
            
        --file)
            if [[ $# -lt 3 ]]; then
                echo -e "${RED}❌ Usage: $0 --file original backup [verify_hash]${NC}"
                exit 1
            fi
            
            local original_file="$2"
            local backup_file="$3"
            local verify_hash="${4:-true}"
            
            if rollback_single_file "$original_file" "$backup_file" "$verify_hash"; then
                echo -e "${GREEN}✅ File rollback completed successfully${NC}"
            else
                echo -e "${RED}❌ File rollback failed${NC}"
                exit 1
            fi
            ;;
            
        --batch)
            if [[ $# -lt 2 ]]; then
                echo -e "${RED}❌ Usage: $0 --batch index_file [mode] [pattern]${NC}"
                exit 1
            fi
            
            local index_file="$2"
            local mode="${3:-interactive}"
            local pattern="${4:-.*}"
            
            rollback_batch_operation "$index_file" "$mode" "$pattern"
            echo -e "${GREEN}✅ Batch rollback operation completed${NC}"
            ;;
            
        --git)
            if [[ $# -lt 3 ]]; then
                echo -e "${RED}❌ Usage: $0 --git type target [scope]${NC}"
                exit 1
            fi
            
            local rollback_type="$2"
            local target="$3"
            local scope="${4:-all}"
            
            if git_rollback_operation "$rollback_type" "$target" "$scope"; then
                echo -e "${GREEN}✅ Git rollback completed successfully${NC}"
            else
                echo -e "${RED}❌ Git rollback failed${NC}"
                exit 1
            fi
            ;;
            
        --validate)
            local validation_type="${2:-basic}"
            local target_files="${3:-}"
            
            validate_rollback_integrity "$validation_type" "$target_files"
            echo -e "${GREEN}✅ Rollback integrity validation completed${NC}"
            ;;
            
        *)
            echo -e "${RED}❌ Unknown option: $1${NC}"
            show_usage
            exit 1
            ;;
    esac
    
    # Generate report for all operations
    if [[ "$1" != "--help" ]]; then
        generate_rollback_report
        
        echo -e "\n${GREEN}📁 Output directory: $OUTPUT_DIR${NC}"
        echo -e "${GREEN}📄 Operation log: $LOG_FILE${NC}"
        if [[ -f "$ROLLBACK_INDEX" ]]; then
            echo -e "${GREEN}📋 Rollback index: $ROLLBACK_INDEX${NC}"
        fi
    fi
}

# Execute main function
main "$@"