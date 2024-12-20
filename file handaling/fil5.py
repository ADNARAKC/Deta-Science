file1=open('New Text Document.txt','w')

file2=open('text2.txt')

file1.write(file2.read())

file1.close()
file1=open("New Text Document.txt",'r')
print(file1.read())
print("The content of file2:-",file2.read())

file2.close()
file1.close()