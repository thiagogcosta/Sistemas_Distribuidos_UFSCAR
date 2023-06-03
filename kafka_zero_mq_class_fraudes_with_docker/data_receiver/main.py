from pprint import pprint
import zmq
import json

from confluent_kafka import Consumer

################
c = Consumer(
    {
        "bootstrap.servers": "localhost:9092",
        "group.id": "python-consumer",
        "auto.offset.reset": "earliest",
    }
)
print("Kafka Consumer has been initiated...")

print("Available topics to consume: ", c.list_topics().topics)
c.subscribe(["creditcard_transactions"])


def main():

    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://0.0.0.0:5555")

    while True:
        msg = c.poll(1.0)  # timeout
        if msg is None:
            continue

        if msg.error():
            print("Error: {msg.error()}")
            continue

        msg_data = msg.value().decode("utf-8")
        msg_data_json = json.loads(msg_data)

        zmq_socket.send_json(msg_data_json)

    c.close()

if __name__ == "__main__":
    main()