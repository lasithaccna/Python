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



x=1
ip_dest=sys.argv[1]
try :
	d_name=socket.gethostbyaddr(ip_dest)[0]
	
except socket.gaierror:
	print "Invalid address !"
	sys.exit()
except socket.herror:
	print "Unreachable Address ! \n"
	d_name=ip_dest
	pass
print "Traceroute to "+str(ip_dest)+" "+str(d_name)+" 30 hops max"

try:
	
	while x<30:
		
		sock =socket.socket(socket.AF_INET, socket.SOCK_RAW ,1)
		sock.setsockopt(socket.SOL_IP, socket.IP_TTL,x)
		sock.settimeout(5)
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
			r_time=round(((recv_time-send_time)*1000),3)
			try :
				c_name=socket.gethostbyaddr(host_add)[0]
			except socket.error:	
				c_name=host_add		
			print str(x)+"  "+str(c_name)+" ("+str(host_add)+") "+str(r_time)+"ms"
			sock.close
			if c_name == d_name or addr[0] == d_name :
				sys.exit()
		except KeyboardInterrupt:
			sys.exit()			
		except socket.timeout :
			print "*   "
		x+=1	

except KeyboardInterrupt:
	sys.exit()       
	
		
	


