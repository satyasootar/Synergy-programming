#WAP to print all the even number & Odd number from  the list using filter

def Even(n):
    return n%2==0

def Odd(n):
    return n%2==1

A = [1,2,3,4,5,6,7,8,9,0,23,34,12,53,65]

El = list(filter(Even, A))
Ol = list(filter(Odd, A))

print("Even no: ",El)
print("Odd no: ",Ol)

# Output
# Even no:  [2, 4, 6, 8, 0, 34, 12]
# Odd no:  [1, 3, 5, 7, 9, 23, 53, 65]