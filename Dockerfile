FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

COPY init-user-db.sql /docker-entrypoint-initdb.d/init-user-db.sql

RUN mkdir /web
WORKDIR /web
COPY requirements.txt /web/
COPY . /web
ADD . /web

RUN apt-get update -qq && apt-get install -y -qq \
    # std libs
    git less nano curl gcc \
    ca-certificates \
    wget build-essential\
    # python basic libs
    python3.8-dev gettext \
    # geodjango
    gdal-bin binutils libproj-dev libgdal-dev \
    # postgresql
    libpq-dev postgresql-client && \
    apt-get clean all && rm -rf /var/apt/lists/* && rm -rf /var/cache/apt/*

# install pip
RUN wget https://bootstrap.pypa.io/get-pip.py && python3.8 get-pip.py && rm get-pip.py
RUN pip3 install --no-cache-dir setuptools wheel -U


RUN pip install -r requirements.txt

EXPOSE 8000


CMD ["/web/manage.py", "runserver", "0.0.0.0:8000"]