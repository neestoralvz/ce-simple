# p-layers - Display Construction Dependencies

**31/07/2025 00:00 CDMX** | Show current project construction layers and dependencies
**LOAD:** /modules:planning_layers_templates + /methodology:analysis

## Function
Display project construction layers, current status, and dependency relationships.

## Usage
```bash
p-layers           # Show current project layers
p-layers detail    # Show with dependency explanations
```

## Display Format

### Standard View → /modules:planning_layers_templates

### Detail View → /modules:planning_layers_templates

## Status Indicators → /modules:planning_layers_templates

## Context Integration

### Project State Loading
**Source:** context/architecture/core/methodology.md project tracking
**Fallback:** If no project initialized, suggest `p-init`
**Authority:** Reference to project template for layer definitions

## Core Function
Display project construction layers with dependencies, status indicators, and cross-command integration

**Features**: Standard display + detail view + status indicators + project examples + gate integration

## Output Examples → /modules:planning_layers_templates

## Error States
- **No project initialized:** Prompt to run `p-init [type]`
- **Invalid project state:** Suggest running `p-status` for diagnosis
- **Missing template:** Reference to available project types

---
**Authority:** Dependency layers methodology + project template system
**Integration:** → p-init, p-gate, p-focus, p-status