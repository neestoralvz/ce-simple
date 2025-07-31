#!/bin/bash
# rollback-validation.sh - Rollback integrity validation and system health monitoring
# Part of rollback-manager.sh L2-MODULAR extraction
# Authority: @context/architecture/patterns/l2-modular-extraction-patterns.md

set -euo pipefail

# Validate rollback integrity
validate_rollback_integrity() {
    local validation_type="${1:-basic}"  # basic, comprehensive, authority
    local target_files="${2:-}"
    
    echo -e "${BLUE}🔍 Validating rollback integrity ($validation_type)...${NC}"
    
    local validation_results="$OUTPUT_DIR/rollback_validation.json"
    
    python3 << 'EOF'
import json
import os
import subprocess
import sys
from datetime import datetime

validation_type = os.environ.get('validation_type', 'basic')
target_files = os.environ.get('target_files', '')
project_root = os.environ.get('PROJECT_ROOT', '')
validation_results = os.environ.get('validation_results', '')

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
print(f"\nVALIDATION_SUMMARY:")
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

    # Pass environment variables to Python script
    export validation_type="$validation_type"
    export target_files="$target_files"
    export PROJECT_ROOT="$PROJECT_ROOT"
    export validation_results="$validation_results"
}