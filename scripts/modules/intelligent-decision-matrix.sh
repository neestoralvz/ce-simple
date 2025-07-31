#!/bin/bash
# Intelligent Decision Matrix - Enhanced Decision Logic
# Extracted from handoff-init.sh with confidence scoring and authority validation

# Logging functions (minimal implementation)
log_debug() { [[ "${DEBUG:-}" == "true" ]] && echo "[DEBUG] $*" >&2; }
log_info() { echo "[INFO] $*" >&2; }
log_warning() { echo "[WARN] $*" >&2; }

# Enhanced decision analysis with confidence scoring
intelligent_decision_analysis() {
    local conversation_context="$1"
    local debug_mode="${2:-false}"
    
    # Initialize scoring variables
    local task_score=0 timeline_score=0 domain_score=0 methodology_score=0 authority_score=0
    local total_confidence=0
    
    # Criterion 1: Task Complexity Analysis (0-100 points)
    local task_count=$(echo "$conversation_context" | grep -i -o -E "(implement|create|develop|fix|update|add|remove|modify|refactor|design|build|configure|setup|integrate|migrate|transform)" | wc -l)
    local complexity_words=$(echo "$conversation_context" | grep -i -o -E "(system|architecture|framework|multiple|several|complex|comprehensive)" | wc -l)
    task_count=$((task_count + complexity_words))
    
    if [[ $task_count -gt 8 ]]; then task_score=100
    elif [[ $task_count -gt 5 ]]; then task_score=75
    elif [[ $task_count -gt 3 ]]; then task_score=50
    elif [[ $task_count -gt 1 ]]; then task_score=25
    else task_score=10
    fi
    
    # Criterion 2: Timeline Scope Analysis (0-100 points)
    if echo "$conversation_context" | grep -i -q -E "(weeks|months|phases|stages|sequential|complex)"; then
        timeline_score=90
    elif echo "$conversation_context" | grep -i -q -E "(days|multi-day|several|multiple)"; then
        timeline_score=60
    elif echo "$conversation_context" | grep -i -q -E "(hours|quick|simple|minor|small)"; then
        timeline_score=20
    else
        timeline_score=40  # Default medium complexity
    fi
    
    # Criterion 3: Cross-Domain Impact (0-100 points)
    local domain_count=$(echo "$conversation_context" | grep -i -c -E "(frontend|backend|database|api|ui|ux|system|architecture|security|infrastructure|workflow)" || true)
    if [[ $domain_count -gt 4 ]]; then domain_score=100
    elif [[ $domain_count -gt 2 ]]; then domain_score=75
    elif [[ $domain_count -gt 1 ]]; then domain_score=50
    elif [[ $domain_count -eq 1 ]]; then domain_score=25
    fi
    
    # Criterion 4: Methodology Requirements (0-100 points)
    if echo "$conversation_context" | grep -i -q -E "(framework|methodology|systematic|architecture|migration|transformation|orchestration)"; then
        methodology_score=85
    elif echo "$conversation_context" | grep -i -q -E "(template|pattern|structure|process|workflow)"; then
        methodology_score=60
    elif echo "$conversation_context" | grep -i -q -E "(standard|guidline|best-practice)"; then
        methodology_score=35
    fi
    
    # Criterion 5: Authority Integration (0-100 points)  
    if echo "$conversation_context" | grep -i -q -E "(user|vision|authority|compliance|validation|quality)"; then
        authority_score=70
    elif echo "$conversation_context" | grep -i -q -E "(standard|requirement|criteria|policy)"; then
        authority_score=50
    elif echo "$conversation_context" | grep -i -q -E "(documentation|reference|integration)"; then
        authority_score=30
    fi
    
    # Calculate total confidence with weights
    local weighted_total=$((
        (task_score * 25 / 100) + 
        (timeline_score * 20 / 100) + 
        (domain_score * 25 / 100) + 
        (methodology_score * 20 / 100) + 
        (authority_score * 10 / 100)
    ))
    total_confidence=$weighted_total
    
    # Decision logic with confidence thresholds
    local decision_type="issue"
    local decision_confidence="medium"
    
    # Emergency override detection
    if echo "$conversation_context" | grep -i -q -E "(critical|urgent|emergency|blocking|error|failure|security)"; then
        decision_type="emergency"
        decision_confidence="high"
        total_confidence=95
    # Phase detection (architectural/systematic work)
    elif echo "$conversation_context" | grep -i -q -E "(architecture|migration|transformation|system)" && [[ $methodology_score -gt 60 ]]; then
        decision_type="phase"
        decision_confidence="high"
        total_confidence=$((total_confidence + 15))
    # Phase detection (high complexity multiple criteria)
    elif [[ $methodology_score -gt 70 ]] && [[ $domain_score -gt 50 ]] && [[ $task_score -gt 50 ]]; then
        decision_type="phase"
        decision_confidence="high"
    # Handoff detection (moderate to high complexity)
    elif [[ $task_score -gt 40 ]] && [[ $domain_score -gt 25 ]] && [[ $total_confidence -gt 45 ]]; then
        decision_type="handoff"
        decision_confidence="medium"
    # Handoff detection (high single criterion)
    elif [[ $task_score -gt 65 ]] || [[ $methodology_score -gt 75 ]]; then
        decision_type="handoff"
        decision_confidence="medium"
    fi
    
    # Confidence level assessment
    if [[ $total_confidence -gt 85 ]]; then decision_confidence="high"
    elif [[ $total_confidence -gt 70 ]]; then decision_confidence="medium"
    elif [[ $total_confidence -gt 50 ]]; then decision_confidence="low"
    else decision_confidence="insufficient"
    fi
    
    # Output structured result
    echo "${decision_type}:${total_confidence}:${decision_confidence}:${task_score}:${timeline_score}:${domain_score}:${methodology_score}:${authority_score}"
    
    # Debug output if requested
    if [[ "$debug_mode" == "true" ]]; then
        log_debug "Decision Analysis: Task($task_score) Timeline($timeline_score) Domain($domain_score) Method($methodology_score) Auth($authority_score)"
        log_debug "Total Confidence: $total_confidence% -> $decision_type ($decision_confidence confidence)"
    fi
}

# Validate decision against authority chain
validate_decision_authority() {
    local decision_type="$1"
    local confidence="$2" 
    local context="$3"
    
    # Authority validation based @context/architecture/core/truth-source.md
    local authority_valid=true
    local validation_msg="Authority validation passed"
    
    if [[ "$decision_type" == "phase" ]] && [[ $confidence -lt 75 ]]; then
        authority_valid=false
        validation_msg="Phase decision requires >75% confidence (current: $confidence%)"
    elif [[ "$decision_type" == "emergency" ]] && ! echo "$context" | grep -i -q -E "(critical|urgent|emergency)"; then
        authority_valid=false  
        validation_msg="Emergency decision requires explicit urgency indicators"
    fi
    
    echo "$authority_valid:$validation_msg"
}

# Enhanced logging with decision trace
log_decision() {
    local decision_data="$1"
    local conversation_summary="$2"
    local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    
    IFS=':' read -r decision confidence level task timeline domain method auth <<< "$decision_data"
    
    cat >> "/tmp/decision_log_$(date +%Y%m%d).txt" << EOF
[$timestamp] DECISION: $decision (confidence: $confidence%, level: $level)
Criteria Scores: Task($task) Timeline($timeline) Domain($domain) Method($method) Auth($auth)  
Context: $conversation_summary
---
EOF
}