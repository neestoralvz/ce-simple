#!/bin/bash
# progress-tracker.sh - Real-time violation monitoring and progress tracking
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Priority Script #5

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
CONTEXT_DIR="$PROJECT_ROOT/context"
OUTPUT_DIR="$PROJECT_ROOT/scripts/progress_tracking_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/progress_tracking_log.txt"
METRICS_FILE="$OUTPUT_DIR/progress_metrics.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${GREEN}📊 PROGRESS TRACKER: Real-time Violation Monitoring${NC}"
echo "Purpose: Monitor H6A/B/C progress and track compliance violations in real-time"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Initialize log
{
    echo "Progress tracking started: $(date)"
    echo "Project root: $PROJECT_ROOT"
    echo "Target: Real-time monitoring of file size violations and compliance progress"
    echo "Baseline: P0B-CLEANUP target of 157 violations → 0 violations"
    echo "=========================================================================="
} > "$LOG_FILE"

# Progress tracking thresholds
declare -A VIOLATION_THRESHOLDS=(
    ["compliant"]="80"
    ["threshold"]="90"
    ["medium"]="200"
    ["high"]="400"
)

declare -A PROGRESS_TARGETS=(
    ["p0b_total"]="157"
    ["h6a_target"]="48"
    ["h6b_target"]="36"
    ["h6c_target"]="73"
    ["baseline_total"]="600"
)

# Scan files and categorize violations
scan_current_violations() {
    local scan_dir="${1:-$PROJECT_ROOT}"
    local include_all="${2:-false}"
    
    python3 << EOF
import os
import json
from datetime import datetime

scan_dir = "$scan_dir"
include_all = "$include_all" == "true"

violations = {
    "compliant": [],      # ≤80 lines
    "threshold": [],      # 81-90 lines  
    "medium": [],         # 91-200 lines
    "high": [],           # 201-400 lines
    "critical": []        # >400 lines
}

scan_results = {
    "timestamp": datetime.now().isoformat(),
    "scan_directory": scan_dir,
    "total_files": 0,
    "violations": violations,
    "summary": {},
    "progress_metrics": {}
}

# Scan for markdown files
for root, dirs, files in os.walk(scan_dir):
    # Skip certain directories unless include_all is true
    if not include_all:
        dirs[:] = [d for d in dirs if not d.startswith('.git') and d != 'node_modules' and 'results' not in d]
    
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, scan_dir)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    line_count = len(f.readlines())
                
                scan_results["total_files"] += 1
                
                # Categorize by violation level
                if line_count <= 80:
                    violations["compliant"].append({"file": relative_path, "lines": line_count})
                elif line_count <= 90:
                    violations["threshold"].append({"file": relative_path, "lines": line_count})
                elif line_count <= 200:
                    violations["medium"].append({"file": relative_path, "lines": line_count})
                elif line_count <= 400:
                    violations["high"].append({"file": relative_path, "lines": line_count})
                else:
                    violations["critical"].append({"file": relative_path, "lines": line_count})
                    
            except Exception as e:
                continue

# Calculate summary statistics
scan_results["summary"] = {
    "compliant_count": len(violations["compliant"]),
    "threshold_count": len(violations["threshold"]),
    "medium_count": len(violations["medium"]),
    "high_count": len(violations["high"]),
    "critical_count": len(violations["critical"]),
    "total_violations": len(violations["threshold"]) + len(violations["medium"]) + 
                       len(violations["high"]) + len(violations["critical"]),
    "compliance_rate": round((len(violations["compliant"]) / scan_results["total_files"]) * 100, 1) if scan_results["total_files"] > 0 else 0
}

# Calculate progress metrics against targets
targets = {
    "p0b_total": ${PROGRESS_TARGETS[p0b_total]},
    "h6a_target": ${PROGRESS_TARGETS[h6a_target]},
    "h6b_target": ${PROGRESS_TARGETS[h6b_target]},
    "h6c_target": ${PROGRESS_TARGETS[h6c_target]},
    "baseline_total": ${PROGRESS_TARGETS[baseline_total]}
}

current_violations = scan_results["summary"]["total_violations"]
scan_results["progress_metrics"] = {
    "current_violations": current_violations,
    "p0b_progress": round(((targets["p0b_total"] - current_violations) / targets["p0b_total"]) * 100, 1) if current_violations <= targets["p0b_total"] else 100,
    "baseline_progress": round(((targets["baseline_total"] - current_violations) / targets["baseline_total"]) * 100, 1),
    "h6a_eligible": len(violations["threshold"]),
    "h6b_eligible": len(violations["medium"]),
    "h6c_eligible": len(violations["high"]) + len(violations["critical"]),
    "target_compliance": current_violations == 0
}

# Output results
print(json.dumps(scan_results, indent=2))
EOF
}

# Compare progress against previous scan
compare_progress() {
    local current_scan="$1"
    local previous_scan="${2:-}"
    
    if [[ -z "$previous_scan" ]] || [[ ! -f "$previous_scan" ]]; then
        echo "NO_COMPARISON:No previous scan for comparison"
        return 0
    fi
    
    python3 << EOF
import json
from datetime import datetime

current_file = "$current_scan"
previous_file = "$previous_scan"

try:
    with open(current_file, 'r') as f:
        current_data = json.load(f)
    
    with open(previous_file, 'r') as f:
        previous_data = json.load(f)
    
    # Calculate changes
    current_violations = current_data["summary"]["total_violations"]
    previous_violations = previous_data["summary"]["total_violations"]
    
    violation_change = current_violations - previous_violations
    
    current_compliance = current_data["summary"]["compliance_rate"]
    previous_compliance = previous_data["summary"]["compliance_rate"]
    
    compliance_change = current_compliance - previous_compliance
    
    # Progress direction
    if violation_change < 0:
        direction = "IMPROVED"
        direction_symbol = "📈"
    elif violation_change > 0:
        direction = "REGRESSED"
        direction_symbol = "📉"
    else:
        direction = "STABLE"
        direction_symbol = "➡️"
    
    comparison = {
        "comparison_timestamp": datetime.now().isoformat(),
        "current_violations": current_violations,
        "previous_violations": previous_violations,
        "violation_change": violation_change,
        "current_compliance": current_compliance,
        "previous_compliance": previous_compliance,
        "compliance_change": round(compliance_change, 1),
        "direction": direction,
        "direction_symbol": direction_symbol
    }
    
    print(json.dumps(comparison, indent=2))

except Exception as e:
    print(f'{{"error": "Comparison failed: {str(e)}"}}')
EOF
}

# Generate progress visualization
generate_progress_visualization() {
    local scan_data="$1"
    
    python3 << EOF
import json

scan_file = "$scan_data"

try:
    with open(scan_file, 'r') as f:
        data = json.load(f)
    
    summary = data["summary"]
    metrics = data["progress_metrics"]
    
    print("\\n" + "="*80)
    print("📊 VIOLATION BREAKDOWN")
    print("="*80)
    
    # Violation categories with progress bars
    categories = [
        ("✅ Compliant (≤80)", summary["compliant_count"], "GREEN"),
        ("⚠️  Threshold (81-90)", summary["threshold_count"], "YELLOW"),
        ("🔶 Medium (91-200)", summary["medium_count"], "ORANGE"),
        ("🔴 High (201-400)", summary["high_count"], "RED"),
        ("🚨 Critical (>400)", summary["critical_count"], "CRITICAL")
    ]
    
    total_files = data["total_files"]
    max_category_length = max(len(cat[0]) for cat in categories)
    
    for category, count, color in categories:
        percentage = (count / total_files * 100) if total_files > 0 else 0
        bar_length = int(percentage / 2)  # Scale to 50 chars max
        bar = "█" * bar_length + "░" * (50 - bar_length)
        
        print(f"{category:<{max_category_length}} │ {bar} │ {count:4d} files ({percentage:5.1f}%)")
    
    print("="*80)
    print(f"📈 PROGRESS METRICS")
    print("="*80)
    print(f"Total Files Scanned: {total_files:,}")
    print(f"Current Violations: {metrics['current_violations']:,}")
    print(f"Compliance Rate: {summary['compliance_rate']}%")
    print(f"P0B Progress: {metrics['p0b_progress']}%")
    print(f"Baseline Progress: {metrics['baseline_progress']}%")
    
    # Handoff eligibility
    print("\\n🎯 HANDOFF ELIGIBILITY")
    print("-"*40)
    print(f"H6A-Ready (Threshold): {metrics['h6a_eligible']} files")
    print(f"H6B-Ready (Medium): {metrics['h6b_eligible']} files")
    print(f"H6C-Ready (High+Critical): {metrics['h6c_eligible']} files")
    
    # Progress status
    if metrics["target_compliance"]:
        print("\\n🎉 STATUS: TARGET ACHIEVED - Zero violations!")
    elif metrics["p0b_progress"] >= 75:
        print(f"\\n🚀 STATUS: Excellent progress ({metrics['p0b_progress']}% complete)")
    elif metrics["p0b_progress"] >= 50:
        print(f"\\n📊 STATUS: Good progress ({metrics['p0b_progress']}% complete)")
    elif metrics["p0b_progress"] >= 25:
        print(f"\\n⏳ STATUS: Moderate progress ({metrics['p0b_progress']}% complete)")
    else:
        print(f"\\n🔄 STATUS: Early stage ({metrics['p0b_progress']}% complete)")

except Exception as e:
    print(f"Visualization error: {e}")
EOF
}

# Monitor progress continuously
monitor_continuous() {
    local scan_interval="${1:-300}"  # 5 minutes default
    local max_iterations="${2:-0}"   # 0 = infinite
    local target_dir="${3:-$PROJECT_ROOT}"
    
    echo -e "${BLUE}🔄 Starting continuous monitoring...${NC}"
    echo "Scan interval: ${scan_interval}s"
    echo "Target directory: $target_dir"
    
    local iteration=0
    local previous_scan=""
    
    while [[ $max_iterations -eq 0 ]] || [[ $iteration -lt $max_iterations ]]; do
        ((iteration++))
        
        echo -e "\n${CYAN}[$(date)] Scan #${iteration}${NC}"
        
        # Perform current scan
        local current_scan="$OUTPUT_DIR/scan_${iteration}_$(date +%H%M%S).json"
        scan_current_violations "$target_dir" "false" > "$current_scan"
        
        # Display current status
        generate_progress_visualization "$current_scan"
        
        # Compare with previous scan if available
        if [[ -n "$previous_scan" ]] && [[ -f "$previous_scan" ]]; then
            echo -e "\n${PURPLE}📈 PROGRESS COMPARISON:${NC}"
            local comparison=$(compare_progress "$current_scan" "$previous_scan")
            
            if [[ "$comparison" != "NO_COMPARISON"* ]]; then
                local direction=$(echo "$comparison" | jq -r '.direction // "UNKNOWN"')
                local violation_change=$(echo "$comparison" | jq -r '.violation_change // 0')
                local compliance_change=$(echo "$comparison" | jq -r '.compliance_change // 0')
                
                case "$direction" in
                    "IMPROVED")
                        echo -e "${GREEN}📈 IMPROVEMENT: $violation_change violations resolved (+${compliance_change}% compliance)${NC}"
                        ;;
                    "REGRESSED")
                        echo -e "${RED}📉 REGRESSION: +$violation_change violations (${compliance_change}% compliance)${NC}"
                        ;;
                    "STABLE")
                        echo -e "${YELLOW}➡️  STABLE: No change in violations${NC}"
                        ;;
                esac
            fi
        fi
        
        # Log iteration
        {
            echo "[$(date)] Scan #${iteration} completed"
            echo "  Violations: $(jq -r '.summary.total_violations' "$current_scan")"
            echo "  Compliance: $(jq -r '.summary.compliance_rate' "$current_scan")%"
            echo "  P0B Progress: $(jq -r '.progress_metrics.p0b_progress' "$current_scan")%"
            echo "  ---"
        } >> "$LOG_FILE"
        
        # Save as latest scan for comparison
        previous_scan="$current_scan"
        
        # Check if target achieved
        local target_achieved=$(jq -r '.progress_metrics.target_compliance' "$current_scan")
        if [[ "$target_achieved" == "true" ]]; then
            echo -e "\n${GREEN}🎉 TARGET ACHIEVED: Zero violations detected!${NC}"
            break
        fi
        
        # Wait for next iteration
        if [[ $max_iterations -eq 0 ]] || [[ $iteration -lt $max_iterations ]]; then
            echo -e "\n${BLUE}⏰ Next scan in ${scan_interval}s... (Ctrl+C to stop)${NC}"
            sleep "$scan_interval"
        fi
    done
    
    echo -e "\n${GREEN}✅ Continuous monitoring completed${NC}"
}

# Generate detailed progress report
generate_progress_report() {
    local scan_data="$1"
    local comparison_data="${2:-}"
    local report_file="$OUTPUT_DIR/PROGRESS_TRACKING_REPORT.md"
    
    python3 << EOF
import json
from datetime import datetime

scan_file = "$scan_data"
comparison_file = "$comparison_data"
report_file = "$report_file"

try:
    with open(scan_file, 'r') as f:
        scan_data = json.load(f)
    
    comparison_data = None
    if comparison_file and comparison_file != "":
        try:
            with open(comparison_file, 'r') as f:
                comparison_data = json.load(f)
        except:
            pass
    
    with open(report_file, 'w') as f:
        f.write(f'''# Progress Tracking Report

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Script**: progress-tracker.sh
**Purpose**: Real-time violation monitoring and progress tracking

## Current Status Summary

### Violation Breakdown
- **✅ Compliant (≤80 lines)**: {scan_data["summary"]["compliant_count"]} files
- **⚠️ Threshold (81-90 lines)**: {scan_data["summary"]["threshold_count"]} files  
- **🔶 Medium (91-200 lines)**: {scan_data["summary"]["medium_count"]} files
- **🔴 High (201-400 lines)**: {scan_data["summary"]["high_count"]} files
- **🚨 Critical (>400 lines)**: {scan_data["summary"]["critical_count"]} files

### Progress Metrics
- **Total Files**: {scan_data["total_files"]:,}
- **Current Violations**: {scan_data["progress_metrics"]["current_violations"]:,}
- **Compliance Rate**: {scan_data["summary"]["compliance_rate"]}%
- **P0B Progress**: {scan_data["progress_metrics"]["p0b_progress"]}%
- **Baseline Progress**: {scan_data["progress_metrics"]["baseline_progress"]}%

### Handoff Readiness
- **H6A-Ready** (Quick wins): {scan_data["progress_metrics"]["h6a_eligible"]} files
- **H6B-Ready** (L2-MODULAR): {scan_data["progress_metrics"]["h6b_eligible"]} files
- **H6C-Ready** (Individual): {scan_data["progress_metrics"]["h6c_eligible"]} files

''')
        
        if comparison_data:
            f.write(f'''## Progress Comparison

### Change Analysis
- **Violation Change**: {comparison_data.get("violation_change", "N/A")}
- **Compliance Change**: {comparison_data.get("compliance_change", "N/A")}%
- **Progress Direction**: {comparison_data.get("direction", "N/A")} {comparison_data.get("direction_symbol", "")}

''')
        
        # Target files by category
        if scan_data["violations"]["threshold"]:
            f.write("### H6A-Ready Files (Threshold 81-90 lines)\\n")
            for file_info in scan_data["violations"]["threshold"][:10]:  # Top 10
                f.write(f"- {file_info['file']} ({file_info['lines']} lines)\\n")
            if len(scan_data["violations"]["threshold"]) > 10:
                f.write(f"- ... and {len(scan_data['violations']['threshold']) - 10} more\\n")
            f.write("\\n")
        
        if scan_data["violations"]["medium"]:
            f.write("### H6B-Ready Files (Medium 91-200 lines)\\n")
            for file_info in scan_data["violations"]["medium"][:10]:  # Top 10
                f.write(f"- {file_info['file']} ({file_info['lines']} lines)\\n")
            if len(scan_data["violations"]["medium"]) > 10:
                f.write(f"- ... and {len(scan_data['violations']['medium']) - 10} more\\n")
            f.write("\\n")
        
        f.write(f'''## Monitoring Recommendations

''')
        
        compliance_rate = scan_data["summary"]["compliance_rate"]
        if compliance_rate >= 95:
            f.write("- **Excellent**: System compliance is excellent, maintain current progress\\n")
        elif compliance_rate >= 85:
            f.write("- **Good**: Good progress, focus on remaining violations\\n")
        elif compliance_rate >= 70:
            f.write("- **Moderate**: Systematic approach needed for remaining violations\\n")
        else:
            f.write("- **Attention**: Significant violations remain, prioritize systematic resolution\\n")
        
        f.write(f'''
### Automation Opportunities
- Use domain-classifier.sh to categorize remaining violations
- Apply batch-l2-modular.sh for pattern-based processing
- Implement authority-validator.sh for quality assurance
- Deploy cross-reference-updater.sh for link maintenance

---
**Generated by**: progress-tracker.sh - H6D-SCRIPTS automation framework
''')
    
    print(f"Progress report generated: {report_file}")

except Exception as e:
    print(f"Report generation failed: {e}")
EOF
}

# Show usage information
show_usage() {
    cat << EOF
Progress Tracker - H6D-SCRIPTS Automation Framework

USAGE:
    $0 --scan [directory] [include_all]         # Single progress scan
    $0 --monitor [interval] [max_iter] [dir]    # Continuous monitoring
    $0 --compare current previous               # Compare two scans
    $0 --report scan_file [comparison_file]     # Generate detailed report
    $0 --help                                   # Show this help

COMMANDS:
    --scan         Perform single violation scan and progress assessment
    --monitor      Continuous monitoring with configurable interval
    --compare      Compare progress between two scan results
    --report       Generate comprehensive progress report

SCAN EXAMPLES:
    $0 --scan                                    # Scan entire project
    $0 --scan context/ false                     # Scan context directory only
    $0 --scan . true                            # Include all files (including results)

MONITOR EXAMPLES:
    $0 --monitor                                # Monitor every 5 minutes indefinitely
    $0 --monitor 120 10                         # Monitor every 2 minutes for 10 iterations
    $0 --monitor 60 0 context/                  # Monitor context/ every minute indefinitely

COMPARE EXAMPLES:
    $0 --compare current_scan.json previous_scan.json
    $0 --compare scan_1.json scan_2.json

REPORT EXAMPLES:
    $0 --report scan_results.json               # Basic progress report
    $0 --report current.json previous.json      # Report with comparison

VIOLATION CATEGORIES:
    ✅ Compliant (≤80):     Target compliance achieved
    ⚠️ Threshold (81-90):   H6A-Ready (quick wins)
    🔶 Medium (91-200):     H6B-Ready (L2-MODULAR candidates)
    🔴 High (201-400):      H6C-Ready (individual assessment)
    🚨 Critical (>400):     H6C-Ready (priority individual assessment)

PROGRESS TARGETS:
    P0B Total Target: 157 violations → 0 violations (100% compliance)
    Baseline Progress: ~600 violations → current violations
    Handoff Distribution: H6A(48) + H6B(36) + H6C(73) = 157 target

OUTPUT:
    - Real-time violation counts and progress percentages
    - Handoff readiness assessment and file categorization
    - Progress comparison and trend analysis
    - Comprehensive progress reports with actionable recommendations
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
            local target_dir="${2:-$PROJECT_ROOT}"
            local include_all="${3:-false}"
            
            echo -e "${BLUE}🔍 Performing progress scan...${NC}"
            local scan_result="$OUTPUT_DIR/current_scan.json"
            
            scan_current_violations "$target_dir" "$include_all" > "$scan_result"
            
            echo -e "${GREEN}✅ Scan completed${NC}"
            generate_progress_visualization "$scan_result"
            
            # Save metrics for continuous use
            cp "$scan_result" "$METRICS_FILE"
            ;;
            
        --monitor)
            local interval="${2:-300}"
            local max_iter="${3:-0}"
            local target_dir="${4:-$PROJECT_ROOT}"
            
            monitor_continuous "$interval" "$max_iter" "$target_dir"
            ;;
            
        --compare)
            if [[ $# -lt 3 ]]; then
                echo -e "${RED}❌ Usage: $0 --compare current_scan previous_scan${NC}"
                exit 1
            fi
            
            local current_scan="$2"
            local previous_scan="$3"
            
            if [[ ! -f "$current_scan" ]]; then
                echo -e "${RED}❌ Current scan file not found: $current_scan${NC}"
                exit 1
            fi
            
            if [[ ! -f "$previous_scan" ]]; then
                echo -e "${RED}❌ Previous scan file not found: $previous_scan${NC}"
                exit 1
            fi
            
            echo -e "${BLUE}📊 Comparing progress...${NC}"
            local comparison_result="$OUTPUT_DIR/comparison_result.json"
            
            compare_progress "$current_scan" "$previous_scan" > "$comparison_result"
            
            # Display comparison results
            local direction=$(jq -r '.direction // "UNKNOWN"' "$comparison_result")
            local violation_change=$(jq -r '.violation_change // 0' "$comparison_result")
            
            case "$direction" in
                "IMPROVED")
                    echo -e "${GREEN}📈 IMPROVEMENT: $violation_change violations resolved${NC}"
                    ;;
                "REGRESSED")
                    echo -e "${RED}📉 REGRESSION: +$violation_change violations${NC}"
                    ;;
                "STABLE")
                    echo -e "${YELLOW}➡️  STABLE: No change in violations${NC}"
                    ;;
            esac
            ;;
            
        --report)
            if [[ $# -lt 2 ]]; then
                echo -e "${RED}❌ Usage: $0 --report scan_file [comparison_file]${NC}"
                exit 1
            fi
            
            local scan_file="$2"
            local comparison_file="${3:-}"
            
            if [[ ! -f "$scan_file" ]]; then
                echo -e "${RED}❌ Scan file not found: $scan_file${NC}"
                exit 1
            fi
            
            echo -e "${BLUE}📄 Generating progress report...${NC}"
            generate_progress_report "$scan_file" "$comparison_file"
            
            echo -e "${GREEN}✅ Progress report generated${NC}"
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
        echo -e "${GREEN}📄 Tracking log: $LOG_FILE${NC}"
        if [[ -f "$METRICS_FILE" ]]; then
            echo -e "${GREEN}📊 Latest metrics: $METRICS_FILE${NC}"
        fi
    fi
}

# Execute main function
main "$@"