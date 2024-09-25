# Write a Python program that prints all the prime numbers between 1 and 100.

import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Run the prime checker for numbers starting from 2
for num in range(2, 101):
    if isPrime(num):
        print(num)