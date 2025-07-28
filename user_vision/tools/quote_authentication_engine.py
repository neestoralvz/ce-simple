#!/usr/bin/env python3
"""
User Vision Quote Authentication Engine
Validates all user_vision/ content against source conversations
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path

class QuoteAuthenticationEngine:
    """Validates user_vision/ quotes against source conversations"""
    
    def __init__(self):
        self.base_path = Path("/Users/nalve/ce-simple")
        self.conversations_path = self.base_path / "narratives/raw/conversations"
        self.user_vision_path = self.base_path / "user_vision"
        self.violations_log = self.base_path / "user_vision/tools/violations.log"
        
    def load_conversation_sources(self):
        """Load all conversation files as source authority"""
        sources = {}
        for conv_file in self.conversations_path.glob("*.md"):
            with open(conv_file, 'r', encoding='utf-8') as f:
                sources[conv_file.name] = f.read()
        return sources
    
    def extract_quotes_from_vision(self, vision_file):
        """Extract all quoted user voice from vision document"""
        with open(vision_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all user voice quotes (between > and newline)
        quotes = re.findall(r'> (.+?)(?:\n|$)', content, re.MULTILINE)
        
        # Also find quotes in **User Voice**: sections
        user_voice_quotes = re.findall(r'\*\*User Voice\*\*:\s*\n> (.+?)(?:\n\n|\n\*\*|$)', 
                                      content, re.MULTILINE | re.DOTALL)
        
        return quotes + user_voice_quotes
    
    def validate_quote_authenticity(self, quote, sources):
        """Validate quote exists exactly in source conversations"""
        quote_clean = quote.strip()
        
        for source_file, source_content in sources.items():
            if quote_clean in source_content:
                return {
                    "valid": True,
                    "source_file": source_file,
                    "quote": quote_clean
                }
        
        return {
            "valid": False,
            "source_file": None,
            "quote": quote_clean,
            "violation": "Quote not found in any source conversation"
        }
    
    def audit_vision_document(self, vision_file):
        """Complete authenticity audit of vision document"""
        sources = self.load_conversation_sources()
        quotes = self.extract_quotes_from_vision(vision_file)
        
        results = {
            "file": str(vision_file),
            "total_quotes": len(quotes),
            "valid_quotes": 0,
            "violations": [],
            "authenticity_score": 0.0,
            "timestamp": datetime.now().isoformat()
        }
        
        for quote in quotes:
            validation = self.validate_quote_authenticity(quote, sources)
            
            if validation["valid"]:
                results["valid_quotes"] += 1
            else:
                results["violations"].append(validation)
                self.log_violation(vision_file, validation)
        
        if results["total_quotes"] > 0:
            results["authenticity_score"] = results["valid_quotes"] / results["total_quotes"]
        
        return results
    
    def audit_all_vision_documents(self):
        """Complete authenticity audit of all user_vision/ documents"""
        audit_results = {
            "audit_timestamp": datetime.now().isoformat(),
            "total_files": 0,
            "files_audited": [],
            "overall_authenticity": 0.0,
            "critical_violations": 0,
            "status": "UNKNOWN"
        }
        
        vision_files = list(self.user_vision_path.glob("**/*.md"))
        audit_results["total_files"] = len(vision_files)
        
        total_score = 0.0
        
        for vision_file in vision_files:
            if vision_file.name.startswith("CONTAMINATION_"):
                continue  # Skip protection system files
                
            file_audit = self.audit_vision_document(vision_file)
            audit_results["files_audited"].append(file_audit)
            
            total_score += file_audit["authenticity_score"]
            audit_results["critical_violations"] += len(file_audit["violations"])
        
        if len(audit_results["files_audited"]) > 0:
            audit_results["overall_authenticity"] = total_score / len(audit_results["files_audited"])
        
        # Determine protection status
        if audit_results["overall_authenticity"] == 1.0:
            audit_results["status"] = "PURE"
        elif audit_results["overall_authenticity"] >= 0.95:
            audit_results["status"] = "MINOR_CONTAMINATION"
        else:
            audit_results["status"] = "CRITICAL_CONTAMINATION"
        
        return audit_results
    
    def log_violation(self, vision_file, violation):
        """Log contamination violation"""
        violation_entry = {
            "timestamp": datetime.now().isoformat(),
            "file": str(vision_file),
            "violation_type": "QUOTE_AUTHENTICATION_FAILURE",
            "quote": violation["quote"],
            "severity": "CRITICAL",
            "action_required": "IMMEDIATE_CORRECTION"
        }
        
        os.makedirs(self.violations_log.parent, exist_ok=True)
        with open(self.violations_log, 'a') as f:
            f.write(json.dumps(violation_entry) + "\n")
    
    def block_operation_if_contaminated(self, target_file, proposed_content):
        """Block operations that would contaminate user_vision/"""
        if not str(target_file).startswith(str(self.user_vision_path)):
            return True  # Allow operations outside user_vision/
        
        # Extract quotes from proposed content
        quotes = re.findall(r'> (.+?)(?:\n|$)', proposed_content, re.MULTILINE)
        sources = self.load_conversation_sources()
        
        for quote in quotes:
            validation = self.validate_quote_authenticity(quote, sources)
            if not validation["valid"]:
                self.log_violation(target_file, validation)
                print(f"🚫 CONTAMINATION BLOCKED: Quote not found in conversations")
                print(f"   File: {target_file}")
                print(f"   Quote: {quote}")
                return False
        
        return True
    
    def generate_purity_report(self):
        """Generate comprehensive purity status report"""
        audit = self.audit_all_vision_documents()
        
        report = f"""
# User Vision Purity Report

**Audit Timestamp**: {audit['audit_timestamp']}
**Overall Status**: {audit['status']}
**Authenticity Score**: {audit['overall_authenticity']:.2%}

## Summary
- **Total Files**: {audit['total_files']}
- **Files Audited**: {len(audit['files_audited'])}
- **Critical Violations**: {audit['critical_violations']}

## File Details
"""
        
        for file_audit in audit["files_audited"]:
            status_emoji = "✅" if file_audit["authenticity_score"] == 1.0 else "⚠️"
            report += f"""
### {status_emoji} {file_audit['file']}
- **Total Quotes**: {file_audit['total_quotes']}
- **Valid Quotes**: {file_audit['valid_quotes']}
- **Authenticity**: {file_audit['authenticity_score']:.2%}
- **Violations**: {len(file_audit['violations'])}
"""
            
            if file_audit['violations']:
                report += "\n**Violations Found**:\n"
                for violation in file_audit['violations']:
                    report += f"- `{violation['quote'][:50]}...`\n"
        
        return report

if __name__ == "__main__":
    engine = QuoteAuthenticationEngine()
    
    print("🔍 User Vision Quote Authentication Engine")
    print("=" * 50)
    
    # Run complete audit
    audit_results = engine.audit_all_vision_documents()
    
    print(f"Overall Authenticity: {audit_results['overall_authenticity']:.2%}")
    print(f"Status: {audit_results['status']}")
    print(f"Critical Violations: {audit_results['critical_violations']}")
    
    if audit_results['critical_violations'] > 0:
        print("\n🚫 CONTAMINATION DETECTED - Manual review required")
    else:
        print("\n✅ USER VISION PURITY CONFIRMED")
    
    # Generate detailed report
    report = engine.generate_purity_report()
    
    report_file = Path("/Users/nalve/ce-simple/user_vision/tools/purity_report.md")
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(f"\n📊 Detailed report saved to: {report_file}")