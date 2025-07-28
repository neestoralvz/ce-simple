#!/bin/bash

# Git-Based Intelligence Automation Engine
# Purpose: Automated Git metrics collection and intelligent orchestration decisions
# Authority: implements user-input/technical-requirements/technical-architecture-user.md Git-Based Intelligence
# Status: Core automation system for VDD framework

set -euo pipefail

# ============================================================================
# CONFIGURATION
# ============================================================================

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
readonly METRICS_DIR="$PROJECT_ROOT/data/git-metrics"
readonly LOG_FILE="$METRICS_DIR/intelligence.log"

# Ensure metrics directory exists
mkdir -p "$METRICS_DIR"

# ============================================================================
# LOGGING FUNCTIONS
# ============================================================================

log_info() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] INFO: $*" | tee -a "$LOG_FILE"
}

log_error() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $*" >&2 | tee -a "$LOG_FILE"
}

# ============================================================================
# GIT METRICS COLLECTION
# ============================================================================

collect_commit_patterns() {
    log_info "Collecting commit pattern analysis..."
    
    local output_file="$METRICS_DIR/commit-patterns.json"
    
    # Collect commit data safely
    {
        echo "{"
        echo "  \"metadata\": {"
        echo "    \"collected_at\": \"$(date -Iseconds)\","
        echo "    \"project_root\": \"$PROJECT_ROOT\","
        echo "    \"analysis_period\": \"30_days\""
        echo "  },"
        echo "  \"commits\": ["
        
        local first=true
        git log --since="30 days ago" --pretty=format:'%H|%ai|%an|%s|%d' | \
        while IFS='|' read -r hash date author message files_changed; do
            if [ "$first" = false ]; then echo ","; fi
            first=false
            
            # Escape JSON strings safely
            hash=$(printf '%s' "$hash" | sed 's/"/\\"/g')
            date=$(printf '%s' "$date" | sed 's/"/\\"/g')
            author=$(printf '%s' "$author" | sed 's/"/\\"/g')
            message=$(printf '%s' "$message" | sed 's/"/\\"/g')
            files_changed=$(printf '%s' "$files_changed" | sed 's/[^0-9]//g')
            
            # Default to 1 if files_changed is empty
            if [[ -z "$files_changed" ]]; then
                files_changed="1"
            fi
            
            echo "    {"
            echo "      \"hash\": \"$hash\","
            echo "      \"date\": \"$date\","
            echo "      \"author\": \"$author\","
            echo "      \"message\": \"$message\","
            echo "      \"files_changed\": $files_changed"
            echo -n "    }"
        done
        
        echo
        echo "  ]"
        echo "}"
    } > "$output_file"
    
    log_info "Commit patterns saved to $output_file"
}

collect_branch_lifecycle() {
    log_info "Collecting branch lifecycle metrics..."
    
    local output_file="$METRICS_DIR/branch-lifecycle.json"
    
    # Analyze branch creation, merge success, and lifecycle
    {
        echo "{"
        echo "  \"metadata\": {"
        echo "    \"collected_at\": \"$(date -Iseconds)\","
        echo "    \"analysis_period\": \"90_days\""
        echo "  },"
        echo "  \"branches\": ["
        
        local first=true
        git for-each-ref --format='%(refname:short) %(committerdate:iso8601) %(authorname)' refs/heads/ | \
        while read -r branch date author; do
            if [ "$first" = false ]; then echo ","; fi
            first=false
            
            local merge_count=$(git log --oneline --merges --grep="$branch" --since="90 days ago" | wc -l)
            local commit_count=$(git rev-list --count --since="90 days ago" "$branch" 2>/dev/null || echo "0")
            
            echo "    {"
            echo "      \"name\": \"$branch\","
            echo "      \"last_commit_date\": \"$date\","
            echo "      \"author\": \"$author\","
            echo "      \"commit_count_90d\": $commit_count,"
            echo "      \"merge_count_90d\": $merge_count"
            echo -n "    }"
        done
        
        echo
        echo "  ]"
        echo "}"
    } > "$output_file"
    
    log_info "Branch lifecycle saved to $output_file"
}

collect_merge_success_metrics() {
    log_info "Collecting merge success tracking..."
    
    local output_file="$METRICS_DIR/merge-success.json"
    
    # Analyze merge conflicts and success rates
    local total_merges=$(git log --oneline --merges --since="60 days ago" | wc -l)
    local successful_merges=$(git log --oneline --merges --grep="Merge" --since="60 days ago" | wc -l)
    local conflict_indicators=$(git log --oneline --grep="conflict\|fix merge\|resolve" --since="60 days ago" | wc -l)
    
    jq -n \
    --arg timestamp "$(date -Iseconds)" \
    --argjson total_merges "$total_merges" \
    --argjson successful_merges "$successful_merges" \
    --argjson conflict_indicators "$conflict_indicators" \
    '{
      metadata: {
        collected_at: $timestamp,
        analysis_period: "60_days"
      },
      metrics: {
        total_merges: $total_merges,
        successful_merges: $successful_merges,
        conflict_indicators: $conflict_indicators,
        success_rate: (if $total_merges > 0 then ($successful_merges / $total_merges * 100) else 0 end),
        conflict_rate: (if $total_merges > 0 then ($conflict_indicators / $total_merges * 100) else 0 end)
      }
    }' > "$output_file"
    
    log_info "Merge success metrics saved to $output_file"
}

collect_performance_timeline() {
    log_info "Collecting performance timeline data..."
    
    local output_file="$METRICS_DIR/performance-timeline.json"
    
    # Analyze commit timing patterns for performance insights
    {
        echo "{"
        echo "  \"metadata\": {"
        echo "    \"collected_at\": \"$(date -Iseconds)\","
        echo "    \"analysis_period\": \"60_days\""
        echo "  },"
        echo "  \"timeline\": ["
        
        local first=true
        git log --since="60 days ago" --pretty=format:'%ai|%H|%s' | \
        while IFS='|' read -r date hash message; do
            if [ "$first" = false ]; then echo ","; fi
            first=false
            
            # Escape JSON strings safely
            date=$(printf '%s' "$date" | sed 's/"/\\"/g')
            hash=$(printf '%s' "$hash" | sed 's/"/\\"/g')
            message=$(printf '%s' "$message" | sed 's/"/\\"/g')
            
            echo "    {"
            echo "      \"date\": \"$date\","
            echo "      \"hash\": \"$hash\","
            echo "      \"message\": \"$message\""
            echo -n "    }"
        done
        
        echo
        echo "  ]"
        echo "}"
    } > "$output_file"
    
    log_info "Performance timeline saved to $output_file"
}

# ============================================================================
# INTELLIGENT DECISION SYSTEM
# ============================================================================

analyze_orchestration_patterns() {
    log_info "Analyzing orchestration patterns for intelligent decisions..."
    
    local analysis_file="$METRICS_DIR/orchestration-analysis.json"
    
    # Combine all metrics for pattern analysis
    if [[ -f "$METRICS_DIR/commit-patterns.json" && -f "$METRICS_DIR/branch-lifecycle.json" && -f "$METRICS_DIR/merge-success.json" ]]; then
        
        local commit_frequency=$(jq '.commits | length' "$METRICS_DIR/commit-patterns.json")
        local active_branches=$(jq '.branches | map(select(.commit_count_90d > 0)) | length' "$METRICS_DIR/branch-lifecycle.json")
        local merge_success_rate=$(jq '.metrics.success_rate' "$METRICS_DIR/merge-success.json")
        
        # Generate intelligent orchestration recommendations
        jq -n \
        --arg timestamp "$(date -Iseconds)" \
        --argjson commit_freq "$commit_frequency" \
        --argjson active_branches "$active_branches" \
        --argjson merge_success "$merge_success_rate" \
        '{
          metadata: {
            analyzed_at: $timestamp,
            data_sources: ["commit-patterns", "branch-lifecycle", "merge-success"]
          },
          current_state: {
            commit_frequency_30d: $commit_freq,
            active_branches: $active_branches,
            merge_success_rate: $merge_success
          },
          recommendations: {
            parallelization_level: (
              if $commit_freq > 50 and $merge_success > 80 then "high"
              elif $commit_freq > 20 and $merge_success > 60 then "medium"
              else "conservative"
              end
            ),
            suggested_agents: (
              if $commit_freq > 50 then 8
              elif $commit_freq > 20 then 5
              else 3
              end
            ),
            risk_assessment: (
              if $merge_success < 50 then "high_risk"
              elif $merge_success < 80 then "medium_risk"
              else "low_risk"
              end
            )
          }
        }' > "$analysis_file"
        
        log_info "Orchestration analysis saved to $analysis_file"
    else
        log_error "Missing required metrics files for orchestration analysis"
        return 1
    fi
}

# ============================================================================
# AUTOMATION INTEGRATION
# ============================================================================

integrate_with_vdd_commands() {
    log_info "Integrating Git intelligence with VDD commands..."
    
    # Create integration file for commands to read
    local integration_file="$METRICS_DIR/vdd-integration.json"
    
    if [[ -f "$METRICS_DIR/orchestration-analysis.json" ]]; then
        local recommendations=$(jq '.recommendations' "$METRICS_DIR/orchestration-analysis.json")
        
        jq -n \
        --arg timestamp "$(date -Iseconds)" \
        --argjson recommendations "$recommendations" \
        '{
          integration: {
            updated_at: $timestamp,
            status: "active",
            git_intelligence_enabled: true
          },
          orchestration_settings: $recommendations,
          usage_instructions: {
            description: "Git-based intelligence settings for VDD command orchestration",
            access_method: "Source this file in commands or read parallelization_level",
            example: "PARALLELIZATION=$(jq -r \".orchestration_settings.parallelization_level\" \"$integration_file\")"
          }
        }' > "$integration_file"
        
        log_info "VDD integration file created at $integration_file"
    else
        log_error "Cannot create integration file: orchestration analysis missing"
        return 1
    fi
}

# ============================================================================
# MAIN EXECUTION
# ============================================================================

main() {
    log_info "Starting Git-Based Intelligence Engine..."
    
    # Verify we're in a git repository
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        log_error "Not in a git repository. Cannot collect Git metrics."
        exit 1
    fi
    
    # Step 1: Collect all Git metrics
    collect_commit_patterns
    collect_branch_lifecycle  
    collect_merge_success_metrics
    collect_performance_timeline
    
    # Step 2: Analyze patterns for intelligent decisions
    analyze_orchestration_patterns
    
    # Step 3: Integrate with VDD command system
    integrate_with_vdd_commands
    
    log_info "Git-Based Intelligence Engine completed successfully"
    log_info "Metrics available in: $METRICS_DIR"
    log_info "Integration file: $METRICS_DIR/vdd-integration.json"
}

# Execute main function if script is run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi