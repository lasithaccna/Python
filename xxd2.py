f=open('l.txt','r')

s=0
while True:
	r=f.read(16)
	if not r:
		break
	he=[]
	
	for i in r:
		he.append('%02x'%ord(i))
		
	step=('%07x'%(s*16))
	print('{0} :'.format(step),he)
	s=s+1