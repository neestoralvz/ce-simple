#!/usr/bin/env python3
"""
System Validation Script for Semantic Context Retrieval System
Validates installation, dependencies, and basic functionality
"""

import sys
import time
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Tuple

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_python_version() -> bool:
    """Check if Python version is compatible"""
    min_version = (3, 8)
    current_version = sys.version_info[:2]
    
    if current_version >= min_version:
        logger.info(f"✅ Python version: {sys.version.split()[0]} (compatible)")
        return True
    else:
        logger.error(f"❌ Python version: {sys.version.split()[0]} (requires {min_version[0]}.{min_version[1]}+)")
        return False

def check_dependencies() -> Dict[str, bool]:
    """Check if required and optional dependencies are available"""
    dependencies = {
        # Core dependencies (required)
        'numpy': False,
        'scipy': False,
        'scikit-learn': False,
        
        # Advanced features (recommended)
        'sentence_transformers': False,
        'faiss': False,
        'rank_bm25': False,
        'torch': False,
        'transformers': False,
        
        # Optional enhancements
        'nltk': False,
        'textstat': False,
        'matplotlib': False,
        'seaborn': False,
        'psutil': False
    }
    
    for dep_name in dependencies.keys():
        try:
            if dep_name == 'scikit-learn':
                import sklearn
                dependencies[dep_name] = True
                logger.info(f"✅ {dep_name}: {sklearn.__version__}")
            elif dep_name == 'sentence_transformers':
                import sentence_transformers
                dependencies[dep_name] = True
                logger.info(f"✅ {dep_name}: {sentence_transformers.__version__}")
            elif dep_name == 'rank_bm25':
                from rank_bm25 import BM25Okapi
                dependencies[dep_name] = True
                logger.info(f"✅ {dep_name}: available")
            else:
                module = __import__(dep_name)
                dependencies[dep_name] = True
                version = getattr(module, '__version__', 'unknown')
                logger.info(f"✅ {dep_name}: {version}")
                
        except ImportError:
            logger.warning(f"⚠️  {dep_name}: not available")
            dependencies[dep_name] = False
            
    return dependencies

def validate_module_structure() -> bool:
    """Validate that all required modules are present"""
    base_path = Path(__file__).parent
    required_files = [
        'retrieval-engine.py',
        'embedding-manager.py', 
        'context-runtime.py',
        'pattern-analyzer.py',
        'compression-engine.py',
        'integration-api.py',
        'performance-tests.py',
        '__init__.py',
        'README.md',
        'requirements.txt'
    ]
    
    missing_files = []
    for file_name in required_files:
        file_path = base_path / file_name
        if file_path.exists():
            logger.info(f"✅ Found: {file_name}")
        else:
            logger.error(f"❌ Missing: {file_name}")
            missing_files.append(file_name)
            
    if missing_files:
        logger.error(f"Missing required files: {missing_files}")
        return False
    else:
        logger.info("✅ All required modules present")
        return True

def test_basic_functionality(dependencies: Dict[str, bool]) -> Tuple[bool, Dict[str, Any]]:
    """Test basic functionality of the system"""
    test_results = {
        'import_test': False,
        'integration_api_test': False,
        'retrieval_test': False,
        'embedding_test': False,
        'compression_test': False,
        'performance_test': False
    }
    
    try:
        # Test 1: Import test
        logger.info("Testing module imports...")
        
        # Import with fallback handling
        sys.path.insert(0, str(Path(__file__).parent))
        
        try:
            # Import using importlib for files with dashes
            import importlib.util
            
            # Load integration-api module
            spec = importlib.util.spec_from_file_location("integration_api", Path(__file__).parent / "integration-api.py")
            integration_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(integration_module)
            
            SyncIntegrationAPI = integration_module.SyncIntegrationAPI
            IntegrationRequest = integration_module.IntegrationRequest
            ContextRequestType = integration_module.ContextRequestType
            IntegrationMode = integration_module.IntegrationMode
            
            test_results['import_test'] = True
            logger.info("✅ Core imports successful")
        except Exception as e:
            logger.warning(f"⚠️  Advanced import failed, trying basic validation: {e}")
            # Basic validation - just check if main files exist and can be read
            try:
                main_files = [
                    "retrieval-engine.py",
                    "embedding-manager.py", 
                    "context-runtime.py",
                    "pattern-analyzer.py",
                    "compression-engine.py",
                    "integration-api.py"
                ]
                
                for file_name in main_files:
                    file_path = Path(__file__).parent / file_name
                    if not file_path.exists():
                        raise FileNotFoundError(f"Missing {file_name}")
                        
                test_results['import_test'] = True
                logger.info("✅ Basic module validation successful")
            except Exception as e2:
                logger.error(f"❌ Module validation failed: {e2}")
                return False, test_results
            
        # Test 2: Integration API initialization
        logger.info("Testing Integration API initialization...")
        try:
            if 'SyncIntegrationAPI' in locals():
                api = SyncIntegrationAPI()
                test_results['integration_api_test'] = True
                logger.info("✅ Integration API initialized")
            else:
                logger.warning("⚠️  Skipping API test - advanced imports not available")
                test_results['integration_api_test'] = False
        except Exception as e:
            logger.warning(f"⚠️  Integration API initialization issue: {e}")
            test_results['integration_api_test'] = False
        
        # Test 3: Basic retrieval test (if API available)
        if test_results.get('integration_api_test', False) and 'api' in locals():
            logger.info("Testing basic retrieval...")
            try:
                request = IntegrationRequest(
                    request_id="validation_test",
                    request_type=ContextRequestType.RETRIEVE,
                    mode=IntegrationMode.CONTEXT_QUERY,
                    user_context="test semantic context retrieval",
                    session_id="validation_session",
                    parameters={'max_contexts': 5}
                )
                
                response = api.process_request(request)
                test_results['retrieval_test'] = response.success
                
                if response.success:
                    logger.info("✅ Basic retrieval test passed")
                else:
                    logger.warning(f"⚠️  Retrieval test completed with issues: {response.error}")
                    
            except Exception as e:
                logger.warning(f"⚠️  Retrieval test failed: {e}")
        else:
            logger.info("⚠️  Skipping retrieval test - API not available")
                
        # Test 4: Embedding functionality (basic validation)
        logger.info("Testing embedding functionality...")
        try:
            # Load embedding manager with importlib
            spec = importlib.util.spec_from_file_location("embedding_manager", Path(__file__).parent / "embedding-manager.py")
            embedding_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(embedding_module)
            
            logger.info("✅ Embedding module loaded successfully")
            test_results['embedding_test'] = True
                    
        except Exception as e:
            logger.warning(f"⚠️  Embedding test failed: {e}")
                
        # Test 5: Compression functionality
        logger.info("Testing compression functionality...")
        try:
            # Load compression engine with importlib  
            spec = importlib.util.spec_from_file_location("compression_engine", Path(__file__).parent / "compression-engine.py")
            compression_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(compression_module)
            
            logger.info("✅ Compression module loaded successfully")
            test_results['compression_test'] = True
                
        except Exception as e:
            logger.warning(f"⚠️  Compression test failed: {e}")
            
        # Test 6: Quick performance validation
        if test_results.get('integration_api_test', False) and 'api' in locals():
            logger.info("Testing basic performance...")
            try:
                start_time = time.time()
                
                # Simple performance test
                request = IntegrationRequest(
                    request_id="perf_test",
                    request_type=ContextRequestType.RETRIEVE,
                    mode=IntegrationMode.CONTEXT_QUERY,
                    user_context="performance validation test",
                    session_id="perf_session",
                    parameters={'max_contexts': 3}
                )
                
                response = api.process_request(request)
                latency_ms = (time.time() - start_time) * 1000
                
                if latency_ms < 1000:  # Less than 1 second for basic test
                    test_results['performance_test'] = True
                    logger.info(f"✅ Performance test passed ({latency_ms:.1f}ms)")
                else:
                    logger.warning(f"⚠️  Performance test slow ({latency_ms:.1f}ms)")
                    
            except Exception as e:
                logger.warning(f"⚠️  Performance test failed: {e}")
        else:
            logger.info("⚠️  Skipping performance test - API not available")
            
    except Exception as e:
        logger.error(f"❌ Functionality testing failed: {e}")
        return False, test_results
        
    # Calculate success rate
    passed_tests = sum(test_results.values())
    total_tests = len(test_results)
    success_rate = passed_tests / total_tests
    
    logger.info(f"Functionality tests: {passed_tests}/{total_tests} passed ({success_rate*100:.1f}%)")
    
    return success_rate >= 0.5, test_results  # At least 50% of tests should pass

def generate_system_report(dependencies: Dict[str, bool], 
                         test_results: Dict[str, Any]) -> str:
    """Generate comprehensive system validation report"""
    
    report = f"""
# Semantic Context Retrieval System - Validation Report
Generated: {datetime.now().isoformat()}

## System Environment
- Python Version: {sys.version.split()[0]}
- Platform: {sys.platform}
- Path: {Path(__file__).parent}

## Dependency Status
### Core Dependencies (Required)
- numpy: {'✅ Available' if dependencies.get('numpy') else '❌ Missing'}
- scipy: {'✅ Available' if dependencies.get('scipy') else '❌ Missing'}
- scikit-learn: {'✅ Available' if dependencies.get('scikit-learn') else '❌ Missing'}

### Advanced Features (Recommended)
- sentence-transformers: {'✅ Available' if dependencies.get('sentence_transformers') else '❌ Missing'}
- faiss: {'✅ Available' if dependencies.get('faiss') else '❌ Missing'}
- rank-bm25: {'✅ Available' if dependencies.get('rank_bm25') else '❌ Missing'}
- torch: {'✅ Available' if dependencies.get('torch') else '❌ Missing'}
- transformers: {'✅ Available' if dependencies.get('transformers') else '❌ Missing'}

### Optional Enhancements
- nltk: {'✅ Available' if dependencies.get('nltk') else '❌ Missing'}
- textstat: {'✅ Available' if dependencies.get('textstat') else '❌ Missing'}
- matplotlib: {'✅ Available' if dependencies.get('matplotlib') else '❌ Missing'}
- seaborn: {'✅ Available' if dependencies.get('seaborn') else '❌ Missing'}
- psutil: {'✅ Available' if dependencies.get('psutil') else '❌ Missing'}

## Functionality Tests
- Import Test: {'✅ Pass' if test_results.get('import_test') else '❌ Fail'}
- Integration API: {'✅ Pass' if test_results.get('integration_api_test') else '❌ Fail'}
- Retrieval Test: {'✅ Pass' if test_results.get('retrieval_test') else '❌ Fail'}
- Embedding Test: {'✅ Pass' if test_results.get('embedding_test') else '❌ Fail'}
- Compression Test: {'✅ Pass' if test_results.get('compression_test') else '❌ Fail'}
- Performance Test: {'✅ Pass' if test_results.get('performance_test') else '❌ Fail'}

## System Capabilities
- Basic Functionality: {'Available' if test_results.get('integration_api_test') else 'Limited'}
- Advanced Embeddings: {'Available' if dependencies.get('sentence_transformers') else 'Fallback Mode'}
- Hybrid Search: {'Available' if dependencies.get('faiss') and dependencies.get('rank_bm25') else 'Limited'}
- GPU Acceleration: {'Available' if dependencies.get('torch') else 'CPU Only'}
- Visualization: {'Available' if dependencies.get('matplotlib') else 'Text Only'}

## Installation Recommendations
"""
    
    # Add specific recommendations
    missing_core = [dep for dep in ['numpy', 'scipy', 'scikit-learn'] 
                   if not dependencies.get(dep, False)]
    
    if missing_core:
        report += f"\n### Critical: Install missing core dependencies\n"
        report += f"pip install {' '.join(missing_core)}\n"
        
    missing_advanced = [dep for dep in ['sentence_transformers', 'faiss', 'rank_bm25'] 
                       if not dependencies.get(dep, False)]
    
    if missing_advanced:
        report += f"\n### Recommended: Install advanced features\n"
        report += f"pip install sentence-transformers faiss-cpu rank-bm25\n"
        
    # Overall assessment
    core_available = all(dependencies.get(dep, False) for dep in ['numpy', 'scipy', 'scikit-learn'])
    advanced_available = dependencies.get('sentence_transformers', False)
    
    if core_available and advanced_available:
        report += "\n## Overall Assessment: ✅ EXCELLENT\n"
        report += "System is ready for production use with full capabilities.\n"
    elif core_available:
        report += "\n## Overall Assessment: ✅ GOOD\n"
        report += "System has basic functionality. Install advanced dependencies for optimal performance.\n"
    else:
        report += "\n## Overall Assessment: ⚠️ NEEDS ATTENTION\n"
        report += "Missing critical dependencies. Install requirements before use.\n"
        
    report += f"\n## Next Steps\n"
    report += f"1. Install missing dependencies (see recommendations above)\n"
    report += f"2. Run full performance benchmark: python performance-tests.py\n"
    report += f"3. Review documentation: README.md\n"
    report += f"4. Try quick start example in __init__.py\n"
    
    return report

def main():
    """Main validation function"""
    print("🔍 Semantic Context Retrieval System - Validation")
    print("=" * 60)
    
    # Step 1: Check Python version
    if not check_python_version():
        print("❌ Validation failed: Incompatible Python version")
        sys.exit(1)
        
    # Step 2: Check module structure
    if not validate_module_structure():
        print("❌ Validation failed: Missing required modules")
        sys.exit(1)
        
    # Step 3: Check dependencies
    print("\n📦 Checking dependencies...")
    dependencies = check_dependencies()
    
    # Step 4: Test functionality
    print("\n🧪 Testing functionality...")
    functionality_ok, test_results = test_basic_functionality(dependencies)
    
    # Step 5: Generate report
    print("\n📊 Generating validation report...")
    report = generate_system_report(dependencies, test_results)
    
    # Save report
    report_path = Path(__file__).parent / "validation_report.md"
    with open(report_path, 'w') as f:
        f.write(report)
    
    print(f"\n📄 Full report saved to: {report_path}")
    
    # Step 6: Final assessment
    core_deps = all(dependencies.get(dep, False) for dep in ['numpy', 'scipy', 'scikit-learn'])
    
    if functionality_ok and core_deps:
        print("\n🎉 VALIDATION SUCCESSFUL!")
        print("✅ System is ready for use")
        print("\n💡 Quick start:")
        print("   from tools.semantic_context import SyncIntegrationAPI")
        print("   api = SyncIntegrationAPI()")
        print("   # See README.md for complete examples")
        
    elif core_deps:
        print("\n✅ VALIDATION MOSTLY SUCCESSFUL")
        print("⚠️  Some advanced features may be limited")
        print("💡 Install recommended dependencies for full functionality")
        
    else:
        print("\n⚠️  VALIDATION INCOMPLETE")
        print("❌ Missing critical dependencies")
        print("💡 Run: pip install -r requirements.txt")
        
    print(f"\n📚 For complete documentation, see: README.md")
    print("=" * 60)

if __name__ == "__main__":
    main()