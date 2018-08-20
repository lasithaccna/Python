import socket,sys
from threading import Thread


sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip=sys.argv[1]
port=int(sys.argv[2])
sock.connect((ip,port))

	

def rec_data():
	while True:
		server_data=sock.recv(1024)
		print(server_data)


thread2=Thread(target=rec_data).start()
while True:
	try:
		client_input=raw_input()
		sock.send(client_input)
	except KeyboardInterrupt:
		sys.exit()
