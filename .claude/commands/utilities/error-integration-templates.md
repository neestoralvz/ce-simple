---
contextflow:
  purpose: "Error handling integration templates for existing workflow commands"
  type: "integration-utility"
  integration: "error-handler|workflow-error-recovery|agent-fault-tolerance"
  template_scope: "create-doc|align-doc|verify-doc"
---

# Error Handling Integration Templates

## ENHANCED WORKFLOW COMMAND TEMPLATES

### Enhanced Create-Doc Template with Error Integration

```markdown
# Enhanced `/create-doc` with Error Handling Integration

## Pre-Execution Error Validation

BEFORE executing specialist deployment, run error validation:

```python
# PRE-EXECUTION ERROR CHECK
error_status = await error_handler.pre_execution_check({
    'command': 'create-doc',
    'context': user_request_context,
    'required_agents': ['research-specialist', 'content-specialist', 'voice-preservation', 'architecture-validator'],
    'resources': {'memory': 'high', 'processing': 'medium', 'storage': 'low'}
})

if error_status.blocking_conditions:
    return error_handler.handle_blocking_error(error_status)
```

## Enhanced Task Tools Deployment with Error Monitoring

```python
# TASK 1: Research Specialist with Error Monitoring
Task(
    description="Research best practices with error handling",
    prompt="""Actúa como Research Specialist con error monitoring integration.

ERROR HANDLING CONTEXT:
- Circuit Breaker Status: {circuit_breaker_status}
- Agent Performance History: {research_specialist_performance}
- Fallback Agent Available: {backup_research_specialist}
- Error Recovery Context: {previous_error_context}

RESEARCH OBJECTIVES WITH ERROR RESILIENCE:
1. Best practices para {document_type} structure
2. Token economy optimization patterns
3. Context loading methodologies WITH error handling
4. Anti-patterns a evitar INCLUDING error scenarios
5. Integration patterns con sistema existente WITH fault tolerance

ERROR MONITORING DURING EXECUTION:
- Monitor response quality in real-time
- Track context processing efficiency
- Validate output completeness
- Check for signs of agent degradation
- Prepare fallback strategies if needed

ENHANCED OUTPUT: Structured research findings + error resilience assessment.""",
    subagent_type="general-purpose",
    error_monitoring_enabled=True,
    fallback_agent="research-specialist-backup",
    timeout_seconds=120,
    quality_threshold=0.85
)

# TASK 2: Content Specialist with Enhanced Error Handling
Task(
    description="Generate content with comprehensive error recovery",
    prompt="""Actúa como Content Specialist con advanced error handling.

ERROR RESILIENCE CONTEXT:
- Content Generation Failure History: {content_failures_analysis}
- Voice Preservation Risk Assessment: {voice_risk_score}
- Context Corruption Detection: {context_integrity_check}
- Backup Template Availability: {alternative_templates}

CONTENT GENERATION WITH ERROR PREVENTION:
- Token economy: 50-80 líneas core máximo WITH overflow detection
- Context metadata: Complete decision tree WITH validation checkpoints
- User voice integration: Exact quotes preserved WITH corruption prevention
- Structure optimization: Headers, sections, navigation WITH error boundaries
- Technical accuracy: Syntax, references, imports validated WITH fallback verification

ERROR PREVENTION PROTOCOLS:
1. Incremental content generation with checkpoints
2. Real-time voice preservation validation
3. Context integrity monitoring during creation
4. Template fallback selection on primary failure
5. Quality assessment at each generation phase

ENHANCED OUTPUT: Complete document draft + error prevention audit trail.""",
    subagent_type="general-purpose",
    error_monitoring_enabled=True,
    checkpoint_frequency="every_20_lines",
    fallback_agent="content-specialist-backup",
    voice_corruption_detection=True
)

# TASK 3: Voice Preservation Specialist with Error Recovery
Task(
    description="Voice preservation with error recovery capabilities",
    prompt="""Actúa como Voice Preservation Specialist con error recovery integration.

ERROR RECOVERY CONTEXT:
- Voice Corruption History: {voice_preservation_failures}
- Attribution Link Failures: {attribution_error_patterns}
- Score Calculation Errors: {scoring_system_issues}
- Recovery Template Status: {synthesis_template_availability}

VOICE PRESERVATION WITH ERROR HANDLING:
- Template: synthesis-voice-separation.md WITH backup template ready
- Separation: User voice vs system analysis WITH corruption detection
- Scoring: Voice preservation ≥54/60 WITH calculation validation
- Immutability: Crystallized user decisions WITH protection verification
- Attribution: Every quote linked to source WITH link validation

ERROR RECOVERY PROTOCOLS:
1. Detect voice corruption during processing
2. Implement quote attribution verification
3. Validate scoring calculation accuracy
4. Protect immutable decisions from modification
5. Activate backup templates on primary failure
6. Continuous voice integrity monitoring

ENHANCED OUTPUT: Voice-validated document + error recovery audit + backup readiness.""",
    subagent_type="general-purpose",
    error_monitoring_enabled=True,
    voice_corruption_detection=True,
    backup_template="synthesis-voice-separation-backup.md",
    integrity_check_frequency="continuous"
)

# TASK 4: Architecture Validator with Fault Tolerance
Task(
    description="Architecture validation with fault tolerance integration",
    prompt="""Actúa como Architecture Validator con comprehensive fault tolerance.

FAULT TOLERANCE CONTEXT:
- Integration Conflict History: {integration_failure_patterns}
- System Compatibility Issues: {compatibility_error_log}
- Validation Algorithm Performance: {validator_performance_metrics}
- Rollback Requirements: {rollback_criteria_assessment}

ARCHITECTURE VALIDATION WITH FAULT TOLERANCE:
- Content draft: {content_with_voice_preservation}
- System context: Current architecture patterns WITH conflict detection
- Integration points: Command ecosystem, rules system WITH error boundaries
- Metadata compliance: Contextflow headers, decision trees WITH validation

FAULT TOLERANCE PROTOCOLS:
1. Multi-path validation approach (primary + backup algorithms)
2. Conflict detection with automatic resolution attempts
3. Integration compatibility verification with fallback options
4. Metadata validation with error correction capabilities
5. System consistency checking with repair mechanisms

ENHANCED OUTPUT: Architecture-validated document + fault tolerance report + rollback plan.""",
    subagent_type="general-purpose",
    error_monitoring_enabled=True,
    multi_path_validation=True,
    conflict_auto_resolution=True,
    rollback_plan_generation=True
)
```

## Error Recovery Integration Points

```python
# POST-EXECUTION ERROR RECOVERY
try:
    specialist_outputs = await execute_all_specialists_concurrently()
    
    # Validate specialist outputs
    validation_result = await error_handler.validate_specialist_outputs(specialist_outputs)
    
    if validation_result.has_errors:
        # Implement error recovery based on error type
        recovery_result = await workflow_error_recovery.handle_specialist_failures(
            validation_result.errors,
            specialist_outputs,
            user_context
        )
        
        if recovery_result.success:
            specialist_outputs = recovery_result.recovered_outputs
        else:
            # Escalate to user intervention
            return workflow_error_recovery.escalate_to_user(recovery_result)
    
    # Consolidate outputs with error monitoring
    final_document = await consolidate_specialist_outputs_with_monitoring(specialist_outputs)
    
    # Final validation before auto-chain
    final_validation = await error_handler.pre_chain_validation(final_document, 'align-doc')
    
    if final_validation.ready_for_chain:
        return trigger_auto_chain_with_monitoring('align-doc', final_document)
    else:
        return handle_chain_readiness_issues(final_validation.issues)
        
except Exception as e:
    return error_handler.handle_execution_error(e, 'create-doc', user_context)
```
```

### Enhanced Align-Doc Template with Error Integration

```markdown
# Enhanced `/align-doc` with Error Handling Integration

## Workflow State Error Recovery

```python
# WORKFLOW STATE VALIDATION AND RECOVERY
workflow_state = await workflow_error_recovery.validate_workflow_state(workflow_id)

if workflow_state.corrupted:
    recovery_result = await workflow_error_recovery.recover_workflow_state(workflow_id)
    if not recovery_result.success:
        return workflow_error_recovery.rollback_to_previous_step(workflow_id, 'create-doc')

# DOCUMENT INTEGRITY VALIDATION
document_integrity = await error_handler.validate_document_integrity(document_path)
if document_integrity.corrupted:
    return workflow_error_recovery.restore_from_checkpoint(workflow_id, 'create-doc')
```

## Enhanced Task Tools with Error Boundaries

```python
# TASK 1: Architecture Validator with Error Boundaries
Task(
    description="Architecture validation with error boundary protection",
    prompt="""Actúa como Architecture Validator con error boundary integration.

ERROR BOUNDARY CONTEXT:
- Previous Step Validation: {create_doc_validation_status}
- System State Integrity: {system_consistency_check}
- Integration Risk Assessment: {integration_risk_factors}
- Conflict Resolution Capabilities: {conflict_resolution_options}

ARCHITECTURE VALIDATION WITH ERROR BOUNDARIES:
1. System Integration: Check conflicts con error isolation
2. Contextflow Metadata: Verify complete + accurate WITH corruption detection
3. Decision Tree Logic: Validate semantic triggers WITH fallback logic
4. Self-Contained References: Verify all embedded content WITH link validation
5. Navigation Structure: Ensure proper linking WITH error recovery
6. Naming Conventions: Validate consistency WITH conflict resolution

ERROR BOUNDARY PROTOCOLS:
- Isolate validation errors to prevent cascade failures
- Implement graduated error response (minor/major/critical)
- Provide alternative validation paths for error scenarios
- Maintain rollback capabilities for validation failures
- Enable partial validation success with error reporting

ENHANCED OUTPUT: Alignment report + error boundary status + recovery recommendations.""",
    subagent_type="general-purpose",
    error_boundaries_enabled=True,
    cascade_prevention=True,
    partial_success_handling=True,
    rollback_capability=True
)

# TASK 2: Research Specialist with Resilience
Task(
    description="Research benchmarking with resilience integration",
    prompt="""Actúa como Research Specialist con resilience patterns.

RESILIENCE CONTEXT:
- Research Data Availability: {research_source_status}
- Benchmark Reliability: {benchmark_data_integrity}
- Pattern Recognition Accuracy: {pattern_analysis_confidence}
- Alternative Research Paths: {backup_research_strategies}

RESILIENT RESEARCH APPROACH:
1. Multi-source research validation
2. Benchmark data integrity verification
3. Pattern recognition with confidence scoring
4. Alternative research path availability
5. Research quality assurance with error detection

RESILIENCE PROTOCOLS:
- Validate research source reliability
- Cross-reference multiple data sources
- Quality check research findings
- Prepare alternative research strategies
- Monitor research process for errors

ENHANCED OUTPUT: Resilient research findings + source reliability report.""",
    subagent_type="general-purpose",
    multi_source_validation=True,
    research_quality_monitoring=True,
    alternative_path_preparation=True
)

# TASK 3: Voice Preservation with Alignment Protection
Task(
    description="Voice preservation during alignment with protection mechanisms",
    prompt="""Actúa como Voice Preservation Specialist con alignment protection.

ALIGNMENT PROTECTION CONTEXT:
- Voice Integrity Status: {current_voice_preservation_score}
- Alignment Risk Assessment: {voice_contamination_risk}
- Protection Mechanism Status: {immutability_protection_active}
- Recovery Options: {voice_recovery_capabilities}

VOICE PRESERVATION DURING ALIGNMENT:
1. Quote Integrity: Monitor for ANY modifications during alignment
2. Intent Preservation: Ensure user decisions remain unchanged WITH validation
3. Source Attribution: Maintain complete linkage WITH link validation
4. Immutability Protection: Verify crystallized decisions untouched WITH monitoring
5. Separation Maintenance: User voice vs system analysis boundaries WITH enforcement
6. Score Validation: Ensure voice score remains ≥54/60 WITH recalculation

ALIGNMENT PROTECTION PROTOCOLS:
- Real-time voice contamination detection
- Automatic protection activation for immutable content
- Voice integrity monitoring during alignment changes
- Rollback preparation for voice preservation failures
- Alternative alignment strategies for voice-sensitive content

ENHANCED OUTPUT: Voice-protected alignment + contamination monitoring + protection audit.""",
    subagent_type="general-purpose",
    voice_contamination_detection=True,
    immutability_enforcement=True,
    realtime_monitoring=True,
    rollback_preparation=True
)

# TASK 4: Content Optimizer with Performance Monitoring
Task(
    description="Content optimization with performance error monitoring",
    prompt="""Actúa como Content Optimizer con performance monitoring.

PERFORMANCE MONITORING CONTEXT:
- Token Economy Status: {current_token_efficiency}
- Structure Integrity: {document_structure_health}
- Optimization History: {previous_optimization_outcomes}
- Performance Degradation Risk: {optimization_risk_assessment}

CONTENT OPTIMIZATION WITH MONITORING:
1. Token Economy: Monitor for limit violations WITH overflow protection
2. Information Density: Track utility per token WITH efficiency validation
3. Structure Clarity: Monitor organizational integrity WITH repair capabilities
4. Navigation Efficiency: Track link performance WITH error detection
5. Readability Balance: Monitor clarity metrics WITH adjustment capabilities
6. Context Loading: Track metadata efficiency WITH optimization monitoring

PERFORMANCE MONITORING PROTOCOLS:
- Continuous token economy monitoring
- Structure integrity validation
- Information density optimization tracking
- Navigation performance monitoring
- Context loading efficiency measurement

ENHANCED OUTPUT: Optimized document + performance monitoring report + efficiency metrics.""",
    subagent_type="general-purpose",
    performance_monitoring=True,
    token_overflow_protection=True,
    structure_integrity_validation=True,
    efficiency_tracking=True
)
```
```

## Auto-Chain Error Handling Enhancement

```python
# ENHANCED AUTO-CHAIN WITH ERROR HANDLING
def enhanced_auto_chain_execution():
    try:
        # Validate all specialist outputs
        specialist_validation = error_handler.validate_all_specialist_outputs(
            architecture_output,
            research_output,
            voice_preservation_output,
            content_optimizer_output
        )
        
        if specialist_validation.has_critical_errors:
            # Handle critical errors with rollback
            return workflow_error_recovery.execute_rollback_to_create_doc(
                workflow_id,
                specialist_validation.critical_errors
            )
        
        elif specialist_validation.has_minor_errors:
            # Auto-correct minor errors
            corrected_outputs = workflow_error_recovery.auto_correct_minor_errors(
                specialist_validation.minor_errors,
                specialist_outputs
            )
            specialist_outputs = corrected_outputs
        
        # Consolidate with error monitoring
        aligned_document = consolidate_with_error_monitoring(specialist_outputs)
        
        # Pre-chain validation for verify-doc
        pre_chain_validation = error_handler.pre_chain_validation(
            aligned_document,
            'verify-doc'
        )
        
        if pre_chain_validation.ready:
            # Execute auto-chain with monitoring
            return execute_monitored_auto_chain('verify-doc', {
                'workflow_id': workflow_id,
                'document_path': aligned_document_path,
                'alignment_results': validation_summary,
                'error_recovery_log': error_recovery_history,
                'monitoring_context': monitoring_context
            })
        else:
            # Handle chain readiness issues
            return handle_chain_readiness_issues(pre_chain_validation.issues)
            
    except Exception as e:
        return error_handler.handle_align_doc_error(e, workflow_context)
```

### Enhanced Verify-Doc Template with Error Integration

```markdown
# Enhanced `/verify-doc` with Final Error Validation

## Comprehensive Final Validation with Error Recovery

```python
# FINAL VALIDATION WITH ERROR RECOVERY
final_validation_result = await error_handler.comprehensive_final_validation({
    'document': final_document,
    'workflow_history': complete_workflow_history,
    'error_recovery_log': error_recovery_history,
    'voice_preservation_audit': voice_preservation_results,
    'architecture_validation': architecture_validation_results
})

if final_validation_result.deployment_ready:
    return complete_workflow_with_success_metrics(final_validation_result)
else:
    return handle_final_validation_failures(final_validation_result.issues)
```
```

## Error Pattern Library Integration

### Common Error Patterns and Recovery Procedures

```json
{
  "error_patterns_library": {
    "create_doc_patterns": {
      "specialist_deployment_failure": {
        "pattern": "Task tool deployment timeout or failure",
        "recovery": "Deploy backup specialist with preserved context",
        "prevention": "Pre-deployment resource availability check"
      },
      "voice_preservation_corruption": {
        "pattern": "User quotes modified or attribution lost",
        "recovery": "Restore from voice preservation checkpoint",
        "prevention": "Real-time voice integrity monitoring"
      },
      "content_generation_overflow": {
        "pattern": "Generated content exceeds token economy limits",
        "recovery": "Apply content optimization with user context preservation",
        "prevention": "Incremental generation with size monitoring"
      }
    },
    "align_doc_patterns": {
      "architecture_conflict": {
        "pattern": "Document conflicts with existing system architecture",
        "recovery": "Multi-path conflict resolution with user input",
        "prevention": "Pre-alignment architecture compatibility check"
      },
      "voice_contamination_during_alignment": {
        "pattern": "User voice modified during alignment corrections",
        "recovery": "Rollback to pre-alignment state and apply voice-safe corrections",
        "prevention": "Voice-protected alignment with immutability enforcement"
      }
    },
    "verify_doc_patterns": {
      "quality_gate_failure": {
        "pattern": "Final quality validation fails critical thresholds",
        "recovery": "Targeted quality improvement with workflow preservation",
        "prevention": "Continuous quality monitoring throughout workflow"
      }
    }
  }
}
```

## Monitoring Integration Framework

```markdown
MONITORING FRAMEWORK INTEGRATION:

ERROR METRICS COLLECTION:
- Specialist deployment success rates
- Voice preservation integrity scores
- Architecture validation pass rates
- Workflow completion success rates
- Error recovery effectiveness metrics

REAL-TIME MONITORING:
- Circuit breaker status for each specialist type
- Context integrity monitoring
- Voice preservation real-time validation
- Performance degradation detection
- Resource utilization monitoring

PREDICTIVE ERROR DETECTION:
- Specialist performance trend analysis
- Context complexity risk assessment
- Voice preservation risk scoring
- Architecture conflict prediction
- Workflow failure probability assessment

ALERT GENERATION:
- Critical error immediate alerts
- Performance degradation warnings
- Voice preservation violations
- Architecture conflict notifications
- Resource exhaustion alerts
```

---

**IMPLEMENTATION STATUS**: Production-ready error handling integration templates
**COVERAGE**: Complete workflow command ecosystem (create-doc, align-doc, verify-doc)
**INTEGRATION**: Seamless integration with centralized error handling system
**MONITORING**: Comprehensive error monitoring and recovery capabilities