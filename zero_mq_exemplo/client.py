# from pprint import pprint

import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)

    socket.connect("tcp://0.0.0.0:5555")

    while True:
        _ = input("Aperte [ENTER] para enviar!")
        socket.send_string("PING!")
        print("Enviado PING!")
        print("Recebido", socket.recv_string())


if __name__ == "__main__":
    main()
