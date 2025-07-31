#!/bin/bash
# validation-protocols.sh - Comprehensive validation framework with systematic protocols
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Error Handling Script #3

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
OUTPUT_DIR="$PROJECT_ROOT/scripts/validation_protocols_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/validation_protocols_log.txt"
VALIDATION_DB="$OUTPUT_DIR/validation_database.json" 

# Colors for output
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'
PURPLE='\033[0;35m'; CYAN='\033[0;36m'; NC='\033[0m'

echo -e "${GREEN}🎯 VALIDATION PROTOCOLS: Comprehensive Validation Framework${NC}"
mkdir -p "$OUTPUT_DIR"

# Initialize log
{
    echo "Validation protocols started: $(date)"
    echo "Project root: $PROJECT_ROOT"
    echo "Target: Comprehensive validation framework for H6D scripts ecosystem"
    echo "Authority: @context/architecture/standards/quality-assurance.md"
    echo "=============================================================================="
} > "$LOG_FILE"

# Validation protocol definitions
declare -A VALIDATION_PROTOCOLS=(
    ["file_integrity"]="File structure, encoding, and accessibility validation"
    ["content_quality"]="User authority preservation and content fidelity validation"
    ["reference_consistency"]="Cross-reference integrity and bidirectional link validation"
    ["size_compliance"]="File size limits and L2-MODULAR compliance validation"
    ["script_functionality"]="Script execution and automation framework validation"
    ["system_coherence"]="Overall system integrity and workflow validation"
)

# Execute comprehensive validation protocol
execute_validation_protocol() {
    local protocol_name="$1"
    local validation_scope="${2:-comprehensive}"
    local output_format="${3:-detailed}"
    
    echo -e "${BLUE}🔍 Executing validation protocol: ${protocol_name}${NC}"
    
    python3 << EOF
import os
import json
import re
import subprocess
from datetime import datetime

protocol_name = "$protocol_name"
validation_scope = "$validation_scope"
output_format = "$output_format"
project_root = "$PROJECT_ROOT"

validation_result = {
    "protocol": protocol_name,
    "scope": validation_scope,
    "timestamp": datetime.now().isoformat(),
    "status": "unknown",
    "score": 0,
    "max_score": 100,
    "findings": [],
    "recommendations": [],
    "execution_time": 0
}

start_time = datetime.now()

def validate_file_integrity():
    """Validate file structure, encoding, and accessibility"""
    findings = []
    score = 100
    
    for root, dirs, files in os.walk(project_root):
        # Skip certain directories
        skip_dirs = {'.git', 'node_modules', 'scripts'}
        dirs[:] = [d for d in dirs if not any(skip in d for skip in skip_dirs)]
        
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_root)
                
                try:
                    # Test file accessibility
                    if not os.access(file_path, os.R_OK):
                        findings.append({
                            "type": "access_error",
                            "file": relative_path,
                            "severity": "high",
                            "description": "File not readable"
                        })
                        score -= 5
                        continue
                    
                    # Test encoding
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Check for encoding issues
                    if '\\ufffd' in content or '\\x00' in content:
                        findings.append({
                            "type": "encoding_error",
                            "file": relative_path,
                            "severity": "medium",
                            "description": "File contains encoding issues or null bytes"
                        })
                        score -= 3
                    
                    # Check for empty files
                    if len(content.strip()) == 0:
                        findings.append({
                            "type": "empty_file",
                            "file": relative_path,
                            "severity": "low",
                            "description": "File is empty"
                        })
                        score -= 1
                    
                    # Check for proper markdown structure
                    if not content.startswith('#') and len(content.strip()) > 10:
                        findings.append({
                            "type": "structure_warning",
                            "file": relative_path,
                            "severity": "low",
                            "description": "File may be missing title header"
                        })
                        score -= 1
                        
                except UnicodeDecodeError:
                    findings.append({
                        "type": "encoding_error",
                        "file": relative_path,
                        "severity": "high",
                        "description": "File has invalid UTF-8 encoding"
                    })
                    score -= 5
                except Exception as e:
                    findings.append({
                        "type": "access_error",
                        "file": relative_path,
                        "severity": "medium",
                        "description": f"File access error: {str(e)}"
                    })
                    score -= 3
    
    return max(0, score), findings

def validate_content_quality():
    """Validate user authority preservation and content fidelity"""
    findings = []
    score = 100
    
    authority_files = 0
    high_fidelity_files = 0
    
    for root, dirs, files in os.walk(os.path.join(project_root, 'context')):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_root)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Check for authority markers
                    has_authority = any(marker in content.upper() for marker in 
                                     ['AUTORIDAD', 'SUPREMA', 'AUTHORITY', 'SUPREME'])
                    
                    if has_authority:
                        authority_files += 1
                        
                        # Assess fidelity markers
                        user_quotes = len(re.findall(r'[">][^"<\\n]{10,}["><]', content))
                        spanish_markers = len(re.findall(r'(autoridad|suprema|usuario|visión|metodología)', 
                                                       content, re.IGNORECASE))
                        authority_declarations = len(re.findall(r'\\*\\*[^*]*(AUTORIDAD|SUPREMA)[^*]*\\*\\*', 
                                                              content, re.IGNORECASE))
                        
                        fidelity_score = (user_quotes * 15) + (spanish_markers * 5) + (authority_declarations * 10)
                        
                        if fidelity_score >= 95:
                            high_fidelity_files += 1
                        elif fidelity_score < 50:
                            findings.append({
                                "type": "low_fidelity",
                                "file": relative_path,
                                "severity": "high",
                                "description": f"Low authority fidelity score: {fidelity_score}"
                            })
                            score -= 10
                        elif fidelity_score < 75:
                            findings.append({
                                "type": "medium_fidelity",
                                "file": relative_path,
                                "severity": "medium",
                                "description": f"Medium authority fidelity score: {fidelity_score}"
                            })
                            score -= 5
                    
                    # Check for proper authority sections
                    if has_authority and '## AUTORIDAD SUPREMA' not in content:
                        findings.append({
                            "type": "missing_authority_section",
                            "file": relative_path,
                            "severity": "medium",
                            "description": "Authority file missing AUTORIDAD SUPREMA section"
                        })
                        score -= 5
                        
                except Exception:
                    continue
    
    # Overall authority preservation assessment
    if authority_files > 0:
        fidelity_rate = (high_fidelity_files / authority_files) * 100
        if fidelity_rate < 90:
            findings.append({
                "type": "system_fidelity",
                "file": "system_wide",
                "severity": "high",
                "description": f"System authority fidelity rate: {fidelity_rate:.1f}% (target: ≥95%)"
            })
            score -= 15
    
    return max(0, score), findings

def validate_reference_consistency():
    """Validate cross-reference integrity and bidirectional links"""
    findings = []
    score = 100
    
    total_refs = 0
    broken_refs = 0
    
    for root, dirs, files in os.walk(project_root):
        skip_dirs = {'.git', 'node_modules'}
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_root)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Find @context/ references
                    refs = re.findall(r'@[a-zA-Z0-9/_.-]+', content)
                    
                    for ref in refs:
                        total_refs += 1
                        ref_path = os.path.join(project_root, ref[1:])  # Remove @
                        
                        if not os.path.exists(ref_path):
                            broken_refs += 1
                            findings.append({
                                "type": "broken_reference",
                                "file": relative_path,
                                "severity": "medium",
                                "description": f"Broken reference: {ref}"
                            })
                            score -= 3
                    
                    # Check reference format compliance
                    non_context_refs = [ref for ref in refs if not ref.startswith('@context/')]
                    if non_context_refs:
                        findings.append({
                            "type": "reference_format",
                            "file": relative_path,
                            "severity": "low",
                            "description": f"Non-standard references: {len(non_context_refs)}"
                        })
                        score -= 2
                        
                except Exception:
                    continue
    
    # Overall reference integrity
    if total_refs > 0:
        integrity_rate = ((total_refs - broken_refs) / total_refs) * 100
        if integrity_rate < 95:
            findings.append({
                "type": "system_integrity",
                "file": "system_wide",
                "severity": "high",
                "description": f"Reference integrity: {integrity_rate:.1f}% (target: ≥98%)"
            })
            score -= 20
    
    return max(0, score), findings

def validate_size_compliance():
    """Validate file size limits and L2-MODULAR compliance"""
    findings = []
    score = 100
    
    total_files = 0
    violations = 0
    
    for root, dirs, files in os.walk(project_root):
        skip_dirs = {'.git', 'node_modules'}
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_root)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        line_count = len(f.readlines())
                    
                    total_files += 1
                    
                    if line_count > 80:
                        violations += 1
                        
                        if line_count > 200:
                            severity = "high"
                            score_deduction = 10
                        elif line_count > 120:
                            severity = "medium"
                            score_deduction = 5
                        else:
                            severity = "low"
                            score_deduction = 2
                        
                        findings.append({
                            "type": "size_violation",
                            "file": relative_path,
                            "severity": severity,
                            "description": f"File size: {line_count} lines (limit: 80)"
                        })
                        score -= score_deduction
                        
                except Exception:
                    continue
    
    # Overall compliance rate
    if total_files > 0:
        compliance_rate = ((total_files - violations) / total_files) * 100
        if compliance_rate < 90:
            findings.append({
                "type": "system_compliance",
                "file": "system_wide",
                "severity": "high",
                "description": f"System compliance: {compliance_rate:.1f}% (target: ≥95%)"
            })
            score -= 15
    
    return max(0, score), findings

def validate_script_functionality():
    """Validate script execution and automation framework"""
    findings = []
    score = 100
    
    scripts_dir = os.path.join(project_root, 'scripts')
    if not os.path.exists(scripts_dir):
        findings.append({
            "type": "missing_scripts",
            "file": "scripts/",
            "severity": "critical",
            "description": "Scripts directory does not exist"
        })
        return 0, findings
    
    # Check key H6D scripts
    key_scripts = [
        'analysis/domain-classifier.sh',
        'batch-processing/batch-l2-modular.sh',
        'validation/authority-validator.sh',
        'validation/reference-integrity-validator.sh',
        'validation/quality-gate-validator.sh',
        'infrastructure/progress-tracker.sh',
        'infrastructure/success-metrics-tracker.sh',
        'backup-safety/rollback-manager.sh',
        'validation/error-recovery.sh',
        'validation/validation-protocols.sh'
    ]
    
    missing_scripts = 0
    non_executable = 0
    
    for script_path in key_scripts:
        full_path = os.path.join(scripts_dir, script_path)
        
        if not os.path.exists(full_path):
            missing_scripts += 1
            findings.append({
                "type": "missing_script",
                "file": script_path,
                "severity": "high",
                "description": "Key H6D script missing"
            })
            score -= 10
        elif not os.access(full_path, os.X_OK):
            non_executable += 1
            findings.append({
                "type": "non_executable",
                "file": script_path,
                "severity": "medium",
                "description": "Script not executable"
            })
            score -= 5
    
    # Framework completeness
    framework_completeness = ((len(key_scripts) - missing_scripts) / len(key_scripts)) * 100
    if framework_completeness < 90:
        findings.append({
            "type": "framework_incomplete",
            "file": "scripts/",
            "severity": "critical",
            "description": f"Framework completeness: {framework_completeness:.1f}% (target: 100%)"
        })
        score -= 25
    
    return max(0, score), findings

def validate_system_coherence():
    """Validate overall system integrity and workflow coherence"""
    findings = []
    score = 100
    
    # Check for required system files
    required_files = [
        'CLAUDE.md',
        'context/vision/vision_foundation.md',
        'context/architecture/core/truth-source.md',
        'context/architecture/core/authority.md',
        'context/architecture/core/methodology.md'
    ]
    
    for req_file in required_files:
        full_path = os.path.join(project_root, req_file)
        if not os.path.exists(full_path):
            findings.append({
                "type": "missing_core_file",
                "file": req_file,
                "severity": "critical",
                "description": "Required system file missing"
            })
            score -= 15
    
    # Check for system coherence indicators
    try:
        claude_path = os.path.join(project_root, 'CLAUDE.md')
        if os.path.exists(claude_path):
            with open(claude_path, 'r', encoding='utf-8') as f:
                claude_content = f.read()
            
            # Check for key coherence elements
            coherence_elements = [
                'AUTORIDAD SUPREMA',
                '@context/architecture/core/truth-source.md',
                'semantic triggers',
                'conditional loading'
            ]
            
            missing_elements = []
            for element in coherence_elements:
                if element not in claude_content:
                    missing_elements.append(element)
            
            if missing_elements:
                findings.append({
                    "type": "coherence_elements",
                    "file": "CLAUDE.md",
                    "severity": "high",
                    "description": f"Missing coherence elements: {', '.join(missing_elements)}"
                })
                score -= len(missing_elements) * 5
                
    except Exception:
        pass
    
    return max(0, score), findings

# Execute the requested protocol
if protocol_name == "file_integrity":
    score, findings = validate_file_integrity()
elif protocol_name == "content_quality":
    score, findings = validate_content_quality()
elif protocol_name == "reference_consistency":
    score, findings = validate_reference_consistency()
elif protocol_name == "size_compliance":
    score, findings = validate_size_compliance()
elif protocol_name == "script_functionality":
    score, findings = validate_script_functionality()
elif protocol_name == "system_coherence":
    score, findings = validate_system_coherence()
else:
    score = 0
    findings = [{
        "type": "unknown_protocol",
        "file": "system",
        "severity": "critical",
        "description": f"Unknown validation protocol: {protocol_name}"
    }]

# Finalize validation result
validation_result["score"] = score
validation_result["findings"] = findings

# Determine status
if score >= 95:
    validation_result["status"] = "excellent"
elif score >= 85:
    validation_result["status"] = "good"
elif score >= 70:
    validation_result["status"] = "acceptable"
elif score >= 50:
    validation_result["status"] = "poor"
else:
    validation_result["status"] = "critical"

# Generate recommendations
recommendations = []
severity_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}

for finding in findings:
    severity = finding.get("severity", "medium")
    severity_counts[severity] += 1

if severity_counts["critical"] > 0:
    recommendations.append("URGENT: Address critical issues immediately")
if severity_counts["high"] > 5:
    recommendations.append("HIGH PRIORITY: Systematic resolution of high-severity issues needed")
if score < 85:
    recommendations.append("IMPROVEMENT: Consider systematic validation and remediation")
if score >= 95:
    recommendations.append("EXCELLENT: Maintain current quality standards")

validation_result["recommendations"] = recommendations

# Calculate execution time
end_time = datetime.now()
execution_time = (end_time - start_time).total_seconds()
validation_result["execution_time"] = round(execution_time, 2)

# Output results
print(json.dumps(validation_result, indent=2))
EOF
}

# Execute comprehensive validation suite
execute_comprehensive_validation() {
    local validation_scope="${1:-full}"
    local output_format="${2:-detailed}"
    local parallel_execution="${3:-true}"
    
    echo -e "${BLUE}🎯 Executing comprehensive validation suite${NC}"
    echo "Scope: $validation_scope"
    echo "Format: $output_format"
    echo "Parallel: $parallel_execution"
    
    local protocols=("file_integrity" "content_quality" "reference_consistency" "size_compliance" "script_functionality" "system_coherence")
    local results=()
    local overall_score=0
    local total_protocols=${#protocols[@]}
    
    echo -e "\n${PURPLE}📊 Validation Results:${NC}"
    printf "%-25s | %-8s | %-10s | %-8s | %s\n" "PROTOCOL" "SCORE" "STATUS" "FINDINGS" "EXEC_TIME"
    printf "%s\n" "$(printf '%.0s-' {1..80})"
    
    for protocol in "${protocols[@]}"; do
        local result_file="$OUTPUT_DIR/validation_${protocol}.json"
        
        if [[ "$parallel_execution" == "true" ]]; then
            # Execute in background for parallel processing
            execute_validation_protocol "$protocol" "$validation_scope" "$output_format" > "$result_file" &
        else
            # Execute sequentially
            execute_validation_protocol "$protocol" "$validation_scope" "$output_format" > "$result_file"
        fi
        
        results+=("$result_file")
    done
    
    # Wait for parallel executions to complete
    if [[ "$parallel_execution" == "true" ]]; then
        wait
    fi
    
    # Process and display results
    for result_file in "${results[@]}"; do
        if [[ -f "$result_file" ]]; then
            local protocol=$(jq -r '.protocol' "$result_file")
            local score=$(jq -r '.score' "$result_file")
            local status=$(jq -r '.status' "$result_file")
            local findings_count=$(jq -r '.findings | length' "$result_file")
            local exec_time=$(jq -r '.execution_time' "$result_file")
            
            overall_score=$((overall_score + score))
            
            # Color code status
            local color="${GREEN}"
            case "$status" in
                "critical"|"poor") color="${RED}" ;;
                "acceptable") color="${YELLOW}" ;;
                "good"|"excellent") color="${GREEN}" ;;
            esac
            
            printf "${color}%-25s | %8d | %-10s | %8d | %6.2fs${NC}\n" \
                "$protocol" "$score" "$status" "$findings_count" "$exec_time"
                
            # Log detailed results
            {
                echo "VALIDATION_PROTOCOL: $protocol"
                echo "  Score: $score/100"
                echo "  Status: $status"
                echo "  Findings: $findings_count"
                echo "  Execution time: ${exec_time}s"
                echo "  ---"
            } >> "$LOG_FILE"
        fi
    done
    
    # Calculate overall assessment
    local avg_score=$((overall_score / total_protocols))
    
    echo -e "\n${GREEN}📈 Comprehensive Validation Summary:${NC}"
    echo "Protocols executed: $total_protocols"
    echo "Average score: $avg_score/100"
    
    # Overall system health assessment
    if [[ $avg_score -ge 95 ]]; then
        echo -e "${GREEN}🎉 EXCELLENT: System validation outstanding${NC}"
        overall_status="EXCELLENT"
    elif [[ $avg_score -ge 85 ]]; then
        echo -e "${GREEN}✅ GOOD: System validation successful with minor issues${NC}"
        overall_status="GOOD"
    elif [[ $avg_score -ge 70 ]]; then
        echo -e "${YELLOW}⚠️  ACCEPTABLE: System validation reveals areas for improvement${NC}"
        overall_status="ACCEPTABLE"
    elif [[ $avg_score -ge 50 ]]; then
        echo -e "${RED}❌ POOR: System validation identifies significant issues${NC}"
        overall_status="POOR"
    else
        echo -e "${RED}🚨 CRITICAL: System validation reveals critical problems${NC}"
        overall_status="CRITICAL"
    fi
    
    return $([ "$overall_status" == "EXCELLENT" ] && echo 0 || echo 1)
}

# Generate comprehensive validation report
generate_validation_report() {
    local results_dir="$1"
    local report_file="$OUTPUT_DIR/COMPREHENSIVE_VALIDATION_REPORT.md"
    
    cat > "$report_file" << EOF
# Comprehensive Validation Report

**Generated**: $(date)
**Script**: validation-protocols.sh
**Purpose**: Comprehensive validation framework for H6D scripts ecosystem

## Validation Summary

### Validation Protocols Executed
$(if [[ -d "$results_dir" ]]; then
    for result_file in "$results_dir"/validation_*.json; do
        if [[ -f "$result_file" ]]; then
            python3 -c "
import json
with open('$result_file', 'r') as f:
    data = json.load(f)
protocol = data.get('protocol', 'unknown')
score = data.get('score', 0)
status = data.get('status', 'unknown')
findings = len(data.get('findings', []))
print(f'- **{protocol.replace(\"_\", \" \").title()}**: {score}/100 ({status}) - {findings} findings')
"
        fi
    done
else
    echo "- Validation results not available"
fi)

## Validation Framework

### Protocol Categories
1. **File Integrity**: Structure, encoding, and accessibility validation
2. **Content Quality**: User authority preservation and fidelity validation
3. **Reference Consistency**: Cross-reference integrity and link validation
4. **Size Compliance**: File size limits and L2-MODULAR compliance
5. **Script Functionality**: Automation framework and script execution validation
6. **System Coherence**: Overall system integrity and workflow validation

### Quality Standards
- **Excellent (≥95)**: Outstanding compliance with all quality standards
- **Good (85-94)**: Strong compliance with minor improvements needed
- **Acceptable (70-84)**: Basic compliance with areas requiring attention
- **Poor (50-69)**: Below standard with significant issues requiring resolution
- **Critical (<50)**: Major problems requiring immediate intervention

## Validation Findings by Category

$(if [[ -d "$results_dir" ]]; then
    for result_file in "$results_dir"/validation_*.json; do
        if [[ -f "$result_file" ]]; then
            echo "### $(python3 -c "import json; data = json.load(open('$result_file')); print(data['protocol'].replace('_', ' ').title())")"
            python3 -c "
import json
with open('$result_file', 'r') as f:
    data = json.load(f)

findings = data.get('findings', [])
if findings:
    severity_counts = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
    for finding in findings:
        severity = finding.get('severity', 'medium')
        if severity in severity_counts:
            severity_counts[severity] += 1
    
    print(f'- **Findings**: {len(findings)} total')
    for severity, count in severity_counts.items():
        if count > 0:
            print(f'  - {severity.title()}: {count}')
    
    print('- **Top Issues**:')
    for finding in findings[:5]:  # Top 5 issues
        print(f'  - {finding.get(\"type\", \"unknown\")}: {finding.get(\"description\", \"no description\")}')
else:
    print('- **Status**: No issues detected')
print()
"
        fi
    done
else
    echo "- Validation findings not available"
fi)

## Recommendations

### Immediate Actions
$(if [[ -d "$results_dir" ]]; then
    for result_file in "$results_dir"/validation_*.json; do
        if [[ -f "$result_file" ]]; then
            python3 -c "
import json
with open('$result_file', 'r') as f:
    data = json.load(f)

findings = data.get('findings', [])
critical_high = [f for f in findings if f.get('severity') in ['critical', 'high']]

if critical_high:
    print(f'#### {data[\"protocol\"].replace(\"_\", \" \").title()}')
    for finding in critical_high[:3]:  # Top 3 critical/high
        print(f'- {finding.get(\"description\", \"no description\")}')
    print()
"
        fi
    done
else
    echo "- Validation recommendations not available"
fi)

### System Improvements
- **Automation Integration**: Utilize H6D scripts for systematic issue resolution
- **Continuous Monitoring**: Implement regular validation cycles
- **Quality Gates**: Enforce validation protocols in automation workflows
- **Documentation**: Maintain validation standards and procedures

## Integration with H6D Framework

### Automated Validation
- **Pre-Operation**: Validation before batch operations
- **Post-Operation**: Validation after script execution
- **Continuous**: Regular system health monitoring
- **Quality Gates**: Automated compliance enforcement

### Script Coordination
- **Domain Classifier**: Categorization validation
- **Batch L2-MODULAR**: Size compliance validation
- **Authority Validator**: Content quality validation
- **Reference Validator**: Link integrity validation
- **Quality Gates**: Comprehensive compliance validation

---
**Generated by**: validation-protocols.sh - H6D-SCRIPTS automation framework
EOF

    echo -e "${GREEN}📄 Validation report: COMPREHENSIVE_VALIDATION_REPORT.md${NC}"
}

# Show usage information
show_usage() {
    cat << EOF
Validation Protocols - H6D-SCRIPTS Automation Framework

USAGE:
    $0 --protocol protocol_name [scope] [format]     # Execute specific protocol
    $0 --comprehensive [scope] [format] [parallel]   # Run all validation protocols
    $0 --report results_directory                    # Generate comprehensive report
    $0 --list                                        # List available protocols
    $0 --help                                        # Show this help

COMMANDS:
    --protocol       Execute specific validation protocol
    --comprehensive  Run complete validation suite
    --report         Generate validation report from results
    --list           List all available validation protocols

PROTOCOL EXAMPLES:
    $0 --protocol file_integrity                     # File structure validation
    $0 --protocol content_quality comprehensive      # Content quality full scope
    $0 --protocol reference_consistency limited      # Reference validation limited scope

COMPREHENSIVE EXAMPLES:
    $0 --comprehensive                               # Full validation suite
    $0 --comprehensive full detailed true           # Detailed parallel execution
    $0 --comprehensive limited summary false        # Limited sequential execution

REPORT EXAMPLES:
    $0 --report validation_results_20250731_143000/ # Generate report from results
    $0 --report ./validation_protocols_output/      # Generate from output directory

VALIDATION PROTOCOLS:
    file_integrity       File structure, encoding, and accessibility validation
    content_quality      User authority preservation and content fidelity
    reference_consistency Cross-reference integrity and bidirectional links
    size_compliance      File size limits and L2-MODULAR compliance
    script_functionality Script execution and automation framework
    system_coherence     Overall system integrity and workflow validation

VALIDATION SCOPES:
    comprehensive        Complete system validation (default)
    full                Full scope with detailed analysis
    limited             Limited scope for quick checks
    critical            Critical issues only

OUTPUT FORMATS:
    detailed            Comprehensive findings and analysis (default)
    summary             High-level results only
    json                Machine-readable JSON output

QUALITY STANDARDS:
    Excellent (≥95)     Outstanding compliance, maintain standards
    Good (85-94)        Strong compliance, minor improvements
    Acceptable (70-84)  Basic compliance, attention needed
    Poor (50-69)        Below standard, significant issues
    Critical (<50)      Major problems, immediate intervention

OUTPUT:
    - Individual protocol validation results with scoring
    - Comprehensive validation suite with parallel execution
    - Detailed findings categorization and severity assessment
    - Integration recommendations and system health assessment
EOF
}

# Main execution function
main() {
    if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
        show_usage
        exit 0
    fi
    
    case "$1" in
        --protocol)
            if [[ $# -lt 2 ]]; then
                echo -e "${RED}❌ Usage: $0 --protocol protocol_name [scope] [format]${NC}"
                exit 1
            fi
            
            local protocol_name="$2"
            local validation_scope="${3:-comprehensive}"
            local output_format="${4:-detailed}"
            
            # Validate protocol name
            if [[ ! "${!VALIDATION_PROTOCOLS[@]}" =~ $protocol_name ]]; then
                echo -e "${RED}❌ Unknown protocol: $protocol_name${NC}"
                echo "Available protocols: ${!VALIDATION_PROTOCOLS[@]}"
                exit 1
            fi
            
            echo -e "${GREEN}🎯 Executing validation protocol: $protocol_name${NC}"
            local result_output=$(execute_validation_protocol "$protocol_name" "$validation_scope" "$output_format")
            
            # Parse and display results
            local score=$(echo "$result_output" | jq -r '.score')
            local status=$(echo "$result_output" | jq -r '.status')
            local findings_count=$(echo "$result_output" | jq -r '.findings | length')
            
            echo -e "\n${BLUE}📊 Protocol Results:${NC}"
            echo "Score: $score/100"
            echo "Status: ${status^^}"
            echo "Findings: $findings_count"
            
            # Save detailed results
            echo "$result_output" > "$OUTPUT_DIR/protocol_${protocol_name}_results.json"
            ;;
            
        --comprehensive)
            local validation_scope="${2:-full}"
            local output_format="${3:-detailed}"
            local parallel_execution="${4:-true}"
            
            echo -e "${GREEN}🚀 Starting comprehensive validation suite${NC}"
            
            if execute_comprehensive_validation "$validation_scope" "$output_format" "$parallel_execution"; then
                echo -e "\n${GREEN}✅ Comprehensive validation completed successfully${NC}"
                exit_code=0
            else
                echo -e "\n${YELLOW}⚠️  Comprehensive validation completed with issues${NC}"
                exit_code=1
            fi
            
            # Generate comprehensive report
            generate_validation_report "$OUTPUT_DIR"
            
            exit $exit_code
            ;;
            
        --report)
            if [[ $# -lt 2 ]]; then
                echo -e "${RED}❌ Usage: $0 --report results_directory${NC}"
                exit 1
            fi
            
            local results_dir="$2"
            
            if [[ ! -d "$results_dir" ]]; then
                echo -e "${RED}❌ Results directory not found: $results_dir${NC}"
                exit 1
            fi
            
            echo -e "${GREEN}📄 Generating comprehensive validation report${NC}"
            generate_validation_report "$results_dir"
            echo -e "${GREEN}✅ Validation report generated successfully${NC}"
            ;;
            
        --list)
            echo -e "${GREEN}📋 Available Validation Protocols:${NC}"
            printf "%-25s | %s\n" "PROTOCOL" "DESCRIPTION"
            printf "%s\n" "$(printf '%.0s-' {1..80})"
            
            for protocol in "${!VALIDATION_PROTOCOLS[@]}"; do
                printf "%-25s | %s\n" "$protocol" "${VALIDATION_PROTOCOLS[$protocol]}"
            done
            ;;
            
        *)
            echo -e "${RED}❌ Unknown option: $1${NC}"
            show_usage
            exit 1
            ;;
    esac
    
    echo -e "\n${GREEN}📁 Output directory: $OUTPUT_DIR${NC}"
    echo -e "${GREEN}📄 Validation log: $LOG_FILE${NC}"
    if [[ -f "$VALIDATION_DB" ]]; then
        echo -e "${GREEN}💾 Validation database: $VALIDATION_DB${NC}"
    fi
}

# Execute main function
main "$@"