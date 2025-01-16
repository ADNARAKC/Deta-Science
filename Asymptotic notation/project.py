def constant_time_example():
    print("This function runs in constant time.")

def linear_time_example(n):
    for i in range(n):
        print(i)  

def quadratic_time_example(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

def logarithmic_time_example(n):
    i = 1
    while i < n:
        print(i)  
        i *= 2
def exponential_time_example(n):
    if n <= 0:
        return
    print(n)
    exponential_time_example(n - 1)  
n = 5
print("O(1) Example:")
constant_time_example()

print("\nO(n) Example:")
linear_time_example(n)

print("\nO(n^2) Example:")
quadratic_time_example(n)

print("\nO(log n) Example:")
logarithmic_time_example(n)

print("\nO(2^n) Example:")
exponential_time_example(n)