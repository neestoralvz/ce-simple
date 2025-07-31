#!/bin/bash

# Naming Compliance Validator
# Validates system files against unified naming conventions

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
REPO_ROOT="/Users/nalve/ce-simple"
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
REPORT_DIR="$REPO_ROOT/tools/validation/reports"
REPORT_FILE="$REPORT_DIR/naming_compliance_$TIMESTAMP.md"

echo -e "${BLUE}🔍 NAMING COMPLIANCE VALIDATION${NC}"
echo "Report: $REPORT_FILE"
echo "========================================"

# Create report directory
mkdir -p "$REPORT_DIR"

# Initialize report
cat > "$REPORT_FILE" << EOF
# Naming Compliance Report

**Generated**: $(date)
**Validator**: naming-compliance-validator.sh

## VALIDATION RESULTS

EOF

# Initialize counters
total_violations=0
spanish_violations=0
convention_violations=0
cleanup_opportunities=0

echo -e "\n${YELLOW}📋 PHASE 1: SPANISH NAME DETECTION${NC}"

# Check for Spanish names in active files
spanish_files=$(find "$REPO_ROOT" -name "*.md" -not -path "*/archive/*" -not -path "*/scripts/validation_results_*" -not -path "*/scripts/analysis_results_*" | xargs grep -l -E "(metodologia|flujos|simplicidad)" 2>/dev/null || true)

if [ -n "$spanish_files" ]; then
    spanish_count=$(echo "$spanish_files" | wc -l)
    spanish_violations=$spanish_count
    echo -e "${RED}❌ SPANISH NAMES DETECTED: $spanish_count files${NC}"
    
    echo -e "\n### ❌ SPANISH NAME VIOLATIONS" >> "$REPORT_FILE"
    echo "$spanish_files" | while read -r file; do
        rel_path=$(echo "$file" | sed "s|$REPO_ROOT/||")
        echo "- \`$rel_path\`" >> "$REPORT_FILE"
        echo "  $rel_path"
    done
else
    echo -e "${GREEN}✅ NO SPANISH NAMES DETECTED${NC}"
    echo -e "\n### ✅ SPANISH NAME COMPLIANCE" >> "$REPORT_FILE"
    echo "No Spanish names detected in active files." >> "$REPORT_FILE"
fi

echo -e "\n${YELLOW}📋 PHASE 2: NAMING CONVENTION VALIDATION${NC}"

# Check naming conventions by file type
echo -e "\n### 📊 NAMING CONVENTION ANALYSIS" >> "$REPORT_FILE"

# Markdown files - should use kebab-case
md_violations=$(find "$REPO_ROOT" -name "*.md" -not -path "*/archive/*" -not -path "*/scripts/*" | grep -E "_[a-z]" | grep -v -E "(ADR-|HANDOFF_|BACKUP_)" || true)
if [ -n "$md_violations" ]; then
    md_count=$(echo "$md_violations" | wc -l)
    convention_violations=$((convention_violations + md_count))
    echo -e "${RED}❌ MARKDOWN CONVENTION VIOLATIONS: $md_count files${NC}"
    echo -e "\n#### ❌ Markdown Files Using snake_case (should be kebab-case)" >> "$REPORT_FILE"
    echo "$md_violations" | while read -r file; do
        rel_path=$(echo "$file" | sed "s|$REPO_ROOT/||")
        echo "- \`$rel_path\`" >> "$REPORT_FILE"
        echo "  $rel_path"
    done
else
    echo -e "${GREEN}✅ MARKDOWN NAMING COMPLIANT${NC}"
    echo -e "\n#### ✅ Markdown Files" >> "$REPORT_FILE"
    echo "All markdown files follow kebab-case convention." >> "$REPORT_FILE"
fi

# Python files - should use snake_case
py_violations=$(find "$REPO_ROOT" -name "*.py" | grep -E "-[a-z]" || true)
if [ -n "$py_violations" ]; then
    py_count=$(echo "$py_violations" | wc -l)
    convention_violations=$((convention_violations + py_count))
    echo -e "${RED}❌ PYTHON CONVENTION VIOLATIONS: $py_count files${NC}"
    echo -e "\n#### ❌ Python Files Using kebab-case (should be snake_case)" >> "$REPORT_FILE"
    echo "$py_violations" | while read -r file; do
        rel_path=$(echo "$file" | sed "s|$REPO_ROOT/||")
        echo "- \`$rel_path\`" >> "$REPORT_FILE"
        echo "  $rel_path"
    done
else
    echo -e "${GREEN}✅ PYTHON NAMING COMPLIANT${NC}"
    echo -e "\n#### ✅ Python Files" >> "$REPORT_FILE"
    echo "All Python files follow snake_case convention." >> "$REPORT_FILE"
fi

echo -e "\n${YELLOW}📋 PHASE 3: CLEANUP OPPORTUNITIES${NC}"

# Check for backup files that should be cleaned up
backup_files=$(find "$REPO_ROOT" -name "*_BACKUP_*" -type f || true)
if [ -n "$backup_files" ]; then
    backup_count=$(echo "$backup_files" | wc -l)
    cleanup_opportunities=$backup_count
    echo -e "${YELLOW}⚠️  BACKUP FILES FOR CLEANUP: $backup_count files${NC}"
    
    echo -e "\n### 🧹 CLEANUP OPPORTUNITIES" >> "$REPORT_FILE"
    echo -e "\n#### Temporary Backup Files" >> "$REPORT_FILE"
    echo "$backup_files" | head -10 | while read -r file; do
        rel_path=$(echo "$file" | sed "s|$REPO_ROOT/||")
        echo "- \`$rel_path\`" >> "$REPORT_FILE"
    done
    if [ $backup_count -gt 10 ]; then
        echo "- ... and $((backup_count - 10)) more backup files" >> "$REPORT_FILE"
    fi
else
    echo -e "${GREEN}✅ NO BACKUP FILES TO CLEANUP${NC}"
    echo -e "\n### ✅ CLEANUP STATUS" >> "$REPORT_FILE"
    echo "No temporary backup files detected." >> "$REPORT_FILE"
fi

# Check for excessive validation result directories
validation_dirs=$(find "$REPO_ROOT/scripts" -name "validation_results_*" -type d 2>/dev/null | wc -l || echo "0")
if [ "$validation_dirs" -gt 5 ]; then
    cleanup_opportunities=$((cleanup_opportunities + validation_dirs - 5))
    echo -e "${YELLOW}⚠️  EXCESSIVE VALIDATION DIRS: $validation_dirs (keep latest 5)${NC}"
    echo -e "\n#### Excessive Validation Result Directories" >> "$REPORT_FILE"
    echo "Found $validation_dirs validation result directories (recommend keeping latest 5)" >> "$REPORT_FILE"
fi

# Calculate total violations
total_violations=$((spanish_violations + convention_violations))

echo -e "\n${BLUE}📊 FINAL SUMMARY${NC}"
echo "========================================"
echo -e "Spanish Name Violations: ${RED}$spanish_violations${NC}"
echo -e "Convention Violations: ${RED}$convention_violations${NC}"
echo -e "Total Violations: ${RED}$total_violations${NC}"
echo -e "Cleanup Opportunities: ${YELLOW}$cleanup_opportunities${NC}"

# Add summary to report
cat >> "$REPORT_FILE" << EOF

## 📊 SUMMARY

| Category | Count | Status |
|----------|-------|--------|
| **Spanish Name Violations** | $spanish_violations | $([ $spanish_violations -eq 0 ] && echo "✅ COMPLIANT" || echo "❌ VIOLATIONS") |
| **Convention Violations** | $convention_violations | $([ $convention_violations -eq 0 ] && echo "✅ COMPLIANT" || echo "❌ VIOLATIONS") |
| **Total Violations** | $total_violations | $([ $total_violations -eq 0 ] && echo "✅ COMPLIANT" || echo "❌ VIOLATIONS") |
| **Cleanup Opportunities** | $cleanup_opportunities | $([ $cleanup_opportunities -eq 0 ] && echo "✅ CLEAN" || echo "⚠️  CLEANUP NEEDED") |

## 🎯 RECOMMENDATIONS

EOF

# Add recommendations
if [ $spanish_violations -gt 0 ]; then
    echo "1. **Spanish Name Migration**: Execute Phase 2 of NAMING_MIGRATION_PLAN.md" >> "$REPORT_FILE"
fi

if [ $convention_violations -gt 0 ]; then
    echo "2. **Convention Compliance**: Rename files to follow type-specific conventions" >> "$REPORT_FILE"
fi

if [ $cleanup_opportunities -gt 0 ]; then
    echo "3. **System Cleanup**: Execute Phase 1 of NAMING_MIGRATION_PLAN.md (safe deletion)" >> "$REPORT_FILE"
fi

if [ $total_violations -eq 0 ] && [ $cleanup_opportunities -eq 0 ]; then
    echo "🎉 **FULL COMPLIANCE ACHIEVED** - No violations or cleanup needed!" >> "$REPORT_FILE"
fi

# Final status
if [ $total_violations -eq 0 ]; then
    echo -e "\n${GREEN}🎉 NAMING COMPLIANCE: ACHIEVED${NC}"
    exit 0
else
    echo -e "\n${RED}❌ NAMING COMPLIANCE: VIOLATIONS DETECTED${NC}"
    echo -e "See report: $REPORT_FILE"
    exit 1
fi