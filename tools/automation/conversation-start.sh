#!/bin/bash
# conversation-start.sh - Standard conversation initiation
# Part of Git Workflow Analysis Implementation
# Created: 2025-07-31

set -euo pipefail

CONVERSATION_NAME="${1:-conversation-$(date +%Y%m%d-%H%M)}"
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

echo "🚀 Starting conversation: $CONVERSATION_NAME"

# Validate we're in a git repository
if [[ ! -d "$PROJECT_ROOT/.git" ]]; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

# 1. Create conversation branch and worktree
cd "$PROJECT_ROOT"
echo "📝 Creating worktree and branch..."

if git worktree list | grep -q "$CONVERSATION_NAME"; then
    echo "⚠️ Warning: Worktree $CONVERSATION_NAME already exists"
    echo "Existing worktrees:"
    git worktree list
    exit 1
fi

git worktree add "../ce-simple-$CONVERSATION_NAME" -b "$CONVERSATION_NAME"

# 2. Initialize conversation context
CONVERSATION_DIR="../ce-simple-$CONVERSATION_NAME"
cd "$CONVERSATION_DIR"

# 3. Verify tools are available
if [[ -f "tools/monitoring/event-capture.py" ]]; then
    echo "📊 Logging conversation start..."
    python3 tools/monitoring/event-capture.py --workflow "conversation_start" \
      --workflow-data "{\"branch\": \"$CONVERSATION_NAME\", \"start_time\": \"$(date -Iseconds)\", \"workspace\": \"$CONVERSATION_DIR\"}" 2>/dev/null || {
        echo "⚠️ Warning: Could not log conversation start"
    }
else
    echo "⚠️ Warning: event-capture.py not found, skipping logging"
fi

# 4. Initial health check
if [[ -f "tools/monitoring/system-health.py" ]]; then
    echo "🔍 Running initial health check..."
    python3 tools/monitoring/system-health.py --dashboard 2>/dev/null || {
        echo "⚠️ Warning: Health check failed, but continuing"
    }
else
    echo "⚠️ Warning: system-health.py not found, skipping health check"
fi

# 5. Show current status
echo ""
echo "✅ Conversation $CONVERSATION_NAME ready"
echo "📁 Workspace: $CONVERSATION_DIR"
echo "🌿 Branch: $CONVERSATION_NAME"
echo "📊 Git status:"
git status --short

echo ""
echo "💡 Next steps:"
echo "   cd $CONVERSATION_DIR"
echo "   # Start your work..."
echo "   # Use tools/automation/standard-commit.sh for commits"
echo "   # Use tools/automation/conversation-complete.sh when done"