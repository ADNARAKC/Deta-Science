def a1(n):
    return n*(n+1)/2
print(a1(4))



def a2(n):
    sum=0
    for i in range(1,n+1):
        sum = sum+i
    return sum
print(a2(4))


def a3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum = sum+1
    return sum
print(a3(4))