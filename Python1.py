Total=0
input=0
while True:
    input=raw_input("Enter Your Number : ")
    if input=='':
        break
    elif input.isdigit()==True:
        i=int(input)
        Total+=i
print("The Total Is ",Total)