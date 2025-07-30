# Template Selection Guide

**30/07/2025 15:45 CDMX** | README template decision matrix and usage guide

## TEMPLATE DECISION MATRIX

### Primary Classification Questions

**Question 1: What is the component's primary function?**
- **Knowledge/Authority Hub** → `core_component_template.md`
- **Directory Organization** → `specialized_directory_template.md`  
- **Historical Preservation** → `archive_component_template.md`
- **Multi-Component Coordination** → `integration_hub_template.md`

**Question 2: How many other components does it connect to?**
- **0-2 connections** → `core_component_template.md` or `specialized_directory_template.md`
- **3-5 connections** → `specialized_directory_template.md` or `integration_hub_template.md`
- **6+ connections** → `integration_hub_template.md`

**Question 3: What type of content does it primarily contain?**
- **Living, evolving knowledge** → `core_component_template.md`
- **Organized file collections** → `specialized_directory_template.md`
- **Historical/archived content** → `archive_component_template.md`
- **Cross-references and coordination** → `integration_hub_template.md`

## TEMPLATE USAGE EXAMPLES

### Core Component Template
**Best for**: methodology.md, authority.md, simplicity.md, patterns.md
**Characteristics**:
- Contains authoritative knowledge that evolves
- Has L1-L2-L3 hierarchical structure
- Includes enforcement and operational patterns
- Serves as single source of truth for domain

**Example indicators**:
- File contains user quotes and supreme authority declarations
- Has methodological frameworks and protocols
- Includes enforcement patterns and anti-patterns
- Evolution happens through user vision changes

### Specialized Directory Template  
**Best for**: data/, claude_code/, resources/, research/
**Characteristics**:
- Manages organized collections of related files
- Has clear subdirectory categorization
- Provides navigation and placement guidance
- Serves specific system functions

**Example indicators**:
- Contains multiple subdirectories with different purposes
- Has semantic placement decision trees
- Provides content categorization frameworks
- Manages file organization and access patterns

### Archive Component Template
**Best for**: context/archive/, conversations_processed/, legacy/
**Characteristics**:
- Preserves historical content with ongoing value
- Maintains authority and context from original sources
- Provides access to historical decisions and evolution
- Cannot be eliminated due to preservation requirements

**Example indicators**:
- Contains content from previous system states
- Preserves historical context and decision rationale
- Maintains authority chain from original sources
- Provides reference value for current system operation

### Integration Hub Template
**Best for**: @context/architecture/core/truth-source.md, CLAUDE.md, components with 6+ cross-references
**Characteristics**:
- Coordinates multiple component interactions
- Manages complex information flows
- Orchestrates system-wide behaviors
- Serves as central coordination point

**Example indicators**:
- Referenced by many other components
- Contains coordination protocols and orchestration patterns
- Manages authority flow between multiple components
- Serves as dispatcher or central intelligence hub

## CUSTOMIZATION GUIDELINES

### Template Adaptation Process
1. **Select base template** using decision matrix
2. **Identify component-specific sections** that need customization
3. **Adapt authority chain** to match actual component relationships
4. **Customize integration points** based on actual connections
5. **Modify content criteria** to match component's specific function
6. **Add specialized sections** unique to the component's domain

### Common Customizations

**Authority Chain Variations**:
- Direct VISION.md authority: `VISION.md → component.md`
- Through TRUTH_SOURCE: `VISION.md → @context/architecture/core/truth-source.md → component.md`
- Directory authority: `parent_authority → directory/ → subdirectory/`
- Integration authority: `multiple_sources → integration_hub → coordination`

**Content Structure Variations**:
- **Flat organization**: Single level content with cross-references
- **Hierarchical organization**: L1-L2-L3 structured authority levels
- **Categorical organization**: Content organized by type or function
- **Temporal organization**: Content organized by time or evolution phase

**Integration Pattern Variations**:
- **Hub pattern**: Many components connect to this one
- **Chain pattern**: Sequential connection through multiple components
- **Network pattern**: Complex many-to-many relationships
- **Hierarchical pattern**: Parent-child authority relationships

## QUALITY VALIDATION CHECKLIST

### All Templates Must Include:
- [ ] **Date and timezone** in header
- [ ] **Authority chain declaration** appropriate to component
- [ ] **Clear purpose statement** explaining component function
- [ ] **Content criteria** defining what belongs in component
- [ ] **Integration points** showing relationships to other components
- [ ] **Navigation guidance** for finding and using content
- [ ] **Evolution guidelines** for how component grows and changes

### Component-Specific Requirements:

**Core Component Template**:
- [ ] User quotes preserving original authority
- [ ] L1-L2-L3 hierarchical structure
- [ ] Enforcement patterns and anti-patterns
- [ ] Revolutionary/advanced pattern sections

**Specialized Directory Template**:
- [ ] Subdirectory organization with purposes
- [ ] Semantic placement decision tree
- [ ] Content categorization framework
- [ ] Integration points with related components

**Archive Component Template**:
- [ ] Historical period organization
- [ ] Preservation rationale for content
- [ ] Authority source maintenance
- [ ] Access protocols for archived content

**Integration Hub Template**:
- [ ] Primary and secondary connections
- [ ] Coordination protocols and triggers
- [ ] Information flow management
- [ ] Orchestration patterns and evolution

### File Size and Structure:
- [ ] **≤80 lines maximum** per template (excluding content)
- [ ] **Reference-only architecture** avoiding content duplication
- [ ] **Cross-reference format** using → file.md:line-range syntax
- [ ] **Authority preservation** throughout template structure

## AUTOMATION GUIDANCE

### Semi-Automatic README Creation Process
1. **Component Analysis**: Identify component type and connections
2. **Template Selection**: Use decision matrix to select appropriate template
3. **Placeholder Population**: Fill in component-specific information
4. **Authority Mapping**: Trace and document authority relationships
5. **Integration Discovery**: Identify and document all component connections
6. **Content Audit**: Validate content against criteria and quality checklist
7. **Cross-Reference Generation**: Create appropriate cross-reference links

### Template Maintenance Integration
- **Template evolution** tracked through architecture/templates/ directory
- **Quality standards** updated through standards.md authority
- **Cross-reference formats** maintained through architecture standards
- **Authority chain validation** automated through template structure

---

**TEMPLATE AUTHORITY**: Templates serve user vision through structured component documentation
**SELECTION EFFICIENCY**: Decision matrix enables rapid template selection based on component characteristics  
**QUALITY ASSURANCE**: Validation checklist ensures consistent quality across all README implementations