from pprint import pprint

from confluent_kafka import Consumer

################
c = Consumer(
    {
        "bootstrap.servers": "localhost:9092",
        "group.id": "python-consumer",
        "auto.offset.reset": "earliest",
    }
)
print("Kafka Fraud Listener has been initiated...")

print("Available topics to consume: ", c.list_topics().topics)
c.subscribe(["fraud_credictcard_transactions"])


def main():
    while True:
        msg = c.poll(1.0)  # timeout
        if msg is None:
            continue

        if msg.error():
            print("Error: {msg.error()}")
            continue

        msg_data = msg.value().decode("utf-8")

        print("-"*10)
        pprint(msg_data)
        print("-"*10)

    c.close()

if __name__ == "__main__":
    main()