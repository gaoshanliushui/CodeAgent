#!/usr/bin/env python3
"""
Example usage of the Multi-Agent Software Development System
Demonstrating the complete workflow
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from system.orchestrator import MultiAgentSystem
import json

def demo_workflow():
    """Demonstrate a complete workflow"""

    print("🚀 Multi-Agent Software Development System Demo")
    print("=" * 60)

    # Create the system
    system = MultiAgentSystem()

    # Example requirements from the readme
    requirements = "Create a task management application with user authentication and CRUD operations"

    print(f"\n🎯 Processing Requirements:")
    print(f"   {requirements}")
    print("-" * 60)

    # Execute the workflow
    result = system.execute_workflow(requirements)

    print("\n📋 GENERATED DELIVERABLES:")
    print("=" * 60)

    # Display PRD
    print("\n📄 Product Requirements Document:")
    print(json.dumps(result["prd"], indent=2, ensure_ascii=False))

    # Display Architecture
    print("\n🏗️  System Architecture:")
    print(json.dumps(result["architecture"], indent=2, ensure_ascii=False))

    # Display Generated Code
    print("\n💻 Generated Code:")
    print("=" * 60)
    print(result["code"])

    # Display Tests
    print("\n🧪 Unit Tests:")
    print("=" * 60)
    print(result["tests"])

    # Display Workflow Status
    print("\n📊 Workflow Progress:")
    print(json.dumps(result["workflow_status"], indent=2, ensure_ascii=False))

    # Display Knowledge Base Integration
    print("\n📚 Knowledge Base Integration:")
    print("Relevant guidelines applied:")
    for guideline in result["knowledge_base_relevance"]:
        print(f"   • {guideline}")

    # Display Workflow Log
    print("\n📝 Workflow Execution Log:")
    for i, entry in enumerate(result["workflow_log"], 1):
        print(f"   {i}. {entry['step']} - {entry['agent']}")

    print(f"\n✅ Workflow completed successfully!")
    print(f"   Time: {result['system_context']['workflow_completed']}")
    print(f"   Status: {result['workflow_status']['status']}")

if __name__ == "__main__":
    demo_workflow()