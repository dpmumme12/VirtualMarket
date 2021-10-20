###########
# BUILDER #
###########

# pull official base image
FROM ubuntu:20.04

WORKDIR /usr/src/app

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get -y upgrade

RUN apt-get install -y python3
RUN apt-get install -y python3-pip


RUN pip3 install --upgrade pip


# install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . $APP_HOME

