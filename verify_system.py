#!/usr/bin/env python3
"""
Simple test script to verify the enhanced MetaGPT system works
"""

import asyncio
import sys
import os

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported correctly"""
    print("🔍 Testing module imports...")

    try:
        from core.enhanced_agents import RAGIntegration, WritePRD
        print("✅ Enhanced agents imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import enhanced agents: {e}")
        return False

    try:
        from enhanced_main import EnhancedMetaGPTSystem
        print("✅ Main system imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import main system: {e}")
        return False

    return True

async def test_system():
    """Test the system with a simple example"""
    print("\n🧪 Testing system functionality...")

    try:
        # Create system instance
        system = EnhancedMetaGPTSystem()

        # Test RAG functionality
        rag = system.rag_integration
        results = rag.retrieve_relevant_documents("security best practices", k=2)
        print(f"✅ RAG system working, retrieved {len(results)} documents")

        # Test a simple workflow without full execution
        status = system.get_system_status()
        print(f"✅ System status accessible: {status['workflow_count']} workflows")

        return True
    except Exception as e:
        print(f"❌ System test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    print("🚀 Enhanced MetaGPT System Verification")
    print("="*50)

    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed!")
        return 1

    # Test system functionality
    if not await test_system():
        print("\n❌ System tests failed!")
        return 1

    print("\n✅ All tests passed! Enhanced MetaGPT system is ready.")
    print("\nTo run the full system:")
    print("  python enhanced_main.py")

    return 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)