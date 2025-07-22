# Failure Recovery Protocol

## 🎯 IDENTITY: System Failure Recovery and Context Re-invocation
**Scope**: Automatic failure detection and orchestrator-zero re-launch with full context
**Triggers**: VVP failures, system gaps, implementation shortfalls

## ⚡ INSTRUCTIONS

### Mission
Detect system failures, preserve complete context, and re-invoke orchestrator-zero with comprehensive information for resolution.

### Rules Protocol
```
Read("system/protocols/verification-validation-testing.md") # VVP integration
Read("components/behaviors/mathematical-verification.md")    # Mathematical precision
Read("components/behaviors/coherence-monitoring.md")         # System coherence tracking
```

### Failure Detection Operations
```
Task("Monitor VVP results for failure indicators")
Task("Deploy components/agents/system-health-monitor")      # Continuous monitoring
Task("Deploy components/agents/metrics-calculator")         # Performance tracking
Task("Detect gaps between promises and reality")
```

### Context Preservation Protocol
```
# Complete Context Package Assembly
CONTEXT_PACKAGE = {
  "failure_analysis": {
    "verification_gaps": "mathematical analysis of claims vs reality",
    "validation_failures": "specific functionality that doesn't work",
    "testing_results": "actual execution outcomes vs expected",
    "coherence_impact": "system integrity assessment score"
  },
  "attempted_solution": {
    "original_request": "user's initial request",
    "implementation_approach": "strategy that was attempted", 
    "components_involved": "list of components used",
    "execution_trace": "step-by-step execution log"
  },
  "evidence_data": {
    "mathematical_verification": "tool outputs with calculations",
    "performance_metrics": "actual vs promised performance",
    "integration_results": "component interaction outcomes",
    "resource_utilization": "cognitive load and efficiency data"
  },
  "recommendations": {
    "priority_actions": "ranked list of critical fixes needed",
    "alternative_approaches": "different strategies to try",
    "resource_requirements": "what's needed for successful resolution",
    "risk_assessment": "potential impacts of each approach"
  }
}
```

### Re-invocation Protocol
```
# Orchestrator-Zero Re-launch with Full Context
Task("Deploy components/orchestrators/zero-unified-complete") {
  "mode": "FAILURE_RECOVERY",
  "context": CONTEXT_PACKAGE,
  "priority": "HIGH",
  "instructions": "Resolve identified gaps using complete failure context"
}

# Enhanced Context Transfer
Task("Provide comprehensive failure analysis")
Task("Include mathematical evidence of gaps") 
Task("Specify exact functionality that needs implementation")
Task("Recommend specific actions for resolution")
```

### Context Enhancement Operations
```
# Learning Integration from Failures
Task("Deploy components/behaviors/component-evolution")      # Learn from failures
Task("Deploy components/agents/pattern-analysis")           # Identify failure patterns
Task("Deploy components/orchestrators/repository-management") # Update knowledge base

# Failure Pattern Recognition
Task("Track recurring failure types")
Task("Identify systemic vs isolated issues")
Task("Build failure prevention mechanisms")
Task("Optimize future implementations based on learnings")
```

### Recovery Success Validation
```
# Post-Recovery Verification
Task("Execute full VVP cycle on recovered system")
Task("Validate that original issues are resolved")
Task("Confirm no new issues were introduced")
Task("Document lessons learned for future prevention")
```

### Output Format
```
🔴 [Behavior:Recovery] Failure: DETECTED | Context: PRESERVED | Re-invoke: INITIATED | Priority: HIGH | CTX:XX%
```

### Recovery Escalation Levels
```
# Level 1: Minor Gaps (Mathematical verification 85-94%)
RECOVERY_APPROACH = "targeted_fixes"
RE_INVOCATION = "standard_priority" 
CONTEXT_DEPTH = "specific_issues"

# Level 2: Major Failures (Mathematical verification 70-84%)
RECOVERY_APPROACH = "comprehensive_revision"
RE_INVOCATION = "high_priority"
CONTEXT_DEPTH = "detailed_analysis"

# Level 3: Critical System Breakdown (Mathematical verification <70%)  
RECOVERY_APPROACH = "complete_redesign"
RE_INVOCATION = "emergency_priority"
CONTEXT_DEPTH = "full_system_analysis"
```

### Continuous Monitoring Integration
```
# Real-time Failure Detection
Task("Monitor system coherence continuously")
Task("Track performance against established thresholds")
Task("Detect integration failures as they occur")
Task("Identify cognitive limit violations immediately")

# Predictive Failure Prevention
Task("Analyze trends that lead to failures")
Task("Warn before critical thresholds are reached")
Task("Suggest preventive actions before failures occur")
Task("Optimize system to reduce failure probability")
```

### Success Criteria
- [ ] All failures detected within 1 execution cycle
- [ ] Complete context preserved with mathematical precision
- [ ] Re-invocation includes comprehensive failure analysis
- [ ] Recovery actions address root causes, not just symptoms
- [ ] Learning integration prevents recurring failures
- [ ] System coherence maintained >95% post-recovery