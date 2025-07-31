# Git Workflow Operational Procedures - Daily Operations Authority

**31/07/2025 09:20 CDMX** | Operational procedures for Git workflow system

## AUTORIDAD SUPREMA
@context/architecture/claude-code.md → git-workflow-operational-procedures.md implements daily Git operations per Claude Code integration authority

## PRINCIPIO FUNDAMENTAL
**"Systematic procedures ensure consistent Git workflow execution while maintaining conversation-first development"** - All Git operations follow established procedures with monitoring and validation.

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

### Conversation Completion Procedure
```bash
#!/bin/bash
# conversation-complete.sh - Standard conversation completion

CONVERSATION_SUMMARY="$1"

if [[ -z "$CONVERSATION_SUMMARY" ]]; then
    echo "❌ Error: Conversation summary required"
    echo "Usage: bash conversation-complete.sh 'Conversation summary'"
    exit 1
fi

CURRENT_BRANCH=$(git branch --show-current)
echo "🏁 Completing conversation on branch: $CURRENT_BRANCH"

# 1. Final system health check
echo "🔍 Final health validation..."
python3 tools/monitoring/system-health.py --report > "conversation-health-report.json"

# 2. Documentation updates (if handoff exists)
if [[ -f "context/roadmap/HANDOFF_*.md" ]]; then
    echo "📋 Updating handoff documentation..."
    # Update handoff status to COMPLETED
fi

# 3. Final commit with conversation summary
echo "📝 Creating final commit..."
git add .
git commit -m "CONVERSATION COMPLETE: $CONVERSATION_SUMMARY

Final commit for conversation on branch $CURRENT_BRANCH.
System health validated, all procedures followed.

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# 4. Integration decision prompt
echo "🔄 Integration options:"
echo "1. Push branch for later integration"
echo "2. Merge to master immediately"  
echo "3. Create pull request"
echo "Select option (1-3): "
read -n 1 -r INTEGRATION_CHOICE

case $INTEGRATION_CHOICE in
    1)
        git push -u origin "$CURRENT_BRANCH"
        echo "✅ Branch pushed: $CURRENT_BRANCH"
        ;;
    2)
        git checkout master
        git merge "$CURRENT_BRANCH"
        git push origin master
        echo "✅ Merged to master and pushed"
        ;;
    3)
        git push -u origin "$CURRENT_BRANCH"
        echo "✅ Branch pushed. Create PR manually on GitHub"
        ;;
    *)
        echo "❌ Invalid choice. Branch not integrated."
        ;;
esac

# 5. Log conversation completion
python3 tools/monitoring/event-capture.py --workflow "conversation_complete" \
  --workflow-data "{\"summary\": \"$CONVERSATION_SUMMARY\", \"branch\": \"$CURRENT_BRANCH\", \"integration\": \"$INTEGRATION_CHOICE\"}"

echo "🎉 Conversation completed successfully!"
```

## TROUBLESHOOTING PROCEDURES

### Git Hook Failure Recovery
```bash
#!/bin/bash
# hook-recovery.sh - Recover from hook failures

echo "🔧 Git Hook Recovery Procedure"

# 1. Identify failing hook
HOOK_DIR=".git/hooks"
echo "📋 Checking hook status..."

for hook in pre-commit post-commit pre-push post-merge commit-msg; do
    if [[ -f "$HOOK_DIR/$hook" ]]; then
        if [[ -x "$HOOK_DIR/$hook" ]]; then
            echo "✅ $hook: executable"
        else
            echo "❌ $hook: not executable - fixing..."
            chmod +x "$HOOK_DIR/$hook"
        fi
    else
        echo "❌ $hook: missing"
    fi
done

# 2. Test hook execution
echo "🧪 Testing hook execution..."
echo "Test commit message" > /tmp/test-commit-msg
bash "$HOOK_DIR/commit-msg" /tmp/test-commit-msg && echo "✅ commit-msg working" || echo "❌ commit-msg failed"

# 3. Validate tools dependencies
echo "🔍 Validating tool dependencies..."
[[ -f "tools/automation/think-x4-validator.sh" ]] && echo "✅ think-x4-validator.sh" || echo "❌ think-x4-validator.sh missing"
[[ -f "tools/monitoring/event-capture.py" ]] && echo "✅ event-capture.py" || echo "❌ event-capture.py missing"

# 4. Regenerate missing tools if needed
if [[ ! -f "tools/automation/think-x4-validator.sh" ]]; then
    echo "🔨 Regenerating think-x4-validator.sh..."
    # Tool would be recreated here
fi

echo "🔧 Hook recovery completed"
```

### Performance Issue Diagnosis
```bash
#!/bin/bash
# performance-diagnosis.sh - Diagnose Git workflow performance issues

echo "📊 Git Workflow Performance Diagnosis"

# 1. System resource check
echo "💾 System Resources:"
python3 tools/monitoring/system-health.py --dashboard | jq '.summary.system'

# 2. Git operation timing
echo "⏱️ Git Operation Performance:"
time git status
time git log --oneline -10

# 3. Hook execution timing
echo "🪝 Hook Performance:"
time bash .git/hooks/pre-commit --test 2>/dev/null || echo "Pre-commit test not available"

# 4. Repository size analysis
echo "📈 Repository Analysis:"
git count-objects -vH

# 5. Performance recommendations
echo "💡 Performance Recommendations:"
REPO_SIZE=$(git count-objects -vH | grep "size-pack" | awk '{print $2}')
if [[ "${REPO_SIZE%.*}" -gt 100000 ]]; then
    echo "⚠️ Large repository detected. Consider git gc or filtering"
fi

FILE_COUNT=$(find . -type f | wc -l)
if [[ $FILE_COUNT -gt 10000 ]]; then
    echo "⚠️ High file count detected. Consider archiving old files"
fi
```

## MONITORING AND MAINTENANCE

### Weekly Maintenance Procedure
```bash
#!/bin/bash
# weekly-maintenance.sh - Weekly Git workflow maintenance

echo "🧹 Weekly Git Workflow Maintenance"

# 1. Repository cleanup
echo "🗑️ Repository cleanup..."
git gc --aggressive
git prune

# 2. Health report generation
echo "📊 Generating health reports..."
python3 tools/monitoring/system-health.py --report > "weekly-health-$(date +%Y%m%d).json"
python3 tools/monitoring/event-capture.py --summary 168 > "weekly-events-$(date +%Y%m%d).json"

# 3. Performance baseline update
echo "📈 Performance baseline update..."
echo "$(date -Iseconds): $(python3 tools/monitoring/system-health.py --dashboard | jq -r '.summary.performance.avg_time')" >> "performance-baseline.log"

# 4. Archive old conversation branches
echo "📦 Conversation branch analysis..."
git branch -r | grep -E "conversation-|handoff-" | head -10

echo "🎯 Weekly maintenance completed"
```

### Emergency Recovery Procedures
```bash
#!/bin/bash  
# emergency-recovery.sh - Emergency Git workflow recovery

echo "🚨 Emergency Git Workflow Recovery"

# 1. Backup current state
echo "💾 Creating emergency backup..."
git stash push -m "Emergency backup $(date -Iseconds)"

# 2. Repository integrity check
echo "🔍 Repository integrity check..."
git fsck --full

# 3. Reset to known good state
echo "🔄 Reset options:"
echo "1. Reset to last known good commit"
echo "2. Reset to master branch"
echo "3. Manual recovery mode"
echo "Select option (1-3): "
read -n 1 -r RECOVERY_CHOICE

case $RECOVERY_CHOICE in
    1)
        LAST_GOOD=$(git log --oneline -10 | grep -E "(✅|COMPLETED)" | head -1 | cut -d' ' -f1)
        if [[ -n "$LAST_GOOD" ]]; then
            git reset --hard "$LAST_GOOD"
            echo "✅ Reset to last good commit: $LAST_GOOD"
        else
            echo "❌ No good commit found"
        fi
        ;;
    2)
        git checkout master
        git reset --hard origin/master
        echo "✅ Reset to master"
        ;;
    3)
        echo "🔧 Manual recovery mode activated"
        echo "Use git commands manually to recover"
        ;;
esac

echo "🚨 Emergency recovery completed"
```

---

**OPERATIONAL PROCEDURES DECLARATION**: These procedures ensure systematic Git workflow execution with monitoring, validation, and recovery capabilities supporting conversation-first development.

**USAGE**: All procedures are bash-executable and integrate with existing monitoring infrastructure for consistent workflow management.