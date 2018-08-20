import socket,sys
from threading import Thread

sock_s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip=sys.argv[1]
port=int(sys.argv[2])

sock_s.bind((ip, port))

sock_s.listen(1)

sock, data =sock_s.accept()

def send_data():
	while True:
		server_input=raw_input()
		sock_s.send(server_input)

def rec_data():
	while True:
		client_data=sock_s.recv(1024)
		print(client_data)

thread1=Thread(target=send_data).start()
thread2=Thread(target=rec_data).start() 
	
