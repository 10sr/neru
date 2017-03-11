FROM python:3.5.3

EXPOSE 9099

ENTRYPOINT ./manage.py
CMD ["runserver", "9099"]
