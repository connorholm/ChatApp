import socket
from threading import Thread

IP = socket.gethostname()
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(5)
clientsInfo = []
print("Listening for Clients")

def listenClients(s):
    while True:
        try:
            message = s.recv(1024).decode('utf-8')
        except Exception as e:
            print(f"Error: {e}")
            clientsInfo.remove(s)
        for client in clientsInfo:
            client.send(message.encode('utf-8'))
while True:
    c , addr = s.accept()
    print("Got connection to "+str(addr))
    clientsInfo.append(c)
    thread = Thread(target=listenClients, args=(c,)) 
    thread.daemon = True
    thread.start()


#get rid of duplicates
#Maybe add a gui?

