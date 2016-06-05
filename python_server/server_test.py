import socket

#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the local host,
# and a well known port
serversocket.bind(('localhost', 8888))

serversocket.listen(1)

while 1:
   #accept connections from outside
   print ("Waiting for someone to connect..")
   (client, address) = serversocket.accept()
   print ("New connection from", address)
   client.setblocking(0)
   if client != 0:
      print("Someone connected..")
      msg = client.recv(14).decode()
      if msg != 0:
         print ("Received message..")
         print (msg)
         msg = "Hello client!"
         client.sendall(msg.encode())
         client.close()