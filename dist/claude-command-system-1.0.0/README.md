# Command System Export

This directory contains the portable command system extracted from ce-simple for distribution to other projects.

## Contents

- `commands/` - Complete command library with dependencies removed
- `CLAUDE.md` - Universal dispatcher configured for any project
- `install.sh` - Installation script for target projects
- `docs/` - Documentation for system usage and customization

## Installation

1. Copy this export folder to your target project
2. Run `./install.sh` to set up the command structure
3. Customize CLAUDE.md with your project-specific context paths
4. Start using the command system with `/workflows:start`

## System Requirements

- Claude Code CLI
- Git repository (recommended)
- Basic directory structure for context organization

## Quick Start

After installation, use:
- `/workflows:start` - Begin any session
- `/roles:orchestrator` - Main coordination role
- `/actions:research` - Research and investigation
- `/workflows:close` - End session with handoff

See `docs/` for complete command reference and customization guide.