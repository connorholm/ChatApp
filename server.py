import socket
import select

HEADER_LENGTH = 10

IP = socket.gethostname()
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen()

clientsInfo = []
def recvMessage():
    return True
while True:
#   for client in clients:
#        if client
    c , addr = s.accept()
    print("Got connection to "+str(addr))
    output = 'Thank you for connecting'
    c.sendall(output.encode('utf-8'))
    clientsInfo.append(
        {
            c,
            addr
        }
    )
    print(clientsInfo)
    input = c.recv(1024)
    print(input.decode("utf-8"))
    c.close()
