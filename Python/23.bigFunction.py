#WAP to perform area of a square, area of a rectangle, volume of a cube, prime or composite , even or odd using function, call according to your choice.

def squareArea(a):
    return a * a    #function to get the area of a square

def rectArea(a, b):  #function to get the area of a rectangle
    return a * b

def volCube(a, b, c):  #Function to get the Volume of the cude
    return a * b * c

def isPrime(n):  # Function to check if a number is prime or composite
    if n <= 1:
        return "Composite"
    for i in range(2, int(n/2) + 1):  # Loop to check for divisors
        if n % i == 0:
            return "Composite"
    return "Prime"

def evenOdd(n):  # Function to check if a number is even or odd
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Choices \n 1. Area of a square \n 2. Area of a Rectangle \n 3. Volume of a Cube \n 4. Prime or Composite \n 5. Even or Odd \n")

n = int(input("Enter your choice: "))

if n == 1:
    s = int(input("Enter side: "))
    print("Area of a square =", squareArea(s))
    
elif n == 2:
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    print("Area of a rectangle =", rectArea(l, b))
    
elif n == 3:
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: ")) 
    h = int(input("Enter height: "))
    print("Volume of a cube =", volCube(l, b, h)) 

elif n == 4:  # Added condition for prime/composite check
    num = int(input("Enter a number: "))
    print("The number is", isPrime(num))
    
elif n == 5:  # Added condition for even/odd check
    num = int(input("Enter a number: "))
    print("The number is", evenOdd(num))
    
else:
    print("Invalid choice!")
                        

# Choices 
#  1. Area of a square 
#  2. Area of a Rectangle 
#  3. Volume of a Cube 
#  4. Prime or Composite 
#  5. Even or Odd 

# Enter your choice: 1
# Enter side: 2
# Area of a square = 4
