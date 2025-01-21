num=int(input("Enter the number: "))
digits = len(str(num))
resultnum=0
temp=num
while temp>0:
    digit=temp%10
    resultnum += digit**digits
    temp //=10
if num == resultnum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")