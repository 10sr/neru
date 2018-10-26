NERU_ENV ?= local

manage_py := env DJANGO_SETTINGS_MODULE=neru.settings_${NERU_ENV} pipenv run python3 manage.py

runserver:
	${manage_py} runserver

migrate:
	${manage_py} migrate

check:
	pipenv check
