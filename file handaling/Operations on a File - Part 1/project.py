
file = open("students.txt", "r") 
content = file.read() 
print("Current content of the file:")
print(content)  
file.close()  

file = open("students.txt", "w")  
brief_introduction = "Name: Roy\nClass: 8\nFavorite Subject: Math\n"
file.write(brief_introduction)  
print("\nFile has been overwritten with the new introduction.")
file.close()  

file = open("students.txt", "a")  
favorite_subject = "Additional Favorite Subject: Science\n"
file.write(favorite_subject)  
print("\nYour favorite subject has been added to the file.")
file.close()  