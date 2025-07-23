#!/usr/bin/env python3
"""
Taxonomy Validation System
Validates >95% file location predictability and taxonomy compliance
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class ValidationResult:
    """Validation result for a single file or category"""
    path: str
    expected_location: str
    actual_location: str
    is_compliant: bool
    reason: str = ""

class TaxonomyValidator:
    """Validates taxonomy compliance and predictability"""
    
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.expected_patterns = self._build_expected_patterns()
        
    def _build_expected_patterns(self) -> Dict[str, Dict]:
        """Build expected file location patterns"""
        return {
            # Python files - core intelligence and automation
            'python': {
                'extensions': ['.py'],
                'patterns': {
                    r'.*orchestrat.*': 'automation/core',
                    r'.*intelligence.*': 'automation/core',
                    r'.*governance.*': 'automation/core', 
                    r'.*performance.*': 'automation/core',
                    r'.*monitor.*': 'automation/core',
                    r'.*test.*': 'automation/testing',
                    r'.*validation.*': 'automation/testing'
                },
                'default': 'automation/core'
            },
            
            # Shell scripts - operational automation
            'shell': {
                'extensions': ['.sh'],
                'patterns': {
                    r'.*test.*': 'automation/testing',
                    r'.*validation.*': 'automation/testing'
                },
                'default': 'automation/scripts'
            },
            
            # JavaScript - web and build
            'javascript': {
                'extensions': ['.js'],
                'default': 'automation/scripts'
            },
            
            # Configuration files
            'config': {
                'extensions': ['.json', '.yaml', '.yml', '.toml', '.ini'],
                'default': 'automation/config'
            },
            
            # Documentation
            'markdown': {
                'extensions': ['.md'],
                'patterns': {
                    r'.*template.*': 'templates/documents',
                    r'.*standard.*': 'docs/standards',
                    r'.*implementation.*': 'docs/implementation',
                    r'README': 'docs/reference'
                },
                'default': 'docs/active'
            }
        }
    
    def _get_expected_location(self, file_path: Path) -> str:
        """Get expected location for a file based on taxonomy rules"""
        ext = file_path.suffix.lower()
        filename = file_path.name.lower()
        
        # Find matching category
        for category, rules in self.expected_patterns.items():
            if ext in rules['extensions']:
                # Check pattern matches
                if 'patterns' in rules:
                    for pattern, location in rules['patterns'].items():
                        if re.search(pattern, filename):
                            return location
                
                # Return default location
                return rules['default']
        
        return None  # Unknown file type
    
    def _get_actual_location(self, file_path: Path) -> str:
        """Get actual location category of a file"""
        # Get relative path from project root
        try:
            rel_path = file_path.relative_to(self.project_root)
            parts = rel_path.parts
            
            if len(parts) >= 2:
                return f"{parts[0]}/{parts[1]}"
            elif len(parts) >= 1:
                return parts[0]
            else:
                return "root"
        except ValueError:
            return "external"
    
    def validate_file_location(self, file_path: Path) -> ValidationResult:
        """Validate a single file's location"""
        expected = self._get_expected_location(file_path)
        actual = self._get_actual_location(file_path)
        
        if expected is None:
            return ValidationResult(
                path=str(file_path),
                expected_location="N/A",
                actual_location=actual,
                is_compliant=True,  # Unknown files are considered compliant
                reason="Unknown file type"
            )
        
        is_compliant = expected == actual
        reason = "Compliant" if is_compliant else f"Expected {expected}, found {actual}"
        
        return ValidationResult(
            path=str(file_path),
            expected_location=expected,
            actual_location=actual,
            is_compliant=is_compliant,
            reason=reason
        )
    
    def scan_project_files(self) -> List[Path]:
        """Scan project for relevant files"""
        files = []
        skip_dirs = {'.git', '.archive', 'rollback', 'node_modules', '__pycache__'}
        
        for root, dirs, filenames in os.walk(self.project_root):
            # Skip unwanted directories
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            root_path = Path(root)
            for filename in filenames:
                file_path = root_path / filename
                
                # Only include files we have rules for
                if self._get_expected_location(file_path) is not None:
                    files.append(file_path)
        
        return files
    
    def validate_taxonomy(self) -> Dict[str, any]:
        """Validate entire project taxonomy"""
        files = self.scan_project_files()
        results = []
        
        compliant_count = 0
        category_stats = defaultdict(lambda: {'total': 0, 'compliant': 0})
        
        for file_path in files:
            result = self.validate_file_location(file_path)
            results.append(result)
            
            if result.is_compliant:
                compliant_count += 1
            
            # Track category statistics
            category = result.expected_location
            category_stats[category]['total'] += 1
            if result.is_compliant:
                category_stats[category]['compliant'] += 1
        
        total_files = len(results)
        predictability = (compliant_count / total_files * 100) if total_files > 0 else 0
        
        return {
            'total_files': total_files,
            'compliant_files': compliant_count,
            'predictability': predictability,
            'meets_target': predictability >= 95.0,
            'category_stats': dict(category_stats),
            'violations': [r for r in results if not r.is_compliant],
            'all_results': results
        }
    
    def generate_report(self) -> str:
        """Generate detailed validation report"""
        validation = self.validate_taxonomy()
        
        report = []
        report.append("=" * 60)
        report.append("TAXONOMY VALIDATION REPORT")
        report.append("=" * 60)
        
        # Summary statistics
        report.append(f"\nSUMMARY:")
        report.append(f"Total files analyzed: {validation['total_files']}")
        report.append(f"Compliant files: {validation['compliant_files']}")
        report.append(f"Predictability: {validation['predictability']:.1f}%")
        report.append(f"Target (95%): {'✓ PASS' if validation['meets_target'] else '✗ FAIL'}")
        
        # Category breakdown
        report.append(f"\nCATEGORY BREAKDOWN:")
        for category, stats in validation['category_stats'].items():
            compliance = (stats['compliant'] / stats['total'] * 100) if stats['total'] > 0 else 0
            report.append(f"{category:25} {stats['compliant']:3d}/{stats['total']:3d} ({compliance:5.1f}%)")
        
        # Violations (if any)
        if validation['violations']:
            report.append(f"\nVIOLATIONS ({len(validation['violations'])}):")
            for violation in validation['violations'][:10]:  # Show first 10
                report.append(f"  {Path(violation.path).name}")
                report.append(f"    Expected: {violation.expected_location}")
                report.append(f"    Actual:   {violation.actual_location}")
                report.append(f"    Reason:   {violation.reason}")
        
        # Recommendations
        report.append("\nRECOMMENDATIONS:")
        if validation['meets_target']:
            report.append("✓ Taxonomy system meets predictability target")
            report.append("✓ File organization is highly predictable")
        else:
            report.append("• Review file placement for taxonomy compliance")
            report.append("• Consider running taxonomy classifier to reorganize files")
            report.append("• Update classification rules if needed")
        
        return "\n".join(report)


def main():
    """Main execution function"""
    import sys
    
    if len(sys.argv) < 2:
        project_root = "/Users/nalve/ce-simple"
    else:
        project_root = sys.argv[1]
    
    validator = TaxonomyValidator(project_root)
    report = validator.generate_report()
    print(report)


if __name__ == "__main__":
    main()