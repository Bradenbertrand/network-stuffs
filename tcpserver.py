import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

serversocket.bind(("", port))

serversocket.listen(3)

print(socket.gethostbyname("chrx"))
while True:
    clientsocket, address = serversocket.accept()

    print("received connection at " + str(address))

    message = "fuck cock"

    clientsocket.send(message.encode("ascii"))

    clientsocket.close()