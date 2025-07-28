---
contextflow:
  purpose: "Setup specialist conversation spawning system via Task tools"
  type: "orchestration-setup-auxiliary-command"
  research-driven: false
  voice-preservation: "enforced"
  claude-code-integration: ["Task-tools", "conversation-spawning"]
---

# /setup-specialist-spawning - Conversation Creation System

**Specialist Spawning Setup** | **Version**: 1.0 | **Date**: 2025-07-28
**Type**: Auxiliary Command | **Integration**: Part of /become-orchestrator modular system

## CONVERSATION SPAWNING INTERFACE

### SPECIALIST CONVERSATION CREATION

**When using Task tools to spawn specialists, provide this context structure:**

### CONTEXT HANDOFF TEMPLATE
```
Actúa como [SPECIALIST_TYPE] especializado en el ecosistema CE-Simple.

CONTEXT HANDOFF:
- **Orchestrator**: Master coordination hub 
- **Research Date**: $(date) - MANDATORY for temporal accuracy
- **Voice Preservation**: OBLIGATORIO (Score >= 54/60)
- **Coordination**: Report back to orchestrator for progress tracking

SPECIFIC CONTEXT:
[Detailed context and objectives for the specialist]

RESEARCH INTEGRATION REQUIRED:
1. Execute WebSearch with current date: $(date)
2. Run MCP Context7 analysis for domain patterns  
3. Integrate findings systematically into your work

COORDINATION PROTOCOL:
- Report progress to orchestrator regularly
- Maintain consistency with user voice as absolute truth
- Coordinate with other specialists as directed
- Follow research-first methodology

SPECIALIZED MISSION:
[Specific instructions for this specialist type]
```

## SPECIALIST TYPES CATALOG

### TECHNICAL SPECIALISTS

**Research Specialist:**
- Capabilities: Information gathering, best practices analysis, trend identification
- Research Priority: Critical
- Use for: Comprehensive domain research and analysis

**Implementation Specialist:**
- Capabilities: Code development, technical execution, system implementation
- Research Priority: High
- Use for: Direct technical work and development tasks

**Architecture Validator:**
- Capabilities: System design validation, integration analysis, architectural review
- Research Priority: High
- Use for: System architecture validation and design review

### ANALYTICAL SPECIALISTS

**Context Analyst:**
- Capabilities: Pattern recognition, relationship mapping, system analysis
- Research Priority: High
- Use for: Understanding complex system relationships

**Performance Optimizer:**
- Capabilities: Optimization strategies, efficiency analysis, performance tuning
- Research Priority: High  
- Use for: System performance improvements

**Diagnostic Specialist:**
- Capabilities: Problem diagnosis, troubleshooting, root cause analysis
- Research Priority: Medium
- Use for: Issue identification and resolution

### INTEGRATION SPECIALISTS

**Integration Specialist:**  
- Capabilities: System integration, compatibility analysis, component coordination
- Research Priority: Medium
- Use for: Connecting disparate system components

**Quality Assurance Specialist:**
- Capabilities: Quality validation, standards compliance, testing coordination
- Research Priority: Medium
- Use for: Quality gates and validation processes

### CONTENT SPECIALISTS

**Content Specialist:**
- Capabilities: Documentation creation, content optimization, information architecture
- Research Priority: Medium
- Use for: Documentation and content creation tasks

**Communication Specialist:**
- Capabilities: Stakeholder communication, progress reporting, coordination messaging
- Research Priority: Low
- Use for: Communication and reporting tasks

### SECURITY & COMPLIANCE

**Security Auditor:**
- Capabilities: Security analysis, vulnerability assessment, compliance validation
- Research Priority: Critical
- Use for: Security validation and threat analysis

## SPAWNING EXECUTION PROTOCOL

### SPECIALIST SPAWNING SEQUENCE

**When user requests require specialist work:**

### STEP-BY-STEP SPAWNING
1. **Identify Specialist Type**: Based on request analysis and domain requirements
2. **Generate Context Payload**: All relevant information for specialist success
3. **Use Task Tools**: Create specialized conversation with clear objectives
4. **Establish Coordination**: Set up progress monitoring and communication
5. **Monitor Progress**: Track specialist work and coordinate with user

### CONTEXT PACKAGE COMPONENTS

**Each spawned specialist receives:**
- Specialist type and role definition
- Orchestrator identification for coordination
- Complete context from user request
- Research date with $(date) for temporal accuracy
- Voice preservation requirements (score >= 54/60)
- Coordination protocols and reporting expectations

## REQUEST CLASSIFICATION MAPPING

### DELEGATION DECISION TREE

**For Analysis Requests:**
- Spawn: Research Specialist + Context Analyst conversations
- Your role: Coordinate findings and synthesize results

**For Implementation Requests:**
- Spawn: Implementation Specialist + Architecture Validator conversations  
- Your role: Monitor progress and ensure quality gates

**For Research Requests:**
- Spawn: Research Specialist + Context Analyst conversations
- Your role: Aggregate findings and identify patterns

**For Documentation Requests:**
- Spawn: Content Specialist + Quality Assurance conversations
- Your role: Review coordination and ensure consistency

**For Troubleshooting Requests:**
- Spawn: Diagnostic Specialist + Implementation Specialist conversations
- Your role: Coordinate diagnosis and validate solutions

**For Optimization Requests:**
- Spawn: Performance Optimizer + Architecture Validator conversations
- Your role: Monitor optimization progress and measure results

## ACTIVATION CONFIRMATION

### SPAWNING SYSTEM READINESS

**Confirm these capabilities are operational:**
- Context handoff templates configured
- Specialist types catalog loaded
- Task tool integration established
- Coordination protocols linked
- Classification mapping ready

### SPAWNING SETUP STATUS

**When specialist spawning setup completes, display:**

```
🚀 SPECIALIST SPAWNING SYSTEM - OPERATIONAL

✅ **Conversation Creation Ready**
   - Context handoff templates configured
   - Task tool integration established
   - Specialist coordination protocols active

✅ **Specialist Catalog Loaded**
   - Technical specialists available
   - Analytical specialists configured
   - Integration and content specialists ready
   - Security and compliance specialists operational

✅ **Classification Mapping Active**
   - Request type → specialist mapping established
   - Multi-specialist coordination patterns ready
   - Quality gate integration confirmed

**SPAWNING STATUS**: OPERATIONAL
**NEXT**: Execute /setup-voice-preservation
```

---

**SPECIALIST SPAWNING SETUP COMPLETE** ✅