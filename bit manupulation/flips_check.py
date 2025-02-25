a=int(input("Enter first number: "))

b=int(input("Enter second number: "))

flips = 0

x= a^b
while x:
    flips += x&1
    x>>=1

print("Minimum flips are", flips)

Write a program to clear (set to 0) the nth bit of a number.

Example: Clear the 1st bit of 7 (binary 111) to get 5 (binary 101).

