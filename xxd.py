import sys
import os.path
	
#define the xxd Function
def xxd(file_path):
	f=open(file_path,'r')
	lines=0
	while True:
		#read First 16 Charactors
		r=f.read(16)
		x=r
		if not r:
			break
		y=[]
		#get first charactor and convert to ascii
		for i in r:
			y.append('%02x'%ord(i))
		w=[]
		#Set Two sequence Ascii Values In To One
		for z in range(0,len(y),2):
			w.append(''.join((y[z:z+2])))
		ch=[]
		#Find The Undefined Charactors And Replace them with "."
		for c in x:
			undef=ord(c)
			if undef<32 or undef>127:
				ch.append('.')
			else:
				ch.append(c)
	
		#Cover Raw Number to hexca
		raws=('%07x'%(lines*16))
		print('{0}: {1:<39} {2}'.format(raws,' '.join(w),''.join(ch)))
		lines=lines+1
	
	
xxd(sys.argv[1])

