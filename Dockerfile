FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

COPY init-user-db.sql /docker-entrypoint-initdb.d/init-user-db.sql

RUN mkdir /web
WORKDIR /web
COPY requirements.txt /web/
COPY . /web
ADD . /web

RUN apt-get update
RUN apt-get install -y postgresql
RUN apt-get install -y gcc
RUN apt-get install -y libpq-dev

RUN pip install -r requirements.txt

EXPOSE 8000


CMD ["/web/manage.py", "runserver", "0.0.0.0:8000"]