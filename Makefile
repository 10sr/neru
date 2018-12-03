NERU_ENV ?= local
NERU_PORT ?= 9099
NERU_HOST ?= 0.0.0.0

APP := app
project := proj

poetry := poetry

manage_py := ${poetry} run env NERU_ENV=${NERU_ENV} NERU_BASE_DIR=${CURDIR} python3 manage.py

check: test mypy black-check

env:
	env

installdeps:
	${poetry} install

runserver:
	${manage_py} runserver ${NERU_HOST}:${NERU_PORT}

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
	${manage_py} create_admin_user

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


###########
# Docker

docker-build:
	docker build . -t local/neru

# TODO: Add file like docker_local.env
docker-run:
	docker run -p 9099:9099 local/neru


#########
# mypy

mypy:
	${poetry} run mypy --config-file .mypy.ini -p app -p proj -p tests


#########
# black

black:
	${poetry} run black app proj tests

black-check:
	${poetry} run black --check app proj tests
