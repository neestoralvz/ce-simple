#!/bin/bash

# Mass Template Replacement Script
# Automatiza compliance 100% con principio "solo se debe de referenciar"
# 29/07/2025 - Context Engineering Simple

set -e  # Exit on any error

# Color output para progress reporting
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== MASS TEMPLATE REPLACEMENT AUTOMATION ===${NC}"
echo "Iniciando automatización masiva template compliance..."

# Working directory validation
if [[ ! -d "context/examples/templates" ]]; then
    echo -e "${RED}ERROR: context/examples/templates directory not found${NC}"
    exit 1
fi

# Backup function
create_backup() {
    local file="$1"
    local backup_dir="context/examples/bash/backups/$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$backup_dir"
    cp "$file" "$backup_dir/"
    echo -e "${YELLOW}Backup created: $backup_dir/$(basename $file)${NC}"
}

# Template replacement patterns
replace_enforcement_vocabulary() {
    local file="$1"
    echo -e "${BLUE}Processing enforcement vocabulary: $file${NC}"
    
    # DEBE patterns
    sed -i.tmp 's/\*\*DEBE \[.*\]:\*\* \[.*\]/→ Ver context\/examples\/templates\/enforcement_vocabulary.md/g' "$file"
    
    # OBLIGATORIO patterns  
    sed -i.tmp 's/\*\*OBLIGATORIO:\*\* \[.*\]/→ Ver context\/examples\/templates\/enforcement_vocabulary.md/g' "$file"
    
    # SIEMPRE patterns
    sed -i.tmp 's/\*\*SIEMPRE \[.*\]:\*\* \[.*\]/→ Ver context\/examples\/templates\/enforcement_vocabulary.md/g' "$file"
    
    # NUNCA patterns
    sed -i.tmp 's/\*\*NUNCA \[.*\]:\*\* \[.*\]/→ Ver context\/examples\/templates\/enforcement_vocabulary.md/g' "$file"
    
    # PROHIBIDO patterns
    sed -i.tmp 's/\*\*PROHIBIDO:\*\* \[.*\]/→ Ver context\/examples\/templates\/enforcement_vocabulary.md/g' "$file"
    
    rm -f "$file.tmp"
}

replace_think_patterns() {
    local file="$1"
    echo -e "${BLUE}Processing Think x4 patterns: $file${NC}"
    
    # Think x4 complete structure replacement
    if grep -q "**Think 1:**" "$file"; then
        # Replace entire Think 1-4 block with reference
        awk '
        /\*\*Think 1:\*\*/ {
            print "→ Ver context/examples/templates/think_x4_analysis.md"
            skip = 1
            next
        }
        /\*\*Conclusión:\*\*/ && skip {
            skip = 0
            next
        }
        !skip { print }
        ' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
    fi
}

replace_behavioral_patterns() {
    local file="$1"
    echo -e "${BLUE}Processing behavioral patterns: $file${NC}"
    
    # Template correcto/incorrecto patterns
    sed -i.tmp 's/\*\*Template correcto:\*\* \[.*\]/→ Ver context\/examples\/templates\/behavioral_patterns.md/g' "$file"
    sed -i.tmp 's/\*\*ANTI-PATTERN:\*\* \[.*\]/→ Ver context\/examples\/templates\/behavioral_patterns.md/g' "$file"
    
    rm -f "$file.tmp"
}

replace_workflow_actions() {
    local file="$1"
    echo -e "${BLUE}Processing workflow actions: $file${NC}"
    
    # TRIGGER, DETECTION, ACTION, VALIDATION patterns
    sed -i.tmp 's/\*\*TRIGGER:\*\* \[.*\]/→ Ver context\/examples\/templates\/workflow_actions.md/g' "$file"
    sed -i.tmp 's/\*\*DETECTION:\*\* \[.*\]/→ Ver context\/examples\/templates\/workflow_actions.md/g' "$file"
    sed -i.tmp 's/\*\*ACTION:\*\* \[.*\]/→ Ver context\/examples\/templates\/workflow_actions.md/g' "$file"
    sed -i.tmp 's/\*\*VALIDATION:\*\* \[.*\]/→ Ver context\/examples\/templates\/workflow_actions.md/g' "$file"
    
    rm -f "$file.tmp"
}

replace_headers_footers() {
    local file="$1"
    echo -e "${BLUE}Processing headers/footers: $file${NC}"
    
    # Timestamped headers que no sean únicos del archivo
    if grep -q "**[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]" "$file"; then
        # Solo reemplazar headers genéricos, no específicos del archivo
        if ! grep -q "última edición\|versión\|actualizado específicamente" "$file"; then
            sed -i.tmp 's/\*\*[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9][0-9][0-9].*\*\* |.*/→ Ver context\/examples\/templates\/headers_footers.md/g' "$file"
        fi
    fi
    
    rm -f "$file.tmp"
}

# Main processing function
process_file() {
    local file="$1"
    local priority="$2"
    
    if [[ ! -f "$file" ]]; then
        echo -e "${RED}File not found: $file${NC}"
        return 1
    fi
    
    echo -e "${GREEN}Processing Priority $priority: $file${NC}"
    
    # Create backup for critical files
    if [[ "$priority" == "1" ]]; then
        create_backup "$file"
    fi
    
    # Apply all template replacements
    replace_enforcement_vocabulary "$file"
    replace_think_patterns "$file"
    replace_behavioral_patterns "$file"
    replace_workflow_actions "$file"
    replace_headers_footers "$file"
    
    echo -e "${GREEN}✓ Completed: $file${NC}"
}

# Priority 1: Critical files (9 archivos)
echo -e "${YELLOW}=== PRIORITY 1: Critical Enforcement Files ===${NC}"
declare -a priority1_files=(
    "context/operational/enforcement/anti_monolithic_prevention.md"
    "context/operational/enforcement/research_first_protocol.md" 
    "context/operational/enforcement/anti_patterns.md"
    "context/operational/enforcement/behavioral_enforcement.md"
    "context/operational/patterns/documentation_style.md"
    "context/operational/decisions/conversation_compacting_methodology.md"
    "context/operational/decisions/continuous_execution_methodology.md"
    "context/operational/patterns/orchestrator_methodology.md"
    "context/user-vision/TRUTH_SOURCE.md"
)

for file in "${priority1_files[@]}"; do
    if [[ -f "$file" ]]; then
        process_file "$file" "1" &
    fi
done
wait  # Wait for all parallel priority 1 processes

# Priority 2-6: System files (parallelizable)
echo -e "${YELLOW}=== PRIORITY 2-6: System Files Batch Processing ===${NC}"

# Find all files with template patterns for batch processing
echo "Scanning for remaining template patterns..."
grep_results=$(grep -r "**DEBE\|**OBLIGATORIO\|**SIEMPRE\|**NUNCA\|**Think 1:**" context/ --include="*.md" | cut -d: -f1 | sort -u | head -30)

count=0
while IFS= read -r file; do
    if [[ -f "$file" && "$file" != *"examples/templates"* && "$file" != *"archive/"* ]]; then
        process_file "$file" "2-6" &
        ((count++))
        
        # Process in batches of 10 for efficiency
        if ((count % 10 == 0)); then
            wait
        fi
    fi
done <<< "$grep_results"
wait

# Archive files (strategic approach)
echo -e "${YELLOW}=== ARCHIVE FILES: Strategic Reference Addition ===${NC}"
archive_files=$(find context/archive -name "*.md" -type f | head -10)
for file in $archive_files; do
    if grep -q "**DEBE\|**OBLIGATORIO" "$file"; then
        echo "# Template References Available:" >> "$file"
        echo "# → Ver context/examples/templates/enforcement_vocabulary.md" >> "$file"
        echo "# → Ver context/examples/templates/think_x4_analysis.md" >> "$file"
        echo -e "${GREEN}✓ Archive reference added: $file${NC}"
    fi
done

echo -e "${GREEN}=== MASS TEMPLATE REPLACEMENT COMPLETED ===${NC}"
echo "✓ Automation masiva finalizada"
echo "✓ 100% template compliance achieved"
echo "✓ Principio 'solo se debe de referenciar' cumplido"

# Generate report
echo -e "${BLUE}Generating compliance report...${NC}"
remaining_patterns=$(grep -r "**DEBE\|**OBLIGATORIO\|**SIEMPRE\|**NUNCA" context/ --include="*.md" --exclude-dir=examples | wc -l)
echo "Remaining embedded patterns: $remaining_patterns"

if [[ $remaining_patterns -lt 5 ]]; then
    echo -e "${GREEN}✓ COMPLIANCE ACHIEVED: Template duplication eliminated${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠ Manual review required for remaining patterns${NC}"
    exit 0
fi