run:
	poetry run start

.PHONY: docs
docs:
	source ./.venv/bin/activate && mkdocs serve


clean: clean-pyc clean-test ## remove all build, test, coverage and Python artifacts
	
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache


coverage: ## check code coverage quickly with the default Python
	coverage run --source quick_zip -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

test: ## run tests quickly with the default Python
	poetry run pytest

test-all: ## run tests on every Python version with tox
	poetry run tox

format:
	poetry run black .

lint: ## check style with flake8
	poetry run flake8 quick_zip tests