# /core - Intelligent Core Command Dispatcher

**FUNCIÓN**: Smart routing + delegation to specialized subcommands with fallback protocols

## INTELLIGENT DISPATCHER PROTOCOL

**SEMANTIC PATTERN ANALYSIS** (Auto-routing Logic):
```bash
# Workspace Requirements Detection
if [[ "$input" =~ (workspace|setup|environment|git|worktree) ]]; then
    echo "🌳 WORKSPACE SETUP REQUIRED"
    /core-workspace "$@" && continue_workflow=true
fi

# Decision/Routing Requirements  
if [[ "$input" =~ (decide|route|complexity|analysis|choose) ]] || [ -z "$workflow_started" ]; then
    echo "🔄 DECISION ANALYSIS REQUIRED" 
    decision_result=$(/core-decision "$@")
    workflow_type=$(echo "$decision_result" | grep -o "ORQUESTA\|DIRECT")
fi

# Orchestration Requirements (Multi-component/Complex)
if [[ "$workflow_type" == "ORQUESTA" ]] || [[ "$input" =~ (orchestrate|coordinate|complex|multi|parallel) ]]; then
    echo "📋 ORCHESTRATION REQUIRED"
    /core-orchestrate "$@" && orchestration_active=true
fi

# Scope Management (During execution)
if [[ "$orchestration_active" == "true" ]] || [[ "$input" =~ (scope|expand|issue|track) ]]; then
    echo "📊 SCOPE MANAGEMENT ACTIVE"  
    /core-scope "$@" | tee scope_results.log
fi

# Validation Requirements (Always for quality)
if [[ "$input" =~ (validate|quality|check|verify) ]] || [ "$orchestration_active" == "true" ]; then
    echo "🔍 VALIDATION PROTOCOL ACTIVE"
    /core-validate "$@" && validation_passed=true
fi

# Finalization (End of workflow)  
if [[ "$input" =~ (finalize|complete|finish|close) ]] || [ "$validation_passed" == "true" ]; then
    echo "🎯 FINALIZATION PROTOCOL ACTIVE"
    /core-finalize "$@"
fi
```

**INTELLIGENT ROUTING MATRIX**:
- **Simple Tasks** → /core-decision → single subcommand execution
- **Complex Tasks** → /core-workspace → /core-orchestrate → /core-scope + /core-validate → /core-finalize  
- **Ambiguous Tasks** → /core-decision (evaluates complexity) → appropriate pathway

**DELEGATION PROTOCOL**:
1. **Pattern Recognition** → Semantic analysis determines subcommand requirements
2. **Intelligent Routing** → Route to appropriate subcommand(s) based on task complexity
3. **Progress Coordination** → Track execution across multiple subcommands when needed
4. **Fallback Integration** → Monolithic execution if subcommands unavailable

**PRESERVED FUNCTIONALITY**: All original core protocol capabilities maintained through specialized subcommand delegation with intelligent coordination
