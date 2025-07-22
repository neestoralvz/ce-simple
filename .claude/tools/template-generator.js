/**
 * Template Generation System - Quick Command Creation
 * 
 * Generates context-aware templates for rapid command creation with
 * intelligent pre-filling based on user patterns and command context.
 */

class TemplateGenerator {
  constructor() {
    this.templateComplexities = {
      SIMPLE: 'simple',
      MEDIUM: 'medium', 
      COMPLEX: 'complex',
      ADVANCED: 'advanced'
    };
    
    this.commandCategories = {
      WORKFLOW: 'workflow',
      ANALYSIS: 'analysis',
      DOCUMENTATION: 'documentation',
      MAINTENANCE: 'maintenance',
      INTEGRATION: 'integration',
      VALIDATION: 'validation'
    };

    this.standardEmojis = {
      workflow: '⟳',
      analysis: '🔍', 
      documentation: '📝',
      maintenance: '🔧',
      integration: '🔗',
      validation: '✅',
      purpose: '🎯',
      usage: '🚀',
      implementation: '🔧',
      triggers: '⚡',
      seeAlso: '🔗'
    };
  }

  /**
   * Generate template based on command name and complexity
   */
  generateTemplate(commandName, complexity = 'medium', category = null) {
    const templateData = this.analyzeCommandName(commandName);
    const detectedCategory = category || this.detectCategory(commandName, templateData);
    
    const generator = this.getTemplateGenerator(complexity);
    return generator(commandName, templateData, detectedCategory);
  }

  /**
   * Generate context-aware template based on user patterns
   */
  generateContextualTemplate(commandName, userPatterns, relatedCommands = []) {
    const templateData = this.analyzeCommandName(commandName);
    const complexity = this.determineComplexityFromPatterns(userPatterns);
    const category = this.detectCategory(commandName, templateData);
    
    // Generate base template
    const baseTemplate = this.generateTemplate(commandName, complexity, category);
    
    // Apply user pattern adaptations
    const adaptedTemplate = this.applyUserPatterns(baseTemplate, userPatterns);
    
    // Integrate related command context
    const contextualTemplate = this.integrateRelatedCommands(adaptedTemplate, relatedCommands);
    
    return {
      template: contextualTemplate,
      metadata: {
        commandName,
        complexity,
        category,
        userPatterns,
        relatedCommands: relatedCommands.map(cmd => cmd.name)
      }
    };
  }

  /**
   * Analyze command name to extract context
   */
  analyzeCommandName(commandName) {
    const analysis = {
      baseAction: this.extractAction(commandName),
      subject: this.extractSubject(commandName),
      scope: this.extractScope(commandName),
      suggestedDescription: this.generateDescription(commandName),
      suggestedKeywords: this.generateKeywords(commandName),
      suggestedTodos: this.generateBasicTodos(commandName)
    };

    return analysis;
  }

  /**
   * Extract action verb from command name
   */
  extractAction(commandName) {
    const actionWords = ['create', 'generate', 'analyze', 'validate', 'optimize', 'execute', 'process', 'maintain', 'integrate', 'explore', 'capture', 'think'];
    
    const found = actionWords.find(action => 
      commandName.toLowerCase().includes(action)
    );
    
    return found || 'execute';
  }

  /**
   * Extract subject from command name
   */
  extractSubject(commandName) {
    const subjects = ['command', 'doc', 'file', 'system', 'data', 'code', 'pattern', 'workflow', 'process'];
    
    const found = subjects.find(subject => 
      commandName.toLowerCase().includes(subject)
    );
    
    return found || commandName.split('-')[1] || 'system';
  }

  /**
   * Extract scope indicators
   */
  extractScope(commandName) {
    if (commandName.includes('global') || commandName.includes('system')) return 'system-wide';
    if (commandName.includes('local') || commandName.includes('file')) return 'local';
    if (commandName.includes('project')) return 'project';
    return 'context-dependent';
  }

  /**
   * Generate description from command name
   */
  generateDescription(commandName) {
    const words = commandName.split('-');
    const action = this.extractAction(commandName);
    const subject = this.extractSubject(commandName);
    
    const descriptions = {
      create: 'Creation and generation workflow',
      analyze: 'Analysis and assessment system',
      validate: 'Validation and verification process',
      optimize: 'Optimization and improvement workflow',
      explore: 'Discovery and exploration system',
      maintain: 'Maintenance and upkeep process',
      process: 'Processing and transformation workflow',
      integrate: 'Integration and coordination system'
    };
    
    return descriptions[action] || `${action.charAt(0).toUpperCase() + action.slice(1)} ${subject} workflow`;
  }

  /**
   * Generate keywords from command name
   */
  generateKeywords(commandName) {
    const baseKeywords = commandName.split('-');
    const action = this.extractAction(commandName);
    const subject = this.extractSubject(commandName);
    
    const additionalKeywords = {
      create: ['generate', 'build', 'construct'],
      analyze: ['examine', 'assess', 'evaluate'],
      validate: ['verify', 'check', 'confirm'],
      optimize: ['improve', 'enhance', 'refine'],
      explore: ['discover', 'investigate', 'search'],
      maintain: ['update', 'repair', 'sustain']
    };
    
    return [...baseKeywords, action, subject, ...(additionalKeywords[action] || [])].slice(0, 5);
  }

  /**
   * Generate basic todos based on command name
   */
  generateBasicTodos(commandName) {
    const action = this.extractAction(commandName);
    const subject = this.extractSubject(commandName);
    const prefix = commandName.split('-')[0] || 'cmd';
    
    const todoTemplates = {
      create: [
        `🏗️ SETUP: Initialize ${subject} creation environment and validation`,
        `⚡ GENERATE: Execute ${subject} generation with quality checks`,
        `✅ VALIDATE: Verify generated ${subject} meets requirements`
      ],
      analyze: [
        `🔍 DISCOVERY: Scan and identify ${subject} patterns and structure`, 
        `📊 ASSESSMENT: Evaluate ${subject} characteristics and metrics`,
        `📝 DOCUMENTATION: Capture analysis findings and recommendations`
      ],
      validate: [
        `🔍 INSPECTION: Execute comprehensive ${subject} validation checks`,
        `📊 SCORING: Calculate validation metrics and quality scores`,
        `⚠️ REPORTING: Generate validation report with recommendations`
      ],
      optimize: [
        `📊 BASELINE: Establish current ${subject} performance metrics`,
        `⚡ OPTIMIZATION: Apply improvement strategies and techniques`,
        `✅ VERIFICATION: Validate optimization results and benefits`
      ],
      explore: [
        `🗺️ MAPPING: Discover and map ${subject} landscape and structure`,
        `🔍 ANALYSIS: Identify patterns and relationships in ${subject}`,
        `📋 SYNTHESIS: Consolidate findings into actionable insights`
      ],
      maintain: [
        `🔍 ASSESSMENT: Evaluate current ${subject} health and status`,
        `🔧 MAINTENANCE: Execute necessary ${subject} updates and repairs`,
        `✅ VALIDATION: Verify maintenance results and system stability`
      ]
    };

    const baseTodos = todoTemplates[action] || [
      `🏗️ SETUP: Initialize ${commandName} execution environment`,
      `⚡ EXECUTE: Run ${commandName} primary workflow`,
      `✅ VALIDATE: Verify ${commandName} completion and results`
    ];

    return baseTodos.map((todo, index) => ({
      content: todo,
      status: 'pending',
      priority: index === 0 ? 'high' : 'medium',
      id: `${prefix}-${action}-${index + 1}`
    }));
  }

  /**
   * Detect command category from name and context
   */
  detectCategory(commandName, templateData) {
    const categoryKeywords = {
      [this.commandCategories.WORKFLOW]: ['workflow', 'process', 'orchestrate', 'coordinate'],
      [this.commandCategories.ANALYSIS]: ['analyze', 'assess', 'evaluate', 'examine', 'think'],
      [this.commandCategories.DOCUMENTATION]: ['docs', 'document', 'generate', 'write'],
      [this.commandCategories.MAINTENANCE]: ['maintain', 'fix', 'repair', 'update', 'optimize'],
      [this.commandCategories.INTEGRATION]: ['integrate', 'connect', 'link', 'merge'],
      [this.commandCategories.VALIDATION]: ['validate', 'verify', 'check', 'test', 'audit']
    };

    for (const [category, keywords] of Object.entries(categoryKeywords)) {
      if (keywords.some(keyword => 
        commandName.toLowerCase().includes(keyword) || 
        templateData.baseAction.includes(keyword)
      )) {
        return category;
      }
    }

    return this.commandCategories.WORKFLOW; // Default
  }

  /**
   * Get template generator function based on complexity
   */
  getTemplateGenerator(complexity) {
    const generators = {
      [this.templateComplexities.SIMPLE]: this.generateSimpleTemplate.bind(this),
      [this.templateComplexities.MEDIUM]: this.generateMediumTemplate.bind(this),
      [this.templateComplexities.COMPLEX]: this.generateComplexTemplate.bind(this),
      [this.templateComplexities.ADVANCED]: this.generateAdvancedTemplate.bind(this)
    };

    return generators[complexity] || generators[this.templateComplexities.MEDIUM];
  }

  /**
   * Generate simple template (minimal structure)
   */
  generateSimpleTemplate(commandName, templateData, category) {
    return `# ${this.formatCommandName(commandName)} - ${templateData.suggestedDescription}

## 🎯 Purpose
${this.generatePurposeText(templateData, category)}

## 🚀 Usage
Execute: \`/${commandName} [parameters]\`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at command initialization**:

\`\`\`javascript
TodoWrite([
${this.formatTodos(templateData.suggestedTodos.slice(0, 3))}
])
\`\`\`

### ${this.getProtocolSectionName(category)}
${this.generateBasicImplementation(templateData, category)}

## ⚡ Triggers

### Input Triggers
**Context**: ${this.generateInputContext(templateData, category)}
**Keywords**: ${templateData.suggestedKeywords.join(', ')}

### Output Triggers
**Chain**: ${this.generateOutputChain(templateData, category)}

## 🔗 See Also
${this.generateSeeAlso(templateData, category)}

---

**CRITICAL**: ${this.generateCriticalNote(templateData, category)}`;
  }

  /**
   * Generate medium template (standard structure)
   */
  generateMediumTemplate(commandName, templateData, category) {
    return `# ${this.formatCommandName(commandName)} - ${templateData.suggestedDescription}

## 🎯 Purpose
${this.generatePurposeText(templateData, category)}

## 🚀 Usage
Execute: \`/${commandName} [parameters]\`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at command initialization**:

\`\`\`javascript
TodoWrite([
${this.formatTodos(templateData.suggestedTodos)}
])
\`\`\`

**Progressive Todo Management**: Mark todos as completed in real-time as actions are executed for complete user transparency

### Structural Enforcement Protocol
**AUTO-EXECUTION**:
${this.generateStructuralProtocol(category)}

### ${this.getProtocolSectionName(category)}
${this.generateMediumImplementation(templateData, category)}

### Integration Protocol
${this.generateIntegrationProtocol(templateData, category)}

## ⚡ Triggers

### Input Triggers
**Context**: ${this.generateInputContext(templateData, category)}
**Previous**: ${this.generatePreviousContext(templateData)}
**Keywords**: ${templateData.suggestedKeywords.join(', ')}

### Output Triggers
**Success**: ${this.generateSuccessContext(templateData)}
**Chain**: ${this.generateOutputChain(templateData, category)}

### Success Patterns
${this.generateSuccessPatterns(templateData, category)}

## 🔗 See Also

### Implementation References
${this.generateImplementationReferences(commandName, templateData)}

### Related Commands
${this.generateRelatedCommands(templateData, category)}

---

**CRITICAL**: ${this.generateCriticalNote(templateData, category)}`;
  }

  /**
   * Generate complex template (full structure with advanced features)
   */
  generateComplexTemplate(commandName, templateData, category) {
    return `# ${this.formatCommandName(commandName)} - ${templateData.suggestedDescription}

## 🎯 Purpose
${this.generatePurposeText(templateData, category)} with advanced ${category} capabilities and intelligent optimization.

## 🚀 Usage
Execute: \`/${commandName} [parameters] [complexity-level] [options]\`

## 🔧 Implementation

### Enhanced Behavioral Reinforcement Protocol
**MANDATORY at command initialization**:

\`\`\`javascript
TodoWrite([
${this.formatTodos(templateData.suggestedTodos)},
  {"content": "🔧 OPTIMIZATION: Apply advanced ${category} optimization techniques", "status": "pending", "priority": "medium", "id": "${commandName.split('-')[0]}-opt-1"},
  {"content": "📊 METRICS: Collect performance and quality metrics", "status": "pending", "priority": "low", "id": "${commandName.split('-')[0]}-metrics-1"}
])
\`\`\`

**Intelligence-Driven Todos**: Add conditional todos based on complexity assessment and runtime analysis

### Structural Enforcement Protocol
**PRE-EXECUTION AUTOMATION**:
${this.generateAdvancedStructuralProtocol(category)}

### Advanced ${this.getProtocolSectionName(category)}
${this.generateAdvancedImplementation(templateData, category)}

### Intelligent Orchestration
${this.generateIntelligentOrchestration(templateData, category)}

### Auto-Activation Framework
${this.generateAutoActivation(templateData, category)}

### Load Management System
${this.generateLoadManagement(templateData)}

### Quality Assurance Protocol
${this.generateQualityAssurance(templateData, category)}

## ⚡ Triggers

### Input Triggers
**Context**: ${this.generateAdvancedInputContext(templateData, category)}
**Auto-Trigger**: ${this.generateAutoTriggerContext(templateData)}
**Previous**: ${this.generatePreviousContext(templateData)}
**Keywords**: ${templateData.suggestedKeywords.join(', ')}, advanced, optimization, intelligence

### Output Triggers
**Success**: ${this.generateSuccessContext(templateData)} → Advanced analysis pipeline
**Integration**: ${this.generateIntegrationContext(templateData)}
**Chain**: ${this.generateAdvancedOutputChain(templateData, category)}

### Success Patterns
${this.generateAdvancedSuccessPatterns(templateData, category)}

### Automatic Learning Integration
${this.generateLearningIntegration(templateData)}

## 🔗 See Also

### Implementation References
${this.generateAdvancedImplementationReferences(commandName, templateData)}

### Related Commands
${this.generateAdvancedRelatedCommands(templateData, category)}

### System Integration
${this.generateSystemIntegration(commandName)}

---

**CRITICAL**: ${this.generateAdvancedCriticalNote(templateData, category)}`;
  }

  /**
   * Generate advanced template (cutting-edge features)
   */
  generateAdvancedTemplate(commandName, templateData, category) {
    // Advanced template would include AI-driven features, predictive analytics, etc.
    // Implementation would be similar to complex but with additional advanced features
    return this.generateComplexTemplate(commandName, templateData, category)
      .replace('Enhanced Behavioral', 'AI-Enhanced Behavioral')
      .replace('Advanced ', 'Next-Generation ')
      .replace('Intelligent Orchestration', 'AI-Driven Orchestration with Predictive Analytics');
  }

  /**
   * Apply user patterns to adapt template
   */
  applyUserPatterns(template, userPatterns) {
    let adaptedTemplate = template;

    // Length adaptation
    if (userPatterns.preferredLength === 'concise') {
      adaptedTemplate = this.condensateTemplate(adaptedTemplate);
    } else if (userPatterns.preferredLength === 'detailed') {
      adaptedTemplate = this.expandTemplate(adaptedTemplate);
    }

    // Structure adaptations
    if (userPatterns.commonStructures.usesSubsections) {
      adaptedTemplate = this.addSubsections(adaptedTemplate);
    }

    if (userPatterns.commonStructures.prefersCodeBlocks) {
      adaptedTemplate = this.enhanceCodeBlocks(adaptedTemplate);
    }

    // Vocabulary adaptations
    if (userPatterns.vocabularyStyle.formalTone > 3) {
      adaptedTemplate = this.formalizeTone(adaptedTemplate);
    }

    return adaptedTemplate;
  }

  /**
   * Integrate related commands into template
   */
  integrateRelatedCommands(template, relatedCommands) {
    if (relatedCommands.length === 0) return template;

    // Add related command context to various sections
    const relatedIntegration = relatedCommands.map(cmd => 
      `- Execute \`/${cmd.name}\` for ${cmd.purpose || 'related functionality'}`
    ).join('\n');

    return template.replace(
      '### Related Commands',
      `### Related Commands\n${relatedIntegration}\n\n### Additional Integration`
    );
  }

  // Helper methods for template generation
  formatCommandName(commandName) {
    return commandName.split('-').map(word => 
      word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
  }

  formatTodos(todos) {
    return todos.map(todo => 
      `  ${JSON.stringify(todo)}`
    ).join(',\n');
  }

  generatePurposeText(templateData, category) {
    const purposes = {
      workflow: `Orchestrate ${templateData.subject} ${templateData.baseAction} with automated coordination`,
      analysis: `Systematically ${templateData.baseAction} ${templateData.subject} patterns and characteristics`,
      documentation: `Generate comprehensive ${templateData.subject} documentation with quality assurance`,
      maintenance: `Maintain and optimize ${templateData.subject} systems with preventive protocols`,
      integration: `Integrate ${templateData.subject} components with seamless coordination`,
      validation: `Validate ${templateData.subject} integrity with comprehensive verification`
    };

    return purposes[category] || `Execute ${templateData.baseAction} workflow for ${templateData.subject} management`;
  }

  getProtocolSectionName(category) {
    const names = {
      workflow: 'Workflow Orchestration Protocol',
      analysis: 'Analysis Framework Protocol',
      documentation: 'Documentation Generation Protocol',
      maintenance: 'Maintenance Execution Protocol',
      integration: 'Integration Coordination Protocol',
      validation: 'Validation Framework Protocol'
    };

    return names[category] || 'Execution Protocol';
  }

  generateBasicImplementation(templateData, category) {
    return `**${templateData.baseAction.toUpperCase()}**: Primary ${category} workflow execution
**VALIDATION**: Verify ${templateData.subject} integrity and compliance
**COMPLETION**: Ensure workflow completion with quality assurance`;
  }

  generateMediumImplementation(templateData, category) {
    const implementations = {
      workflow: `**ORCHESTRATION**: Coordinate ${templateData.subject} workflow components
**EXECUTION**: Deploy parallel/sequential processing as needed
**MONITORING**: Track progress with transparent notifications
**OPTIMIZATION**: Apply efficiency improvements during execution`,

      analysis: `**DISCOVERY**: Systematic ${templateData.subject} pattern identification
**ASSESSMENT**: Comprehensive characteristic evaluation
**SYNTHESIS**: Consolidate findings into actionable insights
**VALIDATION**: Cross-verify analysis results`,

      documentation: `**GENERATION**: Create comprehensive ${templateData.subject} documentation
**OPTIMIZATION**: Apply writing standards and clarity principles  
**VALIDATION**: Verify completeness and accuracy
**INTEGRATION**: Cross-reference with existing documentation`,

      maintenance: `**ASSESSMENT**: Evaluate current ${templateData.subject} status
**EXECUTION**: Apply necessary maintenance procedures
**VERIFICATION**: Validate maintenance results
**PREVENTION**: Implement preventive measures`,

      integration: `**MAPPING**: Identify integration points and dependencies
**COORDINATION**: Establish connection protocols
**EXECUTION**: Deploy integration procedures
**VALIDATION**: Verify integration integrity`,

      validation: `**INSPECTION**: Comprehensive ${templateData.subject} validation
**SCORING**: Calculate quality and compliance metrics
**REPORTING**: Generate detailed validation results
**RECOMMENDATIONS**: Provide improvement suggestions`
    };

    return implementations[category] || this.generateBasicImplementation(templateData, category);
  }

  // Additional helper methods would be implemented for other template components...
  // (generateStructuralProtocol, generateInputContext, etc.)

  generateStructuralProtocol(category) {
    return `1. 🏗️ **VALIDATE**: Structure verification and compliance check
2. 🔍 **ANALYZE**: ${category} context and requirement assessment
3. ⚡ **CORRECT**: Auto-fix structural violations and inconsistencies
4. ✅ **VERIFY**: Confirm corrections and readiness for execution`;
  }

  generateInputContext(templateData, category) {
    return `${templateData.scope} ${templateData.subject} ${templateData.baseAction} required following ${category} protocol initiation`;
  }

  generateOutputChain(templateData, category) {
    return `${templateData.baseAction} → validation → ${category} completion`;
  }

  generateSeeAlso(templateData, category) {
    return `- \`../docs/implementation/${templateData.baseAction}-implementation.md\` - Detailed ${category} framework
- \`../docs/${category}/\` - Category-specific protocols and standards`;
  }

  generateCriticalNote(templateData, category) {
    return `This command executes ${templateData.subject} ${templateData.baseAction} with ${category} optimization and quality assurance protocols.`;
  }

  // ... (Additional helper methods would be implemented for advanced features)

  /**
   * Determine complexity from user patterns
   */
  determineComplexityFromPatterns(userPatterns) {
    let complexityScore = 0;

    // Base complexity from length preference
    if (userPatterns.preferredLength === 'detailed') complexityScore += 2;
    if (userPatterns.preferredLength === 'moderate') complexityScore += 1;

    // Complexity from structure usage
    if (userPatterns.commonStructures.usesSubsections) complexityScore += 1;
    if (userPatterns.commonStructures.prefersCodeBlocks) complexityScore += 1;

    // Complexity from vocabulary
    if (userPatterns.vocabularyStyle.technicalDepth > 5) complexityScore += 1;
    if (userPatterns.vocabularyStyle.formalTone > 3) complexityScore += 1;

    // Map score to complexity
    if (complexityScore <= 2) return this.templateComplexities.SIMPLE;
    if (complexityScore <= 4) return this.templateComplexities.MEDIUM;
    if (complexityScore <= 6) return this.templateComplexities.COMPLEX;
    return this.templateComplexities.ADVANCED;
  }

  /**
   * Condensate template for concise users
   */
  condensateTemplate(template) {
    return template
      .replace(/### [^\n]+\n([^#]*)/g, (match, content) => {
        // Keep essential content, remove verbose explanations
        const essential = content.split('\n').filter(line => 
          line.includes('**') || line.includes('Execute') || line.includes('TodoWrite')
        ).join('\n');
        return match.replace(content, essential);
      })
      .replace(/\*\*([^*]+)\*\*:\s*([^\n]+)/g, '**$1**: $2') // Condense explanations
      .replace(/\n{3,}/g, '\n\n'); // Reduce white space
  }

  /**
   * Expand template for detailed users
   */
  expandTemplate(template) {
    // Add more detailed explanations and examples
    return template
      .replace('## 🔧 Implementation', '## 🔧 Implementation\n\n### Overview\nComprehensive implementation framework with detailed protocols.\n')
      .replace('TodoWrite([', 'TodoWrite([\n  // Comprehensive behavioral reinforcement with detailed tracking\n  // Each todo represents a critical workflow component\n  ')
      .replace('## ⚡ Triggers', '### Execution Context\nDetailed trigger analysis and workflow integration patterns.\n\n## ⚡ Triggers');
  }

  /**
   * Add subsections to template
   */
  addSubsections(template) {
    return template.replace(
      /## 🔧 Implementation\n\n([\s\S]*?)(?=## )/,
      (match, content) => {
        const sections = content.split('### ');
        const enhancedSections = sections.map(section => {
          if (section.includes('Protocol')) {
            return section + '\n\n#### Execution Steps\n[Detailed implementation steps]\n\n#### Quality Assurance\n[Validation and verification protocols]\n';
          }
          return section;
        });
        return `## 🔧 Implementation\n\n${enhancedSections.join('### ')}`;
      }
    );
  }

  /**
   * Enhance code blocks in template
   */
  enhanceCodeBlocks(template) {
    return template.replace(
      /```javascript\nTodoWrite\(\[([\s\S]*?)\]\)\n```/,
      '```javascript\n// Enhanced TodoWrite with comprehensive tracking\n// Each todo includes execution context and validation criteria\nTodoWrite([$1])\n\n// Example usage:\n// - Monitor todo completion in real-time\n// - Add conditional todos based on execution results\n// - Integrate with workflow notification system\n```'
    );
  }

  /**
   * Formalize tone of template
   */
  formalizeTone(template) {
    return template
      .replace(/Execute:/g, 'Formal Execution Protocol:')
      .replace(/\*\*([A-Z]+)\*\*:/g, '**$1 Requirement**:')
      .replace(/workflow/gi, 'systematic process')
      .replace(/check/gi, 'verification procedure');
  }
}

module.exports = TemplateGenerator;