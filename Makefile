default: test

clean: clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

run:
	python inspace/manage.py runserver

migrate:
	python inspace/manage.py migrate

migrations:
	python inspace/manage.py makemigrations

shell:
	python inspace/manage.py shell

collectstatic:
	python inspace/manage.py collectstatic

test:
	pytest inspace

test-coverage:
	pytest inspace --cov-report=html

install: pip-tools
	pip-sync requirements.txt

install-dev: pip-tools
	pip-sync requirements.txt requirements-dev.txt

${VIRTUAL_ENV}/bin/pip-sync:
	pip install pip-tools

pip-tools: ${VIRTUAL_ENV}/bin/pip-sync

lock: pip-tools
	pip-compile --generate-hashes --output-file requirements.txt requirements/base.in

lock-dev: pip-tools
	pip-compile --generate-hashes --output-file requirements-dev.txt requirements/dev.in
