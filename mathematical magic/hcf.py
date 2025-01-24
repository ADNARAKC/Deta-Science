numLarge=int(input("Enter the large number: "))
numSmall=int(input("Enter the small number: "))
while(numSmall):
    numstore=numSmall
    numSmall=numLarge%numSmall
    numLarge=numstore
print(f"HCF is {numLarge}")