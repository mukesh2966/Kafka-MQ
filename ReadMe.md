# ReadMe File

#### This file is also included as docker-setup.properties in docker-demo/setup folder.

#### For setting up kafka cluster in docker environment, you could either go through this ReadMe or docker-demo/setup/docker-setup.properties file.

#### For setting up kafka cluster in k8s environment, you should go to kube-demo/setup/kube-setup.properties file.

###### download the kafka package kafka_2.13-2.8.0 link https://www.apache.org/dyn/closer.cgi?path=/kafka/2.8.0/kafka_2.13-2.8.0.tgz

###### that package and everything is also uploaded in the github repo

###### NO NEED TO DOWNLOAD THE ENTIRE REPO, repo is ther just for reference. You could just copy the files inside the config folder and scripts folder itself.

###### if you do not want to create the keystores and trustores for yourself, you can also use the certs and key-used folder.

###### NOTE : ca.key is private key and ca.cert is the public key.

###### for running secure-producer and secure-consumer.py, you would need librdkafka and confluent_kafka packages.

###### confluent_kafka is just a wrapper around librdkafka

###### also, I have used librdkafka by installing latest from brew, and python 3.93.

###### there were some issues with the version compatibility when using these dependencies some other way.(like confluent_kafka was unable to detect librdkafka)

###### first we need to create the required certificates

## Below are the Example steps to implement CA, truststore and keystore for zookeeper SSL security

#### 𝟏. 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐂𝐀 ==

openssl req -new -x509 -keyout ca-key -out ca-cert -days 3650

#### 𝟐. 𝐂𝐫𝐞𝐚𝐭𝐞 𝐓𝐫𝐮𝐬𝐭𝐬𝐭𝐨𝐫𝐞 ==

keytool -keystore kafka.zookeeper.truststore.jks -alias ca-cert -import -file ca-cert

#### 𝟑. 𝐂𝐫𝐞𝐚𝐭𝐞 𝐊𝐞𝐲𝐬𝐭𝐨𝐫𝐞 ==

keytool -keystore kafka.zookeeper.keystore.jks -alias zookeeper -validity 3650 -genkey -keyalg RSA -ext SAN=dns:localhost

#### 𝟒. 𝐂𝐫𝐞𝐚𝐭𝐞 𝐜𝐞𝐫𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐞 𝐬𝐢𝐠𝐧𝐢𝐧𝐠 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 (𝐂𝐒𝐑) ==

keytool -keystore kafka.zookeeper.keystore.jks -alias zookeeper -certreq -file ca-request-zookeeper

#### 𝟓. 𝐒𝐢𝐠𝐧 𝐭𝐡𝐞 𝐂𝐒𝐑 ==

openssl x509 -req -CA ca-cert -CAkey ca-key -in ca-request-zookeeper -out ca-signed-zookeeper -days 3650 -CAcreateserial

#### 𝟔. 𝐈𝐦𝐩𝐨𝐫𝐭 𝐭𝐡𝐞 𝐂𝐀 𝐢𝐧𝐭𝐨 𝐊𝐞𝐲𝐬𝐭𝐨𝐫𝐞 ==

keytool -keystore kafka.zookeeper.keystore.jks -alias ca-cert -import -file ca-cert

#### 𝟕. 𝐈𝐦𝐩𝐨𝐫𝐭 𝐭𝐡𝐞 𝐬𝐢𝐠𝐧𝐞𝐝 𝐜𝐞𝐫𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐞 𝐢𝐧𝐭𝐨 𝐊𝐞𝐲𝐬𝐭𝐨𝐫𝐞 ==

keytool -keystore kafka.zookeeper.keystore.jks -alias zookeeper -import -file ca-signed-zookeeper

###### starting to create CA

###### Suggestion : use the same password where-ever you are prompted for one.

###### As in this setup multiple passwords will need to be generated. Why take extra headache to remember different passwords.

###### creating the Certificate Authority

openssl req -new -x509 -keyout ca-key -out ca-cert -days 3650

###### for zookeeper

keytool -keystore kafka.zookeeper.truststore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.zookeeper.keystore.jks -alias zookeeper -validity 3650 -genkey -keyalg RSA -ext SAN=dns:localhost
keytool -keystore kafka.zookeeper.keystore.jks -alias zookeeper -certreq -file ca-request-zookeeper
openssl x509 -req -CA ca-cert -CAkey ca-key -in ca-request-zookeeper -out ca-signed-zookeeper -days 3650 -CAcreateserial
keytool -keystore kafka.zookeeper.keystore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.zookeeper.keystore.jks -alias zookeeper -import -file ca-signed-zookeeper

###### for zookeeper clients(zookeepr scripts like zookeeper-shell)

keytool -keystore kafka.zookeeper-client.truststore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.zookeeper-client.keystore.jks -alias zookeeper-client -validity 3650 -genkey -keyalg RSA -ext SAN=dns:localhost
keytool -keystore kafka.zookeeper-client.keystore.jks -alias zookeeper-client -certreq -file ca-request-zookeeper-client
openssl x509 -req -CA ca-cert -CAkey ca-key -in ca-request-zookeeper-client -out ca-signed-zookeeper-client -days 3650 -CAcreateserial
keytool -keystore kafka.zookeeper-client.keystore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.zookeeper-client.keystore.jks -alias zookeeper-client -import -file ca-signed-zookeeper-client

###### for broker0

keytool -keystore kafka.broker0.truststore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.broker0.keystore.jks -alias broker0 -validity 3650 -genkey -keyalg RSA -ext SAN=dns:localhost
keytool -keystore kafka.broker0.keystore.jks -alias broker0 -certreq -file ca-request-broker0
openssl x509 -req -CA ca-cert -CAkey ca-key -in ca-request-broker0 -out ca-signed-broker0 -days 3650 -CAcreateserial
keytool -keystore kafka.broker0.keystore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.broker0.keystore.jks -alias broker0 -import -file ca-signed-broker0

###### for broker 1

keytool -keystore kafka.broker1.truststore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.broker1.keystore.jks -alias broker1 -validity 3650 -genkey -keyalg RSA -ext SAN=dns:localhost
keytool -keystore kafka.broker1.keystore.jks -alias broker1 -certreq -file ca-request-broker1
openssl x509 -req -CA ca-cert -CAkey ca-key -in ca-request-broker1 -out ca-signed-broker1 -days 3650 -CAcreateserial
keytool -keystore kafka.broker1.keystore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.broker1.keystore.jks -alias broker1 -import -file ca-signed-broker1

###### for broker 2

keytool -keystore kafka.broker2.truststore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.broker2.keystore.jks -alias broker2 -validity 3650 -genkey -keyalg RSA -ext SAN=dns:localhost
keytool -keystore kafka.broker2.keystore.jks -alias broker2 -certreq -file ca-request-broker2
openssl x509 -req -CA ca-cert -CAkey ca-key -in ca-request-broker2 -out ca-signed-broker2 -days 3650 -CAcreateserial
keytool -keystore kafka.broker2.keystore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.broker2.keystore.jks -alias broker2 -import -file ca-signed-broker2

###### for consumer

keytool -keystore kafka.consumer.truststore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.consumer.keystore.jks -alias consumer -validity 3650 -genkey -keyalg RSA -ext SAN=dns:localhost
keytool -keystore kafka.consumer.keystore.jks -alias consumer -certreq -file ca-request-consumer
openssl x509 -req -CA ca-cert -CAkey ca-key -in ca-request-consumer -out ca-signed-consumer -days 3650 -CAcreateserial
keytool -keystore kafka.consumer.keystore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.consumer.keystore.jks -alias consumer -import -file ca-signed-consumer

###### for producer

keytool -keystore kafka.producer.truststore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.producer.keystore.jks -alias producer -validity 3650 -genkey -keyalg RSA -ext SAN=dns:localhost
keytool -keystore kafka.producer.keystore.jks -alias producer -certreq -file ca-request-producer
openssl x509 -req -CA ca-cert -CAkey ca-key -in ca-request-producer -out ca-signed-producer -days 3650 -CAcreateserial
keytool -keystore kafka.producer.keystore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.producer.keystore.jks -alias producer -import -file ca-signed-producer

###### foradmin

keytool -keystore kafka.admin.truststore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.admin.keystore.jks -alias admin -validity 3650 -genkey -keyalg RSA -ext SAN=dns:localhost
keytool -keystore kafka.admin.keystore.jks -alias admin -certreq -file ca-request-admin
openssl x509 -req -CA ca-cert -CAkey ca-key -in ca-request-admin -out ca-signed-admin -days 3650 -CAcreateserial
keytool -keystore kafka.admin.keystore.jks -alias ca-cert -import -file ca-cert
keytool -keystore kafka.admin.keystore.jks -alias admin -import -file ca-signed-admin

###### now after the certificates are created lets start setting up the kafka-cluster

###### ------------NOTE---------------------######

###### Please change the host machine paths according to your folder structure

###### Also, do not change the path inside the image, image paths are fixed and the mounted files should be present there only

###### install docker and configure it to run for non-sudo users.

###### USEFUL LINKS FOR THE IMAGES USED BELOW:

For zookeeper:
https://hub.docker.com/r/bitnami/zookeeper/

For broker:
https://github.com/bitnami/bitnami-docker-kafka/blob/master/README.md#setting-up-a-kafka-cluster
https://github.com/bitnami/bitnami-docker-kafka/blob/master/2/debian-10/rootfs/opt/bitnami/scripts/libkafka.sh#L221

# to run zookeeper in docker

docker run --name zookeeper-docker1 --net=host -v /home/mukesh/kube-demo4/docker-demo/certs/:/bitnami/zookeeper/certs -e ZOO_TLS_CLIENT_ENABLE=true -e ZOO_TLS_PORT_NUMBER=2182 -e ZOO_TLS_CLIENT_KEYSTORE_FILE=/bitnami/zookeeper/certs/zookeeper.keystore.jks -e ZOO_TLS_CLIENT_KEYSTORE_PASSWORD=demokafka -e ZOO_TLS_CLIENT_TRUSTSTORE_FILE=/bitnami/zookeeper/certs/zookeeper.truststore.jks -e ZOO_TLS_CLIENT_TRUSTSTORE_PASSWORD=demokafka -e ZOO_TLS_CLIENT_AUTH=need -e ZOO_ENABLE_AUTH=yes bitnami/zookeeper:latest

## execute all bin commands from inside kafka_2.13-2.8.0 package

###### For e.g.

home/mukesh/kafka_2.13-2.8.0~$ <write all commands starting with bin here>

###------check that can connect to zookeeper via zookeeper-shell
bin/zookeeper-shell.sh localhost:2182 -zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties

####-----------creating broker account : like any client of the cluster broker also needs a user account to be registered with zookeeper.

###### this account also needs proper authorization that is already given inside the server.properties(made this account super user)

bin/kafka-configs.sh --zookeeper localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --entity-type users --entity-name broker-admin --alter --add-config 'SCRAM-SHA-512=[password=demokafka]'

###----------- to run broker0 in docker

docker run --name broker0-docker1 --net=host -v /home/mukesh/kube-demo4/docker-demo/config/server-0.properties:/bitnami/kafka/config/server.properties -v /home/mukesh/kube-demo4/docker-demo/certs/:/bitnami/kafka/config/certs -v /home/mukesh/kube-demo4/docker-demo/config/kafka_jaas.config:/opt/bitnami/kafka/config/kafka_jaas.conf -e KAFKA_CFG_LISTENERS=SASL_SSL://localhost:9092 -e KAFKA_ADVERTISED_LISTENERS=SASL_SSL://:9092 -e KAFKA_ZOOKEEPER_PROTOCOL=SSL bitnami/kafka:latest

###----------- to run broker1 in docker

docker run --name broker1-docker1 --net=host -v /home/mukesh/kube-demo4/docker-demo/config/server-1.properties:/bitnami/kafka/config/server.properties -v /home/mukesh/kube-demo4/docker-demo/certs/:/bitnami/kafka/config/certs -v /home/mukesh/kube-demo4/docker-demo/config/kafka_jaas.config:/opt/bitnami/kafka/config/kafka_jaas.conf -e KAFKA_CFG_LISTENERS=SASL_SSL://localhost:9093 -e KAFKA_ADVERTISED_LISTENERS=SASL_SSL://:9093 -e KAFKA_ZOOKEEPER_PROTOCOL=SSL bitnami/kafka:latest

###----------- to run broker2 in docker

docker run --name broker2-docker1 --net=host -v /home/mukesh/kube-demo4/docker-demo/config/server-2.properties:/bitnami/kafka/config/server.properties -v /home/mukesh/kube-demo4/docker-demo/certs/:/bitnami/kafka/config/certs -v /home/mukesh/kube-demo4/docker-demo/config/kafka_jaas.config:/opt/bitnami/kafka/config/kafka_jaas.conf -e KAFKA_CFG_LISTENERS=SASL_SSL://localhost:9094 -e KAFKA_ADVERTISED_LISTENERS=SASL_SSL://:9094 -e KAFKA_ZOOKEEPER_PROTOCOL=SSL bitnami/kafka:latest

###### Now before producing and consuming messages, we need to create topic and consumer account and producer account

#########------------creating admin for creating topic

###### For Production environments, it is not a recommended practice to use the same credentials used for brokers for daily kafka administration activities. Hence, create a new SASL credential using the below command:

bin/kafka-configs.sh --zookeeper localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --entity-type users --entity-name kafka-admin --alter --add-config 'SCRAM-SHA-512=[password=demokafka]'

###### Now, for granting the super-user access to the above credential, execute the following ACLs:

###### FULL ACCESS for Topics

bin/kafka-acls.sh --authorizer-properties zookeeper.connect=localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --add --allow-principal User:kafka-admin --operation READ --operation WRITE --operation DESCRIBE --operation DESCRIBECONFIGS --operation ALTER --operation ALTERCONFIGS --operation CREATE --operation DELETE --topic '\*'

###### FULL ACCESS for Groups

bin/kafka-acls.sh --authorizer-properties zookeeper.connect=localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --add --allow-principal User:kafka-admin --operation READ --operation DESCRIBE --operation DELETE --group '\*'

###### FULL ACCESS for delegation-tokens

bin/kafka-acls.sh --authorizer-properties zookeeper.connect=localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --add --allow-principal User:kafka-admin --operation DESCRIBE --delegation-token '\*'

###### FULL ACCESS for transactional clients

bin/kafka-acls.sh --authorizer-properties zookeeper.connect=localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --add --allow-principal User:kafka-admin --operation DESCRIBE --operation WRITE --transactional-id '\*'

#######....................................................IMPORTANT----------------------------------------------##############3

###### find cluster id by doing $ get /cluster/id ---in zookeeper-shell ---opened the below command

###### below command was already provided above, execute it now if not already executed.

###### bin/zookeeper-shell.sh localhost:2182 -zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties

###### For eg

get /cluster/id
WMe3OUXVTju93SJ1_Iz6Sg

###### Uncomment the below command and replace the cluster id there with the one you just obtanied from zookeeper-shell

###### FULL ACCESS to the cluster, replace cluster id in this before use

###### bin/kafka-acls.sh --authorizer-properties zookeeper.connect=localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --add --allow-principal User:kafka-admin --operation ALTER --operation ALTERCONFIGS --operation CLUSTERACTION --operation CREATE --operation DESCRIBE --operation DESCRIBECONFIGS --operation IDEMPOTENTWRITE --cluster Qln4fSIbShGpAQik8jrkcQ

###### Finally, create the topic using the below command:

bin/kafka-topics.sh --bootstrap-server localhost:9092,localhost:9093,localhost:9094 --command-config /home/mukesh/kube-demo4/docker-demo/config/kafka-admin.properties --create --topic ssl-topic --partitions 2 --replication-factor 3 --config min.insync.replicas=2

#####-----------creating producer account

bin/kafka-configs.sh --zookeeper localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --entity-type users --entity-name demo-producer --alter --add-config 'SCRAM-SHA-512=[password=demokafka]'

####-----------granting producer access to produce to the topic

bin/kafka-acls.sh --authorizer-properties zookeeper.connect=localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --add --allow-principal User:demo-producer --operation WRITE --operation DESCRIBE --operation DESCRIBECONFIGS --topic ssl-topic

####----------creating consumer account

bin/kafka-configs.sh --zookeeper localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --entity-type users --entity-name demo-consumer --alter --add-config 'SCRAM-SHA-512=[password=demokafka]'

####----------to grant consumer access to consume from the topic

bin/kafka-acls.sh --authorizer-properties zookeeper.connect=localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --add --allow-principal User:demo-consumer --operation READ --operation DESCRIBE --topic ssl-topic

######--- any consumer by default exits within a consumer group
####---------allowing consumer account to create a consumer group

bin/kafka-acls.sh --authorizer-properties zookeeper.connect=localhost:2182 --zk-tls-config-file /home/mukesh/kube-demo4/docker-demo/config/zookeeper-client.properties --add --allow-principal User:demo-consumer --operation READ --group consumer-group1

###### now use the given secure-producer and secure-consumer scripts to produce and consume messages respectively

##-- to properly use the consumer and producer
##-- keep in mind the path of ca-cert as mentioned in these scripts
##-- also the username and password should match as set in this configuration
##-- for running secure-producer and secure-consumer.py, you would need librdkafka and confluent_kafka packages.
##-- confluent_kafka is just a wrapper around librdkafka
##-- also, I have used librdkafka by installing latest from brew, and python 3.93.
##-- there were some issues with the version compatibility when using these dependencies some other way.(like confluent_kafka was unable to detect librdkafka)

### Also explicitily mentioning the SSL, SASL configs. These are already setup inside their respective files.

#############################3------------------------------configurations

###### these properties are added to the respective files, if already place replace the one ones.

SSL SPECIFIC PROPERTIES TO CONFIGURE ZOOKEEPER FOR ZOOKEEPER SECURITY:
𝟏. inside 𝐙𝐎𝐎𝐊𝐄𝐄𝐏𝐄𝐑.𝐏𝐑𝐎𝐏𝐄𝐑𝐓𝐈𝐄𝐒 file
secureClientPort=2182
authProvider.x509=org.apache.zookeeper.server.auth.X509AuthenticationProvider
serverCnxnFactory=org.apache.zookeeper.server.NettyServerCnxnFactory
ssl.trustStore.location=kafka.zookeeper.truststore.jks
ssl.trustStore.password=12345
ssl.keyStore.location=kafka.zookeeper.keystore.jks
ssl.keyStore.password=12345
ssl.clientAuth=need

𝟐. inside 𝐒𝐄𝐑𝐕𝐄𝐑.𝐏𝐑𝐎𝐏𝐄𝐑𝐓𝐈𝐄𝐒 file

###### for 2 way ssl connection b/w zookeeper and broker

zookeeper.connect=localhost:2182
zookeeper.clientCnxnSocket=org.apache.zookeeper.ClientCnxnSocketNetty
zookeeper.ssl.client.enable=true
zookeeper.ssl.protocol=TLSv1.2
zookeeper.ssl.truststore.location=kafka.broker0.truststore.jks
zookeeper.ssl.truststore.password=12345
zookeeper.ssl.keystore.location=/kafka.broker0.keystore.jks
zookeeper.ssl.keystore.password=12345
zookeeper.set.acl=true

SSL SPECIFIC PROPERTIES TO CONFIGURE BROKERS, PRODUCERS AND CONSUMERS FOR KAFKA/BROKER SECURITY:
𝟏. inside 𝐒𝐄𝐑𝐕𝐄𝐑.𝐏𝐑𝐎𝐏𝐄𝐑𝐓𝐈𝐄𝐒 file

####---- below is an example shown for broker0, similarly do for broker1 and broker2-docker1
######-- So at the end there will be 3 files, server-0.properties, server-1.properties, server-2.properties

broker.id=0
num.partitions=3

listeners=SASL_SSL://localhost:9092
advertised.listeners=SASL_SSL://localhost:9092
ssl.truststore.location=kafka.broker0.truststore.jks
ssl.truststore.password=12345
ssl.keystore.location=kafka.broker0.keystore.jks
ssl.keystore.password=12345
ssl.key.password=12345
#security.inter.broker.protocol=SSL
security.inter.broker.protocol=SASL_SSL

###### below was for ssl

#ssl.client.auth=required

###### is now for sasl

ssl.client.auth=none
ssl.protocol=TLSv1.2

sasl.enabled.mechanisms=SCRAM-SHA-512
sasl.mechanism.inter.broker.protocol=SCRAM-SHA-512

listener.name.sasl_ssl.scram-sha-512.sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username="broker-admin" password="demokafka";

super.users=User:broker-admin
authorizer.class.name=kafka.security.authorizer.AclAuthorizer

###### below properties are not used for setting up the kafka cluster

###### but for setting up the console consumer and console producer shell scripts, if you want to use them securely.

𝟐. 𝐏𝐑𝐎𝐃𝐔𝐂𝐄𝐑.𝐏𝐑𝐎𝐏𝐄𝐑𝐓𝐈𝐄𝐒
bootstrap.servers=localhost:9092
security.protocol=SSL
ssl.truststore.location=kafka.producer.truststore.jks
ssl.truststore.password=12345
ssl.keystore.location=kafka.producer.keystore.jks
ssl.keystore.password=12345
ssl.key.password=12345
ssl.protocol=TLSv1.2

𝟑. 𝐂𝐎𝐍𝐒𝐔𝐌𝐄𝐑.𝐏𝐑𝐎𝐏𝐄𝐑𝐓𝐈𝐄𝐒
bootstrap.servers=localhost:9092
group.id=ssl-consumer-group
security.protocol=SSL
ssl.truststore.location=kafka.consumer.truststore.jks
ssl.truststore.password=12345
ssl.keystore.location=kafka.consumer.keystore.jks
ssl.keystore.password=12345
ssl.key.password=12345
ssl.protocol=TLSv1.2

###### zookeeper-client.properties and kafka-admin.properties are completely self made files

###### so configs. for those, you can see there itself.

### For Kubernetes setup see kube-setup.properties inside the kube-demo/setup folder
