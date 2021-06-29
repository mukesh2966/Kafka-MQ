FROM bitnami/kafka:latest

COPY /broker2-ssl/ /bitnami/kafka/config/certs
COPY server-2.properties /bitnami/kafka/config/server.properties
COPY kafka_jaas.config /opt/bitnami/kafka/config/kafka_jaas.conf