def num(n):
    iterations=0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end=" ")
            iterations+=1
        print("")
    print(f"When n is {n} the iterations is {iterations}")
num(5)
num(4)
num(3)
print("With every 'n' the time taken equals n^2")
print("O(n^2)")