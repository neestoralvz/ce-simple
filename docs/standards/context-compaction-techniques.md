# Context Compaction Techniques Standard

**Purpose**: Maximize information density while maintaining clarity  
**Authority**: Context economy principle from handoff 01  
**Line Limit**: 100 lines maximum  
**Navigation**: [System Hub](../navigation/index.md) | [Documentation Standards](../rules/documentation-standards.md) | [Communication Rules](../rules/communication-rules.md)

## Quality Preservation Principle
**PRIORITY**: Content quality & value preservation supersedes line limits | Never eliminate valuable content for compression | When compaction risks content loss → file division required | Maintain semantic integrity as non-negotiable requirement

## Core Techniques

### 1. Header Compression
**Instead of**: Multi-level headers (### Subsection)  
**Use**: Bold inline labels (**Label**:)  
**Example**: `### Global System` → `**Global**:`

### 2. Symbol Substitution
**Replace words with symbols**: and → & | arrow/to → → | less than or equal → ≤ | greater than → >

### 3. Pipe Separation
**Instead of**: Multiple bullet points  
**Use**: Single line with pipes  
**Example**: 
```
- Vision holder
- System architect  
- Standards setter
```
→ `Vision holder | System architect | Standards setter`

### 4. Redundancy Elimination
**Remove unnecessary words**: "Maximum 150 lines" → "≤150 lines" | "Complete project initialization" → "Project initialization" | "Zero marketing language" → "No marketing language"

### 5. Reference Consolidation
**Instead of**: Inline explanations  
**Use**: @path/to/details references  
**Example**: Long PTS explanation → `PTS Framework @docs/core/pts-framework.md`

### 6. List Compaction
**Vertical to horizontal** when items are short:
```
- Ask questions
- Validate principles  
- Document decisions
```
→ `Clarify first | Validate principles | Document decisions`

### 7. Smart Line Breaks
**Combine related content**: Group similar items on same line | Use colons for inline lists | Merge short related sections

## Component Extraction Protocol
**Principle**: Extract reusable or separable content before applying compression | Identify extraction opportunities through structural analysis

### Extraction Criteria Assessment
**Reusability Test**: Content used across multiple contexts → Extract to specialized file
**Structural Independence**: Content functions as standalone unit → Candidate for extraction  
**Volume Impact**: Large content blocks (>15 lines) serving specific purpose → Consider extraction
**Reference Frequency**: Content referenced repeatedly → Extract and centralize access
**Functional Content Protection**: Checklists, validation lists, step-by-step procedures → Extract rather than compact | Preserve clear structure and usability

### Implementation Pattern
**Systematic Process**: Analyze content structure → Apply extraction criteria → Create specialized files → Establish reference links → Validate functionality preservation

## Application Guidelines

### Optimization Priority Order
1. **Component Extraction**: Apply extraction criteria assessment first
2. **Traditional Compaction**: Apply core techniques to remaining content  
3. **File Division**: Final option when extraction + compaction insufficient

### When to Compact
- File approaching line limits | Repetitive structure present | Context saturation risk | Navigation efficiency needed

### When NOT to Compact  
- Complex technical specifications | Critical safety instructions | Legal/compliance requirements | First-time user documentation
- **Checklists & Validation Lists**: Must remain clear and functional | Compaction compromises utility | Extract to separate files if needed

### Content Value Assessment
**High Value (Extract if Reusable)**: Core concepts | Critical procedures | Essential references | Authority definitions | Checklists & validation lists
**Medium Value (Compact First)**: Examples | Explanatory text | Redundant phrasing | Verbose descriptions  
**Low Value (Remove if Needed)**: Marketing language | Unnecessary adjectives | Duplicate information

## Validation
**Checklist**: @docs/validation/context-compaction-checklist.md

## Examples
**Practical Applications**: @docs/examples/compaction-examples.md

## File Division Protocol
**When to Divide**: Quality preservation impossible via compaction | Content serves distinct purposes | Natural separation points exist
**Methodology**: Create specialized files → Maintain hub navigation → Use precise line references → Preserve cross-references

## Success Metrics
**Density Ratio**: ≥2:1 compression without loss | **Comprehension Time**: ≤30% increase | **Reference Efficiency**: ≤3 hops to details | **Maintenance Ease**: Updates still straightforward

## See Also
**[Documentation Standards](../rules/documentation-standards.md)** | **[Communication Rules](../rules/communication-rules.md)** | **[Markdown Standards](../rules/markdown-standards.md)** | **[Import Analysis Methodology](import-analysis-methodology.md)** | **[Context Efficiency Optimization](context-efficiency-optimization.md)** | **[CLAUDE_RULES.md](../../CLAUDE_RULES.md)** | **[System Navigation](../navigation/index.md)**

**Self-Compliance**: This standard demonstrates its own techniques while preserving content quality