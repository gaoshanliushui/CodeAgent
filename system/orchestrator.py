"""
Main Multi-Agent System Orchestrator
"""

import json
import logging
from typing import Dict, Any, List
from datetime import datetime
from agents.product_manager import ProductManager
from agents.architect import Architect
from agents.developer import Developer
from agents.tester import Tester
from agents.project_manager import ProjectManager
from knowledge_base.knowledge_base import RAGKnowledgeBase

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MultiAgentSystem:
    """Main system orchestrating all agents"""

    def __init__(self):
        self.agents = {
            "product_manager": ProductManager(),
            "architect": Architect(),
            "developer": Developer(),
            "tester": Tester(),
            "project_manager": ProjectManager()
        }
        self.knowledge_base = RAGKnowledgeBase()
        self.workflow_log = []
        self.system_context = {}

    def execute_workflow(self, requirements: str) -> Dict[str, Any]:
        """Execute complete workflow from requirements to deliverables"""
        logger.info(f"Starting workflow for requirements: {requirements}")

        # Initialize workflow context
        self.system_context = {
            "requirements": requirements,
            "workflow_started": datetime.now().isoformat()
        }

        # Step 1: Product Manager creates PRD
        logger.info("Step 1: Product Manager creating PRD")
        prd_result = self.agents["product_manager"].execute(requirements)
        self.workflow_log.append({
            "step": "PRD Creation",
            "agent": "ProductManager",
            "result_summary": "PRD created successfully",
            "timestamp": datetime.now().isoformat()
        })

        # Step 2: Architect designs system
        logger.info("Step 2: Architect designing system")
        arch_result = self.agents["architect"].execute(requirements)
        self.workflow_log.append({
            "step": "Architecture Design",
            "agent": "Architect",
            "result_summary": "System architecture designed",
            "timestamp": datetime.now().isoformat()
        })

        # Step 3: Developer implements code
        logger.info("Step 3: Developer implementing code")
        dev_result = self.agents["developer"].execute(requirements)
        self.workflow_log.append({
            "step": "Implementation",
            "agent": "Developer",
            "result_summary": "Code generated successfully",
            "timestamp": datetime.now().isoformat()
        })

        # Step 4: Tester writes tests
        logger.info("Step 4: Tester writing tests")
        test_result = self.agents["tester"].execute(requirements)
        self.workflow_log.append({
            "step": "Testing",
            "agent": "Tester",
            "result_summary": "Unit tests generated",
            "timestamp": datetime.now().isoformat()
        })

        # Step 5: Project Manager coordinates
        logger.info("Step 5: Project Manager coordinating workflow")
        pm_result = self.agents["project_manager"].execute(requirements)
        self.workflow_log.append({
            "step": "Project Management",
            "agent": "ProjectManager",
            "result_summary": "Workflow coordinated",
            "timestamp": datetime.now().isoformat()
        })

        # Retrieve knowledge base information
        relevant_info = self.knowledge_base.retrieve_relevant_info(requirements)

        # Update system context with results
        self.system_context.update({
            "workflow_completed": datetime.now().isoformat(),
            "final_status": "completed"
        })

        return {
            "requirements": requirements,
            "prd": json.loads(prd_result),
            "architecture": json.loads(arch_result),
            "code": dev_result,
            "tests": test_result,
            "workflow_status": json.loads(pm_result),
            "knowledge_base_relevance": relevant_info,
            "workflow_log": self.workflow_log,
            "system_context": self.system_context
        }

    def get_system_status(self) -> Dict[str, Any]:
        """Get current system status"""
        return {
            "agents_active": len(self.agents),
            "workflow_log_length": len(self.workflow_log),
            "knowledge_base_entries": len(self.knowledge_base.knowledge_base),
            "last_updated": datetime.now().isoformat()
        }

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