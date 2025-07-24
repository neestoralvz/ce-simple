# Validator Core - Universal Validation Engine

## Purpose
Universal validation engine extracted from enhanced-start, matrix-maintenance, and docs-maintain commands to centralize structure validation, integrity checks, cross-reference validation, and quality assessment protocols.

## Principles and Guidelines

**Single Responsibility**: Focus exclusively on validation operations without execution or implementation
**Granular Validation**: Break validation into specific, measurable validation steps  
**Quality Enforcement**: Clear threshold validation with explicit compliance requirements
**Error Recovery**: Built-in validation failure handling and re-validation protocols

## Execution Process

### Phase 1: Directory Structure Validation
Update TodoWrite: Mark "Directory structure validation" as in_progress

Execute comprehensive structure validation:
- Use LS tool to validate docs/ directory exists and is accessible
- Use LS tool to verify commands/ directory structure and organization
- Use LS tool to confirm context/ directory presence and integrity
- Use LS tool to check system component directories and accessibility

Validate directory organization patterns:
- Map directory hierarchy and component relationships
- Identify primary system boundaries and structural interfaces
- Document directory types and categorization patterns
- Assess structural completeness and organization compliance

Calculate structure completeness using embedded validation:
```bash
expected_dirs="docs commands context"
found_dirs=$(ls -1d docs commands context 2>/dev/null | wc -l)
structure_score=$(echo "scale=1; $found_dirs * 100 / 3" | bc)
```

### Phase 2: File Integrity Validation  
Update TodoWrite: Complete previous, mark "File integrity validation" as in_progress

Execute systematic file integrity checks:
- Use Glob tool to discover all system files requiring validation
- Use Read tool to validate file accessibility and content integrity
- Use Grep tool to identify structural markers and validation patterns
- Assess file completeness and content quality metrics

Validate file integrity patterns:
- Check file accessibility and read permissions
- Verify content structure and formatting compliance
- Identify corrupted or incomplete files requiring attention
- Document file integrity status and quality metrics

Calculate file integrity using systematic assessment:
```bash
total_files=$(find . -name "*.md" | wc -l)
accessible_files=$(find . -name "*.md" -readable | wc -l)  
integrity_score=$(echo "scale=1; $accessible_files * 100 / $total_files" | bc)
```

### Phase 3: Cross-Reference Validation
Update TodoWrite: Complete previous, mark "Cross-reference validation" as in_progress

Execute comprehensive cross-reference analysis:
- Use Grep tool to identify markdown link patterns and references
- Use Grep tool to find command invocations and system references
- Use Grep tool to discover configuration dependencies and connections
- Map all cross-reference relationships and validate targets

Validate reference integrity and accessibility:
- Verify link targets exist and are accessible using LS tool
- Identify broken references and missing dependencies
- Document reference patterns and relationship types
- Assess cross-reference completeness and coverage metrics

Calculate cross-reference validity using pattern analysis:
```bash
total_refs=$(grep -r "\[.*\](.*\.md)" . | wc -l)
valid_refs=$(grep -r "\[.*\](.*\.md)" . | while read ref; do 
  target=$(echo $ref | sed 's/.*(\(.*\.md\)).*/\1/')
  [[ -f "$target" ]] && echo 1
done | wc -l)
reference_score=$(echo "scale=1; $valid_refs * 100 / $total_refs" | bc)
```

### Phase 4: Quality Assessment and Reporting
Update TodoWrite: Complete previous, mark "Quality assessment and reporting" as in_progress

Execute comprehensive quality threshold validation:
- Calculate overall system completeness using aggregated metrics
- Assess compliance against quality thresholds (>85% target)
- Generate detailed validation report with specific findings
- Document validation recommendations and improvement actions

Generate validation metrics and assessment:
- Combine structure, integrity, and reference scores
- Calculate weighted quality assessment score
- Validate against compliance thresholds and standards
- Generate comprehensive validation summary and recommendations

Perform final validation assessment:
```bash
overall_score=$(echo "scale=1; ($structure_score + $integrity_score + $reference_score) / 3" | bc)
compliance_status=$(echo "$overall_score >= 85" | bc)
```

If validation threshold fails (score <85%):
- Add TodoWrite task: "Resolve validation failure: [specific issue]"  
- Generate detailed failure analysis and remediation plan
- Document specific actions required for compliance achievement
- Schedule re-validation with enhanced protocols and standards

Update TodoWrite: Complete all validation engine tasks
Add follow-up: "Universal validation complete with comprehensive quality assessment"

---

**Single Responsibility**: Validation focused exclusively on systematic quality assessment, structural integrity, and compliance threshold enforcement.**