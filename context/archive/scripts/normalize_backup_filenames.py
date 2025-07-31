#!/usr/bin/env python3
"""
Normalize exponential BACKUP suffix chains in emergency backup directories.
Preserves content while cleaning up filename pollution.
"""

import os
import re
import shutil
from pathlib import Path

def normalize_filename(filename):
    """
    Normalize filename by removing exponential BACKUP suffixes.
    
    Example:
    file_BACKUP_123_lines_BACKUP_123_lines_BACKUP_123_lines.md
    -> file_BACKUP_123_lines.md
    """
    # Pattern to match exponential BACKUP suffixes
    pattern = r'(_BACKUP_\d+_lines)(_BACKUP_\d+_lines)+'
    
    # Find the first BACKUP suffix and remove all subsequent ones
    match = re.search(pattern, filename)
    if match:
        # Keep only the first BACKUP suffix
        normalized = filename[:match.start() + len(match.group(1))]
        # Add the file extension back
        if filename.endswith('.md'):
            normalized += '.md'
        return normalized
    
    return filename

def normalize_directory_filenames(directory_path):
    """Normalize all filenames in a directory recursively."""
    directory = Path(directory_path)
    if not directory.exists():
        print(f"Directory {directory_path} does not exist")
        return
    
    normalized_count = 0
    
    for file_path in directory.rglob('*'):
        if file_path.is_file():
            original_name = file_path.name
            normalized_name = normalize_filename(original_name)
            
            if original_name != normalized_name:
                new_path = file_path.parent / normalized_name
                
                # Avoid conflicts - if normalized name already exists, skip
                if new_path.exists():
                    print(f"Skipping {file_path} - normalized name already exists")
                    continue
                
                print(f"Normalizing: {original_name} -> {normalized_name}")
                file_path.rename(new_path)
                normalized_count += 1
    
    print(f"Normalized {normalized_count} filenames in {directory_path}")

def main():
    """Main cleanup function."""
    archive_dir = Path("/Users/nalve/ce-simple/context/archive")
    
    # Find all emergency backup directories
    backup_dirs = list(archive_dir.glob("emergency_backups_*"))
    
    print(f"Found {len(backup_dirs)} emergency backup directories")
    
    for backup_dir in backup_dirs:
        print(f"\nProcessing {backup_dir.name}...")
        normalize_directory_filenames(backup_dir)
    
    print("\nFilename normalization complete!")

if __name__ == "__main__":
    main()