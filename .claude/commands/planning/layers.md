# /planning:layers - Display Construction Dependencies

**LOAD:** /modules:planning_layers_templates + /methodology:analysis

**29/07/2025 16:20 CDMX** | Show current project construction layers and dependencies

## Function
Display project construction layers, current status, and dependency relationships.

## Usage
```bash
/planning:layers           # Show current project layers
/planning:layers detail    # Show with dependency explanations
```

## Display Format

### Standard View → /modules:planning_layers_templates

### Detail View → /modules:planning_layers_templates

## Status Indicators → /modules:planning_layers_templates

## Context Integration

### Project State Loading
**Source:** context/planning/current.md project tracking
**Fallback:** If no project initialized, suggest `/planning:init`
**Authority:** Reference to project template for layer definitions

## Core Function
Display project construction layers with dependencies, status indicators, and cross-command integration

**Features**: Standard display + detail view + status indicators + project examples + gate integration

## Output Examples → /modules:planning_layers_templates

## Error States
- **No project initialized:** Prompt to run `/planning:init [type]`
- **Invalid project state:** Suggest running `/planning:status` for diagnosis
- **Missing template:** Reference to available project types

---
**Authority:** Dependency layers methodology + project template system
**Integration:** → /planning:init, /planning:gate, /planning:focus, /planning:status