#WAP to perform area of a square, area of a rectangle, volume of a cube, prime or composite , even or odd using function, call according to your choice.

def squareArea(a):
    return a*a
def rectArea(a,b):
    return a*b;
def volCube(a , b , c):
    return a*b*c
def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while(i <= n/2):
        if n % i == 0:
            print("Composite")
            break
        i = i+1
        if i >n/2:
            print("prime")
def evenOdd(n):
    if n% 2 ==0:
        print("even")
    else:
        print("odd")
        
                       
print("Choices \n  1. Area of a square \n 2. Area of a Rectangle \n 3.volume of a cube \n 4.prime Number \n 5. Even or Odd \n")

n = int(input("Enter your choices"))
if n == 1:
    s = int(input("Enter sides"))
    print("area of a square =" , squareArea(s))
    
elif n==2:
    l= int(input("Enter length:"))
    b =int(input("Enter  Breadth :"))
    print("Area of a rectangle = ", rectArea(l,b))
    
elif n == 3:
        l= int(input("Enter length:"))
        b =int(input("Enter  Breadth :")) 
        h= int(input("Enter Height :"))
        print("volume of a cube=", volCube(l ,b,h))                 

