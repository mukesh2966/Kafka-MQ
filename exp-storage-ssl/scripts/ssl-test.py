from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='my.server.com',
                          security_protocol='SSL',
                          ssl_check_hostname=True,
                          ssl_cafile='CARoot.pem',
                          ssl_certfile='certificate.pem',
                          ssl_keyfile='key.pem')

# Write hello world to test topic
producer.send("test", bytes("Hello World"))
producer.flush()