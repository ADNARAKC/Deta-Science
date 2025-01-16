def sum_of_numbers(numbers):
    total = 0        
    for num in numbers:  
        total += num
    return total

def main():
    numbers = [1, 2, 3, 4, 5]  
    print(f"Sum of numbers: {sum_of_numbers(numbers)}")

main()
