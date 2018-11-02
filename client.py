import socket,sys,os
from threading import Thread


sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip=sys.argv[1]
port=int(sys.argv[2])
sock.connect((ip,port))

	

def rec_data():
	while True:
		try:	
			server_data=sock.recv(1024)
			print(server_data)
		
		except KeyboardInterrupt:
			sock.close()
			sys.exit()		
		else:
			if not server_data:
				break		
		
thread2=Thread(target=rec_data)
thread2.daemon=True
thread2.start()

while True:
	try:
		client_input=raw_input()
		sock.send(client_input)
	except KeyboardInterrupt:
		sock.close()
		sys.exit()		
			
	
