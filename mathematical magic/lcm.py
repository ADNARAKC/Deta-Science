numLarge=int(input("Enter the large number: "))
numSmall=int(input("Enter the small number: "))
num1=numLarge
num2=numSmall
while(numSmall):
    numstore=numSmall
    numSmall=numLarge%numSmall
    numLarge=numstore
print(f"HCF is {numLarge}")

lcm=num1*num2/numLarge
print(f"The Lcm is {lcm}")