FROM python:3.11

WORKDIR /opt/app
RUN pip install kafka-python pymongo
ENV KAFKA_BROKER1='kafka:9092'
ENV TOPIC='GrupoBases2'

ENV MONGO_HOST='mongo' 
ENV MONGO_PORT='27017'  
ENV MONGO_USER='root' 
ENV MONGO_DB='GrupoBases2'
ENV MONGO_PASSWORD='password'

COPY . .
