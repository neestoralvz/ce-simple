# Universal DO/DON'T Template Structure

## Template Markdown

```markdown
# [COMPONENT_NAME] - [Function]

**DD/MM/YYYY** | [Brief purpose]

## DO
- [Clear positive behavior/action 1]
- [Clear positive behavior/action 2]  
- [When/how to apply this component]
- [Expected outcomes/results]

## DON'T
- [Clear constraint/prohibition 1]
- [Clear constraint/prohibition 2]
- [Common failure modes to avoid]
- [Anti-patterns that violate system principles]

## Next Action
- **Automatic**: /next:command (when conditions are clear and automatic progression appropriate)
- **Recommended**: /suggested:command (when user choice needed but clear suggestion exists)
- **Context-aware**: Different suggestions based on execution environment
```

## Usage Guidelines

### For Commands (/.claude/commands/)
**DO Section Focus**: 
- Clear execution instructions
- When to EXECUTE methodology
- Behavioral constraints for role/function
- Expected interaction patterns

**DON'T Section Focus**:
- Prohibited behaviors that violate command purpose
- Common execution mistakes
- Anti-patterns that break system coherence
- Boundary violations

### For Documentation Components
- Apply structure consistently across system
- Maintain clarity between positive and negative behaviors
- Include context-aware progression logic
- Preserve system coherence principles