# Git Integration Standards - Session-Completion Workflow Tracking

## 🎯 Purpose
Define standardized Git integration patterns for workflow commands to enable automatic session-completion tracking, quality metrics, and collaboration features.

## 🔧 Core Integration Patterns

### Session-Completion Commit Protocol
**PRINCIPLE**: Git operations only execute on successful workflow completion
**TIMING**: Post-execution commit with comprehensive metrics
**FORMAT**: Structured commit messages with actionable intelligence

### Standard Commit Message Structure
```bash
git add . && git commit -m "[command]: [operation] | [key-metric] | [X]min | [outcome]

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

## 📊 Metric Integration Functions

### Quality Score Tracking
```bash
function capture_quality_metrics() {
    local before_score="$1"
    local after_score="$2"
    local delta=$((after_score - before_score))
    
    echo "Quality Score: ${before_score}% → ${after_score}% (+${delta}%)"
}

function assess_quality_threshold() {
    local score="$1"
    local threshold="${2:-85}"
    
    if [ "$score" -ge "$threshold" ]; then
        echo "✅ Threshold: Achieved (${score}% ≥ ${threshold}%)"
    else
        echo "⚠️ Threshold: Below target (${score}% < ${threshold}%)"
    fi
}
```

### File Change Analytics
```bash
function count_file_changes() {
    local files_modified=$(git diff --cached --name-only | wc -l)
    local lines_added=$(git diff --cached --numstat | awk '{sum+=$1} END {print sum}')
    local lines_removed=$(git diff --cached --numstat | awk '{sum+=$2} END {print sum}')
    
    echo "Files: ${files_modified}, Lines: +${lines_added}/-${lines_removed}"
}

function identify_change_types() {
    local new_files=$(git diff --cached --name-status | grep "^A" | wc -l)
    local modified_files=$(git diff --cached --name-status | grep "^M" | wc -l)
    local deleted_files=$(git diff --cached --name-status | grep "^D" | wc -l)
    
    echo "Changes: ${new_files} new, ${modified_files} modified, ${deleted_files} deleted"
}
```

### Workflow Intelligence Capture
```bash
function capture_execution_context() {
    local command_name="$1"
    local execution_mode="$2"
    local start_time="$3"
    local end_time="$4"
    
    local duration=$((end_time - start_time))
    local current_branch=$(git branch --show-current)
    local last_commit=$(git log -1 --format="%h %s" 2>/dev/null || echo "No previous commits")
    
    echo "Context: ${command_name} [${execution_mode}] on ${current_branch} (${duration}s)"
}

function generate_next_recommendations() {
    local quality_score="$1"
    local issues_count="$2"
    
    if [ "$quality_score" -ge 95 ]; then
        echo "System: Excellent health - consider maintenance schedule optimization"
    elif [ "$quality_score" -ge 85 ]; then
        echo "System: Good health - monitor for emerging patterns"
    elif [ "$issues_count" -gt 0 ]; then
        echo "System: Attention needed - address ${issues_count} pending issues"
    else
        echo "System: Below threshold - recommend full workflow analysis"
    fi
}
```

## 🔄 Workflow-Specific Integration

### Documentation Workflow Patterns
**docs-workflow Integration**:
- Pre-execution baseline capture
- Phase-by-phase progress tracking
- Quality improvement measurement
- Recursive iteration documentation

**docs-generate Integration**:
- 3-wave execution tracking
- Parallel agent performance metrics
- Cross-reference network analysis
- Template compliance measurement

**docs-audit Integration**:
- System health assessment capture
- Issue identification and categorization
- Baseline establishment for future comparisons
- Trend analysis preparation

### Error Recovery Integration
```bash
function commit_partial_success() {
    local command_name="$1"
    local completed_phases="$2"
    local pending_issues="$3"
    local recovery_actions="$4"
    
    git add . && git commit -m "${command_name}: partial | ${pending_issues} pending | next: ${recovery_actions}

🤖 Generated with Claude Code - Partial
Co-Authored-By: Claude <noreply@anthropic.com>"
}

function commit_error_recovery() {
    local command_name="$1"
    local error_context="$2"
    local recovery_success="$3"
    
    git add . && git commit -m "${command_name}: recovery | ${error_context} | status: ${recovery_success}

🤖 Generated with Claude Code - Recovery
Co-Authored-By: Claude <noreply@anthropic.com>"
}
```

## 🎯 Collaboration Features

### Multi-User Workflow Support
```bash
function check_collaboration_context() {
    local current_user=$(git config user.name)
    local last_author=$(git log -1 --format="%an" 2>/dev/null || echo "Unknown")
    local branch_ahead=$(git rev-list --count @{u}..HEAD 2>/dev/null || echo "0")
    local branch_behind=$(git rev-list --count HEAD..@{u} 2>/dev/null || echo "0")
    
    echo "User: ${current_user} | Last: ${last_author} | Sync: +${branch_ahead}/-${branch_behind}"
}

function suggest_collaboration_actions() {
    local branch_ahead="$1"
    local branch_behind="$2"
    
    if [ "$branch_behind" -gt 0 ]; then
        echo "🔄 Recommend: git pull before next workflow execution"
    elif [ "$branch_ahead" -gt 3 ]; then
        echo "📤 Recommend: git push to share recent improvements"
    else
        echo "✅ Collaboration: Repository sync optimal"
    fi
}
```

### Branch Strategy Integration
```bash
function create_experimental_branch() {
    local workflow_type="$1"
    local risk_level="$2"
    local timestamp=$(date +%Y%m%d-%H%M)
    
    if [ "$risk_level" = "high" ]; then
        local branch_name="experiment-${workflow_type}-${timestamp}"
        git checkout -b "$branch_name"
        echo "🧪 Experimental branch created: ${branch_name}"
    fi
}

function assess_merge_readiness() {
    local quality_score="$1"
    local issues_count="$2"
    local branch_name=$(git branch --show-current)
    
    if [ "$quality_score" -ge 85 ] && [ "$issues_count" -eq 0 ]; then
        echo "✅ Merge Ready: Quality ${quality_score}%, No issues (git checkout main && git merge ${branch_name})"
    else
        echo "⚠️ Review Required: Quality ${quality_score}%, Issues ${issues_count} (manual review needed)"
    fi
}
```

## 📊 Analytics and Intelligence

### Historical Analysis Functions
```bash
function calculate_workflow_trends() {
    local days="${1:-30}"
    local workflow_executions=$(git log --grep="Generated with Claude Code" --since="${days} days ago" --format="%ai" | wc -l)
    local avg_frequency=$(echo "scale=2; ${workflow_executions} / ${days} * 7" | bc 2>/dev/null || echo "N/A")
    
    echo "Trend: ${workflow_executions} executions in ${days} days (${avg_frequency} per week)"
}

function identify_quality_patterns() {
    local quality_improvements=$(git log --grep="Quality Score.*→.*%" --since="30 days ago" | grep -o '+[0-9]*%' | wc -l)
    local quality_regressions=$(git log --grep="Quality Score.*→.*%" --since="30 days ago" | grep -o '\-[0-9]*%' | wc -l)
    
    echo "Quality Patterns: ${quality_improvements} improvements, ${quality_regressions} regressions"
}
```

### Predictive Intelligence
```bash
function suggest_optimal_execution_time() {
    local recent_executions=$(git log --grep="Duration.*minutes" --since="14 days ago" --format="%ai %s")
    local avg_duration=$(echo "$recent_executions" | grep -o '[0-9]* minutes' | awk '{sum+=$1; count++} END {print sum/count}' 2>/dev/null || echo "N/A")
    
    echo "Performance: Average execution ${avg_duration} minutes (optimal window identified)"
}

function recommend_maintenance_schedule() {
    local last_workflow=$(git log --grep="docs-workflow" -1 --format="%ar" 2>/dev/null || echo "Never")
    local last_audit=$(git log --grep="docs-audit" -1 --format="%ar" 2>/dev/null || echo "Never")
    
    echo "Maintenance: Last workflow ${last_workflow}, Last audit ${last_audit}"
}
```

## ⚡ Implementation Guidelines

### Integration Requirements
- **Success-Only Commits**: Only commit on successful workflow completion
- **Structured Messages**: Follow standard format for consistency and parseability
- **Metric Capture**: Include quantitative data for trend analysis
- **Intelligence Generation**: Provide actionable insights and recommendations

### Error Handling
- **Partial Success**: Document completed phases and recovery plans
- **Failure Recovery**: Track error resolution patterns for system improvement
- **Rollback Safety**: Maintain ability to revert to previous stable state

### Collaboration Standards
- **Multi-User Support**: Context-aware commit messages with user information
- **Branch Strategy**: Experimental branches for high-risk operations
- **Sync Awareness**: Monitor and recommend collaboration synchronization

---

**CRITICAL**: This integration operates on session-completion principle, ensuring Git operations enhance rather than impede workflow execution while providing comprehensive tracking and collaboration capabilities.