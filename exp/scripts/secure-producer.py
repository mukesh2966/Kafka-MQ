from confluent_kafka import Producer
import time
import json


def delivery_report(err, msg):
    if err:
        print(f"Message delivery failed :{str(err)}")
    else:
        print(
            f"Message is delivered to the partition {msg.partition()}; Offset -{msg.offset()}")
        print(f"msg_sent is : {msg.value().decode('utf-8')}")


def run_producer():
    p = Producer({'bootstrap.servers': '34.66.67.234:9092,34.70.95.183:9093,34.122.1.97:9094',
                  'security.protocol': 'sasl_ssl',
                  'sasl.mechanism': 'SCRAM-SHA-512',
                  'sasl.username': 'demo-producer',
                  'sasl.password': 'demokafka',
                  'ssl.ca.location': '/home/mukesh/kube-demo4/kube-demo/key-used/ca-cert',
                  'acks': '-1',  # all
                  'partitioner': 'consistent_random'})
    # batch.num.messages:2
    # linger.ms:5000
    # also something called sticky partitioning, till now not in librdkafka
    # queue.buffering.max.messages:2
    # offsets and other relevant info. will not come, if acks is 0
    # retries:1

    # print(p)

    # topic_info = p.list_topics()

    # print(topic_info.brokers)
    # # will return only those topics to which 'the specified user' has access to
    # print(topic_info.topics)
    # print(topic_info.topics['ssl-topic'].partitions)

    for i in range(1, 6):
        msg_value = {"command": "create"+str(i)}
        msg_header = {"source": b"check"}
        while True:
            try:
                p.poll(timeout=0)
                p.produce(topic='ssl-topic', value=json.dumps(msg_value).encode("utf-8"),
                          headers=msg_header, on_delivery=delivery_report)
                break
            except BufferError as buffer_error:
                print(
                    f"{buffer_error} ::Waiting until the Queue gets some free space.")
                time.sleep(2)
    p.flush()


if __name__ == '__main__':
    run_producer()
