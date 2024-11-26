value=int(input("Enter the value to find the factorial: "))
def factorial(val):
    if val==1:
        return 1
    else:
        return val*factorial(val-1)
print(f"The factorial of the number is= {factorial(value)}")