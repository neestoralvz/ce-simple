# Bash Debugging Patterns - Script Error Resolution Authority

**31/07/2025 13:17 CDMX** | Validated debugging patterns extracted from roadmap-update.sh resolution

## AUTORIDAD SUPREMA
↑ @context/architecture/claude_code/automation-patterns/README.md → bash-debugging-patterns.md implements script debugging methodology per automation authority

## PRINCIPIO FUNDAMENTAL
**"3 systematic debugging patterns resolve complex bash scripting errors"** - Evidence-based solutions for ANSI color code handling, command substitution, and test script dependencies.

## DEBUGGING PATTERN ARCHITECTURE

### **Pattern 1: ANSI Color Code Command Substitution Separation**

**Problem**: ANSI escape sequences contaminate command substitution output causing parsing errors
```bash
# ❌ BROKEN: Log output contaminates command substitution
analyze_data() {
    log_info "Processing..."  # Outputs: \033[0;34mℹ\033[0m Processing...
    echo "$result"
}
data=$(analyze_data)  # Contains ANSI codes + result = parsing error
```

**Solution**: Separate verbose logging from silent data functions
```bash
# ✅ FIXED: Separate verbose and silent functions
analyze_data_verbose() {
    log_info "Processing data..."
    local result=$(process_data)
    log_info "Found: $result items"
    echo "$result"
}

analyze_data_silent() {
    # No log output - only return clean data
    echo "$(process_data)"
}

# Usage
analyze_data_verbose           # For user feedback
data=$(analyze_data_silent)    # For command substitution
```

**Evidence**: Resolved roadmap-update.sh ANSI parsing errors completely
**Reusability**: Apply to all colored script output scenarios

### **Pattern 2: Printf Array ANSI Edge Case Resolution**

**Problem**: Printf array handling breaks with ANSI codes and whitespace contamination
```bash
# ❌ BROKEN: Whitespace and ANSI codes cause printf errors
violation_count=$(wc -l < file.txt)  # Returns "     185" with spaces
printf '- %s\n' "${array[@]}"        # Fails with ANSI contaminated arrays
```

**Solution**: Whitespace cleanup + explicit array validation
```bash
# ✅ FIXED: Clean whitespace and validate arrays
violation_count=$(wc -l < file.txt | tr -d ' ')  # Strip whitespace
for item in "${array[@]}"; do
    [[ -n "$item" ]] && echo "- $item"
done
```

**Evidence**: Fixed printf parsing errors in roadmap report generation
**Technical Value**: Solves recurring array + ANSI interaction issues

### **Pattern 3: Test Script Dependency Resolution**

**Problem**: Test scripts fail when missing log functions from main script
```bash
# ❌ BROKEN: Test script calls undefined functions
log_info "Testing component..."  # Function not defined
log_error "Test failed"         # Crashes test execution
```

**Solution**: Conditional function definition with fallbacks
```bash
# ✅ FIXED: Graceful function dependency handling
if ! command -v log_info &> /dev/null; then
    # Define fallback log functions for test environment
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    BLUE='\033[0;34m'
    NC='\033[0m'
    
    log_info() { echo -e "${BLUE}ℹ${NC} $1"; }
    log_success() { echo -e "${GREEN}✅${NC} $1"; }
    log_error() { echo -e "${RED}❌${NC} $1"; }
fi
```

**Evidence**: Fixed test-roadmap-update.sh execution completely
**Reusability**: Essential pattern for independent test script development

## SYSTEMATIC DEBUGGING METHODOLOGY

### **Error Identification Protocol**
1. **Isolate Command Substitution**: Test functions outside $() context first
2. **Check ANSI Contamination**: Look for color codes in unexpected data output
3. **Validate Array Contents**: Ensure arrays contain expected data types
4. **Test Function Dependencies**: Verify all called functions are defined

### **Resolution Validation**
- **Before/After Testing**: Document exact error vs resolution
- **Edge Case Coverage**: Test with empty arrays, missing files, etc.
- **Isolation Testing**: Verify fixes don't break other functionality

## INTEGRATION REFERENCES

### ← automation-patterns/README.md
**Connection**: Specialized debugging patterns complement automation framework
**Protocol**: Debugging patterns serve automation pattern implementation and maintenance

### ←→ scripts/roadmap-update.sh
**Connection**: Live validation of debugging patterns through proven fixes
**Protocol**: Script serves as pattern validation source and evolution driver

### → methodology/script-automation-framework.md
**Connection**: Debugging patterns inform script development methodology
**Protocol**: Proven debugging solutions enhance automation development standards

---

**BASH DEBUGGING PATTERNS DECLARATION**: Evidence-based debugging patterns providing systematic solutions for complex bash scripting errors with proven effectiveness through roadmap-update.sh resolution.

**EVOLUTION PATHWAY**: Patterns evolve through implementation → debugging → systematic solution → pattern documentation cycle.