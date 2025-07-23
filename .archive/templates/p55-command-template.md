# P55-Integrated Command Template

**Purpose**: Command template with built-in P55/P56 compliance and script execution protocols.

**Authority**: Template for commands requiring integrated P55 script execution and P56 transparency protocols.

---

## Command: `/command-name` (aliases: `/alias1`, `/alias2`)

**Purpose**: Brief description of what this command does

**Philosophy**: "Core philosophy or meta-principle"

---

## 🔧 P55 Script Execution Protocol

**MANDATORY**: This command automatically executes:

```bash
# Pre-execution validation (if needed)
./scripts/validation/validate-system-integrity.sh

# Core execution scripts
./scripts/category/specific-script.sh --parameter
./scripts/category/another-script.sh --context={{COMMAND_NAME}}

# Post-execution validation/monitoring (if needed)
./scripts/compliance/enhanced-p55-p56-monitor.sh --command={{COMMAND_NAME}}
```

**Execution Protocol**:
1. **Pre-execution**: [Description of pre-execution steps]
2. **Core Execution**: [Description of main execution steps]  
3. **Post-execution**: [Description of validation/monitoring steps]
4. **Reporting**: [Description of reporting requirements]

---

## 🔍 P56 Execution Transparency

**I'm going to**:
1. [Action 1 description]
2. [Action 2 description]
3. [Action 3 description]
4. [Action 4 description]

**Status Updates**:
- 🔄 **Starting**: [Command name] execution initiated
- 📊 **Progress**: [Description of progress indicators]
- ✅ **Complete**: [Description of completion status]
- 📈 **Metrics**: [Description of metrics updated]

---

## 🎯 COMMAND DEFINITION

### **Purpose**
[Detailed purpose description with quantifiable outcomes]

**Observable Outcomes**:
- **[Metric 1]**: [≥/≤][value] [unit] [description]
- **[Metric 2]**: [≥/≤][value] [unit] [description]
- **[Metric 3]**: [≥/≤][value] [unit] [description]

### **Complexity**: X.X/X.X (Validated via mathematical analysis)
### **Context Required**: [Context requirements with percentage completeness]
### **Execution Time**: [Expected execution time with phase breakdown]

**Success Criteria**:
- **[Criterion 1]**: [≥/≤][value] [metric] [description]
- **[Criterion 2]**: [≥/≤][value] [metric] [description]
- **[Criterion 3]**: [requirement] with [validation method]

---

## ⚡ ACTIVATION PROTOCOL

### **Input Format**
```markdown
/command-name [required_param] [optional_param?] [optional_param2?]
```

### **Auto-Activation Triggers** (if applicable)
This command EXECUTES automatically when [conditions] with [≥/≤][value] [metric] and [requirements].

**Verification Protocol**:
- **[Verification 1]**: [≥/≤][value] [metric] [description]
- **[Verification 2]**: [requirement] with [validation]
- **[Verification 3]**: [standard] with [compliance method]

---

## 🔧 COMMAND FUNCTIONALITY

### **[Function Category 1]**
[Description of core functionality with specific implementation details]

### **[Function Category 2]**
[Description of additional functionality with integration points]

### **[Function Category 3]**
[Description of specialized features with validation requirements]

---

## 🛡️ P55/P56 COMPLIANCE FRAMEWORK

**Inherits from**: [Universal P55/P56 Compliance](./p55-p56-compliance-template.md)

**Command-Specific Implementation**:
[Description of how this command implements P55/P56 requirements]

### **Tool Call Execution Protocol**
**MANDATORY**: When this command executes ANY Tool Call, the system MUST:

1. **Display visual announcement** before execution
2. **Execute real tool calls** (never simulate)
3. **Capture actual results** from tool execution
4. **Provide complete transparency** of all operations
5. **Maintain evidence trail** for compliance verification

### **Behavioral Requirements**
- **ALWAYS** execute real tool calls (never simulate)
- **DISPLAY** visual announcements before each tool execution
- **CAPTURE** actual results from tool execution
- **PROVIDE** complete transparency of all operations
- **MAINTAIN** evidence trail for compliance verification

---

## 🔗 USAGE CRITERIA

### **Automatic Activation**
- [Use case 1 with conditions and metrics]
- [Use case 2 with triggers and thresholds]
- [Use case 3 with requirements and validation]

### **Manual Activation**
- [Manual use case 1]
- [Manual use case 2]
- [Manual use case 3]

---

## 🎯 SUCCESS METRICS

### **P55 Compliance Metrics**
- **Script Execution**: ≥95% success rate
- **Tool Call Execution**: 100% real execution (0% simulation)
- **Mathematical Precision**: ≥4 decimal places accuracy

### **P56 Transparency Metrics**
- **Execution Visibility**: ≥90% transparency
- **Progress Updates**: Real-time status reporting
- **Result Documentation**: Complete evidence trails

### **Command-Specific Metrics**
- **[Metric Category 1]**: [≥/≤][value] [unit] ([target]: [≥/≤][target_value])
- **[Metric Category 2]**: [≥/≤][value] [unit] ([target]: [≥/≤][target_value])

---

## 🔧 IMPLEMENTATION NOTES

### **P55 Requirements**
- **MANDATORY**: Commands must execute their scripts
- **REQUIRED**: Script paths must be absolute
- **CRITICAL**: Error handling for script failures
- **REQUIRED**: Success/failure reporting

### **P56 Requirements**
- **MANDATORY**: Announce intentions before execution
- **REQUIRED**: Provide progress updates
- **CRITICAL**: Report final status
- **REQUIRED**: Explain any failures

### **Integration Requirements**
- **Cross-Command**: Seamless integration with other commands
- **Error Handling**: Automatic error protocol activation
- **Performance**: Maintain ≤2.0s execution time
- **Documentation**: Real-time documentation updates

---

## 📝 RELATED COMMANDS

- [Related command 1] - [Relationship description]
- [Related command 2] - [Relationship description]
- [Related command 3] - [Relationship description]

---

## 🔗 CROSS-REFERENCES

- [P55/P56 Compliance Template](./p55-p56-compliance-template.md) - Universal compliance standards
- [Command Structure Template](./command-structure-template.md) - Standard command organization
- [Enforcement Template](./enforcement-template.md) - Enforcement patterns and protocols

---

## 📊 TEMPLATE CUSTOMIZATION

### **Variables to Replace**
- `[command-name]`: Actual command name
- `[Command name]`: Human-readable command name
- `[Description/Action/Metric]`: Command-specific content
- `{{COMMAND_NAME}}`: Script parameter placeholder

### **Sections to Customize**
- **Script paths**: Update to actual script locations
- **Metrics**: Replace with command-specific measurements
- **Functions**: Describe actual command functionality
- **Parameters**: Define actual command parameters

### **Optional Sections**
- Remove sections not applicable to the command
- Add command-specific sections as needed
- Customize compliance requirements per command type

---

**Template Type**: P55-integrated command template
**Used By**: Commands requiring P55 script execution and P56 transparency
**Integration**: Built-in P55/P56 compliance protocols
**Authority**: Template for P55-compliant command development