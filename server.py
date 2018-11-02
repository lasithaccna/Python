import socket,sys,os
from threading import Thread

sock_s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip=''
port=int(sys.argv[1])

sock_s.bind((ip, port))

sock_s.listen(1)

sock, data =sock_s.accept()


def rec_data():
	while True:
		try:	
			client_data=sock.recv(1024)
			print(client_data)
		
		except KeyboardInterrupt:
			sock.close()
			sys.exit()		
		else:
			if not client_data:
				break		
		


thread2=Thread(target=rec_data) 
thread2.daemon=True
thread2.start()

while True:	
	try:
		server_input=raw_input()
		sock.send(server_input)
	except KeyboardInterrupt:
		sock.close()
		sys.exit()
			
	
