# /calculate-complexity - Expert Assembly Complexity Assessment

## Purpose
Executes comprehensive domain complexity assessment providing expert-driven analysis for optimal expert panel assembly and sophisticated AI orchestration decisions.

## Principles and Guidelines
- **Expert-Driven Assessment**: Focus on expertise requirements rather than mathematical formulas
- **Domain Analysis**: Comprehensive evaluation of required knowledge domains and specializations
- **Synergy Optimization**: Assess collaborative potential and cross-domain value
- **Dynamic Assembly**: Provide expert assembly recommendations without artificial constraints

## Execution Process

### Phase 1: Domain Complexity Analysis
Update TodoWrite: Mark "domain complexity analysis" as in_progress

Execute comprehensive domain analysis using Task:
- Assess domain breadth (knowledge areas required: qualitative evaluation)
- Evaluate specialization depth (expertise level needed: qualitative assessment)
- Analyze interdisciplinary requirements (cross-domain collaboration: synergy evaluation)
- Determine quality standards (validation complexity: quality assessment)

Use Bash for domain assessment:
```bash
# Domain complexity assessment
echo "EXPERT_ASSEMBLY_QUESTION: ¿Cuál es el grupo de expertos que mejor puede abordar este tema?"

# Domain identification
domains=()
if [[ "$scope" =~ technical|architecture|system|infrastructure ]]; then
    domains+=("Technical Architecture")
    echo "DOMAIN_IDENTIFIED: Technical Architecture expertise required"
fi
if [[ "$scope" =~ user|experience|interface|workflow ]]; then
    domains+=("User Experience")
    echo "DOMAIN_IDENTIFIED: User Experience expertise required"
fi
if [[ "$scope" =~ business|domain|industry|regulatory ]]; then
    domains+=("Domain-Specific")
    echo "DOMAIN_IDENTIFIED: Domain-Specific expertise required"
fi
if [[ "$scope" =~ quality|testing|validation|security ]]; then
    domains+=("Quality Assurance")
    echo "DOMAIN_IDENTIFIED: Quality Assurance expertise required"
fi
if [[ "$scope" =~ strategy|vision|competitive|market ]]; then
    domains+=("Strategic Vision")
    echo "DOMAIN_IDENTIFIED: Strategic Vision expertise required"
fi
```

### Phase 2: Expert Assembly Requirements Analysis
Update TodoWrite: Complete previous, mark "expert assembly requirements analysis" as in_progress

Execute expert panel requirements assessment using Task and Bash:
- Determine optimal expert diversity for comprehensive coverage
- Assess collaborative potential and synergy opportunities
- Evaluate complexity amplification through expert interaction
- Analyze quality enhancement through multi-expert validation

Use Bash for expert assembly analysis:
```bash
# Expert assembly analysis
expert_count=${#domains[@]}
echo "DOMAIN_COUNT: $expert_count identified domains"
echo "EXPERT_DOMAINS: ${domains[*]}"

# Synergy potential assessment
if [ "$expert_count" -gt 1 ]; then
    echo "SYNERGY_ANALYSIS: Multi-domain collaboration potential detected"
    
    # Cross-domain value calculation
    synergy_pairs=0
    for domain in "${domains[@]}"; do
        for other_domain in "${domains[@]}"; do
            if [[ "$domain" != "$other_domain" ]]; then
                ((synergy_pairs++))
            fi
        done
    done
    
    echo "SYNERGY_PAIRS: $synergy_pairs cross-domain collaboration opportunities"
    
    if [ "$synergy_pairs" -gt 4 ]; then
        echo "HIGH_SYNERGY_POTENTIAL: Enhanced expert collaboration recommended"
        synergy_level="HIGH"
    elif [ "$synergy_pairs" -gt 2 ]; then
        echo "MODERATE_SYNERGY_POTENTIAL: Balanced expert collaboration possible"
        synergy_level="MODERATE"
    else
        echo "BASIC_SYNERGY_POTENTIAL: Simple expert collaboration expected"
        synergy_level="BASIC"
    fi
fi
```

### Phase 3: Dynamic Expert Scaling Assessment
Update TodoWrite: Complete previous, mark "dynamic expert scaling assessment" as in_progress

Execute dynamic scaling analysis without fixed ranges:
- Assess breadth requirements for comprehensive coverage
- Evaluate depth requirements for specialized expertise
- Determine enhancement needs for quality and validation
- Calculate optimization potential through expert coordination

Use Bash for dynamic scaling:
```bash
# Dynamic scaling assessment - no fixed numbers
scaling_factors=()

# Breadth assessment
case "$expert_count" in
    1) scaling_factors+=("FOCUSED"); breadth_level="Single domain focus" ;;
    2-3) scaling_factors+=("DIVERSE"); breadth_level="Multi-domain coverage" ;;
    4-5) scaling_factors+=("COMPREHENSIVE"); breadth_level="Broad domain coverage" ;;
    *) scaling_factors+=("EXTENSIVE"); breadth_level="Complete domain coverage" ;;
esac

# Complexity amplification assessment
if [[ "$complexity" =~ high|complex|advanced|sophisticated ]]; then
    scaling_factors+=("AMPLIFIED")
    echo "COMPLEXITY_AMPLIFICATION: Additional expert specialization recommended"
fi

# Quality enhancement assessment
if [[ "$quality_requirements" =~ critical|high|enterprise|mission ]]; then
    scaling_factors+=("QUALITY_ENHANCED")
    echo "QUALITY_ENHANCEMENT: Validation experts recommended for high standards"
fi

# Timeline optimization assessment
if [[ "$timeline" =~ urgent|immediate|fast|parallel ]]; then
    scaling_factors+=("PARALLEL_OPTIMIZED")
    echo "PARALLEL_OPTIMIZATION: Expert coordination optimized for speed"
fi

echo "SCALING_FACTORS: ${scaling_factors[*]}"
echo "BREADTH_LEVEL: $breadth_level"
```

### Phase 4: Expert Assembly Strategy Generation
Update TodoWrite: Complete previous, mark "expert assembly strategy generation" as in_progress

Generate expert assembly strategy and recommendations:
- Determine optimal expert panel composition
- Generate assembly strategy based on domain requirements
- Provide synergy optimization recommendations
- Create deployment guidance for expert coordination

Use Bash for strategy generation:
```bash
# Expert assembly strategy determination
case "${scaling_factors[*]}" in
    *FOCUSED*)
        assembly_strategy="focused-expert-panel"
        recommendation="Deploy focused expert panel for specific domain solutions with deep specialization"
        ;;
    *DIVERSE*)
        assembly_strategy="diverse-expert-team"
        recommendation="Deploy diverse expert team for cross-functional challenges with balanced collaboration"
        ;;
    *COMPREHENSIVE*)
        assembly_strategy="comprehensive-expert-panel"
        recommendation="Deploy comprehensive expert panel for complex multi-domain work with extensive coverage"
        ;;
    *EXTENSIVE*)
        assembly_strategy="extensive-expert-assembly"
        recommendation="Deploy extensive expert assembly for strategic complexity with complete domain mastery"
        ;;
esac

# Strategy enhancement based on modifiers
if [[ "${scaling_factors[*]}" =~ AMPLIFIED ]]; then
    assembly_strategy="${assembly_strategy}-complexity-enhanced"
fi
if [[ "${scaling_factors[*]}" =~ QUALITY_ENHANCED ]]; then
    assembly_strategy="${assembly_strategy}-quality-assured"
fi
if [[ "${scaling_factors[*]}" =~ PARALLEL_OPTIMIZED ]]; then
    assembly_strategy="${assembly_strategy}-parallel-optimized"
fi
```

### Phase 5: Expert Assembly Report Generation
Update TodoWrite: Complete previous, mark "expert assembly report generation" as in_progress

Generate comprehensive expert assembly assessment using Write and Task:
- Document domain complexity assessment with expert identification
- Report assembly strategy with domain rationale and synergy analysis
- Include dynamic scaling recommendations and optimization guidance
- Provide expert coordination strategy based on collaborative potential

Use Write for expert assembly report generation with comprehensive domain analysis validation.

Update TodoWrite: Complete all expert assembly assessment tasks

**Error Handling**: Validate domain identification with fallback analysis, estimate missing expertise through domain inference, handle complexity overflow with comprehensive assembly, provide fallback expert panel using simplified domain analysis

---

**Expert-Driven Foundation**: Domain complexity assessment through expert identification, synergy analysis, and dynamic assembly strategy determination for optimal AI orchestration without mathematical constraints.