num=int(input("Enter the number of rown you want: "))
for i in range(1,num+1):
    for j in range(i):
        print("*",end=" ")
    print()