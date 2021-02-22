import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = "192.168.1.59"

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

socket.gethostname()

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def main():
    inp = input('Enter anything else to send to the server:')
    while inp != "":
        send(inp)
        inp = input('Enter nothing to disconnect. Enter anything else to send to the server')
    send(DISCONNECT_MESSAGE)


if __name__ == '__main__':
    main()