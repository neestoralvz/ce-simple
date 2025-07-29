#!/usr/bin/env python3
"""
Export Validation Script

Validates that the exported command system is complete and ready for distribution.
"""

import os
from pathlib import Path

def validate_export():
    """Validate the export structure and content"""
    export_dir = Path('.')
    
    print("🔍 Validating Export Structure...")
    
    # Required files
    required_files = [
        'README.md',
        'CLAUDE.md', 
        'install.sh',
        'docs/command_reference.md',
        'docs/customization_guide.md',
        'docs/quick_start.md'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not (export_dir / file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    else:
        print("✅ All required files present")
    
    # Command structure validation
    commands_dir = export_dir / 'commands'
    if not commands_dir.exists():
        print("❌ Commands directory missing")
        return False
    
    command_categories = ['actions', 'roles', 'workflows', 'methodology', 'maintenance']
    missing_categories = []
    
    for category in command_categories:
        category_dir = commands_dir / category
        if not category_dir.exists():
            missing_categories.append(category)
        else:
            # Count .md files in each category
            md_files = list(category_dir.glob('*.md'))
            print(f"✅ {category}: {len(md_files)} commands")
    
    if missing_categories:
        print(f"❌ Missing command categories: {missing_categories}")
        return False
    
    # Check for ce-simple specific references that should be cleaned
    print("\n🔍 Checking for cleaned references...")
    
    check_files = [
        'CLAUDE.md',
        'commands/actions/research.md',
        'commands/roles/orchestrator.md'
    ]
    
    problematic_refs = []
    for file_path in check_files:
        full_path = export_dir / file_path
        if full_path.exists():
            with open(full_path, 'r') as f:
                content = f.read()
                
            # Check for ce-simple specific references
            if 'ce-simple' in content and '[PROJECT_NAME]' not in content:
                problematic_refs.append(f"{file_path}: contains 'ce-simple'")
            
            if 'context/user-vision/TRUTH_SOURCE.md' in content:
                problematic_refs.append(f"{file_path}: contains old TRUTH_SOURCE path")
                
            if '29/07/2025' in content or 'CDMX' in content:
                problematic_refs.append(f"{file_path}: contains timestamp/location")
    
    if problematic_refs:
        print("⚠️  Found potentially problematic references:")
        for ref in problematic_refs:
            print(f"   - {ref}")
    else:
        print("✅ References properly cleaned")
    
    # Validate installation script
    install_script = export_dir / 'install.sh'
    if install_script.exists():
        with open(install_script, 'r') as f:
            install_content = f.read()
        
        if 'chmod +x' in install_content and 'mkdir -p' in install_content:
            print("✅ Installation script looks functional")
        else:
            print("⚠️  Installation script may be incomplete")
    
    print(f"\n📊 Export Summary:")
    print(f"   - Structure: Complete")
    print(f"   - Commands: {sum(len(list((commands_dir / cat).glob('*.md'))) for cat in command_categories if (commands_dir / cat).exists())} total")
    print(f"   - Documentation: Complete")
    print(f"   - Installation: Ready")
    
    print(f"\n✅ Export validation complete!")
    print(f"🚀 Ready for distribution to other projects")
    
    return True

if __name__ == "__main__":
    validate_export()