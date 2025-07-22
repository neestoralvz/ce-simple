# Command Template Enforcer - Strict Validation System

**Last Updated: 2025-07-22**

## 🚨 SYSTEM OVERVIEW

Comprehensive command standardization system with **STRICT BLOCKING VALIDATION**, intelligent auto-correction, and creative decision transparency for efficient frequent command creation.

## 🏗️ CORE COMPONENTS

### 1. STRICT COMMAND TEMPLATE SYSTEM

#### Mandatory Structure Template
```markdown
# [Command Name] - [Brief Description]

## 🎯 Purpose
[Single line objective - MANDATORY]

## 🚀 Usage
Execute: `/command-name [parameters]` - MANDATORY format

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at command initialization**:

```javascript
TodoWrite([
  {"content": "[ACTION]: [Description]", "status": "pending", "priority": "high", "id": "[prefix-action-1]"},
  // Minimum 3 todos required, maximum 7 todos allowed
])
```

### [Core Protocol Section - MANDATORY]
[Implementation details - MANDATORY minimum 50 words]

## ⚡ Triggers

### Input Triggers
**Context**: [When to use - MANDATORY]
**Keywords**: [3-5 keywords - MANDATORY]

### Output Triggers
**Chain**: [Next command flow - MANDATORY]

## 🔗 See Also
[Minimum 2 references - MANDATORY]

---

**CRITICAL**: [Command-specific critical note - MANDATORY]
```

#### Template Validation Rules
- **BLOCKING RULE 1**: All 8 sections must be present
- **BLOCKING RULE 2**: TodoWrite block required with 3-7 todos
- **BLOCKING RULE 3**: Purpose must be single sentence ≤100 characters
- **BLOCKING RULE 4**: Implementation must be ≥50 words
- **BLOCKING RULE 5**: File must be ≤200 lines
- **BLOCKING RULE 6**: Must include date in header when referencing system
- **BLOCKING RULE 7**: All emoji symbols must follow standard (🎯📊🔧⚡🔗)

### 2. INTELLIGENT AUTO-CORRECTION ENGINE

#### Formatting Auto-Fixes
```javascript
// Auto-correction algorithms
const autoCorrections = {
  // 1. Header standardization
  fixHeaders: (content) => {
    return content.replace(/^#\s*([^-]+)\s*-?\s*(.*)$/gm, '# $1 - $2');
  },
  
  // 2. Emoji standardization  
  fixEmojis: (content) => {
    const emojiMap = {
      'purpose': '🎯', 'usage': '🚀', 'implementation': '🔧', 
      'triggers': '⚡', 'see also': '🔗', 'data': '📊'
    };
    return content.replace(/##\s*([^🎯🚀🔧⚡🔗📊])(.+)/g, (match, emoji, text) => {
      const key = text.toLowerCase().trim();
      return emojiMap[key] ? `## ${emojiMap[key]} ${text}` : match;
    });
  },
  
  // 3. TodoWrite format standardization
  fixTodoWrite: (content) => {
    // Ensure proper TodoWrite structure with required fields
    return content.replace(/TodoWrite\(\[(.*?)\]\)/gs, (match, todos) => {
      // Parse and fix todo structure
      const todoPattern = /"content":\s*"([^"]+)",\s*"status":\s*"([^"]+)",\s*"priority":\s*"([^"]+)",\s*"id":\s*"([^"]+)"/g;
      return `TodoWrite([${todos}])`;
    });
  },
  
  // 4. Line limit optimization
  optimizeLength: (content) => {
    const lines = content.split('\n');
    if (lines.length > 200) {
      // Compress implementation section while preserving critical info
      return compressImplementation(content);
    }
    return content;
  },
  
  // 5. Cross-reference link validation
  fixCrossReferences: (content) => {
    // Validate and correct internal links
    return content.replace(/\.\.\/(.*?)\.md/g, (match, path) => {
      if (fileExists(path)) return match;
      return findCorrectPath(path) || `[LINK_ERROR: ${path}]`;
    });
  }
};
```

### 3. VALIDATION ENGINE WITH BLOCKING

#### Pre-Creation Validation Pipeline
```javascript
const validationPipeline = {
  // PHASE 1: Structure validation (BLOCKING)
  validateStructure: (content) => {
    const required = [
      '# ',                           // Title
      '## 🎯 Purpose',                // Purpose section
      '## 🚀 Usage',                  // Usage section
      '## 🔧 Implementation',         // Implementation section
      'TodoWrite([',                  // TodoWrite block
      '## ⚡ Triggers',               // Triggers section
      '## 🔗 See Also',              // See Also section
      '**CRITICAL**:'                 // Critical note
    ];
    
    const missing = required.filter(req => !content.includes(req));
    if (missing.length > 0) {
      throw new ValidationError(`BLOCKING: Missing required sections: ${missing.join(', ')}`);
    }
  },
  
  // PHASE 2: Content validation (BLOCKING)
  validateContent: (content) => {
    const lines = content.split('\n');
    
    // Line limit check
    if (lines.length > 200) {
      throw new ValidationError(`BLOCKING: File exceeds 200 line limit (${lines.length} lines)`);
    }
    
    // Purpose length check
    const purposeMatch = content.match(/## 🎯 Purpose\n(.+)/);
    if (!purposeMatch || purposeMatch[1].length > 100) {
      throw new ValidationError('BLOCKING: Purpose must be single line ≤100 characters');
    }
    
    // TodoWrite validation
    const todoMatch = content.match(/TodoWrite\(\[(.*?)\]\)/s);
    if (!todoMatch) {
      throw new ValidationError('BLOCKING: TodoWrite block required');
    }
    
    const todoCount = (todoMatch[1].match(/"content":/g) || []).length;
    if (todoCount < 3 || todoCount > 7) {
      throw new ValidationError(`BLOCKING: TodoWrite must have 3-7 todos (found ${todoCount})`);
    }
  },
  
  // PHASE 3: Quality scoring (WARNING)
  calculateQuality: (content) => {
    let score = 100;
    
    // Deduct for missing optional elements
    if (!content.includes('### ')) score -= 10;  // No subsections
    if (!content.includes('**')) score -= 5;    // No emphasis
    if (!content.includes('```')) score -= 10;  // No code blocks
    
    // Quality thresholds
    if (score < 70) {
      throw new ValidationError(`BLOCKING: Quality score too low (${score}/100, minimum 70)`);
    }
    
    return score;
  }
};
```

#### Real-Time Validation Feedback
```javascript
const validationFeedback = {
  showErrors: (errors) => {
    console.log('🚨 VALIDATION ERRORS - Command creation BLOCKED:');
    errors.forEach((error, i) => {
      console.log(`${i+1}. ${error.message}`);
      console.log(`   Fix: ${error.suggestion}`);
    });
  },
  
  showWarnings: (warnings) => {
    console.log('⚠️ VALIDATION WARNINGS - Auto-correctable:');
    warnings.forEach(warning => {
      console.log(`- ${warning.message} → ${warning.correction}`);
    });
  }
};
```

### 4. CREATIVE DECISION TRANSPARENCY SYSTEM

#### Decision Logging Framework
```javascript
const decisionLogger = {
  logCreativeDecision: (decision) => {
    const logEntry = {
      timestamp: new Date().toISOString(),
      type: decision.type,        // 'structure_variation', 'content_enhancement', 'format_adaptation'
      rationale: decision.why,    // Explanation for variation
      standard: decision.from,    // What standard was adapted
      variation: decision.to,     // What variation was chosen
      impact: decision.impact     // Expected user benefit
    };
    
    appendToLog('/Users/nalve/ce-simple/.claude/tools/creative-decisions.json', logEntry);
  },
  
  explainToUser: (decision) => {
    return `
🎨 CREATIVE DECISION MADE:
Type: ${decision.type}
Rationale: ${decision.why}
Standard Template: ${decision.from}
Creative Variation: ${decision.to}
Benefit: ${decision.impact}
    `;
  }
};
```

#### Transparency Protocols
- **IMMEDIATE NOTIFICATION**: User informed of all creative decisions during command creation
- **DECISION AUDIT**: All variations logged with rationale
- **STANDARD REFERENCE**: Clear indication when deviating from template
- **BENEFIT EXPLANATION**: User impact justification required

### 5. TEMPLATE GENERATION SYSTEM

#### Quick Command Creation
```javascript
const templateGenerator = {
  generateTemplate: (commandName, complexity = 'medium') => {
    const templates = {
      simple: generateSimpleTemplate(commandName),
      medium: generateMediumTemplate(commandName), 
      complex: generateComplexTemplate(commandName)
    };
    
    return templates[complexity];
  },
  
  contextAwareGeneration: (commandName, relatedCommands, userPattern) => {
    // Analyze user's previous commands for pattern matching
    const userStyle = analyzeUserCommandPatterns(userPattern);
    
    // Generate template matching user's established patterns
    return generateContextualTemplate(commandName, userStyle, relatedCommands);
  }
};
```

#### Pre-filled Template Examples
```markdown
# [COMMAND_NAME] - [AUTO_DESCRIPTION]

## 🎯 Purpose
[Generated based on command name and context]

## 🚀 Usage
Execute: \`/[command-name] [auto-detected parameters]\`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at command initialization**:

\`\`\`javascript
TodoWrite([
  {"content": "🏗️ STRUCTURAL: [Auto-generated structural todo]", "status": "pending", "priority": "high", "id": "[prefix]-struct-1"},
  {"content": "⚡ EXECUTION: [Auto-generated execution todo]", "status": "pending", "priority": "high", "id": "[prefix]-exec-1"},  
  {"content": "✅ VALIDATION: [Auto-generated validation todo]", "status": "pending", "priority": "medium", "id": "[prefix]-valid-1"}
])
\`\`\`

### [Auto-Generated Protocol Section]
[Context-aware implementation details]

## ⚡ Triggers

### Input Triggers
**Context**: [Auto-generated context]
**Keywords**: [auto-generated, keywords, list]

### Output Triggers
**Chain**: [auto-generated workflow chain]

## 🔗 See Also
[Auto-generated cross-references based on system analysis]

---

**CRITICAL**: [Auto-generated critical note based on command type]
```

## 🚀 USER WORKFLOW FOR FREQUENT COMMAND CREATION

### 1. Rapid Command Initialization
```bash
# Command: Create new command with auto-validation
/create-command [command-name] [complexity-level]

# System Response:
🏗️ Template generated → Auto-validation → Quality check → Ready for editing
```

### 2. Real-Time Validation Loop
```
1. User starts editing → Real-time structure validation
2. Missing sections detected → Auto-suggestions provided  
3. Format inconsistencies → Auto-corrections applied
4. Quality threshold → Progress indicator updated
5. All validation passed → Command creation enabled
```

### 3. Creative Decision Integration
```
1. User adds unique content → System analyzes for standards compliance
2. Creative variations detected → User notification with rationale
3. Decision approval → Logged and applied
4. Template evolution → Standards updated for future use
```

### 4. Efficiency Optimizations
- **Template Caching**: Previously used patterns stored for quick access
- **Auto-Completion**: IntelliSense-style suggestions for common patterns
- **Batch Validation**: Multiple commands validated simultaneously
- **Pattern Learning**: System adapts to user preferences over time

## 🔧 IMPLEMENTATION SPECIFICATIONS

### File Structure
```
.claude/tools/
├── command-template-enforcer.md     # This file - Main system
├── validation-engine.js             # Core validation logic
├── auto-correction-engine.js        # Auto-fix algorithms  
├── template-generator.js            # Template creation system
├── decision-logger.js               # Creative decision tracking
├── creative-decisions.json          # Decision audit log
└── user-patterns.json              # User preference learning
```

### Integration Points
- **Command Creation**: Pre-creation validation pipeline
- **Command Editing**: Real-time validation feedback
- **System Evolution**: Pattern learning and template evolution
- **Quality Assurance**: Continuous monitoring and improvement

### Performance Metrics
- **Validation Speed**: ≤2 seconds for complete validation
- **Auto-Correction**: ≥95% accuracy for common issues
- **User Efficiency**: ≤60 seconds for simple command creation
- **Quality Score**: ≥85 average for all generated commands

---

**CRITICAL**: This system operates with ZERO TOLERANCE for validation failures. All commands must pass complete validation before creation is allowed. Creative variations require explicit user notification and rationale.