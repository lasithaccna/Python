import socket,struct
from ctypes import *

class IP (Structure):

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
		self.des1=socket.inet_ntoa(struct.pack("@I",self.des))


TH=14
ETH_P=0x0800

sock=socket.socket(socket.AF_PACKET, socket.SOCK_RAW,socket.htons(ETH_P))
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(('enp0s3',0))


while True:
	data=sock.recvfrom(65565)[0]
	ip=IP(data[TH:])
	print (ip.version)
	print (ip.hed_len)
	print (ip.tos)
	print (ip.len)
	print (ip.id)
        print (ip.logs)
        print (ip.ttl)
        print (ip.proto)
	print (ip.chk)
        print (ip.src1)
        print (ip.des1)


