num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
value=int(input("Enter what you want to do.\n 1)Add\n 2)Subtract\n 3)Divide\n 4)Multiplication\n Enter: "))
def add(n1,n2):
    return (n1+n2)
def sub(n1,n2):
    return (n1-n2)
def div(n1,n2):
    return (n1/n2)
def multi(n1,n2):
    return (n1*n2)

if value==1:
    print(add(num1,num2))
elif value==2:
    print(sub(num,num2))
elif value==3:
    print(div(num1,num2))
elif value==4:
    print(multi(num1,num2))
else:
    print("Invalid Input.")