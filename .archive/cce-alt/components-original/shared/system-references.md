# Components Shared Information

## 🎯 INTERNAL OPERATIONAL INFORMATION

**Purpose**: Información operacional mínima necesaria para que los componentes funcionen de manera autocontenida, **SIN referencias a system/**.

### Core Principle  
Esta información debe ser **completamente independiente** - los components no conocen ni referencian system/.

## 📋 OPERATIONAL PROTOCOLS (SELF-CONTAINED)

### Orchestrator Operational Rules
**Internal Protocol** - No external dependencies
**Core Rules**:
- Rule #0: Coherence is survival (>95% threshold)
- Rule #1: Pure coordination - delegate to agents
- Rule #2: Mandatory parallelization when possible
- Rule #3: Mathematical verification required

### Component Communication Standards
**Internal Protocol** - No external dependencies
**Standard Format**: `📊 [LX:TYPE] ACTION | DATA | METRICS`
**Usage**: All internal component communication

### Mathematical Verification Protocol
**Internal Protocol** - No external dependencies
**Requirements**: All operations must be mathematically verified
**Format**: Tool execution → Result validation → Metric calculation

## 🔧 COMPONENT STRUCTURE STANDARDS

### Agent Standard Structure
**Internal Standard** - No external dependencies
**Required Sections**: 
- 🎯 PURPOSE - Clear specialization
- 🚀 DEPLOYMENT - How orchestrators deploy this agent  
- 🔧 OPERATIONAL PROTOCOL - Execution steps
- 📊 SUCCESS METRICS - Performance measurement

### Orchestrator Standard Structure
**Internal Standard** - No external dependencies
**Required Sections**:
- 🎭 IDENTITY - Type, specialization, mission
- 📋 RESPONSIBILITIES - What this orchestrator coordinates
- 🚀 DELEGATION PROTOCOL - How it deploys agents
- 📊 STANDARDS - Quality and performance metrics

### Behavior Standard Structure  
**Internal Standard** - No external dependencies
**Required Sections**:
- 🎯 PURPOSE - What behavior this provides
- 🔧 APPLICATION - How it's applied to components
- 📊 METRICS - How success is measured

## 🏗️ ARCHITECTURE INFORMATION

### System Architecture Summary
**Source**: `../../system/architecture/architecture-overview.md`
**Key Points**:
- Hierarchical cognitive architecture
- Dynamic orchestrator hierarchy
- Component evolution system
- Context optimization protocols

### Cognitive Load Limits
**Source**: `../../system/protocols/cognitive-load-limits.md`
**Critical Limits**:
- Maximum 4 targets per orchestrator
- 200 lines maximum per file
- 70% context usage threshold
- 90% handoff trigger

## 📊 SUCCESS CRITERIA REFERENCES

### Quality Thresholds
**Source**: `../../system/protocols/success-metrics-detailed.md`
**Core Metrics**:
- Precision: ≥85%
- Confidence: ≥90%
- Completeness: ≥75%
- Coherence: >95%

### Performance Targets
**Source**: Various system files
**Key Targets**:
- Response time: <2 seconds
- Context efficiency: <70% usage
- Success rate: >95%
- Error rate: <5%

## 🎭 USAGE PROTOCOL FOR COMPONENTS

### For Agents
```markdown
# ❌ DON'T: ../system/protocols/universal-orchestrator-rules.md
# ✅ DO: components/shared/system-references.md#orchestrator-rules-reference
```

### For Orchestrators
```markdown  
# ❌ DON'T: ../../system/templates/orchestrator-template.md
# ✅ DO: components/shared/system-references.md#orchestrator-template-access
```

### For Behaviors
```markdown
# ❌ DON'T: ../system/architecture/architecture-overview.md  
# ✅ DO: components/shared/system-references.md#system-architecture-summary
```

## ⚡ INTERFACE TO EXTERNAL OPERATIONS

### When System Access Needed
```
Interface.SystemReference("universal-orchestrator-rules") → rules content
Interface.SystemReference("architecture-overview") → architecture info
Interface.SystemReference("success-metrics") → metrics thresholds
```

### Access Patterns
- **Read-only access**: Components never modify system files
- **Reference-based**: Always through this centralized reference
- **Context-aware**: Minimal information transfer
- **Validated access**: Ensure necessary information only

---

**This reference system allows components/ to remain self-contained while accessing essential system information through a controlled, centralized interface.**