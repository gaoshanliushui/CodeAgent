"""
Enhanced MetaGPT Agents with RAG Integration and Optimization
This module extends the core MetaGPT framework with custom functionality
"""

from metagpt.roles import Role
from metagpt.actions import Action
from metagpt.schema import Message
from typing import List, Dict, Any, Optional
import asyncio
import logging
from datetime import datetime
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
import os

logger = logging.getLogger(__name__)

class RAGIntegration:
    """RAG (Retrieval-Augmented Generation) integration for reducing hallucinations"""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.documents = []
        self.embeddings = None
        self.index = None
        self.load_knowledge_base()

    def load_knowledge_base(self):
        """Load enterprise development standards and best practices"""
        # Load pre-defined knowledge base
        self.documents = [
            # Coding Standards
            "Follow PEP 8 style guide for Python code",
            "Use descriptive variable and function names",
            "Write comprehensive docstrings for all functions and classes",
            "Include type hints for better code readability and maintenance",

            # Architecture Patterns
            "Use microservices architecture for scalability",
            "Apply MVC pattern for separation of concerns",
            "Implement event-driven architecture for loose coupling",
            "Follow SOLID principles for maintainable code",

            # Security Guidelines
            "Always validate and sanitize user inputs",
            "Use parameterized queries to prevent SQL injection",
            "Implement proper authentication and authorization",
            "Encrypt sensitive data both in transit and at rest",

            # Performance Best Practices
            "Minimize database queries with efficient indexing",
            "Use caching mechanisms appropriately",
            "Optimize algorithms for time and space complexity",
            "Monitor and profile resource usage regularly",

            # Testing Standards
            "Write unit tests for all business logic",
            "Include integration tests for system components",
            "Perform code coverage analysis",
            "Test both happy path and edge cases",

            # Git Workflow
            "Use feature branching strategy",
            "Write clear and descriptive commit messages",
            "Follow semantic versioning",
            "Perform code reviews before merging",

            # Documentation
            "Maintain up-to-date API documentation",
            "Write clear README files for all modules",
            "Document architectural decisions",
            "Keep user guides current"
        ]

        # Create embeddings for documents
        self.embeddings = self.model.encode(self.documents)

        # Build FAISS index for efficient similarity search
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)  # Inner product (cosine similarity)

        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(self.embeddings)
        self.index.add(self.embeddings.astype('float32'))

    def retrieve_relevant_documents(self, query: str, k: int = 3) -> List[str]:
        """Retrieve most relevant documents for the query"""
        query_embedding = self.model.encode([query])
        faiss.normalize_L2(query_embedding)

        similarities, indices = self.index.search(query_embedding.astype('float32'), k)

        relevant_docs = []
        for idx in indices[0]:
            if idx != -1:  # Valid index
                relevant_docs.append(self.documents[idx])

        return relevant_docs

class ContextOptimizer:
    """Optimizes context management for large projects"""

    def __init__(self):
        self.context_cache = {}
        self.max_context_size = 8000  # Token limit consideration
        self.compression_ratio = 0.7

    def compress_context(self, context: str) -> str:
        """Compress context to manage large inputs"""
        if len(context) <= self.max_context_size:
            return context

        # Simple compression by removing redundant information
        sentences = context.split('. ')
        important_sentences = []

        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in
                   ['important', 'critical', 'requirement', 'must', 'should', 'architecture', 'design']):
                important_sentences.append(sentence)

        compressed = '. '.join(important_sentences)

        # If still too long, truncate while preserving important info
        if len(compressed) > self.max_context_size:
            return compressed[:self.max_context_size] + "... (context truncated)"
        else:
            return compressed

    def update_context(self, key: str, content: str):
        """Update context with new content"""
        self.context_cache[key] = content

    def get_context(self, key: str) -> str:
        """Retrieve context by key"""
        return self.context_cache.get(key, "")

class EnhancedAction(Action):
    """Base class for enhanced actions with RAG and context optimization"""

    def __init__(self):
        super().__init__()
        self.rag_integration = RAGIntegration()
        self.context_optimizer = ContextOptimizer()

    def enhance_with_rag(self, query: str, base_content: str) -> str:
        """Enhance content with relevant knowledge from RAG"""
        relevant_docs = self.rag_integration.retrieve_relevant_documents(query)
        if relevant_docs:
            enhanced = f"CONTEXT FROM KNOWLEDGE BASE:\n"
            for i, doc in enumerate(relevant_docs, 1):
                enhanced += f"{i}. {doc}\n"
            enhanced += f"\nORIGINAL CONTENT:\n{base_content}"
            return enhanced
        return base_content

class WritePRD(EnhancedAction):
    """Enhanced PRD writing with RAG and context optimization"""

    async def run(self, requirements: str):
        """Generate PRD with knowledge base integration"""
        logger.info(f"Creating PRD with requirements: {requirements[:100]}...")

        # Compress if needed
        optimized_requirements = self.context_optimizer.compress_context(requirements)

        # Enhance with RAG knowledge
        enhanced_reqs = self.enhance_with_rag("product requirements document", optimized_requirements)

        # Generate PRD content
        prd_content = {
            "title": f"Product Requirements Document for '{requirements[:50]}...'",
            "description": f"Requirements: {requirements}",
            "features": [
                "Feature 1: Core functionality aligned with business goals",
                "Feature 2: Advanced features for enhanced user experience",
                "Feature 3: Integration capabilities with external systems"
            ],
            "technical_requirements": [
                "Scalable architecture supporting high loads",
                "Security measures following industry standards",
                "Performance benchmarks and monitoring"
            ],
            "success_criteria": [
                "Meets all functional requirements",
                "Achieves performance targets",
                "Follows security and compliance standards"
            ],
            "timeline": "4-6 weeks",
            "deliverables": [
                "Complete product specification",
                "Technical architecture document",
                "API documentation",
                "Deployment guide"
            ],
            "knowledge_base_applied": self.rag_integration.retrieve_relevant_documents("product requirements document")
        }

        return prd_content

class DesignArchitecture(EnhancedAction):
    """Enhanced architecture design with RAG integration"""

    async def run(self, prd_content: dict):
        """Design architecture based on PRD with knowledge base integration"""
        requirements = prd_content.get("description", "")
        logger.info(f"Designing architecture for: {requirements[:100]}...")

        # Enhance with architectural patterns from RAG
        enhanced_reqs = self.enhance_with_rag("system architecture", requirements)

        architecture = {
            "overview": "Scalable microservices architecture with clean separation of concerns",
            "components": [
                {
                    "name": "Frontend Layer",
                    "technology": "React/Next.js or Vue.js",
                    "responsibilities": "User interface and client-side interactions",
                    "best_practices": self.rag_integration.retrieve_relevant_documents("frontend architecture")
                },
                {
                    "name": "Backend Services",
                    "technology": "Python/FastAPI or Node.js/Express",
                    "responsibilities": "Business logic, APIs, and service orchestration",
                    "best_practices": self.rag_integration.retrieve_relevant_documents("backend architecture")
                },
                {
                    "name": "Data Layer",
                    "technology": "PostgreSQL/Redis",
                    "responsibilities": "Data persistence and caching",
                    "best_practices": self.rag_integration.retrieve_relevant_documents("database architecture")
                }
            ],
            "integration_patterns": [
                "API Gateway for unified access",
                "Message queues for asynchronous communication",
                "Event sourcing for audit trails"
            ],
            "security_considerations": self.rag_integration.retrieve_relevant_documents("security architecture"),
            "scalability_features": self.rag_integration.retrieve_relevant_documents("scalable architecture")
        }

        return architecture

class WriteCode(EnhancedAction):
    """Enhanced code writing with best practices integration"""

    async def run(self, architecture: dict, requirements: str):
        """Generate code following architectural guidelines and best practices"""
        logger.info("Generating code with architectural constraints...")

        # Get best practices from RAG
        coding_standards = self.rag_integration.retrieve_relevant_documents("coding standards")
        security_guidelines = self.rag_integration.retrieve_relevant_documents("security guidelines")

        # Generate example implementation
        code_content = f'''
"""
Generated code based on architecture and requirements
'''

# Apply coding standards
        standards_comment = "\\n".join([f"# {standard}" for standard in coding_standards[:3]])

        code_content += f'''{standards_comment}

class TaskManager:
    """Task management system implementation"""

    def __init__(self):
        """Initialize the task manager"""
        self.tasks = []
        self.users = []

    def create_task(self, title: str, description: str, assignee: str):
        """Create a new task with validation"""
        # Security: Input validation
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        task = {{
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "assignee": assignee,
            "status": "pending",
            "created_at": "{datetime.now().isoformat()}"
        }}
        self.tasks.append(task)
        return task

    def get_task(self, task_id: int):
        """Retrieve a task by ID"""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def update_task(self, task_id: int, **updates):
        """Update task properties"""
        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Task with ID {{task_id}} not found")

        for key, value in updates.items():
            if key in ["title", "description", "assignee", "status"]:
                task[key] = value

        return task

    def delete_task(self, task_id: int):
        """Delete a task"""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

# Security and performance considerations applied
security_comments = "\\n".join([f"# Security: {guideline}" for guideline in security_guidelines[:3]])
code_content += f'''

{security_comments}

if __name__ == "__main__":
    # Example usage
    tm = TaskManager()
    task = tm.create_task("Sample Task", "This is a sample task", "user1")
    print(f"Created task: {{task}}")
'''

        return code_content

class WriteTest(EnhancedAction):
    """Enhanced test generation with coverage optimization"""

    async def run(self, code_content: str):
        """Generate comprehensive tests for the provided code"""
        logger.info("Generating tests for provided code...")

        # Get testing standards from RAG
        testing_standards = self.rag_integration.retrieve_relevant_documents("testing standards")

        test_content = f'''
"""
Unit tests for generated code
"""

import unittest
from io import StringIO
import sys
import os
# Import the generated code (assuming it's in the same directory)
# from generated_module import TaskManager

class TestTaskManager(unittest.TestCase):
    """Test cases for TaskManager class"""

    def setUp(self):
        """Setup test fixtures before each test method."""
        self.tm = TaskManager()  # Assuming TaskManager class exists

    def test_create_task_success(self):
        """Test successful task creation"""
        task = self.tm.create_task("Test Task", "Test Description", "test_user")
        self.assertIsNotNone(task)
        self.assertEqual(task["title"], "Test Task")
        self.assertEqual(task["assignee"], "test_user")

    def test_get_task_existing(self):
        """Test retrieving an existing task"""
        task = self.tm.create_task("Get Test", "Description", "user")
        retrieved = self.tm.get_task(task["id"])
        self.assertEqual(retrieved["id"], task["id"])

    def test_get_task_nonexistent(self):
        """Test retrieving a non-existent task"""
        result = self.tm.get_task(999)
        self.assertIsNone(result)

    def test_update_task(self):
        """Test updating task properties"""
        task = self.tm.create_task("Update Test", "Description", "user")
        updated = self.tm.update_task(task["id"], status="completed")
        self.assertEqual(updated["status"], "completed")

    def test_delete_task(self):
        """Test deleting a task"""
        task = self.tm.create_task("Delete Test", "Description", "user")
        initial_count = len(self.tm.tasks)
        success = self.tm.delete_task(task["id"])
        final_count = len(self.tm.tasks)

        self.assertTrue(success)
        self.assertEqual(final_count, initial_count - 1)

    def test_input_validation(self):
        """Test input validation"""
        with self.assertRaises(ValueError):
            self.tm.create_task("", "Description", "user")

    def tearDown(self):
        """Clean up after each test method."""
        pass

if __name__ == "__main__":
    unittest.main()
'''

        return test_content

class ProjectManage(EnhancedAction):
    """Enhanced project management with milestone tracking"""

    async def run(self, current_status: str, deliverables: List[str]):
        """Manage project workflow and milestones"""
        logger.info("Managing project workflow...")

        workflow_content = {
            "status": "in_progress",
            "current_phase": "implementation",
            "milestones": [
                {"name": "Requirements Analysis", "status": "completed", "date": str(datetime.now())},
                {"name": "Architecture Design", "status": "completed", "date": str(datetime.now())},
                {"name": "Implementation", "status": "in_progress", "date": str(datetime.now())},
                {"name": "Testing", "status": "pending", "date": ""},
                {"name": "Documentation", "status": "pending", "date": ""},
                {"name": "Deployment", "status": "pending", "date": ""}
            ],
            "progress_percentage": 50,
            "estimated_completion": "2 days",
            "dependencies": [
                "PRD approval before implementation",
                "Architecture sign-off before coding",
                "Code review completion before testing"
            ],
            "risks": [
                "Scope creep",
                "Resource constraints",
                "Technology limitations"
            ],
            "recommendations": self.rag_integration.retrieve_relevant_documents("project management")
        }

        return workflow_content