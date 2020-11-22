import socket
from threading import Thread
s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
print("Connected to server")

def getMessages():
    while True:
        message = s.recv(1024).decode("utf-8")
        print(f"\n{message}")
thread = Thread(target=getMessages)
thread.daemon = True
thread.start()
while True:
    clientMessage = input("Send to Chat: ")
    if clientMessage == "quit":
        s.close()
        break
    s.send(clientMessage.encode('utf-8'))
