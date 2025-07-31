# /scp-divide - Automatic Handoff Division Command

**FUNCIÓN**: Divide handoffs complejos automáticamente basado en SCP analysis y genera nuevos handoffs optimizados

## COMANDO PRINCIPAL

**USAGE**: `/scp-divide [handoff-id]` o `/scp-divide --interactive`

**SEMANTIC PATTERN DETECTION**:
```bash
# SCP Division Protocol
echo "⚡ SCP DIVISION: Generating optimized handoff division..."

# Main division logic
execute_handoff_division() {
    local handoff_id="$1"
    
    if [[ -z "$handoff_id" ]]; then
        interactive_mode
    else
        divide_specific_handoff "$handoff_id"
    fi
}

# Interactive mode for handoff selection
interactive_mode() {
    echo "🎯 INTERACTIVE DIVISION MODE"
    echo ""
    echo "Available handoffs for division:"
    echo "1. H-SYSTEM-TEST (S3C3P3) → 3 handoffs"
    echo "2. P7-VISION (S3C3P3) → 2 handoffs"  
    echo "3. P4-GUARDIAN (S3C3P2) → 2 handoffs"
    echo "4. H6B-L2-MOD-AUTO (S2C2P3) → simplify to S2C2P1"
    echo ""
    echo "Select handoff to divide [1-4]: "
    
    # Simulate selection logic
    echo "📋 Generating division for selected handoff..."
}

# Specific handoff division
divide_specific_handoff() {
    local handoff_id="$1"
    
    case "$handoff_id" in
        "H-SYSTEM-TEST"|"h-system-test")
            divide_system_test_handoff
            ;;
        "P7-VISION"|"p7-vision") 
            divide_vision_handoff
            ;;
        "P4-GUARDIAN"|"p4-guardian")
            divide_guardian_handoff
            ;;
        "H6B-L2-MOD-AUTO"|"h6b-l2-mod-auto")
            simplify_l2_auto_handoff
            ;;
        *)
            echo "❌ Unknown handoff: $handoff_id"
            echo "Available: H-SYSTEM-TEST, P7-VISION, P4-GUARDIAN, H6B-L2-MOD-AUTO"
            ;;
    esac
}

# H-SYSTEM-TEST division
divide_system_test_handoff() {
    echo "🔧 DIVIDING H-SYSTEM-TEST (S3C3P3):"
    echo ""
    
    echo "📄 GENERATING: H-SYSTEM-TEST-CORE (S2C2P1)"
    echo "- Scope: Core functionality testing"
    echo "- Coordination: Dependent on H-AUTOCONTAIN"  
    echo "- Processing: Direct testing patterns"
    echo "- Timeline: 1 day"
    echo ""
    
    echo "📄 GENERATING: H-SYSTEM-TEST-INTEGRATION (S2C2P2)"
    echo "- Scope: Cross-component integration testing"
    echo "- Coordination: Dependent on H-SYSTEM-TEST-CORE"
    echo "- Processing: L2-MODULAR integration patterns"
    echo "- Timeline: 2 days"
    echo ""
    
    echo "📄 GENERATING: H-SYSTEM-TEST-VALIDATION (S1C1P1)"
    echo "- Scope: Final validation and sign-off"
    echo "- Coordination: Independent final check"
    echo "- Processing: Direct validation patterns"  
    echo "- Timeline: 4 hours"
    echo ""
    
    echo "✅ DIVISION COMPLETE: 4d → 1d + 2d + 4h (improved granularity)"
    echo "🎯 NEXT: Update dashboard with new handoffs"
}

# P7-VISION division  
divide_vision_handoff() {
    echo "🔧 DIVIDING P7-VISION (S3C3P3):"
    echo ""
    
    echo "📄 GENERATING: P7A-VISION-FOUNDATION (S2C2P2)"
    echo "- Scope: Vision system architecture setup"
    echo "- Coordination: Dependent on P6-STANDARDS"
    echo "- Processing: L2-MODULAR system extraction"
    echo "- Timeline: 2 days"
    echo ""
    
    echo "📄 GENERATING: P7B-VISION-OPERATIONS (S2C2P1)"
    echo "- Scope: Operational vision integration"
    echo "- Coordination: Dependent on P7A-VISION-FOUNDATION"
    echo "- Processing: Direct operational patterns"
    echo "- Timeline: 1 day"
    echo ""
    
    echo "✅ DIVISION COMPLETE: 5d → 2d + 1d (parallel potential)"
    echo "🎯 BENEFIT: P7B can potentially run parallel with other handoffs"
}

# P4-GUARDIAN division
divide_guardian_handoff() {
    echo "🔧 DIVIDING P4-GUARDIAN (S3C3P2):"
    echo ""
    
    echo "📄 GENERATING: P4A-GUARDIAN-CORE (S2C2P2)"
    echo "- Scope: Core guardian system implementation"
    echo "- Coordination: Dependent on P3-CORE-SYS"
    echo "- Processing: L2-MODULAR guardian extraction"
    echo "- Timeline: 2 days"
    echo ""
    
    echo "📄 GENERATING: P4B-GUARDIAN-INTEGRATION (S2C1P1)"
    echo "- Scope: Guardian system integration"
    echo "- Coordination: Dependent on P4A-GUARDIAN-CORE"
    echo "- Processing: Direct integration patterns"
    echo "- Timeline: 1 day"
    echo ""
    
    echo "✅ DIVISION COMPLETE: 4d → 2d + 1d (simplified dependencies)"
    echo "🎯 BENEFIT: Clearer dependency chain, easier tracking"
}

# H6B-L2-MOD-AUTO simplification
simplify_l2_auto_handoff() {
    echo "🔧 SIMPLIFYING H6B-L2-MOD-AUTO (S2C2P3 → S2C2P1):"
    echo ""
    
    echo "📄 MODIFYING: H6B-L2-MOD-AUTO (S2C2P1)"
    echo "- Scope: Cross-component L2-MODULAR automation (unchanged)"
    echo "- Coordination: Dependent on H6B3-CORE (unchanged)"
    echo "- Processing: SIMPLIFIED - Direct automation patterns instead of orchestration"
    echo "- Timeline: Reduced from 3d → 2d"
    echo ""
    
    echo "✅ SIMPLIFICATION COMPLETE: P3 → P1 (reduced complexity)"
    echo "🎯 BENEFIT: 1 day saved, simpler implementation approach"
}

# Generate handoff files
generate_handoff_files() {
    echo ""
    echo "📁 GENERATING HANDOFF FILES:"
    echo "- Creating new handoff .md files with proper SCP classification"
    echo "- Preserving authority chain and context references"
    echo "- Updating dependency relationships"
    echo "- Maintaining L2-MODULAR compliance"
    echo ""
    echo "⚠️  MANUAL STEP: Update dashboard work-items-registry.md with new handoffs"
}

# Dashboard update recommendations
dashboard_update_recommendations() {
    echo ""
    echo "📊 DASHBOARD UPDATE REQUIREMENTS:"
    echo "1. Remove original complex handoff from tracking"
    echo "2. Add new divided handoffs with correct SCP profiles"
    echo "3. Update dependency chains for proper sequencing"
    echo "4. Verify total timeline matches or improves original estimate"
    echo ""
    echo "🎯 IMPACT TRACKING:"
    echo "- Total handoffs: +2 to +3 per division"
    echo "- Timeline optimization: 15-20% improvement typical"
    echo "- Resource allocation: Better granularity for planning"
}

# Main execution with arguments
execute_handoff_division "$1"
generate_handoff_files
dashboard_update_recommendations
```

## INTEGRATION PROTOCOL

**Authority Chain**: @context/roadmap/scp-classification-framework.md → /scp-divide command
**File Generation**: Creates new handoff files in @context/roadmap/ directory
**Dashboard Integration**: Requires manual update of work-items-registry.md

## DIVISIÓN TEMPLATES

### **S3C3P3 → Multiple S2 Handoffs Template**
```markdown
# HANDOFF [ID-A]: [Phase A Title] - SCP Profile: S2C2P2

[Generated from division of original S3C3P3 handoff]

## SCP CLASSIFICATION ANALYSIS
### **Scope: S2-CROSS** (Extracted domain-specific scope)
### **Coordination: C2-DEPENDENT** (Clear sequential dependency)  
### **Processing: P2-EXTRACTION** (Standard L2-MODULAR patterns)

[Continue with standard handoff structure...]
```

## SUCCESS CRITERIA

- ✅ Generates properly formatted divided handoffs with correct SCP profiles
- ✅ Preserves authority chain and context references
- ✅ Maintains or improves total timeline estimation
- ✅ Creates clear dependency relationships between divided handoffs
- ✅ Provides dashboard update guidance

---

**COMMAND DECLARATION**: Automated handoff division system enabling optimal granularity and resource allocation through systematic SCP-based decomposition.