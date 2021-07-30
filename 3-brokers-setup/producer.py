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
    bootstrap_servers=['34.66.67.234:9092'], value_serializer=json_serializer)
    # bootstrap_servers=['225.54.188.35.bc.googleusercontent.com:9092'], value_serializer=json_serializer)

    # bootstrap_servers=['localhost:9092'], value_serializer=json_serializer)



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
    # print(registered_user_info)
    producer.send("test", registered_command_info)

    # producer.send("test1", registered_user_info)
    # producer.send("sendMessage", registered_user_info)

        # time.sleep(4)
        # x=x-1

    producer.flush()
    producer.close()