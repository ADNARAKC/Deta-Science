num = int(input("Enter the number to check: "))
def check_if(num):
    if num <= 0:
        return False
    while num %2 ==0:
        num = num//2
    return num==1

if check_if(num):
    print(f"{num} is a power of 2")
else: 
    print(f"{num} is not a power of 2")