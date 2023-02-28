import socket
import random

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9000))
    sock.listen(1)
    myid = ''.join((random.choice('abcd') for i in range(5)))
    while True:
        connection, client_address = sock.accept()
        connection.sendall(f'Hello world from {myid}!'.encode())
        connection.close()

if __name__ == '__main__':
    main()