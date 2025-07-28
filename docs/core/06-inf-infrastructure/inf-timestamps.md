# Timestamp Standards

**Updated**: 2025-07-24 12:54 (Mexico City) | **Authority**: Official timestamp format | **Limit**: 100 lines

## Standard Format

**Required Format**: `**Updated**: YYYY-MM-DD HH:MM (Mexico City)`

**Example**: `**Updated**: 2025-07-24 12:54 (Mexico City)`

## Implementation Rules

### Mandatory Usage
- **All new files**: Must include timestamp in header metadata
- **File updates**: Must update timestamp when content is modified
- **System files**: CLAUDE.md, rules/CLAUDE_RULES.md always use this format

### Format Specifications
- **Date**: YYYY-MM-DD format (ISO 8601 compatible)
- **Time**: 24-hour format (HH:MM)
- **Timezone**: Always specify "(Mexico City)" 
- **Label**: Always use "**Updated**:" (not "Last Updated" or "Created")

### Header Placement
- **Line 3**: Standard placement in document headers
- **Format**: `**Updated**: YYYY-MM-DD HH:MM (Mexico City) | **Other Metadata**...`

## Timezone Reference

**Mexico City Time Zone**:
- **Official**: UTC-6 (CST - Central Standard Time)
- **Daylight**: UTC-5 (CDT - Central Daylight Time, March-November)
- **Generation**: Use `TZ='America/Mexico_City' date '+%Y-%m-%d %H:%M'`

## File Type Guidelines

### Documentation Files
- **docs/**: All markdown files require timestamps
- **Format**: Standard format in line 3
- **Update rule**: Change timestamp when content is modified

### Command Files  
- **commands/**: All command files require timestamps
- **export/**: Global command system requires timestamps
- **Format**: Standard format after main heading

### System Files
- **CLAUDE.md**: Always current timestamp
- **rules/CLAUDE_RULES.md**: Always current timestamp  
- **README files**: Always current timestamp

## Quality Control

### Validation Checklist
- [ ] Format matches exactly: `**Updated**: YYYY-MM-DD HH:MM (Mexico City)`
- [ ] Timezone specified as "(Mexico City)"
- [ ] 24-hour time format used
- [ ] Date in YYYY-MM-DD format
- [ ] Label is "**Updated**:" (not variants)

### Common Mistakes to Avoid
- ❌ `**Last Updated**: 2025-07-24`
- ❌ `**Created: 2025-07-24**`  
- ❌ `**Updated**: 2025-07-24` (missing time/timezone)
- ❌ `**Updated**: 2025-07-24 2:54 PM` (12-hour format)
- ❌ `**Updated**: 24-07-2025 14:54` (wrong date format)

## Automation Support

### Generation Command
```bash
TZ='America/Mexico_City' date '+%Y-%m-%d %H:%M'
```

### Template Integration
- **Templates**: All document templates include timestamp placeholder
- **Variable**: `{{TIMESTAMP}}` → `2025-07-24 12:54 (Mexico City)`
- **Automation**: Timestamp generation integrated into document creation

## Migration Protocol

### Legacy Format Handling
- **Identify**: Search for old timestamp patterns
- **Update**: Convert to standard format
- **Verify**: Ensure consistency across all files

### Batch Update Process
1. **Search patterns**: `**Last Updated`, `**Created`, timestamp variants
2. **Replace systematically**: Use standardized format
3. **Verify completion**: Ensure no old patterns remain

---

**Standard**: All timestamps use Mexico City time in 24-hour format | **Authority**: Official documentation standard | **Compliance**: Mandatory for all files