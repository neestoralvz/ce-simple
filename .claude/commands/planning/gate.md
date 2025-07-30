# /planning:gate - Layer Advancement Validation

**LOAD:** /modules:planning_gate_templates + /methodology:validation

**29/07/2025 16:25 CDMX** | Validate readiness for next construction layer

## Function
Validate current layer completion and authorize advancement to next layer.

## Usage
```bash
/planning:gate              # Validate current layer readiness
/planning:gate check        # Check without advancing
/planning:gate force        # Override validation (caution!)
```

## Validation Process

### 1. Current Layer Assessment
**Completion criteria check:** Verify all layer requirements met
**Quality validation:** Ensure standards maintained (file sizes, references, etc.)
**Dependency verification:** Confirm foundational elements stable

### 2. Readiness Gate Criteria → /modules:planning_gate_templates

### 3. Advancement Decision → /modules:planning_gate_templates

## Project-Specific Gates → /modules:planning_gate_templates

## Override Options

## Core Function
Validate layer completion criteria and authorize advancement with project-specific quality gates

**Features**: Current layer assessment + readiness gate criteria + advancement decision + project-specific gates + override options

## Error States
- **No project initialized:** Prompt to run `/planning:init [type]`
- **Already at final layer:** Congratulate completion, suggest next steps
- **Invalid layer state:** Suggest `/planning:status` for diagnosis

---
**Authority:** Dependency layers methodology + quality gate enforcement
**Integration:** → /planning:layers, /planning:focus, /planning:status