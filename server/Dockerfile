FROM python:latest

ENV FLASK_APP=server.py

ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install flask mysql-connector-python

EXPOSE 5000

COPY . . 

