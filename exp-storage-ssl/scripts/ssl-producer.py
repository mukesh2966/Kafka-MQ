from kafka import KafkaProducer
import json
import time
import ssl

import logging
import sys
# logging.basicConfig(level=logging.DEBUG)



def json_serializer(data):
    return json.dumps(data).encode("utf-8")

cert = "/home/mukesh/kube-demo4/exp-storage-ssl/key-used/ca-cert"
key = "/home/mukesh/kube-demo4/exp-storage-ssl/key-used/ca-key"
context = ssl.create_default_context()
context.load_cert_chain(certfile=cert, keyfile=key)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# context = ssl.create_default_context()
# context.options &= ssl.OP_NO_TLSv1
# context.options &= ssl.OP_NO_TLSv1_1
# context.options &= ssl.OP_NO_TLSv1_2
# context.check_hostname = False
# context.verify_mode = ssl.CERT_NONE



producer = KafkaProducer(bootstrap_servers=['34.66.67.234:9092'],
                          security_protocol='SSL',
                          ssl_check_hostname=False,
                          ssl_cafile='producer1-ssl/CARoot.pem',
                          ssl_certfile='producer1-ssl/certificate.pem',
                          ssl_keyfile='producer1-ssl/key.pem', 
                          ssl_password='demokafka',
                        # api_version=(0,10),
                          ssl_context=context)


if __name__ == "__main__":


    if(len(sys.argv)!=2):
        print("Usage: python3 producer.py <start/delete/update/restart>")
        sys.exit()
    else:
        print("Sending msg. to consumer")


    # registered_command_info = {"command":sys.argv[1]}

    producer.send("test", "gone".encode("utf-8"))


    producer.flush()
    producer.close()