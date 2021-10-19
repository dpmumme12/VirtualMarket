###########
# BUILDER #
###########

# pull official base image
FROM python:3.10-alpine as builder

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade
RUN apk add postgresql-dev \
    gcc \
    musl-dev \
    libc-dev \
    openldap \
    libcurl \
    gpgme-dev \
    python3-dev 

RUN pip install --upgrade pip
COPY . .

# install dependencies
COPY requirements.txt requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

FROM python:3.10-alpine

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# install dependencies
RUN apk add libpq

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt requirements.txt
RUN pip install --no-cache /wheels/*

COPY . $APP_HOME