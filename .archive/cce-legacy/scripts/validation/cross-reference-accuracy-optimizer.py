#!/usr/bin/env python3
"""
Cross-Reference Accuracy Measurement and Optimization System
Enhanced Precision Validation for Cross-Reference Intelligence

This module provides sophisticated accuracy measurement and optimization
algorithms for cross-reference systems with mathematical precision and
automated correction capabilities.
"""

import json
import re
import sys
import hashlib
from pathlib import Path
from typing import Dict, List, Tuple, Set, Any, Optional
from collections import defaultdict, Counter
from datetime import datetime
from dataclasses import dataclass, asdict
from urllib.parse import urlparse
import concurrent.futures

@dataclass
class ReferenceAccuracy:
    """Cross-reference accuracy measurement"""
    reference_id: str
    source_file: str
    target_reference: str
    target_file: str
    accuracy_score: float
    validity_status: str
    semantic_relevance: float
    context_appropriateness: float
    link_quality: float
    issues: List[str]
    recommendations: List[str]

@dataclass
class AccuracyMetrics:
    """Overall accuracy metrics for cross-reference system"""
    total_references: int
    valid_references: int
    broken_references: int
    low_quality_references: int
    accuracy_percentage: float
    semantic_accuracy: float
    context_accuracy: float
    link_quality_score: float
    improvement_potential: float

@dataclass
class OptimizationSuggestion:
    """Cross-reference optimization suggestion"""
    suggestion_type: str
    priority: str
    source_file: str
    current_reference: str
    suggested_reference: str
    improvement_score: float
    rationale: str
    auto_applicable: bool
    confidence: float

class CrossReferenceAccuracyOptimizer:
    """Advanced cross-reference accuracy measurement and optimization"""
    
    def __init__(self, knowledge_path: str = None):
        self.knowledge_path = Path(knowledge_path or "/Users/nalve/claude-context-engineering")
        self.cache_path = self.knowledge_path / "scripts" / "cache" / "accuracy"
        self.cache_path.mkdir(parents=True, exist_ok=True)
        
        # File system mapping
        self.file_mapping = {}
        self.reference_cache = {}
        self.content_cache = {}
        
        # Accuracy measurement parameters
        self.accuracy_weights = {
            'target_validity': 0.35,      # Does target exist and is accessible?
            'semantic_relevance': 0.30,   # Is the reference semantically relevant?
            'context_appropriateness': 0.20,  # Does reference fit context?
            'link_quality': 0.15          # Is the link well-formatted and descriptive?
        }
        
        # Quality thresholds
        self.quality_thresholds = {
            'excellent': 0.90,
            'good': 0.75,
            'acceptable': 0.60,
            'poor': 0.45,
            'broken': 0.30
        }
        
        # Reference patterns
        self.reference_patterns = {
            'markdown_link': r'\[([^\]]+)\]\(([^)]+)\)',
            'relative_path': r'\.\/[^)\s]+',
            'absolute_path': r'\/[^)\s]+',
            'anchor_link': r'#[^)\s]+',
            'principle_reference': r'#(\d+)',
            'file_reference': r'[^\/\s]+\.md'
        }
        
        # Semantic keywords for relevance analysis
        self.semantic_categories = {
            'technical': ['implementation', 'technical', 'system', 'architecture', 'protocol'],
            'conceptual': ['principle', 'concept', 'philosophy', 'theory', 'framework'],
            'operational': ['execution', 'operation', 'workflow', 'process', 'procedure'],
            'validation': ['validation', 'verification', 'testing', 'quality', 'assurance'],
            'documentation': ['documentation', 'guide', 'manual', 'reference', 'standard'],
            'intelligence': ['intelligence', 'automation', 'optimization', 'learning', 'adaptive']
        }
        
        # Initialize file mapping
        self._build_file_mapping()
    
    def _build_file_mapping(self):
        """Build comprehensive file mapping for reference validation"""
        print("🗂️ Building file mapping...")
        
        # Scan all markdown files
        for md_file in self.knowledge_path.rglob("*.md"):
            relative_path = md_file.relative_to(self.knowledge_path)
            
            # Multiple path formats for flexibility
            self.file_mapping[str(relative_path)] = md_file
            self.file_mapping[str(relative_path).replace('\\', '/')] = md_file
            self.file_mapping[md_file.name] = md_file
            
            # Alternative naming patterns
            name_without_ext = md_file.stem
            self.file_mapping[name_without_ext] = md_file
            
            # Path variations
            if relative_path.parts:
                self.file_mapping['/'.join(relative_path.parts)] = md_file
                self.file_mapping['/' + '/'.join(relative_path.parts)] = md_file
                self.file_mapping['./' + '/'.join(relative_path.parts)] = md_file
        
        print(f"📁 Mapped {len(set(self.file_mapping.values()))} files with {len(self.file_mapping)} path variations")
    
    def extract_all_references(self, file_path: Path) -> List[Dict[str, Any]]:
        """Extract all cross-references from a file"""
        try:
            content = file_path.read_text(encoding='utf-8')
            self.content_cache[str(file_path)] = content
        except Exception as e:
            print(f"❌ Could not read {file_path}: {e}")
            return []
        
        references = []
        
        # Extract markdown links
        for match in re.finditer(self.reference_patterns['markdown_link'], content):
            link_text = match.group(1)
            link_target = match.group(2)
            
            reference = {
                'id': hashlib.md5(f"{file_path}:{match.start()}".encode()).hexdigest()[:12],
                'type': 'markdown_link',
                'source_file': str(file_path),
                'link_text': link_text,
                'link_target': link_target,
                'full_match': match.group(0),
                'position': match.start(),
                'context': self._extract_context(content, match.start(), match.end())
            }
            
            references.append(reference)
        
        # Extract principle references
        for match in re.finditer(r'#(\d+)', content):
            principle_num = match.group(1)
            
            reference = {
                'id': hashlib.md5(f"{file_path}:principle:{match.start()}".encode()).hexdigest()[:12],
                'type': 'principle_reference',
                'source_file': str(file_path),
                'link_text': f"#{principle_num}",
                'link_target': f"principle_{principle_num}",
                'full_match': match.group(0),
                'position': match.start(),
                'context': self._extract_context(content, match.start(), match.end())
            }
            
            references.append(reference)
        
        return references
    
    def _extract_context(self, content: str, start_pos: int, end_pos: int, context_size: int = 100) -> str:
        """Extract context around a reference for semantic analysis"""
        context_start = max(0, start_pos - context_size)
        context_end = min(len(content), end_pos + context_size)
        
        context = content[context_start:context_end]
        # Clean up context
        context = re.sub(r'\s+', ' ', context).strip()
        
        return context
    
    def measure_reference_accuracy(self, reference: Dict[str, Any]) -> ReferenceAccuracy:
        """Measure accuracy of a single cross-reference"""
        # Target validity check
        target_validity = self._check_target_validity(reference)
        
        # Semantic relevance analysis
        semantic_relevance = self._analyze_semantic_relevance(reference)
        
        # Context appropriateness
        context_appropriateness = self._analyze_context_appropriateness(reference)
        
        # Link quality assessment
        link_quality = self._assess_link_quality(reference)
        
        # Calculate overall accuracy score
        accuracy_score = (
            target_validity * self.accuracy_weights['target_validity'] +
            semantic_relevance * self.accuracy_weights['semantic_relevance'] +
            context_appropriateness * self.accuracy_weights['context_appropriateness'] +
            link_quality * self.accuracy_weights['link_quality']
        )
        
        # Determine validity status
        validity_status = self._determine_validity_status(accuracy_score, target_validity)
        
        # Identify issues
        issues = self._identify_reference_issues(reference, target_validity, semantic_relevance, 
                                               context_appropriateness, link_quality)
        
        # Generate recommendations
        recommendations = self._generate_reference_recommendations(reference, issues, accuracy_score)
        
        return ReferenceAccuracy(
            reference_id=reference['id'],
            source_file=reference['source_file'],
            target_reference=reference['link_target'],
            target_file=self._resolve_target_file(reference),
            accuracy_score=accuracy_score,
            validity_status=validity_status,
            semantic_relevance=semantic_relevance,
            context_appropriateness=context_appropriateness,
            link_quality=link_quality,
            issues=issues,
            recommendations=recommendations
        )
    
    def _check_target_validity(self, reference: Dict[str, Any]) -> float:
        """Check if reference target is valid and accessible"""
        target = reference['link_target']
        
        # Handle different reference types
        if reference['type'] == 'principle_reference':
            # Check if principle exists in principle network
            return self._validate_principle_reference(target)
        
        # Handle file references
        if '#' in target:
            file_part, anchor_part = target.split('#', 1)
            file_validity = self._validate_file_reference(file_part) if file_part else 1.0
            anchor_validity = self._validate_anchor_reference(file_part or reference['source_file'], anchor_part)
            return (file_validity + anchor_validity) / 2
        else:
            return self._validate_file_reference(target)
    
    def _validate_principle_reference(self, target: str) -> float:
        """Validate principle reference"""
        # Extract principle number
        principle_match = re.search(r'(\d+)', target)
        if not principle_match:
            return 0.0
        
        principle_num = int(principle_match.group(1))
        
        # Check if principle exists (simplified - would check actual principle network)
        if 1 <= principle_num <= 110:  # Assuming 110 principles
            return 1.0
        else:
            return 0.0
    
    def _validate_file_reference(self, target: str) -> float:
        """Validate file reference"""
        if not target or target.startswith('http'):
            return 0.5  # External links are harder to validate
        
        # Clean target path
        clean_target = target.strip()
        if clean_target.startswith('./'):
            clean_target = clean_target[2:]
        if clean_target.startswith('/'):
            clean_target = clean_target[1:]
        
        # Check if file exists in mapping
        if clean_target in self.file_mapping:
            return 1.0
        
        # Check variations
        for path_variant in self.file_mapping:
            if clean_target in path_variant or path_variant in clean_target:
                return 0.8  # Partial match
        
        return 0.0  # Not found
    
    def _validate_anchor_reference(self, file_path: str, anchor: str) -> float:
        """Validate anchor reference within file"""
        # Get file content
        resolved_file = self._resolve_target_file({'link_target': file_path})
        if not resolved_file:
            return 0.0
        
        content = self.content_cache.get(resolved_file, "")
        if not content:
            try:
                content = Path(resolved_file).read_text(encoding='utf-8')
                self.content_cache[resolved_file] = content
            except:
                return 0.0
        
        # Check for anchor in headers
        anchor_clean = anchor.lower().replace('-', ' ').replace('_', ' ')
        
        # Look for matching headers
        header_pattern = r'^#+\s*(.+)$'
        for match in re.finditer(header_pattern, content, re.MULTILINE):
            header_text = match.group(1).lower().replace('-', ' ').replace('_', ' ')
            if anchor_clean in header_text or header_text in anchor_clean:
                return 1.0
        
        # Look for anchor in content
        if anchor in content:
            return 0.7
        
        return 0.0
    
    def _analyze_semantic_relevance(self, reference: Dict[str, Any]) -> float:
        """Analyze semantic relevance of reference to its context"""
        context = reference.get('context', '')
        link_text = reference.get('link_text', '')
        
        # Extract keywords from context and link text
        context_words = set(re.findall(r'\b\w+\b', context.lower()))
        link_words = set(re.findall(r'\b\w+\b', link_text.lower()))
        
        # Analyze semantic categories
        relevance_scores = []
        
        for category, keywords in self.semantic_categories.items():
            category_keywords = set(keywords)
            
            # Context-category overlap
            context_overlap = len(context_words.intersection(category_keywords))
            context_score = min(context_overlap / 3.0, 1.0)  # Normalize to max 3 keywords
            
            # Link-category overlap
            link_overlap = len(link_words.intersection(category_keywords))
            link_score = min(link_overlap / 2.0, 1.0)  # Normalize to max 2 keywords
            
            # Combined score for this category
            if context_score > 0 and link_score > 0:
                category_score = (context_score + link_score) / 2
                relevance_scores.append(category_score)
        
        # Overall semantic relevance
        if relevance_scores:
            semantic_relevance = max(relevance_scores)  # Best category match
        else:
            # Fallback: direct word overlap
            common_words = context_words.intersection(link_words)
            semantic_relevance = min(len(common_words) / 5.0, 1.0)
        
        return semantic_relevance
    
    def _analyze_context_appropriateness(self, reference: Dict[str, Any]) -> float:
        """Analyze if reference is appropriate for its context"""
        context = reference.get('context', '')
        link_text = reference.get('link_text', '')
        
        appropriateness_factors = []
        
        # Length appropriateness
        if 5 <= len(link_text) <= 50:
            appropriateness_factors.append(1.0)
        elif len(link_text) < 5:
            appropriateness_factors.append(0.5)  # Too short
        else:
            appropriateness_factors.append(0.7)  # Too long but acceptable
        
        # Descriptive quality
        if any(word in link_text.lower() for word in ['click', 'here', 'link', 'this']):
            appropriateness_factors.append(0.3)  # Non-descriptive
        else:
            appropriateness_factors.append(0.9)  # Descriptive
        
        # Context integration
        context_sentences = re.split(r'[.!?]+', context)
        reference_sentence = ""
        for sentence in context_sentences:
            if link_text in sentence:
                reference_sentence = sentence
                break
        
        if reference_sentence:
            # Check if reference flows naturally
            before_link = reference_sentence.split(link_text)[0]
            if before_link.strip().endswith(('see', 'refer to', 'check', 'review', 'using')):
                appropriateness_factors.append(1.0)  # Natural flow
            else:
                appropriateness_factors.append(0.7)  # Acceptable integration
        else:
            appropriateness_factors.append(0.5)  # Could not analyze
        
        return sum(appropriateness_factors) / len(appropriateness_factors)
    
    def _assess_link_quality(self, reference: Dict[str, Any]) -> float:
        """Assess the quality of the link formatting and structure"""
        link_text = reference.get('link_text', '')
        link_target = reference.get('link_target', '')
        
        quality_factors = []
        
        # Link text quality
        if link_text.strip():
            if link_text == link_target:
                quality_factors.append(0.6)  # Same as target (not ideal)
            elif len(link_text) >= 3:
                quality_factors.append(1.0)  # Good descriptive text
            else:
                quality_factors.append(0.4)  # Too short
        else:
            quality_factors.append(0.0)  # Empty link text
        
        # Target format quality
        if link_target.startswith('http'):
            quality_factors.append(0.8)  # External link (generally good)
        elif link_target.endswith('.md'):
            quality_factors.append(1.0)  # Proper markdown file reference
        elif '#' in link_target:
            quality_factors.append(0.9)  # Anchor reference (good)
        elif link_target.strip():
            quality_factors.append(0.7)  # Some target specified
        else:
            quality_factors.append(0.0)  # Empty target
        
        # Path quality
        if './' in link_target or '../' in link_target:
            quality_factors.append(0.9)  # Relative path (good practice)
        elif link_target.startswith('/'):
            quality_factors.append(0.7)  # Absolute path (acceptable)
        else:
            quality_factors.append(0.8)  # Other format
        
        return sum(quality_factors) / len(quality_factors)
    
    def _determine_validity_status(self, accuracy_score: float, target_validity: float) -> str:
        """Determine validity status based on accuracy metrics"""
        if target_validity == 0.0:
            return 'BROKEN'
        elif accuracy_score >= self.quality_thresholds['excellent']:
            return 'EXCELLENT'
        elif accuracy_score >= self.quality_thresholds['good']:
            return 'GOOD'
        elif accuracy_score >= self.quality_thresholds['acceptable']:
            return 'ACCEPTABLE'
        elif accuracy_score >= self.quality_thresholds['poor']:
            return 'POOR'
        else:
            return 'BROKEN'
    
    def _identify_reference_issues(self, reference: Dict[str, Any], target_validity: float,
                                 semantic_relevance: float, context_appropriateness: float,
                                 link_quality: float) -> List[str]:
        """Identify specific issues with a reference"""
        issues = []
        
        if target_validity < 0.5:
            issues.append("Target file or anchor not found")
        
        if semantic_relevance < 0.4:
            issues.append("Low semantic relevance to context")
        
        if context_appropriateness < 0.5:
            issues.append("Reference not well integrated into context")
        
        if link_quality < 0.6:
            issues.append("Poor link formatting or structure")
        
        # Specific checks
        link_text = reference.get('link_text', '')
        if link_text.lower() in ['here', 'this', 'click here']:
            issues.append("Non-descriptive link text")
        
        if len(link_text) < 3:
            issues.append("Link text too short")
        
        if not reference.get('link_target', '').strip():
            issues.append("Empty or missing target")
        
        return issues
    
    def _generate_reference_recommendations(self, reference: Dict[str, Any], 
                                          issues: List[str], accuracy_score: float) -> List[str]:
        """Generate recommendations for improving reference"""
        recommendations = []
        
        for issue in issues:
            if "Target file" in issue:
                recommendations.append("Verify target file path and update if necessary")
            elif "semantic relevance" in issue:
                recommendations.append("Improve link text to better match context")
            elif "context" in issue:
                recommendations.append("Add connecting text to integrate reference naturally")
            elif "formatting" in issue:
                recommendations.append("Improve link formatting and target specification")
            elif "Non-descriptive" in issue:
                recommendations.append("Replace with descriptive link text")
            elif "too short" in issue:
                recommendations.append("Expand link text to be more descriptive")
            elif "Empty" in issue:
                recommendations.append("Add proper target specification")
        
        # General improvement suggestions
        if accuracy_score < 0.7:
            recommendations.append("Consider reviewing reference necessity and placement")
        
        if not recommendations:
            recommendations.append("Reference quality is acceptable - minor optimizations possible")
        
        return recommendations
    
    def _resolve_target_file(self, reference: Dict[str, Any]) -> str:
        """Resolve reference target to actual file path"""
        target = reference['link_target']
        
        if '#' in target:
            file_part = target.split('#')[0]
            if not file_part:
                return reference['source_file']  # Same file reference
            target = file_part
        
        # Clean target
        clean_target = target.strip()
        if clean_target.startswith('./'):
            clean_target = clean_target[2:]
        if clean_target.startswith('/'):
            clean_target = clean_target[1:]
        
        # Find in mapping
        if clean_target in self.file_mapping:
            return str(self.file_mapping[clean_target])
        
        return ""
    
    def analyze_directory_accuracy(self, directory: Path) -> Tuple[AccuracyMetrics, List[ReferenceAccuracy]]:
        """Analyze cross-reference accuracy for entire directory"""
        print(f"🔍 Analyzing cross-reference accuracy in {directory}")
        
        all_references = []
        accuracy_results = []
        
        # Extract all references
        md_files = list(directory.rglob("*.md"))
        print(f"📂 Processing {len(md_files)} files...")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            # Extract references
            extract_futures = {executor.submit(self.extract_all_references, file_path): file_path 
                             for file_path in md_files}
            
            for future in concurrent.futures.as_completed(extract_futures):
                file_refs = future.result()
                all_references.extend(file_refs)
        
        print(f"📎 Found {len(all_references)} references")
        
        # Measure accuracy
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            accuracy_futures = {executor.submit(self.measure_reference_accuracy, ref): ref 
                              for ref in all_references}
            
            for future in concurrent.futures.as_completed(accuracy_futures):
                accuracy_result = future.result()
                accuracy_results.append(accuracy_result)
        
        # Calculate metrics
        metrics = self._calculate_accuracy_metrics(accuracy_results)
        
        return metrics, accuracy_results
    
    def _calculate_accuracy_metrics(self, accuracy_results: List[ReferenceAccuracy]) -> AccuracyMetrics:
        """Calculate overall accuracy metrics"""
        if not accuracy_results:
            return AccuracyMetrics(0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0)
        
        total_references = len(accuracy_results)
        
        # Count by status
        status_counts = Counter(result.validity_status for result in accuracy_results)
        valid_references = status_counts.get('EXCELLENT', 0) + status_counts.get('GOOD', 0) + status_counts.get('ACCEPTABLE', 0)
        broken_references = status_counts.get('BROKEN', 0)
        low_quality_references = status_counts.get('POOR', 0)
        
        # Calculate averages
        accuracy_percentage = (valid_references / total_references) * 100
        semantic_accuracy = sum(r.semantic_relevance for r in accuracy_results) / total_references
        context_accuracy = sum(r.context_appropriateness for r in accuracy_results) / total_references
        link_quality_score = sum(r.link_quality for r in accuracy_results) / total_references
        
        # Calculate improvement potential
        current_avg_score = sum(r.accuracy_score for r in accuracy_results) / total_references
        potential_avg_score = 0.85  # Target average
        improvement_potential = max(0.0, potential_avg_score - current_avg_score)
        
        return AccuracyMetrics(
            total_references=total_references,
            valid_references=valid_references,
            broken_references=broken_references,
            low_quality_references=low_quality_references,
            accuracy_percentage=accuracy_percentage,
            semantic_accuracy=semantic_accuracy,
            context_accuracy=context_accuracy,
            link_quality_score=link_quality_score,
            improvement_potential=improvement_potential
        )
    
    def generate_optimization_suggestions(self, accuracy_results: List[ReferenceAccuracy]) -> List[OptimizationSuggestion]:
        """Generate optimization suggestions for improving cross-references"""
        suggestions = []
        
        # Group by issues
        issue_groups = defaultdict(list)
        for result in accuracy_results:
            if result.accuracy_score < 0.75:  # Focus on suboptimal references
                for issue in result.issues:
                    issue_groups[issue].append(result)
        
        # Generate suggestions for each issue type
        for issue_type, results in issue_groups.items():
            for result in results[:5]:  # Limit suggestions per issue type
                suggestion = self._create_optimization_suggestion(result, issue_type)
                if suggestion:
                    suggestions.append(suggestion)
        
        # Sort by improvement potential
        suggestions.sort(key=lambda x: x.improvement_score, reverse=True)
        
        return suggestions[:20]  # Top 20 suggestions
    
    def _create_optimization_suggestion(self, result: ReferenceAccuracy, issue_type: str) -> Optional[OptimizationSuggestion]:
        """Create specific optimization suggestion"""
        current_ref = result.target_reference
        
        if "Target file" in issue_type:
            # Suggest file path correction
            suggested_ref = self._suggest_file_path_correction(current_ref)
            suggestion_type = "PATH_CORRECTION"
            priority = "HIGH"
            improvement_score = 0.8
            auto_applicable = False
            
        elif "semantic relevance" in issue_type:
            # Suggest better link text
            suggested_ref = self._suggest_better_link_text(result)
            suggestion_type = "LINK_TEXT_IMPROVEMENT"
            priority = "MEDIUM"
            improvement_score = 0.6
            auto_applicable = False
            
        elif "Non-descriptive" in issue_type:
            # Suggest descriptive text
            suggested_ref = self._suggest_descriptive_text(result)
            suggestion_type = "DESCRIPTIVE_TEXT"
            priority = "MEDIUM"
            improvement_score = 0.5
            auto_applicable = True
            
        else:
            return None
        
        if not suggested_ref or suggested_ref == current_ref:
            return None
        
        rationale = f"Addresses: {issue_type}. Current score: {result.accuracy_score:.2f}"
        confidence = min(improvement_score + 0.2, 0.9)
        
        return OptimizationSuggestion(
            suggestion_type=suggestion_type,
            priority=priority,
            source_file=result.source_file,
            current_reference=current_ref,
            suggested_reference=suggested_ref,
            improvement_score=improvement_score,
            rationale=rationale,
            auto_applicable=auto_applicable,
            confidence=confidence
        )
    
    def _suggest_file_path_correction(self, current_ref: str) -> str:
        """Suggest corrected file path"""
        # Find closest match in file mapping
        best_match = ""
        best_score = 0
        
        for file_path in self.file_mapping:
            if current_ref in file_path or file_path in current_ref:
                score = len(set(current_ref.lower()) & set(file_path.lower())) / len(set(current_ref.lower()) | set(file_path.lower()))
                if score > best_score:
                    best_score = score
                    best_match = file_path
        
        return best_match if best_score > 0.3 else current_ref
    
    def _suggest_better_link_text(self, result: ReferenceAccuracy) -> str:
        """Suggest better link text based on context"""
        # Extract meaningful phrases from context
        context = result.source_file  # Simplified - would use actual context
        
        # Generate descriptive text based on target
        target = result.target_reference
        if "principle" in target.lower():
            return f"Principle {re.search(r'(\d+)', target).group(1) if re.search(r'(\d+)', target) else 'Reference'}"
        elif "command" in target.lower():
            return "Command Reference"
        elif "protocol" in target.lower():
            return "Protocol Documentation"
        elif "framework" in target.lower():
            return "Framework Guide"
        
        return "Related Documentation"
    
    def _suggest_descriptive_text(self, result: ReferenceAccuracy) -> str:
        """Suggest descriptive text to replace non-descriptive links"""
        target = result.target_reference
        
        # Generate descriptive text based on target type
        if target.endswith('.md'):
            name = Path(target).stem.replace('-', ' ').replace('_', ' ').title()
            return name
        elif '#' in target:
            anchor = target.split('#')[-1]
            return anchor.replace('-', ' ').replace('_', ' ').title()
        
        return "Documentation Reference"
    
    def generate_accuracy_report(self, directory: Path) -> str:
        """Generate comprehensive accuracy report"""
        # Analyze accuracy
        metrics, results = self.analyze_directory_accuracy(directory)
        
        # Generate optimization suggestions
        suggestions = self.generate_optimization_suggestions(results)
        
        # Build report
        report = []
        report.append("# 🎯 Cross-Reference Accuracy Analysis Report")
        report.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Scope**: {directory}")
        report.append("")
        
        # Overall metrics
        report.append("## 📊 Accuracy Metrics")
        report.append("")
        report.append(f"- **Total References**: {metrics.total_references}")
        report.append(f"- **Valid References**: {metrics.valid_references} ({metrics.accuracy_percentage:.1f}%)")
        report.append(f"- **Broken References**: {metrics.broken_references}")
        report.append(f"- **Low Quality References**: {metrics.low_quality_references}")
        report.append("")
        report.append(f"- **Semantic Accuracy**: {metrics.semantic_accuracy:.1%}")
        report.append(f"- **Context Accuracy**: {metrics.context_accuracy:.1%}")
        report.append(f"- **Link Quality Score**: {metrics.link_quality_score:.1%}")
        report.append(f"- **Improvement Potential**: {metrics.improvement_potential:.1%}")
        report.append("")
        
        # Quality breakdown
        status_counts = Counter(r.validity_status for r in results)
        if status_counts:
            report.append("## 📈 Quality Distribution")
            report.append("")
            for status in ['EXCELLENT', 'GOOD', 'ACCEPTABLE', 'POOR', 'BROKEN']:
                count = status_counts.get(status, 0)
                percentage = (count / metrics.total_references) * 100 if metrics.total_references > 0 else 0
                report.append(f"- **{status}**: {count} ({percentage:.1f}%)")
            report.append("")
        
        # Top issues
        all_issues = []
        for result in results:
            all_issues.extend(result.issues)
        
        if all_issues:
            issue_counts = Counter(all_issues)
            report.append("## 🚨 Common Issues")
            report.append("")
            for issue, count in issue_counts.most_common(10):
                report.append(f"- **{issue}**: {count} occurrences")
            report.append("")
        
        # Optimization suggestions
        if suggestions:
            report.append("## ⚡ Optimization Recommendations")
            report.append("")
            
            high_priority = [s for s in suggestions if s.priority == 'HIGH']
            if high_priority:
                report.append("### High Priority")
                report.append("")
                for suggestion in high_priority[:5]:
                    report.append(f"**{Path(suggestion.source_file).name}**")
                    report.append(f"- Type: {suggestion.suggestion_type}")
                    report.append(f"- Current: `{suggestion.current_reference}`")
                    report.append(f"- Suggested: `{suggestion.suggested_reference}`")
                    report.append(f"- Improvement: {suggestion.improvement_score:.1%}")
                    report.append("")
        
        return "\n".join(report)


def main():
    """Main execution function"""
    optimizer = CrossReferenceAccuracyOptimizer()
    
    print("🎯 Starting Cross-Reference Accuracy Analysis...")
    
    # Analyze knowledge directory
    knowledge_dir = Path("/Users/nalve/claude-context-engineering/knowledge")
    if not knowledge_dir.exists():
        print(f"❌ Knowledge directory not found: {knowledge_dir}")
        return 1
    
    # Generate accuracy report
    print("📊 Generating accuracy analysis report...")
    report = optimizer.generate_accuracy_report(knowledge_dir)
    
    # Save report
    report_path = Path("operations/reports/current/cross-reference-accuracy-analysis.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    
    print(f"✅ Accuracy analysis complete!")
    print(f"📋 Report saved to: {report_path}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())