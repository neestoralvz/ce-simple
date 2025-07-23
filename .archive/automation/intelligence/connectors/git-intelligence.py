#!/usr/bin/env python3
"""
Git Intelligence Analyzer - Historical Intelligence Phase 1
==========================================================

**Purpose**: Analyze git history for development patterns, velocity metrics, and 
implementation intelligence extraction.

**Authority Integration**: Historical Intelligence Architecture (Principle #110)
**P55/P56 Compliance**: MANDATORY git pattern analysis integration

This script implements Tier 1 git intelligence analysis for /system-update,
/knowledge-sync, and /intelligent-reorganization commands.
"""

import os
import subprocess
import json
import datetime
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import argparse
from collections import defaultdict, Counter


@dataclass
class CommitPattern:
    """Structure for commit pattern analysis"""
    pattern_type: str
    frequency: int
    files_affected: List[str]
    success_indicators: List[str]
    temporal_distribution: Dict[str, int]
    velocity_metrics: Dict[str, float]


@dataclass
class GitIntelligenceResults:
    """Complete git intelligence analysis results"""
    analysis_period: str
    total_commits: int
    active_files: int
    development_velocity: Dict[str, float]
    commit_patterns: List[CommitPattern]
    high_activity_areas: List[str]
    optimization_opportunities: List[str]
    file_correlation_matrix: Dict[str, List[str]]
    metadata: Dict[str, Any]


class GitIntelligenceAnalyzer:
    """Core git intelligence analysis engine"""
    
    def __init__(self, repo_path: str = None):
        """Initialize analyzer with repository path"""
        self.repo_path = repo_path or os.getcwd()
        self.git_cache = {}
        self.analysis_results = None
        
    def _run_git_command(self, command: List[str]) -> str:
        """Execute git command and return output"""
        try:
            result = subprocess.run(
                ['git'] + command,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"❌ Git command failed: {' '.join(command)}")
            print(f"Error: {e.stderr}")
            return ""
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return ""
    
    def get_commit_history(self, days: int = 30, max_commits: int = 1000) -> List[Dict[str, Any]]:
        """Get commit history for analysis"""
        since_date = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime('%Y-%m-%d')
        
        # Get commit log with detailed format
        log_format = '--pretty=format:{"hash":"%H","author":"%an","date":"%ai","message":"%s","stats":"%+"}||'
        
        log_output = self._run_git_command([
            'log',
            f'--since={since_date}',
            f'--max-count={max_commits}',
            log_format,
            '--stat',
            '--no-merges'
        ])
        
        commits = []
        if log_output:
            # Parse commit entries
            commit_entries = log_output.split('||')
            for entry in commit_entries:
                if entry.strip():
                    try:
                        # Clean up the entry and parse JSON part
                        json_part = entry.split('\n')[0]
                        commit_data = json.loads(json_part)
                        
                        # Get file changes for this commit
                        files_changed = self._get_commit_files(commit_data['hash'])
                        commit_data['files_changed'] = files_changed
                        commit_data['file_count'] = len(files_changed)
                        
                        commits.append(commit_data)
                    except (json.JSONDecodeError, KeyError) as e:
                        continue
        
        print(f"📊 Commits analizados: {len(commits)}")
        return commits
    
    def _get_commit_files(self, commit_hash: str) -> List[str]:
        """Get files changed in a specific commit"""
        files_output = self._run_git_command([
            'show', '--name-only', '--pretty=format:', commit_hash
        ])
        
        files = [f.strip() for f in files_output.split('\n') if f.strip()]
        return files
    
    def analyze_development_velocity(self, commits: List[Dict[str, Any]]) -> Dict[str, float]:
        """Analyze development velocity metrics"""
        if not commits:
            return {}
        
        # Calculate velocity metrics
        total_commits = len(commits)
        
        # Parse dates more robustly
        def parse_git_date(date_str):
            # Handle different git date formats
            try:
                # Remove timezone info for simpler parsing
                date_clean = date_str.split(' ')[0] + ' ' + date_str.split(' ')[1]
                return datetime.datetime.strptime(date_clean, '%Y-%m-%d %H:%M:%S')
            except:
                # Fallback to current time
                return datetime.datetime.now()
        
        if len(commits) > 1:
            first_date = parse_git_date(commits[0]['date'])
            last_date = parse_git_date(commits[-1]['date'])
            days_span = abs((first_date - last_date).days) + 1
        else:
            days_span = 1
        
        total_files = sum(commit['file_count'] for commit in commits)
        
        velocity_metrics = {
            'commits_per_day': total_commits / max(days_span, 1),
            'files_per_commit': total_files / max(total_commits, 1),
            'files_per_day': total_files / max(days_span, 1),
            'total_commits': total_commits,
            'total_files_modified': total_files,
            'analysis_days': days_span
        }
        
        # Calculate hourly patterns
        hour_distribution = defaultdict(int)
        for commit in commits:
            try:
                dt = datetime.datetime.fromisoformat(commit['date'].replace('Z', '+00:00'))
                hour_distribution[dt.hour] += 1
            except (ValueError, KeyError):
                continue
        
        velocity_metrics['peak_hours'] = dict(hour_distribution)
        
        return velocity_metrics
    
    def identify_high_activity_areas(self, commits: List[Dict[str, Any]]) -> List[str]:
        """Identify high-activity file areas"""
        file_activity = Counter()
        
        for commit in commits:
            for file_path in commit.get('files_changed', []):
                # Extract directory path
                dir_path = os.path.dirname(file_path) if os.path.dirname(file_path) else 'root'
                file_activity[dir_path] += 1
                file_activity[file_path] += 1
        
        # Get top activity areas
        high_activity = [area for area, count in file_activity.most_common(20)]
        return high_activity
    
    def analyze_commit_patterns(self, commits: List[Dict[str, Any]]) -> List[CommitPattern]:
        """Analyze commit message patterns and categorize commits"""
        patterns = []
        
        # Define pattern categories
        pattern_categories = {
            'feature': [r'add\s+', r'implement\s+', r'create\s+', r'build\s+', r'new\s+'],
            'fix': [r'fix\s+', r'repair\s+', r'resolve\s+', r'correct\s+', r'patch\s+'],
            'update': [r'update\s+', r'modify\s+', r'change\s+', r'improve\s+', r'enhance\s+'],
            'docs': [r'docs?\s+', r'documentation\s+', r'readme\s+', r'comment\s+'],
            'refactor': [r'refactor\s+', r'reorganize\s+', r'restructure\s+', r'cleanup\s+'],
            'test': [r'test\s+', r'testing\s+', r'spec\s+', r'coverage\s+'],
            'config': [r'config\s+', r'configuration\s+', r'setup\s+', r'env\s+']
        }
        
        categorized_commits = defaultdict(list)
        
        for commit in commits:
            message = commit.get('message', '').lower()
            categorized = False
            
            for category, regexes in pattern_categories.items():
                for regex in regexes:
                    if re.search(regex, message):
                        categorized_commits[category].append(commit)
                        categorized = True
                        break
                if categorized:
                    break
            
            if not categorized:
                categorized_commits['other'].append(commit)
        
        # Create pattern objects
        for category, commits_in_category in categorized_commits.items():
            if commits_in_category:
                files_affected = []
                temporal_distribution = defaultdict(int)
                
                for commit in commits_in_category:
                    files_affected.extend(commit.get('files_changed', []))
                    
                    try:
                        dt = datetime.datetime.fromisoformat(commit['date'].replace('Z', '+00:00'))
                        day_key = dt.strftime('%Y-%m-%d')
                        temporal_distribution[day_key] += 1
                    except (ValueError, KeyError):
                        continue
                
                # Calculate velocity for this pattern
                days_span = len(temporal_distribution) if temporal_distribution else 1
                velocity_metrics = {
                    'commits_per_day': len(commits_in_category) / days_span,
                    'files_per_commit': len(files_affected) / len(commits_in_category),
                    'total_commits': len(commits_in_category)
                }
                
                pattern = CommitPattern(
                    pattern_type=category,
                    frequency=len(commits_in_category),
                    files_affected=list(set(files_affected)),
                    success_indicators=self._extract_success_indicators(commits_in_category),
                    temporal_distribution=dict(temporal_distribution),
                    velocity_metrics=velocity_metrics
                )
                patterns.append(pattern)
        
        return patterns
    
    def _extract_success_indicators(self, commits: List[Dict[str, Any]]) -> List[str]:
        """Extract success indicators from commit messages"""
        success_keywords = [
            'complete', 'success', 'working', 'fixed', 'resolved',
            'optimized', 'improved', 'enhanced', 'stable'
        ]
        
        indicators = []
        for commit in commits:
            message = commit.get('message', '').lower()
            for keyword in success_keywords:
                if keyword in message:
                    indicators.append(f"{keyword}: {commit.get('message', '')[:100]}")
        
        return indicators[:10]  # Top 10 indicators
    
    def calculate_file_correlation_matrix(self, commits: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """Calculate file co-modification correlation matrix"""
        file_comodification = defaultdict(set)
        
        for commit in commits:
            files_changed = commit.get('files_changed', [])
            # For each pair of files in the same commit, record correlation
            for i, file1 in enumerate(files_changed):
                for file2 in files_changed[i+1:]:
                    file_comodification[file1].add(file2)
                    file_comodification[file2].add(file1)
        
        # Convert to correlation matrix (top correlations per file)
        correlation_matrix = {}
        for file_path, correlated_files in file_comodification.items():
            # Limit to top 10 correlations per file
            correlation_matrix[file_path] = list(correlated_files)[:10]
        
        return correlation_matrix
    
    def identify_optimization_opportunities(self, commits: List[Dict[str, Any]], 
                                          patterns: List[CommitPattern]) -> List[str]:
        """Identify optimization opportunities based on git analysis"""
        opportunities = []
        
        # High-churn files (frequently modified)
        file_churn = Counter()
        for commit in commits:
            for file_path in commit.get('files_changed', []):
                file_churn[file_path] += 1
        
        high_churn_files = [f for f, count in file_churn.most_common(10) if count > 5]
        if high_churn_files:
            opportunities.append(f"Archivos con alta rotación requieren atención: {len(high_churn_files)} archivos")
        
        # Pattern-based opportunities
        for pattern in patterns:
            if pattern.pattern_type == 'fix' and pattern.frequency > 10:
                opportunities.append(f"Alta frecuencia de fixes ({pattern.frequency}) indica áreas problemáticas")
            
            if pattern.pattern_type == 'docs' and pattern.frequency > 15:
                opportunities.append(f"Alta actividad de documentación ({pattern.frequency}) indica área de crecimiento")
        
        # Development velocity opportunities
        total_commits = len(commits)
        if total_commits > 50:
            opportunities.append("Alto volumen de commits sugiere automatización de tareas repetitivas")
        
        # File correlation opportunities
        opportunities.append("Archivos frecuentemente modificados juntos candidatos para co-localización")
        
        return opportunities
    
    def generate_git_intelligence(self, timeframe_days: int = 30) -> GitIntelligenceResults:
        """Generate comprehensive git intelligence analysis"""
        print(f"📊 **GIT INTELLIGENCE ANALYSIS** → Patrones de desarrollo ({timeframe_days} días)")
        
        # Get commit history
        commits = self.get_commit_history(timeframe_days)
        if not commits:
            print("⚠️  No se encontraron commits en el período especificado")
            return GitIntelligenceResults(
                f"últimos {timeframe_days} días", 0, 0, {}, [], [], [], {}, {}
            )
        
        # Analyze development patterns
        velocity_metrics = self.analyze_development_velocity(commits)
        commit_patterns = self.analyze_commit_patterns(commits)
        high_activity_areas = self.identify_high_activity_areas(commits)
        file_correlation_matrix = self.calculate_file_correlation_matrix(commits)
        optimization_opportunities = self.identify_optimization_opportunities(commits, commit_patterns)
        
        # Calculate active files
        active_files = set()
        for commit in commits:
            active_files.update(commit.get('files_changed', []))
        
        results = GitIntelligenceResults(
            analysis_period=f"últimos {timeframe_days} días",
            total_commits=len(commits),
            active_files=len(active_files),
            development_velocity=velocity_metrics,
            commit_patterns=commit_patterns,
            high_activity_areas=high_activity_areas,
            optimization_opportunities=optimization_opportunities,
            file_correlation_matrix=file_correlation_matrix,
            metadata={
                'analysis_timestamp': datetime.datetime.now().isoformat(),
                'repository_path': self.repo_path,
                'commit_sample_size': len(commits)
            }
        )
        
        self.analysis_results = results
        return results
    
    def export_analysis_results(self, output_path: str) -> bool:
        """Export git intelligence results to JSON"""
        if not self.analysis_results:
            print("❌ No hay resultados de análisis para exportar")
            return False
        
        try:
            # Convert dataclasses to dict for JSON serialization
            export_data = {
                'analysis_period': self.analysis_results.analysis_period,
                'total_commits': self.analysis_results.total_commits,
                'active_files': self.analysis_results.active_files,
                'development_velocity': self.analysis_results.development_velocity,
                'commit_patterns': [
                    {
                        'pattern_type': p.pattern_type,
                        'frequency': p.frequency,
                        'files_affected': p.files_affected,
                        'success_indicators': p.success_indicators,
                        'temporal_distribution': p.temporal_distribution,
                        'velocity_metrics': p.velocity_metrics
                    } for p in self.analysis_results.commit_patterns
                ],
                'high_activity_areas': self.analysis_results.high_activity_areas,
                'optimization_opportunities': self.analysis_results.optimization_opportunities,
                'file_correlation_matrix': self.analysis_results.file_correlation_matrix,
                'metadata': self.analysis_results.metadata
            }
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Resultados de git intelligence exportados a: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error exportando resultados: {e}")
            return False


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='Análisis de Git Intelligence')
    parser.add_argument('--timeframe', '-t', type=int, default=30,
                       help='Período de análisis en días (default: 30)')
    parser.add_argument('--output', '-o', type=str,
                       help='Archivo de salida para resultados (JSON)')
    parser.add_argument('--repo-path', type=str,
                       help='Ruta al repositorio git')
    
    args = parser.parse_args()
    
    print("📊 **GIT INTELLIGENCE ANALYZER** - Fase 1 Implementación")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = GitIntelligenceAnalyzer(args.repo_path)
    
    # Generate intelligence
    results = analyzer.generate_git_intelligence(args.timeframe)
    
    # Display summary
    print("\n📊 **RESUMEN DE ANÁLISIS GIT**:")
    print(f"⟳ Commits analizados: {results.total_commits}")
    print(f"⟳ Archivos activos: {results.active_files}")
    print(f"⟳ Período: {results.analysis_period}")
    print(f"⟳ Patrones de commit: {len(results.commit_patterns)}")
    print(f"⟳ Áreas de alta actividad: {len(results.high_activity_areas)}")
    print(f"⟳ Oportunidades de optimización: {len(results.optimization_opportunities)}")
    
    if results.development_velocity:
        print(f"⟳ Velocidad promedio: {results.development_velocity.get('commits_per_day', 0):.2f} commits/día")
    
    # Export results if requested
    if args.output:
        analyzer.export_analysis_results(args.output)
    else:
        # Default output location
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        default_output = f"/Users/nalve/claude-context-engineering/scripts/results/intelligence/git-intelligence-{timestamp}.json"
        os.makedirs(os.path.dirname(default_output), exist_ok=True)
        analyzer.export_analysis_results(default_output)
    
    print("\n🎯 **ANÁLISIS GIT COMPLETADO** → Patrones de desarrollo listos para integración")


if __name__ == "__main__":
    main()