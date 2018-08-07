import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip=""
port=8000

s.bind((ip, port))

print "Server Listening On Port ", port
s.listen(1)

(client, (c_ip,port)) =s.accept()
print "Client With: " +c_ip+ "connect to the server"

while 1:
	data=client.recv(2096)
	if not data:
		break
	print "client sent: ", data
	client.send(data)

print "closing the client connection"
client.close()

print "Release Socket"
s.close() 
	
