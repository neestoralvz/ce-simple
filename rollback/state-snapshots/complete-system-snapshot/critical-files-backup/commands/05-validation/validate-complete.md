# validate-complete.md

**Purpose**: Comprehensive system validation orchestrating creative, technical, and visual validation through parallel execution and integrated assessment reporting.

## Command Structure

### Phase 1: Validation Orchestration Setup
- Initialize parallel validation channels (creative, code, visual)
- Configure cross-validation dependencies and priority weighting
- Set up integrated reporting framework and success criteria
- Define escalation protocols for multi-domain validation failures

### Phase 2: Parallel Multi-Type Validation
- **Creative Track**: Execute validate-creative.md for originality and engagement
- **Technical Track**: Execute validate-code.md for quality and performance  
- **Visual Track**: Execute validate-visual.md for UX and accessibility
- **Integration Track**: Cross-validate dependencies and system coherence

### Phase 3: Comprehensive Assessment
- Aggregate validation results across all domains with weighted scoring
- Identify cross-domain conflicts and integration issues
- Generate holistic system health assessment and improvement matrix
- Validate end-to-end user experience and system reliability

### Phase 4: Integrated Feedback & Resolution
- Compile comprehensive validation report with priority-ranked issues
- Orchestrate targeted remediation across failed validation domains
- Execute re-validation cycles until all quality gates pass
- Document system certification with comprehensive compliance record

## Implementation

Execute through Claude Code Task Tool with parallel multi-domain validation:

```bash
# Complete validation orchestration
validate_complete() {
    # Parallel validation execution
    run_creative_validation() &
    run_code_validation() &
    run_visual_validation() &
    
    # Wait for completion and aggregate
    wait_for_validation_completion()
    cross_validate_integration()
    
    # Comprehensive assessment
    generate_integrated_report()
    identify_system_health_status()
    
    # Resolution orchestration
    orchestrate_remediation_if_needed()
    certify_system_quality()
}
```

## Success Criteria

**System Quality Gates**:
- Creative Validation: ≥70/100 (all creativity metrics pass)
- Code Validation: ≥80/100 (all technical quality gates pass)
- Visual Validation: ≥80/100 (all UX criteria meet standards)
- Integration Coherence: ≥85/100 (cross-domain compatibility)
- System Reliability: ≥90/100 (end-to-end functionality)
- Overall System Score: ≥80/100

**Multi-Domain Resolution**: Failed validations trigger orchestrated remediation across affected domains with parallel improvement cycles and comprehensive re-validation until all quality gates achieve certification standards.