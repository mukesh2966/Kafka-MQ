from confluent_kafka import Consumer
import json




c = Consumer({'bootstrap.servers':'34.66.67.234:9092,34.70.95.183:9093,34.122.1.97:9094',
	'security.protocol':'sasl_ssl',
	'sasl.mechanism':'SCRAM-SHA-512',
	'sasl.username':'demo-consumer',
	'sasl.password':'demokafka',
	'group.id':'consumer-group1',
	'auto.offset.reset':'earliest',
	'ssl.ca.location':'/home/mukesh/kube-demo4/kube-demo/key-used/ca-cert'})


c.subscribe(['ssl-topic'])

while True:
	msg=c.poll(1.0)

	if msg is None:
		continue
	if msg.error():
		print("Consumer error: {}".format(msg.error()))
		continue
	d= json.loads(msg.value().decode("utf-8"))
	print('Received message: {}'.format(json.dumps(d)))



c.close()

