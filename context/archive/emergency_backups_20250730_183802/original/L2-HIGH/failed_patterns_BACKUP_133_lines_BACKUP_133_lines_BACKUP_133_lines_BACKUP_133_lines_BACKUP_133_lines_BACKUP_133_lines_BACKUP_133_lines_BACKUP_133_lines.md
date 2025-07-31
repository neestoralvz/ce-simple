# Failed Patterns - Anti-Patterns to Avoid

**30/07/2025 11:15 CDMX** | Empirically identified anti-patterns

## AUTORIDAD SUPREMA
VISION.md → @context/architecture/core/truth-source.md → failed patterns prevention

## EMPIRICALLY IDENTIFIED ANTI-PATTERNS

### Monolithic File Accumulation
> "la estructura de carpetas del proyecto se esta volviendo muy compleja y eso no es bueno"

**Failed Pattern**: Files growing beyond cognitive load limits
**Evidence**: 249-line patterns.md file → critical violation
**Triggers**: >80 lines per file (cognitive overload)
**Prevention**: Modular factorization with bidirectional links
**Recovery**: Empirical elimination → essential content identification

### Authority Contamination Pattern
> "existe demasiado sesgo por la informacion que ya esta"

**Failed Pattern**: AI interpretation layers accumulating over user voice
**Evidence**: Clean slate recreation required for bias elimination
**Triggers**:
- Multiple interpretation cycles on core concepts
- Assumption layering in documentation
- AI inference accumulation over time
**Prevention**: Regular clean slate regeneration from pure user voice
**Recovery**: Source identification → current guidelines → clean reconstruction

### Complexity Creep Pattern
> "Si toma más de 3 pasos explicar, está over-engineered"

**Failed Pattern**: System complexity increasing without user value
**Evidence**: Commands requiring >3 steps explanation
**Triggers**:
- Feature addition without complexity assessment
- Theoretical optimization over practical usage
- Abstract elegance over user efficiency
**Prevention**: 3-step explanation test for all new features
**Recovery**: Empirical elimination methodology

### Context Fragmentation Without Authority
**Failed Pattern**: Directory structures disconnected from user vision
**Evidence**: 160+ files eliminated with preserved functionality
**Triggers**:
- Theoretical organization over user workflow
- Directory creation without user authority validation
- Structure serving system vs serving user
**Prevention**: Authority chain validation for all structural decisions
**Recovery**: Discovery through elimination methodology

### Aggressive Simplification Pattern
> "no estoy de acuerdo, creo que de esa manera se pierde mucha informacion"

**Failed Pattern**: Information loss through structural optimization
**Evidence**: User explicit rejection of consolidation proposals
**Triggers**:
- Structural elegance prioritized over information density
- Simplification without user authority validation
- AI recommendation overriding user preferences
**Prevention**: Information preservation supremacy over structural simplification
**Recovery**: User authority override → information restoration

### Assumption-Based Implementation
**Failed Pattern**: Building on inferred requirements vs explicit user direction
**Evidence**: Socratic discovery revealing different user intent
**Triggers**:
- Premature implementation without full discovery
- Token-constrained discovery conversations
- Technical solution before problem understanding
**Prevention**: Unlimited conversation → true intent discovery → command execution
**Recovery**: Socratic methodology → problem rediscovery

### Hardcoded Dependency Pattern
**Failed Pattern**: System behavior dependent on fixed file paths/structures
**Evidence**: 300+ hardcoded references requiring manual updates
**Triggers**:
- Direct file path references in code
- Hardcoded workflows vs dynamic adaptation
- System assumptions about structure permanence
**Prevention**: Configuration-driven behavior + dynamic path resolution
**Recovery**: Reference architecture implementation

## DETECTION CRITERIA

### Early Warning Signals
1. **File Size Growth**: >60 lines approaching 80-line limit
2. **Explanation Complexity**: Requiring >2 steps to explain feature
3. **User Hesitation**: "no estoy seguro", "no estoy de acuerdo" feedback
4. **Authority Questions**: User questioning system decisions
5. **Interpretation Layers**: Multiple revisions of same concept

### Critical Failure Indicators
1. **User Explicit Rejection**: Direct "no estoy de acuerdo" statements
2. **Functionality Loss**: Features broken during optimization
3. **Authority Override**: User correcting system assumptions
4. **Bias Accumulation**: Original user voice no longer recognizable
5. **Cognitive Overload**: User unable to follow system logic

### Recovery Protocols
1. **Immediate Stop**: Halt current approach upon failure detection
2. **User Authority Validation**: Return to @context/architecture/core/truth-source.md for guidance
3. **Clean Slate Assessment**: Determine if reconstruction needed
4. **Empirical Testing**: Apply discovery through elimination
5. **User Confirmation**: Validate recovery approach before proceeding

## PREVENTION METHODOLOGY

### Guardian Integration
**Binary Enforcement Mode**: Automatic STOP on anti-pattern detection
**Critical Thresholds**:
- File size >80 lines → VIOLATION
- Authority chain breach → VIOLATION
- User explicit rejection → VIOLATION
- Information loss → VIOLATION

### Systematic Monitoring
**Continuous Assessment**:
- File size tracking across all system files
- User feedback sentiment analysis
- Authority chain integrity validation
- Complexity measurement (3-step test)

### Quality Gates Integration
**Pre-execution**: Anti-pattern risk assessment
**Mid-execution**: Continuous monitoring for warning signals
**Post-execution**: Validation against known failure patterns

---

**ANTI-PATTERN AUTHORITY**: These patterns identified through empirical failure evidence
**Prevention Protocol**: Guardian enforcement + user authority supremacy
**Recovery Capability**: Clean slate regeneration + empirical elimination methodology