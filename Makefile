SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.PHONY: help
help:
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: build-venv ## Create virtual environment and install requirements.
build-venv:
	echo "Creating python3,12 virtual environment."
	python3.12 -m venv .venv/
	.venv/bin/python3.12 -m pip install setuptools
	.venv/bin/python3.12 -m pip install .

.PHONY: run ## Run the main.py file using the virtual environment.
run:
	echo "Running main.py with the virtual environment."
	.venv/bin/python3.12 main.py

.PHONY: clean ## Clean the folder and subfolders
clean:
	echo "Cleaning python3.12 virtual environment."
	rm -rf .venv/
	rm -rf data/
