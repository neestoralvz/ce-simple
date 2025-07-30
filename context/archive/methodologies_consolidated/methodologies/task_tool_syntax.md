# Task Tool Syntax - Core Protocol

**29/07/2025 17:30 CDMX** | Essential syntax rules + error prevention

## Required Parameters Protocol
**OBLIGATORIO:** All Task tool calls must include:
```
Task(
  description: "Brief 3-5 word summary",
  prompt: "Detailed instructions with context loading",
  subagent_type: "general-purpose"
)
```

## Parameter Specifications
- **description**: Concise task summary (3-5 words max)
- **prompt**: Detailed instructions including role, context files, methodology
- **subagent_type**: ALWAYS "general-purpose" (only available type)

## Context Loading Protocol

### Mandatory Context References
**Pattern**: All specialized prompts MUST reference specific context files
**Format**: `Load context from context/path/file.md`
**Purpose**: Ensure subagent has required domain knowledge

### Context Path Specifications
- **Authority**: `context/TRUTH_SOURCE.md`
- **Methodology**: `context/operational/patterns/orchestrator_methodology.md`
- **Validation**: `context/operational/patterns/authority_framework.md`
- **Quality**: `context/operational/patterns/simplicity_principles.md`
- **Templates**: `context/system/templates/`

## Error Prevention Protocol

### Common Syntax Errors
- ❌ `Task tool → /roles:research` (slash command syntax)
- ❌ `Task tool → /actions:build` (invalid syntax)
- ❌ Missing subagent_type parameter
- ❌ Invalid subagent types (old slash command references)
- ✅ Proper Task() function with all required parameters

### Correct Task Tool Examples
```
// Research delegation
Task(
  description: "Research investigation",
  prompt: "Act as research specialist. Load context from context/operational/patterns/orchestrator_methodology.md. Conduct systematic investigation using Think x4 methodology. Focus on codebase architecture analysis. Provide insights and recommendations.",
  subagent_type: "general-purpose"
)

// Partner validation
Task(
  description: "Authority validation", 
  prompt: "Act as partner validation specialist. Load context from context/TRUTH_SOURCE.md and context/operational/patterns/authority_framework.md. Challenge architectural decisions using socratic methodology. Verify alignment with user vision and simplicity principles.",
  subagent_type: "general-purpose"
)
```

### Validation Checklist
**Required elements for proper Task tool syntax:**
- ✓ description parameter present (3-5 words)
- ✓ prompt parameter with role definition
- ✓ specific context file references
- ✓ subagent_type: "general-purpose"
- ✓ methodology specification included

## Post-Delegation Validation

### Automatic Second Task Tool
**OBLIGATORIO**: After each major delegation → automatic validation
```
Task(
  description: "Alignment verification",
  prompt: "Verify previous task alignment with context/TRUTH_SOURCE.md and context/operational/patterns/simplicity_principles.md. Validate standards compliance and authority preservation.",
  subagent_type: "general-purpose"
)
```

---
**Authority**: Core syntax definitions for semantic trigger system
**Integration**: → subagent_specialization_patterns.md, orchestration_protocol.md