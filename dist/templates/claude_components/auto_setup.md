# Auto-Setup Behavior

Automatic context structure creation for new projects.

## First Run Detection
If context/ directory doesn't exist, automatically:
1. Create minimal context structure
2. Generate core context files from global templates
3. Initialize project-specific TRUTH_SOURCE.md
4. Set up user-vision/ directory for knowledge capture

## Structure Creation
**Auto-create these directories and files:**
```
context/
├── TRUTH_SOURCE.md                    ← Project authority source
├── operational/
│   ├── patterns/
│   │   ├── socratic_methodology.md   ← Mayeutic dialogue framework
│   │   ├── authority_framework.md    ← Decision authority structure
│   │   ├── simplicity_principles.md  ← Simplicity enforcement rules
│   │   └── documentation_style.md    ← Documentation standards
│   ├── behaviors/
│   │   ├── orchestration_protocol.md ← Orchestration methodology
│   │   └── discovery_execution_flow.md ← Discovery workflow patterns
│   └── enforcement/
│       ├── anti_patterns.md          ← Anti-pattern detection
│       ├── behavioral_enforcement.md ← Behavioral compliance
│       └── quality_gates.md          ← Quality validation
└── system/
    └── templates/                     ← Template directory
user-vision/                           ← Knowledge capture area
```

---

**Auto-deployment**: This system automatically creates its required context structure on first use.