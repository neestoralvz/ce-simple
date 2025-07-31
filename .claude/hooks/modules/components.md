# Components - Configuration & Scripts Authority

**31/07/2025 CDMX** | Complete component configuration and script details

## AUTORIDAD SUPREMA
hooks/README.md → components.md implements complete components authority per hooks system

## PRINCIPIO FUNDAMENTAL
**"Modular component architecture enabling flexible protection configuration"** - Comprehensive component system with clear separation of concerns.

## SYSTEM COMPONENTS

### **Configuration Components**
- **`project-protection.json`**: Main hook configuration with event definitions and project settings
- **`protection.log`**: System activity log (auto-created)

### **Protection Scripts**
- **`root-protection.sh`**: Root directory protection with intelligent auto-relocation
- **`size-validation.sh`**: File size enforcement with context-aware suggestions
- **`standards-check.sh`**: Standards compliance monitoring and suggestions
- **`authority-validation.sh`**: Authority chain integrity validation

### **Hook Events**
- **`file-write`**: Validates files before creation/modification (root-protection.sh)
- **`user-prompt-submit`**: Pre-conversation standards check (standards-check.sh)
- **`tool-call-complete`**: Post-action validation (size-validation.sh)
- **`session-start`**: Authority validation and context initialization (authority-validation.sh)

## COMPONENT COORDINATION

### **Event-Driven Architecture**
Each component operates through event-driven triggers providing seamless integration with Claude Code workflow while maintaining modular independence.

### **Configuration-Based Control**
Central configuration enables fine-tuned control over all protection components with flexible customization options.

## INTEGRATION REFERENCES
**Authority Source**: ← @../README.md (hooks system authority)
**System Overview**: ← system-overview.md (protection features)
**Operation Guide**: → operation-guide.md (component operation details)

---
**COMPONENTS DECLARATION**: Complete component architecture providing modular protection system with flexible configuration and event-driven coordination.