# Interactive Placement Guide - Step-by-Step Content Placement Wizard

**30/07/2025 13:30 CDMX** | Detailed interactive guidance for systematic content placement decisions

## AUTORIDAD SUPREMA
context/architecture/ux/component-decision-flowchart.md → interactive-placement-guide.md implements detailed decision assistance per visual flowchart authority

## PRINCIPIO FUNDAMENTAL
**"Step-by-step guidance eliminates guesswork while preserving systematic accuracy"** - Every content placement follows detailed interactive process with examples and validation at each step.

## INTERACTIVE PLACEMENT WIZARD

### **STEP 1: Content Analysis & Classification**

#### **Content Type Identification**

**QUESTION 1.1**: What is the primary nature of your content?

**A. User Vision/Philosophy Content**
- Examples: User requirements, vision statements, preferences, philosophical guidance
- Keywords: "user wants", "vision", "user authority", "user preferences"
- **Next Step**: Go to User Vision Pathway (Section 2A)

**B. Authority/Permission Content** 
- Examples: Domain boundaries, decision hierarchies, authority rules, permission structures
- Keywords: "authority", "permission", "who decides", "domain boundaries"
- **Next Step**: Go to Authority Pathway (Section 2B)

**C. Technical Implementation Content**
- Examples: Patterns, methods, tools, techniques, implementation approaches
- Keywords: "implementation", "pattern", "method", "tool", "technique"
- **Next Step**: Go to Technical Pathway (Section 2C)

**D. Standards/Compliance Content**
- Examples: Requirements, rules, enforcement, validation protocols, compliance measures
- Keywords: "compliance", "requirement", "standard", "rule", "enforcement"
- **Next Step**: Go to Standards Pathway (Section 2D)

**E. Templates/Structure Content**
- Examples: Formats, examples, frameworks, scaffolds, structural guidance
- Keywords: "structure", "format", "template", "example", "framework"
- **Next Step**: Go to Template Pathway (Section 2E)

**F. Data/Metrics Content**
- Examples: Performance data, analytics, measurements, validation metrics
- Keywords: "metrics", "data", "measurement", "performance", "analytics"
- **Next Step**: Go to Data Pathway (Section 2F)

**G. UX/Conversation Content**
- Examples: Dialogue patterns, user experience, interface design, interaction models
- Keywords: "conversation", "dialogue", "user experience", "interface"
- **Next Step**: Go to UX Pathway (Section 2G)

#### **Authority Source Validation**

**QUESTION 1.2**: Who has ultimate authority over this content?

**User Authority**: Content directly from user or representing user voice
- **Validation Required**: Must reference @vision_foundation.md
- **Authority Chain**: VISION.md → context/principles/vision_foundation.md → [content]
- **Critical Check**: Does content preserve exact user voice/intent?

**System Authority**: Content derived from system implementation/optimization
- **Validation Required**: Must reference @TRUTH_SOURCE.md
- **Authority Chain**: TRUTH_SOURCE.md → context/[domain].md → [content]
- **Critical Check**: Does content align with user vision while optimizing system?

**Shared Authority**: Content requiring both user vision and system implementation
- **Validation Required**: Must reference both authority sources
- **Authority Chain**: VISION.md + TRUTH_SOURCE.md → [content]
- **Critical Check**: Does content balance user authority with system effectiveness?

#### **Scope Analysis**

**QUESTION 1.3**: What is the impact scope of this content?

**Component-Specific**: Affects single component or narrow functionality
- **Placement Strategy**: Component-specific location
- **Integration Needs**: Minimal cross-references
- **Example**: Specific tool usage pattern → context/claude_code/[tool]/

**Cross-Component**: Affects multiple components or requires integration
- **Placement Strategy**: Reference architecture needed
- **Integration Needs**: Bidirectional references required
- **Example**: Authority framework affecting UX → reference architecture

**System-Wide**: Affects entire system architecture or foundational principles
- **Placement Strategy**: Architecture-level placement in context/
- **Integration Needs**: System-wide references from all affected components
- **Example**: New user simplicity principle → context/simplicity.md

## PATHWAY-SPECIFIC GUIDANCE

### **SECTION 2A: User Vision Pathway**

#### **Vision Content Classification**

**Step 2A.1**: Classify your vision content type:

**Foundation Vision**: Core user philosophy and principles
- **Location**: context/vision/foundation/[topic].md
- **Authority**: Direct user voice preservation required
- **Integration**: → All system components for validation
- **Example**: User simplicity philosophy → context/vision/foundation/simplicity_philosophy.md

**Evolution Vision**: User guidance on system evolution
- **Location**: context/vision/evolution/[topic].md  
- **Authority**: User authority on growth direction
- **Integration**: → Architecture and methodology components
- **Example**: User growth preferences → context/vision/evolution/organic_growth.md

**Implementation Vision**: User preferences for how things should work
- **Location**: context/vision/implementation/[topic].md
- **Authority**: User authority on operational preferences
- **Integration**: → Methodology and patterns components
- **Example**: User conversation preferences → context/vision/implementation/conversation_style.md

**Step 2A.2**: Authority Validation Checklist

- [ ] Content preserves exact user voice (95%+ fidelity requirement)
- [ ] User quotes preserved with context and reference
- [ ] Authority chain traces to VISION.md
- [ ] No AI interpretation layering detected
- [ ] Content aligns with existing user vision

**Step 2A.3**: Integration Design

```
Vision Integration Template:
├── Primary Location: context/vision/[category]/[topic].md
├── Authority Reference: ↑ VISION.md (supreme user authority)
├── Implementation References: → [affected components]
├── Validation Protocol: User voice fidelity check required
└── Evolution Protocol: User consultation required for changes
```

### **SECTION 2B: Authority Pathway**

#### **Authority Content Classification**

**Step 2B.1**: Identify authority content type:

**Domain Boundaries**: User-AI role separation and permissions
- **Location**: context/authority.md (domain boundaries section)
- **Integration**: ← All components requiring authority validation
- **Example**: User decision domain vs AI implementation domain

**Authority Hierarchy**: Decision-making hierarchy and chains
- **Location**: context/authority.md (authority hierarchy section)
- **Integration**: ← All authority-dependent components
- **Example**: VISION.md → TRUTH_SOURCE.md → component authority chain

**Permission Protocols**: What requires user permission vs automatic execution
- **Location**: context/authority.md (permission protocols section) 
- **Integration**: ← All automated processes and decision points
- **Example**: Architecture changes require user validation protocol

**Step 2B.2**: Authority Integration Checklist

- [ ] Authority chain clearly defined and traceable
- [ ] No authority conflicts with existing hierarchy
- [ ] Domain boundaries respect user supremacy
- [ ] Permission protocols clearly specified
- [ ] Integration pathways preserve authority flow

### **SECTION 2C: Technical Pathway**

#### **Technical Content Classification**

**Step 2C.1**: Identify technical content type:

**General Patterns**: Cross-tool or system-wide technical patterns
- **Location**: context/patterns.md
- **Integration**: ← All technical implementation needing patterns
- **Example**: Research-first protocol applicable to all investigations

**Tool-Specific Patterns**: Claude Code or specific tool implementation patterns  
- **Location**: context/claude_code/[tool]/[pattern].md
- **Integration**: ← Components using specific tool
- **Example**: Task tool delegation patterns → context/claude_code/methodology/task_patterns.md

**Architecture Patterns**: System architecture and organization patterns
- **Location**: context/architecture/[category]/[pattern].md
- **Integration**: ← Architecture-dependent components
- **Example**: Reference architecture pattern → context/architecture/templates/reference_architecture.md

**Step 2C.2**: Technical Validation Checklist

- [ ] Pattern proven through empirical evidence
- [ ] Integration with existing patterns validated
- [ ] Authority alignment with user vision confirmed
- [ ] Implementation examples provided
- [ ] Evolution pathway defined

### **SECTION 2D: Standards Pathway**

#### **Standards Content Classification**

**Step 2D.1**: Identify standards content type:

**Documentation Standards**: Format, style, structure requirements
- **Location**: @standards/documentation_standards.md (via context/standards.md)
- **Integration**: ← All documentation creation
- **Example**: Header format requirements, footer obligations

**Enforcement Standards**: Compliance, validation, quality gate requirements
- **Location**: @standards/enforcement_standards.md (via context/standards.md)
- **Integration**: ← All quality validation processes
- **Example**: Authority chain validation requirements

**Technical Standards**: Implementation, architecture, design requirements
- **Location**: @standards/technical_standards.md (via context/standards.md)
- **Integration**: ← All technical implementation
- **Example**: File size limits, modular architecture requirements

**Step 2D.2**: Standards Integration Design

```
Standards Reference Architecture:
├── Hub: context/standards.md (reference-only coordinator)
├── Specialized: @standards/[category]_standards.md (detailed requirements)
├── Integration: ← All components requiring compliance
├── Enforcement: Guardian role auto-activation on violations
└── Evolution: Standards adapt while preserving core requirements
```

### **SECTION 2E: Template Pathway**

#### **Template Content Classification**

**Step 2E.1**: Identify template content type:

**Command Templates**: Structure for command creation and organization
- **Location**: @templates/commands/[type]_template.md (via context/templates.md)
- **Integration**: ← All command creation processes
- **Example**: Role command template, workflow command template

**Documentation Templates**: Standard documentation structures and formats
- **Location**: @templates/documentation/[type]_template.md (via context/templates.md)
- **Integration**: ← All documentation creation
- **Example**: README template, decision template

**Architecture Templates**: System architecture and organization templates
- **Location**: @templates/architecture/[type]_template.md (via context/templates.md)
- **Integration**: ← All architecture-level content creation
- **Example**: Reference architecture template, integration template

**Step 2E.2**: Template Authority Validation

- [ ] Template serves user vision and preferences
- [ ] Template promotes simplicity and effectiveness
- [ ] Template integrates with existing system architecture
- [ ] Template provides clear usage guidance
- [ ] Template supports organic evolution

### **SECTION 2F: Data Pathway**

#### **Data Content Classification**

**Step 2F.1**: Identify data content type:

**Performance Data**: Metrics, measurements, effectiveness data
- **Location**: context/data/performance/[category].md
- **Integration**: ← Components generating/consuming performance data
- **Example**: Methodology effectiveness metrics, pattern success rates

**Conversation Data**: Dialogue analysis, conversation effectiveness, user interaction data
- **Location**: context/data/conversations/[category].md
- **Integration**: ← Conversation methodology and UX components
- **Example**: Socratic dialogue effectiveness, conversation pattern analysis

**Validation Data**: Compliance metrics, standards adherence, quality measurements
- **Location**: context/data/validation/[category].md
- **Integration**: ← Standards and quality enforcement components
- **Example**: Authority chain compliance, file size compliance metrics

**Step 2F.2**: Data Integration Protocol

```
Data Integration Protocol:
├── Collection: Automated data collection from system operations
├── Storage: Structured storage in appropriate data category
├── Analysis: Regular analysis for system optimization insights  
├── Integration: Data insights feed back into methodology/pattern improvement
└── Evolution: Data collection evolves with system growth
```

### **SECTION 2G: UX Pathway**

#### **UX Content Classification**

**Step 2G.1**: Identify UX content type:

**Conversation Patterns**: Dialogue methodologies, conversation structures
- **Location**: context/architecture/ux/conversation-patterns/[pattern].md
- **Integration**: ← Methodology and command creation components
- **Example**: Socratic methodology pattern, brainstorming pattern

**Interface Design**: User interaction design, interface optimization
- **Location**: context/architecture/ux/interface-design/[category].md
- **Integration**: ← User-facing components and templates
- **Example**: Command interface design, decision interface optimization

**User Experience**: Overall user experience design and optimization
- **Location**: context/architecture/ux/user-experience/[category].md
- **Integration**: ← All user-interaction components
- **Example**: Workflow user experience, system navigation experience

**Step 2G.2**: UX Authority Integration

```
UX Authority Integration:
├── User Authority: UX must serve user vision and preferences
├── Conversation-First: UX promotes natural conversation over rigid structure
├── Simplicity: UX optimizes for information density and ease of use
├── Evolution: UX adapts organically with user needs and system growth
└── Validation: UX effectiveness measured through user satisfaction and efficiency
```

## STEP 3: IMPLEMENTATION DECISION MATRIX

### **Implementation Strategy Selection**

#### **Strategy A: Single File Implementation**

**When to Use**:
- Content < 80 lines
- Single component scope
- Clear authority source
- Minimal integration needs

**Implementation Steps**:
1. Validate authority source and chain
2. Choose location based on pathway analysis
3. Create content with standard header/footer
4. Add necessary cross-references
5. Validate against quality gates

#### **Strategy B: Reference Architecture Implementation**

**When to Use**:
- Content > 80 lines
- Cross-component scope  
- Shared authority
- Complex integration needs

**Implementation Steps**:
1. Design reference architecture with hub + specialized modules
2. Create reference-only hub with forward references
3. Create specialized modules with backward references
4. Implement bidirectional cross-references
5. Validate reference integrity and authority preservation

#### **Strategy C: Integration Enhancement**

**When to Use**:
- Enhancing existing content
- Adding integration to existing component
- Authority chain already established
- Scope matches existing component

**Implementation Steps**:
1. Validate existing authority chain
2. Identify integration points needed
3. Edit existing content to add integration
4. Update cross-references bidirectionally
5. Validate enhanced integration effectiveness

## STEP 4: QUALITY VALIDATION PROTOCOL

### **Pre-Implementation Validation**

#### **Authority Validation Checklist**:
- [ ] Authority source clearly identified and validated
- [ ] Authority chain traces to supreme authority (VISION.md or TRUTH_SOURCE.md)
- [ ] No authority conflicts with existing hierarchy
- [ ] Domain boundaries respected
- [ ] User authority preserved where applicable

#### **Integration Validation Checklist**:
- [ ] Integration pathways designed and documented
- [ ] Bidirectional references planned
- [ ] Cross-component impacts analyzed
- [ ] Navigation pathways optimized
- [ ] Evolution compatibility ensured

#### **Standards Compliance Checklist**:
- [ ] File size within limits (≤80 lines for single files)
- [ ] Standard header/footer format applied
- [ ] Reference syntax standards followed
- [ ] Documentation standards compliance
- [ ] Template usage appropriate

### **Post-Implementation Validation**

#### **Implementation Success Validation**:
- [ ] Content created/edited successfully
- [ ] Authority chain preserved and functional
- [ ] Cross-references work bidirectionally
- [ ] Integration pathways effective
- [ ] Standards compliance maintained

#### **System Integration Validation**:
- [ ] Content integrates seamlessly with existing system
- [ ] No system functionality broken
- [ ] Performance impact acceptable
- [ ] User experience maintained or improved
- [ ] Evolution readiness preserved

## COMMON SCENARIOS & DETAILED EXAMPLES

### **Scenario Example 1: New User Vision Content**

**Content**: User provides new guidance on conversation style preferences

**Step-by-Step Process**:
1. **Classification**: User Vision Content (Section 2A)
2. **Type**: Implementation Vision (user operational preferences)
3. **Authority**: User Authority (requires vision_foundation.md reference)
4. **Scope**: Cross-Component (affects methodology and UX)
5. **Location**: context/vision/implementation/conversation_style.md
6. **Integration**: → context/methodology.md + context/architecture/ux/
7. **Implementation Strategy**: Single File + Cross-References
8. **Quality Gates**: User voice fidelity + authority chain + standards compliance

### **Scenario Example 2: New Technical Pattern Discovery**

**Content**: Discovered effective pattern for Task tool usage with multiple concurrent operations

**Step-by-Step Process**:
1. **Classification**: Technical Implementation Content (Section 2C)
2. **Type**: Tool-Specific Pattern (Claude Code Task tool pattern)
3. **Authority**: System Authority (with user vision alignment)
4. **Scope**: Component-Specific (Task tool usage)
5. **Location**: context/claude_code/methodology/concurrent_task_patterns.md
6. **Integration**: ← context/patterns.md (general patterns), ← methodology components using Task tool
7. **Implementation Strategy**: Single File + Pattern Integration
8. **Quality Gates**: Empirical validation + pattern integration + effectiveness metrics

### **Scenario Example 3: Standards Enhancement**

**Content**: New enforcement requirement for bidirectional reference validation

**Step-by-Step Process**:
1. **Classification**: Standards/Compliance Content (Section 2D)  
2. **Type**: Enforcement Standards (compliance validation)
3. **Authority**: System Authority (enforcing user vision systematically)
4. **Scope**: System-Wide (affects all cross-references)
5. **Location**: @standards/enforcement_standards.md (via context/standards.md reference)
6. **Integration**: ← All components using cross-references
7. **Implementation Strategy**: Reference Architecture (hub + specialized module)
8. **Quality Gates**: System-wide compatibility + enforcement effectiveness + authority preservation

## ERROR HANDLING & TROUBLESHOOTING

### **Common Placement Errors**

#### **Error 1: Authority Confusion**
**Symptoms**: Unclear who has authority over content
**Diagnosis**: Authority source analysis reveals conflicts or ambiguity
**Resolution**: 
1. Research original authority source (user vs system)
2. Trace authority chain to supreme source
3. Resolve conflicts using authority supremacy principle
4. Document resolved authority in content

#### **Error 2: Scope Mismatch**
**Symptoms**: Content impact broader/narrower than placement location suggests
**Diagnosis**: Scope analysis reveals mismatch between content scope and placement strategy
**Resolution**:
1. Re-analyze content scope accurately
2. Identify correct placement strategy for actual scope
3. Migrate content to appropriate location
4. Update integration pathways accordingly

#### **Error 3: Integration Gaps**
**Symptoms**: Content isolated without proper integration with related components
**Diagnosis**: Missing bidirectional references or integration pathways
**Resolution**:
1. Identify all components that should integrate with content
2. Design bidirectional reference architecture
3. Implement cross-references systematically
4. Validate integration effectiveness

#### **Error 4: Standards Violations**
**Symptoms**: Content doesn't meet system standards (file size, format, etc.)
**Diagnosis**: Standards compliance validation fails
**Resolution**:
1. Identify specific standards violations
2. Apply appropriate resolution (modularization, formatting, etc.)
3. Re-validate against all applicable standards
4. Update content to maintain compliance

### **Emergency Resolution Protocol**

#### **When Decision Process Breaks Down**:

**Step 1**: STOP - Do not proceed with uncertain placement
**Step 2**: RESEARCH - Use semantic analysis and similar content examples
**Step 3**: CONSULT - Review COMPONENT_DECISION_MATRIX.md for integration pathways
**Step 4**: VALIDATE - Check against TRUTH_SOURCE.md authority chain
**Step 5**: TEMPORARY - If urgent, use context/working/[temp].md with migration plan
**Step 6**: REVIEW - Schedule proper placement analysis and resolution

---

**INTERACTIVE PLACEMENT GUIDE DECLARATION**: This detailed guidance system implements comprehensive step-by-step decision assistance preserving systematic accuracy while eliminating placement uncertainty. All decisions maintain authority chain integrity and system effectiveness.

**INTEGRATION AUTHORITY**: ↑ component-decision-flowchart.md (visual guidance authority), ←→ COMPONENT_DECISION_MATRIX.md (detailed integration pathways), ← CLAUDE.md (semantic pattern integration)

**EVOLUTION PATHWAY**: Guide evolves through usage → feedback → optimization cycle maintaining user vision supremacy and decision accuracy.