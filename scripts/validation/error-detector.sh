#!/bin/bash
# error-detector.sh - Proactive issue identification system
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Priority Script #10

set -euo pipefail

# Configuration
# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
CONTEXT_DIR="$PROJECT_ROOT/context"
OUTPUT_DIR="$PROJECT_ROOT/scripts/error_detection_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/error_detection_log.txt"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔍 ERROR DETECTOR: Proactive Issue Identification System${NC}"
echo "Purpose: Comprehensive error detection and early warning system for quality and compliance issues"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Initialize log
{
    echo "Error detection started: $(date)"
    echo "Project root: $PROJECT_ROOT"
    echo "Target: Proactive identification of quality, compliance, and system issues"
    echo "Detection scope: File violations, authority issues, reference problems, system inconsistencies"
    echo "================================================================================================="
} > "$LOG_FILE"

# Error detection patterns and thresholds
declare -A ERROR_THRESHOLDS=(
    ["file_size_critical"]="400"
    ["file_size_high"]="200"
    ["file_size_threshold"]="90"
    ["authority_minimum"]="70.0"
    ["reference_integrity_minimum"]="95.0"
    ["quote_minimum"]="2"
    ["context_refs_minimum"]="1"
)

# Detect file size violations with severity classification
detect_file_size_violations() {
    local severity_filter="${1:-all}"
    
    echo -e "${BLUE}🔎 Detecting file size violations (filter: $severity_filter)${NC}"
    
    python3 << EOF
import os
import json
from datetime import datetime

severity_filter = "$severity_filter"
project_root = "$PROJECT_ROOT"

def classify_violation_severity(line_count):
    """Classify violation severity based on line count"""
    if line_count > ${ERROR_THRESHOLDS[file_size_critical]}:
        return "CRITICAL", 4
    elif line_count > ${ERROR_THRESHOLDS[file_size_high]}:
        return "HIGH", 3
    elif line_count > ${ERROR_THRESHOLDS[file_size_threshold]}:
        return "MEDIUM", 2
    elif line_count > 80:
        return "LOW", 1
    else:
        return "COMPLIANT", 0

violations = {
    "CRITICAL": [],
    "HIGH": [],
    "MEDIUM": [],
    "LOW": [],
    "summary": {
        "total_files": 0,
        "violation_files": 0,
        "compliant_files": 0
    }
}

# Scan all markdown files
for root, dirs, files in os.walk(project_root):
    # Skip certain directories
    dirs[:] = [d for d in dirs if not d.startswith('.git') and d != 'node_modules' and 'results' not in d]
    
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, project_root)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                line_count = len(lines)
                violations["summary"]["total_files"] += 1
                
                severity, severity_level = classify_violation_severity(line_count)
                
                if severity != "COMPLIANT":
                    violations["summary"]["violation_files"] += 1
                    
                    violation_info = {
                        "file": relative_path,
                        "lines": line_count,
                        "severity": severity,
                        "severity_level": severity_level,
                        "excess_lines": line_count - 80
                    }
                    
                    violations[severity].append(violation_info)
                else:
                    violations["summary"]["compliant_files"] += 1
                    
            except Exception as e:
                continue

# Filter results based on severity filter
if severity_filter != "all":
    filter_levels = {
        "critical": ["CRITICAL"],
        "high": ["CRITICAL", "HIGH"],
        "medium": ["CRITICAL", "HIGH", "MEDIUM"],
        "low": ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
    }
    
    if severity_filter in filter_levels:
        filtered_violations = {key: violations[key] for key in filter_levels[severity_filter] if key in violations}
        filtered_violations["summary"] = violations["summary"]
        violations = filtered_violations

print(json.dumps(violations, indent=2))

EOF
}

# Detect authority preservation issues
detect_authority_issues() {
    local check_threshold="${1:-${ERROR_THRESHOLDS[authority_minimum]}}"
    
    echo -e "${BLUE}🔎 Detecting authority preservation issues (threshold: $check_threshold%)${NC}"
    
    python3 << EOF
import os
import re
import json

check_threshold = float("$check_threshold")
project_root = "$PROJECT_ROOT"
context_dir = "$CONTEXT_DIR"

authority_issues = {
    "low_fidelity": [],
    "missing_markers": [],
    "broken_chains": [],
    "insufficient_quotes": [],
    "summary": {
        "files_checked": 0,
        "issues_found": 0,
        "avg_authority_score": 0
    }
}

authority_scores = []

# Check files in context directory (where authority matters most)
for root, dirs, files in os.walk(context_dir):
    dirs[:] = [d for d in dirs if not d.startswith('.git')]
    
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, project_root)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                content_lower = content.lower()
                authority_issues["summary"]["files_checked"] += 1
                
                # Calculate authority score (simplified)
                score = 0
                issues = []
                
                # Check for user quotes
                quotes = len(re.findall(r'[">][^"<\\n]{10,}["><]', content))
                if quotes < ${ERROR_THRESHOLDS[quote_minimum]}:
                    issues.append(f"Insufficient quotes: {quotes}")
                score += quotes * 15
                
                # Check for authority markers
                authority_markers = len(re.findall(r'AUTORIDAD|SUPREMA|Authority|VISION|PRINCIPIO', content, re.IGNORECASE))
                if authority_markers == 0:
                    issues.append("Missing authority markers")
                score += authority_markers * 20
                
                # Check for context references
                context_refs = len(re.findall(r'@context/', content))
                if context_refs < ${ERROR_THRESHOLDS[context_refs_minimum]}:
                    issues.append(f"Insufficient context refs: {context_refs}")
                score += context_refs * 10
                
                # Check for broken authority chains
                auth_refs = re.findall(r'← @context/[^\\s\\)]*', content)
                for ref in auth_refs:
                    clean_ref = ref.replace('← ', '')
                    target_path = os.path.join(project_root, clean_ref[1:])  # Remove @
                    if not os.path.exists(target_path):
                        issues.append(f"Broken authority chain: {clean_ref}")
                
                # Spanish authority markers
                spanish_markers = len(re.findall(r'usuario|visión|metodología|suprema', content_lower))
                score += spanish_markers * 5
                
                final_score = min(100, score)
                authority_scores.append(final_score)
                
                # Categorize issues
                if final_score < check_threshold:
                    authority_issues["low_fidelity"].append({
                        "file": relative_path,
                        "score": round(final_score, 1),
                        "issues": issues
                    })
                    authority_issues["summary"]["issues_found"] += 1
                
                if authority_markers == 0 and any("authority" in relative_path.lower() or "vision" in relative_path.lower() for word in ["authority", "vision"]):
                    authority_issues["missing_markers"].append({
                        "file": relative_path,
                        "expected": "Authority file should have AUTORIDAD SUPREMA markers"
                    })
                
                if quotes < ${ERROR_THRESHOLDS[quote_minimum]} and "authority" in relative_path.lower():
                    authority_issues["insufficient_quotes"].append({
                        "file": relative_path,
                        "quotes": quotes,
                        "minimum": ${ERROR_THRESHOLDS[quote_minimum]}
                    })
                
                # Check for broken authority chains
                for ref in auth_refs:
                    clean_ref = ref.replace('← ', '')
                    target_path = os.path.join(project_root, clean_ref[1:])
                    if not os.path.exists(target_path):
                        authority_issues["broken_chains"].append({
                            "file": relative_path,
                            "broken_ref": clean_ref,
                            "target": target_path
                        })
                        
            except Exception as e:
                continue

# Calculate summary statistics
if authority_scores:
    authority_issues["summary"]["avg_authority_score"] = round(sum(authority_scores) / len(authority_scores), 1)

print(json.dumps(authority_issues, indent=2))

EOF
}

# Detect reference integrity problems
detect_reference_issues() {
    local check_bidirectional="${1:-true}"
    
    echo -e "${BLUE}🔎 Detecting reference integrity issues (bidirectional: $check_bidirectional)${NC}"
    
    python3 << EOF
import os
import re
import json

check_bidirectional = "$check_bidirectional" == "true"
project_root = "$PROJECT_ROOT"

reference_issues = {
    "broken_references": [],
    "missing_bidirectional": [],
    "syntax_errors": [],
    "orphaned_files": [],
    "summary": {
        "total_references": 0,
        "broken_references": 0,
        "files_checked": 0
    }
}

all_md_files = set()
referenced_files = set()

# First pass: collect all markdown files and references
for root, dirs, files in os.walk(project_root):
    dirs[:] = [d for d in dirs if not d.startswith('.git') and d != 'node_modules' and 'results' not in d]
    
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, project_root)
            all_md_files.add(relative_path)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                reference_issues["summary"]["files_checked"] += 1
                
                # Find all @context/ references
                context_refs = re.findall(r'@context/[^\\s\\)]*', content)
                
                for ref in context_refs:
                    reference_issues["summary"]["total_references"] += 1
                    target_path = ref[1:]  # Remove @
                    
                    # Add to referenced files set
                    if target_path.endswith('.md'):
                        referenced_files.add(target_path)
                    
                    # Check if target file exists
                    full_target_path = os.path.join(project_root, target_path)
                    if not os.path.exists(full_target_path):
                        if target_path.endswith('.md') or '.' not in os.path.basename(target_path):
                            # Try adding .md extension
                            alt_target = target_path + '.md' if not target_path.endswith('.md') else target_path
                            alt_full_path = os.path.join(project_root, alt_target)
                            
                            if not os.path.exists(alt_full_path):
                                reference_issues["broken_references"].append({
                                    "source_file": relative_path,
                                    "broken_ref": ref,
                                    "target_path": target_path
                                })
                                reference_issues["summary"]["broken_references"] += 1
                
                # Check for syntax errors in references
                invalid_refs = re.findall(r'@[^c][^\\s\\)]*|@c[^o][^\\s\\)]*', content)
                for invalid_ref in invalid_refs:
                    if not invalid_ref.startswith('@context/'):
                        reference_issues["syntax_errors"].append({
                            "source_file": relative_path,
                            "invalid_ref": invalid_ref,
                            "expected": "Should start with @context/"
                        })
                
                # Check bidirectional references if requested
                if check_bidirectional:
                    bi_refs = re.findall(r'←→ @context/[^\\s\\)]*', content)
                    for bi_ref in bi_refs:
                        clean_ref = bi_ref.replace('←→ ', '')
                        target_path = os.path.join(project_root, clean_ref[1:])
                        
                        if os.path.exists(target_path):
                            # Check if target has reverse reference
                            try:
                                with open(target_path, 'r', encoding='utf-8') as target_f:
                                    target_content = target_f.read()
                                
                                if f"←→.*{relative_path}" not in target_content:
                                    reference_issues["missing_bidirectional"].append({
                                        "source_file": relative_path,
                                        "target_file": clean_ref,
                                        "issue": "Missing reverse reference"
                                    })
                            except:
                                pass
                
            except Exception as e:
                continue

# Find orphaned files (files not referenced by others)
context_files = {f for f in all_md_files if f.startswith('context/')}
orphaned_files = context_files - referenced_files

for orphaned in orphaned_files:
    # Skip certain files that are expected to be unreferenced
    if not any(skip in orphaned.lower() for skip in ['readme', 'index', 'archive']):
        reference_issues["orphaned_files"].append({
            "file": orphaned,
            "issue": "File not referenced by any other files"
        })

print(json.dumps(reference_issues, indent=2))

EOF
}

# Detect system inconsistencies
detect_system_inconsistencies() {
    local check_depth="${1:-standard}"
    
    echo -e "${BLUE}🔎 Detecting system inconsistencies (depth: $check_depth)${NC}"
    
    python3 << EOF
import os
import re
import json

check_depth = "$check_depth"
project_root = "$PROJECT_ROOT"

inconsistencies = {
    "naming_violations": [],
    "duplicate_content": [],
    "missing_components": [],
    "structure_violations": [],
    "summary": {
        "total_issues": 0,
        "files_checked": 0
    }
}

# Expected structure patterns
expected_patterns = {
    "context/vision/": ["vision_foundation.md", "simplicity.md"],
    "context/architecture/core/": ["truth-source.md", "authority.md", "methodology.md"],
    "context/architecture/": ["README.md", "patterns.md", "standards.md"]
}

# Check for missing critical components
for path_pattern, expected_files in expected_patterns.items():
    full_path = os.path.join(project_root, path_pattern)
    if os.path.exists(full_path):
        existing_files = [f for f in os.listdir(full_path) if f.endswith('.md')]
        
        for expected_file in expected_files:
            if expected_file not in existing_files:
                inconsistencies["missing_components"].append({
                    "expected_path": os.path.join(path_pattern, expected_file),
                    "issue": "Critical component missing"
                })
                inconsistencies["summary"]["total_issues"] += 1

# Check naming conventions
for root, dirs, files in os.walk(project_root):
    if '.git' in root or 'node_modules' in root or 'results' in root:
        continue
        
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, project_root)
            inconsistencies["summary"]["files_checked"] += 1
            
            # Check naming violations
            if ' ' in file:
                inconsistencies["naming_violations"].append({
                    "file": relative_path,
                    "issue": "Filename contains spaces",
                    "suggestion": "Use hyphens instead of spaces"
                })
                inconsistencies["summary"]["total_issues"] += 1
            
            if file.upper() == file and file != 'README.md':
                inconsistencies["naming_violations"].append({
                    "file": relative_path,
                    "issue": "All uppercase filename",
                    "suggestion": "Use lowercase with hyphens"
                })
                inconsistencies["summary"]["total_issues"] += 1

# Check for potential duplicate content
if check_depth in ["deep", "comprehensive"]:
    content_hashes = {}
    
    for root, dirs, files in os.walk(os.path.join(project_root, "context")):
        if '.git' in root:
            continue
            
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_root)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Simple duplicate detection based on first 200 chars
                    content_sample = content[:200].strip()
                    if len(content_sample) > 50:  # Only check substantial content
                        content_hash = hash(content_sample)
                        
                        if content_hash in content_hashes:
                            inconsistencies["duplicate_content"].append({
                                "file": relative_path,
                                "similar_to": content_hashes[content_hash],
                                "issue": "Potential duplicate content detected"
                            })
                            inconsistencies["summary"]["total_issues"] += 1
                        else:
                            content_hashes[content_hash] = relative_path
                            
                except Exception as e:
                    continue

print(json.dumps(inconsistencies, indent=2))

EOF
}

# Generate error detection report with prioritized recommendations
generate_error_report() {
    local file_violations="$1"
    local authority_issues="$2"
    local reference_issues="$3"
    local system_issues="$4"
    local report_file="$OUTPUT_DIR/ERROR_DETECTION_REPORT.md"
    
    python3 << EOF
import json
from datetime import datetime

# Load all detection results
files = ["$file_violations", "$authority_issues", "$reference_issues", "$system_issues"]
data = {}

for file_path in files:
    try:
        with open(file_path, 'r') as f:
            key = file_path.split('/')[-1].replace('.json', '')
            data[key] = json.load(f)
    except:
        continue

report_file = "$report_file"

with open(report_file, 'w') as f:
    f.write(f'''# Error Detection Report

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Script**: error-detector.sh
**Purpose**: Proactive issue identification and early warning system

## Executive Summary

### Critical Issues Detected
''')
    
    # Count critical issues
    critical_count = 0
    high_count = 0
    medium_count = 0
    
    if 'file_violations' in data:
        critical_count += len(data['file_violations'].get('CRITICAL', []))
        high_count += len(data['file_violations'].get('HIGH', []))
        medium_count += len(data['file_violations'].get('MEDIUM', []))
    
    if 'authority_issues' in data:
        critical_count += len(data['authority_issues'].get('low_fidelity', []))
        high_count += len(data['authority_issues'].get('missing_markers', []))
    
    if 'reference_issues' in data:
        critical_count += len(data['reference_issues'].get('broken_references', []))
        medium_count += len(data['reference_issues'].get('missing_bidirectional', []))
    
    f.write(f'''- **Critical Issues**: {critical_count}
- **High Priority Issues**: {high_count}
- **Medium Priority Issues**: {medium_count}

## File Size Violations
''')
    
    if 'file_violations' in data:
        violations = data['file_violations']
        for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            if severity in violations and violations[severity]:
                f.write(f'''
### {severity} Violations ({len(violations[severity])} files)
''')
                for violation in violations[severity][:5]:  # Show top 5
                    f.write(f"- {violation['file']} ({violation['lines']} lines, {violation['excess_lines']} excess)\\n")
                
                if len(violations[severity]) > 5:
                    f.write(f"- ... and {len(violations[severity]) - 5} more files\\n")
    
    f.write(f'''
## Authority Preservation Issues
''')
    
    if 'authority_issues' in data:
        auth_issues = data['authority_issues']
        
        if auth_issues.get('low_fidelity', []):
            f.write(f'''
### Low Authority Fidelity ({len(auth_issues['low_fidelity'])} files)
''')
            for issue in auth_issues['low_fidelity'][:3]:
                f.write(f"- {issue['file']} (score: {issue['score']}%)\\n")
                for problem in issue['issues'][:2]:
                    f.write(f"  - {problem}\\n")
        
        if auth_issues.get('broken_chains', []):
            f.write(f'''
### Broken Authority Chains ({len(auth_issues['broken_chains'])} references)
''')
            for chain in auth_issues['broken_chains'][:3]:
                f.write(f"- {chain['file']} → {chain['broken_ref']}\\n")
    
    f.write(f'''
## Reference Integrity Issues
''')
    
    if 'reference_issues' in data:
        ref_issues = data['reference_issues']
        
        if ref_issues.get('broken_references', []):
            f.write(f'''
### Broken References ({len(ref_issues['broken_references'])} references)
''')
            for broken in ref_issues['broken_references'][:5]:
                f.write(f"- {broken['source_file']} → {broken['broken_ref']}\\n")
        
        if ref_issues.get('missing_bidirectional', []):
            f.write(f'''
### Missing Bidirectional References ({len(ref_issues['missing_bidirectional'])} references)
''')
            for missing in ref_issues['missing_bidirectional'][:3]:
                f.write(f"- {missing['source_file']} ←→ {missing['target_file']}\\n")
    
    f.write(f'''
## System Inconsistencies
''')
    
    if 'system_issues' in data:
        sys_issues = data['system_issues']
        
        if sys_issues.get('missing_components', []):
            f.write(f'''
### Missing Critical Components ({len(sys_issues['missing_components'])} components)
''')
            for missing in sys_issues['missing_components']:
                f.write(f"- {missing['expected_path']}\\n")
        
        if sys_issues.get('naming_violations', []):
            f.write(f'''
### Naming Violations ({len(sys_issues['naming_violations'])} files)
''')
            for violation in sys_issues['naming_violations'][:3]:
                f.write(f"- {violation['file']}: {violation['issue']}\\n")
    
    f.write(f'''
## Prioritized Action Plan

### Immediate Actions (Critical)
1. **Address Critical File Size Violations**: Files >400 lines require immediate L2-MODULAR extraction
2. **Fix Broken References**: Repair broken @context/ references to restore system coherence
3. **Restore Authority Chains**: Fix broken authority chain references to maintain user authority supremacy

### High Priority Actions
1. **Authority Preservation**: Enhance user voice fidelity in low-scoring authority files
2. **Reference Integrity**: Complete bidirectional reference validation and repair
3. **Missing Components**: Create missing critical system components

### Medium Priority Actions
1. **File Size Optimization**: Process medium-priority violations through H6B L2-MODULAR automation
2. **System Consistency**: Address naming violations and structural inconsistencies
3. **Orphaned File Review**: Evaluate orphaned files for archival or integration

### Automation Opportunities
- Use domain-classifier.sh to categorize violations for optimal processing
- Apply batch-l2-modular.sh for systematic file size violation resolution
- Deploy reference-integrity-validator.sh for comprehensive reference repair
- Implement authority-validator.sh for systematic authority preservation

## Prevention Strategies

### Continuous Monitoring
- Deploy error-detector.sh in continuous monitoring mode
- Integrate with progress-tracker.sh for real-time issue detection
- Set up automated alerts for critical issue emergence

### Quality Gates
- Implement pre-commit validation using batch-quality-gate.sh
- Establish authority preservation requirements for all modifications
- Maintain reference integrity standards through automated validation

### System Health
- Regular system inconsistency detection and resolution
- Proactive identification of potential issues before they become critical
- Systematic approach to maintaining system coherence and quality

---
**Generated by**: error-detector.sh - H6D-SCRIPTS automation framework
''')

print(f"Error detection report generated: {report_file}")

EOF
}

# Run comprehensive error detection suite
run_comprehensive_detection() {
    local output_format="${1:-detailed}"
    
    echo -e "${BLUE}🔍 Running comprehensive error detection suite${NC}"
    echo "Output format: $output_format"
    
    # Run all detection modules
    local file_violations_file="$OUTPUT_DIR/file_violations.json"
    local authority_issues_file="$OUTPUT_DIR/authority_issues.json"
    local reference_issues_file="$OUTPUT_DIR/reference_issues.json"
    local system_issues_file="$OUTPUT_DIR/system_issues.json"
    
    echo -e "\n${CYAN}1/4 Detecting file size violations...${NC}"
    detect_file_size_violations "all" > "$file_violations_file"
    
    echo -e "\n${CYAN}2/4 Detecting authority preservation issues...${NC}"
    detect_authority_issues "${ERROR_THRESHOLDS[authority_minimum]}" > "$authority_issues_file"
    
    echo -e "\n${CYAN}3/4 Detecting reference integrity issues...${NC}"
    detect_reference_issues "true" > "$reference_issues_file"
    
    echo -e "\n${CYAN}4/4 Detecting system inconsistencies...${NC}"
    detect_system_inconsistencies "standard" > "$system_issues_file"
    
    # Generate summary
    echo -e "\n${PURPLE}📊 Error Detection Summary:${NC}"
    
    python3 << EOF
import json

files = ["$file_violations_file", "$authority_issues_file", "$reference_issues_file", "$system_issues_file"]
total_critical = 0
total_high = 0
total_medium = 0
total_low = 0

for file_path in files:
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Count issues based on file type
        if 'file_violations' in file_path:
            total_critical += len(data.get('CRITICAL', []))
            total_high += len(data.get('HIGH', []))
            total_medium += len(data.get('MEDIUM', []))
            total_low += len(data.get('LOW', []))
        
        elif 'authority_issues' in file_path:
            total_critical += len(data.get('low_fidelity', []))
            total_high += len(data.get('missing_markers', []))
            total_medium += len(data.get('insufficient_quotes', []))
        
        elif 'reference_issues' in file_path:
            total_critical += len(data.get('broken_references', []))
            total_high += len(data.get('missing_bidirectional', []))
            total_medium += len(data.get('syntax_errors', []))
        
        elif 'system_issues' in file_path:
            total_critical += len(data.get('missing_components', []))
            total_medium += len(data.get('naming_violations', []))
            total_low += len(data.get('duplicate_content', []))
            
    except Exception as e:
        continue

print(f"Critical Issues: {total_critical}")
print(f"High Priority Issues: {total_high}")
print(f"Medium Priority Issues: {total_medium}")
print(f"Low Priority Issues: {total_low}")

total_issues = total_critical + total_high + total_medium + total_low
print(f"\\nTotal Issues Detected: {total_issues}")

if total_critical > 0:
    print("\\n🚨 CRITICAL: Immediate attention required")
elif total_high > 10:
    print("\\n⚠️  HIGH: Significant issues detected, systematic resolution needed")
elif total_medium > 20:
    print("\\n📊 MEDIUM: Moderate issues detected, regular maintenance recommended")
else:
    print("\\n✅ GOOD: System health is acceptable, minor issues detected")

EOF
    
    # Generate comprehensive report
    if [[ "$output_format" == "detailed" ]]; then
        echo -e "\n${BLUE}📄 Generating comprehensive error detection report...${NC}"
        generate_error_report "$file_violations_file" "$authority_issues_file" "$reference_issues_file" "$system_issues_file"
    fi
    
    # Log summary
    {
        echo "COMPREHENSIVE_ERROR_DETECTION: $(date)"
        echo "  File violations detected: $(jq -r '.CRITICAL | length' "$file_violations_file" 2>/dev/null || echo 0) critical"
        echo "  Authority issues detected: $(jq -r '.low_fidelity | length' "$authority_issues_file" 2>/dev/null || echo 0) low fidelity"
        echo "  Reference issues detected: $(jq -r '.broken_references | length' "$reference_issues_file" 2>/dev/null || echo 0) broken"
        echo "  System issues detected: $(jq -r '.summary.total_issues' "$system_issues_file" 2>/dev/null || echo 0) total"
        echo "  ---"
    } >> "$LOG_FILE"
}

# Show usage information
show_usage() {
    cat << EOF
Error Detector - H6D-SCRIPTS Automation Framework

USAGE:
    $0 --files [severity]                                # Detect file size violations
    $0 --authority [threshold]                           # Detect authority preservation issues
    $0 --references [check_bidirectional]               # Detect reference integrity issues
    $0 --system [depth]                                  # Detect system inconsistencies
    $0 --comprehensive [format]                          # Run complete error detection suite
    $0 --help                                            # Show this help

COMMANDS:
    --files         File size violation detection with severity classification
    --authority     Authority preservation issue detection and analysis
    --references    Reference integrity validation and broken link detection
    --system        System inconsistency detection and structural validation
    --comprehensive Complete error detection suite with prioritized reporting

FILE VIOLATION EXAMPLES:
    $0 --files                                           # All file size violations
    $0 --files critical                                  # Only critical violations (>400 lines)
    $0 --files high                                      # Critical + high violations (>200 lines)
    $0 --files medium                                    # Critical + high + medium (>90 lines)

AUTHORITY EXAMPLES:
    $0 --authority                                       # Default threshold (70%)
    $0 --authority 85.0                                  # Higher authority threshold
    $0 --authority 95.0                                  # Strict authority requirements

REFERENCE EXAMPLES:
    $0 --references                                      # Full reference integrity check
    $0 --references true                                 # Include bidirectional validation
    $0 --references false                                # Skip bidirectional checks

SYSTEM EXAMPLES:
    $0 --system standard                                 # Standard consistency checks
    $0 --system deep                                     # Deep analysis including duplicates
    $0 --system comprehensive                            # Complete system validation

COMPREHENSIVE EXAMPLES:
    $0 --comprehensive                                   # Full detection with detailed report
    $0 --comprehensive summary                           # Quick detection with summary only
    $0 --comprehensive detailed                          # Complete analysis with full report

SEVERITY LEVELS:
    CRITICAL        Files >400 lines, broken authority chains, missing components
    HIGH           Files >200 lines, missing authority markers, broken references
    MEDIUM         Files >90 lines, insufficient quotes, missing bidirectional refs
    LOW            Files >80 lines, naming violations, orphaned files

DETECTION THRESHOLDS:
    File Size Critical:     >${ERROR_THRESHOLDS[file_size_critical]} lines
    File Size High:         >${ERROR_THRESHOLDS[file_size_high]} lines
    File Size Threshold:    >${ERROR_THRESHOLDS[file_size_threshold]} lines
    Authority Minimum:      ${ERROR_THRESHOLDS[authority_minimum]}% fidelity
    Reference Integrity:    ${ERROR_THRESHOLDS[reference_integrity_minimum]}% accuracy
    Quote Minimum:          ${ERROR_THRESHOLDS[quote_minimum]} quotes per authority file

OUTPUT:
    - Categorized issue detection with severity classification
    - Detailed analysis with specific file and line identification
    - Prioritized action plans with automation recommendations
    - Comprehensive reports with prevention strategies
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
            local severity="${2:-all}"
            detect_file_size_violations "$severity"
            ;;
            
        --authority)
            local threshold="${2:-${ERROR_THRESHOLDS[authority_minimum]}}"
            detect_authority_issues "$threshold"
            ;;
            
        --references)
            local check_bidirectional="${2:-true}"
            detect_reference_issues "$check_bidirectional"
            ;;
            
        --system)
            local depth="${2:-standard}"
            detect_system_inconsistencies "$depth"
            ;;
            
        --comprehensive)
            local format="${2:-detailed}"
            run_comprehensive_detection "$format"
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
        echo -e "${GREEN}📄 Detection log: $LOG_FILE${NC}"
    fi
}

# Execute main function
main "$@"