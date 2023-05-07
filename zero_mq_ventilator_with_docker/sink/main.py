import zmq


def main():
    count = 0
    context = zmq.Context()
    socket = context.socket(zmq.PULL)

    socket.bind("tcp://0.0.0.0:5556")

    while True:
        result = socket.recv_json()
        count += 1

        print("-"*10)
        print({"COUNT": count, "RESULTADO": result})
        print("-"*10)

if __name__ == "__main__":
    main()