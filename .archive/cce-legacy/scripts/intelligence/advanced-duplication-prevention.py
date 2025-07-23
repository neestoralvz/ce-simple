#!/usr/bin/env python3
"""
Advanced Cross-Reference Intelligence Duplication Prevention Engine
Next-Level Automated Connection-Making and Content Deduplication

This module provides sophisticated AI-driven duplication prevention with real-time
semantic analysis, intelligent content deduplication, and automated relationship
discovery for the Context Engineering ecosystem.
"""

import json
import re
import hashlib
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set, Any, Optional
from collections import defaultdict, Counter
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
import difflib
from concurrent.futures import ThreadPoolExecutor
import pickle

@dataclass
class ContentFingerprint:
    """Unique content identification and similarity metrics"""
    content_hash: str
    semantic_hash: str
    functional_keywords: Set[str]
    structural_patterns: List[str]
    concept_clusters: List[str]
    token_count: int
    complexity_score: float

@dataclass
class DuplicationAlert:
    """Duplication detection alert with detailed analysis"""
    source_file: str
    target_file: str
    similarity_score: float
    duplicate_type: str
    confidence: float
    evidence: Dict[str, Any]
    recommendation: str
    auto_resolvable: bool
    priority: str

@dataclass
class ConceptualConnection:
    """Discovered conceptual relationship between content pieces"""
    entity_a: str
    entity_b: str
    connection_type: str
    strength: float
    evidence: List[str]
    automatic_discoverable: bool
    network_benefit: float

class AdvancedDuplicationPrevention:
    """Next-generation duplication prevention with AI-driven analysis"""
    
    def __init__(self, knowledge_path: str = None):
        self.knowledge_path = Path(knowledge_path or "/Users/nalve/claude-context-engineering")
        self.cache_path = self.knowledge_path / "scripts" / "cache"
        self.cache_path.mkdir(parents=True, exist_ok=True)
        
        # Content fingerprint cache
        self.fingerprint_cache = {}
        self.semantic_cache = {}
        self.relationship_cache = defaultdict(list)
        
        # Analysis parameters
        self.similarity_thresholds = {
            'CRITICAL': 0.95,      # Immediate blocking
            'HIGH': 0.85,          # Warning with review
            'MEDIUM': 0.70,        # Monitoring required
            'LOW': 0.55,           # Tracking only
            'CONCEPTUAL': 0.60     # Conceptual similarity
        }
        
        # Content analysis weights
        self.analysis_weights = {
            'exact_content': 0.35,
            'semantic_similarity': 0.25,
            'functional_overlap': 0.20,
            'structural_similarity': 0.15,
            'conceptual_distance': 0.05
        }
        
        # Keywords for functional analysis
        self.functional_keywords = {
            'execution': ['execute', 'run', 'perform', 'implement', 'deploy'],
            'validation': ['validate', 'verify', 'check', 'test', 'confirm'],
            'orchestration': ['orchestrate', 'coordinate', 'manage', 'control'],
            'optimization': ['optimize', 'improve', 'enhance', 'efficient'],
            'intelligence': ['intelligent', 'smart', 'adaptive', 'learning'],
            'documentation': ['document', 'record', 'track', 'log', 'report'],
            'automation': ['automate', 'automatic', 'autonomous', 'self'],
            'integration': ['integrate', 'connect', 'link', 'bridge', 'sync']
        }
        
        # Conceptual clusters for relationship discovery
        self.concept_clusters = {
            'mathematical_rigor': ['mathematical', 'precision', 'accuracy', 'calculation'],
            'system_orchestration': ['orchestration', 'coordination', 'management'],
            'quality_assurance': ['quality', 'validation', 'verification', 'testing'],
            'intelligent_automation': ['intelligence', 'automation', 'adaptive'],
            'documentation_lifecycle': ['documentation', 'living', 'evolution'],
            'parallel_execution': ['parallel', 'concurrent', 'simultaneous'],
            'modular_architecture': ['modular', 'component', 'architecture'],
            'cross_reference': ['cross-reference', 'linking', 'connectivity']
        }
    
    def analyze_content_fingerprint(self, file_path: Path) -> ContentFingerprint:
        """Generate comprehensive content fingerprint for duplication analysis"""
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Content hash (exact matching)
            content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
            
            # Semantic hash (normalized content)
            normalized_content = self._normalize_content(content)
            semantic_hash = hashlib.sha256(normalized_content.encode()).hexdigest()[:16]
            
            # Functional keyword extraction
            functional_keywords = self._extract_functional_keywords(content)
            
            # Structural pattern analysis
            structural_patterns = self._analyze_structural_patterns(content)
            
            # Concept cluster analysis
            concept_clusters = self._identify_concept_clusters(content)
            
            # Metrics
            token_count = len(content.split())
            complexity_score = self._calculate_complexity_score(content)
            
            fingerprint = ContentFingerprint(
                content_hash=content_hash,
                semantic_hash=semantic_hash,
                functional_keywords=functional_keywords,
                structural_patterns=structural_patterns,
                concept_clusters=concept_clusters,
                token_count=token_count,
                complexity_score=complexity_score
            )
            
            # Cache fingerprint
            self.fingerprint_cache[str(file_path)] = fingerprint
            return fingerprint
            
        except Exception as e:
            print(f"❌ Error analyzing {file_path}: {e}")
            return ContentFingerprint("", "", set(), [], [], 0, 0.0)
    
    def _normalize_content(self, content: str) -> str:
        """Normalize content for semantic comparison"""
        # Remove metadata and formatting
        normalized = re.sub(r'^---.*?---', '', content, flags=re.DOTALL)
        normalized = re.sub(r'#+\s*', '', normalized)  # Remove headers
        normalized = re.sub(r'\*\*([^*]+)\*\*', r'\1', normalized)  # Remove bold
        normalized = re.sub(r'\*([^*]+)\*', r'\1', normalized)  # Remove italic
        normalized = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', normalized)  # Remove links
        normalized = re.sub(r'`([^`]+)`', r'\1', normalized)  # Remove code
        
        # Normalize whitespace
        normalized = re.sub(r'\s+', ' ', normalized).strip().lower()
        
        return normalized
    
    def _extract_functional_keywords(self, content: str) -> Set[str]:
        """Extract functional keywords from content"""
        content_lower = content.lower()
        found_keywords = set()
        
        for category, keywords in self.functional_keywords.items():
            for keyword in keywords:
                if keyword in content_lower:
                    found_keywords.add(f"{category}:{keyword}")
        
        return found_keywords
    
    def _analyze_structural_patterns(self, content: str) -> List[str]:
        """Analyze structural patterns in content"""
        patterns = []
        
        # Header patterns
        headers = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
        if headers:
            header_pattern = ''.join([h[0] for h in headers[:5]])  # First 5 headers
            patterns.append(f"headers:{header_pattern}")
        
        # List patterns
        list_items = re.findall(r'^[-*]\s+', content, re.MULTILINE)
        if len(list_items) > 5:
            patterns.append(f"lists:heavy_{len(list_items)}")
        
        # Code block patterns
        code_blocks = re.findall(r'```(\w+)?', content)
        if code_blocks:
            patterns.append(f"code:{len(code_blocks)}")
        
        # Link patterns
        links = re.findall(r'\[([^\]]+)\]\([^)]+\)', content)
        if len(links) > 10:
            patterns.append(f"links:heavy_{len(links)}")
        
        # Table patterns
        tables = re.findall(r'\|.*\|', content)
        if len(tables) > 5:
            patterns.append("tables:present")
        
        return patterns
    
    def _identify_concept_clusters(self, content: str) -> List[str]:
        """Identify conceptual clusters in content"""
        content_lower = content.lower()
        identified_clusters = []
        
        for cluster_name, keywords in self.concept_clusters.items():
            keyword_count = sum(1 for keyword in keywords if keyword in content_lower)
            if keyword_count >= 2:  # Minimum 2 keywords for cluster identification
                identified_clusters.append(f"{cluster_name}:{keyword_count}")
        
        return identified_clusters
    
    def _calculate_complexity_score(self, content: str) -> float:
        """Calculate content complexity score"""
        # Word count factor
        word_count = len(content.split())
        word_factor = min(word_count / 1000.0, 1.0)
        
        # Sentence complexity
        sentences = re.split(r'[.!?]+', content)
        avg_sentence_length = sum(len(s.split()) for s in sentences) / max(len(sentences), 1)
        sentence_factor = min(avg_sentence_length / 20.0, 1.0)
        
        # Technical term density
        technical_terms = re.findall(r'\b[A-Z][a-z]*[A-Z][a-zA-Z]*\b', content)  # CamelCase
        technical_factor = min(len(technical_terms) / 50.0, 1.0)
        
        # Link density
        links = re.findall(r'\[([^\]]+)\]\([^)]+\)', content)
        link_factor = min(len(links) / 20.0, 1.0)
        
        complexity = (word_factor * 0.3 + sentence_factor * 0.3 + 
                     technical_factor * 0.2 + link_factor * 0.2)
        
        return complexity
    
    def detect_content_duplication(self, file_a: Path, file_b: Path) -> Optional[DuplicationAlert]:
        """Detect and analyze content duplication between two files"""
        fingerprint_a = self.analyze_content_fingerprint(file_a)
        fingerprint_b = self.analyze_content_fingerprint(file_b)
        
        # Calculate similarity scores
        similarity_scores = self._calculate_comprehensive_similarity(fingerprint_a, fingerprint_b)
        overall_similarity = self._calculate_weighted_similarity(similarity_scores)
        
        # Determine alert level
        alert_level = self._determine_alert_level(overall_similarity)
        
        if alert_level in ['CRITICAL', 'HIGH', 'MEDIUM']:
            # Analyze duplication type
            duplication_type = self._classify_duplication_type(similarity_scores, fingerprint_a, fingerprint_b)
            
            # Generate evidence
            evidence = self._collect_duplication_evidence(file_a, file_b, fingerprint_a, fingerprint_b, similarity_scores)
            
            # Generate recommendation
            recommendation = self._generate_duplication_recommendation(duplication_type, similarity_scores, alert_level)
            
            # Determine if auto-resolvable
            auto_resolvable = self._is_auto_resolvable(duplication_type, overall_similarity)
            
            return DuplicationAlert(
                source_file=str(file_a),
                target_file=str(file_b),
                similarity_score=overall_similarity,
                duplicate_type=duplication_type,
                confidence=self._calculate_confidence(similarity_scores),
                evidence=evidence,
                recommendation=recommendation,
                auto_resolvable=auto_resolvable,
                priority=alert_level
            )
        
        return None
    
    def _calculate_comprehensive_similarity(self, fp_a: ContentFingerprint, fp_b: ContentFingerprint) -> Dict[str, float]:
        """Calculate comprehensive similarity metrics"""
        similarities = {}
        
        # Exact content similarity
        similarities['exact_content'] = 1.0 if fp_a.content_hash == fp_b.content_hash else 0.0
        
        # Semantic similarity
        similarities['semantic_similarity'] = 1.0 if fp_a.semantic_hash == fp_b.semantic_hash else \
                                            self._calculate_token_similarity(fp_a, fp_b)
        
        # Functional overlap
        if fp_a.functional_keywords and fp_b.functional_keywords:
            common_keywords = fp_a.functional_keywords.intersection(fp_b.functional_keywords)
            total_keywords = fp_a.functional_keywords.union(fp_b.functional_keywords)
            similarities['functional_overlap'] = len(common_keywords) / len(total_keywords)
        else:
            similarities['functional_overlap'] = 0.0
        
        # Structural similarity
        similarities['structural_similarity'] = self._calculate_structural_similarity(fp_a, fp_b)
        
        # Conceptual distance
        similarities['conceptual_distance'] = self._calculate_conceptual_similarity(fp_a, fp_b)
        
        return similarities
    
    def _calculate_token_similarity(self, fp_a: ContentFingerprint, fp_b: ContentFingerprint) -> float:
        """Calculate token-level similarity using fingerprint metadata"""
        # Size similarity
        size_ratio = min(fp_a.token_count, fp_b.token_count) / max(fp_a.token_count, fp_b.token_count, 1)
        
        # Complexity similarity
        complexity_diff = abs(fp_a.complexity_score - fp_b.complexity_score)
        complexity_similarity = max(0.0, 1.0 - complexity_diff)
        
        return (size_ratio * 0.6 + complexity_similarity * 0.4)
    
    def _calculate_structural_similarity(self, fp_a: ContentFingerprint, fp_b: ContentFingerprint) -> float:
        """Calculate structural pattern similarity"""
        if not fp_a.structural_patterns and not fp_b.structural_patterns:
            return 0.0
        
        common_patterns = set(fp_a.structural_patterns).intersection(set(fp_b.structural_patterns))
        total_patterns = set(fp_a.structural_patterns).union(set(fp_b.structural_patterns))
        
        return len(common_patterns) / len(total_patterns) if total_patterns else 0.0
    
    def _calculate_conceptual_similarity(self, fp_a: ContentFingerprint, fp_b: ContentFingerprint) -> float:
        """Calculate conceptual cluster similarity"""
        if not fp_a.concept_clusters and not fp_b.concept_clusters:
            return 0.0
        
        common_clusters = set(fp_a.concept_clusters).intersection(set(fp_b.concept_clusters))
        total_clusters = set(fp_a.concept_clusters).union(set(fp_b.concept_clusters))
        
        return len(common_clusters) / len(total_clusters) if total_clusters else 0.0
    
    def _calculate_weighted_similarity(self, similarities: Dict[str, float]) -> float:
        """Calculate weighted overall similarity score"""
        weighted_sum = sum(similarities[key] * self.analysis_weights[key] 
                          for key in similarities if key in self.analysis_weights)
        return weighted_sum
    
    def _determine_alert_level(self, similarity_score: float) -> str:
        """Determine alert level based on similarity score"""
        for level, threshold in self.similarity_thresholds.items():
            if similarity_score >= threshold:
                return level
        return 'NONE'
    
    def _classify_duplication_type(self, similarities: Dict[str, float], fp_a: ContentFingerprint, fp_b: ContentFingerprint) -> str:
        """Classify the type of duplication detected"""
        if similarities['exact_content'] == 1.0:
            return 'EXACT_DUPLICATE'
        elif similarities['semantic_similarity'] > 0.9:
            return 'SEMANTIC_DUPLICATE'
        elif similarities['functional_overlap'] > 0.8:
            return 'FUNCTIONAL_DUPLICATE'
        elif similarities['structural_similarity'] > 0.8:
            return 'STRUCTURAL_DUPLICATE'
        elif similarities['conceptual_distance'] > 0.7:
            return 'CONCEPTUAL_OVERLAP'
        else:
            return 'PARTIAL_SIMILARITY'
    
    def _collect_duplication_evidence(self, file_a: Path, file_b: Path, 
                                    fp_a: ContentFingerprint, fp_b: ContentFingerprint,
                                    similarities: Dict[str, float]) -> Dict[str, Any]:
        """Collect detailed evidence for duplication alert"""
        evidence = {
            'similarity_breakdown': similarities,
            'file_sizes': {
                'file_a_tokens': fp_a.token_count,
                'file_b_tokens': fp_b.token_count,
                'size_ratio': min(fp_a.token_count, fp_b.token_count) / max(fp_a.token_count, fp_b.token_count, 1)
            },
            'content_hashes': {
                'file_a_content_hash': fp_a.content_hash,
                'file_b_content_hash': fp_b.content_hash,
                'file_a_semantic_hash': fp_a.semantic_hash,
                'file_b_semantic_hash': fp_b.semantic_hash
            },
            'functional_analysis': {
                'common_keywords': list(fp_a.functional_keywords.intersection(fp_b.functional_keywords)),
                'unique_to_a': list(fp_a.functional_keywords - fp_b.functional_keywords),
                'unique_to_b': list(fp_b.functional_keywords - fp_a.functional_keywords)
            },
            'structural_analysis': {
                'common_patterns': list(set(fp_a.structural_patterns).intersection(set(fp_b.structural_patterns))),
                'patterns_a': fp_a.structural_patterns,
                'patterns_b': fp_b.structural_patterns
            },
            'conceptual_analysis': {
                'common_clusters': list(set(fp_a.concept_clusters).intersection(set(fp_b.concept_clusters))),
                'clusters_a': fp_a.concept_clusters,
                'clusters_b': fp_b.concept_clusters
            }
        }
        
        return evidence
    
    def _generate_duplication_recommendation(self, duplication_type: str, similarities: Dict[str, float], alert_level: str) -> str:
        """Generate actionable recommendation for duplication resolution"""
        recommendations = {
            'EXACT_DUPLICATE': "IMMEDIATE ACTION: Remove one file and update all references to point to the remaining file.",
            'SEMANTIC_DUPLICATE': "CONSOLIDATE: Merge content into single authoritative file with enhanced cross-references.",
            'FUNCTIONAL_DUPLICATE': "REVIEW: Analyze functional overlap and consider consolidation or clearer differentiation.",
            'STRUCTURAL_DUPLICATE': "OPTIMIZE: Standardize structure or consolidate if content serves same purpose.",
            'CONCEPTUAL_OVERLAP': "CROSS-REFERENCE: Enhance linking between related concepts without consolidation.",
            'PARTIAL_SIMILARITY': "MONITOR: Track for potential future consolidation as content evolves."
        }
        
        base_recommendation = recommendations.get(duplication_type, "INVESTIGATE: Manual review required.")
        
        if alert_level == 'CRITICAL':
            return f"🚨 CRITICAL: {base_recommendation}"
        elif alert_level == 'HIGH':
            return f"⚠️ HIGH PRIORITY: {base_recommendation}"
        else:
            return f"📋 MONITOR: {base_recommendation}"
    
    def _is_auto_resolvable(self, duplication_type: str, similarity_score: float) -> bool:
        """Determine if duplication can be automatically resolved"""
        auto_resolvable_types = ['EXACT_DUPLICATE']
        return duplication_type in auto_resolvable_types and similarity_score >= 0.98
    
    def _calculate_confidence(self, similarities: Dict[str, float]) -> float:
        """Calculate confidence level in duplication detection"""
        # Higher confidence for multiple high similarity scores
        high_scores = sum(1 for score in similarities.values() if score > 0.8)
        confidence_base = max(similarities.values())
        
        # Boost confidence if multiple metrics agree
        if high_scores >= 3:
            confidence_boost = 0.1
        elif high_scores >= 2:
            confidence_boost = 0.05
        else:
            confidence_boost = 0.0
        
        return min(confidence_base + confidence_boost, 1.0)
    
    def discover_conceptual_connections(self, content_directory: Path) -> List[ConceptualConnection]:
        """Discover conceptual connections between content pieces"""
        connections = []
        
        # Get all markdown files
        md_files = list(content_directory.rglob("*.md"))
        fingerprints = {}
        
        # Generate fingerprints for all files
        for file_path in md_files:
            fingerprints[str(file_path)] = self.analyze_content_fingerprint(file_path)
        
        # Analyze all pairs for conceptual connections
        for i, file_a in enumerate(md_files):
            for file_b in md_files[i+1:]:
                connection = self._analyze_conceptual_connection(
                    str(file_a), str(file_b),
                    fingerprints[str(file_a)], fingerprints[str(file_b)]
                )
                
                if connection and connection.strength > 0.6:
                    connections.append(connection)
        
        # Sort by strength and network benefit
        connections.sort(key=lambda x: (x.strength * x.network_benefit), reverse=True)
        return connections
    
    def _analyze_conceptual_connection(self, file_a: str, file_b: str, 
                                     fp_a: ContentFingerprint, fp_b: ContentFingerprint) -> Optional[ConceptualConnection]:
        """Analyze potential conceptual connection between two files"""
        # Skip if too similar (likely duplicates)
        similarities = self._calculate_comprehensive_similarity(fp_a, fp_b)
        overall_similarity = self._calculate_weighted_similarity(similarities)
        
        if overall_similarity > 0.8:
            return None  # Too similar, likely duplicate
        
        # Calculate conceptual connection strength
        conceptual_strength = self._calculate_connection_strength(fp_a, fp_b)
        
        if conceptual_strength < 0.3:
            return None  # Too weak connection
        
        # Determine connection type
        connection_type = self._determine_connection_type(fp_a, fp_b, similarities)
        
        # Collect evidence
        evidence = self._collect_connection_evidence(fp_a, fp_b)
        
        # Calculate network benefit
        network_benefit = self._calculate_network_benefit_potential(file_a, file_b)
        
        # Determine if automatically discoverable
        auto_discoverable = conceptual_strength > 0.7 and len(evidence) >= 3
        
        return ConceptualConnection(
            entity_a=file_a,
            entity_b=file_b,
            connection_type=connection_type,
            strength=conceptual_strength,
            evidence=evidence,
            automatic_discoverable=auto_discoverable,
            network_benefit=network_benefit
        )
    
    def _calculate_connection_strength(self, fp_a: ContentFingerprint, fp_b: ContentFingerprint) -> float:
        """Calculate strength of conceptual connection"""
        strength_factors = []
        
        # Functional keyword overlap
        if fp_a.functional_keywords and fp_b.functional_keywords:
            common_keywords = fp_a.functional_keywords.intersection(fp_b.functional_keywords)
            keyword_strength = len(common_keywords) / 5.0  # Normalize to max 5 keywords
            strength_factors.append(min(keyword_strength, 1.0) * 0.3)
        
        # Concept cluster overlap
        if fp_a.concept_clusters and fp_b.concept_clusters:
            common_clusters = set(fp_a.concept_clusters).intersection(set(fp_b.concept_clusters))
            cluster_strength = len(common_clusters) / 3.0  # Normalize to max 3 clusters
            strength_factors.append(min(cluster_strength, 1.0) * 0.4)
        
        # Complexity compatibility
        complexity_diff = abs(fp_a.complexity_score - fp_b.complexity_score)
        complexity_strength = max(0.0, 1.0 - complexity_diff)
        strength_factors.append(complexity_strength * 0.2)
        
        # Size compatibility
        if fp_a.token_count > 0 and fp_b.token_count > 0:
            size_ratio = min(fp_a.token_count, fp_b.token_count) / max(fp_a.token_count, fp_b.token_count)
            strength_factors.append(size_ratio * 0.1)
        
        return sum(strength_factors)
    
    def _determine_connection_type(self, fp_a: ContentFingerprint, fp_b: ContentFingerprint, 
                                 similarities: Dict[str, float]) -> str:
        """Determine type of conceptual connection"""
        if similarities['functional_overlap'] > 0.6:
            return 'Functional Synergy'
        elif similarities['conceptual_distance'] > 0.5:
            return 'Conceptual Enhancement'
        elif similarities['structural_similarity'] > 0.5:
            return 'Architectural Alignment'
        else:
            return 'Strategic Integration'
    
    def _collect_connection_evidence(self, fp_a: ContentFingerprint, fp_b: ContentFingerprint) -> List[str]:
        """Collect evidence supporting conceptual connection"""
        evidence = []
        
        # Common functional keywords
        common_keywords = fp_a.functional_keywords.intersection(fp_b.functional_keywords)
        if common_keywords:
            evidence.append(f"Shared functional focus: {', '.join(list(common_keywords)[:3])}")
        
        # Common concept clusters
        common_clusters = set(fp_a.concept_clusters).intersection(set(fp_b.concept_clusters))
        if common_clusters:
            evidence.append(f"Common conceptual areas: {', '.join(list(common_clusters)[:2])}")
        
        # Similar complexity
        if abs(fp_a.complexity_score - fp_b.complexity_score) < 0.2:
            evidence.append(f"Compatible complexity levels ({fp_a.complexity_score:.2f}, {fp_b.complexity_score:.2f})")
        
        # Similar structural patterns
        common_patterns = set(fp_a.structural_patterns).intersection(set(fp_b.structural_patterns))
        if common_patterns:
            evidence.append(f"Similar structural patterns: {', '.join(list(common_patterns)[:2])}")
        
        return evidence
    
    def _calculate_network_benefit_potential(self, file_a: str, file_b: str) -> float:
        """Calculate potential network benefit of connection"""
        # Simplified calculation - would be enhanced with actual network analysis
        path_a = Path(file_a)
        path_b = Path(file_b)
        
        # Cross-directory connections have higher benefit
        if path_a.parent != path_b.parent:
            cross_benefit = 0.3
        else:
            cross_benefit = 0.0
        
        # Strategic file types have higher benefit
        strategic_patterns = ['principle', 'command', 'protocol', 'framework']
        strategic_count = sum(1 for pattern in strategic_patterns 
                            if pattern in path_a.name.lower() or pattern in path_b.name.lower())
        strategic_benefit = strategic_count * 0.2
        
        base_benefit = 0.5
        return min(base_benefit + cross_benefit + strategic_benefit, 1.0)
    
    def generate_intelligence_report(self, scan_directory: Path) -> str:
        """Generate comprehensive intelligence analysis report"""
        report = []
        report.append("# 🧠 Cross-Reference Intelligence Analysis Report")
        report.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Scope**: {scan_directory}")
        report.append("")
        
        # Scan for duplications
        print("🔍 Scanning for content duplications...")
        duplications = self._scan_for_duplications(scan_directory)
        
        # Discover conceptual connections
        print("🚀 Discovering conceptual connections...")
        connections = self.discover_conceptual_connections(scan_directory)
        
        # Duplication analysis section
        if duplications:
            report.append("## 🚨 Duplication Analysis")
            report.append("")
            
            by_priority = defaultdict(list)
            for dup in duplications:
                by_priority[dup.priority].append(dup)
            
            for priority in ['CRITICAL', 'HIGH', 'MEDIUM']:
                if by_priority[priority]:
                    report.append(f"### {priority} Priority Duplications")
                    report.append("")
                    for dup in by_priority[priority][:5]:  # Top 5 per priority
                        report.append(f"**{Path(dup.source_file).name}** ↔ **{Path(dup.target_file).name}**")
                        report.append(f"- Similarity: {dup.similarity_score:.1%}")
                        report.append(f"- Type: {dup.duplicate_type}")
                        report.append(f"- Confidence: {dup.confidence:.1%}")
                        report.append(f"- {dup.recommendation}")
                        report.append("")
        
        # Conceptual connections section
        if connections:
            report.append("## 🔗 Discovered Conceptual Connections")
            report.append("")
            
            high_value_connections = [c for c in connections if c.strength > 0.7]
            if high_value_connections:
                report.append("### High-Value Connection Opportunities")
                report.append("")
                for conn in high_value_connections[:10]:
                    report.append(f"**{Path(conn.entity_a).name}** ↔ **{Path(conn.entity_b).name}**")
                    report.append(f"- Connection Type: {conn.connection_type}")
                    report.append(f"- Strength: {conn.strength:.1%}")
                    report.append(f"- Network Benefit: {conn.network_benefit:.1%}")
                    if conn.evidence:
                        report.append(f"- Evidence: {conn.evidence[0]}")
                    report.append("")
        
        # Intelligence metrics
        report.append("## 📊 Intelligence Metrics")
        report.append("")
        report.append(f"- **Total Files Analyzed**: {len(list(scan_directory.rglob('*.md')))}")
        report.append(f"- **Duplications Detected**: {len(duplications)}")
        report.append(f"- **Conceptual Connections Found**: {len(connections)}")
        report.append(f"- **High-Value Connections**: {len([c for c in connections if c.strength > 0.7])}")
        report.append(f"- **Auto-Resolvable Issues**: {len([d for d in duplications if d.auto_resolvable])}")
        report.append("")
        
        return "\n".join(report)
    
    def _scan_for_duplications(self, directory: Path) -> List[DuplicationAlert]:
        """Scan directory for content duplications"""
        duplications = []
        md_files = list(directory.rglob("*.md"))
        
        print(f"📂 Analyzing {len(md_files)} files for duplications...")
        
        # Compare all file pairs
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = []
            for i, file_a in enumerate(md_files):
                for file_b in md_files[i+1:]:
                    future = executor.submit(self.detect_content_duplication, file_a, file_b)
                    futures.append(future)
            
            for future in futures:
                result = future.result()
                if result:
                    duplications.append(result)
        
        return duplications


def main():
    """Main execution function"""
    prevention = AdvancedDuplicationPrevention()
    
    print("🧠 Starting Advanced Cross-Reference Intelligence Analysis...")
    
    # Analyze knowledge directory
    knowledge_dir = Path("/Users/nalve/claude-context-engineering/knowledge")
    if not knowledge_dir.exists():
        print(f"❌ Knowledge directory not found: {knowledge_dir}")
        return 1
    
    # Generate intelligence report
    print("📊 Generating comprehensive intelligence report...")
    report = prevention.generate_intelligence_report(knowledge_dir)
    
    # Save report
    report_path = Path("operations/reports/current/cross-reference-intelligence-analysis.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    
    print(f"✅ Intelligence analysis complete!")
    print(f"📋 Report saved to: {report_path}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())