# PPO Progressive Disclosure Templates
**Token-Efficient Information Architecture for All System Components**

## 🎯 Token Efficiency Design Philosophy

### Core Principle
**User Insight Applied**: *"Va a costar tokens, entonces hay que hacerlo de manera eficiente"*

**Progressive Disclosure = Core Accessibility + Referenced Depth**
- **Immediate Access**: Essential functionality and interfaces
- **Progressive Access**: Complex details through structured references  
- **Token Optimization**: Maximum information density per cognitive unit
- **Modular Architecture**: Contained complexity with clear interfaces

## 📊 Universal Size Compliance Framework

### File Size Standards (PPO-Compliant)
```javascript
// Universal size targets - token-optimized
const TARGETS = {
  COMMAND_FILE: 140,        // lines - immediate command functionality
  CONTEXT_FILE: 200,        // lines - discovery and pattern documentation  
  IMPLEMENTATION: 500,      // lines - detailed technical specifications
  EXTRACTION_THRESHOLD: 110 // lines - when to apply progressive disclosure
};

// Progressive disclosure trigger protocol
function shouldExtract(file) {
  return file.lines > TARGETS.EXTRACTION_THRESHOLD && 
         file.type === 'command' && 
         hasVerboseContent(file);
}
```

### Token Cost Optimization Matrix
```
┌─────────────────┬──────────────┬──────────────┬──────────────┐
│ Content Type    │ Immediate    │ Progressive  │ Cost Ratio   │
├─────────────────┼──────────────┼──────────────┼──────────────┤
│ Command Core    │ 100%         │ 0%           │ 1:0 (Optimal)│
│ Implementation  │ 20%          │ 80%          │ 1:4 (Efficient)│
│ Context         │ 40%          │ 60%          │ 2:3 (Good)   │
│ Documentation   │ 30%          │ 70%          │ 3:7 (Standard)│
└─────────────────┴──────────────┴──────────────┴──────────────┘
```

## 🎯 Command Progressive Disclosure Template

### Universal Command Structure (PPO-Standard)
```markdown
# Command-Name - PPO-Enabled Brief Description

## 🎯 Purpose
[Single sentence - immediate clarity]

## 🚀 Usage  
Execute: `/command-name [essential-args]`

## 🔧 Implementation

### PPO Behavioral Reinforcement Protocol
**MANDATORY at command initialization**:
```javascript
TodoWrite([
  {"content": "🛡️ PREVENTION: [prevention-specific - immediate clarity]", "status": "pending", "priority": "high"},
  {"content": "📊 PROGRESSIVE: [disclosure optimization - immediate scope]", "status": "pending", "priority": "high"}, 
  {"content": "🤖 ORCHESTRATION: [agent coordination - immediate requirements]", "status": "pending", "priority": "medium"}
])
```

### Core Functionality Protocol
[Essential workflow - immediately accessible - <50 lines]

### Integration Points
[Critical dependencies - immediate awareness - <20 lines]

*Complete implementation details in `docs/implementation/[command-name]-implementation.md`*
*Advanced patterns in `context/patterns/[command-name]-patterns.md`*

## 🔗 PPO Integration
**Prevention**: [How this command prevents failures - 1 sentence]
**Progressive**: [How complexity is managed - 1 sentence]  
**Orchestration**: [How agents are coordinated - 1 sentence]

### Output Locations
- `context/discoveries/` → [Brief output description]
- `context/patterns/` → [Brief pattern documentation]

## 🔗 See Also
- `docs/implementation/[command-name]-implementation.md` - Complete technical specifications
- `context/patterns/[command-name]-patterns.md` - Advanced usage patterns

---
**Target**: ≤140 lines | **Core Function**: 100% accessible | **Complex Details**: Referenced
```

## 📋 Implementation File Template

### Implementation Details Structure (PPO-Referenced)
```markdown
# Command-Name Implementation - PPO Technical Specifications

## 🎯 Complete Technical Framework
*Referenced from `/command-name` for detailed implementation*

### Advanced Configuration Protocols
[Detailed technical specifications - 200-500 lines allowed]

### Complex Integration Patterns  
[Advanced usage patterns and edge cases]

### Performance Optimization Framework
[Detailed performance specifications and tuning]

### FMEA Risk Assessment Matrix
[Complete FMEA analysis with all failure modes]

### Advanced Troubleshooting Guide
[Comprehensive problem resolution protocols]

## 🎯 Success Metrics & Validation
[Detailed performance metrics and validation protocols]

## 🔗 Cross-Reference Network
[Complete integration documentation with other commands]

---
**Purpose**: Progressive disclosure target for complex implementation details
**Access Pattern**: Command → Implementation → Patterns → Context
```

## 📊 Context File Template  

### Discovery Documentation Structure (PPO-Optimized)
```markdown
# Discovery-Topic - PPO Context Documentation

**Session**: [timestamp] | **Learning Value**: [score]/10 | **Complexity**: [level]/10

## 📊 Key Discoveries
[High-density insights - maximum information per line]

### Pattern Identification
[Evidence-based patterns - anti-bias documentation]

### System Integration Insights
[Cross-command implications and integration points]

### Performance Impact Assessment
[Token efficiency and resource optimization insights]

## 🎯 Implementation Recommendations
[Actionable insights for system enhancement]

## 🔗 Cross-References  
[Related discoveries, patterns, and implementation files]

---
**Target**: ≤200 lines | **Density**: Maximum insights per token | **Evidence**: 100% supported
```

## 🚀 Progressive Disclosure Automation

### Extraction Protocol (PPO-Automated)
```javascript
// Automated progressive disclosure application
function applyProgressiveDisclosure(file) {
  if (file.lines > TARGETS.EXTRACTION_THRESHOLD && file.type === 'command') {
    
    // Identify extraction candidates
    const verbose = identifyVerboseContent(file);
    const core = identifyCoreContent(file);
    const references = maintainReferences(file);
    
    // Execute extraction
    extractToImplementation(verbose, `docs/implementation/${file.name}-implementation.md`);
    maintainCoreInCommand(core, file.path);
    updateReferences(references, file.path);
    
    // Validate integrity  
    validateExtractionIntegrity(file);
    confirmAccessibilityMaintained(file);
    
    return {
      status: 'extraction_complete',
      before: file.lines,
      after: calculateNewSize(file),
      efficiency: calculateTokenSavings(file)
    };
  }
}
```

### Reference Integrity Framework
```javascript
// Reference maintenance protocol
function maintainReferenceIntegrity(extraction) {
  const references = generateReferences(extraction);
  const crossLinks = updateCrossLinks(extraction);
  const validation = validateLinkIntegrity(references);
  
  return {
    references: references,      // Updated reference network
    crossLinks: crossLinks,      // Cross-command integration
    integrity: validation,       // Link validation results
    accessibility: 'maintained' // Core functionality preserved
  };
}
```

## 📊 Progressive Disclosure Success Metrics

### Token Efficiency Indicators
- **Size Compliance**: >95% files within optimal ranges
- **Access Efficiency**: Core functionality immediately accessible (100%)
- **Reference Integrity**: Zero broken links after extraction  
- **Cost Optimization**: >40% token usage reduction through disclosure

### Information Architecture Quality
- **Cognitive Load**: <15% increase in access complexity
- **Functionality Preservation**: 100% feature accessibility maintained
- **Progressive Access**: Complex details available within 1-2 clicks
- **Modular Coherence**: Clear separation between core and advanced content

### System Performance Impact
- **Command Execution**: No performance degradation from extraction
- **Cross-Reference Speed**: <500ms average reference resolution
- **Context Loading**: Progressive loading reduces initial token cost
- **Maintenance Overhead**: <10% additional maintenance complexity

## 🎯 Template Application Protocol

### Phase 1: Command Optimization (Immediate)
1. **Audit Current Commands**: Identify files >110 lines needing extraction
2. **Apply Command Template**: Standardize structure with PPO integration
3. **Extract Verbose Content**: Move detailed specifications to implementation files
4. **Update References**: Maintain complete link integrity
5. **Validate Functionality**: Confirm 100% feature accessibility preserved

### Phase 2: Implementation Enhancement (Week 2)
1. **Standardize Implementation Files**: Apply implementation template structure
2. **Enhance Technical Depth**: Expand detailed specifications in referenced files
3. **Integrate FMEA Analysis**: Embed complete risk assessment matrices
4. **Cross-Reference Optimization**: Strengthen inter-file connection network

### Phase 3: Context Optimization (Week 3)  
1. **Apply Context Templates**: Standardize discovery and pattern documentation
2. **Maximize Information Density**: Optimize insights per line ratio
3. **Evidence-Based Documentation**: Ensure all patterns supported by evidence
4. **Cross-Command Integration**: Strengthen pattern interconnection network

## 🔗 Template Compliance Validation

### Automated Template Audit
```javascript
function validateTemplateCompliance(file) {
  const structure = validateStructure(file);
  const size = validateSizeCompliance(file);
  const references = validateReferenceIntegrity(file);
  const ppo = validatePPOIntegration(file);
  
  return {
    compliance: (structure && size && references && ppo),
    score: calculateComplianceScore(file),
    recommendations: generateOptimizations(file)
  };
}
```

### Compliance Success Indicators
- ✅ **Structure**: PPO-standard template followed  
- ✅ **Size**: Within token-optimized ranges
- ✅ **References**: Complete integrity maintained  
- ✅ **PPO Integration**: Prevention + Progressive + Orchestration embedded
- ✅ **Functionality**: 100% accessibility preserved
- ✅ **Efficiency**: >40% token cost optimization achieved

---

**CRITICAL**: These templates operationalize the user insight that "Progressive Disclosure me parece fundamental" and "va a costar tokens, entonces hay que hacerlo de manera eficiente" through systematic information architecture optimization. ALL system components MUST apply these templates for token-efficient, modular design with contained complexity.