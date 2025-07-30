# /planning:focus - Layer Focus Management

**LOAD:** /modules:planning_focus_templates + /methodology:analysis

**29/07/2025 16:30 CDMX** | Set and track current construction layer focus

## Function
Set, check, or change current layer focus for development work.

## Usage
```bash
/planning:focus                    # Show current focus layer
/planning:focus [layer-number]     # Set focus to specific layer
/planning:focus next              # Advance to next layer (if gate passed)
/planning:focus check             # Detailed focus analysis
```

## Focus Management

### Current Focus Display → /modules:planning_focus_templates

### Focus Change Validation → /modules:planning_focus_templates

## Layer-Specific Focus Areas → /modules:planning_focus_templates

## Spontaneous Development Guard → /modules:planning_focus_templates

## Integration Points

### Project State Tracking
**Current focus storage:** Update context/planning/current.md with focus changes
**Progress preservation:** Maintain work item tracking across focus changes
**History logging:** Record focus change rationale and timing

### Cross-Command Coordination
**Layer highlighting:** Coordinate with /planning:layers to highlight current focus
**Gate preparation:** Connect to /planning:gate for advancement readiness
**Status integration:** Sync with /planning:status for overall view

## Advanced Focus Features

## Core Function
Set, track, and validate layer focus with cross-layer change detection and gate validation

**Features**: Current focus display + focus change validation + spontaneous development guard + layer-specific templates

## Error States
- **No project initialized:** Prompt to run `/planning:init [type]`
- **Invalid layer number:** Show available layers with current status
- **Focus on completed layer:** Confirm intention, suggest current layer alternatives

---
**Authority:** Layer focus methodology + spontaneous development guard system  
**Integration:** → /planning:layers, /planning:gate, /planning:status