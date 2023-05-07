# from pprint import pprint

import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)

    socket.bind("tcp://0.0.0.0:5555")

    while True:
        _ = socket.recv_string()
        socket.send_string("PONG!")
        print("Enviado PONG!")


if __name__ == "__main__":
    main()
