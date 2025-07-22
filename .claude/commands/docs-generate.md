# Docs Generate - Todo Plans to Documentation Creation

## 🎯 Purpose
Convert todo list plans into structured Markdown documentation through parallel agent deployment and 3-wave execution strategy.

## 🚀 Usage
Execute: `/docs-generate [scope]`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at generation initialization**:

```javascript
TodoWrite([
  {"content": "📋 ANALYSIS: Analyze todo plans and validate documentation requirements", "status": "pending", "priority": "high", "id": "generate-analysis-1"},
  {"content": "🚀 WAVE1: Execute parallel agent deployment for document creation", "status": "pending", "priority": "high", "id": "generate-wave1-1"},
  {"content": "🔗 WAVE2: Build comprehensive cross-reference integration network", "status": "pending", "priority": "high", "id": "generate-wave2-1"},
  {"content": "✅ WAVE3: Execute quality validation with comprehensive audit", "status": "pending", "priority": "medium", "id": "generate-wave3-1"},
  {"content": "🔄 RECOVERY: Monitor and execute error recovery with targeted corrections", "status": "pending", "priority": "medium", "id": "generate-recovery-1"}
])
```

**Wave-Progressive Todos**: Add stage-specific todos as each wave completes with quality gate validation

### Execution Framework
**3-Wave Strategy**: Parallel creation → Cross-reference integration → Quality validation

**Core Protocol**:
1. **WAVE 1**: Deploy specialized agents per document (parallel execution)
2. **WAVE 2**: Build bidirectional cross-reference network
3. **WAVE 3**: Execute comprehensive quality validation with `/docs-audit`

**Progress Tracking**: Real-time notifications with agent status, completion metrics, and quality gates

**Error Recovery**: Automatic failure detection with targeted correction agents and retry logic

## ⚡ Triggers

### Input Triggers
**Context**: Todo lists containing documentation creation plans
**Previous**: `/start` → documentation workflow detection → `/docs-generate`
**Keywords**: generate, create, documentation, todo, plans

### Output Triggers
**When**: Generation complete → `/docs-audit` for quality validation
**When**: Quality issues → Recursive correction with targeted agents
**When**: Success achieved → Documentation ready for integration
**Chain**: generate → validate → (correct if needed) → complete

### Success Patterns
**Generation Success**: All documents created with template compliance
**Integration Success**: Cross-reference network established with >99% accuracy
**Quality Success**: Combined score ≥85% with no critical failures

## 🔗 See Also

### Implementation Details
- `../docs/implementation/docs-generate-implementation.md` - Complete 3-wave execution framework and integration protocols

### Related Commands
- Execute `/docs-workflow` for complete documentation optimization pipeline
- Execute `/docs-audit` for comprehensive quality assessment and validation
- Execute `/start` for discovery workflow and systematic analysis
- Execute `/think-layers` for complex plan analysis and optimization strategies

### System Integration
- Integrates with `/docs-workflow` as Phase 0 generation step
- Uses `/docs-audit` for quality validation and metrics assessment
- Follows standards for LLM-optimized documentation creation
- Implements anti-bias protocols for neutral content generation

---

**CRITICAL**: This command specializes in todo-to-docs conversion and integrates seamlessly with existing documentation workflow for complete optimization pipeline.