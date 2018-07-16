Total=0

while True:

	x=input("Enter number here :")

	if x=='':

		break
    
	try:
		Total=Total+int(x)

	except ValueError:
		continue

print("The Total Is ",Total)