#WAP to access Roll & name of 10 students and store them in the dictionary having roll number is the key & name is the value

d ={}
n = int(input("For how many students: "))
for i in range(n):
    nm = input("Enter the name: ")
    Roll = input("Enter Roll: ")
    d[Roll] = nm
for k,v in d.items():
    print(k," ",v)    
        
#        Output
#        For how many students: 3
#        Enter the name: Rama
#        Enter Roll: 1
#        Enter the name: Sama
#        Enter Roll: 2
#        Enter the name: Rani
#        Enter Roll: 3
#        1   Rama
#        2   Sama
#        3   Rani 