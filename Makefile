NERU_ENV ?= local

APP := app
project := neru

pipenv := pipenv

manage_py := ${pipenv} run env DJANGO_SETTINGS_MODULE=neru.settings_${NERU_ENV} python3 manage.py

installdeps:
	${pipenv} install

runserver:
	${manage_py} runserver

# https://docs.djangoproject.com/en/1.10/intro/tutorial02/#database-setup
migrate:
	${manage_py} migrate

# https://docs.djangoproject.com/en/1.10/intro/tutorial02/#activating-models
makemigrations:
	${manage_py} makemigrations ${APP}

# Print sql query for migration
sqlmigrate:
	${manage_py} sqlmigrate ${APP} ${target}

createsuperuser:
	${manage_py} createsuperuser

shell:
	${manage_py} shell

manage_py:
	${manage_py} ${command}

check:
	pipenv check
