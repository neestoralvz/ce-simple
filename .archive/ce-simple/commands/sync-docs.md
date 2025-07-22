# Sync Docs - Claude Code Slash Command

## 🎯 Purpose
Maintain system documentation synchronized and coherent automatically, updating counters, lists and references between files.

## 🚀 Usage
Execute: `/sync-docs`

The command performs:
1. **Validate consistency** - Detect discrepancies between files
2. **Update counters** - Commands working in real time
3. **Synchronize lists** - Commands in CLAUDE.md, working-components.md, list-commands.md
4. **Verify references** - Links and file structure
5. **Report changes** - Summary of synchronization performed

## ✅ Quick Test
1. Execute `/sync-docs`
2. MUST complete synchronization in <10 seconds
3. Report synchronized elements and discrepancies found
4. Verify counters match between files

## 🔧 Intelligent Implementation

### Instructions for Claude Code
When executing this command (improved flow with command connection):

1. **STEP 1: Comprehensive Discovery with `/explore-code`**
   - Execute `/explore-code new or modified commands`
   - Execute `/explore-code outdated documentation`
   - Execute `/explore-code files with Spanish text or standards violations`
   - Automatically identify ALL changes requiring attention
   - Create complete list of problematic files for targeted processing

2. **STEP 2: Targeted Standards Application with `/writing-standards`**
   - Apply `/writing-standards` ONLY to files identified by explore-code
   - Verify compliance in specific files: English only, density, imperative tone
   - Detect targeted violations: Spanish text, redundancy, missing technical precision
   - Prepare automatic corrections ONLY where explore-code detected problems
   - Only proceed if explore-code found files requiring correction

3. **STEP 3: Real Commands Analysis** (based on findings)
   - Count files in `.claude/commands/` detected by explore-code
   - Identify new, modified or deleted commands
   - Create dynamic list with each command status

4. **STEP 4: Targeted Inconsistency Validation**
   - **CLAUDE.md lines 43-74**: Functional commands list
   - **CLAUDE.md lines 28-34**: File structure
   - **working-components.md line 9**: "Functional commands: X" 
   - **working-components.md lines 17-43**: Implemented commands list
   - **list-commands.md lines 28-30**: System counters
   - **list-commands.md lines 34-40**: Completed commands list
   - Only validate sections explore-code identified as problematic

5. **STEP 5: Automatic Writing Standards Application** (Targeted)
   - **APPLY** writing-standards corrections identified in STEP 2
   - **CONVERT** Spanish text to English automatically (only in files detected by explore-code)
   - **OPTIMIZE** density and eliminate detected redundancy (targeted processing)
   - **ADD** capitals for critical instructions where missing (specific files)
   - **VERIFY** imperative tone and technical precision (only where explore-code found problems)
   - **FILE REWRITING RULE**: When files require >5 changes, completely rewrite for optimal results

6. **STEP 6: Selective Update**
   - **Only update** elements that actually changed
   - **Counters**: Replace incorrect numbers detected
   - **Lists**: Add/remove commands according to explore-code findings
   - **States**: Verify coherence with physical files
   - **Standards**: Apply writing-standards corrections automatically
   - **Timestamps**: Update only if real changes exist

7. **STEP 7: Intelligent Reference Verification**
   - Verify only references affected by detected changes
   - Internal links related to modified commands
   - File structure vs reality (only if explore-code found discrepancies)

8. **STEP 8: Automatic Validation with `/validate-file`**
   - **EXECUTE MANDATORY**: `/validate-file [modified-file]` for each file that was changed
   - Verify applied changes are correct and complete
   - Validate structure, format and standards compliance
   - Detect any problems introduced during synchronization
   - Report validation results within final report

9. **STEP 9: Detailed Report with Next Steps**
   ```
   🔄 SYNC-DOCS COMPLETED (INTELLIGENT)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🔍 Discovery: /explore-code found [X] problematic files
   📝 Targeted Standards: /writing-standards applied corrections to [Y] specific files
   📊 Commands processed: [Z] (only those identified by explore-code)
   ✅ Files synchronized: [W] (targeted processing)  
   🔧 Discrepancies corrected: [V]
   ✅ Automatic validation: /validate-file verified [W] modified files
   
   📝 Intelligent Updates Performed:
   • Explore-code identified: [specific files needing attention]
   • Writing Standards applied targeted: [Spanish→English, density, capitals in specific files]
   • CLAUDE.md: [specific changes detected]
   • working-components.md: [specific changes detected]  
   • list-commands.md: [specific changes detected]
   • Validation Results: [✅ All files passed | ⚠️ Issues detected | ❌ Validation failed]
   
   💡 Suggested Next Steps:
   • /list-commands - View complete updated status (validate-file ALREADY EXECUTED automatically)
   • [other-command] - If validation detected specific needs
   • Manual review - Only if validation found critical problems
   
   🎯 Status: [SYNCHRONIZED | CHANGES DETECTED | NO CHANGES]
   ```

### Intelligent Synchronization Algorithm

#### Detection Flow with Connected Commands (Optimized):
```
1. problematic_files = /explore-code "new or modified commands"
2. outdated_docs = /explore-code "outdated documentation" 
3. standards_violations = /explore-code "files with Spanish text or standards violations"
4. IF (problematic_files OR outdated_docs OR standards_violations):
   targeted_files = COMBINE_FINDINGS(step1, step2, step3)
   APPLY_WRITING_STANDARDS_ONLY_TO(targeted_files)
   real_commands = count_files(.claude/commands/*.md)
   listed_commands = extract_commands_from_lists()
   modified_files = UPDATE_ONLY_DETECTED_CHANGES()
   FOR EACH file IN modified_files:
       validation_results = EXECUTE_VALIDATE_FILE(file)
   COMPLETE_REPORT(changes, corrections, validations)
5. ELSE:
   REPORT("System synchronized - no problematic files detected")
```

#### Selective Update (Only if changes exist):
- `CLAUDE.md` → Update Available Commands section (if explore-code detected changes)
- `working-components.md` → Update counters and lists (if new commands exist)
- `list-commands.md` → Update working commands (if explore-code found modifications)

#### Contextual Validation:
- Commands detected by explore-code → Verify status ✅ READY
- Commands not found physically → Status "Planned" or remove
- Synchronization only where explore-code identified problems

### 🔗 Related Slash Commands
- `/writing-standards` - CRITICAL PRE-REQUISITE: Verifies and applies standards before any modification
- `/explore-code` - PRE-REQUISITE: Detects changes automatically before synchronizing  
- `/validate-file` - **MANDATORY INTEGRATION**: Validates ALL modified files automatically
- `/create-command` - TRIGGER: Auto-trigger sync after creating command
- `/list-commands` - POST-ACTION: View updated status after synchronization

**RULE**: Only reference other commands, never direct files

### ⚡ Intelligent Triggers (Connected System)
Advanced automatic connection system between commands

#### Input Triggers (When to activate automatically):
- **Context**: `/create-command` completes → Auto-trigger `/sync-docs`
- **Context**: `/writing-standards` detects violations → Auto-trigger synchronization with correction
- **Context**: Modifications detected by `/explore-code` → Activate synchronization
- **Previous**: `/explore-code documentation` → If finds inconsistencies, call sync-docs
- **Keywords**: synchronize, update, coherence, consistency, outdated documentation, standards

#### Pre-triggers (Commands sync-docs executes automatically):
- **ALWAYS FIRST**: `/explore-code new or modified commands` - Comprehensive discovery
- **ALWAYS SECOND**: `/explore-code outdated documentation` - Broad detection
- **ALWAYS THIRD**: `/explore-code files with Spanish text or standards violations` - Standards discovery
- **ALWAYS FOURTH**: `/writing-standards` - Targeted correction ONLY on files detected by explore-code
- **CONDITION**: Only proceed if explore-code detects problematic files

#### Output Triggers (Post-execution connections):
- **When**: Synchronization completed with changes
- **Auto-execute MANDATORY**: `/validate-file [modified-file]` for automatic specific verification
- **Auto-suggest**: `/writing-standards [modified-file]` to verify correct application
- **Auto-suggest**: `/list-commands` to view complete updated status
- **AUTOMATIC intelligent chain**: explore-code → writing-standards → sync-docs → **validate-file** → list-commands

#### Output Triggers (Conditional flows):
- **If NO changes or violations**: Report "System synchronized" + suggest `/list-commands`
- **If standards violations exist**: Auto-apply corrections + report changes made
- **If errors exist**: Auto-execute `/validate-file` on problematic files (ALREADY INCLUDED in automatic flow)
- **If new commands exist**: Suggest `/explore-code new functionalities`
- **Problem chain**: sync-docs → validate-file → writing-standards → explore-code → [manual resolution]

---

*Claude Code slash command - automatic system documentation coherence maintenance*