#!/usr/bin/env python3
"""
Taxonomy Classification System
Applies predictable organization rules to project files
"""

import os
import shutil
import re
from pathlib import Path
from typing import Dict, List, Tuple

class TaxonomyClassifier:
    """Classifies and organizes files based on type and purpose taxonomy"""
    
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.classification_rules = self._build_classification_rules()
        
    def _build_classification_rules(self) -> Dict:
        """Build comprehensive classification rules"""
        return {
            # Python files - intelligence and automation
            '.py': {
                'patterns': {
                    r'.*orchestrat.*': 'automation/core',
                    r'.*intelligence.*': 'automation/core', 
                    r'.*governance.*': 'automation/core',
                    r'.*performance.*': 'automation/core',
                    r'.*monitor.*': 'automation/core',
                    r'.*test.*': 'automation/testing',
                    r'.*validation.*': 'automation/testing',
                    r'.*script.*': 'automation/scripts',
                    r'.*config.*': 'automation/config'
                },
                'default': 'automation/core'
            },
            
            # Shell scripts - operational automation
            '.sh': {
                'patterns': {
                    r'.*test.*': 'automation/testing',
                    r'.*validation.*': 'automation/testing',
                    r'.*git.*': 'automation/scripts',
                    r'.*deploy.*': 'automation/scripts',
                    r'.*setup.*': 'automation/scripts'
                },
                'default': 'automation/scripts'
            },
            
            # JavaScript - web and build automation
            '.js': {
                'patterns': {
                    r'.*dashboard.*': 'automation/scripts/web',
                    r'.*realtime.*': 'automation/scripts/web',
                    r'.*build.*': 'automation/scripts/build',
                    r'.*sync.*': 'automation/scripts'
                },
                'default': 'automation/scripts'
            },
            
            # Configuration files
            '.json': {'default': 'automation/config'},
            '.yaml': {'default': 'automation/config'},
            '.yml': {'default': 'automation/config'},
            '.toml': {'default': 'automation/config'},
            '.ini': {'default': 'automation/config'},
            
            # Documentation files
            '.md': {
                'patterns': {
                    r'.*template.*': 'templates/documents',
                    r'.*standard.*': 'docs/standards',
                    r'.*implementation.*': 'docs/implementation',
                    r'.*spec.*': 'docs/active',
                    r'.*guide.*': 'docs/implementation',
                    r'.*reference.*': 'docs/reference',
                    r'.*index.*': 'docs/reference',
                    r'README': 'docs/reference'
                },
                'default': 'docs/active'
            }
        }
    
    def classify_file(self, file_path: Path) -> str:
        """Classify a single file based on taxonomy rules"""
        ext = file_path.suffix.lower()
        filename = file_path.name.lower()
        
        if ext not in self.classification_rules:
            return None  # Skip unknown file types
            
        rules = self.classification_rules[ext]
        
        # Check pattern matches
        if 'patterns' in rules:
            for pattern, destination in rules['patterns'].items():
                if re.search(pattern, filename):
                    return destination
        
        # Return default location
        return rules.get('default', 'docs/active')
    
    def scan_and_classify(self) -> Dict[str, List[Tuple[Path, str]]]:
        """Scan project and classify all files"""
        classifications = {}
        
        # Skip certain directories
        skip_dirs = {'.git', '.archive', 'rollback', 'node_modules', '__pycache__'}
        
        for root, dirs, files in os.walk(self.project_root):
            # Remove skip directories from dirs to prevent walking them
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            root_path = Path(root)
            for file in files:
                file_path = root_path / file
                classification = self.classify_file(file_path)
                
                if classification:
                    if classification not in classifications:
                        classifications[classification] = []
                    classifications[classification].append((file_path, classification))
        
        return classifications
    
    def preview_classification(self) -> Dict[str, int]:
        """Preview classification without moving files"""
        classifications = self.scan_and_classify()
        
        preview = {}
        for destination, files in classifications.items():
            preview[destination] = len(files)
            
        return preview
    
    def apply_classification(self, dry_run: bool = True) -> Dict[str, List[str]]:
        """Apply file classification (move files to organized structure)"""
        classifications = self.scan_and_classify()
        results = {'moved': [], 'errors': [], 'skipped': []}
        
        for destination, files in classifications.items():
            # Create destination directory
            dest_path = self.project_root / destination
            if not dry_run:
                dest_path.mkdir(parents=True, exist_ok=True)
            
            for file_path, _ in files:
                try:
                    # Skip if file is already in correct location
                    if dest_path in file_path.parents:
                        results['skipped'].append(str(file_path))
                        continue
                    
                    # Calculate new file path
                    new_path = dest_path / file_path.name
                    
                    # Handle naming conflicts
                    counter = 1
                    while new_path.exists():
                        stem = file_path.stem
                        suffix = file_path.suffix
                        new_path = dest_path / f"{stem}-{counter}{suffix}"
                        counter += 1
                    
                    if not dry_run:
                        shutil.move(str(file_path), str(new_path))
                    
                    results['moved'].append(f"{file_path} -> {new_path}")
                    
                except Exception as e:
                    results['errors'].append(f"Error moving {file_path}: {str(e)}")
        
        return results


def main():
    """Main execution function"""
    import sys
    
    if len(sys.argv) < 2:
        project_root = "/Users/nalve/ce-simple"
    else:
        project_root = sys.argv[1]
    
    classifier = TaxonomyClassifier(project_root)
    
    # Preview classification
    print("=== TAXONOMY CLASSIFICATION PREVIEW ===")
    preview = classifier.preview_classification()
    
    total_files = sum(preview.values())
    print(f"Total files to classify: {total_files}")
    print()
    
    for destination, count in sorted(preview.items()):
        print(f"{destination:30} {count:4d} files")
    
    print("\n=== PREDICTABILITY ANALYSIS ===")
    predictable = sum(1 for dest in preview.keys() if '/' in dest)
    total_categories = len(preview)
    predictability = (predictable / total_categories * 100) if total_categories > 0 else 0
    print(f"Predictability: {predictability:.1f}% ({predictable}/{total_categories} categories)")
    
    # Dry run application
    print("\n=== DRY RUN RESULTS ===")
    results = classifier.apply_classification(dry_run=True)
    
    print(f"Files to move: {len(results['moved'])}")
    print(f"Files to skip: {len(results['skipped'])}")
    print(f"Potential errors: {len(results['errors'])}")
    
    if results['errors']:
        print("\nPotential errors:")
        for error in results['errors'][:5]:  # Show first 5 errors
            print(f"  {error}")


if __name__ == "__main__":
    main()