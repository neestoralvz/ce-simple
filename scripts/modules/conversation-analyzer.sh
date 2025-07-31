#!/bin/bash
# Conversation Analyzer Module - L2-MODULAR Extraction
# Intelligent conversation analysis with optimized patterns
# Authority: @context/architecture/core/methodology.md → L2-MODULAR compliance

set -euo pipefail

# Authority Chain Validation
validate_authority_chain() {
    local content="$1"
    # Check for authority patterns in conversation
    if echo "$content" | grep -qi "@context\|CLAUDE\.md\|vision\|authority"; then
        return 0  # Authority chain detected
    fi
    return 1  # No authority chain
}

# Optimized regex patterns for improved accuracy  
declare -A PATTERNS=(
    ["tasks"]="(implementar|crear|desarrollar|build|create|implement|fix|update|add|remove|modify|refactor|design|analyze|optimize)"
    ["domains"]="(frontend|backend|database|api|ui|ux|system|architecture|security|infrastructure|analytics|monitoring)"
    ["timeline"]="(days|weeks|months|phase|stages|sequential|parallel|sprint|iteration)"
    ["quick"]="(quick|simple|small|minor|fast|immediate|urgent)"
    ["dependencies"]="(depends|requires|after|before|blocked|prerequisite|conditional|linked)"
    ["methodology"]="(framework|methodology|systematic|architecture|migration|transformation|pattern|strategy)"
    ["critical"]="(critical|urgent|emergency|blocking|error|failure|broken|crash)"
    ["authority"]="(user|authority|vision|supremacy|@context|CLAUDE\.md)"
)

# Enhanced complexity analysis with optimized patterns
analyze_complexity() {
    local conversation_context="$1"
    local task_count=0 domain_count=0 timeline_days=0
    local has_dependencies=false needs_methodology=false has_authority=false
    
    # Enhanced pattern matching with case-insensitive grep
    task_count=$(echo "$conversation_context" | grep -iEo "${PATTERNS[tasks]}" | wc -l || echo 0)
    domain_count=$(echo "$conversation_context" | grep -iEo "${PATTERNS[domains]}" | wc -l || echo 0)
    
    # Timeline detection with improved logic
    if echo "$conversation_context" | grep -iEq "${PATTERNS[timeline]}"; then
        timeline_days=3
    elif echo "$conversation_context" | grep -iEq "${PATTERNS[quick]}"; then
        timeline_days=1
    else
        timeline_days=2
    fi
    
    # Feature flags detection
    echo "$conversation_context" | grep -iEq "${PATTERNS[dependencies]}" && has_dependencies=true
    echo "$conversation_context" | grep -iEq "${PATTERNS[methodology]}" && needs_methodology=true
    validate_authority_chain "$conversation_context" && has_authority=true
    
    # Enhanced decision logic with authority consideration
    local decision="issue"
    if [[ $task_count -gt 5 ]] || [[ $domain_count -gt 2 ]] || [[ $timeline_days -gt 2 ]] || [[ "$needs_methodology" == "true" ]]; then
        if echo "$conversation_context" | grep -iEq "(system|architecture|migration|transformation|framework)"; then
            decision="phase"
        else
            decision="handoff"
        fi
    fi
    
    # Critical priority override
    echo "$conversation_context" | grep -iEq "${PATTERNS[critical]}" && decision="emergency"
    
    # Authority-aware output format
    echo "$decision:$task_count:$domain_count:$timeline_days:$has_dependencies:$needs_methodology:$has_authority"
}

# Enhanced user quote extraction with improved patterns
extract_user_quotes() {
    local conversation="$1"
    # Multi-pattern quote extraction with fallback
    {
        echo "$conversation" | grep -oE '"[^"]{10,100}"' | head -2
        echo "$conversation" | grep -oE "'[^']{10,100}'" | head -1  
        echo "$conversation" | grep -oE "> [^>]{10,80}" | head -1
    } | sed 's/[">'\'']//g' | head -3 | tr '\n' ' ' | sed 's/^ *//' | cut -c1-150
}

# Context analysis with authority validation
analyze_conversation_context() {
    local conversation="${1:-$(cat)}"
    local context_type="general"
    local complexity_score=1
    local domain_count=1
    local timeline_estimate=1
    
    # Enhanced context classification
    if echo "$conversation" | grep -iEq "${PATTERNS[methodology]}"; then
        context_type="methodology"
        complexity_score=$((complexity_score + 3))
    elif echo "$conversation" | grep -iEq "${PATTERNS[authority]}"; then
        context_type="authority"
        complexity_score=$((complexity_score + 2))
    fi
    
    # Calculate metrics from patterns
    local tasks=$(echo "$conversation" | grep -iEo "${PATTERNS[tasks]}" | wc -l)
    local domains=$(echo "$conversation" | grep -iEo "${PATTERNS[domains]}" | wc -l)
    
    complexity_score=$((complexity_score + tasks + domains))
    domain_count=$((domains > 0 ? domains : 1))
    timeline_estimate=$((tasks > 3 ? 3 : tasks > 0 ? 2 : 1))
    
    echo "$context_type:$complexity_score:$domain_count:$timeline_estimate"
}

# Export functions for external usage
export -f analyze_complexity extract_user_quotes analyze_conversation_context validate_authority_chain