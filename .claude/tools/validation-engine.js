/**
 * Validation Engine - Strict Blocking Validation System
 * 
 * Comprehensive command validation with blocking capabilities and quality thresholds.
 * Prevents command creation until all validation rules pass.
 */

class ValidationEngine {
  constructor() {
    this.validationResults = [];
    this.blockingErrors = [];
    this.warnings = [];
    this.qualityThreshold = 70; // Minimum quality score
    this.maxLines = 200;
    this.maxPurposeLength = 100;
    this.requiredSections = [
      '# ',                           // Title
      '## 🎯 Purpose',                // Purpose section
      '## 🚀 Usage',                  // Usage section
      '## 🔧 Implementation',         // Implementation section
      'TodoWrite([',                  // TodoWrite block
      '## ⚡ Triggers',               // Triggers section
      '## 🔗 See Also',              // See Also section
      '**CRITICAL**:'                 // Critical note
    ];
    this.standardEmojis = ['🎯', '🚀', '🔧', '⚡', '🔗', '📊', '🚨', '⟳', '📋'];
  }

  /**
   * Main validation pipeline - BLOCKS creation on failure
   */
  validateCommand(content, filename) {
    this.resetValidation();
    
    // PHASE 1: Critical Structure Validation (BLOCKING)
    this.validateCriticalStructure(content);
    if (this.hasBlockingErrors()) {
      return this.createBlockedResult('Critical structure validation failed');
    }
    
    // PHASE 2: Content Validation (BLOCKING)
    this.validateContent(content);
    if (this.hasBlockingErrors()) {
      return this.createBlockedResult('Content validation failed');
    }
    
    // PHASE 3: TodoWrite Validation (BLOCKING)
    this.validateTodoWrite(content);
    if (this.hasBlockingErrors()) {
      return this.createBlockedResult('TodoWrite validation failed');
    }
    
    // PHASE 4: Quality Assessment (BLOCKING if below threshold)
    const qualityScore = this.calculateQualityScore(content);
    if (qualityScore < this.qualityThreshold) {
      this.addBlockingError('quality_threshold', 
        `Quality score ${qualityScore}/100 below minimum ${this.qualityThreshold}`,
        'Improve content quality, structure, and formatting');
      return this.createBlockedResult('Quality threshold not met');
    }
    
    // PHASE 5: Cross-Reference Validation (WARNING only)
    this.validateCrossReferences(content, filename);
    
    // PHASE 6: Format Validation (WARNING only)
    this.validateFormatting(content);
    
    return this.createSuccessResult(qualityScore);
  }

  /**
   * Reset validation state for new validation run
   */
  resetValidation() {
    this.validationResults = [];
    this.blockingErrors = [];
    this.warnings = [];
  }

  /**
   * BLOCKING: Validate critical document structure
   */
  validateCriticalStructure(content) {
    // Check all required sections exist
    const missingSections = this.requiredSections.filter(section => 
      !content.includes(section)
    );

    if (missingSections.length > 0) {
      this.addBlockingError('missing_sections', 
        `Missing required sections: ${missingSections.join(', ')}`,
        'Add all required sections using the standard template');
    }

    // Validate title format
    const titleMatch = content.match(/^#\s+(.+)/m);
    if (!titleMatch) {
      this.addBlockingError('invalid_title', 
        'Document must start with properly formatted title (# Name - Description)',
        'Use format: # CommandName - Brief Description');
    } else {
      const title = titleMatch[1];
      if (!title.includes(' - ')) {
        this.addBlockingError('title_format', 
          'Title must include description after dash (Name - Description)',
          'Add description: # CommandName - Brief Description');
      }
    }

    // Validate section order
    this.validateSectionOrder(content);
  }

  /**
   * Validate section order matches template
   */
  validateSectionOrder(content) {
    const expectedOrder = [
      '## 🎯 Purpose',
      '## 🚀 Usage',
      '## 🔧 Implementation',
      '## ⚡ Triggers',
      '## 🔗 See Also'
    ];

    let lastIndex = -1;
    for (const section of expectedOrder) {
      const index = content.indexOf(section);
      if (index !== -1) {
        if (index < lastIndex) {
          this.addBlockingError('section_order', 
            `Section "${section}" appears out of order`,
            `Reorder sections to match template: ${expectedOrder.join(' → ')}`);
          break;
        }
        lastIndex = index;
      }
    }
  }

  /**
   * BLOCKING: Validate content requirements
   */
  validateContent(content) {
    const lines = content.split('\n');
    
    // Line limit check
    if (lines.length > this.maxLines) {
      this.addBlockingError('line_limit', 
        `File exceeds ${this.maxLines} line limit (${lines.length} lines)`,
        'Reduce content or extract detailed sections to separate files');
    }

    // Purpose validation
    this.validatePurposeSection(content);
    
    // Usage validation
    this.validateUsageSection(content);
    
    // Implementation minimum content
    this.validateImplementationSection(content);
    
    // Critical note validation
    this.validateCriticalNote(content);
  }

  /**
   * Validate Purpose section
   */
  validatePurposeSection(content) {
    const purposeMatch = content.match(/## 🎯 Purpose\s*\n([^\n#]+)/);
    
    if (!purposeMatch) {
      this.addBlockingError('missing_purpose', 
        'Purpose section missing or empty',
        'Add a single line describing the command purpose');
      return;
    }

    const purposeText = purposeMatch[1].trim();
    if (purposeText.length > this.maxPurposeLength) {
      this.addBlockingError('purpose_length', 
        `Purpose exceeds ${this.maxPurposeLength} characters (${purposeText.length})`,
        'Make purpose more concise - single line objective');
    }

    if (purposeText.split('\n').length > 1) {
      this.addBlockingError('purpose_multiline', 
        'Purpose must be a single line',
        'Combine into one concise sentence');
    }
  }

  /**
   * Validate Usage section
   */
  validateUsageSection(content) {
    const usageMatch = content.match(/## 🚀 Usage\s*\n([\s\S]*?)(?=\n## |$)/);
    
    if (!usageMatch) {
      this.addBlockingError('missing_usage', 
        'Usage section missing',
        'Add usage section with Execute: format');
      return;
    }

    const usageContent = usageMatch[1];
    if (!usageContent.includes('Execute:')) {
      this.addBlockingError('usage_format', 
        'Usage section must include Execute: line',
        'Add line: Execute: `/command-name [parameters]`');
    }
  }

  /**
   * Validate Implementation section has minimum content
   */
  validateImplementationSection(content) {
    const implMatch = content.match(/## 🔧 Implementation\s*\n([\s\S]*?)(?=\n## |$)/);
    
    if (!implMatch) {
      this.addBlockingError('missing_implementation', 
        'Implementation section missing',
        'Add implementation section with behavioral protocol and details');
      return;
    }

    const implContent = implMatch[1].trim();
    const wordCount = implContent.split(/\s+/).length;
    
    if (wordCount < 50) {
      this.addBlockingError('implementation_length', 
        `Implementation section too short (${wordCount} words, minimum 50)`,
        'Add more implementation details, protocols, or examples');
    }
  }

  /**
   * Validate Critical note exists
   */
  validateCriticalNote(content) {
    if (!content.includes('**CRITICAL**:')) {
      this.addBlockingError('missing_critical', 
        'Critical note missing at end of document',
        'Add **CRITICAL**: note explaining key requirements or usage');
    }
  }

  /**
   * BLOCKING: Validate TodoWrite block structure and content
   */
  validateTodoWrite(content) {
    const todoMatch = content.match(/TodoWrite\s*\(\s*\[([\s\S]*?)\]\s*\)/);
    
    if (!todoMatch) {
      this.addBlockingError('missing_todowrite', 
        'TodoWrite block required in Implementation section',
        'Add TodoWrite block with 3-7 todos using proper format');
      return;
    }

    try {
      const todoContent = todoMatch[1];
      const todoCount = (todoContent.match(/"content":/g) || []).length;
      
      if (todoCount < 3) {
        this.addBlockingError('todowrite_min', 
          `TodoWrite must have at least 3 todos (found ${todoCount})`,
          'Add more todos to reach minimum of 3');
      }
      
      if (todoCount > 7) {
        this.addBlockingError('todowrite_max', 
          `TodoWrite must have maximum 7 todos (found ${todoCount})`,
          'Reduce todos or combine related items');
      }

      // Validate todo structure
      this.validateTodoStructure(todoContent);
      
    } catch (error) {
      this.addBlockingError('todowrite_parse', 
        'TodoWrite block has invalid syntax',
        'Fix JSON formatting and ensure all required fields exist');
    }
  }

  /**
   * Validate individual todo structure
   */
  validateTodoStructure(todoContent) {
    const todoItems = this.extractTodoItems(todoContent);
    const validStatuses = ['pending', 'in_progress', 'completed'];
    const validPriorities = ['low', 'medium', 'high'];

    todoItems.forEach((todo, index) => {
      if (!todo.content) {
        this.addBlockingError('todo_missing_content', 
          `Todo ${index + 1} missing content field`,
          'Add content field with descriptive text');
      }

      if (!validStatuses.includes(todo.status)) {
        this.addBlockingError('todo_invalid_status', 
          `Todo ${index + 1} has invalid status: ${todo.status}`,
          `Use one of: ${validStatuses.join(', ')}`);
      }

      if (!validPriorities.includes(todo.priority)) {
        this.addBlockingError('todo_invalid_priority', 
          `Todo ${index + 1} has invalid priority: ${todo.priority}`,
          `Use one of: ${validPriorities.join(', ')}`);
      }

      if (!todo.id) {
        this.addBlockingError('todo_missing_id', 
          `Todo ${index + 1} missing id field`,
          'Add unique id field for each todo');
      }
    });
  }

  /**
   * Extract todo items from content
   */
  extractTodoItems(todoContent) {
    const todoRegex = /\{[^}]*"content"[^}]*\}/g;
    const todoMatches = todoContent.match(todoRegex) || [];
    
    return todoMatches.map(todoStr => {
      try {
        return JSON.parse(todoStr.replace(/(\w+):/g, '"$1":'));
      } catch (e) {
        return this.parseManually(todoStr);
      }
    });
  }

  /**
   * Manually parse todo when JSON parsing fails
   */
  parseManually(todoStr) {
    return {
      content: this.extractField(todoStr, 'content'),
      status: this.extractField(todoStr, 'status'),
      priority: this.extractField(todoStr, 'priority'),
      id: this.extractField(todoStr, 'id')
    };
  }

  /**
   * Extract field from todo string
   */
  extractField(str, field) {
    const match = str.match(new RegExp(`"${field}"\\s*:\\s*"([^"]*)"`, 'i'));
    return match ? match[1] : null;
  }

  /**
   * Calculate comprehensive quality score (0-100)
   */
  calculateQualityScore(content) {
    let score = 100;

    // Structure quality (40 points)
    score -= this.assessStructureQuality(content);
    
    // Content quality (30 points)
    score -= this.assessContentQuality(content);
    
    // Formatting quality (20 points)
    score -= this.assessFormattingQuality(content);
    
    // Completeness quality (10 points)
    score -= this.assessCompletenessQuality(content);

    return Math.max(0, Math.round(score));
  }

  /**
   * Assess structure quality deductions
   */
  assessStructureQuality(content) {
    let deductions = 0;

    // Missing subsections
    if (!content.includes('### ')) deductions += 10;
    
    // Poor section organization
    if (content.split('## ').length < 6) deductions += 10;
    
    // Missing emphasis
    if (!content.includes('**MANDATORY')) deductions += 5;
    
    // No code blocks
    if (!content.includes('```')) deductions += 10;
    
    // Inconsistent emoji usage
    const sectionHeaders = content.match(/## ([🎯🚀🔧⚡🔗📊🚨⟳📋]) /g) || [];
    if (sectionHeaders.length < 4) deductions += 5;

    return deductions;
  }

  /**
   * Assess content quality deductions
   */
  assessContentQuality(content) {
    let deductions = 0;
    
    const wordCount = content.split(/\s+/).length;
    
    // Content too brief
    if (wordCount < 200) deductions += 15;
    
    // Lack of specific instructions
    if (!content.includes('Execute:')) deductions += 5;
    
    // Missing behavioral reinforcement
    if (!content.includes('TodoWrite')) deductions += 10;

    return deductions;
  }

  /**
   * Assess formatting quality deductions
   */
  assessFormattingQuality(content) {
    let deductions = 0;

    // Inconsistent line breaks
    if (content.includes('\n\n\n')) deductions += 5;
    
    // Trailing whitespace
    if (/\s+$/m.test(content)) deductions += 5;
    
    // Inconsistent bullet formatting
    const bulletTypes = (content.match(/^\s*[-*+]/gm) || []).map(b => b.trim()[0]);
    const uniqueBullets = [...new Set(bulletTypes)];
    if (uniqueBullets.length > 1) deductions += 5;
    
    // Missing proper link formatting
    if (content.includes('](') && !content.match(/\[([^\]]+)\]\(([^)]+)\)/)) {
      deductions += 5;
    }

    return deductions;
  }

  /**
   * Assess completeness quality deductions
   */
  assessCompletenessQuality(content) {
    let deductions = 0;

    // Missing cross-references
    if (!content.includes('## 🔗 See Also')) deductions += 5;
    
    // No related commands
    if (!content.includes('Execute `/')) deductions += 5;

    return deductions;
  }

  /**
   * WARNING: Validate cross-references (non-blocking)
   */
  validateCrossReferences(content, filename) {
    const linkPattern = /\[(.*?)\]\((.*?)\)/g;
    let match;
    
    while ((match = linkPattern.exec(content)) !== null) {
      const [fullMatch, linkText, linkPath] = match;
      
      if (linkPath.startsWith('../')) {
        // Internal link - would need file system check in real implementation
        this.addWarning('cross_reference', 
          `Unverified internal link: ${linkPath}`,
          'Verify link exists and path is correct');
      }
    }
  }

  /**
   * WARNING: Validate formatting (non-blocking)
   */
  validateFormatting(content) {
    // Check emoji consistency
    const sectionPattern = /## (.+)/g;
    let match;
    let nonStandardEmojis = [];
    
    while ((match = sectionPattern.exec(content)) !== null) {
      const sectionHeader = match[1];
      const hasStandardEmoji = this.standardEmojis.some(emoji => 
        sectionHeader.startsWith(emoji)
      );
      
      if (!hasStandardEmoji && !sectionHeader.match(/^[a-zA-Z]/)) {
        nonStandardEmojis.push(sectionHeader);
      }
    }

    if (nonStandardEmojis.length > 0) {
      this.addWarning('emoji_consistency', 
        `Non-standard emojis in sections: ${nonStandardEmojis.join(', ')}`,
        'Use standard emojis for section headers');
    }
  }

  /**
   * Add blocking error to results
   */
  addBlockingError(type, message, suggestion) {
    const error = {
      type,
      message,
      suggestion,
      severity: 'error',
      blocking: true,
      timestamp: new Date().toISOString()
    };
    
    this.blockingErrors.push(error);
    this.validationResults.push(error);
  }

  /**
   * Add warning to results
   */
  addWarning(type, message, suggestion) {
    const warning = {
      type,
      message,
      suggestion,
      severity: 'warning',
      blocking: false,
      timestamp: new Date().toISOString()
    };
    
    this.warnings.push(warning);
    this.validationResults.push(warning);
  }

  /**
   * Check if there are blocking errors
   */
  hasBlockingErrors() {
    return this.blockingErrors.length > 0;
  }

  /**
   * Create blocked validation result
   */
  createBlockedResult(reason) {
    return {
      valid: false,
      blocked: true,
      reason,
      errors: this.blockingErrors,
      warnings: this.warnings,
      qualityScore: 0,
      canProceed: false,
      summary: this.getValidationSummary()
    };
  }

  /**
   * Create successful validation result
   */
  createSuccessResult(qualityScore) {
    return {
      valid: true,
      blocked: false,
      errors: [],
      warnings: this.warnings,
      qualityScore,
      canProceed: true,
      summary: this.getValidationSummary()
    };
  }

  /**
   * Get validation summary
   */
  getValidationSummary() {
    return {
      totalIssues: this.validationResults.length,
      blockingErrors: this.blockingErrors.length,
      warnings: this.warnings.length,
      categories: this.getCategorizedIssues()
    };
  }

  /**
   * Get issues categorized by type
   */
  getCategorizedIssues() {
    const categories = {};
    
    this.validationResults.forEach(result => {
      if (!categories[result.type]) {
        categories[result.type] = [];
      }
      categories[result.type].push(result);
    });
    
    return categories;
  }

  /**
   * Generate detailed validation report
   */
  generateReport() {
    const report = {
      timestamp: new Date().toISOString(),
      summary: this.getValidationSummary(),
      details: {
        blockingErrors: this.blockingErrors,
        warnings: this.warnings
      },
      recommendations: this.generateRecommendations()
    };

    return report;
  }

  /**
   * Generate recommendations based on validation results
   */
  generateRecommendations() {
    const recommendations = [];
    
    if (this.hasBlockingErrors()) {
      recommendations.push({
        priority: 'critical',
        action: 'Fix all blocking errors before proceeding',
        details: this.blockingErrors.map(e => e.suggestion)
      });
    }

    if (this.warnings.length > 0) {
      recommendations.push({
        priority: 'optional',
        action: 'Consider addressing warnings for better quality',
        details: this.warnings.map(w => w.suggestion)
      });
    }

    return recommendations;
  }
}

module.exports = ValidationEngine;