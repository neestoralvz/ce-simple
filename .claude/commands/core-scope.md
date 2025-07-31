# /core-scope - Scope Management & Expansion Detection

**FUNCIÓN**: Standalone scope management + embedded issue creation + expansion detection

## EMBEDDED SCOPE MANAGEMENT PROTOCOL

**EMBEDDED SCOPE EXPANSION DETECTION**:
```bash
# Automatic scope monitoring during execution (zero external dependencies)
detect_scope_expansion() {
    local initial_tasks="${1:-}"
    local discovered_tasks="${2:-}"
    
    if [[ -z "$initial_tasks" ]] || [[ -z "$discovered_tasks" ]]; then
        echo "📊 Scope tracking: No baseline established"
        return 0
    fi
    
    local original_scope_items=$(echo "$initial_tasks" | wc -w)
    local current_scope_items=$(echo "$discovered_tasks" | wc -w)
    
    if (( original_scope_items == 0 )); then
        echo "📊 Scope baseline: $current_scope_items items discovered"
        return 0
    fi
    
    local expansion_percentage=$(( (current_scope_items - original_scope_items) * 100 / original_scope_items ))
    
    echo "📊 Scope Analysis:"
    echo "- Original scope: $original_scope_items items"
    echo "- Current scope: $current_scope_items items"
    echo "- Expansion: ${expansion_percentage}%"
    
    if (( expansion_percentage > 20 )); then
        echo "⚠️ SCOPE EXPANSION DETECTED: ${expansion_percentage}% increase"
        return 1  # Trigger issue creation
    fi
    
    echo "✅ Scope within acceptable bounds"
    return 0
}

# Embedded task classification logic
classify_discovered_task() {
    local task_description="$1"
    local estimated_effort="${2:-unknown}"
    
    # Simple classification based on keywords and effort
    case "$task_description" in
        *"fix"*|*"bug"*|*"error"*|*"typo"*)
            echo "micro-task"
            ;;
        *"implement"*|*"create"*|*"build"*|*"develop"*)
            if [[ "$estimated_effort" =~ (hour|day) ]]; then
                echo "complex-task"
            else
                echo "micro-task"
            fi
            ;;
        *"architecture"*|*"design"*|*"system"*|*"framework"*)
            echo "future-enhancement"
            ;;
        *)
            # Default classification based on description length
            local word_count=$(echo "$task_description" | wc -w)
            if (( word_count > 10 )); then
                echo "complex-task"
            else
                echo "micro-task"
            fi
            ;;
    esac
}

# Embedded issue creation logic
create_discovered_issue() {
    local discovered_task="$1"
    local priority="${2:-medium}"
    local context="${3:-No context provided}"
    local issue_file="${4:-discovered_issues.md}"
    
    echo "📝 Creating issue documentation: $discovered_task"
    
    # Classify the task
    local task_type=$(classify_discovered_task "$discovered_task")
    
    # Set priority based on classification
    case "$task_type" in
        "micro-task")
            priority="low"
            ;;
        "complex-task") 
            priority="medium"
            ;;
        "future-enhancement")
            priority="high"
            ;;
    esac
    
    # Create or append to issues file
    if [[ ! -f "$issue_file" ]]; then
        cat > "$issue_file" << EOF
# Discovered Issues & Tasks

**Generated**: $(date)
**Source**: /core-scope automatic detection

---

EOF
    fi
    
    # Add the issue
    cat >> "$issue_file" << EOF
## Issue: $discovered_task
- **Type**: $task_type
- **Priority**: $priority
- **Context**: $context
- **Discovered**: $(date)
- **Status**: pending
- **Estimated Effort**: $([ "$task_type" = "micro-task" ] && echo "<30min" || [ "$task_type" = "complex-task" ] && echo "1-3hrs" || echo "1-3 days")

EOF
    
    echo "✅ Issue documented in $issue_file"
    echo "- Type: $task_type"
    echo "- Priority: $priority"
    
    return 0
}

# Embedded GitHub issue template creation
create_github_issue_template() {
    local discovered_task="$1"
    local priority="${2:-medium}"
    local context="${3:-No context provided}"
    local template_file="github_issue_template_$(date +%Y%m%d_%H%M%S).md"
    
    echo "🐙 Creating GitHub issue template: $template_file"
    
    local task_type=$(classify_discovered_task "$discovered_task")
    
    cat > "$template_file" << EOF
---
title: "$discovered_task"
labels: ["$task_type", "priority-$priority", "auto-detected"]
assignees: []
---

## Issue Description
$discovered_task

## Context
$context

## Task Classification
- **Type**: $task_type
- **Priority**: $priority
- **Auto-detected**: $(date)

## Acceptance Criteria
- [ ] Task completed as described
- [ ] Documentation updated if needed
- [ ] Quality checks passed

## Additional Context
Automatically detected during scope expansion analysis.

Original conversation context: $context
EOF
    
    echo "✅ GitHub template created: $template_file"
    echo "📋 To create issue: Copy template content to GitHub Issues"
    
    return 0
}

# Main scope management execution
manage_scope_expansion() {
    local initial_tasks="${1:-}"
    local discovered_tasks="${2:-}"
    local create_github_template="${3:-false}"
    
    echo "📊 Starting scope management analysis..."
    
    # Detect scope expansion
    if detect_scope_expansion "$initial_tasks" "$discovered_tasks"; then
        echo "✅ Scope within acceptable bounds - no action needed"
        return 0
    fi
    
    # Process each discovered task
    local task_count=0
    while IFS= read -r task; do
        if [[ -n "$task" ]]; then
            ((task_count++))
            echo ""
            echo "📝 Processing discovered task #$task_count: $task"
            
            create_discovered_issue "$task" "medium" "Scope expansion detection"
            
            if [[ "$create_github_template" == "true" ]]; then
                create_github_issue_template "$task" "medium" "Auto-detected during scope expansion"
            fi
        fi
    done <<< "$discovered_tasks"
    
    echo ""
    echo "📊 Scope Management Summary:"
    echo "- Tasks processed: $task_count"
    echo "- Issues documented: discovered_issues.md"
    echo "- GitHub templates: $([ "$create_github_template" = "true" ] && echo "Created" || echo "Skipped")"
    
    return 0
}
```

**EMBEDDED CLASSIFICATION MATRIX**:
- **micro-task**: Fixes, typos, simple additions (<30min) → Low priority
- **complex-task**: Implementation, creation, development (1-3hrs) → Medium priority
- **future-enhancement**: Architecture, design, system changes (1-3 days) → High priority

**INTEGRATED SCOPE WORKFLOW**:
1. **DETECTA**: Automatic scope expansion detection (>20% threshold)
2. **CLASIFICA**: Embedded task classification based on keywords and complexity
3. **DOCUMENTA**: Standalone issue creation in discovered_issues.md
4. **OPCIONAL**: GitHub issue template generation for external tracking
5. **CONTINÚA**: Non-blocking workflow - issues logged for follow-up

**INTEGRATION**: Completely self-contained scope management with embedded issue creation and classification logic