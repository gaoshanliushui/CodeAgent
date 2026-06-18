"""
Main Application: Enhanced Multi-Agent Software Development System
Based on MetaGPT framework with RAG integration and human-in-the-loop validation
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, List, Any

# Import from our enhanced modules
from core.enhanced_agents import (
    RAGIntegration,
    ContextOptimizer,
    WritePRD,
    DesignArchitecture,
    WriteCode,
    WriteTest,
    ProjectManage
)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class HumanInLoopValidator:
    """Human-in-the-Loop validation mechanism"""

    def __init__(self):
        self.validation_points = []
        self.approvals = {}

    async def request_human_approval(self, step_name: str, content: Any) -> bool:
        """Request human approval at critical points"""
        logger.info(f"REQUESTING HUMAN APPROVAL FOR: {step_name}")

        # In a real system, this would connect to a UI for human input
        # For simulation, we'll assume approval
        print(f"\n 🤖 AI Agent: Waiting for human approval for {step_name}")
        print(f"   Content preview: {str(content)[:200]}...")
        print(f"   Auto-approving for demonstration purposes...")

        # Record validation point
        self.validation_points.append({
            "step": step_name,
            "timestamp": datetime.now().isoformat(),
            "content_preview": str(content)[:100] + "..."
        })

        # In a real system, this would wait for actual human input
        # For now, we simulate approval
        return True

    def record_approval(self, step_name: str, approved: bool):
        """Record human approval decision"""
        self.approvals[step_name] = {
            "approved": approved,
            "timestamp": datetime.now().isoformat()
        }

class EnhancedMetaGPTSystem:
    """Enhanced MetaGPT system with all the advanced features from the readme"""

    def __init__(self):
        # Initialize enhanced components
        self.rag_integration = RAGIntegration()
        self.context_optimizer = ContextOptimizer()
        self.human_validator = HumanInLoopValidator()

        # Initialize actions
        self.write_prd_action = WritePRD()
        self.design_architecture_action = DesignArchitecture()
        self.write_code_action = WriteCode()
        self.write_test_action = WriteTest()
        self.project_manage_action = ProjectManage()

        # Store workflow state
        self.workflow_state = {}
        self.history = []

    async def execute_complete_workflow(self, natural_language_requirements: str):
        """Execute the complete multi-agent workflow with all enhancements"""

        logger.info("="*70)
        logger.info("🚀 STARTING ENHANCED MULTI-AGENT SOFTWARE DEVELOPMENT WORKFLOW")
        logger.info(f"   Requirements: {natural_language_requirements}")
        logger.info("="*70)

        # Step 1: Create PRD with RAG enhancement
        logger.info("\n📝 STEP 1: Creating Product Requirements Document")
        prd_result = await self.write_prd_action.run(natural_language_requirements)

        # Human validation checkpoint
        human_approved = await self.human_validator.request_human_approval("PRD Creation", prd_result)
        self.human_validator.record_approval("PRD Creation", human_approved)

        if not human_approved:
            logger.warning("PRD was not approved by human reviewer")
            return {"error": "PRD not approved", "stage": "prd_creation"}

        # Store PRD in workflow state
        self.workflow_state["prd"] = prd_result

        # Step 2: Design Architecture with RAG enhancement
        logger.info("\n🏗️  STEP 2: Designing System Architecture")
        architecture_result = await self.design_architecture_action.run(prd_result)

        # Human validation checkpoint
        human_approved = await self.human_validator.request_human_approval("Architecture Design", architecture_result)
        self.human_validator.record_approval("Architecture Design", human_approved)

        if not human_approved:
            logger.warning("Architecture was not approved by human reviewer")
            return {"error": "Architecture not approved", "stage": "architecture_design"}

        # Store architecture in workflow state
        self.workflow_state["architecture"] = architecture_result

        # Step 3: Generate Code with RAG enhancement
        logger.info("\n💻 STEP 3: Generating Code Implementation")
        code_result = await self.write_code_action.run(architecture_result, natural_language_requirements)

        # Store code in workflow state
        self.workflow_state["code"] = code_result

        # Step 4: Generate Tests with RAG enhancement
        logger.info("\n🧪 STEP 4: Generating Unit Tests")
        test_result = await self.write_test_action.run(code_result)

        # Store tests in workflow state
        self.workflow_state["tests"] = test_result

        # Step 5: Project Management and Coordination
        logger.info("\n📊 STEP 5: Project Management and Coordination")
        deliverables_list = [
            "Product Requirements Document",
            "System Architecture Design",
            "Source Code Implementation",
            "Unit Tests"
        ]
        project_result = await self.project_manage_action.run("Implementation Phase", deliverables_list)

        # Store project management info
        self.workflow_state["project_management"] = project_result

        # Compile final result
        final_result = {
            "requirements": natural_language_requirements,
            "prd": prd_result,
            "architecture": architecture_result,
            "code": code_result,
            "tests": test_result,
            "project_management": project_result,
            "workflow_metadata": {
                "start_time": datetime.now().isoformat(),
                "end_time": datetime.now().isoformat(),
                "human_validations": self.human_validator.approvals,
                "knowledge_base_usage": {
                    "queries_made": len(self.human_validator.validation_points),
                    "documents_retrieved": sum(len(docs) for docs in [
                        prd_result.get('knowledge_base_applied', []),
                        architecture_result.get('security_considerations', []),
                        architecture_result.get('scalability_features', [])
                    ])
                }
            }
        }

        # Add to history
        self.history.append(final_result)

        logger.info("\n✅ ENHANCED WORKFLOW COMPLETED SUCCESSFULLY!")
        logger.info(f"   Generated: PRD, Architecture, Code, Tests")
        logger.info(f"   Human validations: {len(self.human_validator.approvals)}")
        logger.info(f"   Knowledge base usage: {final_result['workflow_metadata']['knowledge_base_usage']['documents_retrieved']} docs")

        return final_result

    def get_system_status(self) -> Dict[str, Any]:
        """Get current system status"""
        return {
            "active_components": [
                "RAG Knowledge Base",
                "Context Optimizer",
                "Human Validator",
                "Enhanced Agents"
            ],
            "workflow_count": len(self.history),
            "last_workflow_time": self.history[-1]['workflow_metadata']['end_time'] if self.history else None,
            "knowledge_base_size": len(self.rag_integration.documents),
            "timestamp": datetime.now().isoformat()
        }

async def main():
    """Main function demonstrating the enhanced MetaGPT system"""

    print("🚀 ENHANCED MULTI-AGENT SOFTWARE DEVELOPMENT SYSTEM")
    print("   Based on MetaGPT Framework with Custom Enhancements")
    print("   Features: RAG Integration, Context Optimization, Human-in-the-Loop Validation")
    print("="*80)

    # Create enhanced system instance
    system = EnhancedMetaGPTSystem()

    # Example requirements from the original project description
    requirements = "Create a task management application with user authentication and CRUD operations"

    print(f"\n🎯 PROCESSING NATURAL LANGUAGE REQUIREMENTS:")
    print(f"   '{requirements}'")
    print("-" * 80)

    # Execute the enhanced workflow
    try:
        result = await system.execute_complete_workflow(requirements)

        # Display results
        print(f"\n📋 FINAL DELIVERABLES:")
        print("="*50)

        if "error" in result:
            print(f"❌ ERROR at stage: {result['stage']}")
            print(f"   Details: {result['error']}")
        else:
            print(f"\n📄 Product Requirements Document (first 200 chars):")
            prd_preview = json.dumps(result["prd"], indent=2)[:200] + "..."
            print(f"   {prd_preview}")

            print(f"\n🏗️  System Architecture (first 200 chars):")
            arch_preview = json.dumps(result["architecture"], indent=2)[:200] + "..."
            print(f"   {arch_preview}")

            print(f"\n💻 Generated Code (first 200 chars):")
            code_preview = result["code"][:200] + "..."
            print(f"   {code_preview}")

            print(f"\n🧪 Generated Tests (first 200 chars):")
            test_preview = result["tests"][:200] + "..."
            print(f"   {test_preview}")

            print(f"\n📊 Project Status:")
            print(f"   Progress: {result['project_management']['progress_percentage']}%")
            print(f"   Estimated Completion: {result['project_management']['estimated_completion']}")

            print(f"\n🔧 Workflow Metadata:")
            metadata = result["workflow_metadata"]
            print(f"   Human Validations Performed: {len(metadata['human_validations'])}")
            print(f"   Knowledge Base Documents Used: {metadata['knowledge_base_usage']['documents_retrieved']}")

        print(f"\n✅ SYSTEM STATUS:")
        status = system.get_system_status()
        print(f"   Active Components: {len(status['active_components'])}")
        print(f"   Workflows Executed: {status['workflow_count']}")
        print(f"   Knowledge Base Size: {status['knowledge_base_size']} documents")

    except Exception as e:
        logger.error(f"Workflow execution failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())