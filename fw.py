import socket, sys
from struct import *
import os.path
 
#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b
 

try:
    s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0800))
except socket.error , msg:
    print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
path=sys.argv[1] 
# receive a packet
while True:


	try:
	        receive_packet = s.recvfrom(65565)
	        packet = receive_packet[0] 
	except KeyboardInterrupt:
	        sys.exit()

    

    
	       
        ip_header = packet[14:34]
	ip_header_unpack = unpack('!BBHHHBBH4s4s' , ip_header) 
	version_ihl = ip_header_unpack[0]
	version = version_ihl >> 4
	ihl = version_ihl & 0xF 
	iph_length = ihl * 4 
	ttl = ip_header_unpack[5]
	protocol = ip_header_unpack[6]
	src_addr = socket.inet_ntoa(ip_header_unpack[8]);
	dst_addr = socket.inet_ntoa(ip_header_unpack[9]);


	f=open(path,'r')
	lines=0
	while True:
		#read First 16 Charactors
		r=f.read(7)
		x=r
		if not r:
			break
		y=[]
		#get first charactor and convert to ascii
		for i in r:
		
			y.append(i)
			
		if str(y)==str(src_addr):
			print "Packet Ok"




	#print "This Is an IP Packet \n Ip Header Is  \n ---------------------------------------------------------------------------------------------------------"
	#print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(src_addr) + ' Destination Address : ' + str(dst_addr)
	#print "---------------------------------------------------------------------------------------------------------"
