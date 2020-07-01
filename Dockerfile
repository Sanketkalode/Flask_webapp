FROM python:3.6-alpine

WORKDIR /home/app

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /home/app