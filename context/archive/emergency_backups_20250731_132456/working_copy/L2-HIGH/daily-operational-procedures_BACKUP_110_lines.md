# Daily Operational Procedures - Core Git Workflow Operations

**31/07/2025 09:20 CDMX** | Daily operational procedures per git workflow authority

## AUTORIDAD SUPREMA
↑ @git-workflow-operational-procedures.md → daily-operational-procedures.md implements daily Git operations per infrastructure authority

## DAILY OPERATIONAL PROCEDURES

### Morning System Health Check
```bash
# 1. System health validation
python3 tools/monitoring/system-health.py --dashboard

# 2. Git repository status
git status
git log --oneline -5

# 3. Hook system verification
ls -la .git/hooks/ | grep -E "(pre-commit|post-commit|pre-push|post-merge|commit-msg)"

# 4. Performance baseline
python3 tools/monitoring/event-capture.py --summary 24
```

### Conversation Initiation Procedure
```bash
#!/bin/bash
# conversation-start.sh - Standard conversation initiation

CONVERSATION_NAME="${1:-conversation-$(date +%Y%m%d-%H%M)}"
PROJECT_ROOT="/Users/nalve/ce-simple"

echo "🚀 Starting conversation: $CONVERSATION_NAME"

# 1. Create conversation branch and worktree
cd "$PROJECT_ROOT"
git worktree add "../ce-simple-$CONVERSATION_NAME" -b "$CONVERSATION_NAME"

# 2. Initialize conversation context
cd "../ce-simple-$CONVERSATION_NAME"

# 3. Log conversation start
python3 tools/monitoring/event-capture.py --workflow "conversation_start" \
  --workflow-data "{\"branch\": \"$CONVERSATION_NAME\", \"start_time\": \"$(date -Iseconds)\"}"

# 4. Initial health check
python3 tools/monitoring/system-health.py --dashboard

echo "✅ Conversation $CONVERSATION_NAME ready"
echo "📁 Workspace: ../ce-simple-$CONVERSATION_NAME"
```

### Standard Commit Procedure
```bash
#!/bin/bash
# standard-commit.sh - Standardized commit with validation

COMMIT_MESSAGE="$1"

if [[ -z "$COMMIT_MESSAGE" ]]; then
    echo "❌ Error: Commit message required"
    echo "Usage: bash standard-commit.sh 'Your commit message'"
    exit 1
fi

echo "📝 Preparing commit: $COMMIT_MESSAGE"

# 1. Pre-commit validation
echo "🔍 Running pre-commit checks..."
git add .

# 2. Think x4 validation (if applicable)
ANALYSIS_FILES=$(git diff --cached --name-only | grep -E "\.(md|txt)$" | head -1)
if [[ -n "$ANALYSIS_FILES" ]]; then
    bash tools/automation/think-x4-validator.sh "$ANALYSIS_FILES" || {
        echo "⚠️ Think x4 validation issues detected"
        echo "Continue anyway? (y/N)"
        read -n 1 -r
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    }
fi

# 3. Execute commit
git commit -m "$COMMIT_MESSAGE

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# 4. Post-commit logging
python3 tools/monitoring/event-capture.py --workflow "commit_completed" \
  --workflow-data "{\"message\": \"$COMMIT_MESSAGE\", \"branch\": \"$(git branch --show-current)\"}"

echo "✅ Commit completed successfully"
```

## INTEGRATION REFERENCES

### Hub Authority
**Git Workflow Hub**: ← git-workflow-operational-procedures.md (daily operations authority)
**System Integration**: → troubleshooting-procedures.md (problem resolution coordination)
**Monitoring Integration**: → monitoring-maintenance-procedures.md (maintenance coordination)

---

**DAILY PROCEDURES DECLARATION**: This module preserves complete daily Git workflow operations maintaining procedural integrity and monitoring integration.

**EVOLUTION PATHWAY**: Health check → conversation management → commit procedures → systematic workflow execution