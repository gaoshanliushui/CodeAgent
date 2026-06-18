#!/usr/bin/env python3
"""
Multi-Agent Software Development System
Based on MetaGPT framework for automated software development
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from system.orchestrator import MultiAgentSystem

def main():
    """Main function demonstrating the system"""
    print("Multi-Agent Software Development System")
    print("=" * 50)

    # Create the system
    system = MultiAgentSystem()

    # Example requirements
    requirements = "Create a task management application with user authentication and CRUD operations"

    print(f"\nProcessing requirements: {requirements}")
    print("-" * 50)

    # Execute workflow
    result = system.execute_workflow(requirements)

    # Display results
    print("\n📋 Product Requirements Document:")
    import json
    print(json.dumps(result["prd"], indent=2))

    print("\n🏗️  System Architecture:")
    print(json.dumps(result["architecture"], indent=2))

    print("\n💻 Generated Code:")
    print(result["code"])

    print("\n🧪 Generated Tests:")
    print(result["tests"])

    print("\n📊 Workflow Status:")
    print(json.dumps(result["workflow_status"], indent=2))

    print(f"\n📚 Relevant Knowledge Base Items:")
    for item in result["knowledge_base_relevance"]:
        print(f"  • {item}")

    print(f"\n📝 Workflow Log:")
    for entry in result["workflow_log"]:
        print(f"  • {entry['step']} ({entry['agent']}): {entry['result_summary']}")

    print(f"\n✅ Workflow completed successfully!")
    print(f"Timestamp: {result['system_context']['workflow_completed']}")

if __name__ == "__main__":
    main()