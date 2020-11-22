import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1234                # Reserve a port for your service.

s.connect((host, port))
output = s.recv(1024)
print(output.decode("utf-8"))

message = "Message to the server from the client"
s.send(message.encode('utf-8'))

s.close()