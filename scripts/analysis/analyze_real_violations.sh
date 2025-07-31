#!/bin/bash
# analyze_real_violations.sh - Focused analysis excluding backup files
# 30/07/2025 CDMX | Real violation analysis for PHASE_0_EMERGENCY

set -e  # Exit on any error

# Configuration
CONTEXT_DIR="/Users/nalve/ce-simple/context"
OUTPUT_DIR="/Users/nalve/ce-simple/scripts/real_violations_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/real_violations_log.txt"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}PHASE_0_EMERGENCY REAL VIOLATIONS ANALYSIS${NC}"
echo -e "Analyzing real file size violations (excluding backups)..."
echo -e "Context directory: $CONTEXT_DIR"

# Create output directory
mkdir -p "$OUTPUT_DIR"
echo "Real violations analysis started: $(date)" > "$LOG_FILE"

# Find all .md files EXCLUDING backup directories and backup files
echo -e "${YELLOW}Scanning active .md files for violations (>80 lines)...${NC}"
find "$CONTEXT_DIR" -name "*.md" \
    -not -path "*/archive/*" \
    -not -path "*backup*" \
    -not -path "*BACKUP*" \
    -not -name "*backup*" \
    -not -name "*BACKUP*" \
    -exec wc -l {} + | \
    awk '$1 > 80 && $2 !~ /backup|BACKUP/ {print $1, $2}' | \
    sort -nr > "$OUTPUT_DIR/real_violations.txt"

# Count violations by severity
l0_count=$(awk '$1 >= 400' "$OUTPUT_DIR/real_violations.txt" | wc -l | tr -d ' ')
l1_count=$(awk '$1 >= 200 && $1 < 400' "$OUTPUT_DIR/real_violations.txt" | wc -l | tr -d ' ')
l2_count=$(awk '$1 >= 80 && $1 < 200' "$OUTPUT_DIR/real_violations.txt" | wc -l | tr -d ' ')
total_violations=$(wc -l < "$OUTPUT_DIR/real_violations.txt" | tr -d ' ')

echo -e "${BLUE}REAL VIOLATION SUMMARY:${NC}"
echo -e "  ${RED}L0-EMERGENCY (≥400 lines):${NC}        $l0_count files"
echo -e "  ${YELLOW}L1-CRITICAL (200-399 lines):${NC}      $l1_count files"  
echo -e "  ${GREEN}L2-HIGH (80-199 lines):${NC}           $l2_count files"
echo -e "  ${BLUE}TOTAL REAL VIOLATIONS:${NC}             $total_violations files"

# Create priority lists
awk '$1 >= 400' "$OUTPUT_DIR/real_violations.txt" > "$OUTPUT_DIR/l0_emergency.txt"
awk '$1 >= 200 && $1 < 400' "$OUTPUT_DIR/real_violations.txt" > "$OUTPUT_DIR/l1_critical.txt"
awk '$1 >= 80 && $1 < 200' "$OUTPUT_DIR/real_violations.txt" > "$OUTPUT_DIR/l2_high.txt"

# Show top 10 most critical files
echo -e "\n${RED}TOP 10 MOST CRITICAL FILES:${NC}"
head -10 "$OUTPUT_DIR/real_violations.txt" | while read -r lines file; do
    rel_path="${file#$CONTEXT_DIR/}"
    violation_percent=$(( (lines * 100) / 80 ))
    echo -e "  ${RED}✗${NC} $rel_path: $lines lines (${violation_percent}% violation)"
done

# Generate extraction strategy
echo -e "\n${BLUE}HYBRID EXTRACTION STRATEGY:${NC}"
echo -e "  ${RED}Phase 1 - L0 EMERGENCY:${NC} $l0_count files requiring immediate modular extraction"
echo -e "  ${YELLOW}Phase 2 - L1 CRITICAL:${NC} $l1_count files requiring systematic extraction"
echo -e "  ${GREEN}Phase 3 - L2 HIGH:${NC}     $l2_count files requiring optimization extraction"

# Create processing batches (groups of 5 for manageable processing)
echo -e "\n${BLUE}PROCESSING BATCHES (5 files per batch):${NC}"
batch_count=1
while read -r lines file; do
    if (( (batch_count - 1) % 5 == 0 )); then
        echo -e "\n  ${YELLOW}BATCH $((((batch_count - 1) / 5) + 1)):${NC}"
    fi
    rel_path="${file#$CONTEXT_DIR/}"
    echo -e "    ${GREEN}$batch_count.${NC} $rel_path ($lines lines)"
    ((batch_count++))
done < "$OUTPUT_DIR/real_violations.txt"

# Generate ready-to-use command suggestions
echo -e "\n${BLUE}READY-TO-USE PROCESSING COMMANDS:${NC}"
echo -e "  ${GREEN}1. Start with most critical file:${NC}"
head -1 "$OUTPUT_DIR/real_violations.txt" | while read -r lines file; do
    rel_path="${file#$CONTEXT_DIR/}"
    echo -e "     ./scripts/extract_assisted.sh -s \"$rel_path\""
done

echo -e "  ${GREEN}2. Process top 5 critical files:${NC}"
echo -e "     for file in \$(head -5 $OUTPUT_DIR/real_violations.txt | cut -d' ' -f2); do"
echo -e "         rel_path=\"\${file#$CONTEXT_DIR/}\""
echo -e "         ./scripts/extract_assisted.sh -s \"\$rel_path\""
echo -e "     done"

# Create validation script
cat > "$OUTPUT_DIR/validate_progress.sh" << 'EOF'
#!/bin/bash
# Quick validation of extraction progress

CONTEXT_DIR="/Users/nalve/ce-simple/context"
echo "🔍 Current violation status (excluding backups):"
find "$CONTEXT_DIR" -name "*.md" \
    -not -path "*/archive/*" \
    -not -path "*backup*" \
    -not -path "*BACKUP*" \
    -not -name "*backup*" \
    -not -name "*BACKUP*" \
    -exec wc -l {} + | \
    awk '$1 > 80 && $2 !~ /backup|BACKUP/ {print $1, $2}' | \
    sort -nr | wc -l | tr -d ' '
echo "violations remaining"
EOF

chmod +x "$OUTPUT_DIR/validate_progress.sh"

echo -e "\n${GREEN}✓ Real violations analysis complete!${NC}"
echo -e "  📁 Results: $OUTPUT_DIR"
echo -e "  📊 Violation lists: l0_emergency.txt, l1_critical.txt, l2_high.txt"
echo -e "  ✅ Progress validator: validate_progress.sh"
echo -e "  📝 Full log: real_violations_log.txt"

echo "Real violations analysis completed: $(date)" >> "$LOG_FILE"
echo "Total real violations: $total_violations" >> "$LOG_FILE"