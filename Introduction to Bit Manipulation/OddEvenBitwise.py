def isEvenOdd(n):
    if (n^1 == n+1):
        return True;
    else:
        return False;

number=int(input("Enter the number: "))

if isEvenOdd(number):
    print("Number is Even")
else:
    print("Number is Odd.")