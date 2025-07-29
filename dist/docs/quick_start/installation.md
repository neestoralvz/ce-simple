# Installation

Set up the command system in your project.

## Prerequisites

- Claude Code CLI installed and configured
- Git repository (recommended)
- Basic understanding of Claude conversations

## Installation Steps

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

## Verification

Run `/workflows:start` to verify installation success. The system should read your project state and suggest next steps.

---

**Next**: first_session.md to begin using the system.