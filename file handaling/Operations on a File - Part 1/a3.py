file1=open('code.txt.txt','r')
file3=open('b.txt','w')
for line in file1.readlines():
    if not(line.startswith('Coding')):
        print(line)
        file3.write(line)

file1.close()
file3.close()