#WAP a program to find the first n prime number

def is_prime(num):
   
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

n = int(input("Enter the number of prime numbers to find: "))

print(f"The first {n} prime numbers are: {first_n_primes(n)}")


# Output
# Enter the number of prime numbers to find: 10
# The first 10 prime numbers are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]