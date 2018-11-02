import socket, sys
from struct import *
 
#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b
 

try:
    s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0800))
except socket.error , msg:
    print 'Socket could not be created'
    sys.exit()
packet_number=1 
# receive a packet
while True:

    print "\nPacket Number"+str(packet_number)
    try:
        receive_packet = s.recvfrom(65565)
        packet = receive_packet[0] 
    except KeyboardInterrupt:
        sys.exit()

    #Unpacked Ethernet Header 
    ethernet_header = packet[:14]
    ethernet_unpack = unpack('!6s6sH' , ethernet_header)
    ethernet_protocol = socket.ntohs(ethernet_unpack[2])
    ethernet_src=eth_addr(packet[6:12])
    ethernet_dst=eth_addr(packet[0:6])
    print "Ethernet Header Is \n"
    print 'Destination MAC : ' + ethernet_dst + '\nSource MAC : ' + ethernet_src + '\nProtocol : ' + str(ethernet_protocol)
    
    



    #IP Protocol number = 8
    if ethernet_protocol == 8 :       
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
        print "\nThis Is an IP Packet \n"
        print 'Version : ' + str(version) + '\nIP Header Length : ' + str(ihl) + '\nTTL : ' + str(ttl) + '\nProtocol : ' + str(protocol) + '\nSource Address : ' + str(src_addr) + '\nDestination Address : ' + str(dst_addr)
        



        #TCP protocol = 6
        if protocol == 6 :
            t = iph_length + 14
            tcp_header = packet[t:t+20]
            tcp_header_unpack = unpack('!HHLLBBHHH' , tcp_header)             
            source_port = tcp_header_unpack[0]
            dest_port = tcp_header_unpack[1]
            sequence = tcp_header_unpack[2]
            acknowledgement = tcp_header_unpack[3]            
            tcph_length = tcp_header_unpack[4] >> 4
            print "\nTCP Header Is \n" 
            print 'Source Port : ' + str(source_port) + '\nDest Port : ' + str(dest_port) + '\nSequence Number : ' + str(sequence) + '\nAcknowledgement : ' + str(acknowledgement) + '\nTCP header length : ' + str(tcph_length)
            
            h_size = 14 + iph_length + tcph_length * 4
            data_size = len(packet) - h_size 
            data = packet[h_size:]             
            print 'Data : ' + data



 
        #ICMP protocol = 1
        elif protocol == 1 :
            u = iph_length + 14
            icmph_length = 4
            icmp_header = packet[u:u+4] 
            icmp_header_unpack = unpack('!BBH' , icmp_header)             
            icmp_type = icmp_header_unpack[0]
            code = icmp_header_unpack[1]
            checksum = icmp_header_unpack[2]
            print "\nICMP Header Is  \n"  
            print 'Type : ' + str(icmp_type) + '\nCode : ' + str(code) + '\nChecksum : ' + str(checksum)
              
            h_size = 14 + iph_length + icmph_length
            data_size = len(packet) - h_size             
            data = packet[h_size:]             
            print 'Data : ' + data



 
        #UDP protocol = 17
        elif protocol == 17 :
            u = iph_length + 14
            udph_length = 8
            udp_header = packet[u:u+8]            
            udph = unpack('!HHHH' , udp_header)             
            source_port = udph[0]
            dest_port = udph[1]
            length = udph[2]
            checksum = udph[3]
            print "\nUDP Header Is  \n"  
            print 'Source Port : ' + str(source_port) + '\nDest Port : ' + str(dest_port) + '\nLength : ' + str(length) + '\nChecksum : ' + str(checksum)
              
            h_size = 14 + iph_length + udph_length
            data_size = len(packet) - h_size 
            data = packet[h_size:]             
            print 'Data : ' + data

 
        #some other IP packet like IGMP
        else :
            print 'Protocol other than TCP/UDP/ICMP'
	packet_number+=1
