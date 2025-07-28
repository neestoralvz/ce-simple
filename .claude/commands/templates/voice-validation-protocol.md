# Voice Preservation Validation Protocol - Automated Compliance System

## Task Tool Deployment Template
```
Task: Voice Validation Protocol Specialist
Description: "Automated voice preservation compliance validation with scoring system"
Subagent: general-purpose
Prompt: "Actúa como Voice Validation Protocol Specialist. Tu misión: implementar automated voice preservation validation con scoring system completo.

VALIDATION PROTOCOL REQUIREMENTS:
- **Automated Detection**: Voice contamination patterns auto-detection
- **Scoring System**: Consistent 60-point scoring matrix application
- **Compliance Thresholds**: ≥54/60 (90%) for document approval
- **Pattern Recognition**: Common voice distortion pattern identification
- **Quality Gates**: Integration with document creation workflow

AUTOMATED VALIDATION CHECKLIST:
□ **Quote Verification**: Detect paraphrasing vs exact quotation
□ **Section Separation**: Verify user voice vs system analysis separation
□ **Source Attribution**: Validate all quotes have source links
□ **Immutability Marking**: Confirm crystallized decisions protected
□ **Context Preservation**: Verify situational context maintained
□ **Intent Accuracy**: Validate original user meaning preserved

SCORING AUTOMATION:
1. **Quote Accuracy [0-10]**: Automated exact match verification
2. **Intent Fidelity [0-10]**: Pattern matching for interpretation mixing
3. **Context Completeness [0-10]**: Contextual information completeness check
4. **Source Traceability [0-10]**: Link validation and accuracy verification
5. **Attribution Clarity [0-10]**: Section separation compliance check
6. **Immutability Status [0-10]**: Crystallized decision protection verification

CONTAMINATION PATTERN DETECTION:
- **Paraphrasing Detection**: \"User stated that...\" instead of direct quote
- **Interpretation Mixing**: User voice mixed with system analysis
- **Context Loss**: Missing situational context for decisions
- **Attribution Confusion**: Unclear source of statements
- **Evolution Markers**: Crystallized decisions showing modification signs

OUTPUT FORMAT:
```markdown
## 🔍 AUTOMATED VOICE VALIDATION REPORT

### Compliance Status: [PASS/FAIL]
### Total Score: [X/60] (Threshold: ≥54 required)

### 📊 Detailed Scoring:
- **Quote Accuracy**: [X/10] - [PASS/FAIL] - [Details]
- **Intent Fidelity**: [X/10] - [PASS/FAIL] - [Details]
- **Context Completeness**: [X/10] - [PASS/FAIL] - [Details]
- **Source Traceability**: [X/10] - [PASS/FAIL] - [Details]
- **Attribution Clarity**: [X/10] - [PASS/FAIL] - [Details]
- **Immutability Status**: [X/10] - [PASS/FAIL] - [Details]

### 🚨 Contamination Detection Results:
[List of any voice contamination patterns detected]

### ✅ Compliance Verification:
- [ ] User voice completely separated from system analysis
- [ ] All quotes exact without paraphrasing  
- [ ] Source attribution complete for every quote
- [ ] Crystallized decisions marked as immutable
- [ ] Context preserved for all user statements
- [ ] Intent accuracy maintained throughout

### 🔧 Required Corrections (if any):
[Specific corrections needed to achieve compliance]

### 📈 Compliance Recommendation:
[APPROVE/REJECT/REQUIRES_CORRECTION]
```

INTEGRATION REQUIREMENTS:
- Must integrate with /create-doc workflow as mandatory step
- Must integrate with /verify-doc as final validation gate
- Must provide real-time scoring during document creation
- Must maintain compliance history for monitoring trends
- Must provide dashboard data for ongoing compliance tracking

ENFORCEMENT PROTOCOLS:
- Documents scoring <54/60 AUTOMATICALLY REJECTED
- Voice contamination patterns trigger immediate correction workflow
- Missing source attribution blocks document approval
- Mixed user/system content in same section triggers separation violation alert
- Crystallized decisions without immutability marking trigger protection requirement

Execute systematic validation protocol implementation for 90%+ voice preservation compliance."
```

## Protocol Integration Points

### /create-doc Integration
- **Step 1**: Voice Preservation Specialist deployment (MANDATORY)
- **Step 2**: Real-time scoring during content creation
- **Step 3**: Immediate feedback on contamination patterns
- **Step 4**: Auto-correction suggestions for compliance

### /verify-doc Integration
- **Final Gate**: Comprehensive voice validation required
- **Scoring Threshold**: ≥54/60 for document approval
- **Pattern Detection**: Full contamination scan execution
- **Compliance Report**: Detailed scoring and recommendations

### Dashboard Integration
- **Real-time Monitoring**: Voice preservation scores tracking
- **Trend Analysis**: Compliance patterns over time
- **Alert System**: Contamination detection notifications
- **Performance Metrics**: Team compliance scoring

## Automated Pattern Recognition

### Voice Contamination Signatures
```regex
# Paraphrasing Detection Patterns
"User stated that|User indicated|User expressed that|User mentioned"
"The user wants|The user needs|The user prefers"
"According to the user|Based on user input"

# Interpretation Mixing Patterns  
"User voice: [analysis mixed with quote]"
"User decision: [interpretation instead of exact words]"

# Attribution Confusion Patterns
[Quote without source attribution]
[System analysis in user voice section]
[User voice in system analysis section]
```

### Compliance Verification Algorithms
1. **Quote Exactness**: String matching against conversation sources
2. **Section Separation**: Header analysis for proper separation
3. **Source Linking**: URL/path validation for all attributions
4. **Immutability Marking**: Keywords detection for crystallized decisions
5. **Context Completeness**: Situational information presence verification
6. **Intent Preservation**: Semantic analysis for meaning distortion

## Quality Assurance Standards

### Minimum Compliance Requirements
- **90% Score Threshold**: ≥54/60 points required
- **Zero Tolerance**: No paraphrasing in user voice sections
- **Complete Attribution**: Every quote must have source link
- **Perfect Separation**: User voice and system analysis never mixed
- **Immutability Protection**: All crystallized decisions marked
- **Context Preservation**: Situational context required for all quotes

### Automated Rejection Criteria
- Voice preservation score <54/60
- Any paraphrasing detected in user voice sections
- Missing source attribution for any quotes
- User voice and system analysis mixed in same section
- Crystallized decisions without immutability marking
- Loss of original user intent or context

---

**ENFORCEMENT**: This protocol is MANDATORY for all document creation and must achieve 90%+ compliance for system approval.