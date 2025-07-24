# Modular Rule System Architecture

**Last Updated: 2025-07-23**

## Purpose

Design for splitting CLAUDE_RULES.md into specialized rule modules for better maintainability, focused responsibility, and continuous evolution. Each module handles specific aspects of the partnership protocol while maintaining coherent integration.

## Current State Analysis

**CLAUDE_RULES.md (179 lines)** contains:
- Partnership definition and roles (25 lines)
- Communication protocols (15 lines)  
- Development methodology (45 lines)
- STP compliance framework (20 lines)
- Project structure governance (35 lines)
- Development workflow (25 lines)
- Evolution and metrics (14 lines)

## Modular Architecture Design

### Rule Module Categories

#### 1. Partnership Protocol (`rules/partnership-protocol.md`)
**Scope**: Core partnership definition and role boundaries
**Content**:
- Partnership Definition (Your Role vs My Role)
- Core Mission and Objective
- Interaction Standards
- Success Metrics for Partnership

**Size Estimate**: ~60 lines

#### 2. Communication Rules (`rules/communication-rules.md`)
**Scope**: All communication protocols and context management
**Content**:
- Language standards (English-only)
- Communication style requirements (direct, technical, no marketing)
- Question protocols and clarification procedures
- Context management strategies
- Model selection guidance
- Transparency requirements

**Size Estimate**: ~45 lines

#### 3. Development Standards (`rules/development-standards.md`)
**Scope**: Technical implementation requirements and quality frameworks
**Content**:
- Line limits (150 commands, 200 docs)
- Autocontained principle
- Single responsibility enforcement
- STP/PTS 12-component framework
- Quality gates and validation

**Size Estimate**: ~70 lines

#### 4. Tool Usage Protocols (`rules/tool-usage-protocols.md`)
**Scope**: Task Tool optimization and execution patterns
**Content**:
- Task Tool priority and parallel execution defaults
- Think x4 methodology integration
- Wave-based deployment strategies
- Context economy principles
- Token optimization guidelines

**Size Estimate**: ~50 lines

#### 5. Project Governance (`rules/project-governance.md`)
**Scope**: Structure maintenance and file organization
**Content**:
- Directory authority hierarchy
- File management rules
- Command system architecture
- Structure integrity enforcement

**Size Estimate**: ~55 lines

#### 6. Evolution and Learning (`rules/evolution-learning.md`)
**Scope**: System growth and continuous improvement
**Content**:
- Rule updating protocols
- Pattern capture mechanisms
- Learning integration processes
- System scaling strategies
- Backward compatibility requirements

**Size Estimate**: ~40 lines

### New Rules Integration

#### Rules from Recent Conversation
1. **Model Selection Rule**: Clear guidance on when to use different models
2. **Transparency Rule**: Full disclosure of approach and decision-making
3. **Token Economy Rule**: Optimize for context efficiency without sacrificing quality
4. **Rule Update Protocol**: Continuous addition of new rules from insights
5. **Error Resolution Rule**: Systematic debugging with visual validation
6. **Pattern Storage Rule**: Internal timestamp logging (not filename timestamps)
7. **Vision Authority Rule**: docs/vision/ as absolute decision authority

### Integration Strategy

#### Master Rule Registry (`CLAUDE_RULES.md` → `rules/README.md`)
**Purpose**: Navigation hub and integration point
**Content**:
- Quick reference to all rule modules
- Authority hierarchy clarification
- Integration protocols between modules
- Version tracking and update history

**Size**: ~75 lines (reduced from 179)

#### Cross-Module Dependencies
- **Partnership Protocol** ← references → **Communication Rules**
- **Development Standards** ← integrates → **Tool Usage Protocols**
- **Project Governance** ← enforces → **Evolution and Learning**
- **All Modules** ← align with → **Partnership Protocol**

#### Implementation Phases

**Phase 1: Core Modularization**
1. Create `docs/rules/` directory structure
2. Split CLAUDE_RULES.md into 6 core modules
3. Create master registry (`rules/README.md`)
4. Update cross-references throughout system

**Phase 2: New Rules Integration**
1. Add 7 new rules to appropriate modules
2. Update development standards with new insights
3. Integrate error resolution and pattern storage protocols
4. Add model selection and transparency requirements

**Phase 3: Validation and Optimization**
1. Test rule module integration
2. Validate PTS compliance across all modules
3. Optimize for token efficiency
4. Establish update and evolution procedures

## Benefits of Modular Architecture

### Focused Responsibility
- Each module handles specific aspect of partnership
- Clear boundaries reduce confusion and conflicts
- Easier to maintain and update specific areas

### Scalability
- New rules can be added to appropriate modules
- Modules can evolve independently while maintaining integration
- Better organization for future partnership expansions

### Context Efficiency
- Users and systems can reference specific rule areas
- Reduced context consumption for focused queries
- Better tool integration with targeted rule modules

### Continuous Evolution
- Clear update protocols for each module type
- History tracking within each specialized area
- Easier identification of rule gaps and improvement opportunities

## Implementation Considerations

### PTS Compliance
- Each module must meet 12-component PTS framework
- Line limits enforced (≤200 lines per module)
- Clear, direct, and practical rule definitions
- No marketing language or embellishments

### Authority Hierarchy
- Partnership Protocol as foundation authority
- Other modules implement and extend partnership principles
- docs/vision/ remains absolute system authority
- Clear conflict resolution procedures

### Integration Testing
- Validate rule interactions across modules
- Test rule application in real development scenarios
- Ensure no gaps or contradictions between modules
- Verify complete coverage of current CLAUDE_RULES.md content

---

**Next Steps**: Implement Phase 1 core modularization, followed by Phase 2 new rules integration, and Phase 3 validation and optimization.