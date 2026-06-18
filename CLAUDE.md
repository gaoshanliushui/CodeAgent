# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a multi-agent software development system built on the MetaGPT framework. The system simulates a team of specialized AI agents (Product Manager, Architect, Developer, Tester, Project Manager) that collaborate to automatically generate complete software projects from natural language requirements.

## Core Architecture

The system implements a multi-agent collaborative workflow where:

1. **Agent Roles**: Five specialized agents work together:
   - Product Manager (PRD creation)
   - Architect (system design)
   - Developer (coding)
   - Tester (unit testing)
   - Project Manager (workflow coordination)

2. **Key Features**:
   - Natural language to complete software project conversion
   - RAG-based knowledge base for reducing code hallucinations
   - Long-context engineering optimization for large projects
   - Private deployment support for various LLMs
   - Human-in-the-loop validation mechanisms

3. **Technical Stack**:
   - Python backend
   - LangChain for LLM integration
   - RAG with FAISS vector database
   - Git workflow integration
   - Docker for private deployment
   - LLM structured output constraints

## Development Setup

Since this is a conceptual framework rather than a working codebase, the development setup involves:

1. Setting up the MetaGPT framework environment
2. Installing required dependencies from requirements.txt (if available)
3. Configuring LLM access (OpenAI, Qwen, Llama3, etc.)
4. Setting up FAISS vector database for knowledge base
5. Configuring Git workflow integration

## Running Tests

Due to the nature of this project being a framework for automated software development, tests would typically involve:
- Testing individual agent behaviors
- Testing workflow coordination
- Evaluating output quality and compliance
- Validating RAG knowledge base integration

To run tests:
1. Navigate to the appropriate test directory (if exists)
2. Execute test suite with pytest or unittest framework
3. Test individual components like agent interactions, RAG retrieval, etc.

## Building and Deployment

For building and deployment:
1. Docker containerization for private deployment
2. Configuration of LLM endpoints
3. Setup of knowledge base vectors with FAISS
4. Git workflow configuration for version control integration

## Key Implementation Areas

The core areas of implementation include:
- Multi-agent role assignment and communication
- Context management for long-running workflows
- RAG system integration for knowledge retrieval
- Structured output constraints for LLM responses
- Git operations and repository management
- Human-in-the-loop validation mechanisms

This system demonstrates advanced AI application in software engineering automation, with particular emphasis on enterprise-grade reliability and compliance.