a=int(input("Enter first number: "))

b=int(input("Enter second number: "))

flips = 0

x= a^b
while x:
    flips += x&1
    x>>=1

print("Minimum flips are", flips)