import socket
from threading import Thread
from colorama import Fore, init, Back
import random
init()

colors = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
cColor = random.choice(colors)
s = socket.socket()
host = "45.33.20.96"
port = 1234
s.connect((host, port))
print("Connected to server")
username = input("Enter user name: ")
joinedMessage = f"{cColor}{username} has joined the chat!{Fore.RESET}"
s.send(joinedMessage.encode('utf-8'))
def getMessages():
    while True:
        message = s.recv(1024).decode("utf-8")
        print(f"\n{message}")

thread = Thread(target=getMessages)
thread.daemon = True
thread.start()

while True:
    clientMessage = input()
    sendMessage = f"{cColor}{username}: {clientMessage}{Fore.RESET}"
    if clientMessage == "quit":
        break
    s.send(sendMessage.encode('utf-8'))

s.close()
