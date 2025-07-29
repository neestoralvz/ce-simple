# Troubleshooting

Common issues and solutions for the command system.

## Commands Not Working
- Check that `.claude/commands/` directory exists
- Verify CLAUDE.md is in your project root
- Ensure context files exist (run install.sh if missing)

## Context References Failing
- Make sure `context/TRUTH_SOURCE.md` exists
- Check that referenced files in commands exist
- Run install.sh to create basic context structure

## Poor Performance
- Ensure your TRUTH_SOURCE.md is well-defined
- Check that validation rules are clear
- Consider simplifying complex command sequences

## Next Steps

1. **Customize** `context/TRUTH_SOURCE.md` with your specific project vision
2. **Adjust** command patterns in `.claude/commands/` for your domain
3. **Configure** CLAUDE.md triggers for your use cases
4. **Practice** with different command combinations
5. **Evolve** the system based on your usage patterns

## Tips for Success

- Start with simple tasks to learn the system
- Trust the continuous execution - don't interrupt flows
- Use `/workflows:start` at the beginning of each session
- Always end with `/workflows:close` for proper handoff
- Customize gradually based on actual usage
- Remember: the system adapts to your narrative and workflow

The system is designed to feel like natural conversation that leads to results. The more you use it, the more it will adapt to your specific needs and patterns.