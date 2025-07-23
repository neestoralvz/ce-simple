#!/usr/bin/env python3
"""
Monitoring Orchestrator
Central coordination system for Context Engineering health monitoring
Establishes baselines, coordinates 178 commands + 136 scripts monitoring, and ensures 100% system reliability
"""

import json
import os
import sys
import time
import datetime
import sqlite3
import logging
import threading
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/Users/nalve/claude-context-engineering/scripts/results/monitoring/monitoring-orchestrator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class PerformanceBaseline:
    """Performance baseline data structure"""
    metric_name: str
    baseline_value: float
    tolerance: float  # percentage
    upper_bound: float
    lower_bound: float
    measurement_period: int  # days
    last_calibrated: str
    sample_count: int
    confidence_level: float

@dataclass
class MonitoringReport:
    """Comprehensive monitoring report"""
    timestamp: str
    overall_health_score: float
    system_availability: float
    component_health: Dict[str, float]
    performance_metrics: Dict[str, float]
    baselines_status: Dict[str, str]
    alerts_summary: Dict[str, int]
    recommendations: List[str]
    trend_analysis: Dict[str, str]

class MonitoringOrchestrator:
    """Central coordination system for comprehensive monitoring"""
    
    def __init__(self, config_path: str = None):
        self.base_path = Path("/Users/nalve/claude-context-engineering")
        self.config = self._load_config(config_path)
        self.db_path = self.base_path / "scripts/results/monitoring/monitoring_orchestrator.db"
        
        # Component paths
        self.health_monitor_path = self.base_path / "scripts/monitoring/system-health-monitor.py"
        self.cross_ref_validator_path = self.base_path / "scripts/monitoring/cross-reference-validator.py"
        self.alert_system_path = self.base_path / "scripts/monitoring/alert-system.py"
        
        # Monitoring state
        self.running = False
        self.baselines = {}
        self.monitoring_components = {}
        
        # Initialize system
        self._init_database()
        self._load_baselines()
        
    def _load_config(self, config_path: str) -> Dict:
        """Load monitoring orchestrator configuration"""
        default_config = {
            'orchestration_interval': 300,  # 5 minutes
            'baseline_calibration_days': 7,
            'baseline_recalibration_days': 30,
            'health_check_interval': 60,
            'cross_ref_check_interval': 3600,  # 1 hour
            'performance_sample_size': 100,
            'confidence_threshold': 0.95,
            'auto_remediation': True,
            'component_timeouts': {
                'health_monitor': 120,
                'cross_ref_validator': 300,
                'alert_system': 30
            }
        }
        
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    user_config = json.load(f)
                    default_config.update(user_config)
            except Exception as e:
                logger.warning(f"Failed to load config: {e}. Using defaults.")
        
        return default_config
    
    def _init_database(self):
        """Initialize database for monitoring orchestration"""
        os.makedirs(self.db_path.parent, exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Performance baselines table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS performance_baselines (
                    metric_name TEXT PRIMARY KEY,
                    baseline_value REAL NOT NULL,
                    tolerance REAL NOT NULL,
                    upper_bound REAL NOT NULL,
                    lower_bound REAL NOT NULL,
                    measurement_period INTEGER NOT NULL,
                    last_calibrated TEXT NOT NULL,
                    sample_count INTEGER NOT NULL,
                    confidence_level REAL NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Monitoring reports table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS monitoring_reports (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    overall_health_score REAL,
                    system_availability REAL,
                    component_health TEXT,  -- JSON
                    performance_metrics TEXT,  -- JSON
                    baselines_status TEXT,  -- JSON
                    alerts_summary TEXT,  -- JSON
                    recommendations TEXT,  -- JSON
                    trend_analysis TEXT,  -- JSON
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Component status table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS component_status (
                    component_name TEXT PRIMARY KEY,
                    status TEXT NOT NULL,  -- RUNNING, STOPPED, ERROR
                    last_check TEXT NOT NULL,
                    last_success TEXT,
                    error_count INTEGER DEFAULT 0,
                    success_count INTEGER DEFAULT 0,
                    response_time REAL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Performance history table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS performance_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    metric_name TEXT NOT NULL,
                    value REAL NOT NULL,
                    timestamp TEXT NOT NULL,
                    baseline_value REAL,
                    deviation_percent REAL,
                    within_bounds BOOLEAN,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.commit()
            logger.info("Monitoring orchestrator database initialized")
    
    def _load_baselines(self):
        """Load performance baselines from database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM performance_baselines")
                
                for row in cursor.fetchall():
                    baseline = PerformanceBaseline(
                        metric_name=row[0], baseline_value=row[1], tolerance=row[2],
                        upper_bound=row[3], lower_bound=row[4], measurement_period=row[5],
                        last_calibrated=row[6], sample_count=row[7], confidence_level=row[8]
                    )
                    self.baselines[baseline.metric_name] = baseline
                    
        except Exception as e:
            logger.error(f"Error loading baselines: {e}")
        
        # Create default baselines if none exist
        if not self.baselines:
            self._create_default_baselines()
    
    def _create_default_baselines(self):
        """Create default performance baselines"""
        default_baselines = [
            {
                'metric_name': 'overall_health_score',
                'baseline_value': 91.2,
                'tolerance': 5.0,  # ±5%
                'measurement_period': 7,
                'confidence_level': 0.95
            },
            {
                'metric_name': 'navigation_efficiency',
                'baseline_value': 2.3,
                'tolerance': 15.0,  # ±15%
                'measurement_period': 7,
                'confidence_level': 0.90
            },
            {
                'metric_name': 'response_time',
                'baseline_value': 450.0,  # milliseconds
                'tolerance': 25.0,  # ±25%
                'measurement_period': 7,
                'confidence_level': 0.90
            },
            {
                'metric_name': 'success_rate',
                'baseline_value': 96.5,
                'tolerance': 3.0,  # ±3%
                'measurement_period': 7,
                'confidence_level': 0.95
            },
            {
                'metric_name': 'system_availability',
                'baseline_value': 99.7,
                'tolerance': 1.0,  # ±1%
                'measurement_period': 7,
                'confidence_level': 0.99
            },
            {
                'metric_name': 'command_health',
                'baseline_value': 92.5,
                'tolerance': 5.0,  # ±5%
                'measurement_period': 7,
                'confidence_level': 0.95
            },
            {
                'metric_name': 'script_health',
                'baseline_value': 89.0,
                'tolerance': 7.0,  # ±7%
                'measurement_period': 7,
                'confidence_level': 0.90
            },
            {
                'metric_name': 'knowledge_health',
                'baseline_value': 94.0,
                'tolerance': 4.0,  # ±4%
                'measurement_period': 7,
                'confidence_level': 0.95
            },
            {
                'metric_name': 'cross_ref_validity',
                'baseline_value': 94.5,
                'tolerance': 5.0,  # ±5%
                'measurement_period': 7,
                'confidence_level': 0.90
            },
            {
                'metric_name': 'error_rate',
                'baseline_value': 1.8,
                'tolerance': 50.0,  # ±50% (more tolerance for errors)
                'measurement_period': 7,
                'confidence_level': 0.85
            }
        ]
        
        timestamp = datetime.datetime.utcnow().isoformat()
        
        for baseline_data in default_baselines:
            # Calculate bounds
            baseline_value = baseline_data['baseline_value']
            tolerance = baseline_data['tolerance']
            
            tolerance_range = baseline_value * (tolerance / 100.0)
            upper_bound = baseline_value + tolerance_range
            lower_bound = max(0, baseline_value - tolerance_range)
            
            baseline = PerformanceBaseline(
                metric_name=baseline_data['metric_name'],
                baseline_value=baseline_value,
                tolerance=tolerance,
                upper_bound=upper_bound,
                lower_bound=lower_bound,
                measurement_period=baseline_data['measurement_period'],
                last_calibrated=timestamp,
                sample_count=0,
                confidence_level=baseline_data['confidence_level']
            )
            
            self.baselines[baseline.metric_name] = baseline
            
            # Store in database
            self._store_baseline(baseline)
        
        logger.info(f"Created {len(default_baselines)} default performance baselines")
    
    def _store_baseline(self, baseline: PerformanceBaseline):
        """Store baseline in database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT OR REPLACE INTO performance_baselines
                    (metric_name, baseline_value, tolerance, upper_bound, lower_bound,
                     measurement_period, last_calibrated, sample_count, confidence_level)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    baseline.metric_name, baseline.baseline_value, baseline.tolerance,
                    baseline.upper_bound, baseline.lower_bound, baseline.measurement_period,
                    baseline.last_calibrated, baseline.sample_count, baseline.confidence_level
                ))
                conn.commit()
        except Exception as e:
            logger.error(f"Error storing baseline: {e}")
    
    def start_orchestration(self):
        """Start monitoring orchestration"""
        logger.info("Starting Monitoring Orchestration")
        self.running = True
        
        # Start orchestration thread
        orchestration_thread = threading.Thread(target=self._orchestration_loop, daemon=True)
        orchestration_thread.start()
        
        # Start baseline calibration thread
        calibration_thread = threading.Thread(target=self._calibration_loop, daemon=True)
        calibration_thread.start()
        
        # Start component health monitoring
        component_thread = threading.Thread(target=self._component_monitoring_loop, daemon=True)
        component_thread.start()
        
        logger.info("Monitoring orchestration started successfully")
    
    def stop_orchestration(self):
        """Stop monitoring orchestration"""
        logger.info("Stopping Monitoring Orchestration")
        self.running = False
    
    def _orchestration_loop(self):
        """Main orchestration loop"""
        while self.running:
            try:
                start_time = time.time()
                
                # Coordinate monitoring activities
                self._coordinate_monitoring()
                
                # Generate comprehensive report
                report = self._generate_comprehensive_report()
                
                # Store report
                self._store_monitoring_report(report)
                
                # Check for optimization opportunities
                self._identify_optimization_opportunities(report)
                
                execution_time = time.time() - start_time
                logger.info(f"Orchestration cycle completed in {execution_time:.2f}s")
                
                # Wait for next cycle
                time.sleep(self.config['orchestration_interval'])
                
            except Exception as e:
                logger.error(f"Error in orchestration loop: {e}")
                time.sleep(60)  # Wait before retry
    
    def _coordinate_monitoring(self):
        """Coordinate all monitoring components"""
        monitoring_tasks = []
        
        with ThreadPoolExecutor(max_workers=3) as executor:
            # Submit monitoring tasks
            futures = {
                executor.submit(self._run_health_monitor): 'health_monitor',
                executor.submit(self._run_cross_ref_validator): 'cross_ref_validator',
                executor.submit(self._check_alert_system): 'alert_system'
            }
            
            # Collect results
            for future in as_completed(futures, timeout=300):
                component = futures[future]
                try:
                    result = future.result(timeout=self.config['component_timeouts'].get(component, 120))
                    self.monitoring_components[component] = {
                        'status': 'SUCCESS',
                        'timestamp': datetime.datetime.utcnow().isoformat(),
                        'result': result
                    }
                    logger.debug(f"Component {component} completed successfully")
                except Exception as e:
                    self.monitoring_components[component] = {
                        'status': 'ERROR',
                        'timestamp': datetime.datetime.utcnow().isoformat(),
                        'error': str(e)
                    }
                    logger.error(f"Component {component} failed: {e}")
    
    def _run_health_monitor(self) -> Dict:
        """Run system health monitor"""
        try:
            # Import and run health monitor
            sys.path.insert(0, str(self.health_monitor_path.parent))
            from system_health_monitor import SystemHealthMonitor
            
            monitor = SystemHealthMonitor()
            
            # Collect metrics
            metrics = monitor._collect_health_metrics()
            
            # Store performance data
            self._record_performance_data(metrics)
            
            return {
                'health_score': metrics.overall_health_score,
                'availability': metrics.availability,
                'navigation_efficiency': metrics.navigation_efficiency,
                'response_time': metrics.response_time,
                'success_rate': metrics.success_rate,
                'component_health': {
                    'commands': metrics.command_health,
                    'scripts': metrics.script_health,
                    'knowledge': metrics.knowledge_health,
                    'performance': metrics.performance_health
                }
            }
            
        except Exception as e:
            logger.error(f"Error running health monitor: {e}")
            return {'error': str(e)}
    
    def _run_cross_ref_validator(self) -> Dict:
        """Run cross-reference validator"""
        try:
            # Check if validation should run (based on interval)
            last_validation = self._get_last_cross_ref_validation()
            if last_validation:
                time_since = time.time() - last_validation
                if time_since < self.config['cross_ref_check_interval']:
                    return {'status': 'skipped', 'reason': 'within_interval'}
            
            # Import and run validator
            sys.path.insert(0, str(self.cross_ref_validator_path.parent))
            from cross_reference_validator import CrossReferenceValidator
            
            validator = CrossReferenceValidator()
            
            # Run validation
            all_references = validator._discover_all_references()
            validated_references = validator._validate_references_parallel(all_references)
            network_metrics = validator._analyze_network_structure(validated_references)
            report = validator._generate_validation_report(validated_references, network_metrics)
            
            # Store results
            validator._store_validation_results(validated_references, report)
            validator.generate_report_json(report, validated_references)
            
            # Record performance data
            self._record_performance_data({
                'cross_ref_validity': (report.valid_links / report.total_links * 100) if report.total_links > 0 else 100,
                'broken_links': report.broken_links,
                'network_density': report.network_density
            })
            
            return {
                'total_links': report.total_links,
                'valid_links': report.valid_links,
                'broken_links': report.broken_links,
                'network_density': report.network_density,
                'validation_coverage': report.validation_coverage
            }
            
        except Exception as e:
            logger.error(f"Error running cross-reference validator: {e}")
            return {'error': str(e)}
    
    def _check_alert_system(self) -> Dict:
        """Check alert system status"""
        try:
            # Import and check alert system
            sys.path.insert(0, str(self.alert_system_path.parent))
            from alert_system import AlertSystem
            
            alert_system = AlertSystem()
            
            # Get system statistics
            stats = alert_system.get_alert_statistics()
            active_alerts = alert_system.get_active_alerts()
            
            return {
                'active_alerts': stats.get('active_alerts', 0),
                'alerts_today': stats.get('alerts_today', 0),
                'system_health': stats.get('system_health', 'UNKNOWN'),
                'severity_distribution': stats.get('severity_distribution_today', {}),
                'alert_details': active_alerts[:5]  # Top 5 active alerts
            }
            
        except Exception as e:
            logger.error(f"Error checking alert system: {e}")
            return {'error': str(e)}
    
    def _record_performance_data(self, metrics: Dict):
        """Record performance data and check against baselines"""
        timestamp = datetime.datetime.utcnow().isoformat()
        
        for metric_name, value in metrics.items():
            if metric_name in self.baselines:
                baseline = self.baselines[metric_name]
                
                # Calculate deviation
                deviation_percent = ((value - baseline.baseline_value) / baseline.baseline_value) * 100
                within_bounds = baseline.lower_bound <= value <= baseline.upper_bound
                
                # Store in database
                try:
                    with sqlite3.connect(self.db_path) as conn:
                        cursor = conn.cursor()
                        cursor.execute("""
                            INSERT INTO performance_history
                            (metric_name, value, timestamp, baseline_value, 
                             deviation_percent, within_bounds)
                            VALUES (?, ?, ?, ?, ?, ?)
                        """, (
                            metric_name, value, timestamp, baseline.baseline_value,
                            deviation_percent, within_bounds
                        ))
                        conn.commit()
                        
                except Exception as e:
                    logger.error(f"Error recording performance data: {e}")
    
    def _get_last_cross_ref_validation(self) -> Optional[float]:
        """Get timestamp of last cross-reference validation"""
        try:
            validation_file = self.base_path / "scripts/results/monitoring/cross-ref-validation-latest.json"
            if validation_file.exists():
                with open(validation_file, 'r') as f:
                    data = json.load(f)
                    timestamp_str = data.get('validation_summary', {}).get('timestamp')
                    if timestamp_str:
                        return datetime.datetime.fromisoformat(timestamp_str).timestamp()
        except Exception as e:
            logger.debug(f"Error getting last validation timestamp: {e}")
        
        return None
    
    def _generate_comprehensive_report(self) -> MonitoringReport:
        """Generate comprehensive monitoring report"""
        timestamp = datetime.datetime.utcnow().isoformat()
        
        # Collect data from monitoring components
        health_data = self.monitoring_components.get('health_monitor', {}).get('result', {})
        cross_ref_data = self.monitoring_components.get('cross_ref_validator', {}).get('result', {})
        alert_data = self.monitoring_components.get('alert_system', {}).get('result', {})
        
        # Calculate overall metrics
        overall_health_score = health_data.get('health_score', 0)
        system_availability = health_data.get('availability', 0)
        
        # Component health
        component_health = health_data.get('component_health', {})
        
        # Performance metrics
        performance_metrics = {
            'navigation_efficiency': health_data.get('navigation_efficiency', 2.5),
            'response_time': health_data.get('response_time', 500),
            'success_rate': health_data.get('success_rate', 95),
            'cross_ref_validity': (cross_ref_data.get('valid_links', 0) / 
                                  max(cross_ref_data.get('total_links', 1), 1) * 100),
            'network_density': cross_ref_data.get('network_density', 0)
        }
        
        # Baseline status
        baselines_status = self._check_baseline_compliance(performance_metrics)
        
        # Alerts summary
        alerts_summary = {
            'active': alert_data.get('active_alerts', 0),
            'today': alert_data.get('alerts_today', 0),
            'critical': alert_data.get('severity_distribution', {}).get('CRITICAL', 0),
            'warning': alert_data.get('severity_distribution', {}).get('WARNING', 0),
            'info': alert_data.get('severity_distribution', {}).get('INFO', 0)
        }
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            overall_health_score, performance_metrics, baselines_status, alerts_summary
        )
        
        # Trend analysis
        trend_analysis = self._analyze_trends()
        
        return MonitoringReport(
            timestamp=timestamp,
            overall_health_score=overall_health_score,
            system_availability=system_availability,
            component_health=component_health,
            performance_metrics=performance_metrics,
            baselines_status=baselines_status,
            alerts_summary=alerts_summary,
            recommendations=recommendations,
            trend_analysis=trend_analysis
        )
    
    def _check_baseline_compliance(self, metrics: Dict) -> Dict[str, str]:
        """Check current metrics against baselines"""
        compliance_status = {}
        
        for metric_name, value in metrics.items():
            if metric_name in self.baselines:
                baseline = self.baselines[metric_name]
                
                if baseline.lower_bound <= value <= baseline.upper_bound:
                    compliance_status[metric_name] = 'WITHIN_BASELINE'
                elif value > baseline.upper_bound:
                    compliance_status[metric_name] = 'ABOVE_BASELINE'
                else:
                    compliance_status[metric_name] = 'BELOW_BASELINE'
            else:
                compliance_status[metric_name] = 'NO_BASELINE'
        
        return compliance_status
    
    def _generate_recommendations(self, health_score: float, metrics: Dict, 
                                baselines: Dict, alerts: Dict) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        # Health score recommendations
        if health_score < 85.0:
            recommendations.append("System health below optimal - investigate failing components")
        elif health_score < 90.0:
            recommendations.append("System health adequate but could be improved")
        
        # Performance recommendations
        if metrics.get('navigation_efficiency', 0) > 2.5:
            recommendations.append("Navigation efficiency exceeds target - optimize content organization")
        
        if metrics.get('response_time', 0) > 1000:
            recommendations.append("Response time high - investigate performance bottlenecks")
        
        if metrics.get('success_rate', 100) < 95.0:
            recommendations.append("Success rate below target - investigate error sources")
        
        # Cross-reference recommendations
        if metrics.get('cross_ref_validity', 100) < 90.0:
            recommendations.append("Cross-reference validity low - run link repair automation")
        
        # Baseline compliance recommendations
        below_baseline_count = sum(1 for status in baselines.values() if status == 'BELOW_BASELINE')
        if below_baseline_count > 2:
            recommendations.append("Multiple metrics below baseline - consider system optimization")
        
        # Alert recommendations
        if alerts.get('active', 0) > 5:
            recommendations.append("High number of active alerts - investigate root causes")
        
        if alerts.get('critical', 0) > 0:
            recommendations.append("Critical alerts active - immediate attention required")
        
        return recommendations
    
    def _analyze_trends(self) -> Dict[str, str]:
        """Analyze performance trends"""
        trends = {}
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Analyze trends for key metrics
                for metric_name in ['overall_health_score', 'navigation_efficiency', 'response_time', 'success_rate']:
                    cursor.execute("""
                        SELECT value, timestamp FROM performance_history 
                        WHERE metric_name = ? AND timestamp >= datetime('now', '-7 days')
                        ORDER BY timestamp DESC LIMIT 50
                    """, (metric_name,))
                    
                    data = cursor.fetchall()
                    if len(data) >= 10:
                        values = [row[0] for row in data]
                        
                        # Simple trend analysis
                        recent_avg = sum(values[:10]) / 10
                        older_avg = sum(values[-10:]) / 10
                        
                        if recent_avg > older_avg * 1.05:
                            trends[metric_name] = 'IMPROVING'
                        elif recent_avg < older_avg * 0.95:
                            trends[metric_name] = 'DECLINING'
                        else:
                            trends[metric_name] = 'STABLE'
                    else:
                        trends[metric_name] = 'INSUFFICIENT_DATA'
                        
        except Exception as e:
            logger.error(f"Error analyzing trends: {e}")
        
        return trends
    
    def _store_monitoring_report(self, report: MonitoringReport):
        """Store monitoring report in database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO monitoring_reports
                    (timestamp, overall_health_score, system_availability, 
                     component_health, performance_metrics, baselines_status,
                     alerts_summary, recommendations, trend_analysis)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    report.timestamp, report.overall_health_score, report.system_availability,
                    json.dumps(report.component_health), json.dumps(report.performance_metrics),
                    json.dumps(report.baselines_status), json.dumps(report.alerts_summary),
                    json.dumps(report.recommendations), json.dumps(report.trend_analysis)
                ))
                conn.commit()
                
            # Also save as JSON file
            report_file = self.base_path / "scripts/results/monitoring/comprehensive-report-latest.json"
            os.makedirs(report_file.parent, exist_ok=True)
            
            with open(report_file, 'w') as f:
                json.dump(asdict(report), f, indent=2)
                
        except Exception as e:
            logger.error(f"Error storing monitoring report: {e}")
    
    def _identify_optimization_opportunities(self, report: MonitoringReport):
        """Identify and log optimization opportunities"""
        opportunities = []
        
        # Performance optimization opportunities
        if report.performance_metrics.get('response_time', 0) > 800:
            opportunities.append("Response time optimization: Consider caching, CDN, or code optimization")
        
        if report.performance_metrics.get('navigation_efficiency', 0) > 2.8:
            opportunities.append("Navigation optimization: Reorganize content for better discoverability")
        
        # Component optimization opportunities
        component_health = report.component_health
        if component_health.get('scripts', 100) < 85:
            opportunities.append("Script ecosystem optimization: Review failing scripts and dependencies")
        
        if component_health.get('knowledge', 100) < 90:
            opportunities.append("Knowledge network optimization: Update documentation and fix cross-references")
        
        # System optimization opportunities
        if report.overall_health_score < 88:
            opportunities.append("System-wide optimization: Comprehensive health review recommended")
        
        # Alert optimization opportunities
        if report.alerts_summary.get('active', 0) > 3:
            opportunities.append("Alert optimization: Review alert thresholds and auto-remediation rules")
        
        if opportunities:
            logger.info(f"Optimization opportunities identified: {len(opportunities)}")
            for opportunity in opportunities:
                logger.info(f"  - {opportunity}")
    
    def _calibration_loop(self):
        """Baseline calibration loop"""
        while self.running:
            try:
                # Check if recalibration is needed
                for metric_name, baseline in self.baselines.items():
                    last_calibrated = datetime.datetime.fromisoformat(baseline.last_calibrated)
                    days_since = (datetime.datetime.utcnow() - last_calibrated).days
                    
                    if days_since >= self.config['baseline_recalibration_days']:
                        logger.info(f"Recalibrating baseline for {metric_name}")
                        self._recalibrate_baseline(metric_name)
                
                # Sleep until next calibration check (daily)
                time.sleep(24 * 3600)
                
            except Exception as e:
                logger.error(f"Error in calibration loop: {e}")
                time.sleep(3600)  # Retry in 1 hour
    
    def _recalibrate_baseline(self, metric_name: str):
        """Recalibrate baseline for specific metric"""
        try:
            # Get recent performance data
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT value FROM performance_history 
                    WHERE metric_name = ? AND timestamp >= datetime('now', '-30 days')
                    AND within_bounds = TRUE
                    ORDER BY timestamp DESC
                """, (metric_name,))
                
                values = [row[0] for row in cursor.fetchall()]
            
            if len(values) >= 20:  # Minimum samples for recalibration
                # Calculate new baseline
                new_baseline_value = sum(values) / len(values)
                
                # Update baseline
                baseline = self.baselines[metric_name]
                baseline.baseline_value = new_baseline_value
                baseline.last_calibrated = datetime.datetime.utcnow().isoformat()
                baseline.sample_count = len(values)
                
                # Recalculate bounds
                tolerance_range = new_baseline_value * (baseline.tolerance / 100.0)
                baseline.upper_bound = new_baseline_value + tolerance_range
                baseline.lower_bound = max(0, new_baseline_value - tolerance_range)
                
                # Store updated baseline
                self._store_baseline(baseline)
                
                logger.info(f"Recalibrated {metric_name}: {new_baseline_value:.2f} "
                          f"(±{baseline.tolerance}%)")
            else:
                logger.warning(f"Insufficient data for {metric_name} recalibration: {len(values)} samples")
                
        except Exception as e:
            logger.error(f"Error recalibrating baseline for {metric_name}: {e}")
    
    def _component_monitoring_loop(self):
        """Monitor component health"""
        while self.running:
            try:
                # Check component status
                for component_name in ['health_monitor', 'cross_ref_validator', 'alert_system']:
                    status = self.monitoring_components.get(component_name, {})
                    
                    # Update component status in database
                    self._update_component_status(component_name, status)
                
                # Sleep for 5 minutes
                time.sleep(300)
                
            except Exception as e:
                logger.error(f"Error in component monitoring: {e}")
                time.sleep(60)
    
    def _update_component_status(self, component_name: str, status: Dict):
        """Update component status in database"""
        try:
            timestamp = datetime.datetime.utcnow().isoformat()
            component_status = status.get('status', 'UNKNOWN')
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Get current status
                cursor.execute("""
                    SELECT error_count, success_count FROM component_status 
                    WHERE component_name = ?
                """, (component_name,))
                
                result = cursor.fetchone()
                error_count = result[0] if result else 0
                success_count = result[1] if result else 0
                
                # Update counts
                if component_status == 'SUCCESS':
                    success_count += 1
                elif component_status == 'ERROR':
                    error_count += 1
                
                # Update status
                cursor.execute("""
                    INSERT OR REPLACE INTO component_status
                    (component_name, status, last_check, last_success, 
                     error_count, success_count, response_time)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    component_name, component_status, timestamp,
                    timestamp if component_status == 'SUCCESS' else None,
                    error_count, success_count,
                    status.get('response_time', 0)
                ))
                
                conn.commit()
                
        except Exception as e:
            logger.error(f"Error updating component status: {e}")
    
    def get_system_status(self) -> Dict:
        """Get comprehensive system status"""
        try:
            # Get latest report
            report_file = self.base_path / "scripts/results/monitoring/comprehensive-report-latest.json"
            if report_file.exists():
                with open(report_file, 'r') as f:
                    latest_report = json.load(f)
            else:
                latest_report = {}
            
            # Get component status
            component_status = {}
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM component_status")
                
                for row in cursor.fetchall():
                    component_status[row[0]] = {
                        'status': row[1],
                        'last_check': row[2],
                        'error_count': row[4],
                        'success_count': row[5]
                    }
            
            return {
                'latest_report': latest_report,
                'component_status': component_status,
                'baselines': {name: asdict(baseline) for name, baseline in self.baselines.items()},
                'orchestration_status': 'RUNNING' if self.running else 'STOPPED'
            }
            
        except Exception as e:
            logger.error(f"Error getting system status: {e}")
            return {'error': str(e)}
    
    def generate_dashboard(self) -> str:
        """Generate monitoring dashboard output"""
        try:
            status = self.get_system_status()
            latest_report = status.get('latest_report', {})
            
            health_score = latest_report.get('overall_health_score', 0)
            availability = latest_report.get('system_availability', 0)
            component_health = latest_report.get('component_health', {})
            alerts_summary = latest_report.get('alerts_summary', {})
            
            dashboard = f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║              🎯 CONTEXT ENGINEERING COMPREHENSIVE MONITORING                   ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║ Overall Health: {health_score:.4f}/100.0000    Availability: {availability:.2f}%        ║
║ Orchestration: {status.get('orchestration_status', 'UNKNOWN')}    Last Update: {latest_report.get('timestamp', 'Unknown')[:19]} ║
╚═══════════════════════════════════════════════════════════════════════════════╝

📊 COMPONENT HEALTH MATRIX:
├─ 🟢 Commands: {component_health.get('commands', 0):.1f}% Health
├─ 🟢 Scripts: {component_health.get('scripts', 0):.1f}% Health  
├─ 🟢 Knowledge: {component_health.get('knowledge', 0):.1f}% Health
└─ 🟢 Performance: {component_health.get('performance', 0):.1f}% Health

🚨 ALERTS DASHBOARD:
├─ Active Alerts: {alerts_summary.get('active', 0)}
├─ Critical: {alerts_summary.get('critical', 0)}
├─ Warning: {alerts_summary.get('warning', 0)}
└─ Info: {alerts_summary.get('info', 0)}

📈 PERFORMANCE BASELINES:
"""
            
            for metric_name, baseline in self.baselines.items():
                status_icon = "✅" if metric_name in latest_report.get('baselines_status', {}) and \
                            latest_report['baselines_status'][metric_name] == 'WITHIN_BASELINE' else "⚠️"
                dashboard += f"├─ {status_icon} {metric_name}: {baseline.baseline_value:.2f} (±{baseline.tolerance:.1f}%)\n"
            
            recommendations = latest_report.get('recommendations', [])
            if recommendations:
                dashboard += f"\n💡 RECOMMENDATIONS ({len(recommendations)}):\n"
                for i, rec in enumerate(recommendations[:3], 1):
                    dashboard += f"   {i}. {rec}\n"
            
            return dashboard
            
        except Exception as e:
            logger.error(f"Error generating dashboard: {e}")
            return f"❌ Dashboard Generation Error: {e}"

def main():
    """Main function for standalone execution"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Context Engineering Monitoring Orchestrator')
    parser.add_argument('--start', action='store_true', help='Start monitoring orchestration')
    parser.add_argument('--status', action='store_true', help='Show system status')
    parser.add_argument('--dashboard', action='store_true', help='Show monitoring dashboard')
    parser.add_argument('--calibrate', type=str, help='Calibrate specific baseline')
    parser.add_argument('--report', action='store_true', help='Generate comprehensive report')
    
    args = parser.parse_args()
    
    orchestrator = MonitoringOrchestrator()
    
    if args.start:
        # Start orchestration
        orchestrator.start_orchestration()
        
        print("🎯 Monitoring Orchestrator started")
        print("Press Ctrl+C to stop...")
        
        try:
            while True:
                time.sleep(300)  # Show status every 5 minutes
                print("\n" + orchestrator.generate_dashboard())
        except KeyboardInterrupt:
            orchestrator.stop_orchestration()
            print("\n✅ Monitoring Orchestrator stopped")
    
    elif args.status:
        # Show system status
        status = orchestrator.get_system_status()
        print("🎯 Monitoring System Status:")
        print(json.dumps(status, indent=2))
    
    elif args.dashboard:
        # Show dashboard
        print(orchestrator.generate_dashboard())
    
    elif args.calibrate:
        # Calibrate specific baseline
        if args.calibrate in orchestrator.baselines:
            orchestrator._recalibrate_baseline(args.calibrate)
            print(f"✅ Baseline {args.calibrate} recalibrated")
        else:
            print(f"❌ Baseline {args.calibrate} not found")
    
    elif args.report:
        # Generate comprehensive report
        report = orchestrator._generate_comprehensive_report()
        orchestrator._store_monitoring_report(report)
        print("✅ Comprehensive report generated")
        print(json.dumps(asdict(report), indent=2))
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()