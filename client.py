import socket

s = socket.socket()
host = socket.gethostname()
port = 1234

s.connect((host, port))
output = s.recv(1024)
print(output.decode("utf-8"))

message = "Message to the server from the client"
s.send(message.encode('utf-8'))

s.close()