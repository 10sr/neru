# python:3-onbuild is awesome, but I wont use it for learning purpose
FROM python:3.5.3

# Not work without this!
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /root/app
WORKDIR /root/app

COPY requirements.txt /root/app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /root/app

EXPOSE 9099

# ENTRYPOINT ./manage.py
# CMD ["runserver", "9099"]

CMD ["./manage.py", "runserver", "0.0.0.0:9099"]
