binary = input("Enter a binary number: ")
def to_decimal(binary):
    decimal = 0
    i = 0
    for digit in reversed(binary):
        if digit == '1':
            decimal += 2 ** i
        i += 1
    return decimal
print(f"The decimal is equvalent to { to_decimal(binary)}")