#!/usr/bin/env python3
"""
Cross-Reference Intelligence Network Analyzer
Advanced Analytics for Principle Network Optimization

This module provides sophisticated algorithms for analyzing and optimizing
the Context Engineering principle cross-reference network with mathematical
precision and automated intelligence.
"""

import json
import re
import math
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set, Any
from collections import defaultdict, Counter
import networkx as nx
from datetime import datetime
from dataclasses import dataclass

@dataclass
class NetworkMetrics:
    """Network topology and quality metrics"""
    density: float
    avg_path_length: float
    clustering_coefficient: float
    diameter: int
    centrality_stats: Dict[str, float]
    connection_quality: float
    redundancy_index: float

@dataclass
class ConnectionOpportunity:
    """Potential new connection discovery"""
    principle_a: str
    principle_b: str
    confidence: float
    semantic_score: float
    functional_overlap: float
    potential_benefit: float
    connection_type: str

class NetworkIntelligenceAnalyzer:
    """Advanced network analysis and optimization engine"""
    
    def __init__(self, knowledge_path: str = None):
        self.knowledge_path = Path(knowledge_path or "/Users/nalve/claude-context-engineering/knowledge")
        self.principles_path = self.knowledge_path / "principles"
        self.graph = nx.Graph()
        self.principles = {}
        self.connections = defaultdict(list)
        self.semantic_cache = {}
        
        # Analysis thresholds
        self.connection_thresholds = {
            'semantic_similarity': 0.75,
            'functional_overlap': 0.60,
            'conceptual_distance': 0.80,
            'benefit_threshold': 0.70
        }
        
        # Network quality standards
        self.quality_targets = {
            'min_density': 0.85,
            'max_path_length': 3.0,
            'min_clustering': 0.70,
            'max_diameter': 6,
            'min_connection_quality': 0.90
        }
    
    def load_principle_network(self) -> bool:
        """Load and parse the complete principle network"""
        try:
            # Load principle cross-reference network
            network_file = self.principles_path / "principle-cross-reference-network.md"
            if not network_file.exists():
                print(f"❌ Network file not found: {network_file}")
                return False
            
            content = network_file.read_text()
            self._parse_network_structure(content)
            self._build_graph()
            
            print(f"✅ Loaded {len(self.principles)} principles with {len(self.connections)} connection sets")
            return True
            
        except Exception as e:
            print(f"❌ Error loading principle network: {e}")
            return False
    
    def _parse_network_structure(self, content: str):
        """Parse principle definitions and connections from network file"""
        # Extract principle information
        principle_pattern = r'\*\*#(\d+)\s+([^*]+)\*\*[^:]*:\s*([^-\n]+)'
        for match in re.finditer(principle_pattern, content):
            principle_id = f"#{match.group(1)}"
            principle_name = match.group(2).strip()
            principle_desc = match.group(3).strip()
            
            self.principles[principle_id] = {
                'name': principle_name,
                'description': principle_desc,
                'connections': [],
                'categories': []
            }
        
        # Extract connections from network sections
        connection_pattern = r'- \*\*#(\d+)[^*]*\*\*[^(]*\(([^)]+)\)'
        current_principle = None
        
        for line in content.split('\n'):
            # Identify current principle context
            principle_match = re.search(r'\*\*#(\d+)', line)
            if principle_match:
                current_principle = f"#{principle_match.group(1)}"
            
            # Extract connections
            if current_principle and '- **#' in line:
                connection_match = re.search(connection_pattern, line)
                if connection_match:
                    target_principle = f"#{connection_match.group(1)}"
                    connection_type = connection_match.group(2).strip()
                    
                    if current_principle in self.principles:
                        self.connections[current_principle].append({
                            'target': target_principle,
                            'type': connection_type,
                            'weight': self._calculate_connection_weight(connection_type)
                        })
    
    def _calculate_connection_weight(self, connection_type: str) -> float:
        """Calculate connection weight based on relationship type"""
        type_weights = {
            'Implementation': 0.9,
            'Foundation': 0.95,
            'Specialization': 0.8,
            'Enhancement': 0.7,
            'Synergy': 0.75,
            'Strategy': 0.85,
            'Orchestration': 0.8,
            'Integration': 0.7,
            'Optimization': 0.65
        }
        
        for weight_type, weight in type_weights.items():
            if weight_type.lower() in connection_type.lower():
                return weight
        
        return 0.6  # Default weight
    
    def _build_graph(self):
        """Build NetworkX graph from principle connections"""
        # Add nodes
        for principle_id, data in self.principles.items():
            self.graph.add_node(principle_id, **data)
        
        # Add edges
        for source, connections in self.connections.items():
            for conn in connections:
                if conn['target'] in self.principles:
                    self.graph.add_edge(
                        source, 
                        conn['target'], 
                        weight=conn['weight'],
                        connection_type=conn['type']
                    )
    
    def analyze_network_metrics(self) -> NetworkMetrics:
        """Comprehensive network topology analysis"""
        if not self.graph.nodes():
            raise ValueError("Network graph not loaded")
        
        # Basic topology metrics
        density = nx.density(self.graph)
        
        # Path analysis (for connected components)
        if nx.is_connected(self.graph):
            avg_path_length = nx.average_shortest_path_length(self.graph)
            diameter = nx.diameter(self.graph)
        else:
            # Calculate for largest connected component
            largest_cc = max(nx.connected_components(self.graph), key=len)
            subgraph = self.graph.subgraph(largest_cc)
            avg_path_length = nx.average_shortest_path_length(subgraph)
            diameter = nx.diameter(subgraph)
        
        # Clustering coefficient
        clustering_coefficient = nx.average_clustering(self.graph)
        
        # Centrality analysis
        centrality_stats = self._analyze_centrality()
        
        # Connection quality assessment
        connection_quality = self._assess_connection_quality()
        
        # Redundancy analysis
        redundancy_index = self._calculate_redundancy_index()
        
        return NetworkMetrics(
            density=density,
            avg_path_length=avg_path_length,
            clustering_coefficient=clustering_coefficient,
            diameter=diameter,
            centrality_stats=centrality_stats,
            connection_quality=connection_quality,
            redundancy_index=redundancy_index
        )
    
    def _analyze_centrality(self) -> Dict[str, float]:
        """Analyze node centrality metrics"""
        degree_centrality = nx.degree_centrality(self.graph)
        betweenness_centrality = nx.betweenness_centrality(self.graph)
        closeness_centrality = nx.closeness_centrality(self.graph)
        
        # Identify key principles
        top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
        top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            'avg_degree_centrality': sum(degree_centrality.values()) / len(degree_centrality),
            'avg_betweenness_centrality': sum(betweenness_centrality.values()) / len(betweenness_centrality),
            'avg_closeness_centrality': sum(closeness_centrality.values()) / len(closeness_centrality),
            'top_degree_principles': [p[0] for p in top_degree],
            'top_bridge_principles': [p[0] for p in top_betweenness],
            'network_centralization': max(degree_centrality.values()) - min(degree_centrality.values())
        }
    
    def _assess_connection_quality(self) -> float:
        """Assess overall quality of network connections"""
        quality_scores = []
        
        for edge in self.graph.edges(data=True):
            source, target, data = edge
            
            # Weight-based quality
            weight_quality = data.get('weight', 0.5)
            
            # Semantic quality (placeholder - would use NLP in full implementation)
            semantic_quality = self._estimate_semantic_quality(source, target)
            
            # Structural quality (avoiding over-connection)
            degree_source = self.graph.degree(source)
            degree_target = self.graph.degree(target)
            structural_quality = 1.0 - min(degree_source, degree_target) / 20.0  # Normalize
            
            overall_quality = (weight_quality * 0.5 + semantic_quality * 0.3 + structural_quality * 0.2)
            quality_scores.append(overall_quality)
        
        return sum(quality_scores) / len(quality_scores) if quality_scores else 0.0
    
    def _estimate_semantic_quality(self, principle_a: str, principle_b: str) -> float:
        """Estimate semantic relationship quality between principles"""
        # Simplified semantic analysis based on principle names and descriptions
        if principle_a not in self.principles or principle_b not in self.principles:
            return 0.5
        
        name_a = self.principles[principle_a]['name'].lower()
        name_b = self.principles[principle_b]['name'].lower()
        desc_a = self.principles[principle_a]['description'].lower()
        desc_b = self.principles[principle_b]['description'].lower()
        
        # Common word analysis
        words_a = set(name_a.split() + desc_a.split())
        words_b = set(name_b.split() + desc_b.split())
        common_words = words_a.intersection(words_b)
        
        # Conceptual overlap
        conceptual_keywords = {
            'mathematical', 'validation', 'orchestration', 'intelligence', 'automation',
            'documentation', 'execution', 'optimization', 'integration', 'framework'
        }
        
        conceptual_overlap = len(words_a.intersection(conceptual_keywords)) + \
                           len(words_b.intersection(conceptual_keywords))
        
        # Calculate semantic score
        semantic_score = (len(common_words) * 0.6 + conceptual_overlap * 0.4) / 10.0
        return min(semantic_score, 1.0)
    
    def _calculate_redundancy_index(self) -> float:
        """Calculate network redundancy to identify over-connection"""
        total_possible_connections = len(self.principles) * (len(self.principles) - 1) / 2
        actual_connections = self.graph.number_of_edges()
        
        # Calculate redundancy based on clustering patterns
        triangles = sum(nx.triangles(self.graph).values()) / 3
        potential_triangles = sum(nx.triangles(nx.complete_graph(len(self.principles))).values()) / 3
        
        redundancy_ratio = triangles / potential_triangles if potential_triangles > 0 else 0
        connection_ratio = actual_connections / total_possible_connections
        
        return (redundancy_ratio * 0.7 + connection_ratio * 0.3)
    
    def discover_connection_opportunities(self) -> List[ConnectionOpportunity]:
        """Discover potential new valuable connections using AI algorithms"""
        opportunities = []
        
        # Analyze all principle pairs without direct connections
        for principle_a in self.principles:
            for principle_b in self.principles:
                if principle_a >= principle_b:  # Avoid duplicates
                    continue
                
                if not self.graph.has_edge(principle_a, principle_b):
                    opportunity = self._analyze_connection_potential(principle_a, principle_b)
                    if opportunity.confidence > self.connection_thresholds['benefit_threshold']:
                        opportunities.append(opportunity)
        
        # Sort by potential benefit
        opportunities.sort(key=lambda x: x.potential_benefit, reverse=True)
        return opportunities[:20]  # Top 20 opportunities
    
    def _analyze_connection_potential(self, principle_a: str, principle_b: str) -> ConnectionOpportunity:
        """Analyze potential benefit of connecting two principles"""
        # Semantic similarity analysis
        semantic_score = self._estimate_semantic_quality(principle_a, principle_b)
        
        # Functional overlap analysis
        functional_overlap = self._calculate_functional_overlap(principle_a, principle_b)
        
        # Network benefit analysis
        network_benefit = self._calculate_network_benefit(principle_a, principle_b)
        
        # Determine connection type
        connection_type = self._suggest_connection_type(principle_a, principle_b, semantic_score, functional_overlap)
        
        # Calculate overall confidence
        confidence = (semantic_score * 0.4 + functional_overlap * 0.3 + network_benefit * 0.3)
        
        # Calculate potential benefit
        potential_benefit = confidence * self._calculate_strategic_value(principle_a, principle_b)
        
        return ConnectionOpportunity(
            principle_a=principle_a,
            principle_b=principle_b,
            confidence=confidence,
            semantic_score=semantic_score,
            functional_overlap=functional_overlap,
            potential_benefit=potential_benefit,
            connection_type=connection_type
        )
    
    def _calculate_functional_overlap(self, principle_a: str, principle_b: str) -> float:
        """Calculate functional overlap between principles"""
        # Analyze shared neighbors (common connections)
        neighbors_a = set(self.graph.neighbors(principle_a))
        neighbors_b = set(self.graph.neighbors(principle_b))
        common_neighbors = neighbors_a.intersection(neighbors_b)
        
        if not neighbors_a and not neighbors_b:
            return 0.0
        
        shared_ratio = len(common_neighbors) / len(neighbors_a.union(neighbors_b))
        
        # Analyze functional keywords
        functional_keywords = {
            'execution', 'orchestration', 'validation', 'optimization',
            'intelligence', 'automation', 'documentation', 'integration'
        }
        
        words_a = set(self.principles[principle_a]['name'].lower().split())
        words_b = set(self.principles[principle_b]['name'].lower().split())
        
        functional_overlap = len(words_a.intersection(functional_keywords)) + \
                           len(words_b.intersection(functional_keywords))
        
        return min((shared_ratio * 0.7 + functional_overlap * 0.3 / 10.0), 1.0)
    
    def _calculate_network_benefit(self, principle_a: str, principle_b: str) -> float:
        """Calculate network topology benefit of new connection"""
        # Calculate current shortest path
        try:
            current_path_length = nx.shortest_path_length(self.graph, principle_a, principle_b)
        except nx.NetworkXNoPath:
            current_path_length = float('inf')
        
        # Benefit is higher for principles that would be connected by shorter paths
        if current_path_length == float('inf'):
            path_benefit = 1.0  # High benefit for connecting isolated components
        elif current_path_length > 3:
            path_benefit = 0.8  # Good benefit for reducing long paths
        elif current_path_length == 3:
            path_benefit = 0.6  # Moderate benefit
        else:
            path_benefit = 0.2  # Low benefit for already close principles
        
        # Consider centrality impact
        degree_a = self.graph.degree(principle_a)
        degree_b = self.graph.degree(principle_b)
        centrality_benefit = min(1.0, (20 - degree_a - degree_b) / 20.0)  # Prefer less connected nodes
        
        return path_benefit * 0.7 + centrality_benefit * 0.3
    
    def _suggest_connection_type(self, principle_a: str, principle_b: str, 
                                semantic_score: float, functional_overlap: float) -> str:
        """Suggest appropriate connection type based on analysis"""
        name_a = self.principles[principle_a]['name'].lower()
        name_b = self.principles[principle_b]['name'].lower()
        
        # Implementation relationships
        if 'implementation' in name_a or 'implementation' in name_b:
            return 'Implementation'
        
        # Foundation relationships
        if functional_overlap > 0.7 and semantic_score > 0.6:
            return 'Foundation'
        
        # Orchestration relationships
        if 'orchestration' in name_a or 'orchestration' in name_b:
            return 'Orchestration'
        
        # Enhancement relationships
        if semantic_score > 0.8:
            return 'Enhancement'
        
        # Synergy relationships
        if functional_overlap > 0.6:
            return 'Synergy'
        
        return 'Integration'
    
    def _calculate_strategic_value(self, principle_a: str, principle_b: str) -> float:
        """Calculate strategic value of connecting specific principles"""
        # High-value principle categories
        strategic_principles = {
            '#1', '#3', '#5', '#17', '#66', '#67',  # Core meta-principles
            '#80', '#90', '#96',  # Task intelligence
            '#87', '#91', '#92', '#93',  # Documentation
            '#105', '#106', '#107'  # Advanced frameworks
        }
        
        strategic_count = sum(1 for p in [principle_a, principle_b] if p in strategic_principles)
        base_value = 0.5 + (strategic_count * 0.25)
        
        # Bonus for cross-category connections
        categories_a = self._get_principle_categories(principle_a)
        categories_b = self._get_principle_categories(principle_b)
        
        if categories_a != categories_b:
            base_value += 0.1  # Cross-category bonus
        
        return min(base_value, 1.0)
    
    def _get_principle_categories(self, principle_id: str) -> str:
        """Determine principle category based on ID ranges"""
        try:
            num = int(principle_id[1:])
            if num <= 20:
                return 'foundational'
            elif num <= 40:
                return 'operational'
            elif num <= 60:
                return 'technical'
            elif num <= 80:
                return 'intelligent'
            else:
                return 'advanced'
        except ValueError:
            return 'unknown'
    
    def optimize_network_density(self) -> Tuple[List[ConnectionOpportunity], List[str]]:
        """Optimize network to achieve target density while maintaining quality"""
        current_metrics = self.analyze_network_metrics()
        
        new_connections = []
        removable_connections = []
        
        # If density is below target, suggest new connections
        if current_metrics.density < self.quality_targets['min_density']:
            opportunities = self.discover_connection_opportunities()
            new_connections = opportunities[:int((self.quality_targets['min_density'] - current_metrics.density) * 100)]
        
        # If redundancy is high, suggest connection removal
        if current_metrics.redundancy_index > 0.8:
            removable_connections = self._identify_redundant_connections()
        
        return new_connections, removable_connections
    
    def _identify_redundant_connections(self) -> List[str]:
        """Identify potentially redundant connections for removal"""
        redundant = []
        
        for edge in self.graph.edges(data=True):
            source, target, data = edge
            
            # Check if removal would not disconnect the graph
            self.graph.remove_edge(source, target)
            if nx.is_connected(self.graph):
                # Check if alternative paths exist
                try:
                    path_length = nx.shortest_path_length(self.graph, source, target)
                    if path_length <= 3:  # Alternative path is reasonable
                        weight = data.get('weight', 0.5)
                        if weight < 0.6:  # Low-value connection
                            redundant.append(f"{source} → {target}")
                except nx.NetworkXNoPath:
                    pass
            
            # Restore edge
            self.graph.add_edge(source, target, **data)
        
        return redundant[:5]  # Limit suggestions
    
    def generate_network_report(self) -> str:
        """Generate comprehensive network analysis report"""
        metrics = self.analyze_network_metrics()
        opportunities = self.discover_connection_opportunities()
        optimizations = self.optimize_network_density()
        
        report = []
        report.append("# 🕸️ Cross-Reference Intelligence Network Analysis Report")
        report.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Network metrics section
        report.append("## 📊 Network Topology Metrics")
        report.append("")
        report.append(f"- **Network Density**: {metrics.density:.3f} (Target: ≥{self.quality_targets['min_density']})")
        report.append(f"- **Average Path Length**: {metrics.avg_path_length:.2f} (Target: ≤{self.quality_targets['max_path_length']})")
        report.append(f"- **Clustering Coefficient**: {metrics.clustering_coefficient:.3f} (Target: ≥{self.quality_targets['min_clustering']})")
        report.append(f"- **Network Diameter**: {metrics.diameter} (Target: ≤{self.quality_targets['max_diameter']})")
        report.append(f"- **Connection Quality**: {metrics.connection_quality:.3f} (Target: ≥{self.quality_targets['min_connection_quality']})")
        report.append(f"- **Redundancy Index**: {metrics.redundancy_index:.3f}")
        report.append("")
        
        # Network health assessment
        health_score = self._calculate_network_health(metrics)
        report.append(f"**Overall Network Health**: {health_score:.1%}")
        report.append("")
        
        # Key principles section
        report.append("## 🎯 Key Network Principles")
        report.append("")
        report.append("**Most Connected Principles**:")
        for principle in metrics.centrality_stats['top_degree_principles']:
            degree = self.graph.degree(principle)
            report.append(f"- **{principle}** ({self.principles[principle]['name']}): {degree} connections")
        report.append("")
        
        report.append("**Bridge Principles** (High Betweenness Centrality):")
        for principle in metrics.centrality_stats['top_bridge_principles']:
            report.append(f"- **{principle}** ({self.principles[principle]['name']})")
        report.append("")
        
        # Optimization opportunities
        if opportunities:
            report.append("## 🚀 Connection Opportunities")
            report.append("")
            report.append("**Top Connection Recommendations**:")
            for opp in opportunities[:10]:
                report.append(f"- **{opp.principle_a}** ↔ **{opp.principle_b}**")
                report.append(f"  - Connection Type: {opp.connection_type}")
                report.append(f"  - Confidence: {opp.confidence:.1%}")
                report.append(f"  - Potential Benefit: {opp.potential_benefit:.1%}")
                report.append("")
        
        # Network optimization
        new_connections, removable = optimizations
        if new_connections or removable:
            report.append("## ⚡ Network Optimization Recommendations")
            report.append("")
            
            if new_connections:
                report.append("**Recommended New Connections**:")
                for conn in new_connections[:5]:
                    report.append(f"- {conn.principle_a} ↔ {conn.principle_b} ({conn.connection_type})")
                report.append("")
            
            if removable:
                report.append("**Potentially Redundant Connections**:")
                for conn in removable:
                    report.append(f"- {conn}")
                report.append("")
        
        return "\n".join(report)
    
    def _calculate_network_health(self, metrics: NetworkMetrics) -> float:
        """Calculate overall network health score"""
        health_factors = []
        
        # Density health
        density_health = min(metrics.density / self.quality_targets['min_density'], 1.0)
        health_factors.append(density_health * 0.25)
        
        # Path length health
        path_health = min(self.quality_targets['max_path_length'] / metrics.avg_path_length, 1.0)
        health_factors.append(path_health * 0.20)
        
        # Clustering health
        clustering_health = min(metrics.clustering_coefficient / self.quality_targets['min_clustering'], 1.0)
        health_factors.append(clustering_health * 0.15)
        
        # Connection quality health
        quality_health = min(metrics.connection_quality / self.quality_targets['min_connection_quality'], 1.0)
        health_factors.append(quality_health * 0.25)
        
        # Redundancy health (lower redundancy is better)
        redundancy_health = max(0.0, 1.0 - metrics.redundancy_index)
        health_factors.append(redundancy_health * 0.15)
        
        return sum(health_factors)


def main():
    """Main execution function"""
    analyzer = NetworkIntelligenceAnalyzer()
    
    print("🔍 Loading Cross-Reference Intelligence Network...")
    if not analyzer.load_principle_network():
        sys.exit(1)
    
    print("📊 Analyzing network metrics...")
    metrics = analyzer.analyze_network_metrics()
    
    print("🚀 Discovering connection opportunities...")
    opportunities = analyzer.discover_connection_opportunities()
    
    print("⚡ Generating optimization recommendations...")
    report = analyzer.generate_network_report()
    
    # Save report
    report_path = Path("operations/reports/current/network-intelligence-analysis.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    
    print(f"✅ Network analysis complete! Report saved to: {report_path}")
    print(f"📊 Network Health: {analyzer._calculate_network_health(metrics):.1%}")
    print(f"🔗 Connection Opportunities Found: {len(opportunities)}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())