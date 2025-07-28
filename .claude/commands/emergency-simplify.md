# /emergency-simplify - Immediate Over-Engineering Resolution

## PURPOSE
Execute immediate simplification of over-engineered system components. Implements Phase 1 of SIMPLICITY_PROTOCOL.md.

## CRITICAL ACTIONS

### 1. Command Consolidation (60+ → 15)
```bash
# Delete redundant session-close variants
rm .claude/commands/session-close-analysis.md
rm .claude/commands/session-close-direct.md  
rm .claude/commands/session-close-git.md
rm .claude/commands/session-close-subagent.md
# Keep only: session-close.md

# Delete redundant document workflow commands
rm .claude/commands/align-doc-architecture.md
rm .claude/commands/align-doc-completion.md
rm .claude/commands/align-doc-voice.md
rm .claude/commands/verify-doc-completion.md
rm .claude/commands/verify-doc-quality.md
rm .claude/commands/verify-doc-voice.md
# Keep only: create-doc.md, edit-doc.md, align-doc.md, verify-doc.md

# Delete orchestration setup commands
rm .claude/commands/setup-coordination-protocols.md
rm .claude/commands/setup-mayeutic-engine.md
rm .claude/commands/setup-orchestrator-core.md
rm .claude/commands/setup-specialist-spawning.md
rm .claude/commands/setup-voice-preservation.md
# Merge essential setup into start.md
```

### 2. Template Reduction (30+ → 10)
```bash
# Keep essential templates only
cd .claude/commands/templates/
KEEP_TEMPLATES=(
    "research-specialist.md"
    "content-optimizer.md" 
    "quality-assurance.md"
    "architecture-validator.md"
    "voice-preservation.md"
)

# Move to archive folder
mkdir -p archive/over-engineered-templates/
for file in *.md; do
    if [[ ! " ${KEEP_TEMPLATES[@]} " =~ " ${file} " ]]; then
        mv "$file" archive/over-engineered-templates/
    fi
done
```

### 3. Monitoring Tool Cleanup (15+ → 3)
```bash
# Keep essential monitoring only
cd tools/
KEEP_TOOLS=(
    "monitoring/system-health.py"
    "monitoring/dashboard.py"
    "launchers/start_health_monitor.sh"
)

# Archive excessive monitoring
mkdir -p archive/over-engineered-monitoring/
find . -name "*.py" -o -name "*.sh" | while read file; do
    if [[ ! " ${KEEP_TOOLS[@]} " =~ " ${file} " ]]; then
        mv "$file" archive/over-engineered-monitoring/
    fi
done
```

### 4. CLAUDE.md Simplification
```bash
# Backup current CLAUDE.md
cp CLAUDE.md CLAUDE-over-engineered-backup.md

# Create simplified version (50 lines max)
cat > CLAUDE.md << 'EOF'
# CLAUDE.md - Simplified Intelligence System

## AUTHORITY HIERARCHY
1. **SIMPLICITY_PROTOCOL.md** - Supreme anti-over-engineering authority
2. **user_vision/** - User requirements and preferences  
3. **This document** - Basic operational guidelines

## CORE PRINCIPLES
- **Simplicity First**: Simple tasks should be simple
- **Direct Execution**: Use appropriate approach for task complexity
- **User Voice**: Preserve user intent and decisions
- **Practical Results**: Focus on delivering value, not following complex processes

## OPERATIONAL GUIDELINES

### Simple Tasks (Direct Execution)
- File operations (read, write, edit)
- Basic git commands (status, add, commit)
- Simple documentation creation
- Status checks and basic analysis

### Complex Tasks (Specialist Coordination)
- Multi-step technical implementations
- Comprehensive research requiring external knowledge
- Complex system integrations
- Advanced analysis requiring specialized expertise

### Decision Framework
1. **Can this be done in 1-3 simple steps?** → Direct execution
2. **Does this require specialized knowledge/tools?** → Consider specialists
3. **When in doubt** → Choose the simpler approach

## FORBIDDEN PATTERNS
- "ABSOLUTE PROHIBITION" against direct work
- Mandatory orchestration for simple tasks
- Complex coordination protocols for basic operations
- Process worship over productivity

## SUCCESS METRICS
- User tasks completed efficiently
- System remains maintainable
- Complexity stays within reasonable bounds
- Focus on actual work delivery

**Remember**: This system exists to help users get work done, not to demonstrate complex orchestration capabilities.
EOF
```

### 5. Remove Orchestration Mandates
```bash
# Remove workflow enforcement
rm .claude/commands/utilities/workflow-enforcement.md

# Remove orchestration completion protocols  
rm .claude/commands/templates/orchestration-completion-protocol.md

# Archive excessive utilities
mkdir -p .claude/commands/utilities/archive/
mv .claude/commands/utilities/* .claude/commands/utilities/archive/ 2>/dev/null || true
```

## VALIDATION

After execution, verify simplification:
```bash
# Run simplicity check
/simplicity-check

# Verify targets met:
# Commands: <20
# Tools: <5  
# Templates: <10
# Orchestration refs: <100
```

## AUTHORITY
This command has emergency authority to override complex systems and restore operational simplicity per SIMPLICITY_PROTOCOL.md.

**Execute immediately** to restore system usability and prevent further complexity accumulation.