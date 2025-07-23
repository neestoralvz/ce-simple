#!/usr/bin/env python3
"""
Simple Test Daemon - Debug Version
Test basic daemon functionality without complex templates
"""

import json
import time
import logging
from datetime import datetime
from pathlib import Path

class SimpleTestDaemon:
    def __init__(self, daemon_type="test", daemon_id="test123"):
        self.base_path = Path(__file__).parent.parent
        self.daemon_id = daemon_id
        self.daemon_type = daemon_type
        self.cycle_count = 0
        self.success_count = 0
        self.setup_logging()
        
    def setup_logging(self):
        log_dir = self.base_path / "results" / "automation"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / f"simple_test_{datetime.now().strftime('%Y%m%d-%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
        )
        self.logger = logging.getLogger('SimpleTestDaemon')
        
    def execute_test_cycle(self):
        """Execute a simple test cycle"""
        self.cycle_count += 1
        
        # Simulate work
        time.sleep(1)
        
        # Success based on cycle number (80% success rate)
        success = self.cycle_count % 5 != 0
        
        if success:
            self.success_count += 1
            self.logger.info(f"Cycle {self.cycle_count} SUCCESS")
        else:
            self.logger.warning(f"Cycle {self.cycle_count} FAILED")
            
        return success
        
    def send_heartbeat(self):
        """Send simple heartbeat"""
        try:
            comm_dir = self.base_path / "results" / "automation" / "communication"
            comm_dir.mkdir(parents=True, exist_ok=True)
            
            heartbeat_file = comm_dir / "simple_heartbeat.json"
            
            heartbeat_data = {
                self.daemon_id: {
                    'timestamp': datetime.now().isoformat(),
                    'cycle_count': self.cycle_count,
                    'success_count': self.success_count,
                    'success_rate': self.success_count / max(1, self.cycle_count),
                    'health_score': min(1.0, self.success_count / max(1, self.cycle_count))
                }
            }
            
            with open(heartbeat_file, 'w') as f:
                json.dump(heartbeat_data, f, indent=2)
                
            self.logger.info(f"Heartbeat sent - Success rate: {self.success_count / max(1, self.cycle_count) * 100:.1f}%")
            
        except Exception as e:
            self.logger.error(f"Heartbeat failed: {e}")
            
    def run_test_daemon(self, max_cycles=5):
        """Run simple test daemon"""
        self.logger.info(f"Starting simple test daemon (Type: {self.daemon_type}, ID: {self.daemon_id})")
        
        for cycle in range(max_cycles):
            success = self.execute_test_cycle()
            self.send_heartbeat()
            
            if cycle < max_cycles - 1:
                time.sleep(2)
                
        final_success_rate = self.success_count / max(1, self.cycle_count) * 100
        self.logger.info(f"Test daemon completed - Final success rate: {final_success_rate:.1f}%")
        
        return final_success_rate

if __name__ == "__main__":
    daemon = SimpleTestDaemon("test_governance", "simple_test_001")
    success_rate = daemon.run_test_daemon()
    print(f"✅ Simple Test Daemon Success Rate: {success_rate:.1f}%")
    exit(0 if success_rate >= 70 else 1)