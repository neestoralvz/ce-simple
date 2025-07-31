#!/bin/bash
# standard-commit.sh - Standardized commit with validation
# Part of Git Workflow Analysis Implementation
# Created: 2025-07-31

set -euo pipefail

COMMIT_MESSAGE="$1"

if [[ -z "$COMMIT_MESSAGE" ]]; then
    echo "❌ Error: Commit message required"
    echo "Usage: bash tools/automation/standard-commit.sh 'Your commit message'"
    exit 1
fi

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "📝 Preparing commit: $COMMIT_MESSAGE"

# 1. Check if we're in a git repository
if [[ ! -d ".git" ]]; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

# 2. Pre-commit validation
echo "🔍 Running pre-commit checks..."
git add .

# Show what will be committed
STAGED_FILES=$(git diff --cached --name-only)
if [[ -n "$STAGED_FILES" ]]; then
    echo "📋 Files to be committed:"
    echo "$STAGED_FILES" | head -10
    if [[ $(echo "$STAGED_FILES" | wc -l) -gt 10 ]]; then
        echo "... and $(( $(echo "$STAGED_FILES" | wc -l) - 10 )) more files"
    fi
else
    echo "⚠️ No staged files found"
    exit 1
fi

# 3. Think x4 validation (if applicable and tool exists)
if [[ -f "tools/automation/think-x4-validator.sh" ]]; then
    ANALYSIS_FILES=$(git diff --cached --name-only | grep -E "\.(md|txt)$" | head -1 || true)
    if [[ -n "$ANALYSIS_FILES" ]]; then
        echo "🧠 Running Think x4 validation..."
        if ! bash tools/automation/think-x4-validator.sh --validate "$ANALYSIS_FILES" 2>/dev/null; then
            echo "⚠️ Think x4 validation issues detected"
            echo "Continue anyway? (y/N)"
            read -n 1 -r
            echo  # New line after input
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                echo "❌ Commit aborted"
                exit 1
            fi
        fi
    fi
else
    echo "ℹ️ Think x4 validator not found, skipping validation"
fi

# 4. Execute commit with standardized format
CURRENT_BRANCH=$(git branch --show-current)
git commit -m "$COMMIT_MESSAGE

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# 5. Post-commit logging
if [[ -f "tools/monitoring/event-capture.py" ]]; then
    echo "📊 Logging commit completion..."
    python3 tools/monitoring/event-capture.py --workflow "commit_completed" \
      --workflow-data "{\"message\": \"$COMMIT_MESSAGE\", \"branch\": \"$CURRENT_BRANCH\", \"files_count\": $(echo "$STAGED_FILES" | wc -l)}" 2>/dev/null || {
        echo "⚠️ Warning: Could not log commit completion"
    }
fi

echo "✅ Commit completed successfully on branch: $CURRENT_BRANCH"
echo "📊 Commit hash: $(git rev-parse --short HEAD)"