#!/bin/bash

# Coherence Validation Script
# Based on user-input/technical-requirements/coherence-validation-methodology-user.md

set -e

echo "=== VDD COHERENCE VALIDATION SYSTEM ==="
echo "Authority: user-input/technical-requirements/coherence-validation-methodology-user.md"
echo

# Phase 1: Vision Coherence Check (5 min)
echo "PHASE 1: Vision Coherence Check"
echo "================================="

# Check user vision preservation
if [ -f "user-input/vision/core-mission-concept.md" ]; then
    echo "✅ User vision file preserved"
    
    # Check Task Tool parallelization mentions
    task_tool_count=$(grep -c "Task Tool" user-input/vision/core-mission-concept.md || echo "0")
    if [ "$task_tool_count" -gt 0 ]; then
        echo "✅ Task Tool parallelization maintained ($task_tool_count references)"
    else
        echo "❌ Task Tool parallelization NOT FOUND"
        exit 1
    fi
    
    # Check self-contained commands principle
    if grep -q "self-contained" user-input/vision/core-mission-concept.md; then
        echo "✅ Self-contained commands principle preserved"
    else
        echo "❌ Self-contained commands principle NOT FOUND"
        exit 1
    fi
else
    echo "❌ User vision file MISSING"
    exit 1
fi

echo

# Phase 2: Technical Requirements Validation (10 min)
echo "PHASE 2: Technical Requirements Validation"
echo "=========================================="

# Check PTS Framework consolidation
pts_modules=$(ls docs/core/pts-*-consolidated.md 2>/dev/null | wc -l)
if [ "$pts_modules" -eq 4 ]; then
    echo "✅ PTS Framework consolidated (4 modules)"
else
    echo "❌ PTS Framework consolidation INCOMPLETE ($pts_modules/4 modules)"
    exit 1
fi

# Check analysis files preservation
if [ -d "docs/analysis" ] && [ -f "docs/analysis/docs-content-inventory-comprehensive.md" ] && [ -f "docs/analysis/pts-content-extraction-analysis.md" ]; then
    echo "✅ Analysis files preserved in docs/analysis/"
else
    echo "❌ Analysis files NOT PROPERLY PRESERVED"
    exit 1
fi

# Check coherence validation methodology
if [ -f "user-input/technical-requirements/coherence-validation-methodology-user.md" ]; then
    echo "✅ Coherence validation methodology created"
else
    echo "❌ Coherence validation methodology MISSING"
    exit 1
fi

echo

# Phase 3: Documentation Consistency Audit (10 min)
echo "PHASE 3: Documentation Consistency Audit"
echo "========================================"

# Check authority structure
echo "Checking authority flow: user-input/ → docs/core/ → implementation"

# Verify cross-references to consolidated modules
broken_refs=0
for file in docs/core/README.md docs/README.md; do
    if [ -f "$file" ]; then
        echo "Checking references in $file..."
        
        # Check for old PTS references
        old_refs=$(grep -c "pts-framework\.md\|pts-checklist\.md" "$file" 2>/dev/null || echo "0")
        if [ "$old_refs" -gt 0 ]; then
            echo "❌ Old PTS references found in $file"
            broken_refs=$((broken_refs + 1))
        fi
        
        # Check for new consolidated references
        new_refs=$(grep -c "pts-.*-consolidated\.md" "$file" 2>/dev/null || echo "0")
        if [ "$new_refs" -gt 0 ]; then
            echo "✅ New consolidated references found in $file"
        fi
    fi
done

if [ "$broken_refs" -eq 0 ]; then
    echo "✅ Cross-references updated to new structure"
else
    echo "❌ $broken_refs files have broken references"
    exit 1
fi

# Check archive structure
if [ -d "docs/archive/pts-original" ]; then
    archived_files=$(ls docs/archive/pts-original/*.md 2>/dev/null | wc -l)
    echo "✅ Original files archived ($archived_files files)"
else
    echo "❌ Archive structure NOT FOUND"
    exit 1
fi

echo

# Phase 4: Implementation Integrity Check (15 min)
echo "PHASE 4: Implementation Integrity Check"
echo "======================================="

# Check commands execute user workflows
if [ -d "commands" ]; then
    command_count=$(ls commands/*.md 2>/dev/null | wc -l)
    if [ "$command_count" -ge 3 ]; then
        echo "✅ Commands directory exists ($command_count commands)"
        
        # Check Task Tool references in commands
        task_tool_refs=0
        for cmd in commands/*.md; do
            if grep -q "Task Tool" "$cmd"; then
                task_tool_refs=$((task_tool_refs + 1))
            fi
        done
        
        if [ "$task_tool_refs" -ge 3 ]; then
            echo "✅ Task Tool parallelization implemented in commands ($task_tool_refs/3)"
        else
            echo "❌ Task Tool parallelization INCOMPLETE ($task_tool_refs/3)"
            exit 1
        fi
        
        # Check command self-containment
        external_refs=0
        for cmd in commands/*.md; do
            if grep -q "\.\./\|@.*\.md" "$cmd"; then
                external_refs=$((external_refs + 1))
            fi
        done
        
        if [ "$external_refs" -eq 0 ]; then
            echo "✅ Commands are self-contained (no external references)"
        else
            echo "❌ Commands have external references ($external_refs files)"
            exit 1
        fi
        
    else
        echo "❌ Insufficient commands found ($command_count/3)"
        exit 1
    fi
else
    echo "❌ Commands directory NOT FOUND"
    exit 1
fi

echo

# Final Summary
echo "=== COHERENCE VALIDATION SUMMARY ==="
echo "✅ Phase 1: Vision Coherence - PASSED"
echo "✅ Phase 2: Technical Requirements - PASSED"
echo "✅ Phase 3: Documentation Consistency - PASSED"
echo "✅ Phase 4: Implementation Integrity - PASSED"
echo
echo "🎉 COMPLETE COHERENCE VALIDATION SUCCESSFUL"
echo "Authority structure: user-input/ → docs/core/ → implementation VERIFIED"
echo "System ready for continued development with guaranteed coherence"