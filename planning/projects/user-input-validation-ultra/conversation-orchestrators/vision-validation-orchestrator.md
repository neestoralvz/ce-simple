# Vision Validation Orchestrator

**Purpose**: Parallel analysis of user vision files through 8 sub-agents for comprehensive validation  
**Command**: `/start-vision-validation`  
**Authority**: user-input/vision/ (Sacred User Space)  
**Type**: Self-contained Task Tool orchestrator  
**Lines**: ≤80

## Command Definition

```
/start-vision-validation - Deploy 8 parallel sub-agents to analyze user vision files for consistency, completeness, and implementation alignment
```

## Parallel Sub-Agent Deployment

### Agent 1: Core Mission Analysis
**Target**: user-input/vision/core-mission-concept.md
**Task Tool Prompt**:
```
Analyze user-input/vision/core-mission-concept.md for:
1. Mission clarity and specificity
2. Differentiator uniqueness and technical feasibility
3. System purpose alignment with VDD framework
4. Philosophy consistency with parallel-first operation
5. Success metrics measurability and achievability

Report findings with specific quotes and technical assessment.
```

### Agent 2: Command Philosophy Validation
**Target**: user-input/vision/command-philosophy-user.md
**Task Tool Prompt**:
```
Analyze user-input/vision/command-philosophy-user.md for:
1. Command design principles technical soundness
2. Self-containment requirements feasibility
3. User interface simplicity vs sophistication balance
4. Orchestration philosophy implementation clarity
5. Learning system integration possibilities

Report alignment with core mission and technical constraints.
```

### Agent 3: Development Methodology Assessment
**Target**: user-input/vision/development-methodology-user.md
**Task Tool Prompt**:
```
Analyze user-input/vision/development-methodology-user.md for:
1. Development workflow practical applicability
2. Vision-driven approach implementation strategy
3. Continuous learning integration mechanisms
4. Quality assurance framework completeness
5. Evolution methodology technical foundation

Report methodology viability and implementation requirements.
```

### Agent 4: Autonomous Systems Evaluation
**Target**: user-input/vision/autonomous-systems-user.md
**Task Tool Prompt**:
```
Analyze user-input/vision/autonomous-systems-user.md for:
1. Autonomy levels technical achievability
2. Human oversight integration requirements
3. Decision-making framework implementation
4. Error recovery system sophistication
5. Learning system autonomous evolution

Report technical feasibility and development complexity.
```

### Agent 5: Global System Architecture
**Target**: user-input/vision/global-system-user.md
**Task Tool Prompt**:
```
Analyze user-input/vision/global-system-user.md for:
1. Cross-domain integration architecture
2. Scalability framework technical design
3. System interconnection protocols
4. Performance optimization strategies
5. Global coordination mechanisms

Report architectural soundness and implementation pathway.
```

### Agent 6: Application Evolution Framework
**Target**: user-input/vision/application-evolution-user.md
**Task Tool Prompt**:
```
Analyze user-input/vision/application-evolution-user.md for:
1. Evolution strategy technical implementation
2. Adaptation mechanisms automation level
3. User feedback integration systems
4. Performance improvement protocols
5. Feature development methodology

Report evolution framework completeness and automation potential.
```

### Agent 7: Communication Documentation Strategy
**Target**: user-input/vision/communication-documentation-user.md
**Task Tool Prompt**:
```
Analyze user-input/vision/communication-documentation-user.md for:
1. Documentation strategy implementation clarity
2. User communication protocol effectiveness
3. Progress reporting system design
4. Transparency requirement technical delivery
5. Documentation automation possibilities

Report communication framework technical viability.
```

### Agent 8: Vision Integration Synthesis
**Target**: All vision files cross-analysis
**Task Tool Prompt**:
```
Perform cross-analysis of all user-input/vision/ files for:
1. Internal consistency across vision documents
2. Technical requirement integration completeness
3. Implementation priority identification
4. Conflict resolution between competing requirements
5. Missing elements or gaps in vision coverage

Report integration assessment and implementation roadmap.
```

## Individual Agent Reporting Protocol

**Requirement**: Each agent MUST report individual findings before synthesis
**Format**: Direct agent output → user visibility → integration analysis
**Quality Gate**: No synthesis until all 8 agents report complete analysis

## Integration Synthesis Protocol

### Phase 1: Individual Analysis Collection
- Collect all 8 agent reports
- Verify completeness of analysis coverage
- Identify critical findings and recommendations

### Phase 2: Cross-Agent Pattern Analysis
- Identify consistency patterns across agents
- Flag conflicting requirements or assessments
- Synthesize technical feasibility consensus

### Phase 3: Implementation Roadmap Generation
- Priority ranking of vision elements
- Technical complexity assessment
- Resource requirement estimation
- Development timeline projection

## Expected Deliverables

1. **Individual Agent Reports**: 8 detailed vision file analyses
2. **Consistency Matrix**: Cross-vision alignment assessment
3. **Technical Feasibility Report**: Implementation viability analysis
4. **Priority Implementation Roadmap**: Development sequence recommendation
5. **Gap Analysis**: Missing vision elements identification
6. **Risk Assessment**: Technical and strategic risk identification

## Success Metrics

- **Coverage**: 100% of vision files analyzed
- **Depth**: Technical feasibility assessed for all major components
- **Integration**: Cross-vision consistency validated
- **Actionability**: Clear implementation priorities identified
- **Transparency**: Individual agent work visible to user

---

**Orchestration Truth**: Parallel vision validation through transparent sub-agent deployment