# WAP to print the Greatest among three number using nestwd if...else statement



x = int(input("Enter the 1st number \n"))
y = int(input("Enter the 2nd number \n"))
z = int(input("Enter the 3rd numbr \n"))
if(x > y):
    if(x > z):
        print("Greatest is =", x)
    else:
        print("Greatest is =", z)
else:
    if(y > z):
        print("Greatest is =", y)
    else:
        print("Greatest is =", z)         
