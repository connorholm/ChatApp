import socket
import select

HEADER_LENGTH = 10

IP = socket.gethostname()
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen()

while True:
    c , addr = s.accept()
    print("Got connection")
    output = 'Thank you for connecting'
    c.sendall(output.encode('utf-8'))
    c.close()  
