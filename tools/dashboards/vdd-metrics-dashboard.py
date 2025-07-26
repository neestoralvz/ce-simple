#!/usr/bin/env python3
"""
VDD Metrics Dashboard - Token Economy Tracking for Vision Driven Development

Tracks 12 specific metrics for VDD framework focusing on:
- Token density optimization
- Context economy efficiency  
- User-input/ vs docs/ balance
- Automated background calculations

Usage: python3 vdd-metrics-dashboard.py [--watch] [--json] [--file FILE]
"""

import os
import sys
import json
import time
import hashlib
import difflib
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict
import argparse
import re
from typing import Dict, List, Tuple, Optional, Set


class VDDMetricsEngine:
    """Core engine for calculating VDD metrics"""
    
    def __init__(self, project_root: str = "/Users/nalve/ce-simple"):
        self.project_root = Path(project_root)
        self.user_input_path = self.project_root / "user-input"
        self.docs_path = self.project_root / "docs"
        self.export_path = self.project_root / "export"
        self.cache = {}
        self.file_stats = {}
        
    def scan_project_files(self) -> Dict[str, Dict]:
        """Scan all project files and collect basic stats"""
        file_data = {}
        
        for path in [self.user_input_path, self.docs_path, self.export_path]:
            if path.exists():
                for file_path in path.rglob("*.md"):
                    rel_path = file_path.relative_to(self.project_root)
                    try:
                        content = file_path.read_text(encoding='utf-8')
                        lines = content.splitlines()
                        
                        file_data[str(rel_path)] = {
                            'path': file_path,
                            'relative_path': str(rel_path),
                            'content': content,
                            'lines': lines,
                            'line_count': len(lines),
                            'token_count': len(content.split()),
                            'char_count': len(content),
                            'modified_time': file_path.stat().st_mtime,
                            'category': self._categorize_file(rel_path),
                            'content_hash': hashlib.md5(content.encode()).hexdigest()
                        }
                    except Exception as e:
                        print(f"Warning: Could not read {file_path}: {e}")
                        
        return file_data
    
    def _categorize_file(self, rel_path: Path) -> str:
        """Categorize file based on its location"""
        parts = rel_path.parts
        if 'user-input' in parts:
            return 'user-input'
        elif 'docs' in parts:
            return 'docs'
        elif 'export' in parts:
            return 'export'
        else:
            return 'other'
    
    def calculate_all_metrics(self, file_data: Dict[str, Dict]) -> Dict[str, Dict]:
        """Calculate all 12 VDD metrics"""
        metrics = {}
        
        for file_path, data in file_data.items():
            file_metrics = {}
            
            # 1. Token Density: Valuable information / total tokens (0-1 score)
            file_metrics['token_density'] = self._calculate_token_density(data)
            
            # 2. Cross-Reference Count: References to each file
            file_metrics['cross_reference_count'] = self._calculate_cross_references(file_path, file_data)
            
            # 3. Content Age: Days since last significant update
            file_metrics['content_age'] = self._calculate_content_age(data)
            
            # 4. File Length: Current lines vs recommended limit
            file_metrics['file_length'] = self._calculate_file_length_ratio(data)
            
            # 5. Duplication Score: Similarity with other files (0-100%)
            file_metrics['duplication_score'] = self._calculate_duplication_score(file_path, file_data)
            
            # 6. User Input Ratio: % content user-input/ vs docs/
            file_metrics['user_input_ratio'] = self._calculate_user_input_ratio(data, file_data)
            
            # 7. Navigation Health: % files with READMEs navigation
            file_metrics['navigation_health'] = self._calculate_navigation_health(file_path, file_data)
            
            # 8. Modularization Index: Average files per concept
            file_metrics['modularization_index'] = self._calculate_modularization_index(data, file_data)
            
            # 9. Implementation Gap: Ideas in user-input/ without docs/ derivatives
            file_metrics['implementation_gap'] = self._calculate_implementation_gap(data, file_data)
            
            # 10. Session Efficiency: Ideas captured / time session (estimated)
            file_metrics['session_efficiency'] = self._calculate_session_efficiency(data)
            
            # 11. Context Reuse: Frequency of referencing existing content
            file_metrics['context_reuse'] = self._calculate_context_reuse(data, file_data)
            
            # 12. Challenge Success: Ideas refined after challenges
            file_metrics['challenge_success'] = self._calculate_challenge_success(data)
            
            metrics[file_path] = file_metrics
            
        return metrics
    
    def _calculate_token_density(self, data: Dict) -> float:
        """Calculate valuable information density (heuristic-based)"""
        content = data['content']
        total_tokens = data['token_count']
        
        if total_tokens == 0:
            return 0.0
            
        # Count "valuable" indicators
        valuable_patterns = [
            r'\*\*[^*]+\*\*',  # Bold text (important concepts)
            r'`[^`]+`',        # Code snippets
            r'#{1,6}\s+.+',    # Headers
            r'^\s*[-*+]\s+',   # List items
            r'@[a-zA-Z0-9/_-]+\.md',  # References
            r'https?://[^\s]+', # URLs
            r'\[[^\]]+\]\([^\)]+\)',  # Links
        ]
        
        valuable_tokens = 0
        for pattern in valuable_patterns:
            matches = re.findall(pattern, content, re.MULTILINE)
            valuable_tokens += sum(len(match.split()) for match in matches)
        
        return min(1.0, valuable_tokens / total_tokens)
    
    def _calculate_cross_references(self, target_file: str, file_data: Dict[str, Dict]) -> int:
        """Count references to this file from other files"""
        target_name = Path(target_file).stem
        count = 0
        
        for file_path, data in file_data.items():
            if file_path == target_file:
                continue
                
            content = data['content']
            # Look for various reference patterns
            patterns = [
                f"{target_name}.md",
                f"@{target_file}",
                f"[{target_name}]",
                f"/{target_name}/",
            ]
            
            for pattern in patterns:
                if pattern in content:
                    count += content.count(pattern)
                    
        return count
    
    def _calculate_content_age(self, data: Dict) -> int:
        """Calculate days since last modification"""
        modified_time = data['modified_time']
        current_time = time.time()
        age_seconds = current_time - modified_time
        return int(age_seconds / (24 * 3600))  # Convert to days
    
    def _calculate_file_length_ratio(self, data: Dict) -> float:
        """Calculate current lines vs recommended limit"""
        current_lines = data['line_count']
        
        # VDD recommended limits based on file type
        category = data.get('category', 'other')
        limits = {
            'user-input': 200,  # Sacred space can be longer
            'docs': 100,       # Structured docs should be concise
            'export': 150,     # Commands need detail but not excessive
            'other': 100
        }
        
        recommended_limit = limits.get(category, 100)
        return current_lines / recommended_limit
    
    def _calculate_duplication_score(self, target_file: str, file_data: Dict[str, Dict]) -> float:
        """Calculate similarity with other files (0-100%)"""
        target_content = file_data[target_file]['content']
        target_lines = set(line.strip() for line in target_content.splitlines() if line.strip())
        
        if not target_lines:
            return 0.0
            
        max_similarity = 0.0
        
        for file_path, data in file_data.items():
            if file_path == target_file:
                continue
                
            other_lines = set(line.strip() for line in data['content'].splitlines() if line.strip())
            if not other_lines:
                continue
                
            # Calculate Jaccard similarity
            intersection = len(target_lines.intersection(other_lines))
            union = len(target_lines.union(other_lines))
            
            if union > 0:
                similarity = intersection / union
                max_similarity = max(max_similarity, similarity)
        
        return max_similarity * 100
    
    def _calculate_user_input_ratio(self, data: Dict, file_data: Dict[str, Dict]) -> float:
        """Calculate % content from user-input/ vs docs/"""
        category = data.get('category', 'other')
        
        if category == 'user-input':
            return 1.0  # 100% user input
        elif category == 'docs':
            # Check if this docs file has user-input derivatives
            file_path = data['relative_path']
            has_user_input_source = self._find_user_input_source(file_path, file_data)
            return 0.3 if has_user_input_source else 0.1  # Some derivative content
        else:
            return 0.5  # Mixed/other content
    
    def _find_user_input_source(self, docs_file: str, file_data: Dict[str, Dict]) -> bool:
        """Check if docs file has corresponding user-input source"""
        docs_name = Path(docs_file).stem
        
        for file_path, data in file_data.items():
            if data.get('category') == 'user-input':
                if docs_name in file_path or Path(file_path).stem in docs_name:
                    return True
        return False
    
    def _calculate_navigation_health(self, target_file: str, file_data: Dict[str, Dict]) -> float:
        """Calculate navigation health based on README presence"""
        target_dir = Path(target_file).parent
        
        # Count files in same directory
        dir_files = [f for f in file_data.keys() if Path(f).parent == target_dir]
        
        if not dir_files:
            return 1.0
            
        # Check for README in same directory
        readme_exists = any('README' in Path(f).name.upper() for f in dir_files)
        
        return 1.0 if readme_exists else 0.0
    
    def _calculate_modularization_index(self, data: Dict, file_data: Dict[str, Dict]) -> float:
        """Calculate average files per concept (lower is better modularization)"""
        category = data.get('category', 'other')
        
        # Count files in same category
        category_files = [f for f, d in file_data.items() if d.get('category') == category]
        
        # Estimate concepts by unique directory depth levels
        concept_dirs = set(Path(f).parent for f in category_files)
        
        if not concept_dirs:
            return 1.0
            
        return len(category_files) / len(concept_dirs)
    
    def _calculate_implementation_gap(self, data: Dict, file_data: Dict[str, Dict]) -> float:
        """Calculate implementation gap - ideas without derivatives"""
        category = data.get('category', 'other')
        
        if category != 'user-input':
            return 0.0  # Only applies to user-input files
            
        # Check if this user-input file has corresponding docs implementation
        user_input_path = data['relative_path']
        file_name = Path(user_input_path).stem
        
        # Look for docs files that might be derivatives
        has_implementation = False
        for file_path, file_data_item in file_data.items():
            if file_data_item.get('category') == 'docs':
                if file_name in file_path or any(word in file_path for word in file_name.split('-')):
                    has_implementation = True
                    break
        
        return 0.0 if has_implementation else 1.0
    
    def _calculate_session_efficiency(self, data: Dict) -> float:
        """Estimate session efficiency based on content density and recency"""
        content_age = self._calculate_content_age(data)
        token_density = self._calculate_token_density(data)
        
        # More recent files with high density indicate efficient sessions
        if content_age <= 1:  # Same day
            efficiency = token_density * 1.0
        elif content_age <= 7:  # Same week
            efficiency = token_density * 0.7
        else:
            efficiency = token_density * 0.3
            
        return efficiency
    
    def _calculate_context_reuse(self, data: Dict, file_data: Dict[str, Dict]) -> float:
        """Calculate frequency of referencing existing content"""
        content = data['content']
        
        # Count reference patterns
        reference_patterns = [
            r'@[a-zA-Z0-9/_-]+\.md',  # @ imports
            r'\[[^\]]+\]\([^\)]+\.md\)',  # Markdown links to other files
            r'See also|References|Links to',  # Explicit reference sections
            r'docs/[a-zA-Z0-9/_-]+\.md',  # Direct file references
        ]
        
        total_references = 0
        total_tokens = data['token_count']
        
        for pattern in reference_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            total_references += len(matches)
        
        if total_tokens == 0:
            return 0.0
            
        return min(1.0, total_references / (total_tokens / 100))  # Normalize per 100 tokens
    
    def _calculate_challenge_success(self, data: Dict) -> float:
        """Calculate ideas refined after challenges (heuristic)"""
        content = data['content'].lower()
        
        # Look for refinement indicators
        refinement_indicators = [
            'updated:', 'revised:', 'refined:', 'improved:',
            'feedback:', 'challenge:', 'iteration:',
            'v2', 'v3', 'version', 'evolution',
            'after discussion', 'refined after', 'updated after'
        ]
        
        refinement_count = sum(1 for indicator in refinement_indicators if indicator in content)
        
        # Normalize based on file size
        lines = data['line_count']
        if lines == 0:
            return 0.0
            
        return min(1.0, refinement_count / (lines / 50))  # Per 50 lines


class VDDDashboard:
    """Dashboard interface for VDD metrics"""
    
    def __init__(self, project_root: str = "/Users/nalve/ce-simple"):
        self.engine = VDDMetricsEngine(project_root)
        
    def generate_report(self, output_format: str = 'text') -> str:
        """Generate comprehensive metrics report"""
        print("🔍 Scanning VDD project files...")
        file_data = self.engine.scan_project_files()
        
        print(f"📊 Calculating metrics for {len(file_data)} files...")
        metrics = self.engine.calculate_all_metrics(file_data)
        
        if output_format == 'json':
            return self._generate_json_report(metrics, file_data)
        else:
            return self._generate_text_report(metrics, file_data)
    
    def _generate_text_report(self, metrics: Dict[str, Dict], file_data: Dict[str, Dict]) -> str:
        """Generate human-readable text report"""
        report = []
        report.append("=" * 80)
        report.append("🎯 VDD METRICS DASHBOARD - TOKEN ECONOMY TRACKING")
        report.append("=" * 80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Files analyzed: {len(file_data)}")
        report.append("")
        
        # Aggregate metrics summary
        report.append("📈 AGGREGATE METRICS SUMMARY")
        report.append("-" * 40)
        
        totals = self._calculate_aggregate_metrics(metrics, file_data)
        for metric_name, value in totals.items():
            report.append(f"{metric_name:25}: {value:.3f}")
        
        report.append("")
        
        # Category breakdown
        report.append("📂 CATEGORY BREAKDOWN")
        report.append("-" * 40)
        
        categories = defaultdict(list)
        for file_path, data in file_data.items():
            categories[data.get('category', 'other')].append(file_path)
        
        for category, files in categories.items():
            report.append(f"{category:15}: {len(files):3} files")
        
        report.append("")
        
        # Top issues/opportunities
        report.append("⚠️  TOP OPTIMIZATION OPPORTUNITIES")
        report.append("-" * 40)
        
        issues = self._identify_top_issues(metrics, file_data)
        for issue in issues[:10]:  # Top 10
            report.append(f"• {issue}")
        
        report.append("")
        
        # Per-file metrics (top 20 by priority)
        report.append("📋 PER-FILE METRICS (Top 20 Priority Files)")
        report.append("-" * 80)
        
        # Sort files by combined priority score
        priority_files = self._get_priority_files(metrics, file_data)[:20]
        
        for file_path, priority_score in priority_files:
            file_metrics = metrics[file_path]
            data = file_data[file_path]
            
            report.append(f"\n📄 {file_path}")
            report.append(f"   Category: {data.get('category', 'other'):12} | "
                         f"Lines: {data['line_count']:3} | "
                         f"Age: {file_metrics['content_age']:3}d | "
                         f"Priority: {priority_score:.2f}")
            
            # Show key metrics in columns
            report.append(f"   Token Density: {file_metrics['token_density']:.3f} | "
                         f"Cross-Refs: {file_metrics['cross_reference_count']:2} | "
                         f"Duplication: {file_metrics['duplication_score']:5.1f}% | "
                         f"Length Ratio: {file_metrics['file_length']:.2f}")
            
            report.append(f"   User Input: {file_metrics['user_input_ratio']:6.3f} | "
                         f"Nav Health: {file_metrics['navigation_health']:.3f} | "
                         f"Context Reuse: {file_metrics['context_reuse']:.3f} | "
                         f"Session Eff: {file_metrics['session_efficiency']:.3f}")
        
        report.append("")
        report.append("=" * 80)
        report.append("🎯 Analysis complete - VDD token economy optimized")
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def _generate_json_report(self, metrics: Dict[str, Dict], file_data: Dict[str, Dict]) -> str:
        """Generate JSON report for programmatic use"""
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'files_analyzed': len(file_data),
                'aggregate_metrics': self._calculate_aggregate_metrics(metrics, file_data),
                'category_breakdown': self._get_category_breakdown(file_data),
                'top_issues': self._identify_top_issues(metrics, file_data)[:10]
            },
            'file_metrics': metrics,
            'file_data': {
                path: {
                    'category': data.get('category'),
                    'line_count': data['line_count'],
                    'token_count': data['token_count'],
                    'content_age': metrics[path]['content_age']
                }
                for path, data in file_data.items()
            }
        }
        
        return json.dumps(report_data, indent=2)
    
    def _calculate_aggregate_metrics(self, metrics: Dict[str, Dict], file_data: Dict[str, Dict]) -> Dict[str, float]:
        """Calculate aggregate metrics across all files"""
        if not metrics:
            return {}
            
        totals = defaultdict(list)
        
        for file_metrics in metrics.values():
            for metric_name, value in file_metrics.items():
                if isinstance(value, (int, float)):
                    totals[metric_name].append(value)
        
        # Calculate averages
        aggregates = {}
        for metric_name, values in totals.items():
            if values:
                aggregates[metric_name] = sum(values) / len(values)
        
        # Add some specialized aggregates
        user_input_files = sum(1 for data in file_data.values() if data.get('category') == 'user-input')
        docs_files = sum(1 for data in file_data.values() if data.get('category') == 'docs')
        
        aggregates['user_input_vs_docs_ratio'] = user_input_files / max(1, docs_files)
        aggregates['total_token_count'] = sum(data['token_count'] for data in file_data.values())
        aggregates['avg_file_age'] = sum(metrics[path]['content_age'] for path in metrics) / len(metrics)
        
        return aggregates
    
    def _get_category_breakdown(self, file_data: Dict[str, Dict]) -> Dict[str, int]:
        """Get file count breakdown by category"""
        categories = defaultdict(int)
        for data in file_data.values():
            categories[data.get('category', 'other')] += 1
        return dict(categories)
    
    def _identify_top_issues(self, metrics: Dict[str, Dict], file_data: Dict[str, Dict]) -> List[str]:
        """Identify top optimization opportunities"""
        issues = []
        
        # High duplication files
        high_dup = [(path, m['duplication_score']) for path, m in metrics.items() 
                   if m['duplication_score'] > 50]
        high_dup.sort(key=lambda x: x[1], reverse=True)
        for path, score in high_dup[:5]:
            issues.append(f"High duplication in {path}: {score:.1f}%")
        
        # Long files
        long_files = [(path, m['file_length']) for path, m in metrics.items() 
                     if m['file_length'] > 1.5]
        long_files.sort(key=lambda x: x[1], reverse=True)
        for path, ratio in long_files[:5]:
            issues.append(f"Oversized file {path}: {ratio:.1f}x recommended length")
        
        # Old files
        old_files = [(path, m['content_age']) for path, m in metrics.items() 
                    if m['content_age'] > 30]
        old_files.sort(key=lambda x: x[1], reverse=True)
        for path, age in old_files[:3]:
            issues.append(f"Stale content in {path}: {age} days old")
        
        # Implementation gaps
        gaps = [(path, m['implementation_gap']) for path, m in metrics.items() 
               if m['implementation_gap'] > 0.5]
        for path, gap in gaps:
            issues.append(f"Implementation gap: {path} needs docs/ derivative")
        
        # Low token density
        low_density = [(path, m['token_density']) for path, m in metrics.items() 
                      if m['token_density'] < 0.3]
        low_density.sort(key=lambda x: x[1])
        for path, density in low_density[:3]:
            issues.append(f"Low information density in {path}: {density:.3f}")
        
        return issues
    
    def _get_priority_files(self, metrics: Dict[str, Dict], file_data: Dict[str, Dict]) -> List[Tuple[str, float]]:
        """Get files sorted by priority score for attention"""
        priority_scores = []
        
        for file_path, file_metrics in metrics.items():
            data = file_data[file_path]
            
            # Calculate priority score (higher = needs more attention)
            score = 0
            
            # High duplication increases priority
            score += file_metrics['duplication_score'] / 100 * 2
            
            # Large files increase priority
            score += max(0, file_metrics['file_length'] - 1) * 1.5
            
            # Old content increases priority
            score += min(2, file_metrics['content_age'] / 30)
            
            # Implementation gaps increase priority
            score += file_metrics['implementation_gap'] * 3
            
            # Low token density increases priority
            score += max(0, 0.5 - file_metrics['token_density']) * 2
            
            # User-input files get priority boost
            if data.get('category') == 'user-input':
                score += 1
            
            priority_scores.append((file_path, score))
        
        return sorted(priority_scores, key=lambda x: x[1], reverse=True)


def main():
    """Main dashboard application"""
    parser = argparse.ArgumentParser(description='VDD Metrics Dashboard - Token Economy Tracking')
    parser.add_argument('--watch', action='store_true', 
                       help='Run in watch mode (continuous monitoring)')
    parser.add_argument('--json', action='store_true',
                       help='Output in JSON format')
    parser.add_argument('--file', type=str,
                       help='Analyze specific file only')
    parser.add_argument('--project-root', type=str, default='/Users/nalve/ce-simple',
                       help='Project root directory')
    
    args = parser.parse_args()
    
    dashboard = VDDDashboard(args.project_root)
    
    if args.watch:
        print("🔄 Starting VDD metrics monitoring (Ctrl+C to stop)...")
        try:
            while True:
                print("\n" + "="*80)
                print(f"🕐 {datetime.now().strftime('%H:%M:%S')} - Refreshing metrics...")
                report = dashboard.generate_report('json' if args.json else 'text')
                print(report)
                time.sleep(60)  # Update every minute
        except KeyboardInterrupt:
            print("\n👋 VDD metrics monitoring stopped.")
    else:
        # Single run
        report = dashboard.generate_report('json' if args.json else 'text')
        print(report)


if __name__ == '__main__':
    main()