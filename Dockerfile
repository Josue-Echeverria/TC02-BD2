FROM python:3.11

WORKDIR /opt/app
RUN pip install confluent-kafka
ENV KAFKA_BROKER1='host.docker.internal:29092'
ENV KAFKA_BROKER2='host.docker.internal:29093'
ENV KAFKA_BROKER3='host.docker.internal:29094'
ENV TOPIC='GrupoBases2'

COPY . .
