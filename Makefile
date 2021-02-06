# Makefile
VIRTUALENV := python3 -m venv
PIP := venv/bin/pip

all: create venv install run
 
create:
	$(VIRTUALENV) venv

install:
	. venv/bin/activate; \
	pip install -r requirements.txt; \
	deactivate;

venv:
	test -d venv || virtualenv -p python3 --no-site-packages venv

run:
	. venv/bin/activate; \
	cd todo; \
	python manage.py migrate; \
	python manage.py test api.tests --noinput; \
	python manage.py runserver;

clean: 
	rm -rf venv; \
	find . -name "*.pyc" -delete;