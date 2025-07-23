# PPO-FMEA Standardization Framework  
**Failure Mode and Effects Analysis for All Command Workflows**

## 🎯 Universal FMEA Integration Protocol

### Standard FMEA Matrix Template
**Applied to ALL commands in PPO framework:**

```
┌─────────────────┬─────────────────┬─────────┬─────────┬─────────┬─────────┬──────────────┐
│ Component       │ Failure Mode    │ Severity│ Occur   │ Detect  │ RPN     │ Prevention   │
├─────────────────┼─────────────────┼─────────┼─────────┼─────────┼─────────┼──────────────┤
│ Phase 0         │ Skip Validation │    8    │    5    │    3    │   120   │ Mandatory    │
│ Agent Deploy    │ Load Imbalance  │    6    │    4    │    7    │   168   │ Orchestration│
│ Cross-Refs      │ Broken Links    │    9    │    6    │    4    │   216   │ Matrix-Maint │
│ Context Gen     │ Size Violation  │    7    │    7    │    6    │   294   │ Prog Disclos │
│ Git Integration │ Partial Commit  │    5    │    3    │    8    │   120   │ Auto-Verify  │
└─────────────────┴─────────────────┴─────────┴─────────┴─────────┴─────────┴──────────────┘

RPN = Severity × Occurrence × Detection (1-10 scale each)
Risk Levels: <100 (Low) | 100-200 (Medium) | >200 (High)
```

## 🛡️ Command-Specific FMEA Matrices

### /start - Discovery Workflow FMEA
```
┌─────────────────┬─────────────────┬─────────┬─────────┬─────────┬─────────┬──────────────┐
│ Component       │ Failure Mode    │ S │ O │ D │ RPN     │ Prevention Strategy      │
├─────────────────┼─────────────────┼───┼───┼───┼─────────┼──────────────────────────┤
│ Structural Val  │ Skip Directory  │ 8 │ 3 │ 2 │   48    │ Mandatory LS validation  │
│ Complexity Ass  │ Wrong Strategy  │ 7 │ 4 │ 5 │  140    │ Agent-orchestration req  │
│ Agent Deploy    │ Resource Limit  │ 6 │ 5 │ 7 │  210    │ Load balancing protocol  │
│ Context Suffic  │ Incomplete Info │ 9 │ 6 │ 4 │  216    │ Dynamic question gen     │
│ Workflow Chain  │ Broken Handoff  │ 8 │ 4 │ 6 │  192    │ State tracking mandatory │
└─────────────────┴─────────────────┴───┴───┴───┴─────────┴──────────────────────────┘
Critical Risk: Context Sufficiency (RPN: 216) → Dynamic question generation MANDATORY
```

### /matrix-maintenance - Cross-Reference FMEA  
```
┌─────────────────┬─────────────────┬─────────┬─────────┬─────────┬─────────┬──────────────┐
│ Component       │ Failure Mode    │ S │ O │ D │ RPN     │ Prevention Strategy      │
├─────────────────┼─────────────────┼───┼───┼───┼─────────┼──────────────────────────┤
│ Dependency Scan │ Missing Refs    │ 9 │ 4 │ 3 │  108    │ Comprehensive glob scan  │
│ Matrix Update   │ Corruption      │ 8 │ 3 │ 5 │  120    │ Backup + validation      │
│ Integrity Check │ False Positive  │ 6 │ 6 │ 7 │  252    │ Multi-layer verification │
│ Prevention Gen  │ Incomplete Strat│ 7 │ 5 │ 4 │  140    │ FMEA template mandatory  │
│ Real-time Mon   │ Performance Deg │ 5 │ 7 │ 8 │  280    │ Incremental + caching    │
└─────────────────┴─────────────────┴───┴───┴───┴─────────┴──────────────────────────┘
Critical Risk: Real-time Monitoring (RPN: 280) → Incremental scanning + caching MANDATORY
```

### /docs-workflow - Documentation FMEA
```
┌─────────────────┬─────────────────┬─────────┬─────────┬─────────┬─────────┬──────────────┐
│ Component       │ Failure Mode    │ S │ O │ D │ RPN     │ Prevention Strategy      │
├─────────────────┼─────────────────┼───┼───┼───┼─────────┼──────────────────────────┤
│ Health Audit    │ Inaccurate Calc │ 7 │ 3 │ 4 │   84    │ Multi-metric validation  │
│ Progressive Dis │ Lost Reference  │ 8 │ 4 │ 3 │   96    │ Reference integrity chk  │
│ Size Compliance │ Extraction Fail │ 6 │ 5 │ 6 │  180    │ Backup + rollback        │
│ Recursive Opt   │ Infinite Loop   │ 9 │ 2 │ 7 │  126    │ Max iteration limit (3)  │
│ Validation Gate │ False Threshold │ 8 │ 6 │ 5 │  240    │ Multiple validation pts  │
└─────────────────┴─────────────────┴───┴───┴───┴─────────┴──────────────────────────┘
Critical Risk: Validation Gate (RPN: 240) → Multiple validation points MANDATORY
```

### /problem-solving - Enhanced Analysis FMEA
```
┌─────────────────┬─────────────────┬─────────┬─────────┬─────────┬─────────┬──────────────┐
│ Component       │ Failure Mode    │ S │ O │ D │ RPN     │ Prevention Strategy      │
├─────────────────┼─────────────────┼───┼───┼───┼─────────┼──────────────────────────┤
│ Phase 0 Assess  │ Insufficient Exp│ 9 │ 7 │ 2 │  126    │ 85% exploration threshold│
│ Root Cause Anal │ Surface Analysis│ 8 │ 6 │ 3 │  144    │ Cross-ref matrix required│
│ Solution Arch   │ Missing Deps    │ 7 │ 5 │ 4 │  140    │ FMEA mandatory before sol│
│ Risk Assessment │ Incomplete RPN  │ 6 │ 4 │ 5 │  120    │ Standard RPN calculation │
│ Prevention Plan │ No Mitigation   │ 9 │ 3 │ 6 │  162    │ Mitigation for all >100  │
└─────────────────┴─────────────────┴───┴───┴───┴─────────┴──────────────────────────┘
Critical Risk: Phase 0 Assessment (RPN: 126) → 85% exploration threshold MANDATORY
```

### /think-layers - Progressive Analysis FMEA
```
┌─────────────────┬─────────────────┬─────────┬─────────┬─────────┬─────────┬──────────────┐
│ Component       │ Failure Mode    │ S │ O │ D │ RPN     │ Prevention Strategy      │
├─────────────────┼─────────────────┼───┼───┼───┼─────────┼──────────────────────────┤
│ Depth Selection │ Wrong Layer     │ 7 │ 5 │ 6 │  210    │ Complexity matrix reqd   │
│ Cognitive Load  │ Resource Overld │ 8 │ 6 │ 4 │  192    │ Agent-orchestration mand │
│ Layer Escalation│ Skip Critical   │ 9 │ 4 │ 3 │  108    │ Auto-escalation triggers │
│ Plan Consolidat │ Lost Insights   │ 6 │ 7 │ 5 │  210    │ Progressive capture reqd │
│ Integration     │ Context Loss    │ 8 │ 5 │ 7 │  280    │ State preservation mand  │
└─────────────────┴─────────────────┴───┴───┴───┴─────────┴──────────────────────────┘
Critical Risk: Integration (RPN: 280) → State preservation MANDATORY
```

## 🎯 Universal FMEA Implementation Protocol

### Mandatory FMEA TodoWrite Integration
**ALL commands MUST include:**

```javascript
TodoWrite([
  {"content": "🛡️ FMEA-ANALYSIS: Generate failure mode analysis with RPN calculation", "status": "pending", "priority": "high", "id": "fmea-analysis-1"},
  {"content": "⚠️ RISK-ASSESSMENT: Identify all components with RPN >100 for mitigation", "status": "pending", "priority": "high", "id": "fmea-risk-1"},
  {"content": "🔧 PREVENTION: Implement mitigation strategies for high-risk failure modes", "status": "pending", "priority": "medium", "id": "fmea-prevent-1"}
])
```

### Risk Thresholds & Mitigation Requirements

#### Critical Risk (RPN >200)
- **Action**: MANDATORY mitigation before execution
- **Review**: Architecture-level prevention strategies required
- **Escalation**: System-wide impact assessment needed
- **Examples**: Context loss, real-time monitoring degradation

#### High Risk (RPN 100-200)  
- **Action**: Mitigation strategies implemented
- **Review**: Command-level prevention protocols
- **Monitoring**: Performance tracking for effectiveness
- **Examples**: Resource overload, incomplete exploration

#### Medium Risk (RPN 50-99)
- **Action**: Monitoring and improvement recommendations  
- **Review**: Periodic assessment for trend analysis
- **Documentation**: Track patterns for systematic improvement
- **Examples**: Inaccurate calculations, minor validation issues

#### Low Risk (RPN <50)
- **Action**: Standard operational procedures sufficient
- **Review**: Annual assessment for process improvement
- **Documentation**: Basic logging for trend analysis
- **Examples**: Directory validation, backup procedures

### FMEA Integration Success Metrics

#### Prevention Effectiveness
- **First-Attempt Success**: >90% (target from RPN mitigation)
- **Failure Recurrence**: <3% (prevention effectiveness indicator)  
- **Critical Risk Elimination**: 100% (all RPN >200 mitigated)
- **System Reliability**: >99.5% uptime (overall FMEA effectiveness)

#### Risk Management Performance
- **Risk Coverage**: 100% (all failure modes identified)
- **Mitigation Deployment**: >95% (strategies implemented)
- **Performance Impact**: <10% (FMEA overhead acceptable)
- **Learning Integration**: Failure patterns → prevention improvement

## 🔗 Command Integration Requirements

### Universal FMEA Compliance Checklist
**ALL commands must demonstrate:**

- ✅ **FMEA Matrix Generated**: Command-specific failure modes identified
- ✅ **RPN Calculations**: Severity × Occurrence × Detection for all components  
- ✅ **Risk Thresholds**: Critical (>200), High (100-200), Medium (50-99), Low (<50)
- ✅ **Mitigation Strategies**: Prevention protocols for all risks >100 RPN
- ✅ **TodoWrite Integration**: FMEA tasks embedded in behavioral reinforcement
- ✅ **Performance Monitoring**: Success metrics tracking for prevention effectiveness

### FMEA Audit Protocol
```javascript
function auditFMEACompliance(command) {
  const matrix = validateFMEAMatrix(command);
  const rpn = validateRPNCalculations(command);
  const mitigation = validateMitigationStrategies(command);
  const integration = validateTodoWriteIntegration(command);
  
  return {
    compliance: (matrix && rpn && mitigation && integration),
    score: calculateComplianceScore(command),
    recommendations: generateImprovements(command)
  };
}
```

---

**CRITICAL**: This FMEA standardization ensures systematic prevention-first approach across all command workflows. Every command MUST implement its specific FMEA matrix with mandatory mitigation strategies for risks >100 RPN. This framework operationalizes the user insight that "la prevención proactiva es mucho mejor" through systematic risk management.