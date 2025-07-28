#!/bin/bash

# Think×4 Automated Enforcement System
# Purpose: Automated validation of Think×4 methodology application
# Authority: implements user-input/technical-requirements/think-by-four-mandatory.md
# Status: Core automation for cognitive compliance validation

set -euo pipefail

# ============================================================================
# CONFIGURATION
# ============================================================================

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
readonly VALIDATION_DIR="$PROJECT_ROOT/data/think-x4-validation"
readonly LOG_FILE="$VALIDATION_DIR/think-x4-enforcement.log"

# Think×4 validation patterns
readonly THINK_PATTERNS=(
    "Think.*(\(.*Layer.*1.*\)|[Ll]ayer.*1)"
    "Think.*[Hh]ard.*(\(.*Layer.*2.*\)|[Ll]ayer.*2)"
    "Think.*[Hh]arder.*(\(.*Layer.*3.*\)|[Ll]ayer.*3)"
    "Ultra.*[Tt]hink.*(\(.*Layer.*4.*\)|[Ll]ayer.*4)"
)

readonly THINK_LAYER_NAMES=(
    "Think (Layer 1)"
    "Think Hard (Layer 2)" 
    "Think Harder (Layer 3)"
    "Ultra Think (Layer 4)"
)

# Critical decision contexts requiring Think×4
readonly CRITICAL_CONTEXTS=(
    "technical.*architecture.*decision"
    "system.*design.*choice"
    "problem.*analysis.*solution"
    "implementation.*strategy.*planning"
    "quality.*assurance.*validation"
    "performance.*optimization.*decision"
    "documentation.*structure.*decision"
)

# Ensure validation directory exists
mkdir -p "$VALIDATION_DIR"

# ============================================================================
# LOGGING FUNCTIONS
# ============================================================================

log_info() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] INFO: $*" | tee -a "$LOG_FILE"
}

log_warning() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] WARNING: $*" | tee -a "$LOG_FILE"
}

log_error() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $*" >&2 | tee -a "$LOG_FILE"
}

log_violation() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] VIOLATION: $*" >&2 | tee -a "$LOG_FILE"
}

# ============================================================================
# THINK×4 DETECTION FUNCTIONS
# ============================================================================

validate_think_x4_in_file() {
    local file_path="$1"
    local file_name=$(basename "$file_path")
    local violations=()
    local compliance_score=0
    
    if [[ ! -f "$file_path" ]]; then
        log_error "File not found: $file_path"
        return 1
    fi
    
    # Check if file contains critical decision context
    local has_critical_context=false
    for context_pattern in "${CRITICAL_CONTEXTS[@]}"; do
        if grep -Eiq "$context_pattern" "$file_path"; then
            has_critical_context=true
            break
        fi
    done
    
    if [[ "$has_critical_context" == "false" ]]; then
        log_info "File $file_name: No critical decision context detected, Think×4 not required"
        return 0
    fi
    
    log_info "File $file_name: Critical decision context detected, validating Think×4 compliance"
    
    # Check for each Think×4 layer
    local layers_found=0
    for i in "${!THINK_PATTERNS[@]}"; do
        local pattern="${THINK_PATTERNS[$i]}"
        local layer_name="${THINK_LAYER_NAMES[$i]}"
        
        if grep -Eiq "$pattern" "$file_path"; then
            log_info "✅ Found: $layer_name in $file_name"
            ((layers_found++))
        else
            violations+=("Missing: $layer_name")
        fi
    done
    
    # Calculate compliance score
    compliance_score=$((layers_found * 25))  # 25% per layer
    
    # Generate validation report
    local validation_report="$VALIDATION_DIR/validation_$(basename "$file_path" .md)_$(date +%s).json"
    
    cat > "$validation_report" <<EOF
{
  "metadata": {
    "validated_at": "$(date -Iseconds)",
    "file_path": "$file_path",
    "validator_version": "1.0.0"
  },
  "analysis": {
    "has_critical_context": $has_critical_context,
    "layers_found": $layers_found,
    "compliance_score": $compliance_score,
    "status": "$([ $layers_found -eq 4 ] && echo "COMPLIANT" || echo "NON_COMPLIANT")"
  },
  "violations": [
$(if [[ ${#violations[@]} -gt 0 ]]; then
    for i in "${!violations[@]}"; do
        echo "    \"${violations[$i]}\""
        [[ $i -lt $((${#violations[@]} - 1)) ]] && echo ","
    done
fi)
  ],
  "recommendations": {
    "action_required": $([ $layers_found -lt 4 ] && echo "true" || echo "false"),
    "missing_layers": $((4 - layers_found)),
    "compliance_level": "$(
      if [ $compliance_score -ge 100 ]; then echo "FULL_COMPLIANCE"
      elif [ $compliance_score -ge 75 ]; then echo "MOSTLY_COMPLIANT"
      elif [ $compliance_score -ge 50 ]; then echo "PARTIALLY_COMPLIANT"
      else echo "NON_COMPLIANT"
      fi
    )"
  }
}
EOF
    
    # Report results
    if [[ $layers_found -eq 4 ]]; then
        log_info "✅ COMPLIANT: $file_name has complete Think×4 analysis (100% compliance)"
        return 0
    else
        log_violation "❌ NON-COMPLIANT: $file_name missing $((4 - layers_found)) Think×4 layers ($compliance_score% compliance)"
        for violation in "${violations[@]}"; do
            log_violation "  - $violation"
        done
        return 1
    fi
}

validate_directory_compliance() {
    local directory="$1"
    local total_files=0
    local compliant_files=0
    local violations_count=0
    
    log_info "Starting Think×4 compliance validation for directory: $directory"
    
    # Find all markdown files that might contain decisions
    while IFS= read -r -d '' file; do
        ((total_files++))
        
        if validate_think_x4_in_file "$file"; then
            ((compliant_files++))
        else
            ((violations_count++))
        fi
    done < <(find "$directory" -name "*.md" -type f -print0)
    
    # Generate directory compliance report
    local compliance_percentage=0
    if [[ $total_files -gt 0 ]]; then
        compliance_percentage=$(( (compliant_files * 100) / total_files ))
    fi
    
    local directory_report="$VALIDATION_DIR/directory_compliance_$(basename "$directory")_$(date +%s).json"
    
    cat > "$directory_report" <<EOF
{
  "metadata": {
    "validated_at": "$(date -Iseconds)",
    "directory": "$directory",
    "validation_scope": "think_x4_compliance"
  },
  "summary": {
    "total_files_analyzed": $total_files,
    "compliant_files": $compliant_files,
    "non_compliant_files": $violations_count,
    "compliance_percentage": $compliance_percentage
  },
  "status": {
    "overall_compliance": "$(
      if [ $compliance_percentage -ge 95 ]; then echo "EXCELLENT"
      elif [ $compliance_percentage -ge 80 ]; then echo "GOOD"
      elif [ $compliance_percentage -ge 60 ]; then echo "NEEDS_IMPROVEMENT"
      else echo "CRITICAL"
      fi
    )",
    "action_required": $([ $violations_count -gt 0 ] && echo "true" || echo "false")
  },
  "recommendations": {
    "priority": "$([ $violations_count -gt 5 ] && echo "HIGH" || echo "MEDIUM")",
    "next_steps": [
      "Review non-compliant files",
      "Apply Think×4 methodology to critical decisions",
      "Re-run validation after corrections"
    ]
  }
}
EOF
    
    log_info "Directory validation complete: $compliant_files/$total_files files compliant ($compliance_percentage%)"
    
    if [[ $violations_count -gt 0 ]]; then
        log_warning "Found $violations_count non-compliant files requiring Think×4 enforcement"
        return 1
    else
        log_info "All files are Think×4 compliant"
        return 0
    fi
}

# ============================================================================
# AUTOMATED ENFORCEMENT HOOKS
# ============================================================================

create_git_hooks() {
    local hooks_dir="$PROJECT_ROOT/.git/hooks"
    
    if [[ ! -d "$hooks_dir" ]]; then
        log_error "Git hooks directory not found: $hooks_dir"
        return 1
    fi
    
    # Create pre-commit hook for Think×4 validation
    local pre_commit_hook="$hooks_dir/pre-commit"
    
    cat > "$pre_commit_hook" <<'EOF'
#!/bin/bash

# Think×4 Pre-commit Validation Hook
# Validates Think×4 compliance before allowing commits

VALIDATOR_SCRIPT="tools/automation/think-x4-validator.sh"

if [[ ! -f "$VALIDATOR_SCRIPT" ]]; then
    echo "Warning: Think×4 validator not found at $VALIDATOR_SCRIPT"
    exit 0
fi

echo "🧠 Running Think×4 compliance validation..."

# Get list of staged files
staged_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.md$' || true)

if [[ -z "$staged_files" ]]; then
    echo "No markdown files to validate"
    exit 0
fi

violations=0

for file in $staged_files; do
    if [[ -f "$file" ]]; then
        if ! "$VALIDATOR_SCRIPT" validate-file "$file"; then
            ((violations++))
        fi
    fi
done

if [[ $violations -gt 0 ]]; then
    echo ""
    echo "❌ Think×4 compliance violations detected!"
    echo "Please ensure all critical decisions use Think×4 methodology:"
    echo "  1. Think (Layer 1): Basic understanding"
    echo "  2. Think Hard (Layer 2): Deeper analysis" 
    echo "  3. Think Harder (Layer 3): Multi-system integration"
    echo "  4. Ultra Think (Layer 4): Comprehensive synthesis"
    echo ""
    echo "Use 'git commit --no-verify' to bypass (not recommended)"
    exit 1
fi

echo "✅ Think×4 compliance validated"
exit 0
EOF
    
    chmod +x "$pre_commit_hook"
    log_info "Created Think×4 pre-commit hook at $pre_commit_hook"
}

# ============================================================================
# CONTINUOUS MONITORING
# ============================================================================

start_continuous_monitoring() {
    local watch_directories=("$PROJECT_ROOT/docs" "$PROJECT_ROOT/planning" "$PROJECT_ROOT/user-input")
    local monitoring_interval=300  # 5 minutes
    
    log_info "Starting continuous Think×4 monitoring (interval: ${monitoring_interval}s)"
    
    while true; do
        for directory in "${watch_directories[@]}"; do
            if [[ -d "$directory" ]]; then
                log_info "Monitoring directory: $directory"
                validate_directory_compliance "$directory" > /dev/null 2>&1 || true
            fi
        done
        
        # Generate aggregated compliance report
        generate_compliance_dashboard
        
        sleep "$monitoring_interval"
    done
}

generate_compliance_dashboard() {
    local dashboard_file="$VALIDATION_DIR/compliance_dashboard.json"
    local recent_reports=($(find "$VALIDATION_DIR" -name "directory_compliance_*.json" -mtime -1 | sort -r | head -5))
    
    local total_compliance=0
    local report_count=0
    
    echo "{" > "$dashboard_file"
    echo "  \"metadata\": {" >> "$dashboard_file"
    echo "    \"generated_at\": \"$(date -Iseconds)\"," >> "$dashboard_file"
    echo "    \"monitoring_status\": \"active\"" >> "$dashboard_file"
    echo "  }," >> "$dashboard_file"
    echo "  \"recent_validations\": [" >> "$dashboard_file"
    
    for report in "${recent_reports[@]}"; do
        if [[ -f "$report" ]]; then
            if [[ $report_count -gt 0 ]]; then
                echo "    ," >> "$dashboard_file"
            fi
            cat "$report" | sed 's/^/    /' >> "$dashboard_file"
            
            # Extract compliance percentage for average calculation
            local compliance=$(jq -r '.summary.compliance_percentage' "$report" 2>/dev/null || echo "0")
            total_compliance=$((total_compliance + compliance))
            ((report_count++))
        fi
    done
    
    echo "  ]," >> "$dashboard_file"
    
    # Calculate average compliance
    local avg_compliance=0
    if [[ $report_count -gt 0 ]]; then
        avg_compliance=$((total_compliance / report_count))
    fi
    
    echo "  \"summary\": {" >> "$dashboard_file"
    echo "    \"average_compliance\": $avg_compliance," >> "$dashboard_file"
    echo "    \"total_reports\": $report_count," >> "$dashboard_file"
    echo "    \"enforcement_active\": true" >> "$dashboard_file"
    echo "  }" >> "$dashboard_file"
    echo "}" >> "$dashboard_file"
    
    log_info "Generated compliance dashboard: average $avg_compliance% compliance across $report_count reports"
}

# ============================================================================
# MAIN EXECUTION
# ============================================================================

main() {
    local command="${1:-help}"
    
    case "$command" in
        "validate-file")
            if [[ -z "${2:-}" ]]; then
                log_error "Usage: $0 validate-file <file_path>"
                exit 1
            fi
            validate_think_x4_in_file "$2"
            ;;
        
        "validate-directory")
            if [[ -z "${2:-}" ]]; then
                log_error "Usage: $0 validate-directory <directory_path>"
                exit 1
            fi
            validate_directory_compliance "$2"
            ;;
        
        "install-hooks")
            create_git_hooks
            ;;
        
        "monitor")
            start_continuous_monitoring
            ;;
        
        "dashboard")
            generate_compliance_dashboard
            cat "$VALIDATION_DIR/compliance_dashboard.json"
            ;;
        
        "help"|*)
            cat <<EOF
Think×4 Automated Enforcement System

Usage:
  $0 validate-file <file_path>      - Validate Think×4 compliance in specific file
  $0 validate-directory <dir_path>  - Validate Think×4 compliance in directory
  $0 install-hooks                  - Install Git pre-commit hooks for enforcement
  $0 monitor                        - Start continuous monitoring (runs indefinitely)
  $0 dashboard                      - Generate and display compliance dashboard
  $0 help                           - Show this help message

Think×4 Methodology Requirements:
  1. Think (Layer 1): Basic understanding and immediate observations
  2. Think Hard (Layer 2): Deeper analysis with complexity considerations
  3. Think Harder (Layer 3): Multi-system integration and long-term consequences
  4. Ultra Think (Layer 4): Comprehensive synthesis with optimal solutions

Critical contexts requiring Think×4:
  - Technical architecture decisions
  - System design choices
  - Problem analysis and solution development
  - Implementation strategy planning
  - Quality assurance validation
  - Performance optimization decisions
  - Documentation structure decisions
EOF
            ;;
    esac
}

# Execute main function if script is run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi