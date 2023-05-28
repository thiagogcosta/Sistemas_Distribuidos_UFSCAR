import os
from math import sqrt
from image_classifier import Image_Classifier
import zmq


def treinar_testar_modelo(param_1: int, param_2: int):
    # ----Configs----
    classificador = Image_Classifier().instance()
    classificador.configurar(
        size_of_dense_layer_with_relu_activation_1=param_1,
        size_of_dense_layer_with_relu_activation_2=param_2,
    )
    classificador.executar()
    return {
        "loss": classificador.test_loss,
        "acc": classificador.test_acc,
    }


def work():
    _id = str(os.getpid())
    print(f"WORKER: {_id}")

    context = zmq.Context()
    socket_rcv = context.socket(zmq.PULL)
    socket_rcv.connect("tcp://0.0.0.0:5555")

    socket_snd = context.socket(zmq.PUSH)
    socket_snd.connect("tcp://0.0.0.0:5556")

    while True:
        workload = socket_rcv.recv_json()
        result = treinar_testar_modelo(
            workload["parametros"]["size_of_dense_layer_with_relu_activation_1"],
            workload["parametros"]["size_of_dense_layer_with_relu_activation_2"],
        )

        result = {"worker_id": _id, "result": result}

        workload.update(result)

        print("-" * 10)
        print(workload)
        print("-" * 10)
        socket_snd.send_json(workload)


if __name__ == "__main__":
    print("Iniciando o worker...")
    work()
