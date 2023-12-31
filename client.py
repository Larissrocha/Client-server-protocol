import socket
import threading
import os

HEADER = 64
PORT = 18000
FORMAT = "utf-8"
DISCONNECT_MESAGE = "!DISCONNECT"
SERVER = "10.10.18.179"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def go(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b" " * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)


def listen():
    while True:
        string = client.recv(2048).decode(FORMAT)
        if not string:
            break
        print("\n" + string)


def send():
    message = request.form["message"]
    go(message)
    if message == ":D":
        client.close()
        global own_pid
        os.kill(own_pid, 9)
    return chat()


if __name__ == "__main__":
    server = threading.Thread(target=listen)
    server.daemon = True
    server.start()
