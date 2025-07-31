#!/bin/bash
# batch-rollback-operations.sh - Batch rollback operations with pattern matching
# Part of rollback-manager.sh L2-MODULAR extraction
# Authority: @context/architecture/patterns/l2-modular-extraction-patterns.md

set -euo pipefail

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
    
    python3 << 'EOF'
import json
import os
import re
import subprocess
import shutil
from datetime import datetime

backup_index_file = os.environ.get('backup_index_file', sys.argv[1] if len(sys.argv) > 1 else '')
rollback_mode = os.environ.get('rollback_mode', sys.argv[2] if len(sys.argv) > 2 else 'interactive')
file_pattern = os.environ.get('file_pattern', sys.argv[3] if len(sys.argv) > 3 else '.*')
project_root = os.environ.get('PROJECT_ROOT', '')
output_dir = os.environ.get('OUTPUT_DIR', '')

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
        
        print(f"\n[{i+1}/{len(matching_files)}] Processing: {backup_info['original_path']}")
        
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
    print(f"\nBATCH_ROLLBACK_SUMMARY:")
    print(f"  Attempted: {rollback_results['attempted']}")
    print(f"  Succeeded: {rollback_results['succeeded']}")
    print(f"  Failed: {rollback_results['failed']}")
    print(f"  Skipped: {rollback_results['skipped']}")
    
    success_rate = (rollback_results['succeeded'] / rollback_results['attempted'] * 100) if rollback_results['attempted'] > 0 else 0
    print(f"  Success rate: {success_rate:.1f}%")
    
    # Save detailed results
    results_file = f"{output_dir}/batch_rollback_results.json"
    with open(results_file, 'w') as f:
        json.dump(rollback_results, f, indent=2)
    
    print(f"\nDetailed results saved: {results_file}")

except Exception as e:
    print(f"BATCH_ROLLBACK_ERROR: {str(e)}")
EOF

    # Pass environment variables to Python script
    export backup_index_file="$backup_index_file"
    export rollback_mode="$rollback_mode"
    export file_pattern="$file_pattern"
    export PROJECT_ROOT="$PROJECT_ROOT"
    export OUTPUT_DIR="$OUTPUT_DIR"
}