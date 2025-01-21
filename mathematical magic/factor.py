num=int(input("Enter the number: "))
factorial=1
for i in range(1,num+1):
    if num % i == 0:
        print(f"The factors are {i}")