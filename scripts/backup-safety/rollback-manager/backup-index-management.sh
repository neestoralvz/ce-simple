#!/bin/bash
# backup-index-management.sh - Comprehensive backup indexing for rollback operations
# Part of rollback-manager.sh L2-MODULAR extraction
# Authority: @context/architecture/patterns/l2-modular-extraction-patterns.md

set -euo pipefail

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