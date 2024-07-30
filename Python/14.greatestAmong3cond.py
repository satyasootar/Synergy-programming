x = int(input("Enter the 1st numbr"))
y = int(input("Enter the 2nd numbr"))
z = int(input("Enter the 3rd numbr"))

G = x if x>y and x>z else y if y>z else z
print("The Greatest is =", G)