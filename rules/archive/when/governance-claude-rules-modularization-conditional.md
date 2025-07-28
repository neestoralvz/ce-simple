# CLAUDE_RULES Modularization - System Rule

**Updated**: 2025-07-26 | **Authority**: System architecture | **Scope**: CLAUDE_RULES management

## Modularization Protocol

**MANDATORY when CLAUDE_RULES exceeds cognitive load limits**: Extract conditional rules to modular files with conditional loading references.

## When to Apply Modularization

### Triggers for Modularization
- **File length** > 150 lines (cognitive load threshold)
- **Complex conditional logic** with multiple contexts
- **Repeated rule patterns** across different scenarios
- **Context-specific protocols** that don't need always-loading
- **Specialized methodologies** used only in specific situations

### Core vs Modular Rules Distinction

#### Always-Loaded Core (rules/CLAUDE_RULES.md)
**Keep in main file:**
- Core partnership protocol (fundamental AI-user relationship)
- Universal compliance requirements (PTS, English-only, imperative tone)
- Basic orchestration protocol (Task Tool usage)
- Essential quality gates (blocking requirements)
- Authority hierarchy (user-input/ → CLAUDE_RULES → implementation)

#### Conditionally-Loaded Modules (rules/*.md)
**Extract to modular files:**
- Specialized methodologies (planning, content auditing, etc.)
- Context-specific protocols (documentation work, git operations, etc.)
- Complex procedures (multi-step workflows)
- Domain-specific requirements (validation frameworks, etc.)
- Advanced coordination protocols (multi-agent, parallel execution)

## Modularization Process

### Step 1: Content Analysis
1. **Identify conditional sections** - Rules that apply only in specific contexts
2. **Map dependencies** - Which rules reference other rules
3. **Assess frequency** - Which rules are used often vs rarely
4. **Evaluate cognitive load** - Which sections are most complex

### Step 2: Extraction Strategy
1. **Create thematic modules** - Group related conditional rules
2. **Preserve complete context** - Each module is self-contained
3. **Maintain authority references** - Clear hierarchy and sources
4. **Establish loading conditions** - When each module should be loaded

### Step 3: Reference Architecture
**Conditional Loading Pattern:**
```markdown
**IF [condition]** → READ rules/[module-name].md
**IF [condition] + [context]** → READ rules/[module].md:lines-X-Y
```

**Examples:**
```markdown
**IF planning work** → READ rules/planning-methodology.md
**IF content auditing** → READ rules/content-auditing-methodology.md  
**IF documentation work** → READ rules/documentation-first-rule.md
**IF orchestration needed** → READ rules/orchestration-protocols.md
```

### Step 4: Integration Validation
1. **Test conditional loading** - Verify rules load appropriately
2. **Check completeness** - All scenarios have appropriate rules
3. **Validate authority** - Clear hierarchy maintained
4. **Confirm functionality** - System operates correctly with modular architecture

## Modular Architecture Standards

### Module File Standards
- **Single responsibility** - Each module covers one thematic area
- **Complete context** - Module is self-contained and executable
- **Clear authority** - Source and hierarchy explicitly stated
- **Standard format** - Consistent structure across all modules
- **Line limits** - Keep modules ≤100 lines for optimal loading

### Conditional Reference Standards
- **Clear conditions** - Unambiguous when to load each module
- **Specific contexts** - Precise scenarios for rule application
- **Line-level precision** - Reference specific sections when appropriate
- **Logical grouping** - Related conditions grouped together
- **Comprehensive coverage** - All scenarios have appropriate rule coverage

### Integration Standards
- **No circular references** - Modules don't reference each other circularly
- **Clear hierarchy** - CLAUDE_RULES → rules/*.md → implementation
- **Consistent loading** - Same conditions always load same modules
- **Performance optimization** - Minimal cognitive load in always-loaded content

## Quality Validation

### Pre-Modularization Checklist
- [ ] CLAUDE_RULES exceeds cognitive load limits
- [ ] Clear conditional patterns identified
- [ ] Thematic groupings possible
- [ ] Extraction won't break functionality

### Post-Modularization Checklist
- [ ] Core partnership protocol preserved in main file
- [ ] All conditional scenarios have appropriate rule coverage
- [ ] Modules are self-contained and complete
- [ ] References use correct conditional loading format
- [ ] Overall cognitive load reduced while maintaining functionality

### Success Criteria
**Cognitive Load Reduction**: Always-loaded content ≤100 lines
**Functional Completeness**: All scenarios have appropriate rule coverage
**Reference Accuracy**: All conditional loads work correctly
**System Performance**: Faster loading with maintained functionality

## Migration Procedure

### Safe Migration Process
1. **Backup current CLAUDE_RULES** - Preserve original
2. **Create modular files first** - Build modules before modifying main file
3. **Test modules independently** - Verify each module is complete
4. **Update main file gradually** - Replace sections with references incrementally
5. **Validate functionality** - Test system operation after each change
6. **Verify integration** - Confirm all scenarios work correctly

### Rollback Strategy
- **Maintain original backup** - Allow immediate rollback if needed
- **Incremental migration** - Can rollback partial changes
- **Functionality testing** - Validate each step before proceeding
- **Emergency restoration** - Clear procedure for reverting changes

---

**Modularization Truth**: Conditional loading of specialized rules maintains comprehensive guidance while optimizing cognitive load and system performance.