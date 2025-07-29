#!/usr/bin/env python3
"""
Intelligent Command Export Script

Processes commands from .claude/commands/ to create portable versions
by removing ce-simple specific references and dependencies.
"""

import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

class CommandExporter:
    def __init__(self, source_dir: str, export_dir: str):
        self.source_dir = Path(source_dir)
        self.export_dir = Path(export_dir)
        self.replacements = self._init_replacements()
        
    def _init_replacements(self) -> Dict[str, str]:
        """Initialize replacement patterns for making commands portable"""
        return {
            # Specific context paths to generic ones
            r'context/user-vision/TRUTH_SOURCE\.md': 'context/TRUTH_SOURCE.md',
            r'user-vision/TRUTH_SOURCE\.md': 'context/TRUTH_SOURCE.md',
            r'context/patterns/orchestrator_methodology\.md': 'context/patterns/orchestrator_methodology.md',
            r'context/principles/authority\.md': 'context/principles/authority.md',
            r'context/patterns/simplicity\.md': 'context/patterns/simplicity.md',
            r'context/enforcement/core_reminders\.md': 'context/enforcement/core_reminders.md',
            
            # Remove specific project references
            r'ce-simple': '[PROJECT_NAME]',
            r'@context/user-vision/': '@context/',
            r'context/operational/': 'context/',
            r'context/system/': 'context/',
            
            # Generic context loading patterns
            r'@context/operational/enforcement/': '@context/enforcement/',
            r'context/roles:research/': 'context/roles/',
            r'context/patterns/documentation_style\.md': 'context/patterns/documentation_style.md',
            r'context/system/templates/': 'context/templates/',
            r'context/operational/patterns/': 'context/patterns/',
            r'context/operational/behaviors/': 'context/patterns/',
            r'context/operational/operations/': 'context/patterns/',
            
            # Remove timestamp and location specifics
            r'\*\*\d{2}/\d{2}/\d{4}.*?\*\*.*?\n': '',
            r'29/07/2025.*?\|.*?\n': '',
            r'CDMX.*?\|': '',
            
            # Make references more generic
            r'context/conversations/': 'context/conversations/',
            r'/handoff/': '/sessions/',
        }
    
    def process_file_content(self, content: str, filename: str) -> str:
        """Process file content to remove specific dependencies"""
        processed = content
        
        # Apply all replacement patterns
        for pattern, replacement in self.replacements.items():
            processed = re.sub(pattern, replacement, processed, flags=re.MULTILINE)
        
        # Remove empty lines created by timestamp removal
        processed = re.sub(r'\n\n\n+', '\n\n', processed)
        
        # Add generic header for exported commands
        if filename.endswith('.md') and not processed.startswith('# '):
            # Extract command name from path for header
            command_name = self._extract_command_name(filename)
            header = f"# {command_name}\n\n"
            processed = header + processed
        
        return processed.strip() + '\n'
    
    def _extract_command_name(self, filename: str) -> str:
        """Extract command name from filename for header"""
        name = Path(filename).stem
        if '/' in filename:
            category = Path(filename).parent.name
            return f"Comando /{category}:{name}"
        return f"Comando {name}"
    
    def copy_command_structure(self):
        """Copy entire command structure with processing"""
        commands_source = self.source_dir / '.claude' / 'commands'
        commands_dest = self.export_dir / 'commands'
        
        if commands_dest.exists():
            shutil.rmtree(commands_dest)
        commands_dest.mkdir(parents=True)
        
        processed_count = 0
        
        for root, dirs, files in os.walk(commands_source):
            # Create corresponding directory structure
            rel_path = Path(root).relative_to(commands_source)
            dest_dir = commands_dest / rel_path
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            for file in files:
                if file.endswith('.md'):
                    source_file = Path(root) / file
                    dest_file = dest_dir / file
                    
                    # Read, process, and write
                    with open(source_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    relative_path = str(Path(root).relative_to(commands_source) / file)
                    processed_content = self.process_file_content(content, relative_path)
                    
                    with open(dest_file, 'w', encoding='utf-8') as f:
                        f.write(processed_content)
                    
                    processed_count += 1
                    print(f"✓ Processed: {relative_path}")
        
        print(f"\n📋 Processed {processed_count} command files")
        return processed_count
    
    def create_universal_claude_md(self):
        """Create universal CLAUDE.md for any project"""
        claude_source = self.source_dir / 'CLAUDE.md'
        claude_dest = self.export_dir / 'CLAUDE.md'
        
        with open(claude_source, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Process for universal use
        universal_content = self.process_file_content(content, 'CLAUDE.md')
        
        # Add configuration section for new projects
        config_section = """
## PROJECT CONFIGURATION

**Important**: After installation, customize these paths for your project:

- Update `context/TRUTH_SOURCE.md` with your project vision
- Customize context loading patterns in REFERENCIAS CONDICIONALES
- Adjust semantic triggers for your domain requirements
- Configure enforcement rules in context/enforcement/

## CONTEXT LOADING STRUCTURE

The system expects this basic structure:
```
context/
├── TRUTH_SOURCE.md           # Project vision and authority
├── patterns/
│   ├── orchestrator_methodology.md
│   ├── simplicity.md
│   └── documentation_style.md
├── principles/
│   └── authority.md
├── templates/
│   └── template_command.md
└── enforcement/
    ├── core_reminders.md
    ├── anti_patterns.md
    ├── behavioral_enforcement.md
    └── quality_gates.md
```

---

"""
        
        # Insert configuration after the header
        lines = universal_content.split('\n')
        insert_pos = 4  # After header and timestamp line
        lines.insert(insert_pos, config_section)
        universal_content = '\n'.join(lines)
        
        with open(claude_dest, 'w', encoding='utf-8') as f:
            f.write(universal_content)
        
        print("✓ Created universal CLAUDE.md")
    
    def create_documentation(self):
        """Create documentation for the exported system"""
        docs_dir = self.export_dir / 'docs'
        docs_dir.mkdir(exist_ok=True)
        
        # Command reference
        self._create_command_reference(docs_dir)
        
        # Customization guide
        self._create_customization_guide(docs_dir)
        
        # Quick start guide
        self._create_quick_start_guide(docs_dir)
        
        print("✓ Created documentation")
    
    def _create_command_reference(self, docs_dir: Path):
        """Create complete command reference"""
        content = """# Command Reference

Complete reference for all available commands in the system.

## Workflows (Major Operations)

### /workflows:start
Begin any session with planning integration and priority-driven options.
- Reads project state and planning documents
- Presents priority-based next steps
- Provides seamless continuity from previous sessions

### /workflows:close
End session with comprehensive handoff preparation.
- Captures session progress and decisions
- Updates planning documents
- Prepares handoff for next session

### /workflows:explore
Comprehensive codebase understanding and analysis.
- Multi-file analysis and pattern recognition
- Architecture investigation
- System behavior mapping

### /workflows:debug
Systematic problem diagnosis and resolution.
- Root cause analysis
- Solution validation
- Fix implementation

### /workflows:distill
Process and synthesize information from conversations or documents.
- Content analysis and summarization
- Pattern extraction
- Structured output generation

### /workflows:maintenance
System health and optimization operations.
- Performance monitoring
- Cleanup operations
- System optimization

## Actions (Specific Tasks)

### /actions:research
Comprehensive research using concurrent web searches and validation.
- Current information gathering with timestamp validation
- Multi-source concurrent research
- Think x4 analysis methodology

### /actions:write
Content creation with quality standards.
- Template-based writing
- Style guide compliance
- Multi-format output

### /actions:build
System building and documentation generation.
- Automated documentation creation
- Template application
- Quality validation

### /actions:git
Git operations with best practices enforcement.
- Intelligent commit message generation
- Branch management
- Repository optimization

### /actions:compact
Information consolidation and optimization.
- Content compression without information loss
- Structure optimization
- Redundancy elimination

### /actions:expand
Detailed elaboration and enhancement.
- Content expansion with maintained quality
- Context enrichment
- Detail augmentation

### /actions:recreate
Clean slate reconstruction following updated guidelines.
- Bias elimination through recreation
- Updated standard application
- Fresh perspective implementation

## Roles (Consultation/Validation)

### /roles:orchestrator
Main coordination role with intelligent delegation.
- Pattern recognition and task routing
- Continuous execution management
- Multi-agent coordination

### /roles:partner
Strategic consultation and decision validation.
- Architecture discussion partner
- Decision impact analysis
- Strategic alignment validation

### /roles:challenge
System validation against over-engineering and anti-patterns.
- Challenge system decisions
- Identify potential issues
- Suggest alternatives

### /roles:research
Specialized research agent with advanced methodologies.
- Concurrent information gathering
- Multi-source validation
- Structured research output

## Methodology Commands

### /methodology:thinkx4
Apply systematic 4-perspective analysis.

### /methodology:parallel_execution
Optimize operations for concurrent execution.

### /methodology:continuous_flow
Ensure uninterrupted execution until completion.

### /methodology:research_first
Apply research-first protocols with temporal validation.

### /methodology:validation_protocol
Systematic validation against project standards.

## Maintenance

### /maintenance:maintain
System health monitoring and optimization.
- Performance analysis
- Structure optimization
- Quality maintenance

## Usage Patterns

### Basic Session Flow
1. `/workflows:start` - Begin with context and priorities
2. Use appropriate commands based on priorities
3. `/workflows:close` - End with handoff preparation

### Research-Heavy Tasks
1. `/actions:research` - Gather current information
2. `/roles:partner` - Validate findings and decisions
3. `/actions:build` - Create documentation or implementation

### System Maintenance
1. `/maintenance:maintain` - Check system health
2. `/roles:challenge` - Validate against anti-patterns
3. `/actions:recreate` - Rebuild components if needed

## Customization

All commands can be customized by:
- Modifying context references in command files
- Adjusting templates and patterns
- Updating validation criteria
- Adding project-specific triggers
"""
        
        with open(docs_dir / 'command_reference.md', 'w') as f:
            f.write(content)
    
    def _create_customization_guide(self, docs_dir: Path):
        """Create customization guide"""
        content = """# Customization Guide

How to adapt the command system for your specific project needs.

## Essential Customizations

### 1. Project Vision (context/TRUTH_SOURCE.md)
This is the most critical file to customize:

```markdown
# [Your Project] Truth Source

## Core Vision
[Define your project's purpose and objectives]

## Authority Framework  
[Define who decides what and how decisions are made]

## Architectural Principles
[Your project's technical and design principles]

## Quality Standards
[What constitutes quality work in your project]
```

### 2. Context Structure
Organize your context directory to match your project needs:

```
context/
├── TRUTH_SOURCE.md           # Your project vision
├── patterns/                 # Your methodology patterns
├── principles/               # Your decision principles  
├── templates/                # Your document templates
└── enforcement/              # Your quality rules
```

### 3. Command Triggers
Customize semantic triggers in CLAUDE.md for your domain:

```markdown
### [Your Domain] Pattern
**Semantic triggers**: [Your specific keywords and contexts]
**Execute**: Task tool → [Your preferred command sequence]
**Validate**: Task tool → [Your validation criteria]
```

## Advanced Customizations

### Command Modification
Edit command files in `.claude/commands/` to:
- Change context references
- Modify methodology steps
- Adjust validation criteria
- Add domain-specific patterns

### New Command Creation
Create new commands by:
1. Adding `.md` file in appropriate category
2. Following existing command structure
3. Defining clear methodology and objectives
4. Adding appropriate context references

### Integration Patterns
Customize how commands integrate:
- Modify context loading patterns
- Adjust validation sequences
- Change delegation strategies
- Update orchestration logic

## Domain-Specific Adaptations

### Software Development
- Emphasize code quality patterns
- Add testing and deployment workflows
- Include architecture validation
- Focus on technical documentation

### Content Creation
- Emphasize style and voice consistency
- Add editorial workflows
- Include publication processes
- Focus on audience-appropriate output

### Research Projects
- Emphasize validation and sourcing
- Add peer review processes
- Include methodology documentation
- Focus on reproducible results

### Business Operations
- Emphasize process optimization
- Add stakeholder communication
- Include decision documentation
- Focus on measurable outcomes

## Quality Assurance

### Validation Checklist
- [ ] All context references point to existing files
- [ ] Command objectives align with project goals
- [ ] Methodology steps are clear and actionable
- [ ] Enforcement rules match project standards
- [ ] Integration patterns work smoothly

### Testing Your Setup
1. Run `/workflows:start` to test basic functionality
2. Try a research task with `/actions:research`
3. Test orchestration with a complex multi-step task
4. Validate quality with `/roles:challenge`
5. Complete a full session with `/workflows:close`

## Maintenance

### Regular Updates
- Review and update TRUTH_SOURCE.md as project evolves
- Adjust command patterns based on usage experience
- Update enforcement rules based on lessons learned
- Refine integration patterns for better efficiency

### Performance Optimization
- Monitor command execution patterns
- Identify frequently used sequences
- Create shortcuts for common workflows
- Optimize context loading for speed

## Support

If you encounter issues:
1. Check that all context files exist and are properly formatted
2. Verify command syntax matches the reference
3. Ensure CLAUDE.md triggers are properly configured
4. Test individual commands before complex workflows

Remember: The system is designed to be organic and adaptive. Start with basic customizations and evolve based on your actual usage patterns.
"""
        
        with open(docs_dir / 'customization_guide.md', 'w') as f:
            f.write(content)
    
    def _create_quick_start_guide(self, docs_dir: Path):
        """Create quick start guide"""
        content = """# Quick Start Guide

Get up and running with the command system in minutes.

## Prerequisites

- Claude Code CLI installed and configured
- Git repository (recommended)
- Basic understanding of Claude conversations

## Installation

1. **Copy the export to your project**:
   ```bash
   cp -r /path/to/export/* /your/project/
   ```

2. **Run the installation script**:
   ```bash
   ./install.sh
   ```

3. **Customize your project vision**:
   Edit `context/TRUTH_SOURCE.md` with your project specifics.

## First Session

### 1. Start Your Session
```
/workflows:start
```
This will:
- Read your project state
- Show current priorities  
- Suggest next steps

### 2. Try a Research Task  
```
/actions:research
```
Ask it to research something relevant to your project to test the concurrent search capabilities.

### 3. Test Orchestration
```
/roles:orchestrator
```
Give it a multi-step task to see the delegation and continuous execution in action.

### 4. End with Handoff
```
/workflows:close  
```
This will capture your session progress for next time.

## Common Workflows

### Research and Document
1. `/actions:research` - Gather information
2. `/roles:partner` - Validate approach
3. `/actions:build` - Create documentation
4. `/workflows:close` - Save progress

### Explore and Analyze
1. `/workflows:explore` - Understand codebase
2. `/roles:challenge` - Validate findings
3. `/actions:write` - Document insights
4. `/workflows:close` - Prepare handoff

### Debug and Fix
1. `/workflows:debug` - Diagnose issues
2. `/actions:research` - Find solutions
3. `/actions:git` - Commit fixes
4. `/workflows:close` - Document resolution

## Key Concepts

### Continuous Execution
Commands execute continuously until completion. No need to confirm each step.

### Parallel Processing
The system uses multiple tools simultaneously when possible for efficiency.

### Think x4 Methodology
Systematic 4-perspective analysis is applied to all decisions and proposals.

### Authority Framework
You provide the vision and requirements; AI handles implementation decisions.

## Troubleshooting

### Commands Not Working
- Check that `.claude/commands/` directory exists
- Verify CLAUDE.md is in your project root
- Ensure context files exist (run install.sh if missing)

### Context References Failing
- Make sure `context/TRUTH_SOURCE.md` exists
- Check that referenced files in commands exist
- Run install.sh to create basic context structure

### Poor Performance
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
"""
        
        with open(docs_dir / 'quick_start.md', 'w') as f:
            f.write(content)
    
    def export(self) -> Dict[str, int]:
        """Execute complete export process"""
        print("🚀 Starting Command System Export...")
        print(f"Source: {self.source_dir}")
        print(f"Export: {self.export_dir}")
        print()
        
        # Create export directory
        self.export_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy and process commands
        processed_commands = self.copy_command_structure()
        
        # Create universal CLAUDE.md
        self.create_universal_claude_md()
        
        # Create documentation
        self.create_documentation()
        
        print(f"\n✅ Export completed successfully!")
        print(f"📁 Export location: {self.export_dir}")
        print(f"📋 Commands processed: {processed_commands}")
        print()
        print("Next steps:")
        print("1. Review the exported system in export/")
        print("2. Test installation with: cd export && ./install.sh")
        print("3. Customize context/TRUTH_SOURCE.md for target projects")
        print("4. Distribute export/ folder to other projects")
        
        return {
            'commands_processed': processed_commands,
            'files_created': 7  # README, install.sh, CLAUDE.md, 3 docs, 1 directory
        }

def main():
    """Main execution function"""
    import sys
    
    # Default paths
    source_dir = "/Users/nalve/ce-simple"
    export_dir = "/Users/nalve/ce-simple/export"
    
    # Allow command line override
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    if len(sys.argv) > 2:
        export_dir = sys.argv[2]
    
    exporter = CommandExporter(source_dir, export_dir)
    results = exporter.export()
    
    return results

if __name__ == "__main__":
    main()