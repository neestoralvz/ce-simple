#!/usr/bin/env python3
"""
Context Validation and Integrity System
Ensures context quality, validates integrity, and maintains system health
"""

import json
import logging
import sqlite3
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass
from pathlib import Path
import threading
import time

@dataclass
class ValidationResult:
    """Result of context validation"""
    item_id: str
    validation_type: str
    status: str  # 'passed', 'warning', 'failed'
    issues: List[str]
    score: float  # 0.0 to 1.0
    timestamp: str
    recommendations: List[str]

@dataclass
class IntegrityReport:
    """Context integrity report"""
    total_items: int
    validated_items: int
    passed_items: int
    warning_items: int
    failed_items: int
    overall_health: float
    critical_issues: List[str]
    recommendations: List[str]
    validation_timestamp: str

class ContextValidator:
    """
    Comprehensive context validation and integrity system
    Ensures high-quality context data for semantic retrieval
    """
    
    def __init__(self, context_db_path: str):
        self.context_db_path = Path(context_db_path)
        self.validation_cache = {}
        self.cache_lock = threading.Lock()
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Validation rules configuration
        self.validation_rules = {
            'content_quality': {
                'min_length': 10,
                'max_length': 50000,
                'required_patterns': [],
                'forbidden_patterns': ['<?php', '<script>', 'eval(']
            },
            'metadata_integrity': {
                'required_fields': ['context_type', 'timestamp'],
                'valid_context_types': ['command', 'user_voice', 'session', 'project_evolution', 'command_execution'],
                'timestamp_format_check': True
            },
            'structural_consistency': {
                'id_uniqueness': True,
                'cross_reference_validity': True,
                'embedding_consistency': True
            },
            'semantic_coherence': {
                'min_coherence_score': 0.3,
                'content_type_alignment': True,
                'intent_consistency': True
            }
        }
        
        # Quality thresholds
        self.quality_thresholds = {
            'excellent': 0.9,
            'good': 0.7,
            'acceptable': 0.5,
            'poor': 0.3
        }
        
    def validate_context_item(self, item: Dict[str, Any]) -> ValidationResult:
        """
        Validate individual context item
        Returns comprehensive validation result
        """
        validation_issues = []
        recommendations = []
        validation_scores = []
        
        # Content quality validation
        content_score, content_issues, content_recs = self._validate_content_quality(item)
        validation_scores.append(content_score)
        validation_issues.extend(content_issues)
        recommendations.extend(content_recs)
        
        # Metadata integrity validation
        metadata_score, metadata_issues, metadata_recs = self._validate_metadata_integrity(item)
        validation_scores.append(metadata_score)
        validation_issues.extend(metadata_issues)
        recommendations.extend(metadata_recs)
        
        # Structural consistency validation
        struct_score, struct_issues, struct_recs = self._validate_structural_consistency(item)
        validation_scores.append(struct_score)
        validation_issues.extend(struct_issues)
        recommendations.extend(struct_recs)
        
        # Semantic coherence validation
        semantic_score, semantic_issues, semantic_recs = self._validate_semantic_coherence(item)
        validation_scores.append(semantic_score)
        validation_issues.extend(semantic_issues)
        recommendations.extend(semantic_recs)
        
        # Calculate overall score
        overall_score = sum(validation_scores) / len(validation_scores)
        
        # Determine status
        if overall_score >= self.quality_thresholds['good']:
            status = 'passed'
        elif overall_score >= self.quality_thresholds['acceptable']:
            status = 'warning'
        else:
            status = 'failed'
            
        return ValidationResult(
            item_id=item.get('id', 'unknown'),
            validation_type='comprehensive',
            status=status,
            issues=validation_issues,
            score=overall_score,
            timestamp=datetime.now().isoformat(),
            recommendations=recommendations
        )
        
    def validate_context_database(self, sample_size: Optional[int] = None) -> IntegrityReport:
        """
        Validate entire context database integrity
        Returns comprehensive integrity report
        """
        self.logger.info("Starting context database validation")
        
        with sqlite3.connect(self.context_db_path) as conn:
            # Get all context items or sample
            if sample_size:
                cursor = conn.execute('''
                    SELECT * FROM context_items 
                    ORDER BY RANDOM() 
                    LIMIT ?
                ''', (sample_size,))
            else:
                cursor = conn.execute('SELECT * FROM context_items')
                
            items = [dict(zip([col[0] for col in cursor.description], row))
                    for row in cursor.fetchall()]
                    
        # Validate each item
        validation_results = []
        for item in items:
            result = self.validate_context_item(item)
            validation_results.append(result)
            
        # Generate integrity report
        report = self._generate_integrity_report(validation_results, len(items))
        
        self.logger.info(f"Database validation complete: {report.overall_health:.2f} health score")
        return report
        
    def check_cross_reference_integrity(self) -> Dict[str, Any]:
        """
        Check integrity of cross-references between context items
        Identifies broken or invalid references
        """
        with sqlite3.connect(self.context_db_path) as conn:
            cursor = conn.execute('''
                SELECT id, cross_references FROM context_items 
                WHERE cross_references IS NOT NULL
            ''')
            
            items_with_refs = cursor.fetchall()
            
        broken_references = []
        valid_references = 0
        total_references = 0
        
        # Check each cross-reference
        for item_id, cross_refs_json in items_with_refs:
            try:
                cross_refs = json.loads(cross_refs_json) if cross_refs_json else []
                
                for ref_id in cross_refs:
                    total_references += 1
                    
                    # Check if referenced item exists
                    if self._item_exists(ref_id):
                        valid_references += 1
                    else:
                        broken_references.append({
                            'source_id': item_id,
                            'broken_reference': ref_id,
                            'issue': 'Referenced item does not exist'
                        })
                        
            except json.JSONDecodeError:
                broken_references.append({
                    'source_id': item_id,
                    'broken_reference': 'invalid_json',
                    'issue': 'Invalid JSON in cross_references field'
                })
                
        integrity_score = valid_references / total_references if total_references > 0 else 1.0
        
        return {
            'total_references': total_references,
            'valid_references': valid_references,
            'broken_references': len(broken_references),
            'integrity_score': integrity_score,
            'broken_reference_details': broken_references,
            'recommendations': self._generate_cross_ref_recommendations(broken_references)
        }
        
    def validate_embedding_consistency(self) -> Dict[str, Any]:
        """
        Validate consistency of embeddings across context items
        Checks for corrupted or missing embeddings
        """
        with sqlite3.connect(self.context_db_path) as conn:
            cursor = conn.execute('''
                SELECT id, content, embedding_hash FROM context_items
            ''')
            
            items = cursor.fetchall()
            
        embedding_issues = []
        valid_embeddings = 0
        missing_embeddings = 0
        
        for item_id, content, embedding_hash in items:
            if not embedding_hash:
                missing_embeddings += 1
                if len(content) > 20:  # Should have embedding if content is substantial
                    embedding_issues.append({
                        'item_id': item_id,
                        'issue': 'Missing embedding for substantial content',
                        'content_length': len(content)
                    })
            else:
                # Validate embedding hash consistency
                expected_hash = self._calculate_embedding_hash(content)
                if embedding_hash != expected_hash:
                    embedding_issues.append({
                        'item_id': item_id,
                        'issue': 'Embedding hash mismatch - possible corruption',
                        'expected': expected_hash,
                        'actual': embedding_hash
                    })
                else:
                    valid_embeddings += 1
                    
        total_items = len(items)
        consistency_score = valid_embeddings / total_items if total_items > 0 else 0.0
        
        return {
            'total_items': total_items,
            'valid_embeddings': valid_embeddings,
            'missing_embeddings': missing_embeddings,
            'corrupted_embeddings': len(embedding_issues),
            'consistency_score': consistency_score,
            'issues': embedding_issues,
            'recommendations': self._generate_embedding_recommendations(embedding_issues, missing_embeddings)
        }
        
    def audit_context_quality_trends(self, days_back: int = 30) -> Dict[str, Any]:
        """
        Audit context quality trends over time
        Identifies patterns in context degradation or improvement
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_back)
        
        with sqlite3.connect(self.context_db_path) as conn:
            cursor = conn.execute('''
                SELECT * FROM context_items 
                WHERE timestamp >= ? AND timestamp <= ?
                ORDER BY timestamp
            ''', (start_date.isoformat(), end_date.isoformat()))
            
            items = [dict(zip([col[0] for col in cursor.description], row))
                    for row in cursor.fetchall()]
                    
        # Group items by day for trend analysis
        daily_quality = {}
        for item in items:
            try:
                item_date = datetime.fromisoformat(item['timestamp']).date()
                if item_date not in daily_quality:
                    daily_quality[item_date] = []
                    
                # Quick quality assessment
                quality_score = self._quick_quality_assessment(item)
                daily_quality[item_date].append(quality_score)
                
            except ValueError:
                continue  # Skip items with invalid timestamps
                
        # Calculate daily averages
        trend_data = []
        for date, scores in sorted(daily_quality.items()):
            avg_quality = sum(scores) / len(scores)
            trend_data.append({
                'date': date.isoformat(),
                'average_quality': avg_quality,
                'item_count': len(scores)
            })
            
        # Analyze trends
        trend_analysis = self._analyze_quality_trends(trend_data)
        
        return {
            'analysis_period': f"{start_date.date()} to {end_date.date()}",
            'total_items_analyzed': len(items),
            'trend_data': trend_data,
            'trend_analysis': trend_analysis,
            'recommendations': self._generate_trend_recommendations(trend_analysis)
        }
        
    def repair_context_integrity(self, repair_options: Dict[str, bool]) -> Dict[str, Any]:
        """
        Repair context integrity issues
        Applies automated fixes based on repair options
        """
        repair_results = {
            'repairs_attempted': 0,
            'repairs_successful': 0,
            'repairs_failed': 0,
            'repair_details': []
        }
        
        # Repair broken cross-references
        if repair_options.get('fix_cross_references', False):
            cross_ref_results = self._repair_cross_references()
            repair_results['repair_details'].append(cross_ref_results)
            repair_results['repairs_attempted'] += cross_ref_results['attempted']
            repair_results['repairs_successful'] += cross_ref_results['successful']
            repair_results['repairs_failed'] += cross_ref_results['failed']
            
        # Repair missing metadata
        if repair_options.get('fix_metadata', False):
            metadata_results = self._repair_missing_metadata()
            repair_results['repair_details'].append(metadata_results)
            repair_results['repairs_attempted'] += metadata_results['attempted']
            repair_results['repairs_successful'] += metadata_results['successful']
            repair_results['repairs_failed'] += metadata_results['failed']
            
        # Regenerate missing embeddings
        if repair_options.get('regenerate_embeddings', False):
            embedding_results = self._regenerate_missing_embeddings()
            repair_results['repair_details'].append(embedding_results)
            repair_results['repairs_attempted'] += embedding_results['attempted']
            repair_results['repairs_successful'] += embedding_results['successful']
            repair_results['repairs_failed'] += embedding_results['failed']
            
        # Clean up duplicate items
        if repair_options.get('remove_duplicates', False):
            duplicate_results = self._remove_duplicate_items()
            repair_results['repair_details'].append(duplicate_results)
            repair_results['repairs_attempted'] += duplicate_results['attempted']
            repair_results['repairs_successful'] += duplicate_results['successful']
            repair_results['repairs_failed'] += duplicate_results['failed']
            
        self.logger.info(f"Integrity repair complete: {repair_results['repairs_successful']} successful repairs")
        return repair_results
        
    # Private validation methods
    def _validate_content_quality(self, item: Dict[str, Any]) -> Tuple[float, List[str], List[str]]:
        """Validate content quality"""
        content = item.get('content', '')
        issues = []
        recommendations = []
        score = 1.0
        
        # Length validation
        if len(content) < self.validation_rules['content_quality']['min_length']:
            issues.append(f"Content too short ({len(content)} chars)")
            recommendations.append("Ensure content has sufficient detail")
            score -= 0.3
            
        if len(content) > self.validation_rules['content_quality']['max_length']:
            issues.append(f"Content too long ({len(content)} chars)")
            recommendations.append("Consider content compaction")
            score -= 0.2
            
        # Pattern validation
        for pattern in self.validation_rules['content_quality']['forbidden_patterns']:
            if pattern in content:
                issues.append(f"Contains forbidden pattern: {pattern}")
                recommendations.append(f"Remove or sanitize {pattern}")
                score -= 0.5
                
        # Content richness
        word_count = len(content.split())
        if word_count < 5:
            issues.append("Content lacks substance")
            recommendations.append("Add more descriptive content")
            score -= 0.2
            
        return max(score, 0.0), issues, recommendations
        
    def _validate_metadata_integrity(self, item: Dict[str, Any]) -> Tuple[float, List[str], List[str]]:
        """Validate metadata integrity"""
        issues = []
        recommendations = []
        score = 1.0
        
        # Required fields
        for field in self.validation_rules['metadata_integrity']['required_fields']:
            if not item.get(field):
                issues.append(f"Missing required field: {field}")
                recommendations.append(f"Add {field} to item metadata")
                score -= 0.3
                
        # Context type validation
        context_type = item.get('context_type')
        valid_types = self.validation_rules['metadata_integrity']['valid_context_types']
        if context_type and context_type not in valid_types:
            issues.append(f"Invalid context type: {context_type}")
            recommendations.append(f"Use one of: {', '.join(valid_types)}")
            score -= 0.2
            
        # Timestamp validation
        timestamp = item.get('timestamp')
        if timestamp:
            try:
                datetime.fromisoformat(timestamp)
            except ValueError:
                issues.append("Invalid timestamp format")
                recommendations.append("Use ISO format for timestamps")
                score -= 0.2
                
        return max(score, 0.0), issues, recommendations
        
    def _validate_structural_consistency(self, item: Dict[str, Any]) -> Tuple[float, List[str], List[str]]:
        """Validate structural consistency"""
        issues = []
        recommendations = []
        score = 1.0
        
        # ID uniqueness (would need database context for full check)
        item_id = item.get('id')
        if not item_id:
            issues.append("Missing item ID")
            recommendations.append("Generate unique ID for item")
            score -= 0.4
            
        # Cross-reference validity
        cross_refs = item.get('cross_references')
        if cross_refs:
            try:
                if isinstance(cross_refs, str):
                    json.loads(cross_refs)
            except json.JSONDecodeError:
                issues.append("Invalid cross-references JSON")
                recommendations.append("Fix cross-references JSON format")
                score -= 0.2
                
        return max(score, 0.0), issues, recommendations
        
    def _validate_semantic_coherence(self, item: Dict[str, Any]) -> Tuple[float, List[str], List[str]]:
        """Validate semantic coherence"""
        issues = []
        recommendations = []
        score = 1.0
        
        content = item.get('content', '')
        context_type = item.get('context_type', '')
        
        # Content-type alignment
        alignment_score = self._check_content_type_alignment(content, context_type)
        if alignment_score < 0.5:
            issues.append("Content doesn't align with context type")
            recommendations.append("Review content-type classification")
            score -= 0.3
            
        # Intent consistency
        if item.get('user_intent'):
            intent_consistency = self._check_intent_consistency(content, item['user_intent'])
            if intent_consistency < 0.5:
                issues.append("Content doesn't match declared intent")
                recommendations.append("Update intent or content for consistency")
                score -= 0.2
                
        return max(score, 0.0), issues, recommendations
        
    def _check_content_type_alignment(self, content: str, context_type: str) -> float:
        """Check alignment between content and context type"""
        content_lower = content.lower()
        
        if context_type == 'command':
            command_indicators = ['command', 'execute', 'run', 'deploy', 'agent']
            return min(sum(1 for indicator in command_indicators if indicator in content_lower) * 0.3, 1.0)
        elif context_type == 'user_voice':
            voice_indicators = ['user', 'preference', 'want', 'need', 'like', 'prefer']
            return min(sum(1 for indicator in voice_indicators if indicator in content_lower) * 0.3, 1.0)
        elif context_type == 'session':
            session_indicators = ['session', 'conversation', 'discussion', 'meeting']
            return min(sum(1 for indicator in session_indicators if indicator in content_lower) * 0.3, 1.0)
        else:
            return 0.7  # Default alignment for unknown types
            
    def _check_intent_consistency(self, content: str, declared_intent: str) -> float:
        """Check consistency between content and declared intent"""
        content_lower = content.lower()
        intent_lower = declared_intent.lower()
        
        # Simple keyword matching - could be enhanced with NLP
        intent_words = intent_lower.split()
        matches = sum(1 for word in intent_words if word in content_lower)
        
        return matches / len(intent_words) if intent_words else 0.5
        
    def _generate_integrity_report(self, validation_results: List[ValidationResult], 
                                 total_items: int) -> IntegrityReport:
        """Generate comprehensive integrity report"""
        passed = sum(1 for r in validation_results if r.status == 'passed')
        warning = sum(1 for r in validation_results if r.status == 'warning')
        failed = sum(1 for r in validation_results if r.status == 'failed')
        
        overall_health = sum(r.score for r in validation_results) / len(validation_results) if validation_results else 0.0
        
        # Collect critical issues
        critical_issues = []
        for result in validation_results:
            if result.status == 'failed':
                critical_issues.extend(result.issues[:2])  # Top 2 issues per failed item
                
        # Generate recommendations
        recommendations = self._generate_integrity_recommendations(validation_results)
        
        return IntegrityReport(
            total_items=total_items,
            validated_items=len(validation_results),
            passed_items=passed,
            warning_items=warning,
            failed_items=failed,
            overall_health=overall_health,
            critical_issues=critical_issues[:10],  # Top 10 critical issues
            recommendations=recommendations,
            validation_timestamp=datetime.now().isoformat()
        )
        
    def _item_exists(self, item_id: str) -> bool:
        """Check if item exists in database"""
        with sqlite3.connect(self.context_db_path) as conn:
            cursor = conn.execute('SELECT 1 FROM context_items WHERE id = ?', (item_id,))
            return cursor.fetchone() is not None
            
    def _calculate_embedding_hash(self, content: str) -> str:
        """Calculate expected embedding hash"""
        return hashlib.sha256(content.encode()).hexdigest()[:16]
        
    def _quick_quality_assessment(self, item: Dict[str, Any]) -> float:
        """Quick quality assessment for trend analysis"""
        score = 1.0
        
        content = item.get('content', '')
        if len(content) < 20:
            score -= 0.3
        if not item.get('context_type'):
            score -= 0.2
        if not item.get('timestamp'):
            score -= 0.2
            
        return max(score, 0.0)
        
    def _analyze_quality_trends(self, trend_data: List[Dict]) -> Dict[str, Any]:
        """Analyze quality trends"""
        if len(trend_data) < 2:
            return {'trend': 'insufficient_data'}
            
        # Calculate trend direction
        recent_avg = sum(d['average_quality'] for d in trend_data[-7:]) / min(7, len(trend_data))
        earlier_avg = sum(d['average_quality'] for d in trend_data[:-7]) / max(1, len(trend_data) - 7)
        
        trend_direction = 'improving' if recent_avg > earlier_avg else 'declining' if recent_avg < earlier_avg else 'stable'
        trend_strength = abs(recent_avg - earlier_avg)
        
        return {
            'trend': trend_direction,
            'strength': trend_strength,
            'recent_average': recent_avg,
            'earlier_average': earlier_avg,
            'volatility': self._calculate_volatility(trend_data)
        }
        
    def _calculate_volatility(self, trend_data: List[Dict]) -> float:
        """Calculate quality volatility"""
        if len(trend_data) < 2:
            return 0.0
            
        qualities = [d['average_quality'] for d in trend_data]
        mean_quality = sum(qualities) / len(qualities)
        variance = sum((q - mean_quality) ** 2 for q in qualities) / len(qualities)
        
        return variance ** 0.5  # Standard deviation
        
    def _generate_cross_ref_recommendations(self, broken_references: List[Dict]) -> List[str]:
        """Generate recommendations for cross-reference issues"""
        recommendations = []
        
        if broken_references:
            recommendations.append(f"Fix {len(broken_references)} broken cross-references")
            recommendations.append("Implement cross-reference validation before storage")
            recommendations.append("Consider cleanup of orphaned references")
            
        return recommendations
        
    def _generate_embedding_recommendations(self, issues: List[Dict], missing_count: int) -> List[str]:
        """Generate recommendations for embedding issues"""
        recommendations = []
        
        if missing_count > 0:
            recommendations.append(f"Generate embeddings for {missing_count} items")
            recommendations.append("Implement automatic embedding generation")
            
        if issues:
            recommendations.append("Regenerate corrupted embeddings")
            recommendations.append("Add embedding integrity checks")
            
        return recommendations
        
    def _generate_trend_recommendations(self, trend_analysis: Dict) -> List[str]:
        """Generate recommendations based on quality trends"""
        recommendations = []
        
        if trend_analysis.get('trend') == 'declining':
            recommendations.append("Investigate causes of quality decline")
            recommendations.append("Implement quality improvement measures")
            
        if trend_analysis.get('volatility', 0) > 0.2:
            recommendations.append("Stabilize context quality processes")
            recommendations.append("Add quality monitoring alerts")
            
        return recommendations
        
    def _generate_integrity_recommendations(self, validation_results: List[ValidationResult]) -> List[str]:
        """Generate integrity recommendations"""
        recommendations = []
        
        # Analyze common issues
        all_issues = []
        for result in validation_results:
            all_issues.extend(result.issues)
            
        # Count issue frequencies
        issue_counts = {}
        for issue in all_issues:
            issue_type = issue.split(':')[0] if ':' in issue else issue
            issue_counts[issue_type] = issue_counts.get(issue_type, 0) + 1
            
        # Generate recommendations for most common issues
        for issue_type, count in sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
            if count > 2:  # Only recommend for common issues
                recommendations.append(f"Address {issue_type} issues ({count} occurrences)")
                
        return recommendations
        
    # Repair methods
    def _repair_cross_references(self) -> Dict[str, Any]:
        """Repair broken cross-references"""
        # This would implement actual repair logic
        return {
            'repair_type': 'cross_references',
            'attempted': 0,
            'successful': 0,
            'failed': 0,
            'details': 'Cross-reference repair not implemented yet'
        }
        
    def _repair_missing_metadata(self) -> Dict[str, Any]:
        """Repair missing metadata"""
        # This would implement actual repair logic
        return {
            'repair_type': 'metadata',
            'attempted': 0,
            'successful': 0,
            'failed': 0,
            'details': 'Metadata repair not implemented yet'
        }
        
    def _regenerate_missing_embeddings(self) -> Dict[str, Any]:
        """Regenerate missing embeddings"""
        # This would implement actual embedding regeneration
        return {
            'repair_type': 'embeddings',
            'attempted': 0,
            'successful': 0,
            'failed': 0,
            'details': 'Embedding regeneration not implemented yet'
        }
        
    def _remove_duplicate_items(self) -> Dict[str, Any]:
        """Remove duplicate context items"""
        # This would implement duplicate detection and removal
        return {
            'repair_type': 'duplicates',
            'attempted': 0,
            'successful': 0,
            'failed': 0,
            'details': 'Duplicate removal not implemented yet'
        }

if __name__ == "__main__":
    # Example usage
    validator = ContextValidator("/Users/nalve/ce-simple/contextflow/semantic-retrieval/context.db")
    
    # Test item validation
    test_item = {
        'id': 'test_123',
        'content': 'This is test content for validation',
        'context_type': 'command',
        'timestamp': datetime.now().isoformat()
    }
    
    result = validator.validate_context_item(test_item)
    print(f"Validation result: {result.status} (score: {result.score:.2f})")
    print(f"Issues: {result.issues}")
    print(f"Recommendations: {result.recommendations}")