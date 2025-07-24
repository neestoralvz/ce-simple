# start - Project Analysis and Guidance

## Purpose

Analyzes current project context and provides actionable development recommendations through systematic assessment and workflow identification.

## Principles

- **Single Responsibility**: Focus on project analysis and guidance only
- **Keep It Simple**: Straightforward assessment without unnecessary complexity
- **Practical Value**: Provide actionable recommendations for development
- **Error Recovery**: Clear fallback strategies for assessment failures

## Execution Process

### Phase 1: Project Context Assessment
Update TodoWrite: Mark "Project Context Assessment" as in_progress

Pre-analysis validation:
```bash
REQUIREMENT_CHECK: Current directory readable | STATUS: check | ACTION: scope_to_minimal
REQUIREMENT_CHECK: LS tool available | STATUS: check | ACTION: manual_guidance_mode  
REQUIREMENT_CHECK: Read tool available | STATUS: check | ACTION: structure_only_mode
```

Execute project analysis (basic first, enhanced as needed):
- Basic: Quick directory scan and project type identification
- Enhanced: Detailed documentation and configuration analysis
- Advanced: Comprehensive maturity assessment and development state evaluation
- Progressive: Deep needs analysis only when complexity detected

Use LS and Read tools to understand project:
- Directory structure analysis (basic functionality always available)
- Configuration file examination (enhanced when files present)
- Documentation review (progressive based on available content)

If project analysis fails:
```
ERROR: Project structure analysis incomplete
CAUSE: Permission denied on <specific_directories>
IMPACT: Guidance will be generic rather than project-specific
RECOVERY: Grant read permissions: 'chmod +r <directories>'
CONTINUE: Analysis based on accessible files and standard patterns
```

Update TodoWrite: Complete previous, mark "Guidance Generation" as in_progress

### Phase 2: Development Guidance Generation
Execute guidance creation (layered recommendations):
- Basic: Essential next steps and common development actions
- Enhanced: Project-specific recommendations based on analysis results
- Advanced: Detailed workflow guidance with command suggestions
- Progressive: Comprehensive development roadmap when complexity warrants

Use analysis results to create guidance:
- Basic recommendation generation (always functional)
- Enhanced project-specific guidance (when analysis provides clear patterns)

If guidance generation fails:
```
ERROR: Project-specific guidance generation failed
CAUSE: Insufficient project information from limited analysis
IMPACT: Recommendations will be generic development patterns
RECOVERY: Resolve analysis errors above for project-specific guidance
CONTINUE: Providing standard development workflow recommendations
```

Update TodoWrite: Complete previous, mark "Command Routing" as in_progress

### Phase 3: Command Routing and Recommendations
Execute command routing (simple to comprehensive):
- Basic: Essential command suggestions (`/init-project` or `/explore-codebase`)
- Enhanced: Context-aware routing based on project analysis
- Advanced: Multiple pathway recommendations with clear decision criteria
- Progressive: Comprehensive workflow guidance only when project complexity detected

Generate routing recommendations:
- Simple decision logic ensuring basic functionality
- Enhanced explanations when clear patterns emerge from analysis

If routing decisions are unclear:
```
ERROR: Command routing ambiguous - multiple equally valid paths
CAUSE: Project characteristics match multiple workflow patterns
IMPACT: Cannot provide specific command recommendation
RECOVERY: User selection required - options presented with decision criteria
CONTINUE: Presenting all viable options with selection guidance
```

Update TodoWrite: Complete all analysis tasks


---

## Shared Pattern Integration

**TodoWrite Orchestration**: 3-phase standardized tracking (Assessment → Guidance → Routing)
**Error Recovery**: Fallbacks to basic analysis and generic recommendations with user guidance
**Progressive Enhancement**: Basic directory analysis first, enhanced guidance added based on complexity
**Tool Integration**: LS and Read tools with consistent validation and error handling
**Context Reference**: Vision document alignment ensuring consistent system guidance

---

@./docs/core/README.md
@./docs/core/system-principles.md
@./docs/core/shared-patterns.md

**Single Responsibility**: Simple project analysis and development guidance providing practical recommendations with shared pattern compliance ensuring excellent principle adherence.