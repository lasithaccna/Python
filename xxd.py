import os

f=open('l.txt','r')

x = os.fstat(f.fileno()).st_size

s=0
y=[]
z=x/16
w=x%16

for c in f:
		y.append(c)

if  w!=0:
	z+=1
	for l in range (1, int(z), 1):
		if  z<1:
			s=w
			for i in range (0, s, 1):
				print(y)
			print("\n")
		else:
			
			for i in range (s, s+15, 1):
				print(y[i])
			print("\n")
			s+=16
		

