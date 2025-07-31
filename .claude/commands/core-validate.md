# /core-validate - Validation Protocols & Quality Gates

**FUNCIÓN**: Standalone validation + embedded quality gates + context coherence

## EMBEDDED QUALITY VALIDATION PROTOCOL

**EMBEDDED QUALITY GATES VALIDATION**:
```bash
# Embedded file size compliance check (zero external dependencies)
check_file_sizes() {
    echo "📏 Checking file size compliance (≤80 lines)..."
    local violations=0
    local total_files=0
    
    while IFS= read -r file; do
        if [[ -f "$file" ]] && [[ "$file" == *.md ]]; then
            ((total_files++))
            local lines=$(wc -l < "$file" 2>/dev/null || echo 0)
            if (( lines > 80 )); then
                echo "❌ $file: $lines lines (violation)"
                ((violations++))
            fi
        fi
    done < <(find . -name "*.md" -not -path "./.git/*" -not -path "./scripts/*" 2>/dev/null)
    
    echo "📊 File Size Analysis:"
    echo "- Total markdown files: $total_files"
    echo "- Files over 80 lines: $violations"
    
    if (( violations == 0 )); then
        echo "✅ No file size violations detected"
        return 0
    else
        echo "⚠️ Found $violations file size violations"
        return $violations
    fi
}

# Embedded authority chain validation
check_authority_chain() {
    echo "🔗 Checking authority chain integrity..."
    local violations=0
    local authority_files=0
    local broken_refs=0
    
    # Check for AUTORIDAD SUPREMA declarations
    while IFS= read -r file; do
        if [[ -f "$file" ]] && grep -q "AUTORIDAD SUPREMA" "$file" 2>/dev/null; then
            ((authority_files++))
        fi
    done < <(find context/ -name "*.md" 2>/dev/null)
    
    # Check for broken @context/ references
    while IFS= read -r file; do
        if [[ -f "$file" ]]; then
            while IFS= read -r ref; do
                local target_file="${ref#@}"
                if [[ ! -f "$target_file" ]]; then
                    echo "❌ Broken reference in $file: $ref"
                    ((broken_refs++))
                fi
            done < <(grep -o '@[^[:space:]]*\.md' "$file" 2>/dev/null || true)
        fi
    done < <(find . -name "*.md" -not -path "./.git/*" 2>/dev/null)
    
    echo "📊 Authority Chain Analysis:"
    echo "- Files with authority declarations: $authority_files"
    echo "- Broken references: $broken_refs"
    
    if (( broken_refs == 0 )); then
        echo "✅ Authority chain integrity maintained"
        return 0
    else
        echo "⚠️ Found $broken_refs broken references"
        return $broken_refs
    fi
}

# Embedded TodoWrite completion validation
check_todo_completion() {
    echo "📋 Checking TodoWrite completion status..."
    local pending_tasks=0
    
    if [[ -f "todowrite.json" ]]; then
        pending_tasks=$(grep -c '"status":"pending\|in_progress"' todowrite.json 2>/dev/null || echo 0)
    fi
    
    echo "📊 TodoWrite Analysis:"
    echo "- Pending/In-progress tasks: $pending_tasks"
    
    if (( pending_tasks == 0 )); then
        echo "✅ All TodoWrite tasks completed"
        return 0
    else
        echo "⚠️ $pending_tasks tasks still pending completion"
        return $pending_tasks
    fi
}

# Embedded git repository validation
check_git_state() {
    echo "🔄 Checking git repository state..."
    local violations=0
    local uncommitted=0
    local staged=0
    
    # Check for uncommitted changes
    if ! git diff --quiet 2>/dev/null; then
        uncommitted=1
        echo "⚠️ Uncommitted changes in working directory"
        ((violations++))
    else
        echo "✅ Working directory clean"
    fi
    
    # Check for staged changes
    if ! git diff --cached --quiet 2>/dev/null; then
        staged=1
        echo "📋 Staged changes present"
    else
        echo "✅ No staged changes"
    fi
    
    # Check current branch
    local current_branch=$(git branch --show-current 2>/dev/null || echo "unknown")
    echo "📊 Git Status Summary:"
    echo "- Current branch: $current_branch"
    echo "- Uncommitted changes: $([ $uncommitted -eq 0 ] && echo "None" || echo "Present")"
    echo "- Staged changes: $([ $staged -eq 0 ] && echo "None" || echo "Present")"
    
    return $violations
}

# Embedded context coherence validation
check_context_coherence() {
    echo "🧠 Checking context coherence..."
    local coherence_issues=0
    
    # Check CLAUDE.md exists and is accessible
    if [[ ! -f "CLAUDE.md" ]]; then
        echo "❌ CLAUDE.md not found"
        ((coherence_issues++))
    else
        echo "✅ CLAUDE.md present"
    fi
    
    # Check for semantic triggers presence
    if [[ -f "CLAUDE.md" ]] && grep -q "SEMANTIC TRIGGERS" "CLAUDE.md" 2>/dev/null; then
        echo "✅ Semantic triggers system present"
    else
        echo "⚠️ Semantic triggers not detected in CLAUDE.md"
        ((coherence_issues++))
    fi
    
    # Check context directory structure
    if [[ -d "context" ]]; then
        echo "✅ Context directory structure present"
    else
        echo "❌ Context directory not found"
        ((coherence_issues++))
    fi
    
    echo "📊 Context Coherence Analysis:"
    echo "- Coherence issues detected: $coherence_issues"
    
    if (( coherence_issues == 0 )); then
        echo "✅ Context coherence validated"
        return 0
    else
        echo "⚠️ Context coherence issues require attention"
        return $coherence_issues
    fi
}

# Main validation execution
validate_execution() {
    echo "🔍 EMBEDDED VALIDATION PROTOCOL ACTIVE"
    echo ""
    
    local total_violations=0
    local validation_report="validation_report_$(date +%Y%m%d_%H%M%S).md"
    
    # Create validation report header
    cat > "$validation_report" << EOF
# Quality Gate Validation Report

**Generated**: $(date)
**Protocol**: /core-validate embedded validation
**Session**: $(date +%Y%m%d_%H%M%S)

## Validation Results

EOF
    
    # Run all validation checks
    echo "1️⃣ File Size Compliance Check"
    check_file_sizes || total_violations=$((total_violations + $?))
    echo ""
    
    echo "2️⃣ Authority Chain Integrity Check"  
    check_authority_chain || total_violations=$((total_violations + $?))
    echo ""
    
    echo "3️⃣ TodoWrite Completion Check"
    check_todo_completion || total_violations=$((total_violations + $?))
    echo ""
    
    echo "4️⃣ Git Repository State Check"
    check_git_state || total_violations=$((total_violations + $?))
    echo ""
    
    echo "5️⃣ Context Coherence Check"
    check_context_coherence || total_violations=$((total_violations + $?))
    echo ""
    
    # Generate validation summary
    if (( total_violations == 0 )); then
        echo "🎯 QUALITY GATE PASSED - All validation checks successful"
        echo "✅ Zero violations detected across all quality criteria"
        echo ""
        echo "## ✅ VALIDATION PASSED" >> "$validation_report"
        echo "All quality checks completed successfully." >> "$validation_report"
    else  
        echo "⚠️ QUALITY GATE WARNINGS - $total_violations total violations detected"
        echo "📋 Review required for complete validation clearance"
        echo ""
        echo "## ⚠️ VALIDATION WARNINGS" >> "$validation_report"
        echo "Found $total_violations total violations requiring attention." >> "$validation_report"
    fi
    
    echo "📊 QUALITY ASSESSMENT SUMMARY:"
    echo "- File size compliance: $(check_file_sizes >/dev/null 2>&1 && echo "✅ Passed" || echo "⚠️ Issues")"
    echo "- Authority chain integrity: $(check_authority_chain >/dev/null 2>&1 && echo "✅ Passed" || echo "⚠️ Issues")"
    echo "- TodoWrite completion: $(check_todo_completion >/dev/null 2>&1 && echo "✅ Passed" || echo "⚠️ Issues")"
    echo "- Git repository state: $(check_git_state >/dev/null 2>&1 && echo "✅ Passed" || echo "⚠️ Issues")"
    echo "- Context coherence: $(check_context_coherence >/dev/null 2>&1 && echo "✅ Passed" || echo "⚠️ Issues")"
    echo ""
    echo "📄 Detailed validation report: $validation_report"
    
    return $total_violations
}

# Execute validation
validate_execution
```

**EMBEDDED VALIDATION CRITERIA**:
- ✅ **File Size Compliance**: All markdown files ≤80 lines (L2-MODULAR enforcement)
- ✅ **Authority Chain Integrity**: Complete authority references + zero broken @context/ links
- ✅ **TodoWrite Completion**: All tasks marked as completed before finalization
- ✅ **Git Repository State**: Clean working directory + staged changes awareness
- ✅ **Context Coherence**: CLAUDE.md + semantic triggers + context structure validation

**COMPLETION GATES**:
- All embedded quality checks passed ✅
- Context coherence maintained ✅  
- No critical violations pending ✅
- Process compliance verified ✅

**INTEGRATION**: Completely self-contained validation with embedded quality gates and comprehensive compliance checking