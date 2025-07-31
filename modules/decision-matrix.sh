#!/bin/bash
# Decision Matrix - Adaptive Learning System | **31/07/2025 CDMX**
# AUTORIDAD: @context/architecture/core/truth-source.md → authority preservation
# PRINCIPIO: Multi-dimensional scoring with dynamic threshold adjustment

DECISIONS_LOG="/Users/nalve/ce-simple/.decision-history.json"
THRESHOLDS_FILE="/Users/nalve/ce-simple/.adaptive-thresholds.json"

init_thresholds() {
    [[ ! -f "$THRESHOLDS_FILE" ]] && echo '{"task_complexity":0.65,"timeline_factor":0.55,"domain_scope":0.60,"authority_critical":0.85,"documentation_density":0.45,"adaptation_rate":0.1,"learning_decay":0.95}' > "$THRESHOLDS_FILE"
}

calculate_score() {
    local task_count=$1 timeline=$2 domains=$3 authority_level=$4 doc_lines=$5
    local task_score=$(echo "scale=3; $task_count / 10" | bc -l)
    local time_score=$(echo "scale=3; $timeline / 5" | bc -l) 
    local domain_score=$(echo "scale=3; $domains / 6" | bc -l)
    local auth_score=$(echo "scale=3; $authority_level / 3" | bc -l)
    local doc_score=$(echo "scale=3; $doc_lines / 120" | bc -l)
    python3 -c "import json; t=json.load(open('$THRESHOLDS_FILE')); print(f'{(($task_score*t[\"task_complexity\"]+$time_score*t[\"timeline_factor\"]+$domain_score*t[\"domain_scope\"]+$auth_score*t[\"authority_critical\"]+$doc_score*t[\"documentation_density\"])/5):.3f}')"
}

detect_authority_critical() {
    [[ "$1" =~ (vision|authority|user|supreme|critical) ]] && echo "1" || echo "0"
}

adjust_thresholds() {
    local decision_score=$1 outcome=$2 effectiveness=$3
    [[ ! -f "$DECISIONS_LOG" ]] && echo "[]" > "$DECISIONS_LOG"
    python3 -c "import json,time; log=json.load(open('$DECISIONS_LOG')); log.append({'timestamp':time.time(),'score':$decision_score,'outcome':'$outcome','effectiveness':$effectiveness}); log=log[-100:]; json.dump(log,open('$DECISIONS_LOG','w'))"
    python3 -c "
import json
t,log = json.load(open('$THRESHOLDS_FILE')), json.load(open('$DECISIONS_LOG'))
if len(log)>=10:
    avg_eff = sum(float(d['effectiveness']) for d in log[-10:])/10
    if avg_eff<0.85: t['task_complexity'],t['domain_scope'] = min(0.9,t['task_complexity']+t['adaptation_rate']), min(0.9,t['domain_scope']+t['adaptation_rate'])
    elif avg_eff>0.95: t['task_complexity'],t['domain_scope'] = max(0.3,t['task_complexity']-t['adaptation_rate']), max(0.3,t['domain_scope']-t['adaptation_rate'])
    t['adaptation_rate'] *= t['learning_decay']
    json.dump(t,open('$THRESHOLDS_FILE','w'),indent=2)
"
}

emergency_override() {
    local context="$1" score="$2"
    [[ "$context" =~ (VISION|USER.*AUTHORITY|SUPREME) ]] && { echo "SEQUENTIAL_REQUIRED"; return; }
    [[ "$score" > 0.95 ]] && { echo "IMMEDIATE_ESCALATION"; return; }
    [[ "$context" =~ (authority.*violation|chain.*broken) ]] && { echo "SEQUENTIAL_REQUIRED"; return; }
    echo "NORMAL_PROCESSING"
}

make_decision() {
    local task_count=$1 timeline=$2 domains=$3 context="$4" doc_lines=${5:-50}
    init_thresholds
    local authority_level=$(detect_authority_critical "$context")
    local score=$(calculate_score "$task_count" "$timeline" "$domains" "$authority_level" "$doc_lines")
    local override=$(emergency_override "$context" "$score")
    [[ "$override" != "NORMAL_PROCESSING" ]] && { echo "$override"; return; }
    local current_threshold=$(python3 -c "import json; t=json.load(open('$THRESHOLDS_FILE')); print(f'{(t[\"task_complexity\"]+t[\"domain_scope\"])/2:.3f}')")
    if (( $(echo "$score >= $current_threshold" | bc -l) )); then
        echo "ORCHESTRATE_PARALLEL"
    else
        echo "EXECUTE_DIRECT" 
    fi
}

# Usage: decision-matrix.sh <task_count> <timeline_days> <domain_count> "<context>" [doc_lines]
[[ $# -ge 4 ]] && make_decision "$@" || echo "Usage: $0 <tasks> <days> <domains> '<context>' [doc_lines]"

# COMPLETED: Multi-dimensional scoring, dynamic thresholds, authority detection, emergency override, historical learning
# AUTHORITY PRESERVATION: User vision/authority triggers SEQUENTIAL_REQUIRED override
# LEARNING CAPABILITY: Adapts thresholds based on decision effectiveness (target: 85%+ accuracy)
# EMERGENCY PROTOCOLS: Authority violations and critical scores trigger immediate escalation
# CONTINUOUS IMPROVEMENT: Learning decay prevents oscillation, maintains 100 decision history