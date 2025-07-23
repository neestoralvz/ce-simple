#!/usr/bin/env python3
"""
Cross-Reference Integrity Validator
Validates and monitors the integrity of cross-references in the Context Engineering ecosystem
Tracks 110 principles network with 0.847 density and maintains navigation accuracy
"""

import json
import os
import re
import sys
import time
import datetime
import sqlite3
import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass, asdict
from urllib.parse import urlparse
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/Users/nalve/claude-context-engineering/scripts/results/monitoring/cross-ref-validator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class CrossReference:
    """Cross-reference data structure"""
    source_file: str
    target_path: str
    link_text: str
    line_number: int
    link_type: str  # internal, external, relative, absolute
    status: str     # valid, broken, unknown, suspicious
    response_time: Optional[float] = None
    error_message: Optional[str] = None
    last_checked: Optional[str] = None

@dataclass
class ValidationReport:
    """Validation report data structure"""
    timestamp: str
    total_links: int
    valid_links: int
    broken_links: int
    suspicious_links: int
    network_density: float
    validation_coverage: float
    avg_response_time: float
    issues_found: List[str]
    recommendations: List[str]

class CrossReferenceValidator:
    """Comprehensive cross-reference integrity validation and monitoring"""
    
    def __init__(self, base_path: str = None):
        self.base_path = Path(base_path or "/Users/nalve/claude-context-engineering")
        self.db_path = self.base_path / "scripts/results/monitoring/cross_ref_validation.db"
        self.results_path = self.base_path / "scripts/results/monitoring"
        
        # Link patterns for different reference types
        self.link_patterns = {
            'markdown_link': re.compile(r'\[([^\]]+)\]\(([^)]+)\)'),
            'reference_link': re.compile(r'\[([^\]]+)\]:\s*(.+)'),
            'html_link': re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>([^<]*)</a>', re.IGNORECASE),
            'principle_ref': re.compile(r'#(\d+)[-\s]*([^#\n\]]+)'),
            'file_path': re.compile(r'`([^`]+\.(md|py|sh|json|yaml))`'),
            'wiki_link': re.compile(r'\[\[([^\]]+)\]\]')
        }
        
        # Initialize database
        self._init_database()
        
        # Known valid domains for external links
        self.trusted_domains = {
            'github.com', 'docs.github.com', 'claude.ai', 'anthropic.com',
            'stackoverflow.com', 'python.org', 'nodejs.org', 'docker.com'
        }
        
        # Cache for validation results
        self.validation_cache = {}
        self.cache_timeout = 3600  # 1 hour
        
    def _init_database(self):
        """Initialize SQLite database for cross-reference tracking"""
        os.makedirs(self.db_path.parent, exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Cross-references table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cross_references (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_file TEXT NOT NULL,
                    target_path TEXT NOT NULL,
                    link_text TEXT,
                    line_number INTEGER,
                    link_type TEXT,
                    status TEXT,
                    response_time REAL,
                    error_message TEXT,
                    last_checked TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Validation reports table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS validation_reports (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    total_links INTEGER,
                    valid_links INTEGER,
                    broken_links INTEGER,
                    suspicious_links INTEGER,
                    network_density REAL,
                    validation_coverage REAL,
                    avg_response_time REAL,
                    issues_count INTEGER,
                    recommendations_count INTEGER,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Network analysis table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS network_analysis (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    node_count INTEGER,
                    edge_count INTEGER,
                    density REAL,
                    clustering_coefficient REAL,
                    avg_path_length REAL,
                    isolated_nodes INTEGER,
                    hub_nodes TEXT,  -- JSON array
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.commit()
            logger.info("Cross-reference validation database initialized")
    
    def validate_all_references(self) -> ValidationReport:
        """Perform comprehensive validation of all cross-references"""
        logger.info("Starting comprehensive cross-reference validation")
        start_time = time.time()
        
        # Discover all cross-references
        all_references = self._discover_all_references()
        logger.info(f"Discovered {len(all_references)} cross-references")
        
        # Validate references in parallel
        validated_references = self._validate_references_parallel(all_references)
        
        # Analyze network structure
        network_metrics = self._analyze_network_structure(validated_references)
        
        # Generate validation report
        report = self._generate_validation_report(validated_references, network_metrics)
        
        # Store results
        self._store_validation_results(validated_references, report)
        
        execution_time = time.time() - start_time
        logger.info(f"Cross-reference validation completed in {execution_time:.2f}s")
        
        return report
    
    def _discover_all_references(self) -> List[CrossReference]:
        """Discover all cross-references in the codebase"""
        references = []
        
        # Search paths
        search_paths = [
            self.base_path / "docs",
            self.base_path / "scripts",
            self.base_path / "CLAUDE.md",
            self.base_path / "README.md"
        ]
        
        for search_path in search_paths:
            if search_path.is_file():
                refs = self._extract_references_from_file(search_path)
                references.extend(refs)
            elif search_path.is_dir():
                for file_path in search_path.rglob("*.md"):
                    if file_path.is_file():
                        refs = self._extract_references_from_file(file_path)
                        references.extend(refs)
        
        return references
    
    def _extract_references_from_file(self, file_path: Path) -> List[CrossReference]:
        """Extract all cross-references from a single file"""
        references = []
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
            
            # Extract different types of references
            for line_num, line in enumerate(lines, 1):
                # Markdown links
                for match in self.link_patterns['markdown_link'].finditer(line):
                    link_text, target = match.groups()
                    ref = CrossReference(
                        source_file=str(file_path.relative_to(self.base_path)),
                        target_path=target,
                        link_text=link_text,
                        line_number=line_num,
                        link_type=self._classify_link_type(target),
                        status='unknown'
                    )
                    references.append(ref)
                
                # HTML links
                for match in self.link_patterns['html_link'].finditer(line):
                    target, link_text = match.groups()
                    ref = CrossReference(
                        source_file=str(file_path.relative_to(self.base_path)),
                        target_path=target,
                        link_text=link_text,
                        line_number=line_num,
                        link_type=self._classify_link_type(target),
                        status='unknown'
                    )
                    references.append(ref)
                
                # Principle references
                for match in self.link_patterns['principle_ref'].finditer(line):
                    principle_num, principle_text = match.groups()
                    ref = CrossReference(
                        source_file=str(file_path.relative_to(self.base_path)),
                        target_path=f"#principle-{principle_num}",
                        link_text=f"Principle #{principle_num}: {principle_text.strip()}",
                        line_number=line_num,
                        link_type='principle',
                        status='unknown'
                    )
                    references.append(ref)
                
                # File path references
                for match in self.link_patterns['file_path'].finditer(line):
                    file_ref = match.group(1)
                    ref = CrossReference(
                        source_file=str(file_path.relative_to(self.base_path)),
                        target_path=file_ref,
                        link_text=file_ref,
                        line_number=line_num,
                        link_type='file_path',
                        status='unknown'
                    )
                    references.append(ref)
        
        except Exception as e:
            logger.error(f"Error extracting references from {file_path}: {e}")
        
        return references
    
    def _classify_link_type(self, target: str) -> str:
        """Classify the type of link target"""
        if target.startswith('http://') or target.startswith('https://'):
            return 'external'
        elif target.startswith('#'):
            return 'anchor'
        elif target.startswith('/'):
            return 'absolute'
        elif target.startswith('./') or target.startswith('../'):
            return 'relative'
        elif target.startswith('mailto:'):
            return 'email'
        else:
            return 'internal'
    
    def _validate_references_parallel(self, references: List[CrossReference]) -> List[CrossReference]:
        """Validate references in parallel for efficiency"""
        validated_references = []
        
        # Group references by type for optimized validation
        grouped_refs = {}
        for ref in references:
            if ref.link_type not in grouped_refs:
                grouped_refs[ref.link_type] = []
            grouped_refs[ref.link_type].append(ref)
        
        # Validate each group
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_group = {}
            
            for link_type, refs in grouped_refs.items():
                if link_type == 'external':
                    future = executor.submit(self._validate_external_links, refs)
                elif link_type in ['internal', 'relative', 'absolute']:
                    future = executor.submit(self._validate_internal_links, refs)
                elif link_type == 'principle':
                    future = executor.submit(self._validate_principle_references, refs)
                elif link_type == 'file_path':
                    future = executor.submit(self._validate_file_paths, refs)
                else:
                    future = executor.submit(self._validate_other_links, refs)
                
                future_to_group[future] = link_type
            
            # Collect results
            for future in as_completed(future_to_group):
                link_type = future_to_group[future]
                try:
                    validated_refs = future.result(timeout=60)
                    validated_references.extend(validated_refs)
                    logger.info(f"Validated {len(validated_refs)} {link_type} references")
                except Exception as e:
                    logger.error(f"Error validating {link_type} references: {e}")
        
        return validated_references
    
    def _validate_external_links(self, references: List[CrossReference]) -> List[CrossReference]:
        """Validate external HTTP/HTTPS links"""
        validated = []
        
        for ref in references:
            start_time = time.time()
            ref.last_checked = datetime.datetime.utcnow().isoformat()
            
            try:
                # Check cache first
                cache_key = f"external_{ref.target_path}"
                if cache_key in self.validation_cache:
                    cached_result = self.validation_cache[cache_key]
                    if time.time() - cached_result['timestamp'] < self.cache_timeout:
                        ref.status = cached_result['status']
                        ref.response_time = cached_result['response_time']
                        ref.error_message = cached_result.get('error_message')
                        validated.append(ref)
                        continue
                
                # Validate URL format
                parsed_url = urlparse(ref.target_path)
                if not parsed_url.scheme or not parsed_url.netloc:
                    ref.status = 'broken'
                    ref.error_message = 'Invalid URL format'
                    validated.append(ref)
                    continue
                
                # Check if domain is trusted (skip actual HTTP request for untrusted)
                domain = parsed_url.netloc.lower()
                if not any(trusted in domain for trusted in self.trusted_domains):
                    ref.status = 'suspicious'
                    ref.error_message = 'Untrusted domain - manual verification required'
                    validated.append(ref)
                    continue
                
                # Make HTTP request with timeout
                response = requests.head(
                    ref.target_path,
                    timeout=10,
                    allow_redirects=True,
                    headers={'User-Agent': 'Context-Engineering-Validator/1.0'}
                )
                
                ref.response_time = time.time() - start_time
                
                if response.status_code == 200:
                    ref.status = 'valid'
                elif response.status_code in [301, 302, 307, 308]:
                    ref.status = 'valid'
                    ref.error_message = f'Redirect: {response.status_code}'
                elif response.status_code == 404:
                    ref.status = 'broken'
                    ref.error_message = 'Page not found (404)'
                else:
                    ref.status = 'suspicious'
                    ref.error_message = f'HTTP {response.status_code}'
                
                # Cache result
                self.validation_cache[cache_key] = {
                    'status': ref.status,
                    'response_time': ref.response_time,
                    'error_message': ref.error_message,
                    'timestamp': time.time()
                }
                
            except requests.exceptions.Timeout:
                ref.status = 'suspicious'
                ref.error_message = 'Request timeout'
                ref.response_time = time.time() - start_time
            except requests.exceptions.ConnectionError:
                ref.status = 'broken'
                ref.error_message = 'Connection failed'
                ref.response_time = time.time() - start_time
            except Exception as e:
                ref.status = 'broken'
                ref.error_message = str(e)
                ref.response_time = time.time() - start_time
            
            validated.append(ref)
        
        return validated
    
    def _validate_internal_links(self, references: List[CrossReference]) -> List[CrossReference]:
        """Validate internal file and path references"""
        validated = []
        
        for ref in references:
            ref.last_checked = datetime.datetime.utcnow().isoformat()
            
            try:
                # Resolve target path relative to source file
                source_dir = (self.base_path / ref.source_file).parent
                
                if ref.link_type == 'absolute':
                    target_path = self.base_path / ref.target_path.lstrip('/')
                elif ref.link_type == 'relative':
                    target_path = source_dir / ref.target_path
                else:  # internal
                    target_path = source_dir / ref.target_path
                
                # Resolve path and check existence
                try:
                    resolved_path = target_path.resolve()
                    
                    # Check if target exists
                    if resolved_path.exists():
                        ref.status = 'valid'
                    elif '#' in ref.target_path:
                        # Handle anchor links
                        file_part = ref.target_path.split('#')[0]
                        if file_part:
                            file_target = source_dir / file_part
                            if file_target.resolve().exists():
                                ref.status = 'valid'  # Assume anchor exists
                            else:
                                ref.status = 'broken'
                                ref.error_message = 'Target file not found'
                        else:
                            ref.status = 'valid'  # Same-file anchor
                    else:
                        ref.status = 'broken'
                        ref.error_message = 'Target file not found'
                        
                except (OSError, ValueError) as e:
                    ref.status = 'broken'
                    ref.error_message = f'Path resolution error: {e}'
                    
            except Exception as e:
                ref.status = 'broken'
                ref.error_message = str(e)
            
            validated.append(ref)
        
        return validated
    
    def _validate_principle_references(self, references: List[CrossReference]) -> List[CrossReference]:
        """Validate principle number references"""
        validated = []
        
        # Load principle registry
        principle_registry = self._load_principle_registry()
        
        for ref in references:
            ref.last_checked = datetime.datetime.utcnow().isoformat()
            
            try:
                # Extract principle number
                principle_match = re.search(r'#(\d+)', ref.target_path)
                if not principle_match:
                    ref.status = 'broken'
                    ref.error_message = 'Invalid principle format'
                    validated.append(ref)
                    continue
                
                principle_num = int(principle_match.group(1))
                
                # Check if principle exists in registry
                if principle_num in principle_registry:
                    ref.status = 'valid'
                elif 1 <= principle_num <= 110:  # Known range
                    ref.status = 'suspicious'
                    ref.error_message = 'Principle not found in registry'
                else:
                    ref.status = 'broken'
                    ref.error_message = 'Principle number out of range'
                    
            except ValueError:
                ref.status = 'broken'
                ref.error_message = 'Invalid principle number'
            except Exception as e:
                ref.status = 'broken'
                ref.error_message = str(e)
            
            validated.append(ref)
        
        return validated
    
    def _validate_file_paths(self, references: List[CrossReference]) -> List[CrossReference]:
        """Validate file path references in code blocks"""
        validated = []
        
        for ref in references:
            ref.last_checked = datetime.datetime.utcnow().isoformat()
            
            try:
                # Check if file exists in project
                file_path = self.base_path / ref.target_path.lstrip('./')
                
                if file_path.exists():
                    ref.status = 'valid'
                else:
                    # Check in common locations
                    common_paths = [
                        self.base_path / "docs" / ref.target_path,
                        self.base_path / "scripts" / ref.target_path,
                    ]
                    
                    found = False
                    for common_path in common_paths:
                        if common_path.exists():
                            ref.status = 'valid'
                            found = True
                            break
                    
                    if not found:
                        ref.status = 'broken'
                        ref.error_message = 'File not found in project'
                        
            except Exception as e:
                ref.status = 'broken'
                ref.error_message = str(e)
            
            validated.append(ref)
        
        return validated
    
    def _validate_other_links(self, references: List[CrossReference]) -> List[CrossReference]:
        """Validate other types of links (email, etc.)"""
        validated = []
        
        for ref in references:
            ref.last_checked = datetime.datetime.utcnow().isoformat()
            
            if ref.link_type == 'email':
                # Basic email validation
                email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
                email = ref.target_path.replace('mailto:', '')
                if email_pattern.match(email):
                    ref.status = 'valid'
                else:
                    ref.status = 'broken'
                    ref.error_message = 'Invalid email format'
            else:
                ref.status = 'suspicious'
                ref.error_message = 'Unknown link type'
            
            validated.append(ref)
        
        return validated
    
    def _load_principle_registry(self) -> Set[int]:
        """Load principle registry from the knowledge base"""
        principle_registry = set()
        
        try:
            principles_path = self.base_path / "docs/knowledge/principles"
            if principles_path.exists():
                for principle_file in principles_path.rglob("*.md"):
                    with open(principle_file, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        # Extract principle numbers
                        principle_matches = re.findall(r'#(\d+)', content)
                        for match in principle_matches:
                            principle_registry.add(int(match))
        except Exception as e:
            logger.error(f"Error loading principle registry: {e}")
        
        return principle_registry
    
    def _analyze_network_structure(self, references: List[CrossReference]) -> Dict:
        """Analyze the network structure of cross-references"""
        try:
            # Build network graph
            nodes = set()
            edges = []
            
            for ref in references:
                if ref.status == 'valid':
                    source = ref.source_file
                    target = ref.target_path
                    
                    nodes.add(source)
                    nodes.add(target)
                    edges.append((source, target))
            
            node_count = len(nodes)
            edge_count = len(edges)
            
            # Calculate network density
            max_edges = node_count * (node_count - 1) if node_count > 1 else 1
            density = edge_count / max_edges if max_edges > 0 else 0
            
            # Calculate degree distribution
            degree_count = {}
            for source, target in edges:
                degree_count[source] = degree_count.get(source, 0) + 1
                degree_count[target] = degree_count.get(target, 0) + 1
            
            # Find hub nodes (top 10% by degree)
            sorted_nodes = sorted(degree_count.items(), key=lambda x: x[1], reverse=True)
            hub_count = max(1, len(sorted_nodes) // 10)
            hub_nodes = [node for node, degree in sorted_nodes[:hub_count]]
            
            # Count isolated nodes
            isolated_nodes = node_count - len(degree_count)
            
            network_metrics = {
                'node_count': node_count,
                'edge_count': edge_count,
                'density': round(density, 4),
                'clustering_coefficient': 0.0,  # Simplified
                'avg_path_length': 0.0,         # Simplified
                'isolated_nodes': isolated_nodes,
                'hub_nodes': hub_nodes[:10],    # Top 10 hubs
                'degree_distribution': dict(sorted_nodes[:20])  # Top 20
            }
            
            return network_metrics
            
        except Exception as e:
            logger.error(f"Error analyzing network structure: {e}")
            return {
                'node_count': 0,
                'edge_count': 0,
                'density': 0.0,
                'clustering_coefficient': 0.0,
                'avg_path_length': 0.0,
                'isolated_nodes': 0,
                'hub_nodes': [],
                'degree_distribution': {}
            }
    
    def _generate_validation_report(self, references: List[CrossReference], network_metrics: Dict) -> ValidationReport:
        """Generate comprehensive validation report"""
        timestamp = datetime.datetime.utcnow().isoformat()
        
        # Count statuses
        status_counts = {'valid': 0, 'broken': 0, 'suspicious': 0, 'unknown': 0}
        response_times = []
        
        for ref in references:
            status_counts[ref.status] = status_counts.get(ref.status, 0) + 1
            if ref.response_time:
                response_times.append(ref.response_time)
        
        total_links = len(references)
        valid_links = status_counts['valid']
        broken_links = status_counts['broken']
        suspicious_links = status_counts['suspicious']
        
        # Calculate metrics
        validation_coverage = (total_links - status_counts['unknown']) / total_links if total_links > 0 else 0
        avg_response_time = sum(response_times) / len(response_times) if response_times else 0
        
        # Generate issues and recommendations
        issues = []
        recommendations = []
        
        if broken_links > 0:
            issues.append(f"{broken_links} broken links found requiring immediate attention")
            recommendations.append("Fix broken links to maintain navigation integrity")
        
        if suspicious_links > 0:
            issues.append(f"{suspicious_links} suspicious links require manual verification")
            recommendations.append("Review suspicious links for security and validity")
        
        if network_metrics['density'] < 0.1:
            issues.append("Low network density indicates poor cross-referencing")
            recommendations.append("Increase cross-references between related content")
        
        if network_metrics['isolated_nodes'] > 0:
            issues.append(f"{network_metrics['isolated_nodes']} isolated content nodes found")
            recommendations.append("Link isolated content to improve discoverability")
        
        if avg_response_time > 2.0:
            issues.append("High average response time for external links")
            recommendations.append("Consider caching or mirrors for slow external resources")
        
        return ValidationReport(
            timestamp=timestamp,
            total_links=total_links,
            valid_links=valid_links,
            broken_links=broken_links,
            suspicious_links=suspicious_links,
            network_density=network_metrics['density'],
            validation_coverage=round(validation_coverage, 4),
            avg_response_time=round(avg_response_time, 4),
            issues_found=issues,
            recommendations=recommendations
        )
    
    def _store_validation_results(self, references: List[CrossReference], report: ValidationReport):
        """Store validation results in database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Clear old references
                cursor.execute("DELETE FROM cross_references")
                
                # Insert new references
                for ref in references:
                    cursor.execute("""
                        INSERT INTO cross_references 
                        (source_file, target_path, link_text, line_number, link_type, 
                         status, response_time, error_message, last_checked)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        ref.source_file, ref.target_path, ref.link_text, ref.line_number,
                        ref.link_type, ref.status, ref.response_time, ref.error_message,
                        ref.last_checked
                    ))
                
                # Insert validation report
                cursor.execute("""
                    INSERT INTO validation_reports
                    (timestamp, total_links, valid_links, broken_links, suspicious_links,
                     network_density, validation_coverage, avg_response_time, 
                     issues_count, recommendations_count)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    report.timestamp, report.total_links, report.valid_links,
                    report.broken_links, report.suspicious_links, report.network_density,
                    report.validation_coverage, report.avg_response_time,
                    len(report.issues_found), len(report.recommendations)
                ))
                
                conn.commit()
                logger.info("Validation results stored in database")
                
        except Exception as e:
            logger.error(f"Error storing validation results: {e}")
    
    def generate_report_json(self, report: ValidationReport, references: List[CrossReference]) -> str:
        """Generate JSON report file"""
        try:
            # Group references by status
            references_by_status = {}
            for ref in references:
                if ref.status not in references_by_status:
                    references_by_status[ref.status] = []
                references_by_status[ref.status].append(asdict(ref))
            
            # Create comprehensive report
            full_report = {
                'validation_summary': asdict(report),
                'references_by_status': references_by_status,
                'statistics': {
                    'total_references': len(references),
                    'validation_rate': (report.valid_links / report.total_links * 100) if report.total_links > 0 else 0,
                    'broken_rate': (report.broken_links / report.total_links * 100) if report.total_links > 0 else 0,
                    'suspicious_rate': (report.suspicious_links / report.total_links * 100) if report.total_links > 0 else 0
                },
                'network_health': {
                    'density': report.network_density,
                    'connectivity_score': min(report.network_density * 10, 10.0),
                    'integrity_score': (report.valid_links / report.total_links * 100) if report.total_links > 0 else 0
                }
            }
            
            # Save report
            report_file = self.results_path / f"cross-ref-validation-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
            os.makedirs(report_file.parent, exist_ok=True)
            
            with open(report_file, 'w') as f:
                json.dump(full_report, f, indent=2)
            
            # Save latest report
            latest_file = self.results_path / "cross-ref-validation-latest.json"
            with open(latest_file, 'w') as f:
                json.dump(full_report, f, indent=2)
            
            logger.info(f"Validation report saved: {report_file}")
            return str(report_file)
            
        except Exception as e:
            logger.error(f"Error generating report: {e}")
            return ""
    
    def fix_broken_links(self, dry_run: bool = True) -> Dict:
        """Attempt to fix broken links automatically"""
        logger.info(f"Starting link repair (dry_run={dry_run})")
        
        fixes_applied = []
        fixes_failed = []
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT source_file, target_path, link_text, line_number, error_message
                    FROM cross_references 
                    WHERE status = 'broken'
                """)
                
                broken_links = cursor.fetchall()
            
            for source_file, target_path, link_text, line_number, error_message in broken_links:
                try:
                    fix_result = self._attempt_link_fix(
                        source_file, target_path, link_text, line_number, error_message, dry_run
                    )
                    
                    if fix_result['success']:
                        fixes_applied.append(fix_result)
                    else:
                        fixes_failed.append(fix_result)
                        
                except Exception as e:
                    logger.error(f"Error fixing link {target_path}: {e}")
                    fixes_failed.append({
                        'source_file': source_file,
                        'target_path': target_path,
                        'error': str(e),
                        'success': False
                    })
            
            return {
                'fixes_applied': fixes_applied,
                'fixes_failed': fixes_failed,
                'summary': {
                    'total_broken': len(broken_links),
                    'fixes_attempted': len(fixes_applied) + len(fixes_failed),
                    'fixes_successful': len(fixes_applied),
                    'fixes_failed': len(fixes_failed)
                }
            }
            
        except Exception as e:
            logger.error(f"Error in link repair: {e}")
            return {'error': str(e)}
    
    def _attempt_link_fix(self, source_file: str, target_path: str, link_text: str, 
                         line_number: int, error_message: str, dry_run: bool) -> Dict:
        """Attempt to fix a single broken link"""
        try:
            source_path = self.base_path / source_file
            
            # Try to find the target file in common locations
            potential_targets = self._find_potential_targets(target_path)
            
            if potential_targets:
                # Use the best match
                best_match = potential_targets[0]
                relative_path = os.path.relpath(best_match, source_path.parent)
                
                if not dry_run:
                    # Replace the link in the source file
                    self._replace_link_in_file(source_path, target_path, relative_path, line_number)
                
                return {
                    'success': True,
                    'source_file': source_file,
                    'old_target': target_path,
                    'new_target': relative_path,
                    'action': 'replaced' if not dry_run else 'would_replace'
                }
            else:
                return {
                    'success': False,
                    'source_file': source_file,
                    'target_path': target_path,
                    'error': 'No suitable replacement found'
                }
                
        except Exception as e:
            return {
                'success': False,
                'source_file': source_file,
                'target_path': target_path,
                'error': str(e)
            }
    
    def _find_potential_targets(self, target_path: str) -> List[Path]:
        """Find potential target files for a broken link"""
        potential_targets = []
        
        # Extract filename from target
        target_name = os.path.basename(target_path)
        
        # Search for files with similar names
        for search_path in [self.base_path / "docs", self.base_path / "scripts"]:
            if search_path.exists():
                for file_path in search_path.rglob("*"):
                    if file_path.is_file() and file_path.name == target_name:
                        potential_targets.append(file_path)
                    elif file_path.is_file() and target_name.lower() in file_path.name.lower():
                        potential_targets.append(file_path)
        
        return potential_targets
    
    def _replace_link_in_file(self, source_path: Path, old_target: str, new_target: str, line_number: int):
        """Replace a link in a source file"""
        try:
            with open(source_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            if 1 <= line_number <= len(lines):
                line = lines[line_number - 1]
                updated_line = line.replace(old_target, new_target)
                lines[line_number - 1] = updated_line
                
                with open(source_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                    
                logger.info(f"Fixed link in {source_path}:{line_number}")
            
        except Exception as e:
            logger.error(f"Error replacing link in {source_path}: {e}")
            raise
    
    def get_validation_summary(self) -> Dict:
        """Get latest validation summary"""
        try:
            latest_file = self.results_path / "cross-ref-validation-latest.json"
            if latest_file.exists():
                with open(latest_file, 'r') as f:
                    return json.load(f)
            else:
                return {"error": "No validation data available"}
        except Exception as e:
            logger.error(f"Error getting validation summary: {e}")
            return {"error": str(e)}

def main():
    """Main function for standalone execution"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Cross-Reference Integrity Validator')
    parser.add_argument('--validate', action='store_true', help='Run full validation')
    parser.add_argument('--fix', action='store_true', help='Attempt to fix broken links')
    parser.add_argument('--dry-run', action='store_true', help='Dry run mode for fixes')
    parser.add_argument('--report', action='store_true', help='Generate report only')
    
    args = parser.parse_args()
    
    validator = CrossReferenceValidator()
    
    if args.validate or (not args.fix and not args.report):
        # Run validation
        logger.info("Starting cross-reference validation")
        all_references = validator._discover_all_references()
        validated_references = validator._validate_references_parallel(all_references)
        network_metrics = validator._analyze_network_structure(validated_references)
        report = validator._generate_validation_report(validated_references, network_metrics)
        
        # Store results
        validator._store_validation_results(validated_references, report)
        report_file = validator.generate_report_json(report, validated_references)
        
        print(f"\n✅ Validation completed!")
        print(f"📊 Total links: {report.total_links}")
        print(f"✅ Valid: {report.valid_links}")
        print(f"❌ Broken: {report.broken_links}")
        print(f"⚠️  Suspicious: {report.suspicious_links}")
        print(f"🔗 Network density: {report.network_density:.4f}")
        print(f"📄 Report saved: {report_file}")
    
    if args.fix:
        # Attempt fixes
        logger.info("Attempting to fix broken links")
        fix_results = validator.fix_broken_links(dry_run=args.dry_run)
        
        if 'error' in fix_results:
            print(f"❌ Fix error: {fix_results['error']}")
        else:
            summary = fix_results['summary']
            print(f"\n🔧 Link repair completed!")
            print(f"📊 Total broken: {summary['total_broken']}")
            print(f"✅ Fixes successful: {summary['fixes_successful']}")
            print(f"❌ Fixes failed: {summary['fixes_failed']}")
            
            if args.dry_run:
                print("🔍 Dry run mode - no changes were made")
    
    if args.report:
        # Generate report
        summary = validator.get_validation_summary()
        if 'error' in summary:
            print(f"❌ Report error: {summary['error']}")
        else:
            print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()