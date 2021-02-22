import socket
import threading

import time

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected")
    connected = True
    while connected:
        msg = conn.recv()


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print('[SERVER STARTING]')
start()