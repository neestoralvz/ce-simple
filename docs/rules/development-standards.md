# Development Standards

**Last Updated: 2025-07-23**
**Authority**: Technical implementation standards implementing Partnership Protocol

## Quality Framework - PTS Compliance

### PTS (Pragmatic Technical Simplicity) - 12 Mandatory Components

**Technical Cluster**:
- **Directness**: Most direct path to objective (≤3 steps)
- **Precision**: Technical accuracy and specificity (100% correct paths)
- **Sufficiency**: Exactly what's needed, complete but minimal
- **Technical Excellence**: Impeccable quality in simple solution

**Communication Cluster**:
- **Exactitude**: Implementation at exact required point
- **Sobriety**: Professional approach, zero embellishments or marketing language
- **Structure**: Logical, clear, well-structured organization
- **Conciseness**: Maximum value per unit of complexity

**Cognitive Cluster**:
- **Clarity**: Immediate comprehension without ambiguity
- **Coherence**: Absolute internal consistency
- **Effectiveness**: Produces measurable successful results
- **Pragmatism**: Works effectively in real conditions

**🛑 BLOCKING REQUIREMENT**: 12/12 PTS components must pass before proceeding

## Technical Implementation Standards

### Line Limits and Scope Control
- **Commands**: Maximum 150 lines (cognitive load management)
- **Documentation**: Maximum 200 lines (LLM consumption optimization)
- **Blocking Enforcement**: Development stops when limits exceeded
- **Quality over Quantity**: Prefer focused, single-purpose components

### Autocontained Principle
- **Self-Containment**: Commands can only reference other commands via slash command calls
- **Embedded Logic**: All necessary logic, patterns, and templates included inline
- **No External Dependencies**: Commands work without external configuration
- **Single Responsibility**: Each command does exactly one thing well

## New Rules Integration

### Error Resolution Rule
**Systematic Debugging with Visual Validation**:
- **5-Phase Approach**: Deep exploration → External research → Think x4 analysis → Integral solutions → Logging escalation
- **Visual Integration**: Screenshot capture and browser console analysis for UI/frontend issues
- **Root Cause Focus**: Address underlying causes, not symptoms, for permanent resolution
- **Preventive Monitoring**: Build detection and prevention directly into solutions

### Pattern Storage Rule
**Internal Timestamp Logging**:
- **No Filename Timestamps**: Use internal timestamp logging for pattern evolution
- **Flexible Categorization**: Dynamic pattern organization without rigid file structure
- **Auto-Capture Mechanism**: Patterns automatically discovered and documented
- **Evolution Tracking**: Internal timestamp entries for pattern development history

### Vision Authority Rule Implementation
- **docs/vision/ Reference**: All technical decisions validated against vision documents
- **Authority Hierarchy**: Vision → Core Principles → Implementation (strict enforcement)
- **Evolution Control**: Technical changes guided by vision, not reactive development
- **Decision Framework**: Every technical choice traceable to documented vision

## Code Architecture Standards

### Single Responsibility Enforcement
- **One Purpose**: Each component handles exactly one workflow or function
- **Clear Boundaries**: Distinct separation of concerns between components
- **Focused Functionality**: Avoid feature creep and scope expansion
- **Modular Design**: Independent components that can be composed

### Orchestration Patterns
- **Simple Building Blocks**: Basic commands that do one thing well
- **Orchestrator Commands**: Commands that coordinate multiple simple commands
- **Complex Workflows**: Built from composition of simple, reliable components
- **Clear Hierarchies**: Logical organization from simple to complex functionality

## Quality Assurance Framework

### Pre-Development Validation
- **PTS Pre-Check**: 2-minute essential criteria validation
- **Vision Alignment**: Validate concept against docs/vision/overview.md
- **Principle Compliance**: Check against development principles
- **Resource Planning**: Determine optimal implementation approach

### Development Quality Gates
- **Real-Time Validation**: Apply PTS checklist continuously during development
- **Length Monitoring**: Track line count against established limits
- **Compliance Checking**: Verify adherence to technical standards
- **Integration Testing**: Validate component interactions and dependencies

### Post-Development Verification
- **Complete PTS Validation**: Full 12-component assessment before deployment
- **Integration Testing**: Verify system integration and compatibility
- **Documentation Updates**: Ensure all references and documentation current
- **Pattern Capture**: Document successful patterns for reuse

---

**Application**: These standards ensure technical excellence while maintaining system simplicity and user experience. Reference during development, code review, and quality validation processes.