# Makefile for Multi-Agent Software Development System

.PHONY: install test run clean docs

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v

run:
	python main.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

docs:
	mkdir -p docs/html
	sphinx-build -b html docs/ docs/html/

lint:
	flake8 .
	mypy .

format:
	black .

.PHONY: all
all: install test