import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 444

clientsocket.connect((host, port))

message = clientsocket.recv(1024)

clientsocket.close()