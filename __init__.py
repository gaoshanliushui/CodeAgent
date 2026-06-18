"""
Enhanced Multi-Agent Software Development System Package
Based on MetaGPT framework with custom enhancements
"""

__version__ = "1.0.0"
__author__ = "Enhanced MetaGPT Development Team"

# Import main system components
from .core.enhanced_agents import (
    RAGIntegration,
    ContextOptimizer,
    EnhancedAction,
    WritePRD,
    DesignArchitecture,
    WriteCode,
    WriteTest,
    ProjectManage
)

from .enhanced_main import EnhancedMetaGPTSystem, HumanInLoopValidator

__all__ = [
    'EnhancedMetaGPTSystem',
    'HumanInLoopValidator',
    'RAGIntegration',
    'ContextOptimizer',
    'EnhancedAction',
    'WritePRD',
    'DesignArchitecture',
    'WriteCode',
    'WriteTest',
    'ProjectManage'
]