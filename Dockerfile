FROM python:3.11

WORKDIR /opt/app
RUN pip install kafka-python pymongo
ENV KAFKA_BROKER1='kafka:9092'
ENV TOPIC='GrupoBases2'

COPY . .
