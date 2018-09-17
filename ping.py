from  ctypes import *
import struct,sys,os
import socket,time


sock=socket.socket(socket.AF_INET,socket.SOCK_RAW,1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

def checksum(source_string):
    
    sum = 0
    count_to = (len(source_string) / 2) * 2
    for count in xrange(0, count_to, 2):
        this = ord(source_string[count + 1]) * 256 + ord(source_string[count])
        sum = sum + this
        sum = sum & 0xffffffff

    if count_to < len(source_string):
        sum = sum + ord(source_string[len(source_string) - 1])
        sum = sum & 0xffffffff  

    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff

    answer = answer >> 8 | (answer << 8 & 0xff00)

    return answer

TH=14
ETH_P=0x0800
sock1=socket.socket(socket.AF_PACKET, socket.SOCK_RAW,socket.htons(ETH_P))
sock1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ip_dest=sys.argv[1]
x=1
while x<2:
	ip_d=ip_dest
	ip_src=socket.inet_aton(socket.gethostbyname(socket.gethostname()))
	i_type=8
	i_code=0
	i_checksum=0
	i_id=124
	i_seq=x

	i_header1=struct.pack('!BBHHH',i_type,i_code,i_checksum,i_id,i_seq)
	i_checksum=checksum(i_header1)
	i_header2=struct.pack('!BBHHH',i_type,i_code,i_checksum,i_id,i_seq)
	i_packet=i_header2
	sock.sendto(i_packet,(ip_d,1))

	packet = sock.recvfrom(1024)
    	packet = packet[0]
   	     
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
            				
          	  			icmp_header = packet[20:28] 
          	 	 		icmph = unpack('!BBH' , icmp_header)             
          	 	 		icmp_type = icmph[0]
          	  			code = icmph[1]
         		   		checksum = icmph[2]

					if str(icmp_type)=="0":
						print "Reply from"+str(s_addr)+" ttl="+ttl
            
		        
	
		
	


