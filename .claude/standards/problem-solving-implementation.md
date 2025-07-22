# Problem-Solving Implementation Standards

## 🔧 5-Phase Universal Methodology

### Phase 1: Problem Identification & Diagnosis
**Structured Error Analysis**:
```
🔍 SYMPTOM IDENTIFICATION: Document exact error messages, unexpected behaviors
📊 PROBLEM CLASSIFICATION: Code/System/Architecture/Configuration/Performance
🎯 IMPACT ASSESSMENT: Affected components, user experience, system stability
⚡ CONTEXT CAPTURE: Environment, timing, reproducibility, related changes
```

**Diagnostic Framework**:
- **Error Type**: Exception, Logic, Performance, Integration, Configuration
- **Severity**: Critical, High, Medium, Low impact classification
- **Scope**: Local, Module, System-wide, External dependency
- **Reproducibility**: Always, Intermittent, Specific conditions, One-time

### Phase 2: Internal Context Discovery
**Leverage Existing `/explore-codebase`**:
```
⚡ EXECUTE: /explore-codebase with problem-focused search parameters
📁 FILE DISCOVERY: Relevant source files, configuration, dependencies
🔗 DEPENDENCY MAPPING: Related components, imports, function calls
📋 PATTERN ANALYSIS: Similar code structures, error handling approaches
```

**Context Enhancement**:
- Error location analysis and surrounding code examination
- Related function/class/module identification
- Configuration and environment file analysis
- Recent changes and commit history relevant to problem area

### Phase 3: External Knowledge Research
**Leverage Existing `/explore-web` with Enhanced Search Strategy**:
```
⚡ EXECUTE: /explore-web with targeted problem/technology searches
🌐 ERROR PATTERNS: Search specific error messages and symptoms
📚 TECHNOLOGY RESEARCH: Framework/language-specific troubleshooting
🔧 SOLUTION PATTERNS: Best practices, common fixes, implementation approaches
⭐ COMMUNITY INSIGHTS: Stack Overflow, documentation, expert discussions
```

**Targeted Search Enhancement**:
- Specific error message research with technology context
- Framework/library-specific problem resolution patterns
- Performance optimization and debugging techniques
- Security implications and best practice validation

### Phase 4: Enhanced Multi-Layer Analysis
**Leverage Existing `/think-layers` with Problem-Solving Capabilities**:

**🧠 THINK: Problem Understanding & Initial Solutions**
- Root cause analysis based on symptoms and research
- Initial solution approach identification
- Quick wins and immediate mitigation strategies

**💪 THINK-HARD: Deep Pattern Analysis & Solution Architecture** 
- Comprehensive root cause investigation
- Multiple solution strategy evaluation
- Trade-off analysis and approach comparison

**🚀 THINK-HARDER: Complex Integration & Implementation Strategy**
- Detailed implementation planning with dependency consideration
- Risk assessment and rollback strategy design
- Testing approach and validation framework

**⭐ ULTRA-THINK: Comprehensive Solution Plan & Execution Roadmap**
- Complete step-by-step execution plan
- Resource requirements and timeline estimation
- Success criteria definition and monitoring approach

### Phase 5: Solution Planning & Execution Preparation
**Executable Plan Generation**:
```
📋 SOLUTION PLAN: Step-by-step implementation roadmap
🔧 RESOURCE MAPPING: Required tools, files, external dependencies
✅ VALIDATION CRITERIA: Success metrics and testing approach
⚠️ RISK MITIGATION: Rollback procedures and contingency planning
```

## 🤖 Automatic Integration Framework

### Error Detection Triggers
**Auto-Activation Conditions**:
- Command execution failures with error messages
- System health degradation detected
- User reports of unexpected behavior
- Performance threshold violations
- Integration failures between components

### Integration Points with Existing Commands
**Seamless Command Integration**:
- Any command can invoke `/problem-solving` when errors encountered
- Existing commands enhanced with error detection and auto-trigger logic
- Context preservation from originating command to problem-solving workflow
- Solution application coordinated with original command objectives

## 🔍 Enhanced Search Capabilities

### Problem-Specific Web Research
**Targeted Search Strategy** (extending `/explore-web`):
```
🔍 ERROR-SPECIFIC: "[exact error message]" + technology stack
📚 SOLUTION-FOCUSED: "how to fix [problem type]" + framework version
🛠️ IMPLEMENTATION: "[technology] best practices [problem domain]" 
⚡ COMMUNITY: "[error] site:stackoverflow.com OR site:github.com"
```

### Smart Query Generation
- Automatic search query optimization based on problem context
- Technology stack detection and inclusion in searches
- Error message extraction and search query formation
- Solution pattern discovery through intelligent search refinement

## 📊 Notification Integration

### Problem-Solving Progress Tracking
```
🔍 DIAGNOSIS: Problem identified → [type] classified, [severity] level
📁 DISCOVERY: Context analysis → [N] relevant files found
🌐 RESEARCH: External knowledge → [N] solution patterns discovered  
🧠 ANALYSIS: Think-layers active → Level [N] ([problem-solving mode])
📋 SOLUTION: Plan generated → [N] implementation steps ready
✅ READY: Execution plan complete → Solution deployment prepared
```

---

**REFERENCE**: Detailed implementation standards for /problem-solving command execution. Referenced from `.claude/commands/problem-solving.md` for progressive disclosure optimization.