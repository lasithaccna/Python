from ctypes import *
from struct import *
import socket,time,sys,os

def checksum(source_string):
    sum = 0
    countTo = (len(source_string)/2)*2
    count = 0
    while count<countTo:
        thisVal = ord(source_string[count + 1])*256 + ord(source_string[count])
        sum = sum + thisVal
        sum = sum & 0xffffffff
        count = count + 2
    if countTo<len(source_string):
        sum = sum + ord(source_string[len(source_string) - 1])
        sum = sum & 0xffffffff
    sum = (sum >> 16)  +  (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


TH=14
ETH_P=0x0800
x=1
ip_dest=sys.argv[1]

try:
	beg_time=time.time()
	while x<30:
		
		sock =socket.socket(socket.AF_INET, socket.SOCK_RAW ,1)
		sock.setsockopt(socket.SOL_IP, socket.IP_TTL,x)
		sock.settimeout(5)
		x+=1
		ip_d=ip_dest
		i_type=8
		i_code=0
		i_checksum=0
		i_id=1
		i_seq=x
		

		i_header1=pack('!BBHHH',i_type,i_code,i_checksum,i_id,i_seq)
		f_packet=i_header1
		i_checksum=checksum(f_packet)
		i_header2=pack('!BBHHH',i_type,i_code,i_checksum,i_id,i_seq)
		send_time=time.time()
	
 		sock.sendto(i_header2 ,(ip_d,1))
	

		try:
			packet ,addr= sock.recvfrom(1024)
			recv_time=time.time()
			host_add=addr[0]
		except socket.timeout:
			print "Requested Time Out"
			x+=1
			continue

		#print packet
		#print packet2
		
		
		ip_header = packet[:20]
       		ip_header_unpack =unpack('!BBHHHBBH4s4s'  , ip_header) 

    	
		icmp_header = packet[20:28] 
		icmph =unpack('!BBHHH' , icmp_header)             

		ttl = ip_header_unpack[5]
		protocol = ip_header_unpack[6]
      		s_addr = socket.inet_ntoa(ip_header_unpack[8]);
        
        	icmp_type = icmph[0]
        	code = icmph[1]
        	
		r_time=round(((recv_time-send_time)*1000),3)
		
		try :
			c_name=socket.gethostbyaddr(host_add)[0]
		except socket.error:	
			c_name=host_add			
	        sys.stdout.write("%s  (%s ms)  " % (c_name ,r_time))
		sock.close
		if host_add==ip_dest :
			print (host_add)
			sys.exit()	
		
		x+=1	

except KeyboardInterrupt:
	sys.exit()       
	
		
	


