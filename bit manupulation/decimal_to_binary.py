decimal = int(input("Enter a decimal number: "))

def to_binary(decimal):
    binary=''
    
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder)+ binary

        decimal = decimal // 2
        
    return binary
print(f"The binary form is {to_binary(decimal)}")