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
sock = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
sock2 = socket.socket(socket.AF_PACKET,socket.SOCK_RAW, socket.htons(0x0800))
sock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.settimeout(5)
sock2.settimeout(5)
x=0
s=0
l=0
ip_dest=sys.argv[1]
print ("PING %s (%s) 56(84) bytes of data."%(ip_dest,ip_dest))
try:
	beg_time=time.time()
	while x<4:
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
			packet2, addr2=sock2.recvfrom(1024)
		except socket.timeout:
			print "Requested Time Out"
			x+=1			
			continue

		#print packet
		#print packet2

		ip_header = packet2[14:34]
       		ip_header_unpack =unpack('!BBHHHBBH4s4s'  , ip_header) 

    	
		icmp_header = packet[20:28] 
		icmph =unpack('!BBHHH' , icmp_header)             

		ttl = ip_header_unpack[5]
		protocol = ip_header_unpack[6]
      		s_addr = socket.inet_ntoa(ip_header_unpack[8]);
        
        	icmp_type = icmph[0]
        	code = icmph[1]
        	
		r_time=round(((recv_time-send_time)*1000),3)
		
		if s_addr==sys.argv[1]:
	
			if icmp_type==0:
				print str(len(packet2))+" bytes from "+str(s_addr)+": icmp_seq="+str(x)+" ttl="+str(ttl)+" time="+str(r_time)+" ms"
				time.sleep(1)
				s+=1
				
				
	
		elif icmp_type==3:
			if code==1:
				print ip_d+" Destination Unrechable !"
				
				
			
			
	
	l=((x-s)/x)*100
	end_time=time.time()
	tot_time=round(((end_time-beg_time)*1000),2)
	print ("--- %s Ping Statistics ---"%(ip_dest))
	print ("%s packets Transmited   %s packets recieved %s%% packet loss, time %s ms"%(x ,s,l,tot_time))
	sys.exit()	

except KeyboardInterrupt:
	l=((x-s)/x)*100
	end_time=time.time()
	tot_time=round(((end_time-beg_time)*1000),2)
	print ("--- %s Ping Statistics ---"%(ip_dest))
	print ("%s packets Transmited   %s packets recieved %s%% packet loss, time %s ms"%(x ,s,l,tot_time))
	sys.exit()       
	
		
	


