from minio import Minio
import pandas as pd
import datetime
import os
from pathlib import Path
import numpy as np


class Storage_Data:
    def __init__(self, *, access_key, secret_key) -> None:
        self.access_key = access_key
        self.secret_key = secret_key

    # -----Connect to the MinIO-----
    def conn_minio(self):
        self.client = Minio(
            "localhost:9000", access_key=self.access_key, secret_key=self.secret_key, secure=False
        )

    def preprocess_data(self, parametros, result):
        columns = list(parametros.keys()) + list(result.keys())
        values = list(parametros.values()) + list(result.values())
        arr_len = len(values)

        df = pd.DataFrame(
            np.array(values, dtype=object).reshape(1, arr_len), columns=columns
        )

        self.path_to_save = "modelo_class_img_" + datetime.datetime.now().strftime(
            "%d-%M-%Y_%H-%M-%S"
        )
        df.to_csv(self.path_to_save + ".csv")

    def storage_data(self):
        # Make 'artefatos_image_classifier' bucket if not exist.
        found = self.client.bucket_exists("artefatos")
        if not found:
            self.client.make_bucket("artefatos")
        else:
            print("Bucket 'artefatos' already exists")

        self.client.fput_object(
            "artefatos",
            self.path_to_save,
            str(Path(os.getcwd(), self.path_to_save).with_suffix(".csv")),
        )
