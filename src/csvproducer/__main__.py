from pykafka import KafkaClient


def main():
    client = KafkaClient(hosts="localhost:9092")
    topic = client.topics['data'.encode()]
    with topic.get_sync_producer() as producer:
        for i in range(4):
            producer.produce(('test message ' + str(i ** 2)).encode())


if __name__ == '__main__':
    main()
