NERU_ENV ?= local

ADMIN_PASSWORD ?= pw

APP := app
project := proj

poetry := poetry

manage_py := ${poetry} run env NERU_ENV=${NERU_ENV} python3 manage.py

installdeps:
	${poetry} install

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

create_admin_user:
	env ADMIN_PASSWORD=${ADMIN_PASSWORD} ${manage_py} create_admin_user

create_local_user:
	${manage_py} create_local_user

shell:
	${manage_py} shell

manage_py:
	${manage_py} ${command}

check:
	${poetry} check

test:
	${manage_py} test
