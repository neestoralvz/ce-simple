# GitHub Issues Sync - Issue Integration Functions

**31/07/2025 CDMX** | GitHub API integration for issue synchronization and state management

## AUTORIDAD SUPREMA
roadmap-update-analysis-hub.md → github-issues-sync.md implements GitHub integration per hub authority

## GITHUB INTEGRATION FUNCTIONS

### sync_github_issues()
```bash
# Sincroniza estado de todos los issues con GitHub
sync_github_issues() {
    local temp_file=$(mktemp)
    gh issue list --state=all --limit=100 --json number,title,state > "$temp_file"
    echo "$temp_file"
}
```

### detect_new_issues()
```bash
# Detecta issues nuevos no presentes en el roadmap actual
detect_new_issues() {
    local github_data="$1"
    local roadmap_file="$2"
    local new_issues=()
    
    while read -r issue; do
        local number=$(echo "$issue" | jq -r '.number')
        if ! grep -q "#$number" "$roadmap_file"; then
            new_issues+=("$issue")
        fi
    done < <(jq -c '.[]' "$github_data")
    
    printf '%s\n' "${new_issues[@]}"
}
```

### update_issue_states()
```bash
# Actualiza estados de issues en las tablas del roadmap
update_issue_states() {
    local roadmap_file="$1"
    local github_data="$2"
    local temp_file=$(mktemp)
    
    # Process each issue and update state
    while IFS= read -r line; do
        if [[ $line =~ \|\s*\*\*#([0-9]+)\*\* ]]; then
            local issue_number="${BASH_REMATCH[1]}"
            local github_state=$(jq -r ".[] | select(.number==$issue_number) | .state" "$github_data")
            
            if [[ "$github_state" == "CLOSED" ]]; then
                # Update status to CLOSED
                line=$(echo "$line" | sed 's/🟡 OPEN/✅ CLOSED/')
            elif [[ "$github_state" == "OPEN" ]]; then
                # Ensure status is OPEN
                line=$(echo "$line" | sed 's/✅ CLOSED/🟡 OPEN/')
            fi
        fi
        echo "$line" >> "$temp_file"
    done < "$roadmap_file"
    
    mv "$temp_file" "$roadmap_file"
}
```

### detect_completed_work_items()
```bash
# Detecta work items completados recientemente
detect_completed_work_items() {
    local roadmap_file="$1"
    grep -o '✅.*COMPLETED' "$roadmap_file" | cut -d'|' -f2 | sed 's/.*\*\*\(.*\)\*\*.*/\1/'
}
```

## INTEGRATION REFERENCES
**Authority Source**: ← roadmap-update-analysis-hub.md (GitHub integration authority)
**API Integration**: GitHub CLI (gh) and jq for JSON processing
**State Management**: → issue-state-detection.md (state change detection)

---
**GITHUB SYNC DECLARATION**: Complete GitHub issues synchronization providing automated state management and roadmap integration for issue tracking automation.