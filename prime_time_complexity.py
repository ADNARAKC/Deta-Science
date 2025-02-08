num = int(input("Enter a number: "))
def is_prime_slow(number):
    if number <= 1:
        return False  
    for i in range(2, number):  
        print(f"Checking divisibility by {i}:") 
        remainder = number % i  
        print(f"{number} divided by {i} has a remainder of {remainder}")
        if remainder == 0:  
            print(f"{number} is divisible by {i}, therefore not prime.")
            return False  

    print(f"{number} is not divisible by any number up to {number - 1}, so it's prime.")
    return True 

if is_prime_slow(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
"""This is a python project to check weather a given number is prime or not.
 This program is made to be slow and take a long time, especially if you give it a big number.
  It's like a person trying to find a specific grain of sand on a whole beach"""

"""How it works--- The program divides the number by every number starting from 
2 up to one less than your number.  It's like checking if your number can be evenly split into
 groups of 2, groups of 3, groups of 4, and so on."""

import math
num = int(input("Enter a number: "))

def is_prime_fast(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6  
    return True
if is_prime_fast(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

"""This code quickly checks if a number is prime. It first handles small numbers (0, 1, 2, 3).
 Then, it checks if the number is divisible by 2 or 3.  
 The clever part is that it only checks divisibility by numbers up to the square root of the input number, 
 skipping many unnecessary checks. This makes it much faster, especially for large numbers.
 Finally, it tells you if the number is prime or not."""



