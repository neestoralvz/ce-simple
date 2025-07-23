# validate-visual.md

**Purpose**: Visual and UX validation for usability, aesthetics, accessibility, and responsive design through multi-device testing and user experience assessment.

## Command Structure

### Phase 1: Visual Assessment Setup
- Configure multi-device testing environment (desktop, tablet, mobile)
- Initialize accessibility scanning tools and WCAG compliance checkers
- Set up visual regression testing and design consistency validation
- Define UX metrics and user journey evaluation criteria

### Phase 2: Multi-Dimensional UX Validation
- **Usability**: Navigation flow, interaction patterns, user task completion
- **Aesthetics**: Visual hierarchy, color harmony, typography consistency
- **Accessibility**: WCAG compliance, screen reader compatibility, keyboard navigation
- **Responsiveness**: Cross-device compatibility, performance across viewports

### Phase 3: Validation Execution
- Run parallel visual testing across device configurations
- Execute accessibility audit with automated and manual checks
- Perform user journey simulation and interaction validation
- Generate comprehensive UX assessment with quantifiable metrics

### Phase 4: Enhancement Integration
- Compile visual validation report with specific improvement areas
- Identify critical UX issues affecting user experience
- Trigger design iteration cycle if validation scores below threshold
- Document successful validations with design pattern certification

## Implementation

Execute through Claude Code Task Tool with comprehensive visual assessment:

```bash
# Visual validation workflow
validate_visual() {
    # Visual assessment dimensions
    test_usability_patterns()
    validate_aesthetic_consistency()
    audit_accessibility_compliance()
    check_responsive_behavior()
    
    # Cross-device validation
    test_desktop_experience()
    test_tablet_compatibility()
    test_mobile_responsiveness()
    
    # Results compilation
    generate_ux_assessment()
    trigger_design_iteration_if_needed()
}
```

## Success Criteria

**UX Quality Gates**:
- Usability Score: ≥80/100
- Aesthetic Rating: ≥75/100
- Accessibility Compliance: ≥95% WCAG AA
- Responsive Design: 100% viewport compatibility
- Load Performance: ≤3s across devices
- Overall UX Score: ≥80/100

**Design Iteration Triggers**: Any metric below threshold or critical accessibility violation initiates targeted design improvement cycle with specific enhancement recommendations and re-validation protocol.