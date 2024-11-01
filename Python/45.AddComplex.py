#WAP to add two complex number using class

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

    def display(self):
        print(f"{self.real} + {self.imag}i")


real1 = float(input("Enter the real part of the first complex number: "))
imag1 = float(input("Enter the imaginary part of the first complex number: "))

real2 = float(input("Enter the real part of the second complex number: "))
imag2 = float(input("Enter the imaginary part of the second complex number: "))


num1 = ComplexNumber(real1, imag1)
num2 = ComplexNumber(real2, imag2)


result = num1.add(num2)

print("The sum of the complex numbers is:")
result.display()

# Output 
# Enter the real part of the first complex number: 4
# Enter the imaginary part of the first complex number: 21
# Enter the real part of the second complex number: 32
# Enter the imaginary part of the second complex number: 123
# The sum of the complex numbers is:
# 36.0 + 144.0i





#  Info - * Code number 46 is at the top of the repository. It's a Folder *