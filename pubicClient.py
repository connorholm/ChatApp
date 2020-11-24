import socket
from threading import Thread

s = socket.socket()
host = "45.33.20.96"
port = 1234
s.connect((host, port))
print("Connected to server")
username = input("Enter user name: ")

def getMessages():
    while True:
        message = s.recv(1024).decode("utf-8")
        print(f"\n{message}")

thread = Thread(target=getMessages)
thread.daemon = True
thread.start()

while True:
    clientMessage = input()
    sendMessage = f"{username}: {clientMessage}"
    if clientMessage == "quit":
        break
    s.send(sendMessage.encode('utf-8'))

s.close()
