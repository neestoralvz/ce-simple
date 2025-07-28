---
contextflow:
  purpose: "Inter-command communication protocols for self-contained ecosystem"
  core-utility: true
  internal-use: true
  research-driven: true
---

# Inter-Command Protocol - Ecosystem Communication

## Self-Containment Principle
**Commands solo pueden conectarse entre sí - NO external file access outside /commands/**

## Communication Patterns

### Command Chaining
```
/create-doc → /align-doc → /verify-doc
/extract-insights → /process-layer  
/start → [dynamic-command-selection]
```

### Information Passing
```
Command A Output → Command B Input
Via: Structured data format + context preservation
Method: Direct parameter passing + shared context files
```

### Context Sharing
```
Self-contained command ecosystem - NO external file dependencies
Internal references within /.claude/commands/ only
Shared utilities via embedded templates and context
```

## Internal Ecosystem Structure

```
/.claude/commands/
├── [commands].md (executable commands)
├── templates/ (subagent templates)
├── utilities/ (shared functions)
├── context/ (shared context)
└── protocols/ (communication standards)
```

### Shared Utilities Access
```
Embedded utilities within command files
Self-contained functionality - no external references
Scope: Command-specific tools integrated directly
```

### Context Repository
```
/.claude/commands/context/
├── decision-trees.md (optimization metadata)
├── efficiency-metrics.md (performance tracking)
├── user-voice-index.md (voice preservation reference)
└── system-state.md (current architecture status)
```

## Communication Standards

### Command Output Format
```markdown
---
output-type: "[data|context|command-suggestion]"
target-command: "[next-command-in-chain]"
context-preserved: "[user-voice|decisions|state]"
---

## Output Data
[Structured information for next command]

## Context Handoff
[Preserved context for continuity]

## Next Steps
[Suggested command chain continuation]
```

### Error Handling Protocol
```
Error Type: [command-failure|context-missing|invalid-input]
Recovery Action: [retry|fallback-command|user-intervention]
Context Preservation: [maintain-state|reset|partial-recovery]
Error Logging: Internal ecosystem only
```

### Success Metrics Sharing
```
Performance Data: Efficiency metrics + timing
Quality Scores: Output validation results  
User Satisfaction: Voice preservation accuracy
System Health: Integration coherence status
```

## Self-Contained Decision Making

### Command Selection Logic
```
Input: User request + current context
Analysis: Decision tree optimization
Selection: Most efficient command path
Execution: Subagent orchestration
Measurement: Efficiency tracking
```

### Context Loading Optimization
```
Required Context: Minimal necessary for task
Loading Strategy: Lazy loading + caching
Performance Target: <2s context assembly
Efficiency Metric: Context relevance score
```

### Dependency Management
```
Internal Dependencies: Commands → Templates → Utilities
External Dependencies: PROHIBITED (self-containment violation)
Shared Resources: Via internal ecosystem only
Resource Optimization: Minimal duplication + maximum reuse
```

## Evolution Protocols

### Command Addition
1. **Create** new command following ecosystem standards
2. **Integrate** with existing communication protocols
3. **Test** inter-command compatibility
4. **Update** decision trees + efficiency metrics
5. **Document** integration points + usage patterns

### Command Modification  
1. **Backup** current version (anti-bias preparation)
2. **Modify** preserving communication interface
3. **Validate** integration with ecosystem
4. **Update** shared context + metrics
5. **Monitor** performance impact

### Command Deprecation
1. **Identify** redundant/inefficient commands
2. **Migrate** functionality to consolidated commands
3. **Update** command chains + references
4. **Remove** obsolete components
5. **Optimize** ecosystem efficiency

## Success Criteria

### Communication Effectiveness
- [ ] All inter-command communication via internal protocols
- [ ] Zero external file dependencies outside ecosystem
- [ ] Context preservation accuracy 100%
- [ ] Command chaining success rate >95%

### Ecosystem Integrity
- [ ] Self-contained architecture maintained
- [ ] Shared utilities accessible to all commands
- [ ] Performance optimization continuous
- [ ] Evolution capability preserved

---

**Commands ecosystem operates independently while maintaining seamless interoperability via standardized internal protocols.**