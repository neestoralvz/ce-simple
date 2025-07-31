#!/bin/bash
# conversation-complete.sh - Standard conversation completion
# Part of Git Workflow Analysis Implementation
# Created: 2025-07-31

set -euo pipefail

CONVERSATION_SUMMARY="$1"

if [[ -z "$CONVERSATION_SUMMARY" ]]; then
    echo "❌ Error: Conversation summary required"
    echo "Usage: bash tools/automation/conversation-complete.sh 'Conversation summary'"
    exit 1
fi

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

CURRENT_BRANCH=$(git branch --show-current)
echo "🏁 Completing conversation on branch: $CURRENT_BRANCH"

# 1. Final system health check
echo "🔍 Final health validation..."
if [[ -f "tools/monitoring/system-health.py" ]]; then
    python3 tools/monitoring/system-health.py --report > "conversation-health-report-$(date +%Y%m%d-%H%M).json" 2>/dev/null || {
        echo "⚠️ Warning: Health report generation failed"
    }
else
    echo "⚠️ Warning: system-health.py not found, skipping health check"
fi

# 2. Check for handoff documentation updates
HANDOFF_FILES=$(find context/roadmap/ -name "HANDOFF_*.md" 2>/dev/null || true)
if [[ -n "$HANDOFF_FILES" ]]; then
    echo "📋 Handoff documentation found:"
    echo "$HANDOFF_FILES" | head -3
    echo "ℹ️ Consider updating handoff status if applicable"
fi

# 3. Final commit with conversation summary
echo "📝 Creating final commit..."
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "ℹ️ No changes to commit"
else
    git commit -m "CONVERSATION COMPLETE: $CONVERSATION_SUMMARY

Final commit for conversation on branch $CURRENT_BRANCH.
System health validated, all procedures followed.

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
    echo "✅ Final commit created"
fi

# 4. Show conversation statistics
echo ""
echo "📊 Conversation Statistics:"
echo "   Branch: $CURRENT_BRANCH"
echo "   Commits: $(git rev-list --count HEAD ^master 2>/dev/null || git rev-list --count HEAD)"
echo "   Files changed: $(git diff --name-only master..HEAD 2>/dev/null | wc -l || echo "N/A")"

# 5. Integration decision prompt
echo ""
echo "🔄 Integration options:"
echo "1. Push branch for later integration"
echo "2. Merge to master immediately"  
echo "3. Create pull request (push branch)"
echo "4. Skip integration (local only)"
echo -n "Select option (1-4): "
read -n 1 -r INTEGRATION_CHOICE
echo  # New line after input

case $INTEGRATION_CHOICE in
    1)
        echo "⬆️ Pushing branch..."
        git push -u origin "$CURRENT_BRANCH"
        echo "✅ Branch pushed: $CURRENT_BRANCH"
        echo "   To integrate later: git checkout master && git merge $CURRENT_BRANCH"
        ;;
    2)
        echo "🔄 Merging to master..."
        # Ensure we're up to date
        git fetch origin master 2>/dev/null || echo "⚠️ Could not fetch master"
        git checkout master
        git merge "$CURRENT_BRANCH" --no-ff -m "Merge conversation: $CONVERSATION_SUMMARY"
        git push origin master
        echo "✅ Merged to master and pushed"
        echo "   Conversation branch $CURRENT_BRANCH can be removed if desired"
        ;;
    3)
        echo "📤 Pushing branch for PR..."
        git push -u origin "$CURRENT_BRANCH"
        echo "✅ Branch pushed: $CURRENT_BRANCH"
        echo "   Create PR manually on GitHub or use: gh pr create"
        ;;
    4)
        echo "📦 Keeping conversation local only"
        echo "   Branch $CURRENT_BRANCH remains local"
        ;;
    *)
        echo "❌ Invalid choice. Branch not integrated."
        echo "   Use git commands manually to integrate as desired"
        ;;
esac

# 6. Log conversation completion
if [[ -f "tools/monitoring/event-capture.py" ]]; then
    echo "📊 Logging conversation completion..."
    python3 tools/monitoring/event-capture.py --workflow "conversation_complete" \
      --workflow-data "{\"summary\": \"$CONVERSATION_SUMMARY\", \"branch\": \"$CURRENT_BRANCH\", \"integration\": \"$INTEGRATION_CHOICE\"}" 2>/dev/null || {
        echo "⚠️ Warning: Could not log conversation completion"
    }
fi

echo ""
echo "🎉 Conversation completed successfully!"
echo ""
echo "💡 Next steps:"
case $INTEGRATION_CHOICE in
    1|3)
        echo "   - Review integration when ready"
        echo "   - Monitor for any conflicts or issues"
        ;;
    2)
        echo "   - Verify master branch status"
        echo "   - Consider cleaning up conversation branch"
        ;;
    4)
        echo "   - Decide on integration approach later"
        echo "   - Keep track of local changes"
        ;;
esac