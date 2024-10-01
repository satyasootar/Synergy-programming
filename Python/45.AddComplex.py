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


# Input two complex numbers
real1 = float(input("Enter the real part of the first complex number: "))
imag1 = float(input("Enter the imaginary part of the first complex number: "))

real2 = float(input("Enter the real part of the second complex number: "))
imag2 = float(input("Enter the imaginary part of the second complex number: "))

# Create complex number objects
num1 = ComplexNumber(real1, imag1)
num2 = ComplexNumber(real2, imag2)

# Add the two complex numbers
result = num1.add(num2)

# Display the result
print("The sum of the complex numbers is:")
result.display()