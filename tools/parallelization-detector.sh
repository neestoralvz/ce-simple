#!/bin/bash
# Parallelization Opportunity Detector
# Automatically identifies opportunities for aggressive parallelization

set -e

PROJECT_DIR="/Users/nalve/ce-simple"
COMMANDS_DIR="$PROJECT_DIR/.claude/commands"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

log() {
    echo -e "${GREEN}[DETECTOR]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[OPPORTUNITY]${NC} $1"
}

error() {
    echo -e "${RED}[VIOLATION]${NC} $1"
}

info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

# Function to analyze command files for parallelization opportunities
analyze_commands() {
    log "🔍 Analyzing commands for parallelization opportunities..."
    echo ""
    
    for cmd_file in "$COMMANDS_DIR"/*.md; do
        if [ -f "$cmd_file" ]; then
            local cmd_name=$(basename "$cmd_file" .md)
            info "📝 Analyzing: $cmd_name"
            
            # Check for sequential patterns that could be parallelized
            local sequential_patterns=0
            local parallel_patterns=0
            
            # Look for Task tool usage (potential parallelization)
            if grep -q "Task(" "$cmd_file"; then
                local task_count=$(grep -c "Task(" "$cmd_file" 2>/dev/null || echo 0)
                if [ "$task_count" -eq 1 ]; then
                    warn "  Single Task tool detected - could be parallelized"
                    ((sequential_patterns++))
                else
                    log "  Multiple Task tools found: $task_count (GOOD)"
                    ((parallel_patterns++))
                fi
            fi
            
            # Look for WebSearch patterns
            if grep -q -E "(WebSearch|web.*search)" "$cmd_file"; then
                if grep -q -E "4\s+search|sequential|one.*time" "$cmd_file"; then
                    warn "  Limited search parallelization detected"
                    ((sequential_patterns++))
                elif grep -q -E "16\s+search|simultaneous|parallel" "$cmd_file"; then
                    log "  Aggressive search parallelization found (EXCELLENT)"
                    ((parallel_patterns++))
                fi
            fi
            
            # Look for file operation patterns  
            if grep -q -E "(Glob|Grep|Read)" "$cmd_file"; then
                local file_ops=$(grep -c -E "(Glob|Grep|Read)" "$cmd_file" 2>/dev/null || echo 0)
                if [ "$file_ops" -lt 10 ]; then
                    warn "  Limited file operations: $file_ops (could be expanded)"
                    ((sequential_patterns++))
                else
                    log "  Comprehensive file operations: $file_ops (EXCELLENT)"
                    ((parallel_patterns++))
                fi
            fi
            
            # Report findings for this command
            if [ "$sequential_patterns" -gt "$parallel_patterns" ]; then
                error "  ❌ PARALLELIZATION OPPORTUNITY: $cmd_name needs optimization"
            elif [ "$parallel_patterns" -gt 0 ]; then
                log "  ✅ WELL PARALLELIZED: $cmd_name follows aggressive parallelization"
            else
                info "  ℹ️  No clear parallelization patterns detected in $cmd_name"
            fi
            echo ""
        fi
    done
}

# Function to detect parallelizable operations in recent executions
analyze_execution_patterns() {
    log "🚀 Analyzing execution patterns..."
    echo ""
    
    # Look for evidence of sequential execution in recent operations
    if [ -d "$PROJECT_DIR/.claude/context" ]; then
        local context_files=$(find "$PROJECT_DIR/.claude/context" -name "*.md" -newer "$PROJECT_DIR/.claude/commands" 2>/dev/null | wc -l)
        if [ "$context_files" -gt 0 ]; then
            log "Recent execution evidence found: $context_files context files"
            
            # Analyze for parallel vs sequential patterns
            local parallel_evidence=$(find "$PROJECT_DIR/.claude/context" -name "*.md" -exec grep -l -E "(simultaneous|parallel|concurrent)" {} \; 2>/dev/null | wc -l)
            local sequential_evidence=$(find "$PROJECT_DIR/.claude/context" -name "*.md" -exec grep -l -E "(sequential|one.*time|wait.*for)" {} \; 2>/dev/null | wc -l)
            
            if [ "$parallel_evidence" -gt "$sequential_evidence" ]; then
                log "✅ Execution patterns show good parallelization usage"
            else
                warn "⚠️ Execution patterns suggest room for more parallelization"
            fi
        fi
    fi
}

# Function to generate parallelization recommendations
generate_recommendations() {
    log "💡 Generating parallelization recommendations..."
    echo ""
    
    cat << 'EOF'
🎯 AGGRESSIVE PARALLELIZATION RECOMMENDATIONS:

1. WEB RESEARCH:
   - Always use 16 simultaneous WebSearch operations
   - Structure: Core(4) + Contextual(4) + Tools(4) + Advanced(4)
   - Target: 90 seconds for comprehensive research vs 16+ minutes sequential

2. CODEBASE ANALYSIS:  
   - Deploy 52 concurrent operations: 16 Glob + 24 Grep + 12 Read
   - Cover all file types, patterns, and key configurations simultaneously
   - Target: 2 minutes for complete analysis vs 2+ hours sequential

3. DOCUMENTATION CREATION:
   - Generate multiple related documents in single message
   - 6-12 files simultaneously for comprehensive documentation
   - Target: 3-5 minutes vs 30+ minutes sequential

4. BASH OPERATIONS:
   - Identify independent system operations for parallel execution
   - Build, test, deploy operations where no dependencies exist
   - Target: 2 minutes vs 20+ minutes sequential

5. ANALYSIS TASKS:
   - Think-layers with parallel analysis dimensions
   - Pattern recognition across multiple domains simultaneously
   - Multi-angle problem solving in single execution

🚨 CRITICAL RULES:
- Question EVERY sequential operation
- Batch ALL independent operations in single message
- Scale operations to system capacity limits
- Measure and optimize performance continuously

📊 SUCCESS METRICS:
- 5-15x speed improvement over sequential execution
- 70-90% system resource utilization
- >95% quality maintenance despite aggressive scaling
EOF
    echo ""
}

# Function to provide specific optimization suggestions
suggest_optimizations() {
    log "🔧 Specific optimization suggestions:"
    echo ""
    
    # Check current command configurations
    if [ -f "$COMMANDS_DIR/explore-web.md" ]; then
        if ! grep -q "16.*simultaneous" "$COMMANDS_DIR/explore-web.md"; then
            error "URGENT: explore-web.md should use 16 simultaneous searches"
        fi
    fi
    
    if [ -f "$COMMANDS_DIR/explore-codebase.md" ]; then
        if ! grep -q "52.*operations" "$COMMANDS_DIR/explore-codebase.md"; then
            error "URGENT: explore-codebase.md should use 52 concurrent operations"
        fi
    fi
    
    # Look for other commands that could benefit from parallelization
    for cmd_file in "$COMMANDS_DIR"/*.md; do
        if [ -f "$cmd_file" ]; then
            local cmd_name=$(basename "$cmd_file" .md)
            if [ "$cmd_name" != "explore-web" ] && [ "$cmd_name" != "explore-codebase" ]; then
                if grep -q -E "(Task|WebSearch|Glob|Grep|Read|Write)" "$cmd_file"; then
                    info "REVIEW: $cmd_name could benefit from parallelization analysis"
                fi
            fi
        fi
    done
}

# Main execution
main() {
    echo "======================================="
    echo "🚀 PARALLELIZATION OPPORTUNITY DETECTOR"
    echo "======================================="
    echo "Project: ce-simple"
    echo "Time: $(date)"
    echo "======================================="
    echo ""
    
    analyze_commands
    analyze_execution_patterns
    generate_recommendations
    suggest_optimizations
    
    echo "======================================="
    echo "💡 NEXT STEPS:"
    echo "1. Review flagged commands for parallelization opportunities"
    echo "2. Update commands to use aggressive parallelization patterns"  
    echo "3. Test performance improvements with parallel execution"
    echo "4. Monitor system resource utilization during parallel operations"
    echo "======================================="
}

# Execute if run directly
if [ "${BASH_SOURCE[0]}" == "${0}" ]; then
    main "$@"
fi