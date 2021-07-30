from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "test",
        bootstrap_servers="34.66.67.234:9092",
        # bootstrap_servers="225.54.188.35.bc.googleusercontent.com:9092",
        # bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest",
        group_id="consumer-group-a")
    print("Starting the consumer")
    for msg in consumer:
    	# for decoding json-object 
        # print("Received Message -{}".format(json.loads(msg.value)))
        # for decoding simple string
        print("Received Message -{}".format(msg.value.decode("utf-8")))