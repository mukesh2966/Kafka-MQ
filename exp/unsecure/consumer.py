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


# Two files were created:
#  - truststore/ca-key -- the private key used later to
#    sign certificates
#  - truststore/ca-cert -- the certificate that will be
#    stored in the trust store in a moment and serve as the certificate
#    authority (CA). Once this certificate has been stored in the trust
#    store, it will be deleted. It can be retrieved from the trust store via:
#    $ keytool -keystore <trust-store-file> -export -alias CARoot -rfc


# Delete intermediate files? They are:
#  - 'ca-cert.srl': CA serial number
#  - 'cert-file': the keystore's certificate signing request
#    (that was fulfilled)
#  - 'cert-signed': the keystore's certificate, signed by the CA, and stored back
#     into the keystore
