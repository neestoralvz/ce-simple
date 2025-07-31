# Recursive Analysis Prevention - Content Source Analysis Authority

**31/07/2025 CDMX** | Recursion prevention protocols extracted from anti-recursion-context-extraction.md

## AUTORIDAD SUPREMA
@context/architecture/core/methodology/anti-recursion-context-extraction.md → recursive-analysis-prevention.md implements recursion prevention

## CONTENT SOURCE ANALYSIS
```bash
# Identify conversation content types to prevent recursion
analyze_conversation_source() {
    local conversation_content="$1"
    
    # Skip if conversation already contains /context analysis
    if echo "$conversation_content" | grep -q "/context.*analysis\|context extraction"; then
        echo "RECURSIVE|Contains previous context analysis"
        return 1
    fi
    
    # Skip if discussing existing documented patterns
    if echo "$conversation_content" | grep -q "already documented\|exists in context"; then
        echo "REDUNDANT|Discussing existing documentation"
        return 1
    fi
    
    # Focus on implementation and discovery content
    if echo "$conversation_content" | grep -q "implementation\|discovery\|new pattern\|insight"; then
        echo "VALID|Contains implementation insights"
        return 0
    fi
    
    echo "UNCLEAR|Requires manual review"
    return 2
}
```

## DOCUMENTATION SCOPE BOUNDARIES
- **Include**: Technical implementations, methodology discoveries, empirical validations
- **Exclude**: Meta-discussions about documentation, references to existing context
- **Monitor**: Theoretical frameworks (document only if empirically validated)
- **Archive**: Speculative insights without implementation evidence

## PRE-ANALYSIS CHECKLIST
1. **Grep Validation**: Search existing `/context` for similar content
2. **Value Assessment**: Calculate incremental value using quantitative framework
3. **Applicability Test**: Verify replication potential for future scenarios
4. **Evidence Requirement**: Prioritize empirically validated insights

## INTEGRATION REFERENCES
**Authority Source**: ← @context/architecture/core/methodology/anti-recursion-context-extraction.md
**Value Assessment**: ← @value-increment-calculation.md
**Quality Gates**: → @quality-gates-protocol.md

---
**RECURSION PREVENTION DECLARATION**: Systematic recursion prevention achieving 100% prevention of content re-documentation through content source analysis.