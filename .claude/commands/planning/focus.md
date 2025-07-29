# /planning:focus - Layer Focus Management

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

### Current Focus Display
```
🎯 Current Focus: Layer [X] - [Layer Description]

📋 Layer Scope:
  • [Scope item 1]
  • [Scope item 2]  
  • [Scope item 3]

✅ Completed in this layer:
  • [Completed item 1]
  • [Completed item 2]

⏳ Current work:
  • [Active item 1] - [Status/progress]
  • [Active item 2] - [Status/progress]

🎯 Next priorities:
  • [Priority item 1]
  • [Priority item 2]
```

### Focus Change Validation

#### Forward Movement (Higher Layer)
**Gate requirement:** Must pass /planning:gate validation first
**Block advancement:** If gate criteria not met, explain requirements
**Auto-gate:** Option to run gate validation automatically

#### Backward Movement (Lower Layer)  
**Warning:** Confirm intention to return to previous layer
**Context:** Explain potential reasons (fixing foundation, addressing debt)
**Tracking:** Record focus change for project history

#### Lateral Focus (Same Layer)
**Scope clarification:** If layer has multiple focus areas
**Priority shift:** Change emphasis within current layer
**Progress preservation:** Maintain tracking of current work

## Layer-Specific Focus Areas

### Ce-Simple Focus Areas
**Layer 1 (Completed):** Context maturation, authority establishment
**Layer 2 (Current):** System crystallization, file size compliance, command optimization
**Layer 3 (Future):** Distribution readiness, export framework

### Web-App Focus Areas
**Layer 1:** Database schema, architecture decisions, data modeling
**Layer 2:** API development, business logic, authentication system
**Layer 3:** Frontend components, user interface, state management
**Layer 4:** Testing, deployment, performance optimization

### CLI-Tool Focus Areas
**Layer 1:** Core business logic, data structures, algorithm design
**Layer 2:** Command interface, argument parsing, help system
**Layer 3:** Configuration management, environment handling, validation
**Layer 4:** Packaging, installation, documentation, distribution

## Spontaneous Development Guard

### Cross-Layer Change Detection
**Trigger:** Work item affects different layer than current focus
**Warning:** "This change affects Layer [X], currently focused on Layer [Y]"
**Options:**
- Continue if isolated change
- Defer if significant dependency impact  
- Change focus if appropriate

### Validation Questions
```
🔍 Cross-Layer Change Detected:

Current Focus: Layer [Y] - [Description]
Proposed Change: [Change description]
Affects Layer: [X] - [Impact description]

Options:
1. Continue (isolated change, minimal impact)
2. Defer (significant dependencies, handle later)  
3. Change focus to Layer [X] (if appropriate)
4. Cancel (reconsider approach)

Your choice: [1-4]
```

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

### Focus Timer (Optional)
**Time tracking:** Optional layer focus duration tracking
**Productivity insight:** Understand time allocation across layers
**Switch frequency:** Monitor focus change patterns

### Focus Breadcrumbs
**Recent focuses:** Show last 3 focus changes with timestamps
**Switch rationale:** Display reasons for focus changes
**Pattern recognition:** Identify common focus switching patterns

## Error States
- **No project initialized:** Prompt to run `/planning:init [type]`
- **Invalid layer number:** Show available layers with current status
- **Focus on completed layer:** Confirm intention, suggest current layer alternatives

---
**Authority:** Layer focus methodology + spontaneous development guard system  
**Integration:** → /planning:layers, /planning:gate, /planning:status