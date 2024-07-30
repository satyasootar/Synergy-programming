# Write a program to enter your name , 5 differentvmarks . Print the percentage and grade with Name

name = input("Enter you Name \n")
m = int(input("Enter the Math mark \n"))
p = int(input("Enter the Physics mark \n"))
e = int(input("Enter the English mark \n"))
c = int(input("Enter the Chemistry mark \n"))
b = int(input("Enter the Biology mark \n"))

sm = m + p + e + c + b
per = (sm/500)* 100
print("Name =", name)
print("Percentage = ", per)

if(per>= 90):
    print("Grade = o")   

elif(per>= 80):
    print("Grade = E")

elif(per>= 70):
    print("Grade = A")

elif(per>= 60):
    print("Grade = B")
    
else:
    print("Grade = F")            