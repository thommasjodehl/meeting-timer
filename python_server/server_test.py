import socket
import sys

#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the local host,
# and a well known port
serversocket.bind(('localhost', 8888))

serversocket.listen(1)

# Set the timeout of the socket to 250 miliseconds.
serversocket.settimeout(0.250)

client = 0

try: # try to accept a connection.
   print ("Waiting for someone to connect..")
   (client, address) = serversocket.accept()
   if client == 0: # if it was not possible to connect to a client
      print("No one to connect to..")
      serversocket.close()
      sys.exit(1)
   else: # else do the business
      print ("New connection from", address)
      msg = client.recv(14).decode()
      if msg != 0:
         print ("Received message..")
         print (msg)
         msg = "Hello client!"
         client.sendall(msg.encode())
         client.close()
         serversocket.close()
except OSError as msg: # handle when there is no one to connect to.
   serversocket.close()
