#!/usr/bin/env python3
"""
Compliance Dashboard - Context Engineering
MANDATORY: Real-time compliance monitoring dashboard
Displays current compliance status, violations, and remediation progress

CRITICAL FEATURES:
- Real-time compliance metrics
- Violation tracking and remediation status
- Alert summary and escalation queue
- System health monitoring
- Historical compliance trends
"""

import os
import json
import sqlite3
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from pathlib import Path
import argparse

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent.parent
COMPLIANCE_RESULTS = PROJECT_ROOT / 'scripts/results/compliance/enhanced'
GOVERNANCE_RESULTS = PROJECT_ROOT / 'scripts/results/governance'
BRIDGE_DB = GOVERNANCE_RESULTS / 'compliance-bridge.db'
ALERTS_DB = GOVERNANCE_RESULTS / 'alerts.db'
DASHBOARD_DIR = GOVERNANCE_RESULTS / 'dashboard'

class ComplianceDashboard:
    """Real-time compliance monitoring dashboard"""
    
    def __init__(self):
        self.compliance_data = {}
        self.violations_data = []
        self.alerts_data = []
        self.system_status = {}
        
    def load_latest_compliance_report(self) -> Dict[str, Any]:
        """Load the most recent compliance report"""
        try:
            if not COMPLIANCE_RESULTS.exists():
                return {"error": "Compliance results directory not found"}
            
            report_files = list(COMPLIANCE_RESULTS.glob("enhanced-p55-p56-report-*.json"))
            if not report_files:
                return {"error": "No compliance reports found"}
            
            # Get the most recent report
            latest_report = max(report_files, key=lambda f: f.stat().st_mtime)
            
            with open(latest_report, 'r') as f:
                report_data = json.load(f)
            
            # Calculate age of report
            file_age = time.time() - latest_report.stat().st_mtime
            report_data['file_age_minutes'] = file_age / 60
            report_data['file_path'] = str(latest_report.name)
            
            return report_data
            
        except Exception as e:
            return {"error": f"Failed to load compliance report: {e}"}
    
    def load_violations_from_bridge(self) -> List[Dict[str, Any]]:
        """Load violations from bridge database"""
        try:
            if not BRIDGE_DB.exists():
                return []
            
            violations = []
            with sqlite3.connect(BRIDGE_DB) as conn:
                cursor = conn.execute('''
                    SELECT * FROM compliance_violations 
                    WHERE resolved_at IS NULL
                    ORDER BY timestamp DESC
                    LIMIT 50
                ''')
                
                columns = [description[0] for description in cursor.description]
                for row in cursor.fetchall():
                    violation = dict(zip(columns, row))
                    violations.append(violation)
            
            return violations
            
        except Exception as e:
            return [{"error": f"Failed to load violations: {e}"}]
    
    def load_alerts_from_system(self) -> List[Dict[str, Any]]:
        """Load recent alerts from alert system"""
        try:
            alerts = []
            
            # Load from file-based alerts
            alerts_dir = DASHBOARD_DIR / 'alerts'
            if alerts_dir.exists():
                alert_files = list(alerts_dir.glob("alert_*.json"))
                # Get recent alerts (last 24 hours)
                cutoff_time = time.time() - (24 * 3600)
                
                for alert_file in alert_files:
                    if alert_file.stat().st_mtime > cutoff_time:
                        try:
                            with open(alert_file, 'r') as f:
                                alert_data = json.load(f)
                                alerts.append(alert_data)
                        except:
                            continue
            
            # Load from database if available
            if ALERTS_DB.exists():
                try:
                    with sqlite3.connect(ALERTS_DB) as conn:
                        cursor = conn.execute('''
                            SELECT * FROM governance_alerts 
                            WHERE timestamp > datetime('now', '-24 hours')
                            ORDER BY timestamp DESC
                            LIMIT 20
                        ''')
                        
                        columns = [description[0] for description in cursor.description]
                        for row in cursor.fetchall():
                            alert = dict(zip(columns, row))
                            alerts.append(alert)
                except:
                    pass
            
            # Sort by timestamp and limit
            alerts.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
            return alerts[:20]
            
        except Exception as e:
            return [{"error": f"Failed to load alerts: {e}"}]
    
    def get_system_health(self) -> Dict[str, Any]:
        """Get system health status"""
        try:
            health = {
                "timestamp": datetime.now().isoformat(),
                "components": {},
                "overall_status": "unknown"
            }
            
            # Check compliance monitoring
            recent_reports = len(list(COMPLIANCE_RESULTS.glob("*.json"))) if COMPLIANCE_RESULTS.exists() else 0
            health["components"]["compliance_monitoring"] = {
                "status": "active" if recent_reports > 0 else "inactive",
                "recent_reports": recent_reports
            }
            
            # Check bridge system
            bridge_pid_file = GOVERNANCE_RESULTS / 'bridge.pid'
            bridge_active = False
            if bridge_pid_file.exists():
                try:
                    with open(bridge_pid_file, 'r') as f:
                        pid = int(f.read().strip())
                    # Check if process is running (Unix-like systems)
                    os.kill(pid, 0)
                    bridge_active = True
                except:
                    bridge_active = False
            
            health["components"]["remediation_bridge"] = {
                "status": "active" if bridge_active else "inactive",
                "pid_file_exists": bridge_pid_file.exists()
            }
            
            # Check alert system
            alerts_config = PROJECT_ROOT / 'scripts/governance/alerts-config.json'
            health["components"]["alert_system"] = {
                "status": "configured" if alerts_config.exists() else "not_configured",
                "config_exists": alerts_config.exists()
            }
            
            # Determine overall status
            active_components = sum(1 for comp in health["components"].values() 
                                  if comp["status"] in ["active", "configured"])
            total_components = len(health["components"])
            
            if active_components == total_components:
                health["overall_status"] = "healthy"
            elif active_components > 0:
                health["overall_status"] = "partial"
            else:
                health["overall_status"] = "down"
            
            return health
            
        except Exception as e:
            return {"error": f"Failed to get system health: {e}"}
    
    def generate_dashboard_data(self) -> Dict[str, Any]:
        """Generate complete dashboard data"""
        dashboard_data = {
            "generated_at": datetime.now().isoformat(),
            "compliance_report": self.load_latest_compliance_report(),
            "active_violations": self.load_violations_from_bridge(),
            "recent_alerts": self.load_alerts_from_system(),
            "system_health": self.get_system_health()
        }
        
        # Calculate summary statistics
        compliance_report = dashboard_data["compliance_report"]
        if "enhanced_p55_p56_compliance_report" in compliance_report:
            report = compliance_report["enhanced_p55_p56_compliance_report"]
            dashboard_data["summary"] = {
                "overall_compliance": report.get("calculated_metrics", {}).get("overall_compliance", {}),
                "compliance_results": report.get("compliance_results", {}),
                "violations_count": len(dashboard_data["active_violations"]),
                "alerts_count": len(dashboard_data["recent_alerts"]),
                "system_status": dashboard_data["system_health"]["overall_status"]
            }
        else:
            dashboard_data["summary"] = {
                "overall_compliance": {"overall_compliance_percentage": "Unknown"},
                "compliance_results": {},
                "violations_count": len(dashboard_data["active_violations"]),
                "alerts_count": len(dashboard_data["recent_alerts"]),
                "system_status": dashboard_data["system_health"]["overall_status"]
            }
        
        return dashboard_data
    
    def save_dashboard_data(self, dashboard_data: Dict[str, Any]):
        """Save dashboard data to file"""
        try:
            os.makedirs(DASHBOARD_DIR, exist_ok=True)
            
            dashboard_file = DASHBOARD_DIR / 'live-dashboard.json'
            with open(dashboard_file, 'w') as f:
                json.dump(dashboard_data, f, indent=2)
            
            print(f"Dashboard data saved to: {dashboard_file}")
            
        except Exception as e:
            print(f"Failed to save dashboard data: {e}")
    
    def display_dashboard(self, dashboard_data: Dict[str, Any]):
        """Display dashboard in console"""
        print("\n" + "="*80)
        print("COMPLIANCE MONITORING DASHBOARD")
        print("="*80)
        print(f"Generated: {dashboard_data['generated_at']}")
        print("")
        
        # System Health
        system_health = dashboard_data["system_health"]
        status_emoji = {"healthy": "🟢", "partial": "🟡", "down": "🔴"}.get(system_health["overall_status"], "⚪")
        print(f"🏥 SYSTEM HEALTH: {status_emoji} {system_health['overall_status'].upper()}")
        
        for component, details in system_health["components"].items():
            comp_emoji = "✅" if details["status"] in ["active", "configured"] else "❌"
            print(f"  {comp_emoji} {component.replace('_', ' ').title()}: {details['status']}")
        print("")
        
        # Compliance Summary
        summary = dashboard_data["summary"]
        compliance_pct = summary["overall_compliance"].get("overall_compliance_percentage", "Unknown")
        compliance_emoji = "🟢" if compliance_pct != "Unknown" and float(compliance_pct.rstrip('%')) >= 80 else "🔴"
        
        print(f"📊 COMPLIANCE STATUS: {compliance_emoji} {compliance_pct}")
        
        compliance_results = summary["compliance_results"]
        for check, result in compliance_results.items():
            if check != "overall_compliance":
                result_emoji = "✅" if result else "❌"
                check_name = check.replace('_compliant', '').replace('_', ' ').title()
                print(f"  {result_emoji} {check_name}: {'PASS' if result else 'FAIL'}")
        print("")
        
        # Active Violations
        violations_count = summary["violations_count"]
        if violations_count > 0:
            print(f"🚨 ACTIVE VIOLATIONS: {violations_count}")
            for violation in dashboard_data["active_violations"][:5]:  # Show first 5
                if isinstance(violation, dict) and "violation_type" in violation:
                    severity_emoji = {"emergency": "💥", "critical": "🔥", "high": "🚨", "warning": "⚠️"}.get(violation.get("severity", "warning"), "⚠️")
                    print(f"  {severity_emoji} {violation['violation_type'].replace('_', ' ').title()}: "
                          f"{violation.get('current_value', 0):.3f} (req: {violation.get('threshold_value', 0):.3f}) "
                          f"[{violation.get('remediation_status', 'unknown')}]")
            
            if violations_count > 5:
                print(f"  ... and {violations_count - 5} more violations")
        else:
            print("✅ NO ACTIVE VIOLATIONS")
        print("")
        
        # Recent Alerts
        alerts_count = summary["alerts_count"]
        if alerts_count > 0:
            print(f"📢 RECENT ALERTS: {alerts_count} (last 24h)")
            for alert in dashboard_data["recent_alerts"][:3]:  # Show first 3
                if isinstance(alert, dict) and "severity" in alert:
                    alert_emoji = {"emergency": "💥", "critical": "🔥", "high": "🚨", "warning": "⚠️", "info": "ℹ️"}.get(alert.get("severity", "info"), "📢")
                    timestamp = alert.get("timestamp", "unknown")
                    if timestamp != "unknown":
                        try:
                            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                            time_ago = datetime.now() - dt.replace(tzinfo=None)
                            time_str = f"{int(time_ago.total_seconds() / 60)}m ago"
                        except:
                            time_str = "unknown time"
                    else:
                        time_str = "unknown time"
                    
                    print(f"  {alert_emoji} {alert.get('title', 'Unknown Alert')} ({time_str})")
            
            if alerts_count > 3:
                print(f"  ... and {alerts_count - 3} more alerts")
        else:
            print("✅ NO RECENT ALERTS")
        print("")
        
        # Compliance Report Age
        compliance_report = dashboard_data["compliance_report"]
        if "file_age_minutes" in compliance_report:
            age_minutes = compliance_report["file_age_minutes"]
            age_emoji = "🟢" if age_minutes < 10 else "🟡" if age_minutes < 60 else "🔴"
            print(f"📄 LATEST REPORT: {age_emoji} {age_minutes:.1f} minutes old ({compliance_report.get('file_path', 'unknown')})")
        else:
            print("📄 LATEST REPORT: ❌ No valid compliance report found")
        
        print("="*80)
        print("")

def main():
    """Main dashboard execution"""
    parser = argparse.ArgumentParser(description="Compliance Monitoring Dashboard")
    parser.add_argument("--watch", "-w", action="store_true", help="Watch mode - continuous updates")
    parser.add_argument("--interval", "-i", type=int, default=30, help="Update interval in seconds (default: 30)")
    parser.add_argument("--save", "-s", action="store_true", help="Save dashboard data to file")
    parser.add_argument("--quiet", "-q", action="store_true", help="Quiet mode - save only, no display")
    
    args = parser.parse_args()
    
    dashboard = ComplianceDashboard()
    
    try:
        if args.watch:
            print("Starting dashboard in watch mode...")
            print(f"Update interval: {args.interval} seconds")
            print("Press Ctrl+C to stop")
            print("")
            
            while True:
                if not args.quiet:
                    # Clear screen (Unix-like systems)
                    os.system('clear' if os.name == 'posix' else 'cls')
                
                dashboard_data = dashboard.generate_dashboard_data()
                
                if not args.quiet:
                    dashboard.display_dashboard(dashboard_data)
                
                if args.save:
                    dashboard.save_dashboard_data(dashboard_data)
                
                time.sleep(args.interval)
        else:
            # Single run
            dashboard_data = dashboard.generate_dashboard_data()
            
            if not args.quiet:
                dashboard.display_dashboard(dashboard_data)
            
            if args.save:
                dashboard.save_dashboard_data(dashboard_data)
    
    except KeyboardInterrupt:
        print("\nDashboard stopped by user")
    except Exception as e:
        print(f"Dashboard failed: {e}")
        raise

if __name__ == "__main__":
    main()