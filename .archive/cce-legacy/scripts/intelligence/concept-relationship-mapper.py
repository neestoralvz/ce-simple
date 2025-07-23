#!/usr/bin/env python3
"""
Intelligent Concept Relationship Mapping System
Advanced AI-Driven Conceptual Network Discovery and Optimization

This module provides sophisticated algorithms for discovering, mapping, and
optimizing conceptual relationships across the Context Engineering ecosystem
with next-level automated intelligence and network optimization.
"""

import json
import re
import sys
import math
from pathlib import Path
from typing import Dict, List, Tuple, Set, Any, Optional
from collections import defaultdict, Counter
from datetime import datetime
from dataclasses import dataclass, asdict
import networkx as nx
from itertools import combinations
import pickle
import hashlib

@dataclass
class ConceptNode:
    """Individual concept node in the relationship network"""
    concept_id: str
    concept_name: str
    concept_type: str
    source_files: List[str]
    semantic_features: Set[str]
    context_domains: Set[str]
    importance_score: float
    centrality_metrics: Dict[str, float]

@dataclass
class ConceptRelationship:
    """Relationship between two concepts"""
    source_concept: str
    target_concept: str
    relationship_type: str
    strength: float
    confidence: float
    evidence: List[str]
    co_occurrence_frequency: int
    semantic_similarity: float
    contextual_affinity: float
    network_benefit: float

@dataclass
class ConceptCluster:
    """Cluster of related concepts"""
    cluster_id: str
    cluster_name: str
    concepts: List[str]
    cohesion_score: float
    cluster_type: str
    representative_concepts: List[str]
    cross_cluster_connections: Dict[str, int]

@dataclass
class NetworkInsight:
    """Intelligent insight about the concept network"""
    insight_type: str
    insight_level: str
    description: str
    affected_concepts: List[str]
    evidence: List[str]
    actionable_recommendations: List[str]
    confidence: float
    impact_potential: float

class ConceptRelationshipMapper:
    """Advanced intelligent concept relationship mapping system"""
    
    def __init__(self, knowledge_path: str = None):
        self.knowledge_path = Path(knowledge_path or "/Users/nalve/claude-context-engineering")
        self.cache_path = self.knowledge_path / "scripts" / "cache" / "concept_mapping"
        self.cache_path.mkdir(parents=True, exist_ok=True)
        
        # Concept network
        self.concept_graph = nx.Graph()
        self.concepts = {}
        self.relationships = []
        self.clusters = {}
        
        # AI analysis parameters
        self.concept_extraction_patterns = {
            'principle': r'[Pp]rinciple\s*#?(\d+)|[Pp]rinciple\s+([A-Z][^.]*?)(?:\.|$)',
            'command': r'(?:command|cmd)\s*[`"\']?([a-z-]+)[`"\']?',
            'protocol': r'[Pp]rotocol\s*[:\-]?\s*([A-Z][^.]*?)(?:\.|$)',
            'framework': r'[Ff]ramework\s*[:\-]?\s*([A-Z][^.]*?)(?:\.|$)',
            'system': r'[Ss]ystem\s*[:\-]?\s*([A-Z][^.]*?)(?:\.|$)',
            'methodology': r'[Mm]ethodology\s*[:\-]?\s*([A-Z][^.]*?)(?:\.|$)',
            'pattern': r'[Pp]attern\s*[:\-]?\s*([A-Z][^.]*?)(?:\.|$)',
            'architecture': r'[Aa]rchitecture\s*[:\-]?\s*([A-Z][^.]*?)(?:\.|$)'
        }
        
        # Semantic domains for concept classification
        self.semantic_domains = {
            'mathematical': ['mathematical', 'calculation', 'precision', 'formula', 'algorithm', 'metric'],
            'orchestration': ['orchestration', 'coordination', 'management', 'workflow', 'execution'],
            'intelligence': ['intelligence', 'ai', 'automated', 'smart', 'adaptive', 'learning'],
            'documentation': ['documentation', 'document', 'guide', 'manual', 'specification'],
            'validation': ['validation', 'verification', 'testing', 'quality', 'assurance', 'check'],
            'architecture': ['architecture', 'structure', 'design', 'pattern', 'framework', 'system'],
            'optimization': ['optimization', 'performance', 'efficiency', 'improvement', 'enhancement'],
            'integration': ['integration', 'connection', 'linking', 'bridge', 'interface', 'sync']
        }
        
        # Relationship discovery thresholds
        self.relationship_thresholds = {
            'co_occurrence': 3,        # Minimum co-occurrence frequency
            'semantic_similarity': 0.6, # Minimum semantic similarity
            'contextual_affinity': 0.5,  # Minimum contextual affinity
            'network_benefit': 0.4      # Minimum network benefit score
        }
        
        # Clustering parameters
        self.clustering_config = {
            'min_cluster_size': 3,
            'max_cluster_size': 15,
            'cohesion_threshold': 0.7,
            'merge_threshold': 0.8
        }
    
    def extract_concepts_from_content(self, file_path: Path) -> List[Dict[str, Any]]:
        """Extract concepts from file content using AI-driven analysis"""
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"❌ Could not read {file_path}: {e}")
            return []
        
        concepts = []
        
        # Extract explicit concepts using patterns
        for concept_type, pattern in self.concept_extraction_patterns.items():
            for match in re.finditer(pattern, content, re.IGNORECASE):
                concept_text = match.group(1) or match.group(2) if match.lastindex > 1 else match.group(1)
                if concept_text and len(concept_text.strip()) > 2:
                    concept_id = self._generate_concept_id(concept_text, concept_type)
                    
                    concept = {
                        'id': concept_id,
                        'name': concept_text.strip(),
                        'type': concept_type,
                        'source_file': str(file_path),
                        'context': self._extract_concept_context(content, match),
                        'position': match.start()
                    }
                    concepts.append(concept)
        
        # Extract implicit concepts from headers and key terms
        implicit_concepts = self._extract_implicit_concepts(content, file_path)
        concepts.extend(implicit_concepts)
        
        # Analyze semantic features for each concept
        for concept in concepts:
            concept['semantic_features'] = self._analyze_semantic_features(concept['name'], concept['context'])
            concept['context_domains'] = self._classify_context_domains(concept['context'])
            concept['importance_score'] = self._calculate_concept_importance(concept, content)
        
        return concepts
    
    def _generate_concept_id(self, concept_text: str, concept_type: str) -> str:
        """Generate unique concept ID"""
        normalized_text = re.sub(r'\W+', '_', concept_text.lower()).strip('_')
        hash_suffix = hashlib.md5(f"{concept_type}:{concept_text}".encode()).hexdigest()[:8]
        return f"{concept_type}_{normalized_text}_{hash_suffix}"
    
    def _extract_concept_context(self, content: str, match, context_size: int = 200) -> str:
        """Extract context around concept mention"""
        start = max(0, match.start() - context_size)
        end = min(len(content), match.end() + context_size)
        context = content[start:end]
        return re.sub(r'\s+', ' ', context).strip()
    
    def _extract_implicit_concepts(self, content: str, file_path: Path) -> List[Dict[str, Any]]:
        """Extract implicit concepts from content structure"""
        concepts = []
        
        # Extract from headers
        header_pattern = r'^(#{1,6})\s+(.+)$'
        for match in re.finditer(header_pattern, content, re.MULTILINE):
            header_level = len(match.group(1))
            header_text = match.group(2).strip()
            
            if len(header_text) > 3 and header_level <= 3:  # Focus on main headers
                concept_id = self._generate_concept_id(header_text, 'section')
                
                concept = {
                    'id': concept_id,
                    'name': header_text,
                    'type': 'section',
                    'source_file': str(file_path),
                    'context': self._extract_concept_context(content, match),
                    'position': match.start(),
                    'header_level': header_level
                }
                concepts.append(concept)
        
        # Extract from emphasized terms
        emphasis_pattern = r'\*\*([^*]+)\*\*'
        for match in re.finditer(emphasis_pattern, content):
            emphasized_text = match.group(1).strip()
            
            if 5 <= len(emphasized_text) <= 50 and not emphasized_text.isdigit():
                concept_id = self._generate_concept_id(emphasized_text, 'emphasis')
                
                concept = {
                    'id': concept_id,
                    'name': emphasized_text,
                    'type': 'emphasis',
                    'source_file': str(file_path),
                    'context': self._extract_concept_context(content, match),
                    'position': match.start()
                }
                concepts.append(concept)
        
        return concepts
    
    def _analyze_semantic_features(self, concept_name: str, context: str) -> Set[str]:
        """Analyze semantic features of a concept"""
        features = set()
        
        # Combine concept name and context for analysis
        text = f"{concept_name} {context}".lower()
        
        # Extract key terms
        words = re.findall(r'\b\w+\b', text)
        word_freq = Counter(words)
        
        # Identify significant terms
        for word, freq in word_freq.items():
            if len(word) > 3 and freq >= 2:
                features.add(f"term:{word}")
        
        # Identify semantic patterns
        if re.search(r'\b(auto|automatic|automated)\b', text):
            features.add('automation')
        if re.search(r'\b(intelligen|smart|ai|ml)\b', text):
            features.add('intelligence')
        if re.search(r'\b(optim|improv|enhanc)\b', text):
            features.add('optimization')
        if re.search(r'\b(valid|verif|test)\b', text):
            features.add('validation')
        if re.search(r'\b(document|record|track)\b', text):
            features.add('documentation')
        if re.search(r'\b(execut|run|perform)\b', text):
            features.add('execution')
        if re.search(r'\b(connect|link|integrat)\b', text):
            features.add('integration')
        if re.search(r'\b(architect|structur|design)\b', text):
            features.add('architecture')
        
        return features
    
    def _classify_context_domains(self, context: str) -> Set[str]:
        """Classify context into semantic domains"""
        domains = set()
        context_lower = context.lower()
        
        for domain, keywords in self.semantic_domains.items():
            domain_score = sum(1 for keyword in keywords if keyword in context_lower)
            if domain_score >= 2:  # Minimum 2 keywords for domain classification
                domains.add(domain)
        
        return domains
    
    def _calculate_concept_importance(self, concept: Dict[str, Any], full_content: str) -> float:
        """Calculate importance score for a concept"""
        importance_factors = []
        
        # Frequency factor
        concept_mentions = full_content.lower().count(concept['name'].lower())
        frequency_score = min(concept_mentions / 10.0, 1.0)  # Normalize to max 10 mentions
        importance_factors.append(frequency_score * 0.3)
        
        # Position factor (earlier mentions are more important)
        position_score = max(0.0, 1.0 - (concept['position'] / len(full_content)))
        importance_factors.append(position_score * 0.2)
        
        # Type factor
        type_weights = {
            'principle': 1.0,
            'framework': 0.9,
            'protocol': 0.8,
            'system': 0.7,
            'command': 0.6,
            'section': 0.4,
            'emphasis': 0.3
        }
        type_score = type_weights.get(concept['type'], 0.5)
        importance_factors.append(type_score * 0.3)
        
        # Context richness factor
        context_richness = min(len(concept['context'].split()) / 50.0, 1.0)
        importance_factors.append(context_richness * 0.2)
        
        return sum(importance_factors)
    
    def discover_concept_relationships(self, concepts: List[Dict[str, Any]]) -> List[ConceptRelationship]:
        """Discover relationships between concepts using AI algorithms"""
        relationships = []
        
        # Group concepts by source file for co-occurrence analysis
        file_concepts = defaultdict(list)
        for concept in concepts:
            file_concepts[concept['source_file']].append(concept)
        
        # Analyze all concept pairs
        for i, concept_a in enumerate(concepts):
            for concept_b in concepts[i+1:]:
                relationship = self._analyze_concept_relationship(concept_a, concept_b, file_concepts)
                if relationship and relationship.strength > 0.3:
                    relationships.append(relationship)
        
        # Sort by strength and confidence
        relationships.sort(key=lambda r: r.strength * r.confidence, reverse=True)
        
        return relationships
    
    def _analyze_concept_relationship(self, concept_a: Dict[str, Any], concept_b: Dict[str, Any], 
                                   file_concepts: Dict[str, List[Dict]]) -> Optional[ConceptRelationship]:
        """Analyze relationship between two specific concepts"""
        # Skip if same concept
        if concept_a['id'] == concept_b['id']:
            return None
        
        # Calculate relationship metrics
        co_occurrence = self._calculate_co_occurrence(concept_a, concept_b, file_concepts)
        semantic_similarity = self._calculate_semantic_similarity(concept_a, concept_b)
        contextual_affinity = self._calculate_contextual_affinity(concept_a, concept_b)
        
        # Skip if below thresholds
        if (co_occurrence < self.relationship_thresholds['co_occurrence'] and
            semantic_similarity < self.relationship_thresholds['semantic_similarity'] and
            contextual_affinity < self.relationship_thresholds['contextual_affinity']):
            return None
        
        # Determine relationship type
        relationship_type = self._determine_relationship_type(concept_a, concept_b, semantic_similarity, contextual_affinity)
        
        # Calculate overall strength
        strength = self._calculate_relationship_strength(co_occurrence, semantic_similarity, contextual_affinity)
        
        # Calculate confidence
        confidence = self._calculate_relationship_confidence(concept_a, concept_b, co_occurrence, semantic_similarity)
        
        # Collect evidence
        evidence = self._collect_relationship_evidence(concept_a, concept_b, co_occurrence, semantic_similarity, contextual_affinity)
        
        # Calculate network benefit
        network_benefit = self._calculate_relationship_network_benefit(concept_a, concept_b, strength)
        
        return ConceptRelationship(
            source_concept=concept_a['id'],
            target_concept=concept_b['id'],
            relationship_type=relationship_type,
            strength=strength,
            confidence=confidence,
            evidence=evidence,
            co_occurrence_frequency=co_occurrence,
            semantic_similarity=semantic_similarity,
            contextual_affinity=contextual_affinity,
            network_benefit=network_benefit
        )
    
    def _calculate_co_occurrence(self, concept_a: Dict[str, Any], concept_b: Dict[str, Any], 
                               file_concepts: Dict[str, List[Dict]]) -> int:
        """Calculate co-occurrence frequency of two concepts"""
        co_occurrence_count = 0
        
        # Count files where both concepts appear
        for file_path, file_concept_list in file_concepts.items():
            file_concept_ids = {c['id'] for c in file_concept_list}
            if concept_a['id'] in file_concept_ids and concept_b['id'] in file_concept_ids:
                co_occurrence_count += 1
        
        return co_occurrence_count
    
    def _calculate_semantic_similarity(self, concept_a: Dict[str, Any], concept_b: Dict[str, Any]) -> float:
        """Calculate semantic similarity between concepts"""
        # Compare semantic features
        features_a = concept_a.get('semantic_features', set())
        features_b = concept_b.get('semantic_features', set())
        
        if not features_a and not features_b:
            return 0.0
        
        common_features = features_a.intersection(features_b)
        total_features = features_a.union(features_b)
        
        jaccard_similarity = len(common_features) / len(total_features) if total_features else 0.0
        
        # Compare context domains
        domains_a = concept_a.get('context_domains', set())
        domains_b = concept_b.get('context_domains', set())
        
        common_domains = domains_a.intersection(domains_b)
        domain_similarity = len(common_domains) / 3.0  # Normalize to max 3 common domains
        
        # Compare concept types
        type_similarity = 1.0 if concept_a['type'] == concept_b['type'] else 0.3
        
        # Weighted combination
        semantic_similarity = (
            jaccard_similarity * 0.5 +
            min(domain_similarity, 1.0) * 0.3 +
            type_similarity * 0.2
        )
        
        return semantic_similarity
    
    def _calculate_contextual_affinity(self, concept_a: Dict[str, Any], concept_b: Dict[str, Any]) -> float:
        """Calculate contextual affinity between concepts"""
        context_a = concept_a.get('context', '').lower()
        context_b = concept_b.get('context', '').lower()
        
        if not context_a or not context_b:
            return 0.0
        
        # Extract words from contexts
        words_a = set(re.findall(r'\b\w+\b', context_a))
        words_b = set(re.findall(r'\b\w+\b', context_b))
        
        # Calculate word overlap
        common_words = words_a.intersection(words_b)
        total_words = words_a.union(words_b)
        
        word_overlap = len(common_words) / len(total_words) if total_words else 0.0
        
        # Calculate contextual pattern similarity
        pattern_similarity = self._calculate_pattern_similarity(context_a, context_b)
        
        # Combine metrics
        contextual_affinity = word_overlap * 0.7 + pattern_similarity * 0.3
        
        return contextual_affinity
    
    def _calculate_pattern_similarity(self, context_a: str, context_b: str) -> float:
        """Calculate pattern similarity between contexts"""
        # Look for similar patterns (simplified implementation)
        patterns = [
            r'\b(implement|execution|perform)\b',
            r'\b(validat|verif|test)\b',
            r'\b(optim|improv|enhanc)\b',
            r'\b(automat|intelligen|smart)\b',
            r'\b(document|record|track)\b',
            r'\b(connect|link|integrat)\b'
        ]
        
        pattern_scores = []
        for pattern in patterns:
            score_a = 1.0 if re.search(pattern, context_a) else 0.0
            score_b = 1.0 if re.search(pattern, context_b) else 0.0
            
            if score_a == score_b:  # Both have or both don't have pattern
                pattern_scores.append(1.0 if score_a == 1.0 else 0.5)
            else:
                pattern_scores.append(0.0)
        
        return sum(pattern_scores) / len(pattern_scores) if pattern_scores else 0.0
    
    def _determine_relationship_type(self, concept_a: Dict[str, Any], concept_b: Dict[str, Any], 
                                   semantic_similarity: float, contextual_affinity: float) -> str:
        """Determine the type of relationship between concepts"""
        # Hierarchical relationships
        if concept_a['type'] == 'principle' and concept_b['type'] in ['protocol', 'framework']:
            return 'implements'
        elif concept_a['type'] == 'framework' and concept_b['type'] == 'protocol':
            return 'contains'
        elif concept_a['type'] == 'system' and concept_b['type'] in ['command', 'protocol']:
            return 'includes'
        
        # Semantic relationships
        if semantic_similarity > 0.8:
            return 'similar_to'
        elif semantic_similarity > 0.6:
            return 'related_to'
        
        # Contextual relationships
        if contextual_affinity > 0.7:
            return 'co_occurs_with'
        elif contextual_affinity > 0.5:
            return 'appears_with'
        
        # Default
        return 'associated_with'
    
    def _calculate_relationship_strength(self, co_occurrence: int, semantic_similarity: float, 
                                       contextual_affinity: float) -> float:
        """Calculate overall relationship strength"""
        # Normalize co-occurrence
        co_occurrence_score = min(co_occurrence / 5.0, 1.0)  # Max 5 co-occurrences
        
        # Weighted combination
        strength = (
            co_occurrence_score * 0.4 +
            semantic_similarity * 0.35 +
            contextual_affinity * 0.25
        )
        
        return strength
    
    def _calculate_relationship_confidence(self, concept_a: Dict[str, Any], concept_b: Dict[str, Any], 
                                         co_occurrence: int, semantic_similarity: float) -> float:
        """Calculate confidence in relationship discovery"""
        confidence_factors = []
        
        # Co-occurrence confidence
        if co_occurrence >= 3:
            confidence_factors.append(0.9)
        elif co_occurrence >= 1:
            confidence_factors.append(0.6)
        else:
            confidence_factors.append(0.3)
        
        # Semantic confidence
        if semantic_similarity > 0.7:
            confidence_factors.append(0.9)
        elif semantic_similarity > 0.4:
            confidence_factors.append(0.7)
        else:
            confidence_factors.append(0.4)
        
        # Concept importance confidence
        importance_product = concept_a.get('importance_score', 0.5) * concept_b.get('importance_score', 0.5)
        importance_confidence = min(importance_product * 2, 1.0)
        confidence_factors.append(importance_confidence)
        
        return sum(confidence_factors) / len(confidence_factors)
    
    def _collect_relationship_evidence(self, concept_a: Dict[str, Any], concept_b: Dict[str, Any], 
                                     co_occurrence: int, semantic_similarity: float, 
                                     contextual_affinity: float) -> List[str]:
        """Collect evidence supporting the relationship"""
        evidence = []
        
        if co_occurrence > 0:
            evidence.append(f"Co-occurs in {co_occurrence} files")
        
        if semantic_similarity > 0.6:
            evidence.append(f"High semantic similarity ({semantic_similarity:.2f})")
        
        if contextual_affinity > 0.5:
            evidence.append(f"Similar contexts ({contextual_affinity:.2f})")
        
        # Shared features
        features_a = concept_a.get('semantic_features', set())
        features_b = concept_b.get('semantic_features', set())
        common_features = features_a.intersection(features_b)
        
        if common_features:
            evidence.append(f"Shared features: {', '.join(list(common_features)[:3])}")
        
        # Shared domains
        domains_a = concept_a.get('context_domains', set())
        domains_b = concept_b.get('context_domains', set())
        common_domains = domains_a.intersection(domains_b)
        
        if common_domains:
            evidence.append(f"Common domains: {', '.join(common_domains)}")
        
        return evidence
    
    def _calculate_relationship_network_benefit(self, concept_a: Dict[str, Any], concept_b: Dict[str, Any], 
                                              strength: float) -> float:
        """Calculate network benefit of establishing this relationship"""
        # Higher benefit for connecting important concepts
        importance_benefit = (concept_a.get('importance_score', 0.5) + concept_b.get('importance_score', 0.5)) / 2
        
        # Higher benefit for cross-domain connections
        domains_a = concept_a.get('context_domains', set())
        domains_b = concept_b.get('context_domains', set())
        cross_domain_benefit = 0.2 if domains_a and domains_b and not domains_a.intersection(domains_b) else 0.0
        
        # Strength-based benefit
        strength_benefit = strength * 0.5
        
        network_benefit = importance_benefit * 0.5 + strength_benefit + cross_domain_benefit
        
        return min(network_benefit, 1.0)
    
    def build_concept_network(self, directory: Path) -> Tuple[List[ConceptNode], List[ConceptRelationship]]:
        """Build comprehensive concept network from directory"""
        print(f"🧠 Building concept network from {directory}")
        
        all_concepts = []
        concept_dict = {}
        
        # Extract concepts from all files
        md_files = list(directory.rglob("*.md"))
        print(f"📂 Processing {len(md_files)} files...")
        
        for file_path in md_files:
            file_concepts = self.extract_concepts_from_content(file_path)
            for concept in file_concepts:
                concept_id = concept['id']
                if concept_id in concept_dict:
                    # Merge with existing concept
                    existing = concept_dict[concept_id]
                    existing['source_files'].append(concept['source_file'])
                    existing['importance_score'] = max(existing['importance_score'], concept['importance_score'])
                else:
                    # New concept
                    concept_node = ConceptNode(
                        concept_id=concept_id,
                        concept_name=concept['name'],
                        concept_type=concept['type'],
                        source_files=[concept['source_file']],
                        semantic_features=concept.get('semantic_features', set()),
                        context_domains=concept.get('context_domains', set()),
                        importance_score=concept['importance_score'],
                        centrality_metrics={}
                    )
                    concept_dict[concept_id] = concept_node
                    all_concepts.append(concept)
        
        concept_nodes = list(concept_dict.values())
        print(f"🔍 Extracted {len(concept_nodes)} unique concepts")
        
        # Discover relationships
        print("🔗 Discovering concept relationships...")
        relationships = self.discover_concept_relationships(all_concepts)
        print(f"🌐 Found {len(relationships)} relationships")
        
        # Build network graph
        self._build_network_graph(concept_nodes, relationships)
        
        # Calculate centrality metrics
        self._calculate_centrality_metrics(concept_nodes)
        
        return concept_nodes, relationships
    
    def _build_network_graph(self, concept_nodes: List[ConceptNode], relationships: List[ConceptRelationship]):
        """Build NetworkX graph from concepts and relationships"""
        self.concept_graph.clear()
        
        # Add nodes
        for concept in concept_nodes:
            self.concept_graph.add_node(
                concept.concept_id,
                name=concept.concept_name,
                type=concept.concept_type,
                importance=concept.importance_score
            )
        
        # Add edges
        for relationship in relationships:
            if relationship.strength > 0.3:  # Only add significant relationships
                self.concept_graph.add_edge(
                    relationship.source_concept,
                    relationship.target_concept,
                    weight=relationship.strength,
                    type=relationship.relationship_type,
                    confidence=relationship.confidence
                )
    
    def _calculate_centrality_metrics(self, concept_nodes: List[ConceptNode]):
        """Calculate network centrality metrics for concepts"""
        if not self.concept_graph.nodes():
            return
        
        # Calculate various centrality measures
        degree_centrality = nx.degree_centrality(self.concept_graph)
        betweenness_centrality = nx.betweenness_centrality(self.concept_graph)
        closeness_centrality = nx.closeness_centrality(self.concept_graph)
        eigenvector_centrality = nx.eigenvector_centrality(self.concept_graph, max_iter=1000)
        
        # Update concept nodes with centrality metrics
        for concept in concept_nodes:
            concept_id = concept.concept_id
            concept.centrality_metrics = {
                'degree': degree_centrality.get(concept_id, 0.0),
                'betweenness': betweenness_centrality.get(concept_id, 0.0),
                'closeness': closeness_centrality.get(concept_id, 0.0),
                'eigenvector': eigenvector_centrality.get(concept_id, 0.0)
            }
    
    def discover_concept_clusters(self, concept_nodes: List[ConceptNode], 
                                relationships: List[ConceptRelationship]) -> List[ConceptCluster]:
        """Discover clusters of related concepts"""
        print("🔍 Discovering concept clusters...")
        
        # Use community detection algorithms
        clusters = []
        
        if not self.concept_graph.nodes():
            return clusters
        
        # Detect communities using modularity
        communities = nx.community.greedy_modularity_communities(self.concept_graph)
        
        for i, community in enumerate(communities):
            if len(community) >= self.clustering_config['min_cluster_size']:
                cluster_concepts = list(community)
                
                # Calculate cluster cohesion
                cohesion_score = self._calculate_cluster_cohesion(cluster_concepts, relationships)
                
                if cohesion_score >= self.clustering_config['cohesion_threshold']:
                    # Determine cluster type and name
                    cluster_type, cluster_name = self._analyze_cluster_characteristics(cluster_concepts, concept_nodes)
                    
                    # Find representative concepts
                    representative_concepts = self._find_representative_concepts(cluster_concepts, concept_nodes)
                    
                    # Analyze cross-cluster connections
                    cross_connections = self._analyze_cross_cluster_connections(cluster_concepts, communities, relationships)
                    
                    cluster = ConceptCluster(
                        cluster_id=f"cluster_{i+1:02d}",
                        cluster_name=cluster_name,
                        concepts=cluster_concepts,
                        cohesion_score=cohesion_score,
                        cluster_type=cluster_type,
                        representative_concepts=representative_concepts,
                        cross_cluster_connections=cross_connections
                    )
                    
                    clusters.append(cluster)
        
        return clusters
    
    def _calculate_cluster_cohesion(self, cluster_concepts: List[str], 
                                  relationships: List[ConceptRelationship]) -> float:
        """Calculate cohesion score for a concept cluster"""
        if len(cluster_concepts) < 2:
            return 0.0
        
        # Count internal relationships
        internal_relationships = 0
        total_strength = 0.0
        
        concept_set = set(cluster_concepts)
        for relationship in relationships:
            if relationship.source_concept in concept_set and relationship.target_concept in concept_set:
                internal_relationships += 1
                total_strength += relationship.strength
        
        # Calculate possible internal relationships
        possible_relationships = len(cluster_concepts) * (len(cluster_concepts) - 1) / 2
        
        if possible_relationships == 0:
            return 0.0
        
        # Cohesion = relationship density * average strength
        relationship_density = internal_relationships / possible_relationships
        average_strength = total_strength / internal_relationships if internal_relationships > 0 else 0.0
        
        cohesion_score = relationship_density * average_strength
        return cohesion_score
    
    def _analyze_cluster_characteristics(self, cluster_concepts: List[str], 
                                       concept_nodes: List[ConceptNode]) -> Tuple[str, str]:
        """Analyze cluster characteristics to determine type and name"""
        concept_dict = {node.concept_id: node for node in concept_nodes}
        
        # Analyze concept types in cluster
        type_counts = Counter()
        domain_counts = Counter()
        
        for concept_id in cluster_concepts:
            if concept_id in concept_dict:
                concept = concept_dict[concept_id]
                type_counts[concept.concept_type] += 1
                for domain in concept.context_domains:
                    domain_counts[domain] += 1
        
        # Determine cluster type
        most_common_type = type_counts.most_common(1)[0][0] if type_counts else 'mixed'
        
        # Determine cluster name
        if domain_counts:
            primary_domain = domain_counts.most_common(1)[0][0]
            cluster_name = f"{primary_domain.title()} Concepts"
        else:
            cluster_name = f"{most_common_type.title()} Cluster"
        
        return most_common_type, cluster_name
    
    def _find_representative_concepts(self, cluster_concepts: List[str], 
                                    concept_nodes: List[ConceptNode]) -> List[str]:
        """Find most representative concepts in cluster"""
        concept_dict = {node.concept_id: node for node in concept_nodes}
        
        # Score concepts by importance and centrality
        concept_scores = []
        for concept_id in cluster_concepts:
            if concept_id in concept_dict:
                concept = concept_dict[concept_id]
                
                # Combined score
                score = (
                    concept.importance_score * 0.4 +
                    concept.centrality_metrics.get('degree', 0.0) * 0.3 +
                    concept.centrality_metrics.get('betweenness', 0.0) * 0.3
                )
                
                concept_scores.append((concept_id, score))
        
        # Sort by score and return top 3
        concept_scores.sort(key=lambda x: x[1], reverse=True)
        return [concept_id for concept_id, _ in concept_scores[:3]]
    
    def _analyze_cross_cluster_connections(self, cluster_concepts: List[str], 
                                         all_communities: List[Set[str]], 
                                         relationships: List[ConceptRelationship]) -> Dict[str, int]:
        """Analyze connections between this cluster and other clusters"""
        cluster_set = set(cluster_concepts)
        cross_connections = defaultdict(int)
        
        # Find which community each concept belongs to
        concept_to_community = {}
        for i, community in enumerate(all_communities):
            for concept in community:
                concept_to_community[concept] = i
        
        # Count cross-cluster relationships
        for relationship in relationships:
            source_cluster = concept_to_community.get(relationship.source_concept)
            target_cluster = concept_to_community.get(relationship.target_concept)
            
            if (relationship.source_concept in cluster_set and 
                relationship.target_concept not in cluster_set and 
                target_cluster is not None):
                cross_connections[f"cluster_{target_cluster+1:02d}"] += 1
            elif (relationship.target_concept in cluster_set and 
                  relationship.source_concept not in cluster_set and 
                  source_cluster is not None):
                cross_connections[f"cluster_{source_cluster+1:02d}"] += 1
        
        return dict(cross_connections)
    
    def generate_network_insights(self, concept_nodes: List[ConceptNode], 
                                relationships: List[ConceptRelationship], 
                                clusters: List[ConceptCluster]) -> List[NetworkInsight]:
        """Generate intelligent insights about the concept network"""
        insights = []
        
        # Analyze network structure
        structural_insights = self._analyze_network_structure(concept_nodes, relationships)
        insights.extend(structural_insights)
        
        # Analyze concept importance
        importance_insights = self._analyze_concept_importance(concept_nodes)
        insights.extend(importance_insights)
        
        # Analyze cluster patterns
        cluster_insights = self._analyze_cluster_patterns(clusters)
        insights.extend(cluster_insights)
        
        # Analyze relationship patterns
        relationship_insights = self._analyze_relationship_patterns(relationships)
        insights.extend(relationship_insights)
        
        # Sort by impact potential
        insights.sort(key=lambda x: x.impact_potential, reverse=True)
        
        return insights
    
    def _analyze_network_structure(self, concept_nodes: List[ConceptNode], 
                                 relationships: List[ConceptRelationship]) -> List[NetworkInsight]:
        """Analyze network structural insights"""
        insights = []
        
        if not self.concept_graph.nodes():
            return insights
        
        # Network density analysis
        density = nx.density(self.concept_graph)
        if density < 0.1:
            insights.append(NetworkInsight(
                insight_type='network_structure',
                insight_level='HIGH',
                description=f"Network density is low ({density:.3f}) - opportunities for more connections",
                affected_concepts=[],
                evidence=[f"Current density: {density:.3f}", "Sparse network detected"],
                actionable_recommendations=[
                    "Identify potential concept connections",
                    "Review related concepts for missing relationships",
                    "Enhance cross-domain linking"
                ],
                confidence=0.8,
                impact_potential=0.7
            ))
        
        # Isolated concepts analysis
        isolated_concepts = [node for node in concept_nodes 
                           if self.concept_graph.degree(node.concept_id) == 0]
        
        if isolated_concepts:
            insights.append(NetworkInsight(
                insight_type='isolated_concepts',
                insight_level='MEDIUM',
                description=f"Found {len(isolated_concepts)} isolated concepts with no connections",
                affected_concepts=[c.concept_id for c in isolated_concepts],
                evidence=[f"{len(isolated_concepts)} concepts have no relationships"],
                actionable_recommendations=[
                    "Review isolated concepts for potential connections",
                    "Integrate concepts into relevant clusters",
                    "Enhance concept context analysis"
                ],
                confidence=0.9,
                impact_potential=0.6
            ))
        
        return insights
    
    def _analyze_concept_importance(self, concept_nodes: List[ConceptNode]) -> List[NetworkInsight]:
        """Analyze concept importance insights"""
        insights = []
        
        # Find highly important but poorly connected concepts
        importance_threshold = 0.7
        connection_threshold = 3
        
        underconnected_important = []
        for concept in concept_nodes:
            if (concept.importance_score > importance_threshold and 
                self.concept_graph.degree(concept.concept_id) < connection_threshold):
                underconnected_important.append(concept)
        
        if underconnected_important:
            insights.append(NetworkInsight(
                insight_type='underconnected_important',
                insight_level='HIGH',
                description=f"Found {len(underconnected_important)} important concepts that are underconnected",
                affected_concepts=[c.concept_id for c in underconnected_important],
                evidence=[f"High importance (>{importance_threshold}) but <{connection_threshold} connections"],
                actionable_recommendations=[
                    "Increase connectivity for important concepts",
                    "Review concept relationships for enhancement opportunities",
                    "Create strategic cross-references"
                ],
                confidence=0.8,
                impact_potential=0.8
            ))
        
        return insights
    
    def _analyze_cluster_patterns(self, clusters: List[ConceptCluster]) -> List[NetworkInsight]:
        """Analyze cluster pattern insights"""
        insights = []
        
        # Analyze cluster sizes
        cluster_sizes = [len(cluster.concepts) for cluster in clusters]
        if cluster_sizes:
            avg_size = sum(cluster_sizes) / len(cluster_sizes)
            large_clusters = [c for c in clusters if len(c.concepts) > avg_size * 1.5]
            
            if large_clusters:
                insights.append(NetworkInsight(
                    insight_type='large_clusters',
                    insight_level='MEDIUM',
                    description=f"Found {len(large_clusters)} clusters that may be too large",
                    affected_concepts=[],
                    evidence=[f"Clusters with >{avg_size*1.5:.1f} concepts detected"],
                    actionable_recommendations=[
                        "Consider splitting large clusters",
                        "Analyze cluster subcategories",
                        "Improve cluster organization"
                    ],
                    confidence=0.7,
                    impact_potential=0.5
                ))
        
        return insights
    
    def _analyze_relationship_patterns(self, relationships: List[ConceptRelationship]) -> List[NetworkInsight]:
        """Analyze relationship pattern insights"""
        insights = []
        
        # Analyze relationship types
        type_counts = Counter(r.relationship_type for r in relationships)
        
        if 'implements' in type_counts and type_counts['implements'] > len(relationships) * 0.3:
            insights.append(NetworkInsight(
                insight_type='implementation_heavy',
                insight_level='LOW',
                description="Network shows strong implementation relationships",
                affected_concepts=[],
                evidence=[f"High proportion of 'implements' relationships ({type_counts['implements']})"],
                actionable_recommendations=[
                    "Maintain implementation relationship quality",
                    "Ensure balanced relationship types",
                    "Document implementation hierarchies"
                ],
                confidence=0.6,
                impact_potential=0.4
            ))
        
        return insights
    
    def generate_comprehensive_report(self, directory: Path) -> str:
        """Generate comprehensive concept relationship mapping report"""
        # Build concept network
        concept_nodes, relationships = self.build_concept_network(directory)
        
        # Discover clusters
        clusters = self.discover_concept_clusters(concept_nodes, relationships)
        
        # Generate insights
        insights = self.generate_network_insights(concept_nodes, relationships, clusters)
        
        # Build report
        report = []
        report.append("# 🧠 Intelligent Concept Relationship Mapping Report")
        report.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Scope**: {directory}")
        report.append("")
        
        # Network overview
        report.append("## 🌐 Network Overview")
        report.append("")
        report.append(f"- **Total Concepts**: {len(concept_nodes)}")
        report.append(f"- **Total Relationships**: {len(relationships)}")
        report.append(f"- **Concept Clusters**: {len(clusters)}")
        report.append(f"- **Network Density**: {nx.density(self.concept_graph):.3f}")
        report.append("")
        
        # Top concepts by importance
        top_concepts = sorted(concept_nodes, key=lambda x: x.importance_score, reverse=True)[:10]
        if top_concepts:
            report.append("## ⭐ Most Important Concepts")
            report.append("")
            for concept in top_concepts:
                connections = self.concept_graph.degree(concept.concept_id) if self.concept_graph.has_node(concept.concept_id) else 0
                report.append(f"- **{concept.concept_name}** ({concept.concept_type})")
                report.append(f"  - Importance: {concept.importance_score:.2f}")
                report.append(f"  - Connections: {connections}")
                report.append(f"  - Domains: {', '.join(concept.context_domains) if concept.context_domains else 'None'}")
                report.append("")
        
        # Strongest relationships
        strong_relationships = sorted(relationships, key=lambda x: x.strength, reverse=True)[:10]
        if strong_relationships:
            report.append("## 🔗 Strongest Concept Relationships")
            report.append("")
            concept_dict = {c.concept_id: c for c in concept_nodes}
            for rel in strong_relationships:
                source_name = concept_dict.get(rel.source_concept, {}).concept_name or rel.source_concept
                target_name = concept_dict.get(rel.target_concept, {}).concept_name or rel.target_concept
                report.append(f"**{source_name}** → **{target_name}**")
                report.append(f"- Type: {rel.relationship_type}")
                report.append(f"- Strength: {rel.strength:.2f}")
                report.append(f"- Confidence: {rel.confidence:.2f}")
                if rel.evidence:
                    report.append(f"- Evidence: {rel.evidence[0]}")
                report.append("")
        
        # Concept clusters
        if clusters:
            report.append("## 🔍 Concept Clusters")
            report.append("")
            for cluster in clusters:
                report.append(f"### {cluster.cluster_name}")
                report.append(f"- **Size**: {len(cluster.concepts)} concepts")
                report.append(f"- **Cohesion**: {cluster.cohesion_score:.2f}")
                report.append(f"- **Type**: {cluster.cluster_type}")
                
                if cluster.representative_concepts:
                    rep_names = []
                    concept_dict = {c.concept_id: c for c in concept_nodes}
                    for concept_id in cluster.representative_concepts:
                        if concept_id in concept_dict:
                            rep_names.append(concept_dict[concept_id].concept_name)
                    if rep_names:
                        report.append(f"- **Key Concepts**: {', '.join(rep_names[:3])}")
                
                report.append("")
        
        # Network insights
        if insights:
            report.append("## 💡 Network Insights")
            report.append("")
            
            high_impact = [i for i in insights if i.impact_potential > 0.6]
            if high_impact:
                report.append("### High Impact Opportunities")
                report.append("")
                for insight in high_impact[:5]:
                    report.append(f"**{insight.description}**")
                    report.append(f"- Level: {insight.insight_level}")
                    report.append(f"- Impact Potential: {insight.impact_potential:.1%}")
                    report.append(f"- Confidence: {insight.confidence:.1%}")
                    if insight.actionable_recommendations:
                        report.append(f"- Recommendation: {insight.actionable_recommendations[0]}")
                    report.append("")
        
        return "\n".join(report)


def main():
    """Main execution function"""
    mapper = ConceptRelationshipMapper()
    
    print("🧠 Starting Intelligent Concept Relationship Mapping...")
    
    # Analyze knowledge directory
    knowledge_dir = Path("/Users/nalve/claude-context-engineering/knowledge")
    if not knowledge_dir.exists():
        print(f"❌ Knowledge directory not found: {knowledge_dir}")
        return 1
    
    # Generate comprehensive report
    print("📊 Generating concept relationship mapping report...")
    report = mapper.generate_comprehensive_report(knowledge_dir)
    
    # Save report
    report_path = Path("operations/reports/current/concept-relationship-mapping.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    
    print(f"✅ Concept relationship mapping complete!")
    print(f"📋 Report saved to: {report_path}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())