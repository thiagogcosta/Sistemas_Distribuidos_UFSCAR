import time
import zmq
import random
import os


def produce():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://0.0.0.0:5555")

    vector_architecture = [16, 32, 64, 128, 256]

    # Generate hash names
    random_bits = random.getrandbits(18)
    hash_name = "%08x" % random_bits

    _id = str(os.getpid())

    while True:
        for i in range(len(vector_architecture)):
            for j in range(len(vector_architecture)):
                parametros = {
                    "size_of_dense_layer_with_relu_activation_1": vector_architecture[
                        i
                    ],
                    "size_of_dense_layer_with_relu_activation_2": vector_architecture[
                        j
                    ],
                }

                requisicao = {"requisicao": hash_name, "parametros": parametros}

                print("-" * 10)
                print("VENTILATOR: " + _id)
                print(requisicao)
                print("-" * 10)

                zmq_socket.send_json(requisicao)

                time.sleep(5)


if __name__ == "__main__":
    produce()
