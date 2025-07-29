# Infrastructure Components

Core components of the export system for distributing the command system.

## 1. Export Script (`scripts/export_commands.py`)
**Purpose**: Intelligently processes commands from `.claude/commands/` to create portable versions

**Features**:
- Removes ce-simple specific references
- Cleans up timestamps and location data
- Converts specific context paths to generic ones
- Maintains command functionality while making them universal
- Processes 27+ command files automatically

**Usage**:
```bash
python3 scripts/export_commands.py
```

## 2. Export Directory (`export/`)
**Purpose**: Contains the complete portable command system ready for distribution

**Structure**:
```
export/
├── README.md              # Distribution overview
├── CLAUDE.md              # Universal dispatcher
├── install.sh             # Installation script
├── commands/              # Complete command library (27+ commands)
├── docs/                  # Complete documentation
│   ├── command_reference.md
│   ├── customization_guide.md
│   └── quick_start.md
└── validate_export.py     # Validation script
```

## 3. Distribution Package (`scripts/create_distribution.sh`)
**Purpose**: Creates ready-to-ship .tar.gz packages with checksums

**Output**: `dist/claude-command-system-1.0.0.tar.gz`

**Usage**:
```bash
bash scripts/create_distribution.sh
```

---

**Next**: distribution_workflow.md for the complete distribution process.