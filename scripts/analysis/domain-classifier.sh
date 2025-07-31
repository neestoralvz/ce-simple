#!/bin/bash
# domain-classifier.sh - Automated content domain classification for H6A/B/C processing
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Priority Script #1

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
CONTEXT_DIR="$PROJECT_ROOT/context"
OUTPUT_DIR="$PROJECT_ROOT/scripts/classification_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/classification_log.txt"

# Silent script - no user notifications (Claude Code communicates results)

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Initialize log (technical data only)
{
    echo "$(date)"
    echo "$PROJECT_ROOT"
    echo "classification_start"
} > "$LOG_FILE"

# Domain classification patterns
declare -A DOMAIN_PATTERNS=(
    ["archive"]="backup|original|legacy|deprecated|old|unused|session_|COMPACTED|ARCHIVE"
    ["authority"]="authority|suprema|user.*voice|vision|permission|mandate"
    ["methodology"]="methodology|protocol|workflow|process|systematic|framework"
    ["patterns"]="pattern|template|structure|format|standard|convention"
    ["technical"]="script|code|implementation|technical|system|config"
    ["documentation"]="readme|guide|overview|documentation|instruction|manual"
    ["context"]="context|architecture|core|foundation|principle|truth"
    ["roadmap"]="roadmap|phase|handoff|timeline|execution|planning"
    ["templates"]="template|format|structure|blueprint|example|sample"
    ["validation"]="validation|quality|compliance|testing|verification|audit"
)

# Classification scoring system
classify_file_domain() {
    local file_path="$1"
    
    if [[ ! -f "$file_path" ]]; then
        echo "unknown:0"
        return
    fi
    
    python3 << EOF
import re
import os

file_path = "$file_path"
patterns = {
    "archive": r"backup|original|legacy|deprecated|old|unused|session_|COMPACTED|ARCHIVE",
    "authority": r"authority|suprema|user.*voice|vision|permission|mandate",
    "methodology": r"methodology|protocol|workflow|process|systematic|framework",
    "patterns": r"pattern|template|structure|format|standard|convention",
    "technical": r"script|code|implementation|technical|system|config",
    "documentation": r"readme|guide|overview|documentation|instruction|manual",
    "context": r"context|architecture|core|foundation|principle|truth",
    "roadmap": r"roadmap|phase|handoff|timeline|execution|planning",
    "templates": r"template|format|structure|blueprint|example|sample",
    "validation": r"validation|quality|compliance|testing|verification|audit"
}

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().lower()
    
    filename = os.path.basename(file_path).lower()
    directory = os.path.dirname(file_path).lower()
    
    scores = {}
    
    for domain, pattern in patterns.items():
        # Content analysis (60% weight)
        content_matches = len(re.findall(pattern, content, re.IGNORECASE))
        
        # Filename analysis (25% weight)  
        filename_matches = len(re.findall(pattern, filename, re.IGNORECASE))
        
        # Directory analysis (15% weight)
        directory_matches = len(re.findall(pattern, directory, re.IGNORECASE))
        
        # Calculate weighted score
        total_score = (content_matches * 0.6) + (filename_matches * 0.25) + (directory_matches * 0.15)
        scores[domain] = total_score
    
    # Find highest scoring domain
    if scores:
        best_domain = max(scores, key=scores.get)
        best_score = scores[best_domain]
        
        # Confidence thresholds
        if best_score >= 3.0:
            confidence = "high"
        elif best_score >= 1.5:
            confidence = "medium"
        elif best_score >= 0.5:
            confidence = "low"
        else:
            confidence = "uncertain"
            
        print(f"{best_domain}:{best_score:.2f}:{confidence}")
    else:
        print("unknown:0:uncertain")

except Exception as e:
    print("unknown:0:error")
EOF
}

# Analyze file characteristics for processing recommendation
analyze_processing_needs() {
    local file_path="$1"
    local domain="$2"
    local score="$3"
    local confidence="$4"
    
    python3 << EOF
import os

file_path = "$file_path"
domain = "$domain"
score = float("$score")
confidence = "$confidence"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    line_count = len(lines)
    
    # Processing recommendation based on domain and size
    if domain == "archive" and line_count > 80:
        processing = "H6A-ARCHIVE"
        priority = "high"
        reason = "Archive content suitable for batch processing"
    elif domain in ["authority", "context", "methodology"] and 91 <= line_count <= 200:
        processing = "H6B-L2MODULAR"
        priority = "high"
        reason = "Authority-rich content suitable for L2-MODULAR extraction"
    elif domain in ["patterns", "templates", "validation"] and 80 <= line_count <= 90:
        processing = "H6A-QUICKWINS"
        priority = "medium"
        reason = "Threshold content suitable for quick optimization"
    elif domain == "technical" and line_count > 90:
        processing = "H6C-INDIVIDUAL"
        priority = "medium"
        reason = "Technical content requiring individual assessment"
    elif line_count <= 80:
        processing = "COMPLIANT"
        priority = "low"
        reason = "Already compliant - no processing needed"
    else:
        processing = "H6C-INDIVIDUAL"
        priority = "low"
        reason = "General content requiring individual assessment"
    
    print(f"{processing}|{priority}|{reason}")

except Exception as e:
    print("ERROR|low|Classification error")
EOF
}

# Process single file classification
classify_single_file() {
    local file_path="$1"
    local relative_path="${file_path#$PROJECT_ROOT/}"
    
    # Get domain classification
    local classification=$(classify_file_domain "$file_path")
    local domain=$(echo "$classification" | cut -d: -f1)
    local score=$(echo "$classification" | cut -d: -f2)
    local confidence=$(echo "$classification" | cut -d: -f3)
    
    # Get processing recommendation
    local processing_info=$(analyze_processing_needs "$file_path" "$domain" "$score" "$confidence")
    local processing=$(echo "$processing_info" | cut -d'|' -f1)
    local priority=$(echo "$processing_info" | cut -d'|' -f2)
    local reason=$(echo "$processing_info" | cut -d'|' -f3)
    
    # Get file size
    local line_count=$(wc -l < "$file_path" 2>/dev/null || echo "0")
    
    # Output classification result
    printf "%-50s | %-12s | %-8s | %-10s | %-15s | %-8s | %4d | %s\n" \
        "$relative_path" "$domain" "$confidence" "$processing" "$priority" "$score" "$line_count" "$reason"
    
    # Log detailed classification (technical data only)
    {
        echo "$relative_path|$domain|$score|$confidence|$processing|$priority|$line_count|$reason"
    } >> "$LOG_FILE"
}

# Find files needing classification
find_classification_targets() {
    local target_pattern="${1:-.*}"
    
    # Find files that likely need processing (size violations or specific patterns)
    find "$PROJECT_ROOT" -type f -name "*.md" | while read -r file; do
        # Skip certain directories
        if [[ "$file" =~ /\.git/|/node_modules/|/scripts/.*results/ ]]; then
            continue
        fi
        
        # Check if file matches target pattern
        if [[ "$file" =~ $target_pattern ]]; then
            local line_count=$(wc -l < "$file" 2>/dev/null || echo "0")
            
            # Include files over 80 lines or in specific directories
            if [[ $line_count -gt 80 ]] || [[ "$file" =~ /context/|/\.claude/ ]]; then
                echo "$file"
            fi
        fi
    done
}

# Generate classification report
generate_classification_report() {
    local output_file="$OUTPUT_DIR/DOMAIN_CLASSIFICATION_REPORT.md"
    
    cat > "$output_file" << 'EOF'
# Domain Classification Report

**Generated**: $(date)
**Script**: domain-classifier.sh
**Purpose**: Automated content categorization for H6A/B/C processing optimization

## Classification Results

### Summary by Domain
EOF

    # Count files by domain
    local domains=(archive authority methodology patterns technical documentation context roadmap templates validation)
    
    for domain in "${domains[@]}"; do
        local count=$(grep -c "| $domain " "$OUTPUT_DIR/classification_results.txt" 2>/dev/null || echo "0")
        echo "- **$domain**: $count files" >> "$output_file"
    done
    
    cat >> "$output_file" << 'EOF'

### Processing Recommendations
- **H6A-ARCHIVE**: Archive content for batch processing
- **H6B-L2MODULAR**: Authority-rich content for L2-MODULAR extraction  
- **H6A-QUICKWINS**: Threshold content for quick optimization
- **H6C-INDIVIDUAL**: Individual assessment required
- **COMPLIANT**: Already compliant files

### Quality Metrics
- **High Confidence**: Clear domain identification
- **Medium Confidence**: Probable domain identification
- **Low Confidence**: Uncertain domain identification

---
**Generated by**: domain-classifier.sh - H6D-SCRIPTS automation framework
EOF

}

# Main execution function
main() {
    local target_pattern="${1:-.*}"
    local max_files="${2:-100}"
    
    
    # Create output file with headers
    local results_file="$OUTPUT_DIR/classification_results.txt"
    printf "%-50s | %-12s | %-8s | %-10s | %-15s | %-8s | %4s | %s\n" \
        "FILE_PATH" "DOMAIN" "CONF" "PROCESSING" "PRIORITY" "SCORE" "LINES" "REASON" > "$results_file"
    printf "%s\n" "$(printf '%.0s-' {1..150})" >> "$results_file"
    
    # Process files
    printf "%-50s | %-12s | %-8s | %-10s | %-15s | %-8s | %4s | %s\n" \
        "FILE_PATH" "DOMAIN" "CONF" "PROCESSING" "PRIORITY" "SCORE" "LINES" "REASON"
    printf "%s\n" "$(printf '%.0s-' {1..150})"
    
    local processed=0
    local h6a_count=0
    local h6b_count=0
    local h6c_count=0
    local compliant_count=0
    
    while IFS= read -r file && [[ $processed -lt $max_files ]]; do
        local result=$(classify_single_file "$file")
        echo "$result"
        echo "$result" >> "$results_file"
        
        # Count by processing type
        if [[ "$result" =~ H6A ]]; then
            ((h6a_count++))
        elif [[ "$result" =~ H6B ]]; then
            ((h6b_count++))
        elif [[ "$result" =~ H6C ]]; then
            ((h6c_count++))
        elif [[ "$result" =~ COMPLIANT ]]; then
            ((compliant_count++))
        fi
        
        ((processed++))
    done < <(find_classification_targets "$target_pattern")
    
    # Technical summary (data only)
    {
        echo "$(date)|$processed|$h6a_count|$h6b_count|$h6c_count|$compliant_count"
    } >> "$LOG_FILE"
    
    generate_classification_report
}

# Show usage
show_usage() {
    cat << EOF
Domain Classifier - H6D-SCRIPTS Automation Framework

USAGE:
    $0 [pattern] [max_files]
    $0 --help

ARGUMENTS:
    pattern     Regex pattern for file filtering (default: .*)
    max_files   Maximum files to process (default: 100)

EXAMPLES:
    $0                          # Classify all violation files
    $0 "context/.*" 50         # Classify context files (max 50)
    $0 ".*backup.*" 20         # Classify backup files (max 20)

OUTPUT:
    - Classification results table
    - Domain distribution summary  
    - Processing recommendations for H6A/B/C
    - Detailed log and report files

DOMAINS:
    archive, authority, methodology, patterns, technical,
    documentation, context, roadmap, templates, validation

PROCESSING TYPES:
    H6A-ARCHIVE    - Batch archive processing
    H6B-L2MODULAR  - L2-MODULAR extraction candidates
    H6A-QUICKWINS  - Quick optimization targets
    H6C-INDIVIDUAL - Individual assessment required
    COMPLIANT      - Already meets requirements
EOF
}

# Handle command line arguments
if [[ $# -gt 0 ]] && [[ "$1" == "--help" ]]; then
    show_usage
    exit 0
fi

# Execute main function
main "$@"