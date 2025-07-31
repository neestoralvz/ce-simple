# Troubleshooting Procedures - Problem Resolution Protocols

**31/07/2025 09:20 CDMX** | Troubleshooting and problem resolution procedures per git workflow authority

## AUTORIDAD SUPREMA
↑ @git-workflow-operational-procedures.md → troubleshooting-procedures.md implements problem resolution per infrastructure authority

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

## RECOVERY PROTOCOLS
**Hook System Recovery**: Systematic hook failure diagnosis and repair procedures
**Performance Optimization**: Resource analysis and performance improvement recommendations
**Tool Dependency Validation**: Automation tool availability verification and regeneration
**System Health Integration**: Complete integration with monitoring infrastructure

## INTEGRATION REFERENCES

### Hub Authority
**Git Workflow Hub**: ← git-workflow-operational-procedures.md (troubleshooting authority)
**Daily Operations**: ← daily-operational-procedures.md (operational coordination)
**Maintenance Integration**: → monitoring-maintenance-procedures.md (maintenance coordination)

---

**TROUBLESHOOTING DECLARATION**: This module preserves complete troubleshooting and problem resolution procedures maintaining recovery capability and system reliability.

**EVOLUTION PATHWAY**: Problem identification → systematic diagnosis → recovery procedures → system reliability assurance