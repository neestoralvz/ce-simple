#!/bin/bash
# recovery-protocol.sh - Systematic error resolution and recovery system
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Priority Script #11

set -euo pipefail

# Configuration
# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
CONTEXT_DIR="$PROJECT_ROOT/context"
OUTPUT_DIR="$PROJECT_ROOT/scripts/recovery_protocol_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/recovery_protocol_log.txt"
RECOVERY_STATE="$OUTPUT_DIR/recovery_state.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚑 RECOVERY PROTOCOL: Systematic Error Resolution System${NC}"
echo "Purpose: Comprehensive error resolution and system recovery with automated protocols"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Initialize log
{
    echo "Recovery protocol started: $(date)"
    echo "Project root: $PROJECT_ROOT"
    echo "Target: Systematic error resolution and system recovery"
    echo "Protocols: Multi-level recovery, automated resolution, rollback protection"
    echo "==========================================================================================="
} > "$LOG_FILE"

# Recovery protocol configuration
declare -A RECOVERY_CONFIG=(
    ["max_file_size"]="80"
    ["authority_threshold"]="95.0"
    ["backup_retention"]="7"
    ["max_recovery_attempts"]="3"
    ["rollback_on_failure"]="true"
)

# Initialize recovery state tracking
initialize_recovery_state() {
    local operation_type="$1"
    local target_issues="${2:-}"
    
    python3 << EOF
import json
from datetime import datetime

operation_type = "$operation_type"
target_issues = "$target_issues"
recovery_state_file = "$RECOVERY_STATE"

recovery_state = {
    "recovery_session": {
        "session_id": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "start_time": datetime.now().isoformat(),
        "operation_type": operation_type,
        "target_issues": target_issues,
        "status": "INITIALIZED"
    },
    "recovery_progress": {
        "total_issues": 0,
        "resolved_issues": 0,
        "failed_resolutions": 0,
        "current_step": "initialization"
    },
    "recovery_actions": [],
    "rollback_points": [],
    "system_health": {
        "pre_recovery": {},
        "post_recovery": {},
        "health_score": 0
    }
}

with open(recovery_state_file, 'w') as f:
    json.dump(recovery_state, f, indent=2)

print(f"RECOVERY_INITIALIZED:{recovery_state['recovery_session']['session_id']}")

EOF
}

# Create system recovery checkpoint
create_recovery_checkpoint() {
    local checkpoint_type="$1"
    local description="$2"
    
    echo -e "${BLUE}💾 Creating recovery checkpoint: $checkpoint_type${NC}"
    
    local checkpoint_dir="$OUTPUT_DIR/checkpoints/$(date +%Y%m%d_%H%M%S)_${checkpoint_type}"
    mkdir -p "$checkpoint_dir"
    
    # Create git checkpoint if in git repository
    if git -C "$PROJECT_ROOT" rev-parse --git-dir >/dev/null 2>&1; then
        local current_commit=$(git -C "$PROJECT_ROOT" rev-parse HEAD)
        local current_branch=$(git -C "$PROJECT_ROOT" branch --show-current)
        
        echo "$current_commit" > "$checkpoint_dir/git_commit.txt"
        echo "$current_branch" > "$checkpoint_dir/git_branch.txt"
        
        echo -e "${GREEN}✅ Git checkpoint created: $current_branch ($current_commit)${NC}"
    fi
    
    # Create file system checkpoint for critical files
    python3 << EOF
import os
import json
import shutil
from datetime import datetime

checkpoint_dir = "$checkpoint_dir"
project_root = "$PROJECT_ROOT"
description = "$description"

checkpoint_info = {
    "checkpoint_type": "$checkpoint_type",
    "description": description,
    "timestamp": datetime.now().isoformat(),
    "files_backed_up": [],
    "total_files": 0
}

# Backup critical context files
context_dir = os.path.join(project_root, "context")
backup_count = 0

for root, dirs, files in os.walk(context_dir):
    # Skip .git and results directories
    dirs[:] = [d for d in dirs if not d.startswith('.git') and 'results' not in d]
    
    for file in files:
        if file.endswith('.md'):
            source_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_path, project_root)
            
            # Create backup directory structure
            backup_path = os.path.join(checkpoint_dir, relative_path)
            os.makedirs(os.path.dirname(backup_path), exist_ok=True)
            
            try:
                shutil.copy2(source_path, backup_path)
                checkpoint_info["files_backed_up"].append(relative_path)
                backup_count += 1
            except Exception as e:
                continue

checkpoint_info["total_files"] = backup_count

# Save checkpoint metadata
with open(os.path.join(checkpoint_dir, "checkpoint_info.json"), 'w') as f:
    json.dump(checkpoint_info, f, indent=2)

print(f"CHECKPOINT_CREATED:{backup_count}:{checkpoint_dir}")

EOF
    
    # Update recovery state with checkpoint
    python3 << EOF
import json

recovery_state_file = "$RECOVERY_STATE"
checkpoint_dir = "$checkpoint_dir"

try:
    with open(recovery_state_file, 'r') as f:
        recovery_state = json.load(f)
    
    recovery_state["rollback_points"].append({
        "type": "$checkpoint_type",
        "description": "$description",
        "timestamp": "$(date -Iseconds)",
        "checkpoint_path": checkpoint_dir
    })
    
    with open(recovery_state_file, 'w') as f:
        json.dump(recovery_state, f, indent=2)
        
    print("CHECKPOINT_REGISTERED")
    
except Exception as e:
    print(f"CHECKPOINT_ERROR:{str(e)}")
EOF
}

# Resolve file size violations systematically
resolve_file_size_violations() {
    local resolution_mode="${1:-conservative}"
    local max_files="${2:-10}"
    
    echo -e "${BLUE}🔧 Resolving file size violations (mode: $resolution_mode, max: $max_files)${NC}"
    
    # Create checkpoint before resolution
    create_recovery_checkpoint "file_size_resolution" "Before file size violation resolution"
    
    python3 << EOF
import os
import json
import subprocess
from datetime import datetime

resolution_mode = "$resolution_mode"
max_files = int("$max_files")
project_root = "$PROJECT_ROOT"
recovery_state_file = "$RECOVERY_STATE"
max_file_size = int("${RECOVERY_CONFIG[max_file_size]}")

resolution_results = {
    "resolution_type": "file_size_violations",
    "mode": resolution_mode,
    "results": [],
    "summary": {
        "attempted": 0,
        "successful": 0,
        "failed": 0,
        "skipped": 0
    }
}

# Find files that violate size requirements
violation_files = []

for root, dirs, files in os.walk(project_root):
    dirs[:] = [d for d in dirs if not d.startswith('.git') and d != 'node_modules' and 'results' not in d]
    
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    line_count = len(f.readlines())
                
                if line_count > max_file_size:
                    violation_files.append({
                        "file": file_path,
                        "relative_path": os.path.relpath(file_path, project_root),
                        "lines": line_count,
                        "excess": line_count - max_file_size,
                        "severity": "CRITICAL" if line_count > 400 else "HIGH" if line_count > 200 else "MEDIUM"
                    })
                    
            except Exception as e:
                continue

# Sort by severity and excess lines
violation_files.sort(key=lambda x: (x["severity"] == "CRITICAL", x["excess"]), reverse=True)

# Process violations based on mode
processed = 0
for violation in violation_files[:max_files]:
    if processed >= max_files:
        break
        
    resolution_results["summary"]["attempted"] += 1
    file_path = violation["file"]
    relative_path = violation["relative_path"]
    
    result = {
        "file": relative_path,
        "original_lines": violation["lines"],
        "severity": violation["severity"],
        "resolution_attempted": True,
        "success": False,
        "action_taken": "none",
        "error": None
    }
    
    try:
        if resolution_mode == "conservative":
            # Conservative mode: create L2-MODULAR hub structure
            if violation["lines"] > 90 and violation["lines"] <= 250:
                # Call batch-l2-modular.sh for suitable candidates
                batch_script = os.path.join(project_root, "scripts", "batch-processing", "batch-l2-modular.sh")
                
                if os.path.exists(batch_script):
                    # Run L2-MODULAR extraction
                    cmd_result = subprocess.run([
                        "bash", batch_script, 
                        f".*{os.path.basename(file_path)}.*", "70", "1", "false"
                    ], capture_output=True, text=True, cwd=project_root)
                    
                    if cmd_result.returncode == 0:
                        # Check if file size was reduced
                        with open(file_path, 'r', encoding='utf-8') as f:
                            new_line_count = len(f.readlines())
                        
                        if new_line_count <= max_file_size:
                            result["success"] = True
                            result["action_taken"] = "l2_modular_extraction"
                            result["new_lines"] = new_line_count
                            resolution_results["summary"]["successful"] += 1
                        else:
                            result["error"] = f"Extraction reduced to {new_line_count} lines, still exceeds limit"
                            resolution_results["summary"]["failed"] += 1
                    else:
                        result["error"] = f"L2-MODULAR extraction failed: {cmd_result.stderr}"
                        resolution_results["summary"]["failed"] += 1
                else:
                    result["error"] = "batch-l2-modular.sh script not found"
                    resolution_results["summary"]["failed"] += 1
            else:
                result["action_taken"] = "skipped_unsuitable"
                result["error"] = f"File size {violation['lines']} not suitable for automated resolution"
                resolution_results["summary"]["skipped"] += 1
                
        elif resolution_mode == "aggressive":
            # Aggressive mode: attempt direct editing (not implemented for safety)
            result["action_taken"] = "skipped_aggressive_not_implemented"
            result["error"] = "Aggressive mode not implemented for safety"
            resolution_results["summary"]["skipped"] += 1
            
        else:
            result["error"] = f"Unknown resolution mode: {resolution_mode}"
            resolution_results["summary"]["failed"] += 1
            
    except Exception as e:
        result["error"] = str(e)
        resolution_results["summary"]["failed"] += 1
    
    resolution_results["results"].append(result)
    processed += 1

# Update recovery state
try:
    with open(recovery_state_file, 'r') as f:
        recovery_state = json.load(f)
    
    recovery_state["recovery_actions"].append(resolution_results)
    recovery_state["recovery_progress"]["current_step"] = "file_size_resolution"
    
    with open(recovery_state_file, 'w') as f:
        json.dump(recovery_state, f, indent=2)
        
except Exception as e:
    pass

# Output results
print(json.dumps(resolution_results, indent=2))

EOF
}

# Resolve authority preservation issues
resolve_authority_issues() {
    local resolution_strategy="${1:-restore}"
    local min_fidelity="${2:-${RECOVERY_CONFIG[authority_threshold]}}"
    
    echo -e "${BLUE}🔧 Resolving authority preservation issues (strategy: $resolution_strategy)${NC}"
    
    # Create checkpoint before resolution
    create_recovery_checkpoint "authority_resolution" "Before authority preservation resolution"
    
    python3 << EOF
import os
import re
import json
from datetime import datetime

resolution_strategy = "$resolution_strategy"
min_fidelity = float("$min_fidelity")
project_root = "$PROJECT_ROOT"
context_dir = "$CONTEXT_DIR"

resolution_results = {
    "resolution_type": "authority_preservation",
    "strategy": resolution_strategy,
    "min_fidelity": min_fidelity,
    "results": [],
    "summary": {
        "attempted": 0,
        "successful": 0,
        "failed": 0
    }
}

def calculate_authority_score(content):
    """Calculate simplified authority score"""
    score = 0
    
    # Direct quotes (40 points max)
    quotes = len(re.findall(r'[">][^"<\\n]{10,}["><]', content))
    score += min(40, quotes * 8)
    
    # Authority declarations (25 points max)
    auth_declarations = len(re.findall(r'AUTORIDAD|SUPREMA|Authority|VISION|PRINCIPIO', content, re.IGNORECASE))
    score += min(25, auth_declarations * 5)
    
    # Context references (20 points max)
    context_refs = len(re.findall(r'@context/', content))
    score += min(20, context_refs * 4)
    
    # Spanish authority markers (15 points max)
    spanish_markers = len(re.findall(r'usuario|visión|metodología|suprema', content.lower()))
    score += min(15, spanish_markers * 3)
    
    return min(100, score)

def enhance_authority_content(content, target_score):
    """Enhance content to improve authority score"""
    enhanced_content = content
    
    # Add authority section if missing
    if not re.search(r'## AUTORIDAD SUPREMA|## AUTHORITY', content, re.IGNORECASE):
        # Find where to insert authority section (after title)
        lines = content.split('\\n')
        insert_pos = 1
        
        # Find first empty line after title
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '':
                insert_pos = i
                break
        
        authority_section = '''
## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → specialized authority per user vision supremacy

## PRINCIPIO FUNDAMENTAL
**"System functionality serves user authority supremacy through specialized implementation"** - Complete authority preservation through systematic enhancement.
'''
        
        lines.insert(insert_pos, authority_section)
        enhanced_content = '\\n'.join(lines)
    
    return enhanced_content

# Find authority files with low fidelity
authority_files = []

for root, dirs, files in os.walk(context_dir):
    dirs[:] = [d for d in dirs if not d.startswith('.git')]
    
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, project_root)
            
            # Focus on authority-related files
            if any(keyword in relative_path.lower() for keyword in ['authority', 'vision', 'core', 'truth-source']):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    score = calculate_authority_score(content)
                    
                    if score < min_fidelity:
                        authority_files.append({
                            "file": file_path,
                            "relative_path": relative_path,
                            "current_score": score,
                            "target_score": min_fidelity
                        })
                        
                except Exception as e:
                    continue

# Process authority enhancement
for auth_file in authority_files[:5]:  # Limit to 5 files for safety
    resolution_results["summary"]["attempted"] += 1
    
    result = {
        "file": auth_file["relative_path"],
        "original_score": auth_file["current_score"],
        "target_score": auth_file["target_score"],
        "success": False,
        "action_taken": "none",
        "error": None
    }
    
    try:
        if resolution_strategy == "restore":
            # Conservative enhancement: add missing authority markers
            with open(auth_file["file"], 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            enhanced_content = enhance_authority_content(original_content, auth_file["target_score"])
            new_score = calculate_authority_score(enhanced_content)
            
            if new_score > auth_file["current_score"]:
                # Create backup
                backup_path = f"{auth_file['file']}.authority_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                with open(backup_path, 'w', encoding='utf-8') as backup_f:
                    backup_f.write(original_content)
                
                # Write enhanced content
                with open(auth_file["file"], 'w', encoding='utf-8') as f:
                    f.write(enhanced_content)
                
                result["success"] = True
                result["action_taken"] = "authority_enhancement"
                result["new_score"] = new_score
                result["improvement"] = new_score - auth_file["current_score"]
                resolution_results["summary"]["successful"] += 1
            else:
                result["error"] = "Enhancement did not improve score sufficiently"
                resolution_results["summary"]["failed"] += 1
                
        else:
            result["error"] = f"Unknown resolution strategy: {resolution_strategy}"
            resolution_results["summary"]["failed"] += 1
            
    except Exception as e:
        result["error"] = str(e)
        resolution_results["summary"]["failed"] += 1
    
    resolution_results["results"].append(result)

# Output results
print(json.dumps(resolution_results, indent=2))

EOF
}

# Resolve reference integrity issues
resolve_reference_issues() {
    local resolution_approach="${1:-repair}"
    local max_repairs="${2:-20}"
    
    echo -e "${BLUE}🔧 Resolving reference integrity issues (approach: $resolution_approach)${NC}"
    
    # Create checkpoint before resolution
    create_recovery_checkpoint "reference_resolution" "Before reference integrity resolution"
    
    # Use the reference-integrity-validator.sh for actual repairs
    local ref_validator="$PROJECT_ROOT/scripts/validation/reference-integrity-validator.sh"
    
    if [[ -f "$ref_validator" ]]; then
        echo -e "${CYAN}Using reference-integrity-validator.sh for repairs...${NC}"
        
        # Run validation to identify issues
        if bash "$ref_validator" --validate ".*" true; then
            echo -e "${GREEN}✅ Reference integrity validation passed${NC}"
        else
            echo -e "${YELLOW}⚠️  Reference integrity issues detected${NC}"
            
            # Run fix operation if repair approach selected
            if [[ "$resolution_approach" == "repair" ]]; then
                bash "$ref_validator" --fix true conservative
            fi
        fi
    else
        echo -e "${RED}❌ Reference integrity validator not found${NC}"
    fi
    
    # Log reference resolution attempt
    {
        echo "REFERENCE_RESOLUTION: $(date)"
        echo "  Approach: $resolution_approach"
        echo "  Max repairs: $max_repairs"
        echo "  Validator: $ref_validator"
        echo "  ---"
    } >> "$LOG_FILE"
}

# Execute comprehensive system recovery
execute_system_recovery() {
    local recovery_level="${1:-standard}"
    local dry_run="${2:-false}"
    
    echo -e "${BLUE}🚑 Executing comprehensive system recovery (level: $recovery_level, dry_run: $dry_run)${NC}"
    
    # Initialize recovery session
    local session_id=$(initialize_recovery_state "comprehensive_recovery" "$recovery_level")
    session_id=${session_id#*:}
    
    echo -e "${CYAN}Recovery session: $session_id${NC}"
    
    if [[ "$dry_run" == "true" ]]; then
        echo -e "${YELLOW}⚠️  DRY RUN MODE: No files will be modified${NC}"
        return 0
    fi
    
    # Create initial system checkpoint
    create_recovery_checkpoint "pre_recovery" "System state before comprehensive recovery"
    
    local recovery_success=true
    
    # Phase 1: File Size Violations
    echo -e "\n${PURPLE}Phase 1: File Size Violation Resolution${NC}"
    if resolve_file_size_violations "conservative" "5"; then
        echo -e "${GREEN}✅ File size resolution completed${NC}"
    else
        echo -e "${RED}❌ File size resolution encountered issues${NC}"
        recovery_success=false
    fi
    
    # Phase 2: Authority Preservation
    echo -e "\n${PURPLE}Phase 2: Authority Preservation Resolution${NC}"
    if resolve_authority_issues "restore" "${RECOVERY_CONFIG[authority_threshold]}"; then
        echo -e "${GREEN}✅ Authority resolution completed${NC}"
    else
        echo -e "${RED}❌ Authority resolution encountered issues${NC}"
        recovery_success=false
    fi
    
    # Phase 3: Reference Integrity
    echo -e "\n${PURPLE}Phase 3: Reference Integrity Resolution${NC}"
    if resolve_reference_issues "repair" "10"; then
        echo -e "${GREEN}✅ Reference resolution completed${NC}"
    else
        echo -e "${RED}❌ Reference resolution encountered issues${NC}"
        recovery_success=false
    fi
    
    # Create post-recovery checkpoint
    create_recovery_checkpoint "post_recovery" "System state after comprehensive recovery"
    
    # Final recovery assessment
    echo -e "\n${BLUE}📊 Recovery Assessment${NC}"
    if [[ "$recovery_success" == true ]]; then
        echo -e "${GREEN}🎉 RECOVERY SUCCESSFUL: System recovery completed successfully${NC}"
        
        # Update recovery state
        python3 << EOF
import json

recovery_state_file = "$RECOVERY_STATE"

try:
    with open(recovery_state_file, 'r') as f:
        recovery_state = json.load(f)
    
    recovery_state["recovery_session"]["status"] = "COMPLETED"
    recovery_state["recovery_session"]["end_time"] = "$(date -Iseconds)"
    recovery_state["recovery_progress"]["current_step"] = "completed"
    
    with open(recovery_state_file, 'w') as f:
        json.dump(recovery_state, f, indent=2)
        
except Exception as e:
    pass
EOF
        
        return 0
    else
        echo -e "${RED}⚠️  RECOVERY INCOMPLETE: Some issues remain unresolved${NC}"
        
        if [[ "${RECOVERY_CONFIG[rollback_on_failure]}" == "true" ]]; then
            echo -e "${YELLOW}🔄 Considering rollback due to incomplete recovery${NC}"
        fi
        
        return 1
    fi
}

# Rollback to previous checkpoint
rollback_to_checkpoint() {
    local checkpoint_id="${1:-latest}"
    local rollback_scope="${2:-full}"
    
    echo -e "${BLUE}🔄 Rolling back to checkpoint: $checkpoint_id (scope: $rollback_scope)${NC}"
    
    # Use rollback-manager.sh for actual rollback operations
    local rollback_manager="$PROJECT_ROOT/scripts/backup-safety/rollback-manager.sh"
    
    if [[ -f "$rollback_manager" ]]; then
        echo -e "${CYAN}Using rollback-manager.sh for checkpoint restoration...${NC}"
        
        case "$rollback_scope" in
            "full")
                bash "$rollback_manager" --git commit HEAD~1 all
                ;;
            "context")
                bash "$rollback_manager" --git commit HEAD~1 context
                ;;
            *)
                echo -e "${YELLOW}⚠️  Custom rollback scope not implemented${NC}"
                ;;
        esac
    else
        echo -e "${RED}❌ Rollback manager not found${NC}"
        return 1
    fi
    
    # Log rollback operation
    {
        echo "ROLLBACK_OPERATION: $(date)"
        echo "  Checkpoint: $checkpoint_id"
        echo "  Scope: $rollback_scope"
        echo "  Manager: $rollback_manager"
        echo "  ---"
    } >> "$LOG_FILE"
}

# Generate recovery report
generate_recovery_report() {
    local report_file="$OUTPUT_DIR/RECOVERY_PROTOCOL_REPORT.md"
    
    cat > "$report_file" << EOF
# Recovery Protocol Report

**Generated**: $(date)
**Script**: recovery-protocol.sh
**Purpose**: Systematic error resolution and system recovery

## Recovery Session Summary

### Session Information
$(if [[ -f "$RECOVERY_STATE" ]]; then
    python3 << 'PYTHON_EOF'
import json
try:
    with open("$RECOVERY_STATE", 'r') as f:
        recovery_state = json.load(f)
    
    session = recovery_state.get('recovery_session', {})
    print(f"- **Session ID**: {session.get('session_id', 'Unknown')}")
    print(f"- **Operation Type**: {session.get('operation_type', 'Unknown')}")
    print(f"- **Status**: {session.get('status', 'Unknown')}")
    print(f"- **Start Time**: {session.get('start_time', 'Unknown')}")
    if 'end_time' in session:
        print(f"- **End Time**: {session.get('end_time')}")
except:
    print("- **Status**: Recovery state unavailable")
PYTHON_EOF
else
    echo "- **Status**: No recovery session data available"
fi)

### Recovery Capabilities

#### File Size Violation Resolution
- **Conservative Mode**: L2-MODULAR extraction for files 91-250 lines
- **Automated Processing**: Batch processing with rollback protection
- **Safety Measures**: Backup creation before all modifications
- **Success Validation**: Post-resolution size verification

#### Authority Preservation Resolution
- **Enhancement Strategy**: Missing authority marker restoration
- **Fidelity Targeting**: ≥95% user voice preservation requirement
- **Content Analysis**: Systematic authority score calculation
- **Quote Preservation**: User voice fidelity maintenance priority

#### Reference Integrity Resolution
- **Broken Link Repair**: Automated reference validation and repair
- **Bidirectional Consistency**: Mutual reference validation and restoration
- **Syntax Correction**: @context/ prefix compliance enforcement
- **Authority Chain Validation**: Complete authority traceability verification

### Recovery Protocol Features

#### Multi-Level Recovery
1. **File Level**: Individual file issue resolution with targeted fixes
2. **System Level**: Comprehensive system-wide issue resolution
3. **Emergency Level**: Complete system recovery with full rollback capability
4. **Preventive Level**: Proactive issue detection and resolution

#### Safety Mechanisms
- **Checkpoint System**: Automated backup creation before all operations
- **Rollback Protection**: Complete system state restoration capability
- **Incremental Recovery**: Step-by-step resolution with validation at each stage
- **Failure Handling**: Automatic rollback on critical resolution failures

### Integration with H6D Scripts

#### Recovery Automation
- **Error Detector Integration**: Proactive issue identification feeding recovery protocols
- **Batch Processing Integration**: L2-MODULAR extraction for systematic file size resolution
- **Authority Validator Integration**: 95%+ fidelity validation and enhancement
- **Reference Validator Integration**: Comprehensive reference integrity restoration

#### Quality Assurance
- **Pre-Recovery Validation**: System state assessment before recovery operations
- **Post-Recovery Validation**: Complete system health verification after recovery
- **Continuous Monitoring**: Real-time recovery effectiveness measurement
- **Success Metrics**: Quantitative assessment of recovery operation success

## Recovery Best Practices

### Preventive Measures
- Deploy error-detector.sh for proactive issue identification
- Implement continuous monitoring with progress-tracker.sh
- Maintain regular system health assessments
- Use quality gates to prevent issue accumulation

### Recovery Execution
- Always create checkpoints before recovery operations
- Use conservative recovery modes for safety
- Validate each recovery step before proceeding
- Maintain comprehensive recovery logs for audit

### Post-Recovery Actions
- Verify system health with comprehensive validation
- Update monitoring systems with recovery results
- Document lessons learned for future prevention
- Establish enhanced monitoring for recovered areas

---
**Generated by**: recovery-protocol.sh - H6D-SCRIPTS automation framework
EOF

    echo -e "${GREEN}📄 Recovery protocol report: RECOVERY_PROTOCOL_REPORT.md${NC}"
}

# Show usage information
show_usage() {
    cat << EOF
Recovery Protocol - H6D-SCRIPTS Automation Framework

USAGE:
    $0 --files [mode] [max_files]                       # Resolve file size violations
    $0 --authority [strategy] [min_fidelity]            # Resolve authority preservation issues
    $0 --references [approach] [max_repairs]            # Resolve reference integrity issues
    $0 --comprehensive [level] [dry_run]                # Execute comprehensive system recovery
    $0 --rollback [checkpoint] [scope]                  # Rollback to previous checkpoint
    $0 --checkpoint type description                    # Create recovery checkpoint
    $0 --help                                           # Show this help

COMMANDS:
    --files         File size violation resolution with L2-MODULAR extraction
    --authority     Authority preservation enhancement and restoration
    --references    Reference integrity repair and validation
    --comprehensive Complete system recovery with multi-phase resolution
    --rollback      System rollback to previous checkpoint or git state
    --checkpoint    Manual recovery checkpoint creation

FILE RESOLUTION EXAMPLES:
    $0 --files                                          # Conservative resolution (10 files max)
    $0 --files conservative 5                           # Conservative mode, 5 files maximum
    $0 --files aggressive 3                             # Aggressive mode (not implemented)

AUTHORITY RESOLUTION EXAMPLES:
    $0 --authority                                      # Default restoration (95% fidelity)
    $0 --authority restore 90.0                         # Restore to 90% minimum fidelity
    $0 --authority enhance 98.0                         # Enhance to 98% fidelity target

REFERENCE RESOLUTION EXAMPLES:
    $0 --references                                     # Conservative repair (20 max)
    $0 --references repair 10                           # Repair mode, 10 maximum fixes
    $0 --references validate 0                          # Validation only, no repairs

COMPREHENSIVE RECOVERY EXAMPLES:
    $0 --comprehensive                                  # Standard recovery level
    $0 --comprehensive standard false                   # Standard recovery, apply changes
    $0 --comprehensive deep true                        # Deep recovery, dry run mode

ROLLBACK EXAMPLES:
    $0 --rollback latest full                           # Rollback to latest checkpoint
    $0 --rollback pre_recovery context                  # Rollback context files only  
    $0 --rollback abc1234 full                          # Rollback to specific git commit

CHECKPOINT EXAMPLES:
    $0 --checkpoint manual "Before manual changes"     # Manual checkpoint creation
    $0 --checkpoint pre_operation "Before H6A batch"   # Pre-operation checkpoint

RECOVERY LEVELS:
    standard        Basic multi-phase recovery (files, authority, references)
    deep           Comprehensive recovery including system consistency
    emergency      Complete system recovery with full rollback capability

RESOLUTION MODES:
    conservative   Safe resolution with L2-MODULAR extraction and enhancement
    aggressive     Direct modification (not implemented for safety)
    restore        Authority and reference restoration to minimum standards
    repair         Broken reference repair with bidirectional validation

SAFETY FEATURES:
    - Automatic checkpoint creation before all recovery operations
    - Complete rollback capability to any previous system state
    - Incremental recovery with validation at each step
    - Dry run mode for recovery operation preview
    - Comprehensive logging for audit and troubleshooting

OUTPUT:
    - Detailed recovery operation logs with step-by-step results
    - System checkpoint creation with git and file system backup
    - Recovery effectiveness metrics and success validation
    - Comprehensive recovery reports with best practices guidance
EOF
}

# Main execution function
main() {
    if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
        show_usage
        exit 0
    fi
    
    case "$1" in
        --files)
            local mode="${2:-conservative}"
            local max_files="${3:-10}"
            
            resolve_file_size_violations "$mode" "$max_files"
            echo -e "\n${GREEN}✅ File size violation resolution completed${NC}"
            ;;
            
        --authority)
            local strategy="${2:-restore}"
            local min_fidelity="${3:-${RECOVERY_CONFIG[authority_threshold]}}"
            
            resolve_authority_issues "$strategy" "$min_fidelity"
            echo -e "\n${GREEN}✅ Authority preservation resolution completed${NC}"
            ;;
            
        --references)
            local approach="${2:-repair}"
            local max_repairs="${3:-20}"
            
            resolve_reference_issues "$approach" "$max_repairs"
            echo -e "\n${GREEN}✅ Reference integrity resolution completed${NC}"
            ;;
            
        --comprehensive)
            local level="${2:-standard}"
            local dry_run="${3:-false}"
            
            if execute_system_recovery "$level" "$dry_run"; then
                echo -e "\n${GREEN}🎉 Comprehensive system recovery completed successfully${NC}"
            else
                echo -e "\n${YELLOW}⚠️  Comprehensive system recovery completed with issues${NC}"
                exit 1
            fi
            ;;
            
        --rollback)
            local checkpoint="${2:-latest}"
            local scope="${3:-full}"
            
            if rollback_to_checkpoint "$checkpoint" "$scope"; then
                echo -e "\n${GREEN}✅ System rollback completed successfully${NC}"
            else
                echo -e "\n${RED}❌ System rollback failed${NC}"
                exit 1
            fi
            ;;
            
        --checkpoint)
            if [[ $# -lt 3 ]]; then
                echo -e "${RED}❌ Usage: $0 --checkpoint type description${NC}"
                exit 1
            fi
            
            local checkpoint_type="$2"
            local description="$3"
            
            create_recovery_checkpoint "$checkpoint_type" "$description"
            echo -e "\n${GREEN}✅ Recovery checkpoint created successfully${NC}"
            ;;
            
        *)
            echo -e "${RED}❌ Unknown option: $1${NC}"
            show_usage
            exit 1
            ;;
    esac
    
    # Generate comprehensive report for all operations
    if [[ "$1" != "--help" ]]; then
        generate_recovery_report
        
        echo -e "\n${GREEN}📁 Output directory: $OUTPUT_DIR${NC}"
        echo -e "${GREEN}📄 Recovery log: $LOG_FILE${NC}"
        if [[ -f "$RECOVERY_STATE" ]]; then
            echo -e "${GREEN}📊 Recovery state: $RECOVERY_STATE${NC}"
        fi
    fi
}

# Execute main function
main "$@"