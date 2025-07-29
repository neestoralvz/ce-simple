# Distribution Workflow

Step-by-step process for distributing the command system.

## Step 1: Generate Export
```bash
# From ce-simple project root
python3 scripts/export_commands.py
```

This will:
- Process all 27+ commands removing specific dependencies
- Create universal CLAUDE.md dispatcher
- Generate complete documentation
- Create installation script

## Step 2: Validate Export
```bash
# Validate the export structure
cd export && python3 validate_export.py
```

## Step 3: Create Distribution Package
```bash
# Create distributable package
bash scripts/create_distribution.sh
```

This creates:
- `dist/claude-command-system-1.0.0.tar.gz` - Complete package
- `dist/claude-command-system-1.0.0.sha256` - Checksum verification

## Step 4: Distribute
Recipients get the `.tar.gz` file and can install with:

```bash
# Extract package
tar -xzf claude-command-system-1.0.0.tar.gz

# Install to their project
cd claude-command-system-1.0.0
./install.sh

# Customize for their project
# Edit context/TRUTH_SOURCE.md

# Start using
/workflows:start
```

---

**Next**: cleaning_conversion.md for details on what gets processed during export.