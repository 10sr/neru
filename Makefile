NERU_ENV ?= local

runserver:
	env DJANGO_SETTINGS_MODULE=neru.settings_${NERU_ENV} pipenv run python3 manage.py runserver

check:
	pipenv check
