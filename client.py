import socket
import sys

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((sys.argv[1], int(sys.argv[2])))

while 1:
	ip=raw_input()
	client.send(ip)
	print client.recv(2096)

client.close()

