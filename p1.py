
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

a = a + b + c  
b = a - (b + c)  
c = a - (b + c)  
a = a - (b + c)  

print(f"After swapping: a = {a}, b = {b}, c = {c}")
