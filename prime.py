def is_even(n):
    return (n & 1)==0
num = 101
if is_even(num):
    print(f"The {num} is even.")
else:
    print(f"The {num} is odd")