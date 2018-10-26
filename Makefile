NERU_ENV ?= local

APP := app
project := neru

manage_py := env DJANGO_SETTINGS_MODULE=neru.settings_${NERU_ENV} pipenv run python3 manage.py

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
