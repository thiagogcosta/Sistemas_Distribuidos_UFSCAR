# pip install confluent-kafka
import json
import random
import time
from uuid import uuid4

import pandas as pd
from confluent_kafka import Producer

p = Producer({"bootstrap.servers": "localhost:9092"})
print("Kafka Producer has been initiated...")

TOPIC = "creditcard_transactions"


def main():
    csv_data = pd.read_csv("data/creditcard.csv")
    csv_data.drop("Time", axis=1, inplace=True)
    csv_data.drop("Class", axis=1, inplace=True)

    count = 0

    while True:
        
        row = csv_data.sample()
        data = {"vals": row.values.tolist()[0], "transactionId": str(uuid4())}
        
        m = json.dumps(data)
        p.produce(TOPIC, m.encode("utf-8"))
        p.flush()

        print("-"*10)
        print(f"Sent Transaction, id = {count}")
        print("data: ", data)
        print("-"*10)

        count += 1
        
if __name__ == "__main__":
    main()
