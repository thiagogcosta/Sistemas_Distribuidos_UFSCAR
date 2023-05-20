import time
import zmq


def produce():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://0.0.0.0:5555")

    vector_architecture = [16, 32, 64, 128, 256]

    count = 0
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

                print("-" * 10)
                print("REQUISICAO: ", count)
                print("PARAMETROS: ", parametros)
                print("-" * 10)

                zmq_socket.send_json(parametros)

                time.sleep(15)

                count += 1


if __name__ == "__main__":
    produce()
