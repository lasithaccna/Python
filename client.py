import socket,sys
from threading import Thread


sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip=sys.argv[1]
port=int(sys.argv[2])
sock.connect((ip,port))
def send_data():
	while True:
		client_input=raw_input()
		sock.send(client_input)
	

def rec_data():
	while True:
		server_data=sock.recv(1024)
		print(server_data)

thread1=Thread(target=send_data).start()
thread2=Thread(target=rec_data).start()

