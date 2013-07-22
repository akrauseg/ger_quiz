import socket               # Import socket module
import sys

user_names = ("John","Dave","Peter","Mark","Lisa","Alyssa","Rick","Michael","Michelle","Marina")


def register_user_name (user_name , s):
	s.send(bytes(user_name,"utf-8")) #send over actual username








for i in range(10):
	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = 12345                # Reserve a port for your service.
	s.connect((host, port))
	print(s.recv(1024))
	print("sending message to server")
	host = socket.gethostname()
	s.send(bytes(host,"utf-8"))
	print("host: ",host)
	s.send(bytes("sent by client","utf-8"))
	register_user_name("blah",s)
	s.close()                     # Close the socket when done
