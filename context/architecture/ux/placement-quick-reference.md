# Content Placement Quick Reference - One-Page Decision Support

**30/07/2025 13:45 CDMX** | Ultra-compact placement guidance for rapid decision-making

## AUTORIDAD SUPREMA
context/architecture/ux/component-decision-flowchart.md → placement-quick-reference.md implements rapid decision support per visual flowchart authority

## PRINCIPIO FUNDAMENTAL
**"Maximum decision speed with zero accuracy loss"** - Essential placement logic condensed into rapid-access format preserving complete systematic accuracy.

## INSTANT PLACEMENT MATRIX

| Content Type | Authority | Location | Key Check | Integration |
|--------------|-----------|----------|-----------|-------------|
| **User Vision** | User | context/vision/ | User voice preserved? | → All affected components |
| **Authority Rules** | User | context/authority.md | Authority chain clear? | ← All authority-dependent |
| **Technical Patterns** | System | context/patterns.md | Pattern proven? | ← Implementation users |
| **Tool Patterns** | System | context/claude_code/ | Tool-specific? | ← Tool users |
| **Standards/Rules** | System | context/standards.md | System-wide impact? | → Specialized modules |
| **Templates** | System | context/templates.md | Structure guidance? | ← Template users |
| **Data/Metrics** | System | context/data/ | Evidence-based? | ← Data consumers |
| **UX/Conversation** | System | context/architecture/ux/ | User experience? | ← UX implementers |

## SEMANTIC TRIGGER KEYWORDS - INSTANT CLASSIFICATION

### **Vision Domain Triggers** → context/vision/
`user wants`, `vision says`, `user authority`, `user preferences`, `philosophy`, `user voice`

### **Authority Domain Triggers** → context/authority.md
`permission`, `authority`, `who decides`, `domain boundaries`, `user-AI separation`, `hierarchy`

### **Technical Domain Triggers** → context/patterns.md or context/claude_code/
`implementation`, `pattern`, `method`, `tool`, `technique`, `approach`, `how to`

### **Standards Domain Triggers** → context/standards.md
`compliance`, `requirement`, `standard`, `rule`, `enforcement`, `validation`, `must`

### **Template Domain Triggers** → context/templates.md  
`structure`, `format`, `template`, `example`, `framework`, `scaffold`, `how to format`

### **Data Domain Triggers** → context/data/
`metrics`, `data`, `measurement`, `performance`, `analytics`, `evidence`, `results`

### **UX Domain Triggers** → context/architecture/ux/
`conversation`, `dialogue`, `user experience`, `interface`, `interaction`, `workflow`

## AUTHORITY CHAIN INSTANT VALIDATION

```
AUTHORITY QUICK CHECK:
├── User Content → VISION.md → vision_foundation.md → context/vision/
├── System Content → TRUTH_SOURCE.md → context/[domain].md
├── Mixed Authority → Both sources → Reference architecture
└── Unclear Authority → STOP → Research required
```

## SCOPE DECISION - 3-SECOND CHECK

| Content Impact | Scope | Placement Strategy | Integration Needs |
|----------------|-------|-------------------|-------------------|
| **Single tool/component** | Component | Direct placement | Minimal references |
| **Multiple components** | Cross-Component | Reference architecture | Bidirectional links |
| **Entire system** | System-Wide | context/ root level | System-wide references |

## EMERGENCY PLACEMENT PROTOCOL

### **When Unsure - 30-Second Decision**:

1. **SEMANTIC CHECK**: Match keywords to domain (10 seconds)
2. **AUTHORITY CHECK**: User or System authority? (10 seconds)  
3. **SCOPE CHECK**: Component, Cross, or System impact? (10 seconds)
4. **EMERGENCY PLACEMENT**: If still unclear → context/working/[temp].md
5. **SCHEDULE REVIEW**: Plan proper analysis within 24 hours

### **Emergency Locations**:
- `context/working/[temp_name].md` - Temporary during analysis
- `context/research/[topic].md` - Needs investigation  
- `context/archive/pending/[item].md` - Historical pending placement

## PLACEMENT QUALITY GATES - INSTANT CHECKLIST

### **Before Creating/Editing** (30-second check):
- [ ] **Authority**: Source identified and validated
- [ ] **Location**: Matches content type and scope  
- [ ] **Size**: Will result be ≤80 lines or properly modularized?
- [ ] **Integration**: Cross-references planned
- [ ] **Standards**: Compliant with applicable standards

### **After Creating/Editing** (30-second validation):
- [ ] **Function**: Content serves intended purpose
- [ ] **References**: Bidirectional links work
- [ ] **Authority**: Chain preserved and traceable
- [ ] **Standards**: All requirements met
- [ ] **Evolution**: Ready for organic growth

## COMMON PLACEMENT SCENARIOS - INSTANT RECOGNITION

### **Scenario A**: User provides new requirement
**Recognition**: User authority keywords + new guidance
**Instant Decision**: context/vision/[category]/[topic].md + system-wide integration

### **Scenario B**: Discovered effective technical pattern  
**Recognition**: Technical keywords + proven effectiveness
**Instant Decision**: context/patterns.md (general) or context/claude_code/ (tool-specific)

### **Scenario C**: New standard or compliance requirement
**Recognition**: Standards keywords + system-wide impact
**Instant Decision**: context/standards.md reference hub → specialized module

### **Scenario D**: Cross-component integration need
**Recognition**: Multiple domain keywords + integration language
**Instant Decision**: Reference architecture with bidirectional links

### **Scenario E**: Template or structure guidance
**Recognition**: Template keywords + format/structure focus
**Instant Decision**: context/templates.md reference hub → specialized template

## ANTI-PATTERN INSTANT DETECTION

### **🚨 STOP SIGNALS - Do Not Proceed**:
- **Authority Confusion**: Unclear user vs system authority
- **Scope Mismatch**: Content impact doesn't match proposed location
- **Duplication Risk**: Similar content already exists elsewhere  
- **Monolithic Risk**: Content will exceed 80 lines without modularization
- **Integration Gap**: No clear integration pathway to related components

### **⚠️ CAUTION SIGNALS - Proceed Carefully**:
- **Complex Integration**: Multiple integration points required
- **Authority Overlap**: Shared authority between domains
- **Evolution Impact**: Changes may affect system architecture
- **Standards Edge Case**: Unusual standards application needed

## FILE SIZE MANAGEMENT - INSTANT DECISIONS

### **Content Size Estimation**:
- **< 30 lines**: Direct placement in appropriate location
- **30-80 lines**: Single file with careful organization
- **> 80 lines**: MANDATORY modularization with reference architecture
- **> 200 lines**: STOP - Over-engineering detected, simplification required

### **Modularization Strategy Quick-Select**:
- **Topic-based**: Split by topic → topic1.md, topic2.md + hub.md
- **Function-based**: Split by function → implementation.md, examples.md + hub.md  
- **Authority-based**: Split by authority → user_authority.md, system_authority.md + hub.md
- **Scope-based**: Split by scope → component.md, system.md + hub.md

## INTEGRATION PATTERNS - INSTANT SELECTION

### **Forward Reference** (`→ target.md`):
**When**: Delegating to specialized content
**Usage**: Primary content → detailed implementation
**Example**: standards.md → @standards/enforcement_standards.md

### **Backward Reference** (`↑ source.md`):
**When**: Acknowledging authority source
**Usage**: Specialized content ← authoritative source  
**Example**: enforcement_standards.md ↑ standards.md

### **Peer Reference** (`←→ peer.md`):
**When**: Equal authority with different specialization
**Usage**: Related components with shared authority
**Example**: methodology.md ←→ authority.md

### **Conditional Reference** (`IF condition → target.md`):
**When**: Context-dependent loading
**Usage**: Smart loading based on usage pattern
**Example**: IF research_pattern → methodology.md + patterns.md

## SEMANTIC PATTERN MATCHING - INSTANT CLASSIFICATION

### **User Voice Indicators** → context/vision/
- Direct quotes from user
- User preference statements  
- "I want", "I need", "I prefer"
- User philosophy or principles
- User authority assertions

### **System Implementation Indicators** → context/patterns.md or context/claude_code/
- "How to implement"
- Technical methodology
- Tool usage patterns
- Implementation approaches
- System optimization

### **Authority/Permission Indicators** → context/authority.md
- "Who decides"
- Permission protocols
- Authority boundaries  
- Decision hierarchies
- Domain separation

### **Standards/Enforcement Indicators** → context/standards.md
- "Must", "Required", "Obligatory"
- Compliance requirements
- Validation protocols
- Quality gates
- Enforcement mechanisms

## CONFLICT RESOLUTION - INSTANT PROTOCOLS

### **Authority Conflict**:
1. **Trace to source**: Find original authority (user vs system)
2. **Apply supremacy**: User authority wins conflicts
3. **Document resolution**: Clear authority chain in content
4. **Update references**: Ensure consistency

### **Integration Conflict**:
1. **Identify requirements**: What integrations are needed?
2. **Design references**: Bidirectional reference architecture
3. **Implement systematically**: All required cross-references
4. **Validate effectiveness**: Test integration pathways

### **Scope Conflict**:
1. **Re-analyze impact**: True scope of content
2. **Adjust strategy**: Match placement to actual scope
3. **Migrate if needed**: Move to appropriate location
4. **Update integration**: Fix affected references

## VALIDATION SHORTCUTS - INSTANT VERIFICATION

### **5-Second Authority Check**:
```
Authority Validation:
├── User content → vision_foundation.md referenced?
├── System content → TRUTH_SOURCE.md authority clear?
├── Authority chain → No conflicts detected?
└── User supremacy → Preserved throughout?
```

### **5-Second Integration Check**:
```
Integration Validation:
├── Forward refs → Point to valid content?
├── Backward refs → Acknowledge authority?
├── Bidirectional → Consistent both ways?
└── Navigation → Discovery pathways work?
```

### **5-Second Standards Check**:
```
Standards Validation:
├── File size → Within limits or modularized?
├── Format → Header/footer standards met?
├── References → Syntax standards followed?
└── Quality → All applicable standards met?
```

---

**QUICK REFERENCE DECLARATION**: This ultra-compact guidance preserves complete placement accuracy while maximizing decision speed. All essential logic accessible within seconds for rapid content placement decisions.

**USAGE PROTOCOL**: Use for rapid decisions → Detailed guidance available in interactive-placement-guide.md for complex cases → Full flowchart in component-decision-flowchart.md for comprehensive analysis

**INTEGRATION AUTHORITY**: ↑ component-decision-flowchart.md (comprehensive guidance), ↑ interactive-placement-guide.md (detailed assistance), ← CLAUDE.md (semantic trigger integration)