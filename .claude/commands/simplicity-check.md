# /simplicity-check - Anti-Over-Engineering Command

## PURPOSE
Detect and prevent complexity creep in the system. Enforces SIMPLICITY_PROTOCOL.md rules.

## EXECUTION
```bash
# Run comprehensive simplicity analysis
./.claude/hooks/simplicity-enforcement.sh

# Quick complexity metrics
echo "📊 SYSTEM COMPLEXITY SNAPSHOT:"
echo "Commands: $(find .claude/commands -name '*.md' | wc -l)"
echo "Tools: $(find tools -name '*.py' | wc -l)" 
echo "Templates: $(find . -name '*template*' | wc -l)"
echo "Orchestration refs: $(grep -r 'orchestrat' --include='*.md' . | wc -l)"
```

## THRESHOLDS (RED FLAGS)
- Commands: >20 (current: 60+) 
- Tools: >5 (current: 15+)
- Templates: >10 (current: 30+)
- Orchestration refs: >100 (current: 628)

## IMMEDIATE ACTIONS
When thresholds exceeded:
1. **Commands**: Consolidate redundant functionality
2. **Tools**: Remove duplicate monitoring systems  
3. **Templates**: Delete unnecessary abstractions
4. **Orchestration**: Remove mandatory delegation for simple tasks

## FORBIDDEN PATTERNS
- "ABSOLUTE PROHIBITION"
- "Deploy specialist via Task tools" for simple operations
- Mandatory multi-step workflows for basic tasks
- Complex coordination protocols

## AUTHORITY
This command enforces SIMPLICITY_PROTOCOL.md with supreme authority over complexity prevention.

Use regularly to maintain system simplicity and prevent over-engineering recurrence.