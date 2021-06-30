from kafka import KafkaProducer
import json
# from data import get_registered_user
import time
from kafka.admin import KafkaAdminClient, NewTopic
import logging
import sys
# logging.basicConfig(level=logging.DEBUG)



def json_serializer(data):
    return json.dumps(data).encode("utf-8")


# def get_partition(key, all, ava):
#     return 0


# producer = KafkaProducer(
#     bootstrap_servers=['192.168.0.139:9092'], value_serializer=json_serializer, partitioner=get_partition)

producer = KafkaProducer(
    # bootstrap_servers=['35.188.54.225:9092'], value_serializer=json_serializer)
    # bootstrap_servers=['225.54.188.35.bc.googleusercontent.com:9092'], value_serializer=json_serializer)

    bootstrap_servers=['localhost:9092'], value_serializer=json_serializer)



if __name__ == "__main__":

    # admin_client = KafkaAdminClient(
    #     bootstrap_servers="35.188.54.225:9092:9092", 
    #     client_id='test'
    # )

    # topic_list = []
    # topic_list.append(NewTopic(name="example_topic", num_partitions=2, replication_factor=1))
    # admin_client.create_topics(new_topics=topic_list, validate_only=False)

    if(len(sys.argv)!=2):
        print("Usage: python3 producer.py <start/delete/update/restart>")
        sys.exit()
    else:
        print("Sending msg. to consumer")


    # x =1
    # while x>0:
    registered_command_info = {"command":sys.argv[1]}
    print(registered_user_info)
    producer.send("admintome-test", registered_command_info)

    # producer.send("test1", registered_user_info)
    # producer.send("sendMessage", registered_user_info)

        # time.sleep(4)
        # x=x-1

    producer.flush()
    producer.close()



# to run zookeeper docker
# docker run --net=host --name=zookeeper -e ZOOKEEPER_CLIENT_PORT=2181 confluentinc/cp-zookeeper:6.2.0

# to run kafka-server
# JMX_PORT=8004 docker run --net=host --name=kafka -e KAFKA_ZOOKEEPER_CONNECT=localhost:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 confluentinc/cp-kafka:6.2.0


# to run kafka-manager
# bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8084


# to run zookeeper locally
# bin/zookeeper-server-start.sh config/zookeeper.properties

# to run kafka-server locally
# JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties


# worked for bitnami

# zookeeper
# docker run --net=host --name=zookeeper -e ZOOKEEPER_CLIENT_PORT=2181 -e ALLOW_ANONYMOUS_LOGIN=yes bitnami/zookeeper:latest 

# server
# JMX_PORT=8004 docker run --net=host --name=kafka -e KAFKA_ZOOKEEPER_CONNECT=localhost:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181 -e ALLOW_PLAINTEXT_LISTENER=yes bitnami/kafka:latest
# also this
# JMX_PORT=8004 docker run --net=host --name=kafka -e KAFKA_CFG_ZOOKEEPER_CONNECT=localhost:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e ALLOW_PLAINTEXT_LISTENER=yes bitnami/kafka:latest
# also this
# JMX_PORT=8004 docker run --net=host --name=kafka -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e ALLOW_PLAINTEXT_LISTENER=yes bitnami/kafka:latest

# also working for bitnami
# zookeeper
# docker run --net=host --name=zookeeper -e ZOOKEEPER_CLIENT_PORT=2181 -e ALLOW_ANONYMOUS_LOGIN=yes bitnami/zookeeper:latest 

# server
# JMX_PORT=8004 docker run --net=host --name=kafka -e KAFKA_CFG_ZOOKEEPER_CONNECT=localhost:2181 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e ALLOW_PLAINTEXT_LISTENER=yes bitnami/kafka:latest



#!/bin/bash
#Step 1
# keytool -keystore server.keystore.jks -alias localhost -validity 365 -keyalg RSA -genkey
# #Step 2
# openssl req -new -x509 -keyout ca-key -out ca-cert -days 365
# keytool -keystore server.truststore.jks -alias CARoot -import -file ca-cert
# keytool -keystore client.truststore.jks -alias CARoot -import -file ca-cert
# #Step 3
# keytool -keystore server.keystore.jks -alias localhost -certreq -file cert-file
# openssl x509 -req -CA ca-cert -CAkey ca-key -in cert-file -out cert-signed -days 365 -CAcreateserial -passin pass:demokafka
# keytool -keystore server.keystore.jks -alias CARoot -import -file ca-cert
# keytool -keystore server.keystore.jks -alias localhost -import -file cert-signed



# to list the topics
# bin/kafka-topics.sh --list --zookeeper localhost:2181

# to create a topic
# bin/kafka-topics.sh --create --zookeeper localhost:2181 --topic first-topic --partitions 2 --replication-factor 3

# to describe a topic
# bin/kafka-topics.sh --zookeeper localhost:2181 --topic first-topic --describe

# to use console producer
# bin/kafka-console-producer.sh --broker-list localhost:9092,localhost:9093 --topic first-topic

# to use console consumer
# bin/kafka-console-consumer.sh --bootstrap-server localhost:9092,localhost:9093,localhost:9094 --topic first-topic --from-beginning -group first-consumer

# to describe/monitor the consumer groups
# bin/kafka-run-class.sh kafka.admin.ConsumerGroupCommand --bootstrap-server localhost:9092,localhost:9093 --describe --all-groups

# to monitor the offset being produced on topic level
# bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9092,localhost:9093 --topic first-topic

# #
# #Sat Jun 26 13:32:05 IST 2021
# broker.id=0
# version=0
# cluster.id=BTWM-9WkRoG5U6gblg4K0w
