#!/bin/bash
# analyze_violations.sh - Comprehensive file size violation analysis
# 30/07/2025 CDMX | Systematic analysis for PHASE_0_EMERGENCY

set -e  # Exit on any error

# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Configuration
CONTEXT_DIR="$PROJECT_ROOT/context"
OUTPUT_DIR="$PROJECT_ROOT/scripts/analysis_results_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/analysis_log.txt"

# Colors for output

# Analysis phase

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Initialize log
echo "Analysis started: $(date)" > "$LOG_FILE"
echo "Context directory: $CONTEXT_DIR" >> "$LOG_FILE"

# Function: Analyze violations by category
analyze_violations() {
    
    # Generate comprehensive violation list
    find "$CONTEXT_DIR" -name "*.md" -exec wc -l {} + | \
    awk '$1 > 80 {print $1, $2}' | \
    sort -nr > "$OUTPUT_DIR/all_violations.txt"
    
    # Categorize violations
    awk '$1 >= 400 {print $1, $2}' "$OUTPUT_DIR/all_violations.txt" > "$OUTPUT_DIR/L0_EMERGENCY.txt"
    awk '$1 >= 200 && $1 < 400 {print $1, $2}' "$OUTPUT_DIR/all_violations.txt" > "$OUTPUT_DIR/L1_CRITICAL.txt"
    awk '$1 >= 80 && $1 < 200 {print $1, $2}' "$OUTPUT_DIR/all_violations.txt" > "$OUTPUT_DIR/L2_HIGH.txt"
    
    # Count violations by category
    local l0_count=$(wc -l < "$OUTPUT_DIR/L0_EMERGENCY.txt")
    local l1_count=$(wc -l < "$OUTPUT_DIR/L1_CRITICAL.txt")
    local l2_count=$(wc -l < "$OUTPUT_DIR/L2_HIGH.txt")
    local total_count=$(wc -l < "$OUTPUT_DIR/all_violations.txt")
    
    
    # Log summary
    echo "L0-EMERGENCY: $l0_count files" >> "$LOG_FILE"
    echo "L1-CRITICAL: $l1_count files" >> "$LOG_FILE"
    echo "L2-HIGH: $l2_count files" >> "$LOG_FILE"
    echo "TOTAL: $total_count violations" >> "$LOG_FILE"
}

# Function: Analyze content structure for extraction hints
analyze_structure() {
    
    # Create structure analysis for each violation level
    for level in "L0_EMERGENCY" "L1_CRITICAL" "L2_HIGH"; do
        
        mkdir -p "$OUTPUT_DIR/structure_analysis/$level"
        
        while read -r lines file; do
            if [[ -f "$file" ]]; then
                filename=$(basename "$file" .md)
                rel_path="${file#$CONTEXT_DIR/}"
                
                # Count sections (## headers)
                section_count=$(grep -c "^##" "$file" 2>/dev/null || echo "0")
                
                # Count subsections (### headers)
                subsection_count=$(grep -c "^###" "$file" 2>/dev/null || echo "0")
                
                # Extract main sections for division guidance
                echo "# Structure Analysis: $rel_path ($lines lines)" > "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                echo "## Main Sections ($section_count found):" >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                grep "^## " "$file" 2>/dev/null | head -10 >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt" || echo "No main sections found" >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                
                echo "## Subsections ($subsection_count found):" >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                grep "^### " "$file" 2>/dev/null | head -15 >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt" || echo "No subsections found" >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                
                # Suggest division points
                echo "## Suggested Division Strategy:" >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                if [[ $section_count -gt 3 ]]; then
                    echo "- Create hub with navigation (≤80 lines)" >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                    echo "- Extract each main section as separate module" >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                    echo "- Estimated modules needed: $((section_count + 1))" >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                else
                    echo "- Create hub with core content (≤80 lines)" >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                    echo "- Group related subsections into thematic modules" >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                    echo "- Estimated modules needed: $((subsection_count / 3 + 1))" >> "$OUTPUT_DIR/structure_analysis/$level/${filename}_structure.txt"
                fi
                
            fi
        done < "$OUTPUT_DIR/$level.txt"
    done
}

# Function: Generate pilot test candidates
generate_pilot_candidates() {
    
    # Select 5 L2-HIGH files for pilot testing (100-120 lines range)
    awk '$1 >= 100 && $1 <= 120 {print $1, $2}' "$OUTPUT_DIR/L2_HIGH.txt" | \
    head -5 > "$OUTPUT_DIR/pilot_candidates.txt"
    
    while read -r lines file; do
        rel_path="${file#$CONTEXT_DIR/}"
    done < "$OUTPUT_DIR/pilot_candidates.txt"
    
    echo "Pilot candidates selected" >> "$LOG_FILE"
}

# Function: Generate comprehensive report
generate_analysis_report() {
    
    cat > "$OUTPUT_DIR/VIOLATION_ANALYSIS_REPORT.md" << EOF
# PHASE_0_EMERGENCY Violation Analysis Report

**Date**: $(date)
**Analysis Directory**: $OUTPUT_DIR

## Executive Summary

$(wc -l < "$OUTPUT_DIR/all_violations.txt") files violate the 80-line limit and require modular extraction.

### Violation Categories

#### L0-EMERGENCY (≥400 lines) - $(wc -l < "$OUTPUT_DIR/L0_EMERGENCY.txt") files
- **Priority**: Immediate intervention required
- **Risk**: Critical system violations (>400% over limit)
- **Approach**: Maximum supervision + manual validation

#### L1-CRITICAL (200-399 lines) - $(wc -l < "$OUTPUT_DIR/L1_CRITICAL.txt") files  
- **Priority**: High priority systematic extraction
- **Risk**: Significant violations (150-400% over limit)
- **Approach**: Proven methodology application

#### L2-HIGH (80-199 lines) - $(wc -l < "$OUTPUT_DIR/L2_HIGH.txt") files
- **Priority**: Optimization required
- **Risk**: Standard violations (1-150% over limit)  
- **Approach**: Pilot testing + methodology validation

## Pilot Test Strategy

5 L2-HIGH files selected for methodology validation:
$(while read -r lines file; do echo "- $(basename "$file") ($lines lines)"; done < "$OUTPUT_DIR/pilot_candidates.txt")

## Implementation Sequence

1. **Pilot Phase**: L2-HIGH pilot candidates (5 files)
2. **L2 Phase**: Remaining L2-HIGH files ($(( $(wc -l < "$OUTPUT_DIR/L2_HIGH.txt") - 5 )) files)
3. **L1 Phase**: L1-CRITICAL files ($(wc -l < "$OUTPUT_DIR/L1_CRITICAL.txt") files)
4. **L0 Phase**: L0-EMERGENCY files ($(wc -l < "$OUTPUT_DIR/L0_EMERGENCY.txt") files)

## Success Metrics

- **Zero Tolerance**: $(wc -l < "$OUTPUT_DIR/all_violations.txt") violations → 0 violations (100% compliance)
- **Authority Preservation**: 95%+ user voice fidelity across all extractions
- **Functionality Integrity**: 100% system functionality through reference architecture
- **Security**: Triple backup + validation at each phase

## Files by Category

### L0-EMERGENCY Files
$(cat "$OUTPUT_DIR/L0_EMERGENCY.txt" | while read -r lines file; do echo "- $(basename "$file"): $lines lines ($(( (lines * 100) / 80 ))% violation)"; done)

### L1-CRITICAL Files  
$(cat "$OUTPUT_DIR/L1_CRITICAL.txt" | while read -r lines file; do echo "- $(basename "$file"): $lines lines ($(( (lines * 100) / 80 ))% violation)"; done)

### L2-HIGH Files (First 10)
$(head -10 "$OUTPUT_DIR/L2_HIGH.txt" | while read -r lines file; do echo "- $(basename "$file"): $lines lines ($(( (lines * 100) / 80 ))% violation)"; done)
$(if [[ $(wc -l < "$OUTPUT_DIR/L2_HIGH.txt") -gt 10 ]]; then echo "... and $(( $(wc -l < "$OUTPUT_DIR/L2_HIGH.txt") - 10 )) more files"; fi)

---
**ANALYSIS COMPLETE**: Ready for secure extraction with hybrid approach.
EOF

}

# Main execution
echo "Context directory: $CONTEXT_DIR"
echo "Output directory: $OUTPUT_DIR"

# Execute analysis sequence
analyze_violations
analyze_structure
generate_pilot_candidates
generate_analysis_report


echo ""
echo "1. Review analysis report: $OUTPUT_DIR/VIOLATION_ANALYSIS_REPORT.md"
echo "2. Examine structure analysis for extraction guidance"
echo "3. Run backup_secure.sh before extraction"
echo "4. Begin with pilot test candidates"

echo "Analysis completed: $(date)" >> "$LOG_FILE"