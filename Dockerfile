FROM python:3.5.3

# Django not work without this!
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /root/app
WORKDIR /root/app

COPY requirements.txt /root/app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 9099

COPY . /root/app
RUN git rev-parse HEAD >git_commit_hash.txt

# ENTRYPOINT ./manage.py
# CMD ["runserver", "9099"]

CMD ["python3", "./manage.py", "runserver", "0.0.0.0:9099"]
