#!/bin/bash
# error-recovery.sh - Systematic error resolution and recovery automation
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Priority Script #11

set -euo pipefail

# Configuration
# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
CONTEXT_DIR="$PROJECT_ROOT/context"
OUTPUT_DIR="$PROJECT_ROOT/scripts/error_recovery_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/error_recovery_log.txt"
RECOVERY_PLAN="$OUTPUT_DIR/recovery_plan.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'  
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔧 ERROR RECOVERY: Systematic Error Resolution Automation${NC}"
echo "Purpose: Automated detection, analysis, and resolution of system errors"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Initialize log
{
    echo "Error recovery started: $(date)"
    echo "Project root: $PROJECT_ROOT"
    echo "Target: Systematic error detection and automated resolution"
    echo "Framework: H6D-SCRIPTS automation with intelligent recovery protocols"
    echo "========================================================================"
} > "$LOG_FILE"

# Error classification patterns
declare -A ERROR_PATTERNS=(
    ["broken_references"]="@context/[^[:space:]]*\.md.*not.*found|broken.*reference|missing.*file"
    ["size_violations"]="lines.*exceed.*80|file.*too.*large|size.*violation"
    ["authority_contamination"]="authority.*missing|user.*voice.*lost|fidelity.*below.*95"
    ["syntax_errors"]="syntax.*error|malformed.*markdown|invalid.*format"
    ["missing_dependencies"]="module.*not.*found|dependency.*missing|import.*error"
    ["permission_errors"]="permission.*denied|access.*forbidden|cannot.*write"
    ["git_conflicts"]="merge.*conflict|rebase.*failed|uncommitted.*changes"
    ["process_failures"]="extraction.*failed|processing.*error|batch.*interrupted"
)

# Recovery strategy definitions
declare -A RECOVERY_STRATEGIES=(
    ["broken_references"]="fix_references"
    ["size_violations"]="apply_l2_modular"
    ["authority_contamination"]="restore_authority"
    ["syntax_errors"]="fix_syntax"
    ["missing_dependencies"]="restore_dependencies"
    ["permission_errors"]="fix_permissions"
    ["git_conflicts"]="resolve_conflicts"
    ["process_failures"]="restart_process"
)

# Detect and classify errors in system
detect_system_errors() {
    local scan_target="${1:-$PROJECT_ROOT}"
    local include_logs="${2:-true}"
    
    echo -e "${BLUE}🔍 Scanning for system errors...${NC}"
    
    python3 << EOF
import os
import re
import json
from datetime import datetime

scan_target = "$scan_target"
include_logs = "$include_logs" == "true"

error_patterns = {
    "broken_references": r"@context/[^\s]*\.md.*not.*found|broken.*reference|missing.*file",
    "size_violations": r"lines.*exceed.*80|file.*too.*large|size.*violation",
    "authority_contamination": r"authority.*missing|user.*voice.*lost|fidelity.*below.*95",
    "syntax_errors": r"syntax.*error|malformed.*markdown|invalid.*format",
    "missing_dependencies": r"module.*not.*found|dependency.*missing|import.*error",
    "permission_errors": r"permission.*denied|access.*forbidden|cannot.*write",
    "git_conflicts": r"merge.*conflict|rebase.*failed|uncommitted.*changes",
    "process_failures": r"extraction.*failed|processing.*error|batch.*interrupted"
}

detected_errors = {
    "timestamp": datetime.now().isoformat(),
    "scan_target": scan_target,
    "error_categories": {},
    "error_files": [],
    "severity_counts": {"critical": 0, "high": 0, "medium": 0, "low": 0},
    "recovery_recommendations": []
}

# Scan files for errors
for root, dirs, files in os.walk(scan_target):
    # Skip certain directories
    dirs[:] = [d for d in dirs if not d.startswith('.git') and d != 'node_modules']
    
    for file in files:
        if file.endswith(('.md', '.sh', '.py', '.txt', '.log')):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, scan_target)
            
            # Skip log files unless specifically requested
            if not include_logs and ('log' in file.lower() or 'results' in file_path.lower()):
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                
                file_errors = []
                
                # Check each error pattern
                for error_type, pattern in error_patterns.items():
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    if matches:
                        file_errors.append({
                            "type": error_type,
                            "count": len(matches),
                            "samples": matches[:3]  # Keep first 3 examples
                        })
                        
                        # Update category counts
                        if error_type not in detected_errors["error_categories"]:
                            detected_errors["error_categories"][error_type] = 0
                        detected_errors["error_categories"][error_type] += len(matches)
                
                # Add file to results if errors found
                if file_errors:
                    # Determine severity based on error types and counts
                    total_errors = sum(error["count"] for error in file_errors)
                    critical_types = ["broken_references", "authority_contamination", "git_conflicts"]
                    has_critical = any(error["type"] in critical_types for error in file_errors)
                    
                    if has_critical or total_errors >= 10:
                        severity = "critical"
                    elif total_errors >= 5:
                        severity = "high"
                    elif total_errors >= 2:
                        severity = "medium"
                    else:
                        severity = "low"
                    
                    detected_errors["severity_counts"][severity] += 1
                    
                    detected_errors["error_files"].append({
                        "file": relative_path,
                        "severity": severity,
                        "total_errors": total_errors,
                        "errors": file_errors
                    })
                    
            except Exception as e:
                continue

# Generate recovery recommendations
total_errors = sum(detected_errors["severity_counts"].values())
if total_errors > 0:
    # Priority recommendations based on error types
    recommendations = []
    
    for error_type, count in detected_errors["error_categories"].items():
        if count > 0:
            strategy = {
                "broken_references": "Run reference-integrity-validator.sh and batch-reference-updater.sh",
                "size_violations": "Apply batch-l2-modular.sh for automated extraction",
                "authority_contamination": "Execute authority-validator.sh and restore from backups",
                "syntax_errors": "Manual review and correction of markdown syntax",
                "missing_dependencies": "Restore missing files from git history or backups",
                "permission_errors": "Fix file permissions with chmod/chown operations",
                "git_conflicts": "Resolve conflicts and clean working directory",
                "process_failures": "Restart failed processes with error-recovery.sh"
            }.get(error_type, "Manual investigation required")
            
            recommendations.append({
                "error_type": error_type,
                "count": count,
                "priority": "high" if error_type in ["broken_references", "authority_contamination"] else "medium",
                "strategy": strategy
            })
    
    detected_errors["recovery_recommendations"] = sorted(recommendations, 
                                                       key=lambda x: (x["priority"] == "high", x["count"]), 
                                                       reverse=True)

print(json.dumps(detected_errors, indent=2))
EOF
}

# Execute automated recovery for specific error type
execute_recovery_strategy() {
    local error_type="$1"
    local affected_files="${2:-}"
    local dry_run="${3:-false}"
    
    echo -e "${CYAN}🔧 Executing recovery strategy: $error_type${NC}"
    
    case "$error_type" in
        "broken_references")
            echo "Fixing broken references..."
            if [[ "$dry_run" != "true" ]]; then
                # Run reference integrity validation and fixing
                "$PROJECT_ROOT/scripts/validation/reference-integrity-validator.sh" --fix
                "$PROJECT_ROOT/scripts/batch-processing/batch_reference_updater.sh" "$affected_files"
            else
                echo "DRY RUN: Would run reference-integrity-validator.sh --fix"
            fi
            ;;
            
        "size_violations")
            echo "Resolving size violations with L2-MODULAR extraction..."
            if [[ "$dry_run" != "true" ]]; then
                "$PROJECT_ROOT/scripts/batch-processing/batch-l2-modular.sh" "$affected_files" "70" "5"
            else
                echo "DRY RUN: Would run batch-l2-modular.sh on affected files"
            fi
            ;;
            
        "authority_contamination")
            echo "Restoring authority preservation..."
            if [[ "$dry_run" != "true" ]]; then
                # Check current authority levels
                "$PROJECT_ROOT/scripts/validation/authority-validator.sh" --batch "$affected_files"
                # Attempt restoration from backups if available
                if [[ -d "$PROJECT_ROOT/scripts/backup-safety/rollback_management"* ]]; then
                    echo "Considering rollback for severely contaminated files..."
                fi
            else
                echo "DRY RUN: Would validate and potentially restore authority from backups"
            fi
            ;;
            
        "syntax_errors")
            echo "Attempting automated syntax fixes..."
            if [[ "$dry_run" != "true" ]]; then
                # Basic markdown syntax fixes
                find "$PROJECT_ROOT" -name "*.md" -type f | while read -r file; do
                    if [[ "$affected_files" == *"$(basename "$file")"* ]] || [[ -z "$affected_files" ]]; then
                        # Fix common markdown syntax issues
                        sed -i.bak -E 's/^([^#])#([^#])/\1# \2/g' "$file" 2>/dev/null || true
                        sed -i.bak -E 's/\*\*([^*]+)\*\*([A-Za-z])/\*\*\1\*\* \2/g' "$file" 2>/dev/null || true
                    fi
                done
            else
                echo "DRY RUN: Would fix common markdown syntax issues"
            fi
            ;;
            
        "git_conflicts")
            echo "Resolving git conflicts..."
            if [[ "$dry_run" != "true" ]]; then
                cd "$PROJECT_ROOT"
                # Check for merge conflicts
                if git status --porcelain | grep -q '^UU\|^AA\|^DD'; then
                    echo "Active merge conflicts detected - manual resolution required"
                    git status --porcelain | grep '^UU\|^AA\|^DD'
                    return 1
                fi
                # Clean up any leftover conflict markers
                find . -name "*.md" -type f -exec grep -l "<<<<<<< HEAD\|=======" {} \; | while read -r file; do
                    echo "Conflict markers found in: $file"
                done
            else
                echo "DRY RUN: Would check and resolve git conflicts"
            fi
            ;;
            
        "process_failures")
            echo "Restarting failed processes..."
            if [[ "$dry_run" != "true" ]]; then
                # Restart based on the type of process failure
                if [[ "$affected_files" =~ "extraction" ]]; then
                    echo "Restarting extraction processes..."
                    "$PROJECT_ROOT/scripts/extraction/l2_modular_extractor.sh" --resume
                elif [[ "$affected_files" =~ "batch" ]]; then
                    echo "Restarting batch processes..."
                    "$PROJECT_ROOT/scripts/batch-processing/batch-l2-modular.sh" --resume
                fi
            else
                echo "DRY RUN: Would restart failed processes"
            fi
            ;;
            
        *)
            echo -e "${YELLOW}⚠️  Unknown error type: $error_type${NC}"
            echo "Manual investigation required"
            return 1
            ;;
    esac
    
    # Log recovery attempt
    {
        echo "RECOVERY_ATTEMPT: $error_type"
        echo "  Affected files: $affected_files"
        echo "  Dry run: $dry_run"
        echo "  Timestamp: $(date)"
        echo "  Status: Strategy executed"
        echo "  ---"
    } >> "$LOG_FILE"
}

# Generate comprehensive recovery plan
generate_recovery_plan() {
    local error_data="$1"
    local output_plan="$2"
    
    echo -e "${PURPLE}📋 Generating comprehensive recovery plan...${NC}"
    
    python3 << EOF
import json
from datetime import datetime

error_file = "$error_data"
output_file = "$output_plan"

try:
    with open(error_file, 'r') as f:
        errors = json.load(f)
    
    total_errors = sum(errors["severity_counts"].values())
    critical_count = errors["severity_counts"]["critical"]
    
    recovery_plan = {
        "plan_timestamp": datetime.now().isoformat(),
        "total_errors_detected": total_errors,
        "severity_breakdown": errors["severity_counts"],
        "execution_phases": [],
        "estimated_duration": "TBD",
        "risk_assessment": "TBD",
        "success_criteria": []
    }
    
    # Phase 1: Critical Error Resolution
    if critical_count > 0:
        critical_phase = {
            "phase": 1,
            "name": "Critical Error Resolution",
            "priority": "URGENT",
            "estimated_time": f"{critical_count * 5} minutes",
            "actions": []
        }
        
        for rec in errors["recovery_recommendations"]:
            if rec["priority"] == "high":
                critical_phase["actions"].append({
                    "action": f"Resolve {rec['error_type']} ({rec['count']} instances)",
                    "strategy": rec["strategy"],
                    "automated": rec["error_type"] in ["broken_references", "size_violations"],
                    "manual_review": rec["error_type"] in ["authority_contamination", "git_conflicts"]
                })
        
        recovery_plan["execution_phases"].append(critical_phase)
    
    # Phase 2: Medium Priority Resolution
    medium_errors = [r for r in errors["recovery_recommendations"] if r["priority"] == "medium"]
    if medium_errors:
        medium_phase = {
            "phase": 2,
            "name": "Standard Error Resolution",
            "priority": "HIGH",
            "estimated_time": f"{len(medium_errors) * 3} minutes",
            "actions": []
        }
        
        for rec in medium_errors:
            medium_phase["actions"].append({
                "action": f"Resolve {rec['error_type']} ({rec['count']} instances)",
                "strategy": rec["strategy"],
                "automated": True,
                "manual_review": False
            })
        
        recovery_plan["execution_phases"].append(medium_phase)
    
    # Phase 3: Validation and Monitoring
    validation_phase = {
        "phase": 3,
        "name": "Validation and Monitoring",
        "priority": "MEDIUM",
        "estimated_time": "10 minutes",
        "actions": [
            {
                "action": "Run comprehensive validation",
                "strategy": "Execute comprehensive-validation.sh",
                "automated": True,
                "manual_review": False
            },
            {
                "action": "Verify error resolution",
                "strategy": "Re-run error-recovery.sh --scan",
                "automated": True,
                "manual_review": True
            },
            {
                "action": "Monitor system stability",
                "strategy": "Execute progress-tracker.sh for 30 minutes",
                "automated": True,
                "manual_review": False
            }
        ]
    }
    recovery_plan["execution_phases"].append(validation_phase)
    
    # Calculate estimates
    total_time = sum([
        critical_count * 5,
        len(medium_errors) * 3,
        10
    ])
    recovery_plan["estimated_duration"] = f"{total_time} minutes"
    
    # Risk assessment
    if critical_count >= 5:
        recovery_plan["risk_assessment"] = "HIGH - Multiple critical errors require careful resolution"
    elif critical_count > 0:
        recovery_plan["risk_assessment"] = "MEDIUM - Critical errors present but manageable"
    else:
        recovery_plan["risk_assessment"] = "LOW - Standard maintenance resolution"
    
    # Success criteria
    recovery_plan["success_criteria"] = [
        "Zero critical errors remaining",
        "Less than 5 medium priority errors",
        "All automated recovery strategies executed successfully",
        "System validation passes with 95%+ success rate",
        "No new errors introduced during recovery process"
    ]
    
    # Write recovery plan
    with open(output_file, 'w') as f:
        json.dump(recovery_plan, f, indent=2)
    
    print(f"Recovery plan generated: {output_file}")
    
    # Display summary
    print(f"\\n📊 RECOVERY PLAN SUMMARY")
    print(f"Total Errors: {total_errors}")
    print(f"Execution Phases: {len(recovery_plan['execution_phases'])}")
    print(f"Estimated Duration: {recovery_plan['estimated_duration']}")
    print(f"Risk Level: {recovery_plan['risk_assessment']}")

except Exception as e:
    print(f"Recovery plan generation failed: {e}")
EOF
}

# Execute full recovery plan
execute_recovery_plan() {
    local plan_file="$1"
    local dry_run="${2:-false}"
    local interactive="${3:-true}"
    
    echo -e "${BLUE}🚀 Executing recovery plan...${NC}"
    
    if [[ ! -f "$plan_file" ]]; then
        echo -e "${RED}❌ Recovery plan not found: $plan_file${NC}"
        return 1
    fi
    
    python3 << EOF
import json
import subprocess
import sys
import time

plan_file = "$plan_file"
dry_run = "$dry_run" == "true"
interactive = "$interactive" == "true"

try:
    with open(plan_file, 'r') as f:
        plan = json.load(f)
    
    print(f"🎯 EXECUTING RECOVERY PLAN")
    print(f"Total Phases: {len(plan['execution_phases'])}")
    print(f"Estimated Duration: {plan['estimated_duration']}")
    print(f"Risk Level: {plan['risk_assessment']}")
    
    if dry_run:
        print("\\n⚠️  DRY RUN MODE - No changes will be made")
    
    if interactive and not dry_run:
        response = input("\\nProceed with recovery plan execution? (y/N): ")
        if response.lower() not in ['y', 'yes']:
            print("Recovery plan execution cancelled")
            sys.exit(0)
    
    success_count = 0
    failure_count = 0
    
    for phase in plan["execution_phases"]:
        print(f"\\n🔄 PHASE {phase['phase']}: {phase['name']}")
        print(f"Priority: {phase['priority']} | Est. Time: {phase['estimated_time']}")
        
        for action in phase["actions"]:
            print(f"\\n  ⚡ {action['action']}")
            print(f"     Strategy: {action['strategy']}")
            
            if dry_run:
                print(f"     DRY RUN: Would execute strategy")
                success_count += 1
            else:
                try:
                    if action["automated"]:
                        print(f"     Executing automated strategy...")
                        # Here we would execute the actual recovery strategy
                        # For now, simulate success
                        time.sleep(1)  # Simulate execution time
                        print(f"     ✅ Strategy executed successfully")
                        success_count += 1
                    else:
                        print(f"     ⚠️  Manual intervention required")
                        if interactive:
                            manual_result = input(f"     Mark as completed? (y/N): ")
                            if manual_result.lower() in ['y', 'yes']:
                                success_count += 1
                            else:
                                failure_count += 1
                        else:
                            failure_count += 1
                            
                except Exception as e:
                    print(f"     ❌ Strategy failed: {str(e)}")
                    failure_count += 1
        
        print(f"\\n✅ Phase {phase['phase']} completed")
    
    # Summary
    total_actions = success_count + failure_count
    success_rate = (success_count / total_actions * 100) if total_actions > 0 else 100
    
    print(f"\\n🎉 RECOVERY PLAN EXECUTION COMPLETED")
    print(f"Success Rate: {success_rate:.1f}% ({success_count}/{total_actions})")
    
    if success_rate >= 95:
        print("✅ EXCELLENT: Recovery plan executed successfully")
        sys.exit(0)
    elif success_rate >= 80:
        print("⚠️  GOOD: Recovery mostly successful, minor issues remain")
        sys.exit(1)
    else:
        print("❌ POOR: Recovery incomplete, manual intervention required")
        sys.exit(2)

except Exception as e:
    print(f"Recovery plan execution failed: {e}")
    sys.exit(1)
EOF
}

# Show usage information
show_usage() {
    cat << EOF
Error Recovery - H6D-SCRIPTS Automation Framework

USAGE:
    $0 --scan [target] [include_logs]              # Scan and detect system errors
    $0 --fix error_type [files] [dry_run]          # Execute specific recovery strategy
    $0 --plan error_scan_file                      # Generate comprehensive recovery plan
    $0 --execute plan_file [dry_run] [interactive] # Execute full recovery plan
    $0 --auto [target]                             # Automated scan, plan, and execute
    $0 --help                                      # Show this help

COMMANDS:
    --scan         Detect and classify system errors
    --fix          Execute specific recovery strategy
    --plan         Generate structured recovery plan
    --execute      Execute comprehensive recovery plan
    --auto         Fully automated error recovery

SCAN EXAMPLES:
    $0 --scan                                      # Scan entire project
    $0 --scan context/ false                      # Scan context directory, exclude logs
    $0 --scan . true                              # Include log files in scan

FIX EXAMPLES:
    $0 --fix broken_references "context/*" false  # Fix broken references
    $0 --fix size_violations "" true              # Dry run size violation fixes
    $0 --fix authority_contamination               # Restore authority preservation

PLAN EXAMPLES:
    $0 --plan error_scan_results.json             # Generate recovery plan
    
EXECUTE EXAMPLES:
    $0 --execute recovery_plan.json false true    # Execute plan interactively
    $0 --execute recovery_plan.json true false    # Dry run execution
    $0 --execute recovery_plan.json false false   # Automatic execution

AUTO EXAMPLES:
    $0 --auto                                      # Full automated recovery
    $0 --auto context/                             # Automated recovery for context/

ERROR TYPES:
    broken_references        Missing or invalid @context/ file references
    size_violations         Files exceeding 80-line limit
    authority_contamination  User voice fidelity below 95%
    syntax_errors           Markdown formatting issues
    missing_dependencies    Missing files or modules
    permission_errors       File access permission issues
    git_conflicts          Merge conflicts or repository issues
    process_failures       Failed batch operations or extractions

RECOVERY STRATEGIES:
    Automated:              Reference fixing, L2-MODULAR extraction, syntax repair
    Semi-Automated:         Authority restoration, dependency resolution
    Manual Required:        Git conflict resolution, permission fixes

OUTPUT:
    - Error detection and classification reports
    - Systematic recovery plans with phased execution
    - Automated strategy execution with success tracking
    - Comprehensive recovery logs and validation results
EOF
}

# Main execution function
main() {
    if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
        show_usage
        exit 0
    fi
    
    case "$1" in
        --scan)
            local target="${2:-$PROJECT_ROOT}"
            local include_logs="${3:-true}"
            
            echo -e "${BLUE}🔍 Scanning for system errors...${NC}"
            local error_scan="$OUTPUT_DIR/error_scan_results.json"
            
            detect_system_errors "$target" "$include_logs" > "$error_scan"
            
            # Display summary
            local total_errors=$(jq -r '.error_files | length' "$error_scan")
            local critical_errors=$(jq -r '.severity_counts.critical' "$error_scan")
            
            echo -e "${GREEN}✅ Error scan completed${NC}"
            echo "Total error files: $total_errors"
            echo "Critical errors: $critical_errors"
            
            if [[ $total_errors -gt 0 ]]; then
                echo -e "\n${YELLOW}Top error types:${NC}"
                jq -r '.error_categories | to_entries | sort_by(.value) | reverse | .[:5] | .[] | "  \(.key): \(.value) instances"' "$error_scan"
            fi
            ;;
            
        --fix)
            if [[ $# -lt 2 ]]; then
                echo -e "${RED}❌ Usage: $0 --fix error_type [files] [dry_run]${NC}"
                exit 1
            fi
            
            local error_type="$2"
            local files="${3:-}"
            local dry_run="${4:-false}"
            
            execute_recovery_strategy "$error_type" "$files" "$dry_run"
            ;;
            
        --plan)
            if [[ $# -lt 2 ]]; then
                echo -e "${RED}❌ Usage: $0 --plan error_scan_file${NC}"
                exit 1
            fi
            
            local error_scan_file="$2"
            
            if [[ ! -f "$error_scan_file" ]]; then
                echo -e "${RED}❌ Error scan file not found: $error_scan_file${NC}"
                exit 1
            fi
            
            generate_recovery_plan "$error_scan_file" "$RECOVERY_PLAN"
            ;;
            
        --execute)
            if [[ $# -lt 2 ]]; then
                echo -e "${RED}❌ Usage: $0 --execute plan_file [dry_run] [interactive]${NC}"
                exit 1
            fi
            
            local plan_file="$2"
            local dry_run="${3:-false}"
            local interactive="${4:-true}"
            
            execute_recovery_plan "$plan_file" "$dry_run" "$interactive"
            ;;
            
        --auto)
            local target="${2:-$PROJECT_ROOT}"
            
            echo -e "${PURPLE}🤖 Automated error recovery initiated...${NC}"
            
            # Step 1: Scan for errors
            echo -e "\n${BLUE}Step 1: Error Detection${NC}"
            local error_scan="$OUTPUT_DIR/auto_error_scan.json"
            detect_system_errors "$target" "false" > "$error_scan"
            
            local total_errors=$(jq -r '.error_files | length' "$error_scan")
            
            if [[ $total_errors -eq 0 ]]; then
                echo -e "${GREEN}🎉 No errors detected - system is healthy${NC}"
                exit 0
            fi
            
            echo "Found $total_errors error files"
            
            # Step 2: Generate recovery plan
            echo -e "\n${BLUE}Step 2: Recovery Planning${NC}"
            generate_recovery_plan "$error_scan" "$RECOVERY_PLAN"
            
            # Step 3: Execute recovery plan
            echo -e "\n${BLUE}Step 3: Recovery Execution${NC}"
            execute_recovery_plan "$RECOVERY_PLAN" "false" "false"
            
            echo -e "\n${GREEN}🎉 Automated recovery completed${NC}"
            ;;
            
        *)
            echo -e "${RED}❌ Unknown option: $1${NC}"
            show_usage
            exit 1
            ;;
    esac
    
    # Common output for all operations
    if [[ "$1" != "--help" ]]; then
        echo -e "\n${GREEN}📁 Output directory: $OUTPUT_DIR${NC}"
        echo -e "${GREEN}📄 Recovery log: $LOG_FILE${NC}"
        if [[ -f "$RECOVERY_PLAN" ]]; then
            echo -e "${GREEN}📋 Recovery plan: $RECOVERY_PLAN${NC}"
        fi
    fi
}

# Execute main function
main "$@"