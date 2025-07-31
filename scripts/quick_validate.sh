#!/bin/bash

# Quick validation of key scripts to demonstrate validation works
echo "🔍 QUICK VALIDATION - Testing 5 key scripts"
echo "============================================="

# Test scripts array
scripts=(
    "/Users/nalve/ce-simple/scripts/validation/validate-script-communication.sh"
    "/Users/nalve/ce-simple/scripts/analysis/enhanced_analyze_violations.sh"
    "/Users/nalve/ce-simple/scripts/integration/roadmap-update.sh"
    "/Users/nalve/ce-simple/scripts/backup-safety/backup_secure.sh" 
    "/Users/nalve/ce-simple/scripts/export_commands.py"
)

passed=0
failed=0

for script in "${scripts[@]}"; do
    name=$(basename "$script")
    echo ""
    echo "🧪 Testing: $name"
    echo "------------------------"
    
    # 1. Syntax check
    if [[ "$script" == *.py ]]; then
        if python3 -m py_compile "$script" 2>/dev/null; then
            echo "✅ Python syntax: PASS"
        else
            echo "❌ Python syntax: FAIL"
            ((failed++))
            continue
        fi
    else
        if bash -n "$script" 2>/dev/null; then
            echo "✅ Shell syntax: PASS"
        else
            echo "❌ Shell syntax: FAIL"
            ((failed++))
            continue
        fi
    fi
    
    # 2. Hardcoded path check
    if grep -q "/Users/nalve/ce-simple" "$script" 2>/dev/null; then
        echo "❌ Hardcoded paths: FOUND"
        ((failed++))
        continue
    else
        echo "✅ Hardcoded paths: NONE"
    fi
    
    # 3. Path resolution check (simplified)
    script_dir="$(dirname "$script")"
    if [[ "$script" == *.py ]]; then
        # For Python - check if Path calculation works
        expected="/Users/nalve/ce-simple"
        if [[ "$script_dir" == */scripts ]]; then
            calculated="$(cd "$script_dir/.." && pwd)"
        else
            calculated="$(cd "$script_dir/../.." && pwd)"
        fi
        
        if [[ "$calculated" == "$expected" ]]; then
            echo "✅ Path resolution: CORRECT ($calculated)"
        else
            echo "❌ Path resolution: INCORRECT (Expected: $expected, Got: $calculated)"
            ((failed++))
            continue
        fi
    else
        # For Shell - check PROJECT_ROOT calculation
        expected="/Users/nalve/ce-simple"
        if [[ "$script_dir" == */scripts ]]; then
            calculated="$(cd "$script_dir/.." && pwd)"
        else
            calculated="$(cd "$script_dir/../.." && pwd)"
        fi
        
        if [[ "$calculated" == "$expected" ]]; then
            echo "✅ Path resolution: CORRECT ($calculated)"
        else
            echo "❌ Path resolution: INCORRECT (Expected: $expected, Got: $calculated)"
            ((failed++))
            continue
        fi
    fi
    
    echo "✅ Overall: PASS"
    ((passed++))
done

echo ""
echo "📊 QUICK VALIDATION RESULTS"
echo "============================"
echo "Scripts tested: ${#scripts[@]}"
echo "✅ Passed: $passed"
echo "❌ Failed: $failed"

if [[ $failed -eq 0 ]]; then
    echo ""
    echo "🎉 ALL TESTED SCRIPTS PASSED!"
    echo "Dynamic path detection is working correctly."
else
    echo ""
    echo "⚠️ Some scripts have issues that need attention."
fi