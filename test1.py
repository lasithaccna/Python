from ctypes import *
import struct
import socket

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
ip_src=socket.inet_aton('192.168.1.1')
ip_dest=socket.inet_aton('192.168.1.100')

ip_header=struct.pack('!BBHHHBBH4s4s',ip_hl_ver,ip_tos,ip_lenth,ip_id,ip_flag,ip_ttl,ip_prot,ip_check,ip_src,ip_dest)

print (ip_header)

print(len(ip_header))
