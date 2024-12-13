file=open('New Text Document.txt')
counter=0
content=file.read()
lis1=content.split("\n")
for i in lis1:
    if i:
        counter+=1

print("The number of lines in the file is", counter)
