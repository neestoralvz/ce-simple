# Mandatory Exploration Protocol

## Purpose
Verify all file and directory references using exploration tools before making claims.

## Core Rule
Every existence claim MUST be preceded by tool verification:
- File existence → Use LS, Glob, or Read
- Directory structure → Use LS
- Content patterns → Use Grep
- System state → Use Bash

## Tool Selection Guide
- **Directory Structure**: LS tool
- **File Patterns**: Glob tool  
- **Content Search**: Grep tool
- **Specific Files**: Read tool
- **System State**: Bash tool

## Forbidden Patterns
Never make these claims without prior tool verification:
- "The file exists..."
- "The directory contains..."
- "Based on the structure..." 
- "The system has..."

## Correct Workflow
1. Execute exploration tool
2. Analyze results
3. Make claims based on actual findings
4. Reference only verified resources

## Implementation Template
1. **Exploration Phase**: Execute verification tools
2. **Results Phase**: State findings from tool outputs
3. **Action Phase**: Implement using verified information only

## Warning Signs
- Claims without preceding tool calls
- Unverified system state statements
- References without exploration
- Assumptions about resources

## Success Metrics
- Tool calls ≥ existence claims (1:1 minimum ratio)
- All references point to verified resources
- Zero unverified claims in responses

## Enforcement
**Pre-response checks**:
1. Identify all existence claims
2. Verify tool call precedence
3. Block unverified responses
4. Require exploration before proceeding

## Implementation Rules
1. Every existence claim needs tool verification
2. Every directory reference needs LS validation
3. Every file mention needs appropriate tool
4. Every system assertion needs verification
5. Zero exceptions allowed

---

**MANDATORY**: Explore before claiming. Violations undermine system accuracy and user trust.