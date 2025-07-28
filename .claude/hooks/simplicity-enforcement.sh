#!/bin/bash
# Simplicity Enforcement Hook - Anti-Over-Engineering
# Authority: SIMPLICITY_PROTOCOL.md

set -e

echo "🔍 SIMPLICITY ENFORCEMENT ACTIVE"

# Complexity Detection Thresholds
MAX_COMMANDS=20
MAX_TOOLS=5
MAX_TEMPLATES=10
MAX_ORCHESTRATION_REFS=100

# Count current complexity indicators
COMMANDS=$(find .claude/commands -name "*.md" 2>/dev/null | wc -l || echo 0)
TOOLS=$(find tools -name "*.py" 2>/dev/null | wc -l || echo 0)
TEMPLATES=$(find . -name "*template*" -type f 2>/dev/null | wc -l || echo 0)
ORCHESTRATION=$(grep -r "orchestrat" --include="*.md" . 2>/dev/null | wc -l || echo 0)

# Current status
echo "📊 COMPLEXITY STATUS:"
echo "   Commands: $COMMANDS (max: $MAX_COMMANDS)"
echo "   Tools: $TOOLS (max: $MAX_TOOLS)"
echo "   Templates: $TEMPLATES (max: $MAX_TEMPLATES)"
echo "   Orchestration refs: $ORCHESTRATION (max: $MAX_ORCHESTRATION_REFS)"

# Check thresholds
ALERT_COUNT=0

if [ $COMMANDS -gt $MAX_COMMANDS ]; then
    echo "🚨 COMPLEXITY ALERT: Too many commands ($COMMANDS > $MAX_COMMANDS)"
    echo "   Action: Consolidate redundant commands"
    ALERT_COUNT=$((ALERT_COUNT + 1))
fi

if [ $TOOLS -gt $MAX_TOOLS ]; then
    echo "🚨 COMPLEXITY ALERT: Too many tools ($TOOLS > $MAX_TOOLS)"
    echo "   Action: Remove redundant monitoring/automation tools"
    ALERT_COUNT=$((ALERT_COUNT + 1))
fi

if [ $TEMPLATES -gt $MAX_TEMPLATES ]; then
    echo "🚨 COMPLEXITY ALERT: Too many templates ($TEMPLATES > $MAX_TEMPLATES)"
    echo "   Action: Delete unnecessary template files"
    ALERT_COUNT=$((ALERT_COUNT + 1))
fi

if [ $ORCHESTRATION -gt $MAX_ORCHESTRATION_REFS ]; then
    echo "🚨 COMPLEXITY ALERT: Orchestration overload ($ORCHESTRATION > $MAX_ORCHESTRATION_REFS)"
    echo "   Action: Remove mandatory orchestration for simple tasks"
    ALERT_COUNT=$((ALERT_COUNT + 1))
fi

# Check for forbidden patterns in recent changes
if git diff --cached 2>/dev/null | grep -iE "(ABSOLUTE PROHIBITION|Deploy specialist|orchestration completion|MANDATORY.*orchestration)" >/dev/null 2>&1; then
    echo "🚫 FORBIDDEN PATTERN DETECTED in staged changes:"
    echo "   Over-engineering patterns found"
    echo "   Either simplify approach or justify complexity in commit message"
    ALERT_COUNT=$((ALERT_COUNT + 1))
fi

# Summary
if [ $ALERT_COUNT -eq 0 ]; then
    echo "✅ SIMPLICITY CHECK PASSED"
else
    echo ""
    echo "⚠️  SIMPLICITY VIOLATIONS: $ALERT_COUNT issues detected"
    echo "📖 See SIMPLICITY_PROTOCOL.md for resolution guidance"
    echo ""
    echo "🎯 IMMEDIATE ACTIONS RECOMMENDED:"
    echo "   1. Review and consolidate redundant components"
    echo "   2. Remove unnecessary complexity"
    echo "   3. Follow 3-step rule for workflows"
    echo "   4. Apply simplicity gate to new additions"
fi

echo ""
echo "🎯 Remember: Simple things should remain simple"
echo "📋 Full analysis: over-engineering-analysis.md"
echo "📖 Prevention rules: SIMPLICITY_PROTOCOL.md"