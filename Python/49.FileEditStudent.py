#WAP to access the name , branch & age of 4 students and write them into the file named "student.txt" & display them.


P = open("student.txt", "a")
n = int(input("Enter number of Students: "))

for i in range (n):
    nm = input("Enter the name: ")
    br = input("Enter the branch: ")
    age = int(input("Enter the age: "))
    
    P.write("Name: "+ nm+"\n")
    P.write("Branch: "+br+"\n")
    P.write("Age: "+str(age)+"\n\n")
    
P.close()
P = open("student.txt", "r")
print(P.read())
P.close()


# OUTPUT
# Enter number of Students: 4
# Enter the name: Satya
# Enter the branch: CSE
# Enter the age: 19
# Enter the name: Rahul
# Enter the branch: Civil
# Enter the age: 20
# Enter the name: Soumya
# Enter the branch: EE
# Enter the age: 20
# Enter the name: Jagdish
# Enter the branch: Mech
# Enter the age: 19
# Name: Satya
# Branch: CSE
# Age: 19

# Name: Rahul
# Branch: Civil
# Age: 20

# Name: Soumya
# Branch: EE
# Age: 20

# Name: Jagdish
# Branch: Mech
# Age: 19