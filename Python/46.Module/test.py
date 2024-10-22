import algo
from algo import Car

num = int(input("Enter a number: "))

print(f"The area of a square is {algo.squareArea(num)}")
print(f"The Perimeter of a square is {algo.squarePerimeter(num)}")
print(f"The Volume of a square is {algo.squareVolume(num)}")


print(f"Factorial {algo.factorial(num)}")


myCar = Car("Maruti", "Blue", 100, 250)
myCar.build()

# Output
# Enter a number: 3
# The area of a square is 9
# The Perimeter of a square is 12
# The Volume of a square is 27
# Factorial 6
# Congratulation your car is ready

# The name of your car is Maruti. The color is Blue. It has a milage of 100. It can go upto 250km/h