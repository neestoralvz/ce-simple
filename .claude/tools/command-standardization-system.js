/**
 * Command Standardization System - Main Controller
 * 
 * Comprehensive command standardization system integrating all components:
 * - Strict blocking validation
 * - Intelligent auto-correction
 * - Creative decision transparency
 * - Efficient template generation
 * - User workflow optimization
 */

const ValidationEngine = require('./validation-engine');
const AutoCorrectionEngine = require('./auto-correction-engine');
const DecisionLogger = require('./decision-logger');
const TemplateGenerator = require('./template-generator');

class CommandStandardizationSystem {
  constructor(options = {}) {
    this.options = {
      blockingValidation: true,
      autoCorrection: true,
      creativeTransparency: true,
      userLearning: true,
      performanceTracking: true,
      ...options
    };

    // Initialize system components
    this.validator = new ValidationEngine();
    this.corrector = new AutoCorrectionEngine();
    this.decisionLogger = new DecisionLogger();
    this.templateGenerator = new TemplateGenerator();
    
    // System state
    this.userPatterns = this.loadUserPatterns();
    this.systemMetrics = this.initializeMetrics();
    this.activeSession = null;
  }

  /**
   * Main command creation workflow
   */
  async createCommand(commandName, options = {}) {
    console.log(`🚀 Starting command creation: ${commandName}`);
    
    // Initialize session
    this.activeSession = this.initializeSession(commandName, options);
    
    try {
      // PHASE 1: Template Generation
      const template = await this.generateTemplate(commandName, options);
      
      // PHASE 2: Pre-validation
      const preValidation = this.performPreValidation(template);
      
      // PHASE 3: Auto-correction (if needed)
      const correctedTemplate = await this.performAutoCorrection(template, preValidation);
      
      // PHASE 4: Final validation (BLOCKING)
      const finalValidation = this.performFinalValidation(correctedTemplate);
      
      // PHASE 5: Creative decision resolution
      const finalTemplate = await this.resolveCreativeDecisions(correctedTemplate, finalValidation);
      
      // PHASE 6: Quality assurance
      const result = this.performQualityAssurance(finalTemplate);
      
      // PHASE 7: Session completion
      this.completeSession(result);
      
      return result;
      
    } catch (error) {
      this.handleError(error);
      throw error;
    }
  }

  /**
   * Generate template with context awareness
   */
  async generateTemplate(commandName, options) {
    console.log('🏗️ Generating template...');
    const startTime = Date.now();
    
    try {
      let template;
      
      if (options.contextual || this.userPatterns.commands.length >= 3) {
        // Use contextual generation with user patterns
        const contextResult = this.templateGenerator.generateContextualTemplate(
          commandName,
          this.userPatterns,
          options.relatedCommands || []
        );
        template = contextResult.template;
        
        // Log any creative decisions made during generation
        if (contextResult.decisions) {
          contextResult.decisions.forEach(decision => {
            this.decisionLogger.logCreativeDecision(decision);
            console.log(this.decisionLogger.explainDecisionToUser(decision));
          });
        }
        
      } else {
        // Use standard generation
        template = this.templateGenerator.generateTemplate(
          commandName,
          options.complexity || 'medium',
          options.category
        );
      }
      
      const duration = Date.now() - startTime;
      this.updateMetric('template_generation_time', duration);
      console.log(`✅ Template generated in ${duration}ms`);
      
      return {
        content: template,
        metadata: {
          commandName,
          generatedAt: new Date().toISOString(),
          duration,
          method: options.contextual ? 'contextual' : 'standard'
        }
      };
      
    } catch (error) {
      this.updateMetric('template_generation_errors', 1);
      throw new Error(`Template generation failed: ${error.message}`);
    }
  }

  /**
   * Perform pre-validation for early error detection
   */
  performPreValidation(template) {
    console.log('🔍 Pre-validation check...');
    const startTime = Date.now();
    
    try {
      // Quick validation to catch obvious issues early
      const validation = this.validator.validateCommand(template.content, template.metadata.commandName);
      
      const duration = Date.now() - startTime;
      this.updateMetric('pre_validation_time', duration);
      
      if (validation.blocked) {
        console.log('⚠️ Pre-validation found blocking issues');
        this.logValidationIssues(validation);
      } else {
        console.log('✅ Pre-validation passed');
      }
      
      return validation;
      
    } catch (error) {
      this.updateMetric('pre_validation_errors', 1);
      throw new Error(`Pre-validation failed: ${error.message}`);
    }
  }

  /**
   * Perform auto-correction if issues detected
   */
  async performAutoCorrection(template, validation) {
    if (validation.valid && validation.warnings.length === 0) {
      console.log('⏭️ Auto-correction skipped - no issues detected');
      return template;
    }

    console.log('🔧 Performing auto-correction...');
    const startTime = Date.now();
    
    try {
      const correction = this.corrector.correctCommand(template.content, template.metadata.commandName);
      
      const duration = Date.now() - startTime;
      this.updateMetric('auto_correction_time', duration);
      
      if (correction.corrections.length > 0) {
        console.log(`✅ Auto-correction applied ${correction.corrections.length} fixes`);
        
        // Log significant corrections as creative decisions
        const significantCorrections = correction.corrections.filter(c => 
          ['content_compression', 'structure_enhancement'].includes(c.type)
        );
        
        significantCorrections.forEach(corr => {
          const decision = {
            type: 'creative_optimization',
            rationale: `Auto-correction: ${corr.message}`,
            standard: 'Original content',
            variation: 'Optimized content',
            userBenefit: 'Improved quality and compliance',
            confidence: 0.9
          };
          
          this.decisionLogger.logCreativeDecision(decision);
        });
        
        // Show correction summary
        const summary = correction.getCorrectionSummary();
        console.log(`📊 Corrections: ${summary.autoFixes} auto-fixes, ${summary.warnings} warnings, ${summary.errors} errors`);
      }
      
      return {
        ...template,
        content: correction.content,
        correctionApplied: true,
        corrections: correction.corrections
      };
      
    } catch (error) {
      this.updateMetric('auto_correction_errors', 1);
      throw new Error(`Auto-correction failed: ${error.message}`);
    }
  }

  /**
   * Perform final validation (BLOCKING)
   */
  performFinalValidation(template) {
    console.log('✅ Final validation (BLOCKING)...');
    const startTime = Date.now();
    
    try {
      const validation = this.validator.validateCommand(template.content, template.metadata.commandName);
      
      const duration = Date.now() - startTime;
      this.updateMetric('final_validation_time', duration);
      
      if (validation.blocked) {
        console.log('🚨 VALIDATION BLOCKED - Command creation cannot proceed');
        this.logValidationIssues(validation);
        
        // Generate user-friendly error report
        const report = this.generateValidationReport(validation);
        throw new Error(`Command validation failed: ${report}`);
        
      } else {
        console.log(`✅ Final validation passed - Quality score: ${validation.qualityScore}/100`);
        this.updateMetric('successful_validations', 1);
      }
      
      return validation;
      
    } catch (error) {
      this.updateMetric('final_validation_errors', 1);
      throw error;
    }
  }

  /**
   * Resolve creative decisions with user transparency
   */
  async resolveCreativeDecisions(template, validation) {
    const decisions = this.decisionLogger.currentSession.decisions;
    
    if (decisions.length === 0) {
      console.log('⏭️ No creative decisions to resolve');
      return template;
    }

    console.log(`🎨 Resolving ${decisions.length} creative decisions...`);
    
    // For now, auto-approve high-confidence decisions
    // In real implementation, would interact with user
    const approvedDecisions = decisions.filter(d => d.confidence >= 0.8);
    const pendingDecisions = decisions.filter(d => d.confidence < 0.8);
    
    if (pendingDecisions.length > 0) {
      console.log(`⚠️ ${pendingDecisions.length} decisions require user approval:`);
      pendingDecisions.forEach(decision => {
        console.log(this.decisionLogger.explainDecisionToUser(decision));
      });
      
      // Simulate user approval (in real implementation, would wait for user input)
      console.log('🤖 Simulating user approval for demonstration...');
    }
    
    console.log(`✅ Creative decisions resolved: ${approvedDecisions.length} approved, ${pendingDecisions.length} pending`);
    
    return template;
  }

  /**
   * Perform final quality assurance
   */
  performQualityAssurance(template) {
    console.log('🔍 Final quality assurance...');
    
    const qaResult = {
      template,
      qualityMetrics: {
        structureCompliance: this.assessStructureCompliance(template.content),
        contentQuality: this.assessContentQuality(template.content),
        validationScore: template.metadata.validationScore || 0,
        correctionEfficiency: this.assessCorrectionEfficiency(template),
        userExperienceScore: this.assessUserExperience()
      },
      recommendations: this.generateRecommendations(template),
      success: true
    };
    
    const overallScore = this.calculateOverallScore(qaResult.qualityMetrics);
    qaResult.overallQualityScore = overallScore;
    
    console.log(`📊 Quality assurance complete - Overall score: ${overallScore}/100`);
    
    return qaResult;
  }

  /**
   * Complete session and update learning
   */
  completeSession(result) {
    console.log('🎯 Completing session...');
    
    // Update user patterns based on session
    this.updateUserPatterns(result);
    
    // Update system metrics
    this.updateSystemMetrics(result);
    
    // Generate session report
    const sessionReport = this.decisionLogger.generateSessionReport();
    
    // Save session data
    this.saveSession(this.activeSession, result, sessionReport);
    
    console.log('✅ Session completed successfully');
    console.log(`📈 Session metrics: ${result.qualityMetrics.validationScore}/100 validation, ${sessionReport.summary.totalDecisions} decisions`);
    
    this.activeSession = null;
  }

  /**
   * Handle errors gracefully
   */
  handleError(error) {
    console.error('❌ Command creation failed:', error.message);
    
    if (this.activeSession) {
      this.activeSession.error = {
        message: error.message,
        timestamp: new Date().toISOString(),
        stack: error.stack
      };
      
      this.updateMetric('creation_errors', 1);
    }
  }

  /**
   * Initialize user session
   */
  initializeSession(commandName, options) {
    return {
      id: this.generateSessionId(),
      commandName,
      options,
      startTime: Date.now(),
      phases: [],
      metrics: {},
      decisions: []
    };
  }

  /**
   * Load user patterns from storage
   */
  loadUserPatterns() {
    // In real implementation, would load from file system
    return {
      preferredLength: 'medium',
      commonStructures: {
        usesSubsections: false,
        prefersCodeBlocks: true,
        usesBulletPoints: true
      },
      vocabularyStyle: {
        formalTone: 2,
        technicalDepth: 4,
        actionOriented: 5
      },
      complexityPreference: 'medium',
      commands: [] // Previous commands for pattern analysis
    };
  }

  /**
   * Initialize system metrics
   */
  initializeMetrics() {
    return {
      template_generation_time: [],
      pre_validation_time: [],
      auto_correction_time: [],
      final_validation_time: [],
      total_creation_time: [],
      successful_validations: 0,
      creation_errors: 0,
      user_satisfaction: []
    };
  }

  /**
   * Update specific metric
   */
  updateMetric(metricName, value) {
    if (Array.isArray(this.systemMetrics[metricName])) {
      this.systemMetrics[metricName].push(value);
    } else {
      this.systemMetrics[metricName] += value;
    }
  }

  /**
   * Log validation issues for debugging
   */
  logValidationIssues(validation) {
    if (validation.errors.length > 0) {
      console.log('❌ Blocking errors:');
      validation.errors.forEach(error => {
        console.log(`   - ${error.message}`);
        console.log(`     Fix: ${error.suggestion}`);
      });
    }
    
    if (validation.warnings.length > 0) {
      console.log('⚠️ Warnings:');
      validation.warnings.forEach(warning => {
        console.log(`   - ${warning.message}`);
      });
    }
  }

  /**
   * Generate user-friendly validation report
   */
  generateValidationReport(validation) {
    const errorCount = validation.errors.length;
    const warningCount = validation.warnings.length;
    
    let report = `${errorCount} blocking errors, ${warningCount} warnings.\n`;
    
    if (errorCount > 0) {
      report += '\nRequired fixes:\n';
      validation.errors.forEach((error, i) => {
        report += `${i + 1}. ${error.message}\n   → ${error.suggestion}\n`;
      });
    }
    
    return report;
  }

  /**
   * Assessment helper methods
   */
  assessStructureCompliance(content) {
    const requiredSections = ['🎯 Purpose', '🚀 Usage', '🔧 Implementation', '⚡ Triggers', '🔗 See Also'];
    const foundSections = requiredSections.filter(section => content.includes(section));
    return Math.round((foundSections.length / requiredSections.length) * 100);
  }

  assessContentQuality(content) {
    const wordCount = content.split(/\s+/).length;
    const hasExamples = content.includes('```');
    const hasProperFormatting = content.includes('**') && content.includes('- ');
    
    let score = 60; // Base score
    if (wordCount >= 200) score += 20;
    if (hasExamples) score += 10;
    if (hasProperFormatting) score += 10;
    
    return Math.min(score, 100);
  }

  assessCorrectionEfficiency(template) {
    if (!template.correctionApplied) return 100;
    
    const corrections = template.corrections || [];
    const errorCorrections = corrections.filter(c => c.severity === 'error').length;
    const totalCorrections = corrections.length;
    
    // Higher efficiency if fewer corrections needed
    return Math.max(100 - (totalCorrections * 5), 60);
  }

  assessUserExperience() {
    // Based on session metrics and patterns
    const avgGenerationTime = this.getAverageMetric('template_generation_time');
    const avgValidationTime = this.getAverageMetric('final_validation_time');
    
    let score = 100;
    if (avgGenerationTime > 5000) score -= 20; // >5s is too slow
    if (avgValidationTime > 3000) score -= 10;  // >3s is slow
    
    return Math.max(score, 50);
  }

  calculateOverallScore(metrics) {
    const weights = {
      structureCompliance: 0.3,
      contentQuality: 0.25,
      validationScore: 0.25,
      correctionEfficiency: 0.1,
      userExperienceScore: 0.1
    };
    
    let score = 0;
    Object.entries(weights).forEach(([metric, weight]) => {
      score += (metrics[metric] || 0) * weight;
    });
    
    return Math.round(score);
  }

  generateRecommendations(template) {
    const recommendations = [];
    
    if (template.corrections && template.corrections.length > 5) {
      recommendations.push('Consider using more structured initial content to reduce auto-corrections needed');
    }
    
    if (!template.content.includes('### ')) {
      recommendations.push('Adding subsections could improve document organization');
    }
    
    return recommendations;
  }

  /**
   * Learning and pattern updates
   */
  updateUserPatterns(result) {
    // Update patterns based on successful creation
    // In real implementation, would analyze choices and update patterns
    this.userPatterns.commands.push({
      name: result.template.metadata.commandName,
      timestamp: new Date().toISOString(),
      qualityScore: result.overallQualityScore,
      corrections: result.template.corrections?.length || 0
    });
    
    // Keep only last 20 commands for pattern analysis
    if (this.userPatterns.commands.length > 20) {
      this.userPatterns.commands = this.userPatterns.commands.slice(-20);
    }
  }

  updateSystemMetrics(result) {
    const totalTime = Date.now() - this.activeSession.startTime;
    this.updateMetric('total_creation_time', totalTime);
  }

  /**
   * Utility methods
   */
  getAverageMetric(metricName) {
    const values = this.systemMetrics[metricName];
    if (!Array.isArray(values) || values.length === 0) return 0;
    return values.reduce((a, b) => a + b, 0) / values.length;
  }

  generateSessionId() {
    return `session-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  }

  saveSession(session, result, report) {
    // In real implementation, would save to file system
    console.log('💾 Session saved:', {
      id: session.id,
      duration: Date.now() - session.startTime,
      qualityScore: result.overallQualityScore,
      decisionsCount: report.summary.totalDecisions
    });
  }

  /**
   * Public API methods
   */

  /**
   * Get system status and metrics
   */
  getSystemStatus() {
    return {
      metrics: {
        averageGenerationTime: this.getAverageMetric('template_generation_time'),
        averageValidationTime: this.getAverageMetric('final_validation_time'),
        successRate: this.calculateSuccessRate(),
        totalCommands: this.userPatterns.commands.length
      },
      userPatterns: this.userPatterns,
      activeSession: this.activeSession?.id || null
    };
  }

  calculateSuccessRate() {
    const total = this.systemMetrics.successful_validations + this.systemMetrics.creation_errors;
    if (total === 0) return 100;
    return Math.round((this.systemMetrics.successful_validations / total) * 100);
  }

  /**
   * Validate existing command
   */
  async validateExistingCommand(filePath, content) {
    console.log(`🔍 Validating existing command: ${filePath}`);
    return this.validator.validateCommand(content, filePath);
  }

  /**
   * Auto-correct existing command
   */
  async correctExistingCommand(filePath, content) {
    console.log(`🔧 Auto-correcting existing command: ${filePath}`);
    return this.corrector.correctCommand(content, filePath);
  }
}

module.exports = CommandStandardizationSystem;