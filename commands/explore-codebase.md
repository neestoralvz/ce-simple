# explore-codebase

## Purpose

Analyze project structure, identify coding patterns, and document architectural insights.

## Principles

- **Single Responsibility**: Codebase analysis only - no modification or external research
- **Direct Analysis**: Sequential tool usage without orchestration overhead  
- **Technical Precision**: Specific file types, patterns, and architectural elements
- **Error Recovery**: Scope reduction with clear continuation paths

## Execution Process

### Phase 1: Project Structure Analysis
Analyze directory structure and file organization:

Pre-execution validation:
```bash
REQUIREMENT_CHECK: Directory traversal permissions | STATUS: check | ACTION: set_scope_level
```

Use LS to examine directories:
```bash
# Root structure
ls -la
# Source directories 
find . -type d -name "src" -o -name "lib" -o -name "components"
# Configuration files
find . -name "*.json" -o -name "*.yaml" -o -name "*.toml" -o -name "*.config.*"
```

Document findings:
- Directory organization patterns
- File naming conventions
- Technology stack indicators
- Project scale and complexity

If directory access fails:
```
ERROR: Directory analysis incomplete - <count> directories inaccessible
CAUSE: Permission denied: <specific_directory_list>
IMPACT: Project structure understanding limited to accessible areas
RECOVERY: Grant permissions: 'chmod +r <directories>' for complete analysis
CONTINUE: Analysis proceeding with directories: <accessible_list>
```

### Phase 2: Code Pattern Analysis  
Identify coding conventions and architectural patterns:

Pre-execution validation:
```bash  
REQUIREMENT_CHECK: File read permissions | STATUS: check | ACTION: set_analysis_depth
```

Use Grep to search for patterns:
```bash
# Import/export patterns
grep -r "import\|export\|require" --include="*.js" --include="*.ts"
# Function definitions
grep -r "function\|const.*=\|class " --include="*.js" --include="*.ts" --include="*.py"
# API endpoints
grep -r "GET\|POST\|PUT\|DELETE\|@app.route" --include="*.py" --include="*.js"
```

Use Read to examine key files:
- Package.json, requirements.txt, Cargo.toml
- Main entry points (index.js, main.py, app.py)
- Configuration files
- Documentation files

Document patterns:
- Coding style and conventions
- Architectural patterns used
- Dependencies and tech stack
- API design patterns

If pattern analysis fails:
```
ERROR: Code pattern search incomplete
CAUSE: <specific_error: permission/file_not_found/grep_failure>
IMPACT: Coding convention analysis limited
RECOVERY: <specific_recovery_steps_based_on_cause>
CONTINUE: Pattern analysis based on available files: <file_list>
```

### Phase 3: Architecture Documentation
Generate comprehensive codebase summary:

Create analysis report with:
1. **Project Overview**: Technology, scale, purpose
2. **Structure Analysis**: Directory organization, file patterns
3. **Code Conventions**: Style patterns, naming, architecture
4. **Technical Stack**: Dependencies, frameworks, tools
5. **Development Insights**: Potential improvements, patterns to follow

Final validation with completeness reporting:
```
ANALYSIS_COMPLETENESS:
- Structure Analysis: <percentage>% complete
- Pattern Analysis: <percentage>% complete  
- Stack Analysis: <percentage>% complete
- Gaps Identified: <specific_missing_elements>
- Confidence Level: <high/medium/low>

RECOVERY_NEEDED:
- For complete analysis: <specific_steps>
- For pattern enhancement: <specific_steps>
- For architecture validation: <specific_steps>
```

---

## Implementation Standards

**Single Responsibility**: Codebase analysis only - structure, patterns, and documentation
**Tool Usage**: Direct LS, Grep, and Read calls without orchestration
**Error Handling**: Scope reduction with specific limitation reporting
**Output**: Structured analysis report with actionable development insights

**Authority References**:
@./docs/core/development-principles.md
@./docs/vision/overview.md