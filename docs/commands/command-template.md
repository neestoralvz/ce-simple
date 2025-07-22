# Command Template - Standardized Command Structure

## 🎯 Purpose
Provide standardized template for creating consistent, functional commands with all required sections and cross-reference integration.

## 🚀 Template Structure

### Universal Command Format
```markdown
# [Command-Name] - [Brief Description]

## 🎯 Purpose
[Single line objective - what this command accomplishes]

## 🚀 Usage  
Execute: `/[command-name] [parameters]`

## 🔧 Implementation

### [Primary Protocol Name]
1. **[STEP-1]**: [Specific implementation instruction]
2. **[STEP-2]**: [Additional implementation details]  
3. **[STEP-3]**: [Result processing requirements]
4. **[STEP-4]**: [Error handling procedures]
5. **[STEP-5]**: [Context integration protocols]

### [Secondary Framework Name]
[Additional implementation details as needed]

### [Integration Protocol Name]
[How this command connects with others]

## ⚡ Triggers

### Input Triggers
**Context**: [Situation requiring this command]
**Previous**: `/[previous-command]` → [condition leading here]
**Keywords**: [contextual terms that suggest this command]

### Output Triggers
**When**: [Result condition] → `/[next-command]` for [reason]
**When**: [Alternative condition] → `/[alternative-command]` for [reason]
**Chain**: [command1] → [command2] → [command3]

### Success Patterns
**[Success-Type] Success**: [Success condition] → [Suggested next action]
**[Quality-Type] Success**: [Quality condition] → [Quality next action]
**[Integration-Type] Success**: [Integration condition] → [Integration action]

---

**CRITICAL**: [Any critical implementation requirements or warnings]
```

## 📋 REQUIRED SECTIONS

### Header Requirements
- **Command Name**: Clear, action-oriented, hyphen-separated
- **Brief Description**: 3-5 words describing primary function
- **Purpose**: Single line explaining value and objective

### Usage Requirements  
- **Execute Format**: Standard `/command-name [parameters]` format
- **Parameter Clarity**: Clear parameter descriptions when applicable
- **Optional Indicators**: Mark optional parameters clearly

### Implementation Requirements
- **Protocol Structure**: Numbered steps with action verbs
- **Capital Keywords**: CRITICAL, MANDATORY, REQUIRED for important actions
- **Integration Points**: How command connects with system
- **Error Handling**: Explicit failure and recovery procedures

### Triggers Requirements
- **Input Triggers**: What conditions activate this command
- **Output Triggers**: What commands this leads to  
- **Success Patterns**: Clear success criteria and next steps
- **Chain Definition**: Typical workflow sequences

## 🔧 TEMPLATE VARIABLES

### Replaceable Elements
- `[Command-Name]` → Actual command name in Title Case
- `[command-name]` → Lowercase command name with hyphens
- `[Brief Description]` → 3-5 word functional description
- `[parameters]` → Actual parameter list or "none"
- `[STEP-N]` → Implementation step with action verb
- `[Previous-Command]` → Actual previous command in workflow
- `[Next-Command]` → Actual next command in workflow

### Standard Sections
- `[Primary Protocol Name]` → Main implementation approach
- `[Secondary Framework Name]` → Additional methodologies
- `[Integration Protocol Name]` → Cross-command connections
- `[Success-Type]` → Specific success category

## 📊 SYMBOL STANDARDS

### Required Symbols
- **🎯 Purpose**: Objective and value statement
- **🚀 Usage**: Command execution format
- **🔧 Implementation**: Technical implementation details
- **⚡ Triggers**: Input/output command connections

### Optional Symbols
- **📊 Data/Metrics**: When command involves data analysis
- **🔄 Workflow**: When command manages process flows  
- **✓ Validation**: When command includes verification steps
- **⚠️ Warnings**: When command has important limitations
- **🔗 Integration**: When command has complex cross-references

## 📋 QUALITY STANDARDS

### Content Requirements
- **File Size Limits**: Follow standards in `standards/writing-standards.md` for consistency
- **Single Responsibility**: One primary function per command
- **Self-Contained**: All necessary information included
- **Cross-Referenced**: Clear connections to related commands

### 🚫 COMPLEXITY CHECKPOINTS

**MANDATORY Validation**:
- [ ] Role clarity (coordinator vs documentation)
- [ ] Section value (execution vs explanation)
- [ ] Transparency method (concise vs verbose)
- [ ] Line count (follow `standards/writing-standards.md`)

**PATTERNS**:
- ✅ **GOOD**: One-line reasoning, function-focused, usage examples, cross-references
- ⚠️ **WARNING**: Extensive examples, detailed criteria, concept explanations
- ❌ **BAD**: Documentation repository, theoretical frameworks, science education

**EMERGENCY** (≥180 lines): AUDIT → EXTRACT → REFERENCE → VALIDATE

### Standards
**LANGUAGE**: English only, action-oriented, technical precision, LLM optimized
**STRUCTURE**: Hierarchical organization, progressive detail, consistent formatting, reference integration

## 🚫 ANTI-BIAS ENFORCEMENT

### Content Creation Rules
- **NO Predetermined Categories**: Let patterns emerge from content
- **NO Assumption-Based Logic**: All logic must be evidence-based
- **NO Selective Information**: Present all relevant options equally
- **NO Hidden Preferences**: Transparent evaluation criteria

### Implementation Validation
- **Discovery-Based**: Use exploration tools for factual basis
- **Evidence-Required**: All recommendations backed by data
- **Option-Neutral**: Present alternatives without bias
- **Context-Driven**: Decisions based on specific situation analysis

## 🔗 CROSS-REFERENCE STANDARDS

### Internal References
**MANDATORY**: Reference related commands and standards
- **Standards**: Link to applicable writing standards and anti-bias rules
- **Commands**: Reference triggering and triggered commands
- **Context**: Connect to generated context files
- **Workflows**: Show position in overall system flows

### Reference Format
```markdown
**See Also**: 
- `/[related-command]` - [Brief description]
- `standards/[standard-file].md` - [Purpose]
- `context/[context-type]/` - [Generated content]
```

## ⚡ CREATION WORKFLOW

### Template Usage Process
1. **COPY**: Use this template as base structure
2. **REPLACE**: Substitute all bracketed variables
3. **CUSTOMIZE**: Add command-specific implementation details
4. **VALIDATE**: Ensure all required sections completed
5. **INTEGRATE**: Add cross-references to existing commands
6. **TEST**: Verify command functions as specified

### Quality Checklist
- [ ] All bracketed variables replaced
- [ ] **File Size Check**: Follow limits in `standards/writing-standards.md`
- [ ] **Feature Creep Check**: Role clarity maintained (coordinator vs documentation)
- [ ] **Simplicity Check**: Concise reasoning vs verbose criteria
- [ ] **Value Check**: Each section enables execution vs explains concepts
- [ ] Clear triggers defined
- [ ] Integration points specified
- [ ] Anti-bias compliance confirmed
- [ ] Cross-references added
- [ ] Implementation testable

---

**CRITICAL**: This template MUST be used for all new commands to ensure system consistency and autocontained functionality.