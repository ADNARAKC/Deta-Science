file1=input("Enter the name of the first file: ")
file2=input("Enter the name of the secong file: ")

f1=open(file1,'r')
f2=open(file2,'r')

print("The content of file1 before append method:",f1.read())
print("The content of file2 before append method:",f2.read())

f1.close()
f2.close()

f1a=open(file1,'a')
f2a=open(file2,'r')

f1a.write(f2a.read())
f1a.seek(0)
f2a.seek(0)
f1a.close()
f1a=open(file1)
print("The content of file 1 after appending",f1a.read())
print("The content of file 2 after appending",f2a.read())

f1a.close()
f2a.close()