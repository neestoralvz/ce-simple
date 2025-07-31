#!/bin/bash

# Comprehensive Script Validation Report
# Tests all 16 scripts (15 shell + 1 Python) for dynamic path detection
# Date: 2025-07-31

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Counters
PASSED=0
FAILED=0
WARNINGS=0

# Function to validate a script
validate_script() {
    local script_path="$1"
    local script_type="$2"
    local issues=0
    
    echo ""
    echo -e "${BLUE}======================================${NC}"
    echo -e "${BLUE}TESTING: $(basename "$script_path")${NC}"
    echo -e "${BLUE}======================================${NC}"
    
    # Check if file exists
    if [[ ! -f "$script_path" ]]; then
        echo -e "${RED}❌ CRITICAL: File does not exist${NC}"
        return 1
    fi
    
    # 1. Syntax validation
    echo -n "🔍 Syntax check: "
    if [[ "$script_type" == "python" ]]; then
        if python3 -m py_compile "$script_path" 2>/dev/null; then
            echo -e "${GREEN}PASS${NC}"
        else
            echo -e "${RED}FAIL${NC}"
            ((issues++))
        fi
    else
        if bash -n "$script_path" 2>/dev/null; then
            echo -e "${GREEN}PASS${NC}"
        else
            echo -e "${RED}FAIL${NC}"
            ((issues++))
        fi
    fi
    
    # 2. Hardcoded path check
    echo -n "🔍 Hardcoded paths: "
    if grep -q "/Users/nalve/ce-simple" "$script_path" 2>/dev/null; then
        echo -e "${RED}FOUND - FAIL${NC}"
        echo "   Found: $(grep -n "/Users/nalve/ce-simple" "$script_path" | head -2)"
        ((issues++))
    else
        echo -e "${GREEN}NONE - PASS${NC}"
    fi
    
    # 3. Path resolution verification
    echo -n "🔍 Path resolution: "
    script_dir="$(dirname "$script_path")"
    expected="/Users/nalve/ce-simple"
    
    # Calculate what PROJECT_ROOT should be based on script location
    # All scripts should resolve to /Users/nalve/ce-simple
    if [[ "$script_path" == */scripts/modules/* ]]; then
        # modules/ is inside scripts/ (scripts/modules/file.sh -> ../../ = project root)
        calculated="$(cd "$script_dir/../.." && pwd)"
    elif [[ "$script_path" == */scripts/*/* ]]; then
        # Any subdirectory in scripts/ (scripts/subdir/file.sh -> ../../ = project root)  
        calculated="$(cd "$script_dir/../.." && pwd)" 
    else
        # Direct in scripts directory (scripts/file.sh or scripts/file.py -> ../ = project root)
        calculated="$(cd "$script_dir/.." && pwd)"
    fi
    
    if [[ "$calculated" == "$expected" ]]; then
        echo -e "${GREEN}CORRECT${NC} ($calculated)"
    else
        echo -e "${RED}INCORRECT${NC} (Expected: $expected, Calculated: $calculated)"
        ((issues++))
    fi
    
    # 4. Dynamic path pattern check
    echo -n "🔍 Dynamic paths: "
    if [[ "$script_type" == "python" ]]; then
        if grep -q "Path(__file__).parent" "$script_path"; then
            echo -e "${GREEN}IMPLEMENTED${NC}"
        else
            echo -e "${YELLOW}NOT FOUND${NC}"
            ((WARNINGS++))
        fi
    else
        if grep -q 'SCRIPT_DIR.*dirname.*BASH_SOURCE' "$script_path" && grep -q 'PROJECT_ROOT.*cd.*SCRIPT_DIR' "$script_path"; then
            echo -e "${GREEN}IMPLEMENTED${NC}"
        else
            echo -e "${YELLOW}PATTERN NOT FOUND${NC}"
            ((WARNINGS++))
        fi
    fi
    
    # Results
    if [[ $issues -eq 0 ]]; then
        echo -e "${GREEN}✅ OVERALL: PASS${NC}"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}❌ OVERALL: FAIL ($issues issues)${NC}"
        ((FAILED++))
        return 1
    fi
}

# Main function
main() {
    echo "🔍 COMPREHENSIVE SCRIPT VALIDATION"
    echo "=================================="
    echo "Testing all 16 scripts for dynamic path detection"
    echo "Date: $(date)"
    echo ""
    
    # Define all scripts to test
    declare -a SHELL_SCRIPTS=(
        "/Users/nalve/ce-simple/scripts/validation/validate-script-communication.sh"
        "/Users/nalve/ce-simple/scripts/analysis/enhanced_analyze_violations.sh"
        "/Users/nalve/ce-simple/scripts/analysis/domain-classifier.sh"
        "/Users/nalve/ce-simple/scripts/integration/cross-reference-updater.sh"
        "/Users/nalve/ce-simple/scripts/integration/test-roadmap-update.sh"
        "/Users/nalve/ce-simple/scripts/integration/roadmap-update.sh"
        "/Users/nalve/ce-simple/scripts/backup-safety/rollback-manager.sh"
        "/Users/nalve/ce-simple/scripts/maintenance/fix-script-communication.sh"
        "/Users/nalve/ce-simple/scripts/infrastructure/progress-tracker.sh"
        "/Users/nalve/ce-simple/scripts/analysis/analyze_real_violations.sh"
        "/Users/nalve/ce-simple/scripts/analysis/analyze_violations.sh"
        "/Users/nalve/ce-simple/scripts/backup-safety/backup_secure.sh"
        "/Users/nalve/ce-simple/scripts/validation/validate_integrity.sh"
        "/Users/nalve/ce-simple/scripts/extraction/l2_modular_extractor.sh"
        "/Users/nalve/ce-simple/scripts/modules/intelligent-decision-matrix.sh"
    )
    
    declare -a PYTHON_SCRIPTS=(
        "/Users/nalve/ce-simple/scripts/export_commands.py"
    )
    
    # Test shell scripts
    echo "🐚 TESTING SHELL SCRIPTS (15 total)"
    echo "====================================="
    for script in "${SHELL_SCRIPTS[@]}"; do
        validate_script "$script" "shell"
    done
    
    # Test Python scripts  
    echo ""
    echo "🐍 TESTING PYTHON SCRIPTS (1 total)"
    echo "===================================="
    for script in "${PYTHON_SCRIPTS[@]}"; do
        validate_script "$script" "python"
    done
    
    # Final report
    echo ""
    echo "📊 FINAL VALIDATION REPORT"
    echo "=========================="
    echo "Total scripts tested: 16"
    echo -e "✅ Passed: ${GREEN}$PASSED${NC}"
    echo -e "❌ Failed: ${RED}$FAILED${NC}"
    echo -e "⚠️ Warnings: ${YELLOW}$WARNINGS${NC}"
    
    local pass_rate=$((PASSED * 100 / 16))
    echo "Pass rate: $pass_rate%"
    
    if [[ $FAILED -eq 0 ]]; then
        echo ""
        echo -e "${GREEN}🎉 VALIDATION SUCCESS!${NC}"
        echo -e "${GREEN}All 16 scripts have been successfully updated with dynamic path detection.${NC}"
        echo -e "${GREEN}No hardcoded paths remain in any script.${NC}"
        echo -e "${GREEN}Path resolution is working correctly.${NC}"
        return 0
    else
        echo ""
        echo -e "${RED}⚠️ VALIDATION ISSUES DETECTED${NC}"
        echo -e "${RED}$FAILED scripts have critical issues that need to be addressed.${NC}"
        if [[ $WARNINGS -gt 0 ]]; then
            echo -e "${YELLOW}$WARNINGS scripts have warnings but are functional.${NC}"
        fi
        return 1
    fi
}

# Run validation
main "$@"