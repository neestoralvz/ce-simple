# Problem Solving - Analysis Command

## Purpose
Universal methodology for systematic problem resolution through structured diagnosis, comprehensive research, and progressive analysis leading to executable solution plans.

## Principles and Guidelines

**Single Responsibility**: Focus exclusively on problem analysis without solution implementation or execution
**Granular Analysis**: Break problem resolution into small, manageable analysis steps
**Research Management**: Clear investigation phases with explicit validation requirements
**Error Recovery**: Built-in analysis failure handling and methodology adjustment protocols

## Execution Process

### Phase 1: Problem Structural Assessment
Update TodoWrite: Mark "Problem structural assessment" as in_progress

Execute pre-solution structural mapping:
- Use Grep to find problem context and error patterns in codebase
- Use Glob to identify domain-specific files related to problem
- Map problem domain scope and affected components
- Document structural constraints and system dependencies

Use Grep for problem pattern detection:
- Search for error keywords and failure patterns across files
- Identify constraint and limitation references
- Extract existing solution attempts and outcomes
- Validate problem scope completeness

Generate structural assessment baseline:
- Document problem domain analysis and scope
- Record affected components and dependencies
- Identify structural constraints and limitations
- Assess risk factors and potential failure modes

### Phase 2: Comprehensive Internal Discovery
Update TodoWrite: Complete previous, mark "Internal context discovery" as in_progress

Execute comprehensive internal research:
- Use Task Tool executing `/explore-codebase` for internal context discovery
- Focus exploration on problem domain and related components
- Gather existing documentation and implementation patterns
- Identify internal resources and potential solutions

Analyze internal findings:
- Extract relevant patterns and existing approaches
- Identify successful implementations and best practices
- Document internal constraints and limitations
- Validate internal context completeness

### Phase 3: External Research and Validation
Update TodoWrite: Complete previous, mark "External research execution" as in_progress

Execute external research coordination:
- Use Task Tool executing `/explore-web` for external solution research
- Research industry best practices and standard approaches
- Gather expert recommendations and proven solutions
- Cross-validate external findings with internal context

Synthesize external research results:
- Document external solution patterns and approaches
- Identify applicable solutions for current context
- Assess external solution feasibility and constraints
- Validate research completeness and quality

### Phase 4: Multi-Layer Analysis and Solution Development
Update TodoWrite: Complete previous, mark "Solution analysis and development" as in_progress

Execute progressive analysis:
- Use Task Tool executing `/think-layers` for deep problem analysis
- Apply multi-layer thinking to solution development
- Generate solution alternatives and evaluation criteria
- Develop comprehensive solution strategy

Generate solution patterns and recommendations:
- Use Grep to extract solution and success patterns from research
- Analyze effective approaches and implementation strategies
- Document solution options with feasibility assessment
- Validate solution approaches against problem constraints

Use Write tool to document solution plan:
- Create comprehensive executable solution plan
- Document step-by-step implementation approach
- Include rollback procedures and risk mitigation
- Specify success criteria and validation methods

If analysis issues detected:
- Add TodoWrite task: "Resolve analysis gap: [specific issue]"
- Re-execute problematic analysis phases with adjustments
- Validate resolution approach before proceeding
- Document lessons learned for methodology improvement

Update TodoWrite: Complete all problem analysis tasks
Add follow-up: "Problem analysis complete with executable solution plan ready"

---

**Single Responsibility**: Analysis focused exclusively on systematic problem investigation and solution strategy development.**