# Progressive Disclosure Template

**Purpose**: Template for organizing complex information using progressive disclosure principles to maintain accessibility while providing comprehensive detail.

**Authority**: Template for managing information complexity through layered presentation.

---

## Progressive Disclosure Structure

### Layer 1: Overview (Essential Information)
```markdown
# [Topic Name]

## Quick Summary
[One sentence describing the core concept]

## Key Points
- **[Point 1]**: [Brief essential detail]
- **[Point 2]**: [Brief essential detail]  
- **[Point 3]**: [Brief essential detail]

## Immediate Actions
1. [Most important action]
2. [Second most important action]
3. [Third most important action]

## Success Indicator
[How to know if this is working correctly]

---
*For detailed implementation → See [Layer 2: Implementation Details](#layer-2-implementation-details)*
*For advanced configuration → See [Layer 3: Advanced Details](#layer-3-advanced-details)*
```

### Layer 2: Implementation Details (How-To Information)
```markdown
## Layer 2: Implementation Details

### Prerequisites
- [Requirement 1 with verification method]
- [Requirement 2 with verification method]
- [Requirement 3 with verification method]

### Step-by-Step Process
1. **[Step 1 Name]**: [Detailed description]
   - Expected outcome: [What should happen]
   - Troubleshooting: [Common issues and solutions]

2. **[Step 2 Name]**: [Detailed description]
   - Expected outcome: [What should happen]
   - Troubleshooting: [Common issues and solutions]

3. **[Step 3 Name]**: [Detailed description]
   - Expected outcome: [What should happen]
   - Troubleshooting: [Common issues and solutions]

### Validation Steps
- [ ] [Checkpoint 1]: [How to verify]
- [ ] [Checkpoint 2]: [How to verify]
- [ ] [Checkpoint 3]: [How to verify]

### Common Issues and Solutions
| Issue | Symptoms | Solution |
|-------|----------|----------|
| [Issue 1] | [What you'll see] | [How to fix] |
| [Issue 2] | [What you'll see] | [How to fix] |
| [Issue 3] | [What you'll see] | [How to fix] |

---
*For configuration options → See [Layer 3: Advanced Details](#layer-3-advanced-details)*
*For integration patterns → See [Layer 4: Expert Information](#layer-4-expert-information)*
```

### Layer 3: Advanced Details (Configuration and Customization)
```markdown
## Layer 3: Advanced Details

### Configuration Options
```yaml
# Standard configuration
option_1: value_1  # [Description of what this controls]
option_2: value_2  # [Description of what this controls]
option_3: value_3  # [Description of what this controls]

# Advanced configuration
advanced_option_1: advanced_value_1  # [When to use this]
advanced_option_2: advanced_value_2  # [When to use this]
```

### Customization Patterns
#### Pattern 1: [Pattern Name]
```markdown
**Use Case**: [When to use this pattern]
**Implementation**: [How to implement]
**Benefits**: [Why use this approach]
**Considerations**: [What to be aware of]
```

#### Pattern 2: [Pattern Name]
```markdown
**Use Case**: [When to use this pattern]
**Implementation**: [How to implement]
**Benefits**: [Why use this approach]
**Considerations**: [What to be aware of]
```

### Performance Optimization
- **[Optimization 1]**: [What it does] - [Expected improvement]
- **[Optimization 2]**: [What it does] - [Expected improvement]
- **[Optimization 3]**: [What it does] - [Expected improvement]

### Security Considerations
- **[Security Aspect 1]**: [Requirement and implementation]
- **[Security Aspect 2]**: [Requirement and implementation]
- **[Security Aspect 3]**: [Requirement and implementation]

---
*For architecture details → See [Layer 4: Expert Information](#layer-4-expert-information)*
*For troubleshooting → See [Layer 5: Deep Troubleshooting](#layer-5-deep-troubleshooting)*
```

### Layer 4: Expert Information (Architecture and Theory)
```markdown
## Layer 4: Expert Information

### Architectural Overview
```
[ASCII diagram or description of architecture]
Component A ←→ Component B ←→ Component C
     ↓              ↓              ↓
  Storage A    Processing     Storage B
```

### Design Principles
1. **[Principle 1]**: [Description and rationale]
2. **[Principle 2]**: [Description and rationale]
3. **[Principle 3]**: [Description and rationale]

### Integration Patterns
- **[Integration Type 1]**: [How it works and when to use]
- **[Integration Type 2]**: [How it works and when to use]
- **[Integration Type 3]**: [How it works and when to use]

### Performance Characteristics
| Metric | Typical Range | Optimal Range | Factors |
|--------|---------------|---------------|---------|
| [Metric 1] | [Range] | [Range] | [What affects this] |
| [Metric 2] | [Range] | [Range] | [What affects this] |
| [Metric 3] | [Range] | [Range] | [What affects this] |

### Extension Points
- **[Extension 1]**: [How to extend and what it enables]
- **[Extension 2]**: [How to extend and what it enables]
- **[Extension 3]**: [How to extend and what it enables]

---
*For debugging and diagnostics → See [Layer 5: Deep Troubleshooting](#layer-5-deep-troubleshooting)*
```

### Layer 5: Deep Troubleshooting (Diagnostic Information)
```markdown
## Layer 5: Deep Troubleshooting

### Diagnostic Commands
```bash
# System status check
command --status --verbose

# Performance analysis
command --analyze --performance --duration=300

# Debug mode execution
command --debug --log-level=trace --output=debug.log
```

### Log Analysis
#### Normal Operation Logs
```
[TIMESTAMP] INFO: [Normal message pattern]
[TIMESTAMP] DEBUG: [Debug information pattern]
```

#### Error Patterns
```
[TIMESTAMP] ERROR: [Error pattern 1] → [Cause and solution]
[TIMESTAMP] WARN: [Warning pattern 1] → [Implication and action]
[TIMESTAMP] FATAL: [Critical pattern 1] → [Emergency response]
```

### Advanced Debugging Techniques
1. **[Technique 1]**: [When to use] - [How to execute] - [What to look for]
2. **[Technique 2]**: [When to use] - [How to execute] - [What to look for]
3. **[Technique 3]**: [When to use] - [How to execute] - [What to look for]

### System State Analysis
- **[State Check 1]**: [Command] → [Expected result] vs [Problem indicators]
- **[State Check 2]**: [Command] → [Expected result] vs [Problem indicators]
- **[State Check 3]**: [Command] → [Expected result] vs [Problem indicators]

### Recovery Procedures
#### Scenario 1: [Problem Type]
1. [Recovery step 1]
2. [Recovery step 2]
3. [Verification step]

#### Scenario 2: [Problem Type]
1. [Recovery step 1]
2. [Recovery step 2]
3. [Verification step]
```

---

## Progressive Disclosure Guidelines

### Information Layering Principles
1. **Essential First**: Most critical information in Layer 1
2. **Logical Progression**: Each layer builds on previous layers
3. **Clear Navigation**: Easy movement between layers
4. **Self-Contained Layers**: Each layer provides complete information for its level
5. **Consistent Structure**: Same organization pattern across layers

### Layer Design Standards
- **Layer 1**: ≤200 words, 3-5 key points maximum
- **Layer 2**: Detailed implementation, practical focus
- **Layer 3**: Configuration and customization options
- **Layer 4**: Architecture and theoretical background
- **Layer 5**: Deep diagnostic and troubleshooting information

### Navigation Standards
- **Forward Navigation**: Clear links to more detailed layers
- **Backward Navigation**: Easy return to higher-level information
- **Cross-References**: Links to related topics at appropriate layers
- **Search Optimization**: Keywords and terms for easy discovery

---

## Implementation Guidelines

### For New Topics
1. **Start with Layer 1**: Identify the 3-5 most essential points
2. **Expand systematically**: Build each layer with appropriate detail level
3. **Test navigation**: Ensure easy movement between layers
4. **Validate completeness**: Verify each layer serves its purpose

### For Existing Content
1. **Assess current structure**: Determine if progressive disclosure would help
2. **Identify information layers**: Sort existing content into appropriate layers
3. **Reorganize gradually**: Restructure without losing information
4. **Improve navigation**: Add clear layer transitions and cross-references

---

**Template Type**: Progressive disclosure organization template
**Used By**: Complex topics requiring layered information presentation
**Benefit**: Maintains accessibility while providing comprehensive detail
**Authority**: Standard approach for managing information complexity