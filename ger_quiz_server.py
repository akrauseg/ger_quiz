import socket               # Import socket module
import threading
import random
import sys
import ger_quiz		    #import DB functions

#we need something to be able to do a user/group lookup for competition

registered_ips={}

def myfunc(c): #testing various networking things - > to be removed
	c.send(bytes("Thank you for connecting\n","utf-8"))
	print("getting data from client")
	data = str(c.recv(1024))
	print("ip we got:",data)
	print("\n")
	data = str(c.recv(1024))
	print("data we got:",data)
	print("\n")
	data = str(c.recv(1024))
	print("username we got",data)
	print("\n")
	ger_quiz.start_game()
	c.close()                # Close the connection


#not rlly a fan of the next 2 functions
def get_random_user( current_user ):
	if len(registered_ips) < 2:
		print("No other players available\n")
	else:
		random_user = random.choice(registered_ips.keys()) #get random user
		while random_user == current_user:
			random_user = random.choice(registered_ip.keys())
		return random_user

def get_requested_user( current_user, requested_user ):
	if current_user == requested_user:
		print("User requesting self\n")
		#what are we going to return here?
	if requested_user in registered_ips.keys():
		print("Requested user found\n")
		
		
			



s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
count=0
while True:
	c, addr = s.accept()     # Establish connection with client.
	print('Got connection from', addr)
	hostname=socket.gethostbyaddr(str(addr[0]))
	print(hostname)
	registered_ips[hostname[0]]=addr
	print(registered_ips)
	t=threading.Thread(target=myfunc,args=(c,))
	t.start()



