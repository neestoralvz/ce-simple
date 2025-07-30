# User Experience Architecture

**30/07/2025 15:45 CDMX** | Conversation-first design and interaction patterns

## PURPOSE
Define user experience architecture following core vision: "conversation natural que de esa conversación natural salga el resultado" - natural conversation-driven results.

## COMPONENT ORGANIZATION

### `/conversation-patterns/` - Conversation Design
**Purpose**: Natural dialogue patterns and conversation flows
**Content**: Socratic patterns, discovery flows, interaction design

### `/interface-design/` - Interface Architecture  
**Purpose**: System interface design and interaction models
**Content**: CLI patterns, semantic triggers, response formats

### `/user-experience/` - Experience Design
**Purpose**: End-to-end user experience and journey design
**Content**: User workflows, experience optimization, accessibility

### **COMPONENT DECISION FLOWCHART SYSTEM** (NEW)

#### `component-decision-flowchart.md` - Visual Decision Authority
**Purpose**: Visual decision tree for systematic content placement with authority validation
**Content**: Mermaid flowcharts, decision logic, quality gates, authority validation checkpoints
**Integration**: ←→ COMPONENT_DECISION_MATRIX.md + CROSS_REFERENCE_SYSTEM.md + CLAUDE.md semantic triggers

#### `interactive-placement-guide.md` - Step-by-Step Decision Support  
**Purpose**: Detailed interactive guidance for complex placement decisions
**Content**: Pathway-specific guidance, classification wizards, implementation strategies, error handling
**Integration**: ↑ component-decision-flowchart.md + ←→ COMPONENT_DECISION_MATRIX.md + ← All components

#### `placement-quick-reference.md` - Rapid Decision Support
**Purpose**: One-page ultra-compact placement guidance for rapid decisions
**Content**: Instant classification matrix, semantic trigger keywords, emergency protocols
**Integration**: ↑ component-decision-flowchart.md + ↑ interactive-placement-guide.md + ← CLAUDE.md

#### `flowchart-system-integration.md` - Integration Protocol Authority
**Purpose**: Comprehensive integration protocol connecting flowchart system with existing architecture
**Content**: CLAUDE.md integration, COMPONENT_DECISION_MATRIX.md enhancement, system-wide protocols
**Integration**: → All flowchart components + ←→ All system architecture + ← CLAUDE.md

#### `flowchart-validation-protocol.md` - Testing and Evolution Framework
**Purpose**: Systematic validation and continuous improvement protocol for flowchart effectiveness
**Content**: Multi-phase testing, empirical validation, user experience measurement, evolution protocols
**Integration**: ↑ flowchart-system-integration.md + Validation across all flowchart components

## CONTENT CRITERIA
**Belongs here:**
- User interaction patterns and conversation design
- Interface architecture and semantic trigger systems
- Experience optimization and user journey mapping
- Accessibility and usability architectural decisions
- **Content placement decision guidance and systematic placement protocols**
- **Visual decision support and interactive placement assistance**
- **Flowchart systems for UX decision acceleration**

**Exclusions:**
- Technical implementation (goes to @architecture/standards/)
- Command-specific UX (stays in commands/)
- Content formatting (goes to @context/standards.md)
- **Authority definitions (stays in @context/authority.md)**
- **Technical patterns (stays in @context/architecture/patterns.md)**

## NAMING CONVENTIONS
Format: `[interaction-type]-[pattern-name].md`
Examples:
- `dialogue-socratic-discovery.md`
- `interface-semantic-triggers.md`
- `experience-progressive-disclosure.md`

## INTEGRATION REFERENCES

### ← vision/
**Connection**: Vision-driven UX architecture serves discovered user vision through natural interaction
**Protocol**: UX patterns must manifest vision discoveries through conversation-first design

### ←→ @context/methodology.md
**Connection**: Socratic discovery and conversation methodology integration
**Protocol**: UX patterns implement methodology through natural conversation flows

### ↑ @context/authority.md
**Authority Source**: User-centric behaviors and authority validation drive UX decisions
**Protocol**: All UX architecture serves user authority supremacy and vision preservation

### → @architecture/workflows/
**Connection**: UX patterns inform process integration and workflow design
**Protocol**: User experience architecture guides implementation workflow optimization

---
**UX AUTHORITY**: Natural conversation architecture serves user vision supremacy