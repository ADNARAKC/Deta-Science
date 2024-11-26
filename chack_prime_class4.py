num=int(input("Enter the number you want to check: "))
prime= False
for i in range (2,num):
    if num%i==0:
        prime=False
        break
    else:
        prime=True
if prime:
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")