file = open("students.txt", "r")
content = file.read()  
print("Complete content of the file:")
print(content)  
file.close()  

file = open("students.txt", "r")  
first_ten_characters = file.read(10) 
print("\nFirst 10 characters of the file:")
print(first_ten_characters)  
file.close() 

file = open("students.txt", "r") 
first_line = file.readline() 
print("\nFirst line of the file:")
print(first_line) 
file.close()  

file = open("students.txt", "r") 
print("\nFirst four lines of the file:")
for _ in range(4):
    print(file.readline(), end="")  
file.close() 

file = open("students.txt", "r") 
print("\nAll lines of the file:")
for line in file: 
    print(line, end="")  
file.close()  