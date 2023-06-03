# pip install confluent-kafka
import json
from uuid import uuid4
import zmq

import joblib
import pandas as pd

from confluent_kafka import Producer

p = Producer({"bootstrap.servers": "localhost:9092"})
print("Kafka Fraud Generator has been initiated...")

TOPIC = "fraud_credictcard_transactions"


def main():
   
    context = zmq.Context()
    socket_rcv = context.socket(zmq.PULL)
    socket_rcv.connect("tcp://0.0.0.0:5555")

    while True:
        
        result = socket_rcv.recv_json()

        loaded_svc = joblib.load("svm.joblib")

        input_arr = pd.array(result.get("vals")).reshape(1, -1)
        
        resultado = loaded_svc.predict(input_arr)[0]

        if resultado == 1:

            msg = {
                "fraud": True,
                "transactionId": result.get("transactionId")
            }

            m = json.dumps(msg)
            p.produce(TOPIC, m.encode("utf-8"))
            p.flush()

            print("-"*10)
            print(f"Sent to fraud_credictcard_transactions")
            print("data: ", msg)
            print("-"*10)
        
if __name__ == "__main__":
    main()
