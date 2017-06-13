default: test

run:
	python inspace/manage.py runserver

clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

test:
	py.test -vv inspace/tests/

test-coverage:
	py.test -vv inspace/tests/ --cov olist-webapp/apps --cov-report=term-missing --cov-report=html

install-local:
	pip install -r requirements/local.txt

install-local:
	pip install -r requirements/test.txt

${VIRTUAL_ENV}/bin/pip-sync:
	pip install pip-tools

pip-tools: ${VIRTUAL_ENV}/bin/pip-sync

pip-compile: pip-tools
	@rm -f requirements/production.txt
	pip-compile requirements/production.in

pip-install: pip-compile
	pip install --upgrade -r requirements/local.txt

pip-upgrade: pip-tools
	pip-compile --upgrade requirements/production.in
