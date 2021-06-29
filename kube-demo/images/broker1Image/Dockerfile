FROM bitnami/kafka:latest

COPY /broker1-ssl/ /bitnami/kafka/config/certs
COPY server-1.properties /bitnami/kafka/config/server.properties
COPY kafka_jaas.config /opt/bitnami/kafka/config/kafka_jaas.conf