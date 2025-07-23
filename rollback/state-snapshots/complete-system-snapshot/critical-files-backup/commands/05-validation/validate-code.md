# validate-code.md

**Purpose**: Technical validation for code quality, performance, security, and maintainability through automated analysis and manual review protocols.

## Command Structure

### Phase 1: Technical Analysis Setup
- Initialize static code analysis tools and security scanners
- Configure performance profiling and dependency validation
- Set up testing environment with coverage requirements
- Define quality gates and compliance standards

### Phase 2: Multi-Layer Code Validation
- **Syntax & Logic**: Parse correctness, control flow, error handling
- **Performance**: Runtime efficiency, memory usage, scalability metrics
- **Security**: Vulnerability scanning, input validation, access controls
- **Maintainability**: Code complexity, documentation, test coverage

### Phase 3: Validation Execution
- Run parallel automated analysis across all validation layers
- Execute comprehensive test suites with coverage reporting
- Perform security vulnerability assessment and dependency audit
- Generate quantifiable metrics for each validation dimension

### Phase 4: Results Processing & Feedback
- Compile technical validation report with actionable insights
- Identify critical issues requiring immediate attention
- Trigger remediation workflow if quality gates fail
- Document successful validations with compliance certification

## Implementation

Execute through Claude Code Task Tool with comprehensive technical assessment:

```bash
# Code validation workflow
validate_code() {
    # Technical analysis layers
    analyze_syntax_and_logic()
    profile_performance_metrics()
    scan_security_vulnerabilities()
    assess_maintainability_factors()
    
    # Validation execution
    run_comprehensive_tests()
    validate_dependencies()
    check_compliance_standards()
    
    # Results processing
    generate_validation_report()
    trigger_remediation_if_needed()
}
```

## Success Criteria

**Quality Gates**:
- Syntax Correctness: 100% (zero errors)
- Test Coverage: ≥85%
- Performance Score: ≥80/100
- Security Rating: ≥90/100 (zero critical vulnerabilities)
- Maintainability Index: ≥75/100
- Overall Code Quality: ≥80/100

**Remediation Triggers**: Any critical failure or score below threshold initiates automated remediation workflow with specific fix recommendations and re-validation cycle.