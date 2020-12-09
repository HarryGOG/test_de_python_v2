WORKFLOW_MODULE = test_de_python_v2.workflow

REPORT_OUTPUT_DIR = ./target/report
VENV_ACTIVATE_FILE = ./activate_venv

all: info

info:  ## Show this infomation
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

venv:  ## Create virtualenv
	python -m venv venv
	cp -f pip.conf venv/pip.conf
	cp -f pip.conf venv/pip.ini
	. $(VENV_ACTIVATE_FILE); python -m pip install -U -q -c constraints.txt pip pypandoc
	. $(VENV_ACTIVATE_FILE); pip install -U -q -c constraints.txt -e . -r requirements-dev.txt
	. $(VENV_ACTIVATE_FILE); azfr-spark-install-all

update: venv  ## Update dependencies
	cp -f pip.conf venv/pip.conf
	cp -f pip.conf venv/pip.ini
	. $(VENV_ACTIVATE_FILE); pip install -U -q -e . -r requirements-dev.txt -c constraints.txt
	. $(VENV_ACTIVATE_FILE); azfr-spark-install-all

$(IPYTHON_VENV_KERNELS): venv
	. $(VENV_ACTIVATE_FILE); ipython kernel install --prefix venv --name venv


test: venv  ## Run tests
	. $(VENV_ACTIVATE_FILE); pytest $(PYTEST_OPTIONS)


coverage: venv  ## Run tests and compute test coverage
	. $(VENV_ACTIVATE_FILE) && \
	coverage run -m pytest --duration=0 $(PYTEST_OPTIONS) && \
	coverage report



reports: clean-reports  ## Create coverage report
	. $(VENV_ACTIVATE_FILE); coverage run -m pytest \
		--duration=0 \
		--html=$(REPORT_OUTPUT_DIR)/test/pytests.html --self-contained-html \
		--junitxml=$(REPORT_OUTPUT_DIR)/test/junit.xml $(PYTEST_OPTIONS)
	. $(VENV_ACTIVATE_FILE); \
		coverage html -d $(REPORT_OUTPUT_DIR)/coverage_html; \
		coverage xml -o $(REPORT_OUTPUT_DIR)/coverage.xml


clean-reports:  ## Clean reports
	rm -rf $(REPORT_OUTPUT_DIR)


docs: venv clean-docs  ## Generate API documents
	. $(VENV_ACTIVATE_FILE); sphinx-apidoc -T -M --separate -o docs src
	. $(VENV_ACTIVATE_FILE); $(MAKE) -C docs html


clean-docs:  ## Clean API documents
	rm -rf $(DOCUMENT_OUTPUT_DIR)


.PHONY: info all update test coverage cov reports clean-reports package deploy clean distclean