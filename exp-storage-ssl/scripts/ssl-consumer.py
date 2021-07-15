from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
                        "test",
                        bootstrap_servers='34.66.67.234:9092,34.70.95.183:9093,34.122.1.97:9094',
                        security_protocol='SSL',
                        ssl_check_hostname=True,
                        ssl_cafile='consumer-ssl/CARoot.pem',
                        ssl_certfile='consumer-ssl/certificate.pem',
                        ssl_keyfile='consumer-ssl/key.pem',
                        auto_offset_reset="earliest",
                        group_id="consumer-group1")



print("Starting the consumer")
for msg in consumer:
    # for decoding json-object 
    # print("Received Message -{}".format(json.loads(msg.value)))
    # for decoding simple string
    print("Received Message -{}".format(msg.value.decode("utf-8")))