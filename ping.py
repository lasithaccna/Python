from  ctypes import *
import struct,sys
import socket,time

ip_ver=4
ip_hl=5
ip_hl_ver=(ip_ver<<4)+ip_hl
ip_tos=0
ip_lenth=0
ip_id=54321
ip_flag=0
ip_ttl=255
ip_prot=0
ip_check=0
ip_src=socket.inet_aton(socket.gethostbyname(socket.gethostname()))
ip_dest=socket.inet_aton(sys.argv[1])

ip_header=struct.pack('!BBHHHBBH4s4s',ip_hl_ver,ip_tos,ip_lenth,ip_id,ip_flag,ip_ttl,ip_prot,ip_check,ip_src,ip_dest)


sock=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)



'''class IP (Structure):

	_fields_=[
		("version",c_ubyte,4),
		("hed_len",c_ubyte,4),
                ("tos",c_ubyte),
                ("len",c_ushort),
                ("id",c_ubyte),
                ("logs",c_ubyte),
		("ttl",c_ubyte),
		("proto",c_ubyte),
		("chk",c_ubyte),
                ("src",c_uint32),
                ("des",c_uint32)]

	def __new__(self, socket_buffer=None):
		return self.from_buffer_copy(socket_buffer)

	def __init__(self,socket_buffer=None):
		self.src1=socket.inet_ntoa(struct.pack("@I",self.src))
		self.des1=socket.inet_ntoa(struct.pack("@I",self.des))'''


TH=14
ETH_P=0x0800
try:
    	sock1=socket.socket(socket.AF_PACKET, socket.SOCK_RAW,socket.htons(ETH_P))
	sock1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
except socket.error , msg:
    	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    	sys.exit()

while True:
	sock.sendto(ip_header,(ip_dest,0))

	
 
		# receive a packet
	while True:
    		try:	
    			packet = sock1.recvfrom(65565)
    		except KeyboardInterrupt:
       			sys.exit()
	#sock1.bind(('enp0s3',0))
	#data=sock1.recvfrom(65565)[0]
	#if not data:
		#print "Request Time Out"	
	#else:
		#ip=IP(data[TH:])
	#packet string from tuple
    		packet = packet[0]
    #parse ethernet header     
    ethernet_header = packet[:14]
    ethernet_unpack = unpack('!6s6sH' , ethernet_header)
    ethernet_protocol = socket.ntohs(ethernet_unpack[2])
    
    
    #Parse IP packets, IP Protocol number = 8
    if ethernet_protocol == 8 :
        
        ip_header = packet[14:34]           
        ip_header_unpack = unpack('!BBHHHBBH4s4s' , ip_header) 
         
        ttl = ip_header_unpack[5]
        protocol = ip_header_unpack[6]
        s_addr = socket.inet_ntoa(ip_header_unpack[8]);
        
        
	if str(s_addr)==sys.argv[1]:
        	#ICMP Packets
        	if protocol == 1 :
            		u = iph_length + 14
            		icmph_length = 4
            		icmp_header = packet[u:u+4] 
            		icmph = unpack('!BBH' , icmp_header)             
            		icmp_type = icmph[0]
            		code = icmph[1]
            		checksum = icmph[2]

			if str(icmp_type)=="0":
				print "Reply from"+str(s_addr)+" ttl="+ttl "
            
	else:
		time.sleep(5)
		print "Request Time Out "
	
		
	


