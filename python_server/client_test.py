import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8888))
msg = "Hello server!"
clientsocket.sendall(msg.encode())
print("Message sent..")

msg = clientsocket.recv(14).decode()
print("Received messange..")
print (msg)

clientsocket.close()