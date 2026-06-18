"""
Unit tests for the Multi-Agent System
"""

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.product_manager import ProductManager
from agents.architect import Architect
from agents.developer import Developer
from agents.tester import Tester
from agents.project_manager import ProjectManager
from knowledge_base.knowledge_base import RAGKnowledgeBase
from system.orchestrator import MultiAgentSystem

class TestAgents(unittest.TestCase):

    def setUp(self):
        self.product_manager = ProductManager()
        self.architect = Architect()
        self.developer = Developer()
        self.tester = Tester()
        self.project_manager = ProjectManager()
        self.knowledge_base = RAGKnowledgeBase()

    def test_product_manager_execute(self):
        result = self.product_manager.execute("Test requirements")
        self.assertIsInstance(result, str)
        self.assertIn("Project for", result)

    def test_architect_execute(self):
        result = self.architect.execute("Test requirements")
        self.assertIsInstance(result, str)
        self.assertIn("overview", result)

    def test_developer_execute(self):
        result = self.developer.execute("Test requirements")
        self.assertIsInstance(result, str)
        self.assertIn("Generated code", result)

    def test_tester_execute(self):
        result = self.tester.execute("Test requirements")
        self.assertIsInstance(result, str)
        self.assertIn("Unit tests", result)

    def test_project_manager_execute(self):
        result = self.project_manager.execute("Test requirements")
        self.assertIsInstance(result, str)
        self.assertIn("status", result)

    def test_knowledge_base_retrieve(self):
        result = self.knowledge_base.retrieve_relevant_info("coding standards")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

class TestMultiAgentSystem(unittest.TestCase):

    def setUp(self):
        self.system = MultiAgentSystem()

    def test_system_initialization(self):
        self.assertIsNotNone(self.system.agents)
        self.assertIsNotNone(self.system.knowledge_base)
        self.assertEqual(len(self.system.agents), 5)

    def test_system_status(self):
        status = self.system.get_system_status()
        self.assertIn("agents_active", status)
        self.assertIn("workflow_log_length", status)

if __name__ == '__main__':
    unittest.main()