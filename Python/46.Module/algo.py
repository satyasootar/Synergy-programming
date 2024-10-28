#WAP to create a module and import it to the test file and access it's functionality.

import random

PI = 3.14

def squareArea(s):
    return s*s

def squarePerimeter(s):
    return 4*s

def squareVolume(s):
    return s*s*s

def rectangleArea(l, b):
    return l*b

def rectanglePerimeter(l, b):
    return 2(l+b)

def rectangleVolume(l , b, h):
    return l*b*h

def factorial(n):
    f = 1;
    while n > 0:
        f = f* n
        n = n-1
    return f    


def circleArea(radius):
    return PI * radius * radius


def circlePerimeter(radius):
    return 2 * PI * radius

def cylinderVolume(radius, height):
    return circleArea(radius) * height

def triangleArea(base, height):
    return 0.5 * base * height


def trianglePerimeter(side):
    return 3 * side

def randomNumber(min_value, max_value):
    return random.randint(min_value, max_value)


def power(base, exponent):
    return base ** exponent


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class Car:
    name = "none"
    color = "None"
    milage = 0
    topSpeed = 0
    
    def __init__(self,Name ,color, milage , speed ):
        self.name = Name
        self.color = color
        self.milage = milage
        self.topspeed = speed
    
    def build(self):
        print("Congratulation your car is ready\n")
        print(f"The name of your car is {self.name}. The color is {self.color}. It has a milage of {self.milage}. It can go upto {self.topspeed}km/h")
        
    