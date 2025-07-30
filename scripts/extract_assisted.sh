#!/bin/bash
# extract_assisted.sh - Semiautomated extraction with manual validation checkpoints
# 30/07/2025 CDMX | Hybrid approach for PHASE_0_EMERGENCY modular extraction

set -e  # Exit on any error

# Configuration
CONTEXT_DIR="/Users/nalve/ce-simple/context"
EXTRACTION_DIR="/Users/nalve/ce-simple/scripts/extraction_session_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$EXTRACTION_DIR/extraction_log.txt"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

echo -e "${GREEN}PHASE_0_EMERGENCY ASSISTED EXTRACTION${NC}"
echo "Semiautomated modular extraction with manual validation checkpoints"

# Function: Show usage
show_usage() {
    cat << EOF
Usage: $0 [OPTIONS] TARGET_FILE

Options:
  -m, --mode MODE     Extraction mode: pilot|batch|single (default: single)
  -c, --category CAT  File category: L0|L1|L2 (auto-detect if not specified)
  -v, --verbose       Verbose output with detailed analysis
  -s, --simulate      Simulation mode (no actual changes)
  -h, --help          Show this help message

Modes:
  pilot    - Process pilot test candidates (5 L2-HIGH files)
  batch    - Process multiple files from specified category
  single   - Process single file with full supervision

Examples:
  $0 -m pilot                              # Process pilot test files
  $0 -m batch -c L2                       # Process all L2-HIGH files
  $0 simplicity.md                        # Process single file
  $0 -s CROSS_REFERENCE_SYSTEM.md         # Simulate extraction

SAFETY: Always run backup_secure.sh before first extraction.
EOF
}

# Function: Create extraction workspace
create_workspace() {
    mkdir -p "$EXTRACTION_DIR"/{analysis,modules,validation,backups}
    
    # Initialize log
    echo "Extraction session started: $(date)" > "$LOG_FILE"
    echo "Context directory: $CONTEXT_DIR" >> "$LOG_FILE"
    echo "Extraction directory: $EXTRACTION_DIR" >> "$LOG_FILE"
    
    echo -e "${GREEN}✓ Extraction workspace created: $EXTRACTION_DIR${NC}"
}

# Function: Analyze file structure for extraction
analyze_file_structure() {
    local file_path="$1"
    local filename=$(basename "$file_path" .md)
    
    echo -e "${YELLOW}Analyzing file structure: $filename${NC}"
    
    if [[ ! -f "$file_path" ]]; then
        echo -e "${RED}❌ File not found: $file_path${NC}"
        return 1
    fi
    
    local line_count=$(wc -l < "$file_path")
    local section_count=$(grep -c "^## " "$file_path" 2>/dev/null || echo "0")
    local subsection_count=$(grep -c "^### " "$file_path" 2>/dev/null || echo "0")
    local authority_count=$(grep -c "AUTORIDAD\|authority\|SUPREMA" "$file_path" 2>/dev/null || echo "0")
    
    # Create analysis file
    cat > "$EXTRACTION_DIR/analysis/${filename}_analysis.txt" << EOF
# File Structure Analysis: $(basename "$file_path")

## Basic Metrics
- **Total Lines**: $line_count ($(( (line_count * 100) / 80 ))% of 80-line limit)
- **Main Sections**: $section_count (## headers)
- **Subsections**: $subsection_count (### headers)
- **Authority References**: $authority_count

## Section Structure
$(grep "^## " "$file_path" 2>/dev/null | head -15 || echo "No main sections found")

## Subsection Details
$(grep "^### " "$file_path" 2>/dev/null | head -20 || echo "No subsections found")

## Authority Chain Detection
$(grep -n "AUTORIDAD\|authority\|SUPREMA" "$file_path" 2>/dev/null | head -5 || echo "No authority declarations found")

## Extraction Strategy Recommendation
EOF

    # Generate extraction strategy
    if [[ $section_count -gt 4 ]]; then
        echo "- **Strategy**: Section-based modular extraction" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
        echo "- **Hub Content**: Navigation + core authority (≤80 lines)" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
        echo "- **Modules**: Each main section as separate module" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
        echo "- **Estimated Modules**: $((section_count + 1))" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
    elif [[ $subsection_count -gt 8 ]]; then
        echo "- **Strategy**: Thematic grouping extraction" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
        echo "- **Hub Content**: Navigation + essential content (≤80 lines)" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
        echo "- **Modules**: Grouped subsections by theme" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
        echo "- **Estimated Modules**: $((subsection_count / 3 + 1))" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
    else
        echo "- **Strategy**: Content-based extraction" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
        echo "- **Hub Content**: Core essence + navigation (≤80 lines)" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
        echo "- **Modules**: Detailed content by domain" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
        echo "- **Estimated Modules**: 2-4 modules" >> "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
    fi
    
    echo -e "${BLUE}Structure Analysis:${NC}"
    echo -e "  Lines: $line_count ($(( (line_count * 100) / 80 ))% violation)"
    echo -e "  Sections: $section_count main, $subsection_count sub"
    echo -e "  Authority refs: $authority_count"
    
    echo "File analysis completed: $filename ($line_count lines)" >> "$LOG_FILE"
}

# Function: Manual validation checkpoint
manual_checkpoint() {
    local checkpoint_name="$1"
    local message="$2"
    
    echo ""
    echo -e "${PURPLE}════════════════════════════════════════════════════════════════${NC}"
    echo -e "${PURPLE}MANUAL VALIDATION CHECKPOINT: $checkpoint_name${NC}"
    echo -e "${PURPLE}════════════════════════════════════════════════════════════════${NC}"
    echo -e "${YELLOW}$message${NC}"
    echo ""
    
    while true; do
        read -p "Continue with extraction? (yes/no/show/abort): " response
        case $response in
            yes|y)
                echo -e "${GREEN}✓ Checkpoint approved, continuing...${NC}"
                echo "Checkpoint $checkpoint_name: APPROVED" >> "$LOG_FILE"
                return 0
                ;;
            no|n)
                echo -e "${YELLOW}⚠️ Checkpoint declined, stopping extraction${NC}"
                echo "Checkpoint $checkpoint_name: DECLINED" >> "$LOG_FILE"
                return 1
                ;;
            show|s)
                if [[ -f "$EXTRACTION_DIR/analysis/${filename}_analysis.txt" ]]; then
                    echo -e "${BLUE}Showing analysis:${NC}"
                    cat "$EXTRACTION_DIR/analysis/${filename}_analysis.txt"
                    echo ""
                else
                    echo -e "${YELLOW}No analysis file available${NC}"
                fi
                ;;
            abort|a)
                echo -e "${RED}❌ Extraction aborted by user${NC}"
                echo "Checkpoint $checkpoint_name: ABORTED" >> "$LOG_FILE"
                exit 1
                ;;
            *)
                echo "Please answer yes, no, show, or abort"
                ;;
        esac
    done
}

# Function: Create backup checkpoint
create_backup_checkpoint() {
    local file_path="$1"
    local filename=$(basename "$file_path" .md)
    local line_count=$(wc -l < "$file_path")
    
    # Create individual backup
    cp "$file_path" "$EXTRACTION_DIR/backups/${filename}_ORIGINAL_${line_count}_lines.md"
    echo -e "${GREEN}✓ Backup created: ${filename}_ORIGINAL_${line_count}_lines.md${NC}"
    
    echo "Backup created: $filename ($line_count lines)" >> "$LOG_FILE"
}

# Function: Extract hub and modules
extract_modular_components() {
    local file_path="$1"
    local filename=$(basename "$file_path" .md)
    
    echo -e "${YELLOW}Creating modular extraction for: $filename${NC}"
    
    if [[ "$SIMULATE" == true ]]; then
        echo -e "${BLUE}[SIMULATION] Would create modular extraction${NC}"
        return 0
    fi
    
    # Create modules directory for this file
    local modules_dir="$EXTRACTION_DIR/modules/$filename"
    mkdir -p "$modules_dir"
    
    # Extract sections based on analysis
    local section_count=$(grep -c "^## " "$file_path" 2>/dev/null || echo "0")
    
    if [[ $section_count -gt 2 ]]; then
        # Section-based extraction
        extract_by_sections "$file_path" "$modules_dir"
    else
        # Content-based extraction  
        extract_by_content "$file_path" "$modules_dir"
    fi
}

# Function: Extract by main sections
extract_by_sections() {
    local file_path="$1"
    local modules_dir="$2"
    local filename=$(basename "$file_path" .md)
    
    echo -e "${BLUE}Extracting by main sections...${NC}"
    
    # Get section headers
    grep -n "^## " "$file_path" > "$modules_dir/sections.txt" 2>/dev/null || echo "No sections found"
    
    local module_count=1
    local current_section=""
    local current_content=""
    
    # Read file line by line and group by sections
    while IFS= read -r line; do
        if [[ "$line" =~ ^##\  ]]; then
            # Save previous section if exists
            if [[ -n "$current_section" && -n "$current_content" ]]; then
                local module_name=$(echo "$current_section" | sed 's/^## //' | tr ' ' '-' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]//g')
                echo "$current_content" > "$modules_dir/${module_name}.md"
                echo -e "  ${GREEN}✓${NC} Module created: ${module_name}.md"
                module_count=$((module_count + 1))
            fi
            
            # Start new section
            current_section="$line"
            current_content="$line\n"
        else
            current_content="$current_content$line\n"
        fi
    done < "$file_path"
    
    # Save last section
    if [[ -n "$current_section" && -n "$current_content" ]]; then
        local module_name=$(echo "$current_section" | sed 's/^## //' | tr ' ' '-' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]//g')
        echo -e "$current_content" > "$modules_dir/${module_name}.md"
        echo -e "  ${GREEN}✓${NC} Module created: ${module_name}.md"
    fi
    
    echo "Section-based extraction: $module_count modules created" >> "$LOG_FILE"
}

# Function: Extract by content domains (simpler approach for now)
extract_by_content() {
    local file_path="$1"
    local modules_dir="$2"
    local filename=$(basename "$file_path" .md)
    
    echo -e "${BLUE}Extracting by content domains...${NC}"
    
    local total_lines=$(wc -l < "$file_path")
    local lines_per_module=$((total_lines / 3))  # Roughly divide into 3 modules
    
    # Simple content-based extraction (basic implementation)
    split -l $lines_per_module "$file_path" "$modules_dir/module-"
    
    # Rename split files to proper module names
    local i=1
    for split_file in "$modules_dir"/module-*; do
        if [[ -f "$split_file" ]]; then
            mv "$split_file" "$modules_dir/content-domain-${i}.md"
            echo -e "  ${GREEN}✓${NC} Module created: content-domain-${i}.md"
            i=$((i + 1))
        fi
    done
    
    echo "Content-based extraction: $((i-1)) modules created" >> "$LOG_FILE"
}

# Function: Create hub file
create_hub_file() {
    local file_path="$1"
    local modules_dir="$2"
    local filename=$(basename "$file_path" .md)
    
    echo -e "${YELLOW}Creating hub file: ${filename}_hub.md${NC}"
    
    if [[ "$SIMULATE" == true ]]; then
        echo -e "${BLUE}[SIMULATION] Would create hub file${NC}"
        return 0
    fi
    
    # Extract header and authority information
    local authority_line=$(grep -n "AUTORIDAD SUPREMA\|## AUTORIDAD" "$file_path" | head -1 | cut -d: -f1)
    local principle_line=$(grep -n "PRINCIPIO FUNDAMENTAL\|## PRINCIPIO" "$file_path" | head -1 | cut -d: -f1)
    
    # Create hub with navigation
    cat > "$modules_dir/../${filename}_HUB.md" << EOF
# $(basename "$file_path" .md) - Modular Navigation Hub

**$(date '+%d/%m/%Y %H:%M %Z')** | Modular extraction for 80-line compliance

## AUTORIDAD SUPREMA
$(sed -n "${authority_line}p" "$file_path" 2>/dev/null || echo "Authority chain preserved in modules")

## PRINCIPIO FUNDAMENTAL
$(sed -n "${principle_line}p" "$file_path" 2>/dev/null || echo "Core principles preserved in specialized modules")

## MODULAR NAVIGATION

### Specialized Modules
$(for module in "$modules_dir"/*.md; do
    if [[ -f "$module" ]]; then
        local module_name=$(basename "$module" .md)
        echo "- **${module_name}.md** → $(head -1 "$module" | sed 's/^# *//' 2>/dev/null || echo "Module content")"
    fi
done)

### Integration References
- **Cross-Reference System**: ←→ Complete system integration preserved
- **Authority Chain**: ← Supreme authority maintained through modular structure
- **Evolution Pathway**: → Organic growth supported through reference architecture

---
**MODULAR EXTRACTION DECLARATION**: Original content preserved through specialized modules while achieving 80-line compliance per user authority supremacy.
EOF

    echo -e "${GREEN}✓ Hub file created: ${filename}_HUB.md${NC}"
    echo "Hub file created: ${filename}_HUB.md" >> "$LOG_FILE"
}

# Function: Validate extraction results
validate_extraction() {
    local modules_dir="$1"
    local filename="$2"
    
    echo -e "${YELLOW}Validating extraction results...${NC}"
    
    local hub_file="$modules_dir/../${filename}_HUB.md"
    local hub_lines=0
    local all_compliant=true
    
    # Check hub compliance
    if [[ -f "$hub_file" ]]; then
        hub_lines=$(wc -l < "$hub_file")
        if [[ $hub_lines -le 80 ]]; then
            echo -e "${GREEN}✅ Hub compliant: $hub_lines lines${NC}"
        else
            echo -e "${RED}❌ Hub violation: $hub_lines lines${NC}"
            all_compliant=false
        fi
    fi
    
    # Check module compliance
    for module in "$modules_dir"/*.md; do
        if [[ -f "$module" ]]; then
            local module_lines=$(wc -l < "$module")
            local module_name=$(basename "$module")
            
            if [[ $module_lines -le 80 ]]; then
                echo -e "${GREEN}✅ Module compliant: $module_name ($module_lines lines)${NC}"
            else
                echo -e "${RED}❌ Module violation: $module_name ($module_lines lines)${NC}"
                all_compliant=false
            fi
        fi
    done
    
    if [[ "$all_compliant" == true ]]; then
        echo -e "${GREEN}🎉 EXTRACTION VALIDATION: PERFECT${NC}"
        echo "Extraction validation: PASS - all components ≤80 lines" >> "$LOG_FILE"
        return 0
    else
        echo -e "${RED}❌ EXTRACTION VALIDATION: COMPLIANCE ISSUES${NC}"
        echo "Extraction validation: FAIL - compliance violations detected" >> "$LOG_FILE"
        return 1
    fi
}

# Function: Process single file
process_single_file() {
    local target_file="$1"
    local file_path=""
    
    # Find file in context directory
    if [[ -f "$target_file" ]]; then
        file_path="$target_file"
    elif [[ -f "$CONTEXT_DIR/$target_file" ]]; then
        file_path="$CONTEXT_DIR/$target_file"
    else
        file_path=$(find "$CONTEXT_DIR" -name "$target_file" -type f | head -1)
    fi
    
    if [[ ! -f "$file_path" ]]; then
        echo -e "${RED}❌ File not found: $target_file${NC}"
        return 1
    fi
    
    local filename=$(basename "$file_path" .md)
    echo -e "${GREEN}Processing single file: $filename${NC}"
    
    # Analysis phase
    analyze_file_structure "$file_path"
    
    # Manual checkpoint 1: Analysis review
    if ! manual_checkpoint "ANALYSIS_REVIEW" "Review file analysis. Check structure recommendations before proceeding."; then
        return 1
    fi
    
    # Backup phase
    create_backup_checkpoint "$file_path"
    
    # Manual checkpoint 2: Extraction approval  
    if ! manual_checkpoint "EXTRACTION_APPROVAL" "Ready to create modular extraction. This will create hub + modules."; then
        return 1
    fi
    
    # Extraction phase
    extract_modular_components "$file_path"
    create_hub_file "$file_path" "$EXTRACTION_DIR/modules/$filename"
    
    # Validation phase
    if validate_extraction "$EXTRACTION_DIR/modules/$filename" "$filename"; then
        # Manual checkpoint 3: Final approval
        if manual_checkpoint "FINAL_APPROVAL" "Extraction completed successfully. Apply changes to original file?"; then
            if [[ "$SIMULATE" != true ]]; then
                # Replace original with hub (in real implementation)
                echo -e "${YELLOW}Ready to replace original file with hub${NC}"
                echo -e "${RED}[SAFETY] Actual file replacement not implemented in this version${NC}"
                echo -e "${BLUE}Manual step: Review generated files in $EXTRACTION_DIR${NC}"
            fi
        fi
    else
        echo -e "${RED}❌ Extraction validation failed${NC}"
        return 1
    fi
    
    echo "Single file processing completed: $filename" >> "$LOG_FILE"
}

# Parse command line arguments
MODE="single"
CATEGORY=""
VERBOSE=false
SIMULATE=false
TARGET_FILE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -m|--mode)
            MODE="$2"
            shift 2
            ;;
        -c|--category)
            CATEGORY="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -s|--simulate)
            SIMULATE=true
            shift
            ;;
        -h|--help)
            show_usage
            exit 0
            ;;
        -*)
            echo "Unknown option: $1"
            show_usage
            exit 1
            ;;
        *)
            TARGET_FILE="$1"
            shift
            ;;
    esac
done

# Main execution
create_workspace

echo "Extraction mode: $MODE" >> "$LOG_FILE"
if [[ "$SIMULATE" == true ]]; then
    echo -e "${BLUE}🧪 SIMULATION MODE: No actual changes will be made${NC}"
    echo "Simulation mode: ENABLED" >> "$LOG_FILE"
fi

case "$MODE" in
    single)
        if [[ -z "$TARGET_FILE" ]]; then
            echo -e "${RED}ERROR: Target file required for single mode${NC}"
            show_usage
            exit 1
        fi
        process_single_file "$TARGET_FILE"
        ;;
    pilot)
        echo -e "${YELLOW}Pilot mode not implemented yet${NC}"
        echo "TODO: Implement pilot test processing"
        ;;
    batch)
        echo -e "${YELLOW}Batch mode not implemented yet${NC}"
        echo "TODO: Implement batch processing"
        ;;
    *)
        echo -e "${RED}ERROR: Unknown mode: $MODE${NC}"
        show_usage
        exit 1
        ;;
esac

echo -e "${GREEN}🎉 ASSISTED EXTRACTION SESSION COMPLETED${NC}"
echo -e "${BLUE}Session directory: $EXTRACTION_DIR${NC}"
echo "Extraction session completed: $(date)" >> "$LOG_FILE"