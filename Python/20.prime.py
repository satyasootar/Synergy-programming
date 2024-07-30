#WAP to check the number is prime or composite

num = int(input("Enter a number \n"))
i = 2
while(i < num):
    if(num % i == 0):
        print("Composite")
        break
    i = i+1      
else:
 print("Prime") 

                       
    
if(num == 2 or num == 1):
    print("prime")