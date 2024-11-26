#First of all, take two numbers from the user, store them in variables x and y, respectively. Write a Python program to swap the values present inside x and y and display the results.
num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))

n1=num1
n2=num2

num2=n1
num1=n2

print("The value of num1 when swapped is", num1)
print("The value of num2 when swapped is", num2)