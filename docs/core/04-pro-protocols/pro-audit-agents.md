# Audit Agents Rule

**Authority**: Modular Rule System  
**Scope**: File generation validation  
**Enforcement**: MANDATORY for bulk operations

## Deployment Triggers
- **File Generation**: >3 files OR >300 total lines
- **Bulk Updates**: >5 file modifications in single operation  
- **Standards Compliance**: PTS framework, line limits, compaction

## Audit Matrix
```yaml
FileType:
  commands: {max_lines: 150, pts_required: 12/12, compaction: extreme}
  docs: {max_lines: 200, pts_required: 10/12, compaction: high}
  config: {max_lines: 100, pts_required: 8/12, compaction: moderate}
ValidationScope:
  structure: [line_count, formatting, syntax, dependencies]
  compliance: [pts_components, naming_standards, english_only]
  efficiency: [token_density, duplication, unnecessary_verbosity]
```

## Agent Deployment Pattern
```bash
# Wave 1: Parallel validation (3-5 agents)
/agent-deploy audit-pts "Validate PTS compliance for [files]"
/agent-deploy audit-lines "Check line limits: commands≤150, docs≤200"  
/agent-deploy audit-compact "Identify compaction opportunities >20%"

# Wave 2: Correction agents (2-3 agents)
/agent-deploy fix-compaction "Apply extreme compaction to [violations]"
/agent-deploy fix-compliance "Correct PTS failures in [components]"
```

## Audit Prompts
**PTS Audit**: "Validate 12 PTS components for [file]. Return: component/status/reason matrix"
**Line Audit**: "Count lines excluding blank/comments. Flag: >150 commands, >200 docs"
**Compaction Audit**: "Identify: redundant comments, verbose patterns, consolidation opportunities"

## Expected Outputs
```yaml
AuditReport:
  file: path/to/file
  pts_score: 11/12  
  line_count: {total: 145, code: 120, comments: 25}
  violations: ["Clarity: complex nested logic", "Conciseness: 30% redundancy"]
  compaction_potential: "25% reduction via pattern consolidation"
  action_required: ["Apply template patterns", "Remove redundant validation"]
```

## References
- **PTS Framework**: @docs/core/pts-framework.md (12 components)
- **Compaction Standards**: @docs/core/compaction-techniques.md
- **Validation Engine**: @export/commands/14-utils/validation-engine.md

**Enforcement**: Deployment failure if audit agents not used for qualifying operations