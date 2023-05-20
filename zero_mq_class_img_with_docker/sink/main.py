import zmq
from minio import Minio
import pickle
import pandas as pd
from pathlib import Path
import os
import datetime
from storage_data import Storage_Data


def main():
    count = 0
    context = zmq.Context()
    socket = context.socket(zmq.PULL)

    socket.bind("tcp://0.0.0.0:5556")

    while True:
        result = socket.recv_json()
        print("-" * 10)
        print({"REQUISICAO": count, "RESULTADO": result})

        try:
            # -----Storage the data-----
            storage_data = Storage_Data(access_key="minio", secret_key="minio123")
            print("ok1")
            storage_data.conn_minio()
            print("ok2")
            storage_data.preprocess_data(result.get("result"))
            print("ok3")
            storage_data.storage_data()
            print("ok4")

        except Exception as error:
            print("Erro ao persistir as informacoes!")
            pass

        print("-" * 10)
        count += 1


if __name__ == "__main__":
    main()
