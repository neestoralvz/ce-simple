# Decision Criteria - Complexity Assessment Framework

## 🎯 Purpose
Provide systematic criteria for evaluating request complexity, exploration needs, and analysis depth requirements in discovery workflows.

## 📊 COMPLEXITY ASSESSMENT FRAMEWORK

### Scoring Components (1-10 Scale)
**Total Score = Domain Scope + Technical Depth + Context Requirements + Implementation Steps**

#### Domain Scope (1-3 points)
- **1 point**: Single domain, isolated changes
- **2 points**: Dual domain interaction required
- **3 points**: Multi-domain integration, system-wide impact

#### Technical Depth (1-3 points)  
- **1 point**: Surface-level modifications, existing patterns
- **2 points**: Moderate complexity, some architectural considerations
- **3 points**: Deep architectural changes, new patterns required

#### Context Requirements (1-2 points)
- **1 point**: Self-contained, existing knowledge sufficient
- **2 points**: External knowledge, research, or validation needed

#### Implementation Steps (1-2 points)
- **1 point**: Linear execution, independent steps
- **2 points**: Complex dependencies, ordered execution required

### Complexity Categories
- **Simple (1-3)**: Direct execution, minimal analysis
- **Medium (4-6)**: Moderate analysis, single-domain solutions
- **Complex (7-9)**: Multi-domain analysis, architectural planning
- **Critical (10)**: System-wide impact, comprehensive research

## 🔧 EXPLORATION DECISION MATRIX

### Web Exploration Triggers
**ACTIVATE when**:
- Complexity score ≥7 AND external patterns needed
- Recent technologies (post-2023) involved
- Best practices validation required for critical implementations
- Domain expertise beyond current codebase scope

**SKIP when**:
- Complexity score ≤6 AND local patterns sufficient
- Established technologies with known implementations
- Time-sensitive requests with adequate internal context
- Proven patterns exist within current system

### Agent Deployment Strategy
**PARALLEL Execution**:
- Independent research domains (web + codebase)
- No dependency chain between tasks
- High complexity (≥8) requiring distributed cognitive load
- Multiple pattern sources need simultaneous analysis

**SEQUENTIAL Execution**:
- Analysis dependencies detected (results inform next steps)
- Medium complexity (≤7) manageable by ordered workflow
- Context building requires information hierarchy
- Resource optimization for focused exploration

## ⚡ ANALYSIS DEPTH PROGRESSION

### Think-Layer Advancement Criteria
**Level 1 (Think)**: Basic pattern recognition sufficient
- Simple implementation with clear precedents
- Straightforward problem-solution mapping
- Minimal integration complexity

**Level 2 (Think-Hard)**: Pattern analysis required
- Multiple implementation approaches available
- Integration considerations identified
- Moderate architectural impact

**Level 3 (Think-Harder)**: Complex integration needed
- System-wide pattern implications
- Multiple domain coordination required
- Architectural decision significance

**Level 4 (Ultra-Think)**: Comprehensive planning required
- Critical system changes with broad impact
- Multiple stakeholder considerations
- Long-term architectural implications

### Progression Decision Points
**CONTINUE to Next Level**:
- Current analysis reveals additional complexity
- Integration patterns require deeper understanding
- Multiple solution paths need comprehensive evaluation
- Critical implementation risks require thorough analysis

**SUFFICIENT at Current Level**:
- Request complexity fully addressed
- Clear execution path with manageable risks
- Additional analysis unlikely to improve solution quality
- Time/resource constraints favor execution over analysis

## 📋 QUICK REFERENCE MATRIX

### Complexity Score → Strategy Mapping
- **Score 1-3**: Local exploration → Sequential agents → Level 1-2 analysis
- **Score 4-6**: Mixed exploration → Context-dependent agents → Level 2-3 analysis  
- **Score 7-9**: Full exploration → Parallel agents → Level 3-4 analysis
- **Score 10**: Comprehensive exploration → Distributed agents → Level 4 + validation

### Decision Validation Checkpoints
1. **Complexity Assessment**: Score matches request characteristics
2. **Exploration Strategy**: Approach aligns with information needs
3. **Agent Deployment**: Resource allocation optimizes coverage
4. **Analysis Depth**: Thinking level addresses solution requirements
5. **Execution Readiness**: Clear implementation path identified
6. **File Size Compliance**: Commands ≤140 optimal (200 max), Documentation ≤200 max

---

**CRITICAL**: These criteria provide systematic decision-making framework while maintaining flexibility for edge cases and evolving requirements.