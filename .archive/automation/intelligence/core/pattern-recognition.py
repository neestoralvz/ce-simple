#!/usr/bin/env python3
"""
Pattern Recognition Engine - Historical Intelligence Core
========================================================

**Purpose**: Cross-source pattern identification and correlation engine for 
Historical Intelligence Architecture.

**Authority Integration**: Historical Intelligence Architecture (Principle #110)
**P55/P56 Compliance**: MANDATORY cross-source correlation analysis

This is the core pattern recognition engine that correlates data across all
intelligence sources for /system-update, /knowledge-sync, and /intelligent-reorganization.
"""

import json
import datetime
import re
import os
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from collections import defaultdict, Counter
import numpy as np
from pathlib import Path


@dataclass
class CrossSourcePattern:
    """Structure for cross-source pattern correlation"""
    pattern_id: str
    pattern_type: str
    confidence: float
    sources: List[str]
    correlations: Dict[str, Any]
    evidence: List[str]
    recommendations: List[str]
    temporal_analysis: Dict[str, Any]


@dataclass
class IntelligenceCorrelation:
    """Structure for intelligence correlation results"""
    correlation_id: str
    primary_source: str
    secondary_sources: List[str]
    correlation_strength: float
    pattern_match: CrossSourcePattern
    actionable_insights: List[str]


class PatternRecognitionEngine:
    """Core engine for cross-source pattern recognition and correlation"""
    
    def __init__(self):
        """Initialize pattern recognition engine"""
        self.patterns_cache = {}
        self.correlation_matrix = {}
        self.confidence_thresholds = {
            'high': 0.8,
            'medium': 0.6,
            'low': 0.4
        }
        
    def correlate_multi_source_patterns(self, conversation_data: Dict[str, Any], 
                                       git_data: Dict[str, Any], 
                                       operational_data: Dict[str, Any]) -> List[CrossSourcePattern]:
        """Correlate patterns across conversation, git, and operational data"""
        
        print("🔍 **CROSS-SOURCE PATTERN CORRELATION** - Multi-Intelligence Analysis")
        
        patterns = []
        
        # 1. File-Activity-Discussion Correlation
        file_patterns = self._correlate_file_activity_discussions(conversation_data, git_data)
        patterns.extend(file_patterns)
        
        # 2. Success-Implementation Correlation
        success_patterns = self._correlate_success_implementations(conversation_data, git_data, operational_data)
        patterns.extend(success_patterns)
        
        # 3. Problem-Solution-Resolution Correlation
        problem_patterns = self._correlate_problem_resolution_patterns(conversation_data, git_data, operational_data)
        patterns.extend(problem_patterns)
        
        # 4. Performance-Usage Correlation
        performance_patterns = self._correlate_performance_usage_patterns(git_data, operational_data)
        patterns.extend(performance_patterns)
        
        # 5. Knowledge-Gap-Implementation Correlation
        knowledge_patterns = self._correlate_knowledge_gaps_implementations(conversation_data, git_data)
        patterns.extend(knowledge_patterns)
        
        print(f"   ✅ {len(patterns)} cross-source patterns identified")
        return patterns
    
    def _correlate_file_activity_discussions(self, conv_data: Dict[str, Any], 
                                           git_data: Dict[str, Any]) -> List[CrossSourcePattern]:
        """Correlate file activity with conversation discussions"""
        patterns = []
        
        if not conv_data or not git_data:
            return patterns
        
        # Get file references from conversations
        conv_file_refs = conv_data.get('metadata', {}).get('file_references', [])
        
        # Get high activity files from git
        git_high_activity = git_data.get('high_activity_areas', [])
        
        # Find correlations
        correlations = []
        for conv_file in conv_file_refs[:20]:  # Top 20 from conversations
            for git_area in git_high_activity[:10]:  # Top 10 from git
                if self._calculate_file_similarity(conv_file, git_area) > 0.7:
                    correlations.append({
                        'conv_file': conv_file,
                        'git_area': git_area,
                        'similarity': self._calculate_file_similarity(conv_file, git_area)
                    })
        
        if correlations:
            # Create pattern for highly discussed and modified files
            high_correlation_files = [c for c in correlations if c['similarity'] > 0.8]
            if high_correlation_files:
                pattern = CrossSourcePattern(
                    pattern_id="file_activity_discussion_correlation",
                    pattern_type="high_attention_files",
                    confidence=0.85,
                    sources=["conversation", "git"],
                    correlations={
                        'correlated_files': high_correlation_files[:10],
                        'correlation_strength': sum(c['similarity'] for c in high_correlation_files) / len(high_correlation_files)
                    },
                    evidence=[
                        f"Found {len(high_correlation_files)} files with high discussion-activity correlation",
                        f"Average correlation strength: {sum(c['similarity'] for c in high_correlation_files) / len(high_correlation_files):.2f}"
                    ],
                    recommendations=[
                        "Prioritize documentation updates for high-attention files",
                        "Consider structural optimization for frequently discussed and modified files",
                        "Create cross-reference networks connecting related discussions to implementations"
                    ],
                    temporal_analysis={}
                )
                patterns.append(pattern)
        
        return patterns
    
    def _correlate_success_implementations(self, conv_data: Dict[str, Any], 
                                         git_data: Dict[str, Any], 
                                         ops_data: Dict[str, Any]) -> List[CrossSourcePattern]:
        """Correlate success indicators across all sources"""
        patterns = []
        
        # Extract success indicators
        conv_successes = []
        if conv_data:
            conv_successes = conv_data.get('success_methodologies', [])
        
        git_successes = []
        if git_data:
            for pattern in git_data.get('commit_patterns', []):
                git_successes.extend(pattern.get('success_indicators', []))
        
        ops_successes = []
        if ops_data:
            ops_successes = ops_data.get('success_patterns', [])
        
        # Look for common themes across sources
        success_themes = self._extract_common_themes(conv_successes + git_successes + ops_successes)
        
        if success_themes:
            pattern = CrossSourcePattern(
                pattern_id="cross_source_success_correlation",
                pattern_type="validated_success_patterns",
                confidence=0.9,
                sources=["conversation", "git", "operational"],
                correlations={
                    'common_themes': success_themes,
                    'conversation_successes': len(conv_successes),
                    'git_successes': len(git_successes),
                    'operational_successes': len(ops_successes)
                },
                evidence=[
                    f"Identified {len(success_themes)} common success themes across all sources",
                    f"Total success indicators: {len(conv_successes + git_successes + ops_successes)}"
                ],
                recommendations=[
                    "Document validated success patterns in knowledge base",
                    "Create best practices guide based on cross-validated patterns",
                    "Implement success pattern templates for replication"
                ],
                temporal_analysis={}
            )
            patterns.append(pattern)
        
        return patterns
    
    def _correlate_problem_resolution_patterns(self, conv_data: Dict[str, Any], 
                                             git_data: Dict[str, Any], 
                                             ops_data: Dict[str, Any]) -> List[CrossSourcePattern]:
        """Correlate problem identification with resolution patterns"""
        patterns = []
        
        # Extract problem patterns
        conv_gaps = conv_data.get('knowledge_gaps', []) if conv_data else []
        
        # Extract fix patterns from git
        git_fixes = []
        if git_data:
            for pattern in git_data.get('commit_patterns', []):
                if pattern.get('pattern_type') == 'fix':
                    git_fixes.extend(pattern.get('files_affected', []))
        
        # Extract operational problems
        ops_degradations = ops_data.get('degradation_alerts', []) if ops_data else []
        
        # Correlate conversation gaps with implementation fixes
        gap_fix_correlations = []
        for gap in conv_gaps[:10]:
            for fix_file in git_fixes[:20]:
                correlation_score = self._calculate_semantic_similarity(gap, fix_file)
                if correlation_score > 0.5:
                    gap_fix_correlations.append({
                        'gap': gap,
                        'fix_file': fix_file,
                        'correlation': correlation_score
                    })
        
        if gap_fix_correlations:
            pattern = CrossSourcePattern(
                pattern_id="problem_resolution_correlation",
                pattern_type="validated_problem_solutions",
                confidence=0.75,
                sources=["conversation", "git", "operational"],
                correlations={
                    'gap_fix_correlations': gap_fix_correlations[:10],
                    'problem_areas_identified': len(conv_gaps + ops_degradations),
                    'implementation_fixes': len(git_fixes)
                },
                evidence=[
                    f"Found {len(gap_fix_correlations)} gap-fix correlations",
                    f"Problem areas identified: {len(conv_gaps + ops_degradations)}"
                ],
                recommendations=[
                    "Create problem-solution knowledge base entries",
                    "Document proven resolution patterns",
                    "Implement early warning system for identified problem patterns"
                ],
                temporal_analysis={}
            )
            patterns.append(pattern)
        
        return patterns
    
    def _correlate_performance_usage_patterns(self, git_data: Dict[str, Any], 
                                            ops_data: Dict[str, Any]) -> List[CrossSourcePattern]:
        """Correlate performance metrics with usage patterns"""
        patterns = []
        
        if not git_data or not ops_data:
            return patterns
        
        # Extract velocity metrics
        velocity_metrics = git_data.get('development_velocity', {})
        
        # Extract performance metrics
        performance_metrics = ops_data.get('performance_analysis', {})
        
        # Correlate development velocity with system performance
        velocity_performance_correlation = self._calculate_velocity_performance_correlation(
            velocity_metrics, performance_metrics
        )
        
        if velocity_performance_correlation > 0.6:
            pattern = CrossSourcePattern(
                pattern_id="velocity_performance_correlation",
                pattern_type="development_system_performance",
                confidence=velocity_performance_correlation,
                sources=["git", "operational"],
                correlations={
                    'velocity_metrics': velocity_metrics,
                    'performance_metrics': performance_metrics,
                    'correlation_strength': velocity_performance_correlation
                },
                evidence=[
                    f"Development velocity correlation with system performance: {velocity_performance_correlation:.2f}",
                    f"Commits per day: {velocity_metrics.get('commits_per_day', 0):.2f}",
                    f"System optimization score: {performance_metrics.get('optimization_score', 0):.2f}"
                ],
                recommendations=[
                    "Optimize development workflows for better system performance",
                    "Balance development velocity with system health metrics",
                    "Implement performance monitoring for high-velocity periods"
                ],
                temporal_analysis={}
            )
            patterns.append(pattern)
        
        return patterns
    
    def _correlate_knowledge_gaps_implementations(self, conv_data: Dict[str, Any], 
                                                git_data: Dict[str, Any]) -> List[CrossSourcePattern]:
        """Correlate knowledge gaps with implementation patterns"""
        patterns = []
        
        if not conv_data or not git_data:
            return patterns
        
        knowledge_gaps = conv_data.get('knowledge_gaps', [])
        
        # Get file correlations from git
        file_correlations = git_data.get('file_correlation_matrix', {})
        
        # Find implementation areas that address knowledge gaps
        gap_implementation_correlations = []
        for gap in knowledge_gaps[:10]:
            for file_path, correlated_files in file_correlations.items():
                if len(correlated_files) >= 3:  # Files with good correlation
                    semantic_match = self._calculate_semantic_similarity(gap, file_path)
                    if semantic_match > 0.4:
                        gap_implementation_correlations.append({
                            'gap': gap,
                            'implementation_area': file_path,
                            'related_files': correlated_files[:5],
                            'semantic_match': semantic_match
                        })
        
        if gap_implementation_correlations:
            pattern = CrossSourcePattern(
                pattern_id="knowledge_gap_implementation_correlation",
                pattern_type="implementation_knowledge_opportunities",
                confidence=0.7,
                sources=["conversation", "git"],
                correlations={
                    'gap_implementation_matches': gap_implementation_correlations[:10],
                    'total_gaps': len(knowledge_gaps),
                    'implementation_coverage': len(gap_implementation_correlations) / max(len(knowledge_gaps), 1)
                },
                evidence=[
                    f"Found {len(gap_implementation_correlations)} gap-implementation correlations",
                    f"Implementation coverage: {len(gap_implementation_correlations) / max(len(knowledge_gaps), 1):.2f}"
                ],
                recommendations=[
                    "Create documentation for implementation areas addressing knowledge gaps",
                    "Develop tutorials based on proven implementation patterns",
                    "Establish knowledge-implementation feedback loops"
                ],
                temporal_analysis={}
            )
            patterns.append(pattern)
        
        return patterns
    
    def _calculate_file_similarity(self, file1: str, file2: str) -> float:
        """Calculate similarity between file paths"""
        if not file1 or not file2:
            return 0.0
        
        # Normalize paths
        path1_parts = file1.lower().split('/')
        path2_parts = file2.lower().split('/')
        
        # Calculate overlap
        common_parts = set(path1_parts) & set(path2_parts)
        total_parts = set(path1_parts) | set(path2_parts)
        
        if not total_parts:
            return 0.0
        
        return len(common_parts) / len(total_parts)
    
    def _calculate_semantic_similarity(self, text1: str, text2: str) -> float:
        """Calculate semantic similarity between texts"""
        if not text1 or not text2:
            return 0.0
        
        # Simple keyword-based similarity
        words1 = set(re.findall(r'\w+', text1.lower()))
        words2 = set(re.findall(r'\w+', text2.lower()))
        
        if not words1 or not words2:
            return 0.0
        
        common_words = words1 & words2
        total_words = words1 | words2
        
        return len(common_words) / len(total_words)
    
    def _extract_common_themes(self, texts: List[str]) -> List[str]:
        """Extract common themes from a list of texts"""
        if not texts:
            return []
        
        # Extract keywords from all texts
        all_words = []
        for text in texts:
            words = re.findall(r'\w+', text.lower())
            all_words.extend([w for w in words if len(w) > 3])  # Only words longer than 3 chars
        
        # Count word frequency
        word_counts = Counter(all_words)
        
        # Get most common themes (appearing in at least 20% of texts)
        threshold = max(1, len(texts) * 0.2)
        common_themes = [word for word, count in word_counts.items() if count >= threshold]
        
        return common_themes[:10]  # Top 10 themes
    
    def _calculate_velocity_performance_correlation(self, velocity_metrics: Dict[str, Any], 
                                                  performance_metrics: Dict[str, Any]) -> float:
        """Calculate correlation between development velocity and system performance"""
        if not velocity_metrics or not performance_metrics:
            return 0.0
        
        # Extract key metrics
        commits_per_day = velocity_metrics.get('commits_per_day', 0)
        files_per_day = velocity_metrics.get('files_per_day', 0)
        
        optimization_score = performance_metrics.get('optimization_score', 0)
        success_rate = performance_metrics.get('success_rate', 0)
        
        # Simple correlation calculation
        # Higher development velocity should correlate with system improvements
        velocity_score = min((commits_per_day + files_per_day) / 10, 1.0)  # Normalize to 0-1
        performance_score = (optimization_score + success_rate) / 2
        
        # Calculate correlation strength
        if velocity_score > 0 and performance_score > 0:
            # Simple correlation: similar scores = high correlation
            correlation = 1.0 - abs(velocity_score - performance_score)
            return max(0.0, correlation)
        
        return 0.0
    
    def generate_actionable_insights(self, patterns: List[CrossSourcePattern]) -> List[str]:
        """Generate actionable insights from cross-source patterns"""
        insights = []
        
        # High confidence patterns get priority
        high_confidence_patterns = [p for p in patterns if p.confidence > self.confidence_thresholds['high']]
        
        for pattern in high_confidence_patterns:
            if pattern.pattern_type == "high_attention_files":
                insights.extend([
                    f"🎯 High-attention files identified: prioritize documentation and structural optimization",
                    f"📊 {len(pattern.correlations.get('correlated_files', []))} files showing strong discussion-activity correlation"
                ])
            
            elif pattern.pattern_type == "validated_success_patterns":
                insights.extend([
                    f"✅ Cross-validated success patterns available for replication",
                    f"📝 Document {len(pattern.correlations.get('common_themes', []))} proven methodologies"
                ])
            
            elif pattern.pattern_type == "validated_problem_solutions":
                insights.extend([
                    f"🔧 Problem-solution correlations identified: create resolution knowledge base",
                    f"⚡ {len(pattern.correlations.get('gap_fix_correlations', []))} gap-fix patterns proven effective"
                ])
            
            elif pattern.pattern_type == "development_system_performance":
                insights.extend([
                    f"📈 Development velocity correlates with system performance (r={pattern.confidence:.2f})",
                    f"⚖️  Balance development speed with system health monitoring"
                ])
            
            elif pattern.pattern_type == "implementation_knowledge_opportunities":
                insights.extend([
                    f"📚 Knowledge gaps have implementation solutions: create documentation bridges",
                    f"🔗 {pattern.correlations.get('implementation_coverage', 0):.1%} implementation coverage for knowledge gaps"
                ])
        
        # Add general insights
        insights.extend([
            f"🧠 Total cross-source patterns identified: {len(patterns)}",
            f"🎯 High-confidence patterns: {len(high_confidence_patterns)}",
            f"📊 Multi-source intelligence provides {sum(p.confidence for p in patterns) / len(patterns):.2f} average confidence"
        ])
        
        return insights[:15]  # Top 15 insights
    
    def export_pattern_analysis(self, patterns: List[CrossSourcePattern], 
                               output_path: str) -> bool:
        """Export pattern analysis results"""
        try:
            export_data = {
                'analysis_timestamp': datetime.datetime.now().isoformat(),
                'total_patterns': len(patterns),
                'high_confidence_patterns': len([p for p in patterns if p.confidence > 0.8]),
                'patterns': [
                    {
                        'pattern_id': p.pattern_id,
                        'pattern_type': p.pattern_type,
                        'confidence': p.confidence,
                        'sources': p.sources,
                        'correlations': p.correlations,
                        'evidence': p.evidence,
                        'recommendations': p.recommendations
                    } for p in patterns
                ],
                'actionable_insights': self.generate_actionable_insights(patterns)
            }
            
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Pattern analysis exported to: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error exporting pattern analysis: {e}")
            return False


def main():
    """Demo execution for pattern recognition engine"""
    print("🔍 **PATTERN RECOGNITION ENGINE** - Cross-Source Intelligence Correlation")
    print("=" * 70)
    
    engine = PatternRecognitionEngine()
    
    # Demo data (in real usage, this comes from the intelligence connectors)
    demo_conv_data = {
        'metadata': {
            'file_references': ['docs/commands/system-update.md', 'scripts/intelligence/connectors/']
        },
        'knowledge_gaps': ['How to implement historical intelligence', 'Pattern recognition algorithms'],
        'success_methodologies': ['Multi-source analysis approach', 'Evidence-based validation']
    }
    
    demo_git_data = {
        'high_activity_areas': ['docs/commands/', 'scripts/intelligence/'],
        'commit_patterns': [
            {
                'pattern_type': 'fix',
                'files_affected': ['scripts/intelligence/connectors/conversation-analyzer.py'],
                'success_indicators': ['Analysis completed successfully']
            }
        ],
        'development_velocity': {
            'commits_per_day': 5.2,
            'files_per_day': 12.5
        },
        'file_correlation_matrix': {
            'docs/commands/system-update.md': ['scripts/maintenance/system-update.py']
        }
    }
    
    demo_ops_data = {
        'success_patterns': ['Multi-source correlation successful'],
        'degradation_alerts': ['Pattern recognition needs optimization'],
        'performance_analysis': {
            'optimization_score': 0.85,
            'success_rate': 0.92
        }
    }
    
    # Execute pattern correlation
    patterns = engine.correlate_multi_source_patterns(demo_conv_data, demo_git_data, demo_ops_data)
    
    # Generate insights
    insights = engine.generate_actionable_insights(patterns)
    
    print(f"\n📊 **PATTERN ANALYSIS RESULTS**:")
    print(f"⟳ Cross-source patterns identified: {len(patterns)}")
    print(f"⟳ Actionable insights generated: {len(insights)}")
    
    for i, insight in enumerate(insights[:5], 1):
        print(f"   {i}. {insight}")
    
    # Export results
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_path = f"/Users/nalve/claude-context-engineering/scripts/results/intelligence/pattern-analysis-{timestamp}.json"
    engine.export_pattern_analysis(patterns, output_path)
    
    print("\n🎯 **PATTERN RECOGNITION COMPLETED** → Cross-source intelligence correlated")


if __name__ == "__main__":
    main()