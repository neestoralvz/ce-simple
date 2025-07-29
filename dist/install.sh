#!/bin/bash

# Command System Installation Script
# Installs the portable command system to target project

set -e

echo "🚀 Installing Command System..."

# Create directory structure
echo "📁 Creating directory structure..."
mkdir -p .claude/commands/{actions,workflows,roles,maintenance,methodology,validations}
mkdir -p context/{patterns,principles,templates,enforcement}

# Copy commands
echo "📋 Installing commands..."
cp -r commands/* .claude/commands/

# Install CLAUDE.md dispatcher
echo "⚙️ Installing dispatcher..."
cp CLAUDE.md ./

# Create basic context structure if it doesn't exist
if [ ! -f "context/TRUTH_SOURCE.md" ]; then
    echo "📝 Creating basic context structure..."
    
    cat > context/TRUTH_SOURCE.md << 'EOF'
# Project Truth Source

This file should contain your project's vision, principles, and decision authority.

## Core Vision
[Define your project's core vision and objectives]

## Authority Framework
[Define decision-making authority and domains]

## Architectural Principles
[Define your project's architectural guidelines]

## Quality Standards
[Define quality expectations and validation criteria]

---
**Note**: This is a template. Customize it with your project-specific content.
EOF

    cat > context/patterns/orchestrator_methodology.md << 'EOF'
# Orchestrator Methodology

Basic orchestration patterns for task delegation and coordination.

## Core Principles
- Delegate complex tasks via Task tool
- Execute continuously until completion
- Use parallel tools when possible
- Validate results systematically

---
**Note**: This is a basic template. Expand with project-specific patterns.
EOF

    cat > context/principles/authority.md << 'EOF'
# Authority Framework

Decision domains and authority structure for the project.

## Decision Domains
- User Domain: Vision, requirements, acceptance criteria
- AI Domain: Implementation, optimization, execution

---
**Note**: Customize with your project's authority structure.
EOF

    cat > context/patterns/simplicity.md << 'EOF'
# Simplicity Principles

Guidelines for maintaining system simplicity and avoiding over-engineering.

## Core Principle
Beauty lies in simplicity - natural conversation leading to results.

---
**Note**: Define your project's simplicity standards.
EOF

    cat > context/enforcement/core_reminders.md << 'EOF'
# Core Reminders

Fundamental methodologies that must always be applied.

## Think x4 Methodology
Always apply systematic 4-perspective analysis before conclusions.

## Continuous Execution
Never pause for confirmations during task execution flows.

## Parallel Tools
Use concurrent tools when information is independent.

---
**Note**: Customize enforcement rules for your project.
EOF

fi

# Make scripts executable
chmod +x install.sh

echo "✅ Command System installed successfully!"
echo ""
echo "Next steps:"
echo "1. Customize context/TRUTH_SOURCE.md with your project vision"
echo "2. Review and adjust CLAUDE.md references if needed"
echo "3. Start using the system with: /workflows:start"
echo ""
echo "📖 See docs/ for complete customization guide"