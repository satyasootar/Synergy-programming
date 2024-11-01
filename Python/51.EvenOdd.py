#WAP to create a file name number.txt containing 50 intigers, Separate all the even and odd into two different files.

P = open("number.txt", "a")

n = int(input("Please enter the number of values"))

for i in range (n):
    P.write(str(i)+", ")

P.close()    


P = open("number.txt", "r")
value = P.read()

P.close()
numArr = value.split(",")
numArr.pop()
Even = []
Odd = []

for i in range (len(numArr)):
    if(int(numArr[i]) % 2 == 0):
        Even.append(int(numArr[i]))
    else:
        Odd.append(int(numArr[i]))    

   
P = open("Even.txt", "w")
P.write(str(Even))
P.close()

P = open("Odd.txt", "w")
P.write(str(Odd))
P.close()

    
    
    
    


