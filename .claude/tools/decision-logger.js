/**
 * Creative Decision Transparency System
 * 
 * Logs and explains creative variations from standard templates,
 * providing full transparency to users about AI decision-making.
 */

class DecisionLogger {
  constructor(logFilePath = '/Users/nalve/ce-simple/.claude/tools/creative-decisions.json') {
    this.logFilePath = logFilePath;
    this.currentSession = {
      sessionId: this.generateSessionId(),
      timestamp: new Date().toISOString(),
      decisions: [],
      deviations: [],
      userNotifications: []
    };
    this.decisionTypes = {
      STRUCTURE_VARIATION: 'structure_variation',
      CONTENT_ENHANCEMENT: 'content_enhancement', 
      FORMAT_ADAPTATION: 'format_adaptation',
      CREATIVE_OPTIMIZATION: 'creative_optimization',
      USER_PREFERENCE_ADAPTATION: 'user_preference_adaptation'
    };
  }

  /**
   * Log a creative decision with full transparency
   */
  logCreativeDecision(decision) {
    const logEntry = {
      id: this.generateDecisionId(),
      timestamp: new Date().toISOString(),
      type: decision.type,
      rationale: decision.rationale,
      standard: decision.standard,
      variation: decision.variation,
      impact: decision.impact,
      confidence: decision.confidence || 0.8,
      userBenefit: decision.userBenefit,
      alternatives: decision.alternatives || [],
      context: decision.context || {}
    };

    this.currentSession.decisions.push(logEntry);
    this.persistDecision(logEntry);
    
    return logEntry;
  }

  /**
   * Log deviation from standard template
   */
  logTemplateDeviation(deviation) {
    const deviationEntry = {
      id: this.generateDeviationId(),
      timestamp: new Date().toISOString(),
      section: deviation.section,
      standardFormat: deviation.standardFormat,
      actualFormat: deviation.actualFormat,
      reason: deviation.reason,
      severity: deviation.severity || 'minor',
      approved: deviation.approved || false
    };

    this.currentSession.deviations.push(deviationEntry);
    return deviationEntry;
  }

  /**
   * Generate user-friendly explanation of creative decisions
   */
  explainDecisionToUser(decision) {
    const explanation = this.formatUserExplanation(decision);
    
    this.currentSession.userNotifications.push({
      id: decision.id,
      timestamp: new Date().toISOString(),
      explanation,
      userAcknowledged: false
    });

    return explanation;
  }

  /**
   * Format decision explanation for user
   */
  formatUserExplanation(decision) {
    const explanationTemplates = {
      [this.decisionTypes.STRUCTURE_VARIATION]: `
🏗️ STRUCTURAL DECISION MADE:
Rationale: ${decision.rationale}
Standard Template: ${decision.standard}
Creative Adaptation: ${decision.variation}
User Benefit: ${decision.userBenefit}
Confidence: ${(decision.confidence * 100).toFixed(0)}%`,

      [this.decisionTypes.CONTENT_ENHANCEMENT]: `
✨ CONTENT ENHANCEMENT APPLIED:
Enhancement: ${decision.variation}
Reasoning: ${decision.rationale}
Original Standard: ${decision.standard}
Added Value: ${decision.userBenefit}
Quality Impact: ${decision.impact}`,

      [this.decisionTypes.FORMAT_ADAPTATION]: `
🎨 FORMAT ADAPTATION CHOSEN:
Standard Format: ${decision.standard}
Adapted Format: ${decision.variation}
Adaptation Reason: ${decision.rationale}
Improved Experience: ${decision.userBenefit}`,

      [this.decisionTypes.CREATIVE_OPTIMIZATION]: `
🚀 CREATIVE OPTIMIZATION IMPLEMENTED:
Optimization: ${decision.variation}
Why Different: ${decision.rationale}
Standard Approach: ${decision.standard}
Performance Benefit: ${decision.impact}
User Advantage: ${decision.userBenefit}`,

      [this.decisionTypes.USER_PREFERENCE_ADAPTATION]: `
👤 USER PREFERENCE DETECTED:
Adapted To: ${decision.variation}
User Pattern: ${decision.context.userPattern || 'Detected usage pattern'}
Standard Default: ${decision.standard}
Personalization Benefit: ${decision.userBenefit}`
    };

    return explanationTemplates[decision.type] || this.formatGenericExplanation(decision);
  }

  /**
   * Format generic explanation for unknown decision types
   */
  formatGenericExplanation(decision) {
    return `
🤖 CREATIVE DECISION APPLIED:
Type: ${decision.type}
Reasoning: ${decision.rationale}
Standard: ${decision.standard}
Variation: ${decision.variation}
Benefit: ${decision.userBenefit}
Impact: ${decision.impact}`;
  }

  /**
   * Analyze user command patterns to inform decisions
   */
  analyzeUserPatterns(userCommands) {
    const patterns = {
      preferredLength: this.analyzePreferredLength(userCommands),
      commonStructures: this.analyzeStructurePreferences(userCommands),
      vocabularyStyle: this.analyzeVocabularyStyle(userCommands),
      complexityPreference: this.analyzeComplexityPreference(userCommands)
    };

    return patterns;
  }

  /**
   * Analyze user's preferred command length
   */
  analyzePreferredLength(commands) {
    const lengths = commands.map(cmd => cmd.content.split('\n').length);
    const avgLength = lengths.reduce((a, b) => a + b, 0) / lengths.length;
    
    if (avgLength < 50) return 'concise';
    if (avgLength < 150) return 'moderate';
    return 'detailed';
  }

  /**
   * Analyze user's structure preferences
   */
  analyzeStructurePreferences(commands) {
    const structures = {
      usesSubsections: commands.some(cmd => cmd.content.includes('### ')),
      prefersCodeBlocks: commands.some(cmd => cmd.content.includes('```')),
      usesBulletPoints: commands.some(cmd => cmd.content.includes('- ')),
      prefersNumberedLists: commands.some(cmd => cmd.content.includes('1. '))
    };

    return structures;
  }

  /**
   * Analyze user's vocabulary and tone style
   */
  analyzeVocabularyStyle(commands) {
    const allText = commands.map(cmd => cmd.content).join(' ').toLowerCase();
    
    return {
      formalTone: this.countOccurrences(allText, ['shall', 'must', 'required', 'mandatory']),
      technicalDepth: this.countOccurrences(allText, ['implementation', 'protocol', 'algorithm', 'framework']),
      actionOriented: this.countOccurrences(allText, ['execute', 'run', 'apply', 'deploy'])
    };
  }

  /**
   * Count occurrences of words in text
   */
  countOccurrences(text, words) {
    return words.reduce((count, word) => {
      return count + (text.match(new RegExp(word, 'g')) || []).length;
    }, 0);
  }

  /**
   * Analyze user's complexity preferences
   */
  analyzeComplexityPreference(commands) {
    const avgTodoCount = commands
      .filter(cmd => cmd.content.includes('TodoWrite'))
      .map(cmd => (cmd.content.match(/"content":/g) || []).length)
      .reduce((a, b) => a + b, 0) / commands.length || 3;

    if (avgTodoCount <= 3) return 'simple';
    if (avgTodoCount <= 5) return 'moderate';
    return 'complex';
  }

  /**
   * Generate contextual decision based on user patterns
   */
  generateContextualDecision(standardTemplate, userPatterns, commandContext) {
    const decisions = [];

    // Length adaptation
    if (userPatterns.preferredLength === 'concise' && standardTemplate.length > 100) {
      decisions.push({
        type: this.decisionTypes.USER_PREFERENCE_ADAPTATION,
        rationale: 'User prefers concise commands based on historical pattern',
        standard: 'Standard detailed template',
        variation: 'Condensed format with essential information only',
        userBenefit: 'Faster reading and comprehension',
        confidence: 0.85,
        context: { userPattern: userPatterns.preferredLength }
      });
    }

    // Structure adaptation
    if (userPatterns.commonStructures.usesSubsections) {
      decisions.push({
        type: this.decisionTypes.STRUCTURE_VARIATION,
        rationale: 'User consistently uses subsections for organization',
        standard: 'Flat section structure',
        variation: 'Enhanced subsection organization',
        userBenefit: 'Better information hierarchy matching user style',
        confidence: 0.9
      });
    }

    // Complexity adaptation
    if (userPatterns.complexityPreference === 'complex' && commandContext.isAdvanced) {
      decisions.push({
        type: this.decisionTypes.CONTENT_ENHANCEMENT,
        rationale: 'User handles complex workflows effectively',
        standard: 'Basic implementation details',
        variation: 'Advanced implementation with optimization techniques',
        userBenefit: 'Leverages user expertise for better results',
        confidence: 0.8
      });
    }

    return decisions;
  }

  /**
   * Validate decision against system constraints
   */
  validateDecision(decision) {
    const validation = {
      valid: true,
      warnings: [],
      constraints: []
    };

    // Check if decision maintains essential structure
    if (decision.type === this.decisionTypes.STRUCTURE_VARIATION) {
      if (!this.preservesEssentialStructure(decision)) {
        validation.warnings.push('Structural change may affect template compatibility');
      }
    }

    // Check if decision impacts validation
    if (this.impactsValidation(decision)) {
      validation.constraints.push('Decision may affect validation requirements');
    }

    // Check confidence threshold
    if (decision.confidence < 0.7) {
      validation.warnings.push('Low confidence decision - consider standard approach');
    }

    return validation;
  }

  /**
   * Check if decision preserves essential structure
   */
  preservesEssentialStructure(decision) {
    const essentialElements = [
      '## 🎯 Purpose',
      '## 🚀 Usage', 
      '## 🔧 Implementation',
      'TodoWrite([',
      '## ⚡ Triggers',
      '## 🔗 See Also'
    ];

    return essentialElements.every(element => 
      decision.variation.includes(element) || decision.standard.includes(element)
    );
  }

  /**
   * Check if decision impacts validation
   */
  impactsValidation(decision) {
    const validationCritical = [
      'TodoWrite',
      'Purpose',
      'Usage',
      'CRITICAL'
    ];

    return validationCritical.some(critical =>
      decision.variation.toLowerCase().includes(critical.toLowerCase()) ||
      decision.standard.toLowerCase().includes(critical.toLowerCase())
    );
  }

  /**
   * Generate decision approval request
   */
  generateApprovalRequest(decision) {
    return {
      id: decision.id,
      type: decision.type,
      summary: this.formatDecisionSummary(decision),
      impact: decision.impact,
      alternatives: decision.alternatives,
      recommendation: decision.confidence > 0.8 ? 'approve' : 'review',
      timeout: 30000 // 30 seconds for approval
    };
  }

  /**
   * Format decision summary for approval
   */
  formatDecisionSummary(decision) {
    return `${decision.type.replace(/_/g, ' ')} - ${decision.rationale}`;
  }

  /**
   * Persist decision to log file
   */
  async persistDecision(decision) {
    try {
      const existingLog = await this.loadExistingLog();
      existingLog.sessions = existingLog.sessions || [];
      
      // Add to current session
      let sessionIndex = existingLog.sessions.findIndex(s => s.sessionId === this.currentSession.sessionId);
      if (sessionIndex === -1) {
        existingLog.sessions.push(this.currentSession);
        sessionIndex = existingLog.sessions.length - 1;
      } else {
        existingLog.sessions[sessionIndex] = this.currentSession;
      }

      await this.saveLogFile(existingLog);
    } catch (error) {
      console.error('Failed to persist decision:', error.message);
    }
  }

  /**
   * Load existing log file
   */
  async loadExistingLog() {
    try {
      // In real implementation, would read from file system
      return { 
        version: '1.0',
        created: new Date().toISOString(),
        sessions: []
      };
    } catch (error) {
      return { 
        version: '1.0',
        created: new Date().toISOString(),
        sessions: []
      };
    }
  }

  /**
   * Save log file
   */
  async saveLogFile(logData) {
    // In real implementation, would write to file system
    console.log('Decision log saved:', JSON.stringify(logData, null, 2));
  }

  /**
   * Generate session report
   */
  generateSessionReport() {
    return {
      sessionId: this.currentSession.sessionId,
      timestamp: this.currentSession.timestamp,
      summary: {
        totalDecisions: this.currentSession.decisions.length,
        deviations: this.currentSession.deviations.length,
        userNotifications: this.currentSession.userNotifications.length,
        averageConfidence: this.calculateAverageConfidence(),
        decisionTypes: this.groupDecisionsByType()
      },
      decisions: this.currentSession.decisions,
      deviations: this.currentSession.deviations,
      userFeedback: this.currentSession.userNotifications
    };
  }

  /**
   * Calculate average confidence across decisions
   */
  calculateAverageConfidence() {
    if (this.currentSession.decisions.length === 0) return 0;
    
    const totalConfidence = this.currentSession.decisions.reduce((sum, d) => sum + d.confidence, 0);
    return totalConfidence / this.currentSession.decisions.length;
  }

  /**
   * Group decisions by type for analysis
   */
  groupDecisionsByType() {
    const grouped = {};
    
    this.currentSession.decisions.forEach(decision => {
      if (!grouped[decision.type]) {
        grouped[decision.type] = 0;
      }
      grouped[decision.type]++;
    });

    return grouped;
  }

  /**
   * Generate unique session ID
   */
  generateSessionId() {
    return `session-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  }

  /**
   * Generate unique decision ID
   */
  generateDecisionId() {
    return `decision-${Date.now()}-${Math.random().toString(36).substr(2, 6)}`;
  }

  /**
   * Generate unique deviation ID
   */
  generateDeviationId() {
    return `deviation-${Date.now()}-${Math.random().toString(36).substr(2, 6)}`;
  }
}

module.exports = DecisionLogger;