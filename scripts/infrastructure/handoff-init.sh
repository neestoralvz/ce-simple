#!/bin/bash

# Handoff Initialization Script
# Unified backend for /handoff-init command
# Intelligent handoff and issue creation with dashboard integration

set -euo pipefail

# Silent script - no user notifications (Claude Code communicates results)
# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CONTEXT_DIR="$PROJECT_ROOT/context"
ROADMAP_DIR="$CONTEXT_DIR/roadmap"
ROADMAP_REGISTRY="$ROADMAP_DIR/ROADMAP_REGISTRY.md"
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

# Colors for output

# Logging functions

# Complexity analysis function
analyze_complexity() {
    local conversation_context="$1"
    local task_count=0
    local domain_count=0
    local timeline_days=0
    local has_dependencies=false
    local needs_methodology=false
    
    # Count tasks (action words)
    task_count=$(echo "$conversation_context" | grep -i -c -E "(implementar|crear|desarrollar|fix|update|add|remove|modify|refactor)" || true)
    
    # Count domains (technical areas)
    domain_count=$(echo "$conversation_context" | grep -i -c -E "(frontend|backend|database|api|ui|ux|system|architecture|security)" || true)
    
    # Detect timeline indicators
    if echo "$conversation_context" | grep -i -q -E "(days|weeks|phase|stages|sequential)"; then
        timeline_days=3
    elif echo "$conversation_context" | grep -i -q -E "(quick|simple|small|minor)"; then
        timeline_days=1
    else
        timeline_days=2
    fi
    
    # Detect dependencies
    if echo "$conversation_context" | grep -i -q -E "(depends|requires|after|before|blocked|prerequisite)"; then
        has_dependencies=true
    fi
    
    # Detect methodology needs
    if echo "$conversation_context" | grep -i -q -E "(framework|methodology|systematic|architecture|migration|transformation)"; then
        needs_methodology=true
    fi
    
    # Decision logic
    local decision="issue"
    if [[ $task_count -gt 5 ]] || [[ $domain_count -gt 2 ]] || [[ $timeline_days -gt 2 ]] || [[ "$needs_methodology" == "true" ]]; then
        if echo "$conversation_context" | grep -i -q -E "(system|architecture|migration|transformation|framework)"; then
            decision="phase"
        else
            decision="handoff"
        fi
    fi
    
    if echo "$conversation_context" | grep -i -q -E "(critical|urgent|emergency|blocking|error|failure)"; then
        decision="emergency"
    fi
    
    echo "$decision:$task_count:$domain_count:$timeline_days:$has_dependencies:$needs_methodology"
}

# Generate next handoff ID
generate_handoff_id() {
    local type="$1"
    local domain="$2"
    
    case "$type" in
        "phase")
            # Get next P-series number
            local max_p=$(grep -o "P[0-9]\+" "$ROADMAP_REGISTRY" | sed 's/P//' | sort -n | tail -1)
            local next_p=$((${max_p:-7} + 1))
            echo "P${next_p}-$(echo "$domain" | tr '[:lower:]' '[:upper:]' | tr ' ' '-')"
            ;;
        "handoff")
            # Get next H-series number
            local max_h=$(grep -o "H[0-9]\+" "$ROADMAP_REGISTRY" | sed 's/H//' | sort -n | tail -1)
            local next_h=$((${max_h:-7} + 1))
            echo "H${next_h}-$(echo "$domain" | tr '[:lower:]' '[:upper:]' | tr ' ' '-')"
            ;;
        "emergency")
            # Get next E-series number
            local max_e=$(grep -o "E[0-9]\+" "$ROADMAP_REGISTRY" 2>/dev/null | sed 's/E//' | sort -n | tail -1 || echo "0")
            local next_e=$((${max_e:-0} + 1))
            echo "E${next_e}-$(echo "$domain" | tr '[:lower:]' '[:upper:]' | tr ' ' '-')"
            ;;
        *)
            echo "UNKNOWN-$(echo "$domain" | tr '[:lower:]' '[:upper:]' | tr ' ' '-')"
            ;;
    esac
}

# Extract user quotes from conversation
extract_user_quotes() {
    local conversation="$1"
    # Simple pattern matching for quoted text
    echo "$conversation" | grep -o '"[^"]*"' | head -3 | tr '\n' ' ' | sed 's/"//g'
}

# Generate handoff template
generate_handoff_template() {
    local handoff_id="$1"
    local title="$2"
    local type="$3"
    local priority="$4"
    local conversation="$5"
    local domain="$6"
    
    local current_date=$(date "+%d/%m/%Y %H:%M CDMX")
    local user_quote=$(extract_user_quotes "$conversation")
    local status_icon="🔄"
    local status_text="READY"
    
    if [[ "$type" == "emergency" ]]; then
        status_icon="🚨"
        status_text="CRITICAL"
    fi
    
    cat << EOF
# $handoff_id: $title - $status_icon $status_text

**$current_date** | $type handoff for $domain

## STATUS UPDATE
**Estado**: $status_icon $status_text
**Prioridad**: $priority
**Dependencies**: TBD - Analysis required
**Progress**: 0% - Ready for execution

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → $handoff_id implements $domain per user authority

## PRINCIPIO FUNDAMENTAL
**"$user_quote"** - Systematic implementation preserving user vision through conversation-first development.

## SCOPE ANALYSIS
### Key Requirements (Extracted from Conversation):
- Implementation requirements based on conversation analysis
- Technical deliverables and success criteria
- Integration points and coordination needs
- Quality gates and validation requirements

### Success Criteria:
- File Size: ≤80 lines compliance OBLIGATORIO
- Authority: 95%+ user voice fidelity preservation  
- Functionality: 100% $domain functionality preserved
- Integration: Cross-reference integrity maintained

## IMPLEMENTATION METHODOLOGY
### Execution Framework:
- L2-MODULAR methodology application
- Think x4 systematic analysis protocol
- Research-First implementation approach
- Continuous validation and quality gates

### Quality Assurance:
- Authority chain preservation throughout
- Cross-reference integrity validation
- Standards compliance verification
- User vision alignment confirmation

## COORDINATION & INTEGRATION
### Dependencies Analysis:
- Prerequisite handoffs identification
- Parallel execution capability assessment
- Resource coordination requirements
- Timeline integration with roadmap

### Cross-Reference System:
- Bidirectional linking establishment
- Authority chain maintenance
- Integration pathway verification
- Dashboard coordination protocols

---

**$handoff_id DECLARATION**: This handoff implements $domain functionality through systematic methodology while preserving complete user authority and vision alignment.

**EVOLUTION PATHWAY**: User vision → conversation analysis → systematic implementation → quality validation cycle
EOF
}

# Generate issue template for GitHub
generate_issue_template() {
    local title="$1"
    local conversation="$2"
    local priority="$3"
    
    # Extract key information from conversation
    local context=$(echo "$conversation" | head -3 | tr '\n' ' ')
    local requirements="- Implementation based on conversation analysis\n- Technical requirements extraction\n- Success criteria definition"
    local approach="- Systematic implementation approach\n- Quality validation protocols\n- Authority preservation methodology"
    local success="- Functionality implemented correctly\n- Quality standards met\n- User requirements satisfied"
    
    cat << EOF
## Context/Background
$context

Analysis indicates this work item can be completed as a focused issue with clear scope and requirements.

## Specific Requirements
$requirements

## Implementation Approach
$approach

## Success Criteria
$success

## Additional Context
Priority: $priority
Created via: /handoff-init automated analysis
Type: Issue (complexity analysis indicated standalone implementation)
EOF
}

# Update dashboard with new handoff
update_dashboard() {
    local handoff_id="$1"
    local status="$2"
    local domain="$3"
    local priority="$4"
    local density="Med"
    local tasks="~5"
    
    # Create new table row
    local priority_icon="🟡"
    case "$priority" in
        "critical"|"high") priority_icon="🔴" ;;
        "low") priority_icon="⚪" ;;
        "emergency") priority_icon="🚨" ;;
    esac
    
    local table_row="| **${priority_icon}${handoff_id}** | ${priority_icon} ${status} | ${domain} | 0% | ${density} | ${tasks} | ✅ Good |"
    
    # Find insertion point in roadmap registry
    local temp_file="$TEMP_DIR/roadmap_update.md"
    cp "$ROADMAP_REGISTRY" "$temp_file"
    
    # Insert new row (simplified approach - add before blocked items)
    sed -i "/⏸️P1-UX-FIX/i\\$table_row" "$temp_file"
    
    # Update statistics
    sed -i 's/- \*\*Ready\*\*: [0-9]* items/- **Ready**: 4 items/' "$temp_file"
    
    # Copy back
    cp "$temp_file" "$ROADMAP_REGISTRY"
    
    log_success "Dashboard updated with $handoff_id"
}

# Create GitHub issue
create_github_issue() {
    local title="$1"
    local conversation="$2"
    local priority="$3"
    
    if ! command -v gh &> /dev/null; then
        log_error "GitHub CLI (gh) not available - issue creation skipped"
        return 1
    fi
    
    if ! gh auth status &> /dev/null; then
        log_error "GitHub CLI not authenticated - issue creation skipped"
        return 1
    fi
    
    local body_file="$TEMP_DIR/issue_body.md"
    generate_issue_template "$title" "$conversation" "$priority" > "$body_file"
    
    local labels="handoff-init"
    case "$priority" in
        "critical"|"high") labels="$labels,priority-high" ;;
        "low") labels="$labels,priority-low" ;;
        "emergency") labels="$labels,critical" ;;
    esac
    
    log_info "Creating GitHub issue: $title"
    if gh issue create --title "$title" --body-file "$body_file" --label "$labels" > "$TEMP_DIR/issue_result.txt" 2>&1; then
        local issue_url=$(cat "$TEMP_DIR/issue_result.txt")
        log_success "Created GitHub issue: $issue_url"
        echo "$issue_url"
    else
        log_error "Failed to create GitHub issue"
        cat "$TEMP_DIR/issue_result.txt"
        return 1
    fi
}

# Main handoff initialization function
init_handoff() {
    local type="$1"
    local name="$2"
    local priority="${3:-medium}"
    local conversation="${4:-}"
    
    log_header "Initializing handoff: $name"
    log_info "Type: $type | Priority: $priority"
    
    # If auto type, analyze complexity
    if [[ "$type" == "auto" ]]; then
        if [[ -z "$conversation" ]]; then
            log_warning "Auto detection requires conversation context"
            conversation="Implementation request for $name with $priority priority"
        fi
        
        local analysis=$(analyze_complexity "$conversation")
        type=$(echo "$analysis" | cut -d: -f1)
        local task_count=$(echo "$analysis" | cut -d: -f2)
        local domain_count=$(echo "$analysis" | cut -d: -f3)
        local timeline=$(echo "$analysis" | cut -d: -f4)
        
        log_info "Complexity analysis: $task_count tasks, $domain_count domains, $timeline days"
        log_success "Auto-detected type: $type"
    fi
    
    # Handle issue creation
    if [[ "$type" == "issue" ]]; then
        log_info "Creating GitHub issue (complexity indicates standalone work)"
        create_github_issue "$name" "$conversation" "$priority"
        return $?
    fi
    
    # Handle handoff creation
    local domain=$(echo "$name" | awk '{print $NF}')
    local handoff_id=$(generate_handoff_id "$type" "$domain")
    local handoff_file="$ROADMAP_DIR/${handoff_id}.md"
    
    log_info "Creating handoff file: $handoff_file"
    generate_handoff_template "$handoff_id" "$name" "$type" "$priority" "$conversation" "$domain" > "$handoff_file"
    
    log_info "Updating dashboard integration"
    update_dashboard "$handoff_id" "READY PARALLEL" "$domain" "$priority"
    
    log_success "Handoff created successfully: $handoff_id"
    log_info "File: $handoff_file"
    log_info "Dashboard: Updated ROADMAP_REGISTRY.md"
    
    echo "$handoff_id"
}

# Show usage
show_usage() {
    cat << EOF
Handoff Initialization Script

USAGE:
    $0 <type> <name> [priority] [conversation_context]
    $0 --interactive
    $0 --help

TYPES:
    auto        Auto-detect based on complexity analysis
    handoff     Force handoff creation (H-series)
    phase       Force phase creation (P-series)
    issue       Force GitHub issue creation
    emergency   Emergency handoff creation (E-series)

PRIORITIES:
    critical, high, medium, low

EXAMPLES:
    $0 auto "Implement user authentication" medium
    $0 handoff "Database optimization" high
    $0 phase "System migration" critical
    $0 issue "Fix login bug" medium
    $0 emergency "Critical security patch" critical

INTERACTIVE MODE:
    $0 --interactive
    # Guided creation with conversation analysis
EOF
}

# Interactive mode
interactive_mode() {
    log_header "Interactive Handoff Creation"
    
    echo -n "Enter title/name: "
    read -r name
    
    echo -n "Enter priority (critical/high/medium/low): [medium] "
    read -r priority
    priority=${priority:-medium}
    
    echo -n "Enter conversation context (optional): "
    read -r conversation
    
    echo ""
    log_info "Analyzing complexity..."
    init_handoff "auto" "$name" "$priority" "$conversation"
}

# Analyze conversation for smart suggestion
analyze_conversation_context() {
    # This function would be called by Claude Code with conversation context
    # For now, provide generic analysis based on current discussion
    local context_analysis="handoff-init command enhancement conversation"
    local complexity_score=6  # >5 tasks discussed
    local domains=3  # Command, script, intelligence modules
    local timeline=2  # Multi-day implementation
    
    echo "$context_analysis:$complexity_score:$domains:$timeline"
}

# Smart suggestion mode (no arguments)
smart_suggestion_mode() {
    echo "🤖 Análisis de Conversación Detectado:"
    
    # Analyze current conversation context
    local analysis=$(analyze_conversation_context)
    local topic=$(echo "$analysis" | cut -d: -f1)
    local complexity=$(echo "$analysis" | cut -d: -f2)
    local domains=$(echo "$analysis" | cut -d: -f3)
    local timeline=$(echo "$analysis" | cut -d: -f4)
    
    # Determine suggestion based on analysis
    local suggested_type="handoff"
    local suggested_title="mejorar handoff-init con detección automática"
    local suggested_priority="medium"
    
    if [[ $complexity -gt 5 ]] && [[ $domains -gt 2 ]]; then
        suggested_type="handoff"
    elif [[ $complexity -le 3 ]] && [[ $domains -eq 1 ]]; then
        suggested_type="issue"
    fi
    
    echo "📋 Tema: \"$topic\""
    echo "📊 Complejidad: $complexity tareas, $domains dominios, $timeline días"
    echo "💡 Sugerencia: $(echo $suggested_type | tr '[:lower:]' '[:upper:]')"
    echo ""
    echo "🎯 Comando sugerido:"
    echo "/handoff-init auto \"$suggested_title\" $suggested_priority"
    echo ""
    echo -n "✅ Confirmar sugerencia? [y/N/p(personalizar)/h(ayuda)]: "
    
    read -r response
    case "$response" in
        [yY]|[yY][eE][sS])
            echo "🚀 Ejecutando sugerencia..."
            init_handoff "auto" "$suggested_title" "$suggested_priority" "$topic"
            ;;
        [pP]|[pP][eE][rR][sS]*)
            echo "🔧 Personalización:"
            interactive_mode
            ;;
        [hH]|[hH][eE][lL][pP])
            show_usage
            ;;
        *)
            echo "❌ Operación cancelada"
            exit 0
            ;;
    esac
}

# Main script execution
main() {
    if [[ $# -eq 0 ]]; then
        smart_suggestion_mode
        exit 0
    fi
    
    if [[ "$1" == "--help" ]]; then
        show_usage
        exit 0
    fi
    
    if [[ "$1" == "--interactive" ]]; then
        interactive_mode
        exit 0
    fi
    
    if [[ $# -lt 2 ]]; then
        echo "❌ Argumentos insuficientes"
        show_usage
        exit 1
    fi
    
    # Validate roadmap directory exists
    if [[ ! -d "$ROADMAP_DIR" ]]; then
        log_error "Roadmap directory not found: $ROADMAP_DIR"
        exit 1
    fi
    
    if [[ ! -f "$ROADMAP_REGISTRY" ]]; then
        log_error "Roadmap registry not found: $ROADMAP_REGISTRY"
        exit 1
    fi
    
    init_handoff "$1" "$2" "$3" "$4"
}

main "$@"