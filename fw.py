import socket, sys
from struct import *
import os.path,IN
from threading import Thread
 

def eth_addr (a) :
  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b

path=sys.argv[1]
f=open(path,'r')
block=[]
while True:
        	r=f.read(16)        
        	if not r:
               		break 
		block.append(r) 
			
				
for p in range (0,len(block),1):
	print (block[p])
		

def checkip(ip):
	#This Part Not Work. This Wrote For Check The Block Ip List .
	'''for i in range(0,len(block),1):
		if str(ip)==str(block[i]):
			return True'''
			
	#Sample Data
	if (ip=="8.8.8.8"):
		return True
try:
	sock1 = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0800))
	sock1.setsockopt(socket.SOL_SOCKET, IN.SO_BINDTODEVICE, "enp0s3")
	sock2 = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0800))
	sock2.setsockopt(socket.SOL_SOCKET, IN.SO_BINDTODEVICE, "enp0s8")

except socket.error , msg:
	print 'Socket could not be created.'
	sys.exit()



def int1():

	while True:
		try:
	       	 	receive_packet = sock1.recvfrom(65565)
	        	packet = receive_packet[0] 
		except KeyboardInterrupt:
	        	sys.exit()  
	       
        	ip_header = packet[14:34]
		ip_header_unpack = unpack('!BBHHHBBH4s4s' , ip_header) 		
		protocol = ip_header_unpack[6]
		src_addr = socket.inet_ntoa(ip_header_unpack[8]);
		dst_addr = socket.inet_ntoa(ip_header_unpack[9]);
	
		block=checkip(src_addr);	
		try:		
			if (str(block)=="True"):
				print "Blocked Packet"
				#sock1.sendto(packet,("enp0s8",0))
			else:
				print "Allowed Packet"
		except KeyboardInterrupt:
	        	sys.exit() 

def int2():

	while True:
		try:
	        	receive_packet = sock2.recvfrom(65565)
	        	packet = receive_packet[0] 
		except KeyboardInterrupt:
	        	sys.exit()  
	       
        	ip_header = packet[14:34]
		ip_header_unpack = unpack('!BBHHHBBH4s4s' , ip_header) 		 
		protocol = ip_header_unpack[6]
		src_addr = socket.inet_ntoa(ip_header_unpack[8]);
		dst_addr = socket.inet_ntoa(ip_header_unpack[9]);
	
		block=checkip(src_addr);	
		try:
			if (str(block)=="True"):
				print "Blocked Packet"
				#sock2.sendto(packet,("enp0s3",0))
			else:
				print "Allowed Packet"
		except KeyboardInterrupt:
	        	sys.exit() 

thread1=Thread(target=int1) 
thread1.start()

thread2=Thread(target=int2) 
thread2.start()

		

