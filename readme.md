#Goal

We have csv file that has meta data and meta data. We want to find a way to
automatically load metadata and data into different topics.

To start, we use Apache Kafka

#start zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

#start kafka
bin/kafka-server-start.sh config/server.properties
 
#create topic 
bin/kafka-topics.sh --create --topic kmi_test --zookeeper localhost:2181 --replication-factor 1 --partitions 1

#create consumer 
kafka-console-consumer.sh --bootstrap-server=localhost:9092 --consumer.config=config/consumer.properties --topic kmi_test --from-beginning
