from math import sqrt
num=int(input("Enter the number to check: "))
print(f"The number is {num}")
if num>1:
    if num==2:
        print(f"{num} is prime number.")
    else:
        for i in range (2,int(sqrt(num))+1):
            if (num%i==0):
                print(f"{num} is not a prme number.")
                break
            else:
                print(f"{num} is a prime number.")
else:
        print(f"{num} is not a prime number.")
