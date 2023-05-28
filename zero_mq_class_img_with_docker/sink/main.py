import zmq
from minio import Minio
import pickle
import pandas as pd
from pathlib import Path
import os
import datetime
from storage_data import Storage_Data
import random


def main():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)

    socket.bind("tcp://0.0.0.0:5556")

    _id = str(os.getpid())

    while True:
        result = socket.recv_json()
        print("-" * 10)
        print("SINK: " + _id)
        print(result)

        try:
            # -----Storage the data-----
            storage_data = Storage_Data(access_key="minio", secret_key="minio123")

            storage_data.conn_minio()

            storage_data.preprocess_data(
                parametros=result.get("parametros"), result=result.get("result")
            )

            storage_data.storage_data()
            print("Informacoes persistidas com sucesso!")
        except Exception as error:
            print("Erro ao persistir as informacoes!")
            pass

        print("-" * 10)


if __name__ == "__main__":
    main()
