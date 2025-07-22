# Quick Start - Start in 5 Minutes

## 🚀 IMMEDIATE START

### What is ce-simple?
An intelligent system for Claude Code that works with simple and pragmatic components.

### How does it work?
1. **You have a problem** → Search for a component
2. **Component does not exist** → Create it in 15 minutes  
3. **It works** → Document it in 3 lines
4. **It improves** → One iteration per week

## 📋 CURRENT STRUCTURE

```
ce-simple/
├── CLAUDE.md                   # Main instructions
├── .claude/commands/           # Functional components (few but working)
├── system/                    # Pragmatic documentation (4 files maximum)
└── .archive/                  # Historical knowledge (reference)
```

## 🎯 FIRST STEPS

### 1. Read the Principle (2 minutes)
- Open: `system/pragmatic-foundation.md`
- Understand: "Practical effectiveness over theoretical perfection"

### 2. Review Working Commands (2 minutes)  
- Open: `system/working-components.md` 
- See what commands exist and work NOW

### 3. Use a Command (1 minute)
- Execute: `/validate-file [file]`
- See immediate result
- If it works → use it regularly
- If it does not work → report it for fixing

## 🔧 CREATE A NEW COMMAND

### Golden Rules
1. **Maximum 50 lines** documentation
2. **Single unique function** and clear
3. **Testable in 5 minutes** 
4. **Immediately useful**

### Minimum Template (in `.claude/commands/`)
```markdown
# Command Name

## 🎯 Purpose (1 line)
[What it does exactly]

## 🚀 Usage (1 line)
Execute: `/command-name [parameters]`

## ✅ Test (2 lines)
[How to verify it works]

## 🔧 Implementation
[Instructions for Claude Code]
```

## 📊 NEXT STEPS

1. **Today**: Test `/validate-file` with a file
2. **This week**: Use the command regularly and give feedback
3. **Next week**: Suggest improvements or necessary new command

---

*Ready to start! Remember: simple, functional, immediate.*