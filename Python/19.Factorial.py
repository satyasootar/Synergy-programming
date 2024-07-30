# WAP to print the factorial of a number

num = int(input("Enter a number \n"))
i = 1
fact = 1
while(i <= num):
    fact = fact * i
    i =  i +1
    
print("The factorial of" , num ," =" ,fact)    
    