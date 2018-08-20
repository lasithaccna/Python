import socket,sys
from threading import Thread

sock_s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip=sys.argv[1]
port=int(sys.argv[2])

sock_s.bind((ip, port))

sock_s.listen(1)

sock, data =sock_s.accept()


def rec_data():
	while True:
		client_data=sock.recv(1024)
		print(client_data)


thread2=Thread(target=rec_data).start() 
while True:	
	try:
		server_input=raw_input()
		sock.send(server_input)
	except KeyboardInterrupt:
		sys.exit()
