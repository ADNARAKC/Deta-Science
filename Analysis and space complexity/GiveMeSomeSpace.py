def sum(n):
    return n*(n+2)/2
print(sum(4))
def arraysum(a):
    sum=0
    for i in a:
        sum+=i
    return sum
a=[12,3,4,15]
print(arraysum(a))
def sumn(n):
    if(n<=0):
        return 0 
    return n + sumn(n-1)
print(sumn(2))