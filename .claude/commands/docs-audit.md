# /docs-audit - Documentation System Audit

**Purpose**: Automated audit of docs/ structure for duplications, broken references, and organizational issues  
**Authority**: Auto-maintenance command for docs/ system health  
**Target**: Developers maintaining the VDD documentation system

## Principles

**PTS Compliance**: 12/12 component validation focusing on directness (≤3 steps), precision (100% accurate detection), sufficiency (complete audit coverage), and effectiveness (actionable results).

**Parallel Detection**: Deploy 8-12 concurrent agents across different audit dimensions for comprehensive system analysis.

**Self-Contained Logic**: All audit logic, validation patterns, and detection algorithms embedded inline.

## Execution Process

### Phase 0: Root Directory Validation (1 minute)
Deploy rapid audit agents for root directory cleanliness:

**Agent 0: Root Directory Scanner**
```yaml
Task: "Scan root directory for files that don't belong and classify their proper location"
Scope: "Project root directory"
Focus:
  - Identify files beyond essential: CLAUDE.md, CLAUDE_RULES.md, README.md, mkdocs.yml
  - Detect backup files (*.txt, *-backup.*, docs-structure-*)
  - Find misplaced documentation or planning files
  - Catalog temporary or analysis files that should be relocated
  - Check for uncommitted configuration or tool files
Output: "Root directory compliance report with relocation recommendations"
→ **INDIVIDUAL REPORT TO USER**: Agent 0 will report root directory audit directly to you before synthesis
```

### Phase 1: Structure Analysis (2 minutes)
Deploy parallel agents for comprehensive structure audit:

**Agent 1-3: Directory Structure Validation**
```yaml
Task: "Analyze docs/ directory structure and validate against established architecture"
Scope: "Project docs/ directory"
Focus: 
  - Verify core/, standards/, templates/, governance/ as essential directories
  - Detect any recreated analysis/, frameworks/, validation/ directories
  - Identify orphaned directories not referenced in README.md files
  - Check directory naming consistency with VDD standards
Output: "Directory structure compliance report with recommendations"
→ **INDIVIDUAL REPORT TO USER**: Agents 1-3 will report structure analysis directly to you before synthesis
```

**Agent 4-6: Content Duplication Detection**  
```yaml
Task: "Scan all .md files for content duplication patterns using intelligent analysis"
Scope: "Project docs/ directory"
Focus:
  - Compare file content for semantic similarity >80%
  - Detect PTS framework content duplication outside core/
  - Identify redundant validation checklists  
  - Find repeated command patterns across files
  - Check for Spanish content duplication (should be eliminated)
Output: "Duplication analysis with specific file pairs and similarity scores"
→ **INDIVIDUAL REPORT TO USER**: Agents 4-6 will report duplication findings directly to you before synthesis
```

**Agent 7-9: Reference Integrity Validation**
```yaml  
Task: "Validate all internal references and links within docs/ system"
Scope: "Current project docs/ directory"
Focus:
  - Test all path/file.md references for accuracy
  - Check relative/path.md links functionality
  - Verify README.md navigation links work correctly
  - Detect phantom references to deleted directories
  - Validate cross-directory reference patterns
Output: "Reference integrity report with broken links and fixes needed"
→ **INDIVIDUAL REPORT TO USER**: Agents 7-9 will report reference integrity directly to you before synthesis
```

### Phase 2: Quality Gate Analysis (3 minutes)
Deploy specialized audit agents for quality compliance:

**Agent 10-11: Standards Compliance**
```yaml
Task: "Audit documentation compliance with established standards"
Scope: "Project docs/ directory"  
Focus:
  - Verify ≤80 line limits for core/ files
  - Check README.md files exist in essential directories
  - Validate PTS framework authority (single source in core/)
  - Confirm English-only content compliance
  - Check timestamp consistency and update patterns
Output: "Standards compliance audit with specific violations and corrections"
→ **INDIVIDUAL REPORT TO USER**: Agents 10-11 will report standards compliance directly to you before synthesis
```

**Agent 12: CLAUDE.md Reference Integrity**
```yaml
Task: "Validate CLAUDE.md accurately reflects current docs/core/ structure and references"
Scope: "Project root CLAUDE.md and docs/core/ directory"
Focus:
  - Verify all new files in docs/core/ are referenced in CLAUDE.md
  - Check for orphaned references to moved or deleted files
  - Validate navigation paths and authority claims
  - Ensure Section 2 implementation references match actual structure
Output: "CLAUDE.md reference integrity report with required updates"
→ **INDIVIDUAL REPORT TO USER**: Agent 12 will report CLAUDE.md integrity directly to you before synthesis
```

### Phase 3: Optimization Recommendations (2 minutes)
Generate improvement recommendations:

**Integration Analysis**: Cross-reference all audit results to identify systemic issues
**Priority Matrix**: Rank findings by impact (high/medium/low) and effort (quick/moderate/extensive)  
**Action Plan**: Specific recommendations with implementation steps
**Prevention**: Suggested process improvements to prevent future issues

## Error Handling

**Agent Deployment Failures**:
- Fallback: Sequential audit if parallel deployment fails
- Recovery: Retry failed agents with reduced scope
- Alternative: Manual checklist provided for critical validations

**Directory Access Issues**:
- Permission problems: Provide manual verification steps
- Missing directories: Guide recreation with proper structure
- Network issues: Offline audit capabilities with local validation

**Large Repository Performance**:
- Scale down parallel operations if system performance degrades
- Implement progressive audit for repositories >10GB
- Provide sampling methodology for massive codebases

## Success Metrics

**Detection Accuracy**: ≥95% identification of actual issues  
**False Positive Rate**: ≤5% incorrect issue reporting  
**Audit Completion Time**: ≤8 minutes for typical VDD repository (includes root validation)  
**Actionable Results**: 100% findings include specific fix recommendations

---

**Implementation Note**: This command uses real Task Tool parallelization to achieve comprehensive docs/ audit through intelligent agent coordination, providing maintainable documentation architecture for VDD system evolution.