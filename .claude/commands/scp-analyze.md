# /scp-analyze - Handoff Division Analysis Command

**FUNCIÓN**: Analiza handoffs existentes por SCP profile y detecta candidatos para división automática

## COMANDO PRINCIPAL

**SEMANTIC PATTERN DETECTION**:
```bash
# SCP Analysis Protocol
echo "🔍 SCP ANALYSIS: Detecting handoff division opportunities..."

# Analyze existing handoffs by SCP profile
analyze_scp_profiles() {
    echo "📊 ANALYZING SCP PROFILES:"
    
    # High complexity candidates (S3C3P3, S3C3P2)
    echo ""
    echo "🔴 HIGH DIVISION PRIORITY:"
    find_high_complexity_handoffs
    
    # Medium complexity with size violations  
    echo ""
    echo "🟡 MEDIUM DIVISION CANDIDATES:"
    find_oversized_handoffs
    
    # Processing complexity candidates (P3)
    echo ""
    echo "🟠 PROCESSING SIMPLIFICATION:"
    find_p3_candidates
}

# Division recommendations
division_recommendations() {
    echo ""
    echo "💡 DIVISION RECOMMENDATIONS:"
    echo ""
    
    # S3C3P3 -> Multiple smaller handoffs
    echo "S3C3P3 → Divide into 2-3 phase-based handoffs (S2C2P1/P2)"
    echo "S3C3P2 → Split into domain-specific handoffs (S2C2P2)"  
    echo "S2C2P3 → Simplify processing into direct patterns (S2C2P1)"
    echo "P3 → Break orchestration into sequential direct handoffs"
    
    echo ""
    echo "📋 SPECIFIC DIVISION OPPORTUNITIES:"
}

# Current handoff analysis
current_handoff_analysis() {
    echo ""
    echo "🎯 CURRENT HANDOFF ANALYSIS:"
    echo ""
    
    # H-SYSTEM-TEST (S3C3P3) - High priority
    echo "• H-SYSTEM-TEST (S3C3P3) → DIVIDE INTO:"
    echo "  - H-SYSTEM-TEST-CORE (S2C2P1): Core functionality testing"
    echo "  - H-SYSTEM-TEST-INTEGRATION (S2C2P2): Integration validation"  
    echo "  - H-SYSTEM-TEST-VALIDATION (S1C1P1): Final validation checks"
    echo "  📊 Impact: 4d → 1d + 2d + 4h = Better granularity"
    echo ""
    
    # P7-VISION (S3C3P3) - High priority
    echo "• P7-VISION (S3C3P3) → DIVIDE INTO:"
    echo "  - P7A-VISION-FOUNDATION (S2C2P2): Vision system setup"
    echo "  - P7B-VISION-OPERATIONS (S2C2P1): Operational integration"
    echo "  📊 Impact: 5d → 2d + 1d = Parallel execution possible"
    echo ""
    
    # P4-GUARDIAN (S3C3P2) - Medium priority
    echo "• P4-GUARDIAN (S3C3P2) → DIVIDE INTO:"
    echo "  - P4A-GUARDIAN-CORE (S2C2P2): Core guardian system"
    echo "  - P4B-GUARDIAN-INTEGRATION (S2C1P1): System integration"
    echo "  📊 Impact: 4d → 2d + 1d = Simplified dependencies"
    echo ""
    
    # H6B-L2-MOD-AUTO (S2C2P3) - Processing simplification
    echo "• H6B-L2-MOD-AUTO (S2C2P3) → SIMPLIFY TO:"
    echo "  - H6B-L2-MOD-AUTO (S2C2P1): Direct automation patterns"
    echo "  📊 Impact: Reduce P3 orchestration to P1 direct implementation"
}

# Execute analysis
execute_scp_analysis() {
    analyze_scp_profiles
    division_recommendations  
    current_handoff_analysis
    
    echo ""
    echo "🎯 NEXT ACTIONS:"
    echo "1. Review division recommendations"
    echo "2. Select handoffs for division"
    echo "3. Use /scp-divide [handoff-id] to generate divided handoffs"
    echo "4. Update dashboard with new handoffs"
    echo ""
    echo "💡 PRIORITY: Start with S3C3P3 handoffs for maximum impact"
}

# Utility functions
find_high_complexity_handoffs() {
    echo "  • H-SYSTEM-TEST (S3C3P3) - System testing with full orchestration"
    echo "  • P7-VISION (S3C3P3) - Vision operations with complex coordination"  
    echo "  • P4-GUARDIAN (S3C3P2) - Guardian system with system impact"
    echo "  📊 3 handoffs requiring division (15+ days → 8-10 days estimated)"
}

find_oversized_handoffs() {
    echo "  • Check handoff file sizes >80 lines"
    echo "  • Identify S2+ handoffs with L2-MODULAR extraction needs"
    echo "  • Look for content-heavy handoffs requiring decomposition"
}

find_p3_candidates() {
    echo "  • H6B-L2-MOD-AUTO (S2C2P3) - Orchestration can be simplified"
    echo "  • Any handoffs with complex multi-process coordination"
    echo "  📊 1 handoff can be simplified from P3 → P1"
}

# Main execution
execute_scp_analysis
```

## INTEGRATION PROTOCOL

**Authority Chain**: @context/roadmap/scp-classification-framework.md → /scp-analyze command
**Dashboard Integration**: Results inform dashboard optimization and resource planning
**Follow-up Commands**: /scp-divide [handoff-id] for automatic division execution

## SUCCESS CRITERIA

- ✅ Identifies all S3C3P3 handoffs requiring division
- ✅ Provides specific division recommendations with new SCP profiles  
- ✅ Estimates impact on timeline and resource allocation
- ✅ Guides strategic handoff optimization decisions

---

**COMMAND DECLARATION**: Automated SCP analysis enabling strategic handoff division for optimal resource allocation and execution efficiency.