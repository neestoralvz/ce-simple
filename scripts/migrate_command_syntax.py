#!/usr/bin/env python3
"""
Mass Command Syntax Migration Script
Migrates slash commands from old syntax (/command) to new /{folder}:{command} format
Based on analysis of 626 occurrences across 144 files
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set

# Command mapping: old_command -> (folder, new_command)
COMMAND_MAPPING = {
    # Workflows
    'start': ('workflows', 'start'),
    'distill': ('workflows', 'distill'), 
    'close': ('workflows', 'close'),
    'explore': ('workflows', 'explore'),
    'debug': ('workflows', 'debug'),
    
    # Actions
    'docs': ('actions', 'docs'),
    'git': ('actions', 'git'),
    'compact': ('actions', 'compact'),
    
    # Roles
    'partner': ('roles', 'partner'),
    'challenge': ('roles', 'challenge'),
    'orchestrator': ('roles', 'orchestrator'),
    'research': ('roles', 'research'),
    
    # Validations (maintenance patterns)
    'validate': ('validations', 'validate'),
    'check': ('validations', 'check'),
    
    # Maintenance
    'backup': ('maintenance', 'backup'),
    'cleanup': ('maintenance', 'cleanup'),
    'reset': ('maintenance', 'reset')
}

# File patterns to process (based on analysis)
INCLUDE_PATTERNS = [
    '**/*.md',
    '**/*.txt', 
    '**/*.py',
    '**/*.js',
    '**/*.json'
]

# Directories to exclude
EXCLUDE_DIRS = {
    '.git',
    'node_modules',
    '__pycache__',
    '.pytest_cache',
    'venv',
    'env'
}

def get_project_root() -> Path:
    """Get project root directory"""
    return Path('/Users/nalve/ce-simple')

def should_skip_file(file_path: Path) -> bool:
    """Check if file should be skipped"""
    # Skip if in excluded directories
    for part in file_path.parts:
        if part in EXCLUDE_DIRS:
            return True
    
    # Skip binary files
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.read(1024)  # Try to read first 1KB
    except UnicodeDecodeError:
        return True
    
    return False

def find_slash_commands(content: str) -> List[Tuple[str, int, str]]:
    """
    Find all slash command occurrences in content
    Returns: [(match, line_number, context)]
    """
    matches = []
    lines = content.split('\n')
    
    # Pattern to match slash commands: /command_name (with word boundaries)
    pattern = r'/([a-zA-Z_][a-zA-Z0-9_]*)\b'
    
    for line_num, line in enumerate(lines, 1):
        for match in re.finditer(pattern, line):
            command_name = match.group(1)
            if command_name in COMMAND_MAPPING:
                matches.append((match.group(0), line_num, line.strip()))
    
    return matches

def migrate_content(content: str) -> Tuple[str, int]:
    """
    Migrate slash commands in content to new syntax
    Returns: (migrated_content, num_changes)
    """
    migrated = content
    num_changes = 0
    
    # Process each command mapping
    for old_cmd, (folder, new_cmd) in COMMAND_MAPPING.items():
        old_pattern = f'/{old_cmd}\\b'
        new_syntax = f'/{folder}:{new_cmd}'
        
        # Count matches before replacement
        matches = len(re.findall(old_pattern, migrated))
        if matches > 0:
            migrated = re.sub(old_pattern, new_syntax, migrated)
            num_changes += matches
    
    return migrated, num_changes

def process_file(file_path: Path, dry_run: bool = True) -> Dict:
    """
    Process a single file for command migration
    Returns: dict with processing results
    """
    result = {
        'file': str(file_path),
        'original_commands': [],
        'changes_made': 0,
        'success': False,
        'error': None
    }
    
    try:
        # Read original content
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Find existing commands
        result['original_commands'] = find_slash_commands(original_content)
        
        # Migrate content
        migrated_content, num_changes = migrate_content(original_content)
        result['changes_made'] = num_changes
        
        # Write changes if not dry run and changes were made
        if not dry_run and num_changes > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(migrated_content)
        
        result['success'] = True
        
    except Exception as e:
        result['error'] = str(e)
    
    return result

def scan_project_files() -> List[Path]:
    """Scan project for files to process"""
    project_root = get_project_root()
    files_to_process = []
    
    for pattern in INCLUDE_PATTERNS:
        for file_path in project_root.glob(pattern):
            if file_path.is_file() and not should_skip_file(file_path):
                files_to_process.append(file_path)
    
    return sorted(files_to_process)

def main():
    """Main migration execution"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Migrate slash command syntax')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be changed without making changes')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Show detailed output')
    parser.add_argument('--file', help='Process specific file instead of entire project')
    
    args = parser.parse_args()
    
    print("🔄 Command Syntax Migration Script")
    print("=" * 50)
    
    # Determine files to process
    if args.file:
        files_to_process = [Path(args.file)]
    else:
        print("📁 Scanning project files...")
        files_to_process = scan_project_files()
        print(f"Found {len(files_to_process)} files to analyze")
    
    # Process files
    total_files = len(files_to_process)
    total_changes = 0
    files_with_changes = 0
    errors = []
    
    print(f"\n{'🔍 DRY RUN MODE' if args.dry_run else '✏️  MIGRATION MODE'}")
    print("-" * 30)
    
    for i, file_path in enumerate(files_to_process, 1):
        if args.verbose:
            print(f"[{i}/{total_files}] Processing: {file_path}")
        
        result = process_file(file_path, dry_run=args.dry_run)
        
        if result['error']:
            errors.append(f"{file_path}: {result['error']}")
            if args.verbose:
                print(f"  ❌ Error: {result['error']}")
            continue
        
        if result['changes_made'] > 0:
            files_with_changes += 1
            total_changes += result['changes_made']
            
            if args.verbose or args.dry_run:
                print(f"  📝 {file_path}")
                print(f"     Changes: {result['changes_made']}")
                
                if args.verbose and result['original_commands']:
                    print("     Original commands found:")
                    for cmd, line_num, context in result['original_commands'][:3]:  # Show first 3
                        print(f"       Line {line_num}: {cmd} in '{context[:50]}...'")
                    if len(result['original_commands']) > 3:
                        print(f"       ... and {len(result['original_commands']) - 3} more")
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 MIGRATION SUMMARY")
    print("=" * 50)
    print(f"Files analyzed: {total_files}")
    print(f"Files with changes: {files_with_changes}")
    print(f"Total changes: {total_changes}")
    
    if errors:
        print(f"Errors: {len(errors)}")
        if args.verbose:
            for error in errors:
                print(f"  ❌ {error}")
    
    if args.dry_run and total_changes > 0:
        print(f"\n🎯 To execute migration: python {sys.argv[0]} (without --dry-run)")
    elif not args.dry_run and total_changes > 0:
        print(f"\n✅ Migration completed successfully!")
        print("💡 Recommended: Run tests and validate system functionality")
    elif total_changes == 0:
        print(f"\n✨ No slash commands found that need migration")

if __name__ == '__main__':
    main()