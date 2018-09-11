from  ctypes import *
import struct,sys
import socket,time


sock=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

TH=14
ETH_P=0x0800
try:
    	sock1=socket.socket(socket.AF_PACKET, socket.SOCK_RAW,socket.htons(ETH_P))
	sock1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
except socket.error , msg:
    	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    	sys.exit()
x=1
while x<5:
	
	ip_src=socket.inet_aton(socket.gethostbyname(socket.gethostname()))
	ip_dest=sys.argv[1]
	i_type=8
	i_code=0
	i_checksum=0
	i_id=124
	i_seq=x

	i_header1=struct.pack('!BBHHH',i_type,i_code,i_checksum,i_id,i_seq)
	i_checksum=checksum(i_header1)
	i_header2=struct.pack('!BBHHH',i_type,i_code,i_checksum,i_id,i_seq)
	i_packet=i_header2
	sock.sendto(ip_packet,(ip_dest,0))
	# receive a packet
	
    	try:	
    		packet = sock1.recvfrom(65565)
    	except KeyboardInterrupt:
       		sys.exit()
	
    	packet = packet[0]
   	 #parse ethernet header     
	ethernet_header = packet[:14]
	ethernet_unpack = unpack('!6s6sH' , ethernet_header)
	ethernet_protocol = socket.ntohs(ethernet_unpack[2])
    
    
    
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
						print "Reply from"+str(s_addr)+" ttl="+ttl 
					elif str(icmp_code)==
            
		         else:
				time.sleep(5)
				print "Request Time Out "
	
		
	


