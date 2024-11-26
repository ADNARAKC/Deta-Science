import random
num=int(input("Guss a number from 1 to 10: "))
compt=random.randint(1,10)
if num==compt:
    print("WOW! you have gussed the correct number")
else:
    print("Opps! you are wrong")