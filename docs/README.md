# Documentation Directory

**Purpose**: Comprehensive documentation system with topic-based organization.

## Directory Structure

### Active (`/active/`)
**Current Specifications** - Active documentation (≤150 lines per file)
- System specifications
- Current implementation guides
- Active standards and policies
- Working procedures

### Implementation (`/implementation/`)
**Detailed Implementation Guides** - Comprehensive technical documentation
- Step-by-step implementation guides
- Architecture deep dives
- Integration documentation
- Technical specifications

### Standards (`/standards/`)
**Consolidated Standards** - Development and operational standards
- Development standards
- Documentation standards
- Quality standards
- Compliance requirements

### Reference (`/reference/`)
**Cross-Reference Matrices** - Navigation and relationship documentation
- Cross-reference indexes
- Dependency matrices
- Navigation guides
- System maps

## Legacy Structure Integration

**Existing Directories** (preserved):
- `commands/` - Command implementation documentation
- `context/` - Context system documentation
- `core/` - Core architecture documentation
- `frameworks/` - Framework specifications
- `templates/` - Document templates
- `vision/` - System philosophy

## File Organization Rules

**Markdown Files** (.md):
- Active specs: `/active/` (≤150 lines)
- Detailed guides: `/implementation/` (no size limit)
- Standards: `/standards/` (consolidated)
- References: `/reference/` (indexes and matrices)

**Size Guidelines**:
- Active documentation: ≤150 lines (progressive disclosure)
- Implementation guides: Comprehensive (detailed)
- Standards: Consolidated (authoritative)
- References: Structured (navigable)

## Navigation Patterns

**Predictable Locations**:
- Current specs: `docs/active/{topic}-spec.md`
- Implementation: `docs/implementation/{system}-implementation.md`
- Standards: `docs/standards/{domain}-standards.md`
- References: `docs/reference/{topic}-index.md`

**Progressive Disclosure**:
1. Start with active specifications
2. Refer to implementation guides for details
3. Check standards for requirements
4. Use references for navigation

## Topic Categories

**Core Topics**:
- Architecture and system design
- Command system and orchestration
- Performance and optimization
- Quality and validation
- Learning and evolution

**Integration Points**:
- **Commands**: Implementation docs for executable commands
- **Automation**: Technical guides for scripts and systems
- **Templates**: Reusable documentation patterns
- **Standards**: Authoritative requirements