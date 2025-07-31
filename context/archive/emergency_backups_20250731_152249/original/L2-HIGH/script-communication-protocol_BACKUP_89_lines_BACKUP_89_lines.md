# Script Communication Protocol - Silent Scripts Authority

**31/07/2025 CDMX** | Communication protocol for bash scripts and Claude Code interaction

## AUTORIDAD SUPREMA
@context/architecture/standards.md → script-communication-protocol.md implements natural communication standards per user authority

## PRINCIPIO FUNDAMENTAL
**"Claude Code communicates with users, bash scripts process data silently"** - Clear separation between technical processing and user communication maintains natural conversation flow.

## COMMUNICATION PROTOCOL STANDARDS

### **SILENT SCRIPTS MANDATORY**
- **NO echo/printf**: Scripts must not output user-facing messages
- **NO colored output**: No ANSI color codes for user notifications
- **NO progress indicators**: No user-visible progress bars or status updates
- **TECHNICAL DATA ONLY**: Scripts output only parseable technical data

### **CLAUDE CODE COMMUNICATION AUTHORITY**
- **INTERPRETS results**: Claude processes script outputs and communicates findings
- **NATURAL language**: All user communication in natural Spanish/English
- **CONTEXTUAL explanation**: Claude provides context and meaning for technical results
- **USER-FRIENDLY format**: Results formatted for human understanding

## CORRECT PATTERNS

### **❌ INCORRECT (Script communicates directly):**
```bash
echo "🔍 DOMAIN CLASSIFIER: Automated Content Categorization"
echo "Files processed: $processed"
echo -e "${GREEN}📈 Classification Summary:${NC}"
echo "H6A-suitable: $h6a_count"
```

### **✅ CORRECT (Script provides data, Claude communicates):**
```bash
# Silent processing - no user output
echo "$processed|$h6a_count|$h6b_count|$h6c_count" > results.txt
```

**Claude Code then communicates:**
"He ejecutado la clasificación de dominios y procesé 47 archivos. Encontré 12 archivos adecuados para H6A (archival), 18 para H6B (L2-MODULAR), y 10 para H6C (evaluación individual)."

## IMPLEMENTATION STANDARDS

### **Script Design Requirements**
- **Data output only**: Scripts produce parseable data (CSV, JSON, pipe-delimited)
- **Error codes**: Use exit codes for success/failure indication
- **Log files**: Technical logging to files, not stdout for user consumption
- **Silent execution**: No user-visible output during normal operation

### **Claude Code Integration**
- **Result interpretation**: Claude reads script outputs and explains significance
- **Context provision**: Claude provides business context for technical results
- **Natural flow**: Communication maintains conversation-first development approach
- **Authority preservation**: Claude ensures user authority is maintained in all communications

## VALIDATION CHECKLIST

### **Script Compliance Validation**
- ✅ No echo/printf statements for user communication
- ✅ No colored output or formatting for users
- ✅ Technical data output only (results, logs, error codes)
- ✅ Silent execution during normal operation

### **Communication Quality Validation**
- ✅ Claude Code interprets all technical results
- ✅ Natural language communication with users
- ✅ Contextual explanation of script findings
- ✅ User authority preservation in all communications

## SCRIPT CATEGORIES

### **Silent Processing Scripts** (✅ Compliant)
- Data processing and analysis scripts
- File operation scripts
- Validation and compliance checking scripts
- System automation scripts

### **Interactive Scripts** (Requires Special Handling)
- User input collection scripts
- Configuration setup scripts
- Emergency diagnostic scripts
- Must explicitly separate data collection from user communication

---

**COMMUNICATION PROTOCOL DECLARATION**: This protocol ensures natural conversation flow by maintaining clear separation between technical processing (bash scripts) and user communication (Claude Code) per user authority and conversation-first development principles.

**ENFORCEMENT**: All scripts must comply with silent processing standards, with Claude Code providing all user-facing communication and result interpretation.