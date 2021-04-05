import socket
import threading
import addr_list

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)
server.bind(ADDR)


def main():
    print('[STARTING] server is starting...')
    start(addr_list.conn_list())


def distribute_messages(connections, msg):
    for client in connections.contents:
        print(f'sent to {client}')
        client.conn.send(msg.encode(FORMAT))


def handle_client(connections, conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            distribute_messages(connections, msg)

    conn.close()


def start(connections):
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        connections.insert(conn, addr)
        print(f'{addr} added to list')
        thread = threading.Thread(target=handle_client, args=(connections, conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == '__main__':
    main()
