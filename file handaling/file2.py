file=open('New Text Document.txt')
print("File in read mode-",file.read())
file.close()

fil1=open('New Text Document.txt','w')
fil1.write("Codingal")
fil1.write("My name is Adhrit Narayanan KC.")
fil1.close()

file=open('New Text Document.txt')
print("File in read mode-",file.read())
file.close()

file2=open('New Text Document.txt','a')
file2.write("I read in class IX")
file2.close()
file=open('New Text Document.txt')
print("File in read mode-",file.read())
file.close()